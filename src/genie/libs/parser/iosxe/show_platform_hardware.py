"""show_platform_hardware.py

    * 'show platform hardware qfp active feature appqoe stats all'
    * 'show platform hardware qfp active datapath utilization summary'
    * 'show platform hardware qfp active tcam resource-manager usage'
    * 'show platform hardware throughput crypto'
    * 'show platform hardware throughput crypto'
    * 'show platform hardware authentication status'
    * 'show platform hardware chassis fantray detail switch {mode}'
    * 'show platform hardware chassis power-supply detail switch {mode} all'
    * 'show platform hardware qfp active infrastructure bqs status | include QOS|QFP'
    * 'show platform hardware qfp active feature qos interface {interface} hierarchy detail | include subdev'
    * 'show platform hardware qfp active interface all statistics drop_summary'
    * 'show platform hardware qfp active infra punt stat type per | ex _0_'
    * 'show platform hardware qfp active datapath infra sw-cio'
    * 'show platform hardware qfp active datapath infra sw-nic'
    * 'show platform hardware qfp {status} statistics drop clear'
    * 'show platform hardware qfp {status} statistics drop | exclude _0_'
    * 'show platform hardware qfp active system state'
    * 'show platform hardware qfp active feature ipsec datapath drops all'
    * 'show platform hardware qfp active datapath pmd ifdev'
    * 'show platform hardware throughput level'
    * 'show platform hardware iomd <slot> qos port <no> ingress queue stats'
    * 'show platform hardware iomd switch <switch_no> <slot> qos port <no> ingress queue stats'
    * 'show platform hardware iomd <slot> portgroups'
    * 'show platform hardware iomd switch <switch_no> <slot> portgroups'
    * 'show platform hardware subslot {id} module interface {intf} status'
    * show platform hardware crypto-device utilization
    * show platform hardware qfp active classification feature tcam-usage
    * 'show platform hardware qfp {status} interface if-name {interface} path'
    * 'show platform hardware qfp {status} interface if-name {interface} path'

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


class ShowPlatformHardwareSchema(MetaParser):
    """Schema for show platform hardware qfp active infrastructure bqs queue output default all
    show platform hardware qfp active infrastructure bqs queue output default interface {interface}
    """

    schema = {
        Any(): {
            "if_h": int,
            Optional("index"): {
                Any(): {
                    "queue_id": str,
                    "name": str,
                    "software_control_info": {
                        "cache_queue_id": str,
                        "wred": str,
                        Optional("qlimit_bytes"): int,
                        Optional("qlimit_pkts"): int,
                        "parent_sid": str,
                        "debug_name": str,
                        "sw_flags": str,
                        "sw_state": str,
                        "port_uidb": int,
                        "orig_min": int,
                        "min": int,
                        "min_qos": int,
                        "min_dflt": int,
                        "orig_max": int,
                        "max": int,
                        "max_qos": int,
                        "max_dflt": int,
                        "share": int,
                        "plevel": int,
                        "priority": int,
                        Optional("defer_obj_refcnt"): int,
                        Optional("cp_ppe_addr"): str,
                    },
                    "statistics": {
                        "tail_drops_bytes": int,
                        "tail_drops_packets": int,
                        "total_enqs_bytes": int,
                        "total_enqs_packets": int,
                        Optional("queue_depth_bytes"): int,
                        Optional("queue_depth_pkts"): int,
                        Optional("lic_throughput_oversub_drops_bytes"): int,
                        Optional("lic_throughput_oversub_drops_packets"): int,
                    },
                },
            },
        },
    }


class ShowPlatformHardware(ShowPlatformHardwareSchema):
    """Parser for show platform hardware qfp active infrastructure bqs queue output default all
    show platform hardware qfp active infrastructure bqs queue output default interface {interface}
    """

    cli_command = [
        "show platform hardware qfp active infrastructure bqs queue output default all",
        "show platform hardware qfp active infrastructure bqs queue output default interface {interface}",
    ]

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Interface: GigabitEthernet1/0/7 QFP: 0.0 if_h: 32 Num Queues/Schedules: 1
        # Interface: Loopback2 QFP: 0.0 if_h: 34 Num Queues/Schedules: 0
        # Interface: GigabitEthernet0/0/1.2 QFP: 0.0 if_h: 35 Num Queues/Schedules: 0
        # Interface: GigabitEthernet0/0/1.EFP2054 QFP: 0.0 if_h: 36 Num Queues/Schedules: 0
        # Interface: BG4048.10207e1 QFP: 0.0 if_h: 4079 Num Queues/Schedules: 0
        # Interface: VPLS-2944.10207e2 QFP: 0.0 if_h: 4080 Num Queues/Schedules:
        # Interface: internal0/0/recycle:0 QFP: 0.0 if_h: 1 Num Queues/Schedules: 0
        p1 = re.compile(
            r"^Interface: +(?P<intf_name>[\w\d\/\.\-\:]+)"
            " +QFP: +(?P<qfp>[\d\.]+)"
            " +if_h: +(?P<if_h>\d+)"
            " +Num Queues/Schedules: +(?P<num_queues>\d+)$"
        )

        #     Index 0 (Queue ID:0xa6, Name: GigabitEthernet1/0/7)
        p2 = re.compile(
            r"^Index +(?P<index>\d+)"
            " +\(Queue +ID:(?P<queue_id>[\w\d]+),"
            " +Name: +(?P<interf_name>[\w\d\/\.\-\:]+)\)$"
        )

        #       Software Control Info:
        #  PARQ Software Control Info:
        p3_1 = re.compile(r"^(PARQ +)?Software Control Info:$")

        #  (cache) queue id: 0x000000a6, wred: 0x88b16ac2, qlimit (bytes): 3281312
        #  (cache) queue id: 0x00000070, wred: 0xe73cfde0, qlimit (pkts ): 418
        p3_2 = re.compile(
            r"^\(cache\) +queue +id: +(?P<cache_queue_id>[\w\d]+),"
            " +wred: +(?P<wred>[\w\d]+),"
            " +qlimit +\((?P<type>bytes|pkts +)\): +(?P<qlimit>\d+)$"
        )

        #       parent_sid: 0x284, debug_name: GigabitEthernet1/0/7
        p4 = re.compile(
            r"^parent_sid: +(?P<parent_sid>[\w\d]+),"
            " debug_name: +(?P<debug_name>[\w\d\/\.\-\:]+)$"
        )

        #       sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245728
        p5 = re.compile(
            r"^sw_flags: +(?P<sw_flags>[\w\d]+),"
            " +sw_state: +(?P<sw_state>[\w\d]+),"
            " +port_uidb: +(?P<port_uidb>\d+)$"
        )

        #       orig_min  : 0                   ,      min: 105000000
        p6 = re.compile(r"^orig_min +: +(?P<orig_min>\d+) +," " +min: +(?P<min>\d+)$")

        #       min_qos   : 0                   , min_dflt: 0
        p7 = re.compile(
            r"^min_qos +: +(?P<min_qos>\d+) +," " +min_dflt: +(?P<min_dflt>\d+)$"
        )

        #       orig_max  : 0                   ,      max: 0
        p8 = re.compile(r"^orig_max +: +(?P<orig_max>\d+) +," " +max: +(?P<max>\d+)$")

        #       max_qos   : 0                   , max_dflt: 0
        p9 = re.compile(
            r"^max_qos +: +(?P<max_qos>\d+) +," " +max_dflt: +(?P<max_dflt>\d+)$"
        )

        #       share     : 1
        p10 = re.compile(r"^share +: +(?P<share>\d+)$")

        #       plevel    : 0, priority: 65535
        p11 = re.compile(
            r"^plevel +: +(?P<plevel>\d+)," " +priority: +(?P<priority>\d+)$"
        )

        #       defer_obj_refcnt: 0
        #   defer_obj_refcnt: 0, cp_ppe_addr: 0x00000000
        p12 = re.compile(
            r"^defer_obj_refcnt: +(?P<defer_obj_refcnt>\d+)"
            r"(, +cp_ppe_addr: +(?P<cp_ppe_addr>\w+))?$"
        )

        #     Statistics:
        p13_1 = re.compile(r"^Statistics:$")

        #       tail drops  (bytes): 0                   ,          (packets): 0
        p13_2 = re.compile(
            r"^tail +drops +\(bytes\): +(?P<tail_drops_bytes>\d+) +,"
            " +\(packets\): +(?P<tail_drops_packets>\d+)$"
        )

        #       total enqs  (bytes): 0                   ,          (packets): 0
        p14 = re.compile(
            r"^total +enqs +\(bytes\): +(?P<total_enqs_bytes>\d+) +,"
            " +\(packets\): +(?P<total_enqs_packets>\d+)$"
        )

        #       queue_depth (bytes): 0
        #       queue_depth (pkts ): 0
        p15 = re.compile(
            r"^queue_depth +\((?P<type>bytes|pkts +)\): +(?P<queue_depth>\d+)$"
        )

        #       licensed throughput oversubscription drops:
        #                   (bytes): 0                   ,          (packets): 0
        p16 = re.compile(
            r"^\(bytes\): +(?P<lic_throughput_oversub_drops_bytes>\d+) +,"
            " +\(packets\): +(?P<lic_throughput_oversub_drops_packets>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group["intf_name"]
                ret_dict.setdefault(interface, {})
                ret_dict[interface]["if_h"] = int(group["if_h"])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                index = group["index"]
                if "index" not in ret_dict[interface]:
                    ret_dict[interface].setdefault("index", {})
                ret_dict[interface]["index"].setdefault(index, {})
                ret_dict[interface]["index"][index]["queue_id"] = group["queue_id"]
                ret_dict[interface]["index"][index]["name"] = group["interf_name"]
                continue

            m = p3_1.match(line)
            if m:
                ret_dict[interface]["index"][index].setdefault(
                    "software_control_info", {}
                )
                continue

            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["software_control_info"][
                    "cache_queue_id"
                ] = group["cache_queue_id"]
                ret_dict[interface]["index"][index]["software_control_info"][
                    "wred"
                ] = group["wred"]
                if group["type"].strip() == "bytes":
                    ret_dict[interface]["index"][index]["software_control_info"][
                        "qlimit_bytes"
                    ] = int(group["qlimit"])
                else:
                    ret_dict[interface]["index"][index]["software_control_info"][
                        "qlimit_pkts"
                    ] = int(group["qlimit"])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["software_control_info"].update(
                    {k: v for k, v in group.items()}
                )
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["software_control_info"][
                    "sw_flags"
                ] = group["sw_flags"]
                ret_dict[interface]["index"][index]["software_control_info"][
                    "sw_state"
                ] = group["sw_state"]
                ret_dict[interface]["index"][index]["software_control_info"][
                    "port_uidb"
                ] = int(group["port_uidb"])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["software_control_info"].update(
                    {k: int(v) for k, v in group.items()}
                )
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["software_control_info"].update(
                    {k: int(v) for k, v in group.items()}
                )
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["software_control_info"].update(
                    {k: int(v) for k, v in group.items()}
                )
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["software_control_info"].update(
                    {k: int(v) for k, v in group.items()}
                )
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["software_control_info"][
                    "share"
                ] = int(group["share"])
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["software_control_info"].update(
                    {k: int(v) for k, v in group.items()}
                )
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["software_control_info"][
                    "defer_obj_refcnt"
                ] = int(group["defer_obj_refcnt"])

                if group["cp_ppe_addr"]:
                    ret_dict[interface]["index"][index]["software_control_info"][
                        "cp_ppe_addr"
                    ] = group["cp_ppe_addr"]
                continue

            m = p13_1.match(line)
            if m:
                ret_dict[interface]["index"][index].setdefault("statistics", {})
                continue

            m = p13_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["statistics"].update(
                    {k: int(v) for k, v in group.items()}
                )
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["statistics"].update(
                    {k: int(v) for k, v in group.items()}
                )
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                if group["type"].strip() == "bytes":
                    ret_dict[interface]["index"][index]["statistics"][
                        "queue_depth_bytes"
                    ] = int(group["queue_depth"])
                else:
                    ret_dict[interface]["index"][index]["statistics"][
                        "queue_depth_pkts"
                    ] = int(group["queue_depth"])
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]["index"][index]["statistics"].update(
                    {k: int(v) for k, v in group.items()}
                )
                continue

        return ret_dict


class ShowPlatformHardwarePlimSchema(MetaParser):
    """Schema for show platform hardware port <x/x/x> plim statistics
    show platform hardware slot <x> plim statistics
    show platform hardware slot <x> plim statistics internal
    show platform hardware subslot <x/x> plim statistics"""

    schema = {
        Optional("port"): {
            Any(): {
                "received": {
                    "low_priority": {
                        "pkts": int,
                        "dropped_pkts": int,
                        "errored_pkts": int,
                        "bytes": int,
                        "dropped_bytes": int,
                        "errored_bytes": int,
                    },
                    "high_priority": {
                        "pkts": int,
                        "dropped_pkts": int,
                        "errored_pkts": int,
                        "bytes": int,
                        "dropped_bytes": int,
                        "errored_bytes": int,
                    },
                },
                "transmitted": {
                    "low_priority": {
                        "pkts": int,
                        "dropped_pkts": int,
                        "bytes": int,
                        "dropped_bytes": int,
                    },
                    "high_priority": {
                        "pkts": int,
                        "dropped_pkts": int,
                        "bytes": int,
                        "dropped_bytes": int,
                    },
                },
            },
        },
        Optional("slot"): {
            Any(): {
                "subslot": {
                    Any(): {
                        "name": str,
                        "status": str,
                        "received": {
                            Optional("pkts"): int,
                            Optional("ipc_pkts"): int,
                            Optional("bytes"): int,
                            Optional("ipc_bytes"): int,
                            Optional("ipc_err"): int,
                            Optional("spi4_interrupt_counters"): {
                                "out_of_frame": int,
                                "dip4_error": int,
                                "disabled": int,
                                "loss_of_sync": int,
                                "sequence_error": int,
                                "burst_error": int,
                                "eop_abort": int,
                                "packet_gap_error": int,
                                "control_word_error": int,
                            },
                        },
                        "transmitted": {
                            Optional("pkts"): int,
                            Optional("ipc_pkts"): int,
                            Optional("bytes"): int,
                            Optional("ipc_bytes"): int,
                            Optional("ipc_err"): int,
                            Optional("spi4_interrupt_counters"): {
                                "out_of_frame": int,
                                "frame_error": int,
                                "fifo_over_flow": int,
                                "dip2_error": int,
                            },
                        },
                    },
                }
            },
        },
    }


class ShowPlatformHardwarePlim(ShowPlatformHardwarePlimSchema):
    """Parser for show platform hardware port <x/x/x> plim statistics
    show platform hardware slot <x> plim statistics
    show platform hardware slot <x> plim statistics internal
    show platform hardware subslot <x/x> plim statistics"""

    cli_command = [
        "show platform hardware port {port} plim statistics",
        "show platform hardware slot {slot} plim statistics",
        "show platform hardware slot {slot} plim statistics internal",
        "show platform hardware subslot {subslot} plim statistics",
    ]

    def cli(self, port=None, slot=None, subslot=None, internal=False, output=None):
        if output is None:
            if port:
                cmd = self.cli_command[0].format(port=port)
            elif slot:
                if internal:
                    cmd = self.cli_command[2].format(slot=slot)
                else:
                    cmd = self.cli_command[1].format(slot=slot)
            elif subslot:
                cmd = self.cli_command[3].format(subslot=subslot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Interface 0/0/0
        p1 = re.compile(r"^Interface +(?P<port>[\d\/]+)$")

        #   RX Low Priority
        #   RX High Priority
        p2 = re.compile(r"^RX +(?P<direction>\w+) +Priority$")

        #     RX Pkts      369         Bytes 27789
        p3 = re.compile(
            r"^RX +Pkts +(?P<rx_total_pkts>\d+) +Bytes +(?P<rx_total_bytes>\d+)$"
        )

        #     RX Drop Pkts 0           Bytes 0
        p4 = re.compile(
            r"^RX +Drop +Pkts +(?P<rx_dropped_pkts>\d+) +Bytes +(?P<rx_dropped_bytes>\d+)$"
        )

        #     RX Err  Pkts 0           Bytes 0
        p5 = re.compile(
            r"^RX +Err +Pkts +(?P<rx_errored_pkts>\d+) +Bytes +(?P<rx_errored_bytes>\d+)$"
        )

        #   TX Low Priority
        #   TX High Priority
        p6 = re.compile(r"^TX +(?P<direction>\w+) +Priority$")

        #     TX Pkts      1265574622  Bytes 250735325722
        p7 = re.compile(
            r"^TX +Pkts +(?P<tx_total_pkts>\d+) +Bytes +(?P<tx_total_bytes>\d+)$"
        )

        #     TX Drop Pkts 0           Bytes 0
        p8 = re.compile(
            r"^TX +Drop +Pkts +(?P<tx_dropped_pkts>\d+) +Bytes +(?P<tx_dropped_bytes>\d+)$"
        )

        # 0/3, SPA-1XTENGE-XFP-V2, Online
        p9 = re.compile(
            r"^(?P<slot>\d+)/(?P<subslot>\d+),"
            " +(?P<name>[\w\d\-]+),"
            " +(?P<status>\w+)$"
        )

        #   RX IPC Pkts 0           Bytes 0
        p10 = re.compile(
            r"^RX +IPC +Pkts +(?P<rx_ipc_pkts>\d+) +Bytes +(?P<rx_ipc_bytes>\d+)$"
        )

        #   TX IPC Pkts 0           Bytes 0
        p11 = re.compile(
            r"^TX +IPC +Pkts +(?P<tx_ipc_pkts>\d+) +Bytes +(?P<tx_ipc_bytes>\d+)$"
        )

        #   RX IPC Err 0
        p12 = re.compile(r"^RX +IPC +Err +(?P<rx_ipc_err>\d+)$")

        #   TX IPC Err 0
        p13 = re.compile(r"^TX +IPC +Err +(?P<tx_ipc_err>\d+)$")

        #   RX Spi4 Interrupt Counters
        #   TX Spi4 Interrupt Counters
        p14 = re.compile(r"^(?P<tx_rx>\w+) +Spi4 +Interrupt +Counters$")

        #     Out Of Frame 0
        p15 = re.compile(r"^Out +Of +Frame +(?P<out_of_frame>\d+)$")

        #     Dip4 Error 0
        p16 = re.compile(r"^Dip4 +Error +(?P<rx_dip4_error>\d+)$")

        #     Disabled 0
        p17 = re.compile(r"^Disabled +(?P<rx_disbaled>\d+)$")

        #     Loss Of Sync 0
        p18 = re.compile(r"^Loss +Of +Sync +(?P<rx_loss_of_sync>\d+)$")

        #     Sequence Error 0
        p19 = re.compile(r"^Sequence +Error +(?P<rx_sequence_error>\d+)$")

        #     Burst Error 0
        p20 = re.compile(r"^Burst +Error +(?P<rx_burst_error>\d+)$")

        #     EOP Abort 0
        p21 = re.compile(r"^EOP +Abort +(?P<rx_eop_abort>\d+)$")

        #     Packet Gap Error 0
        p22 = re.compile(r"^Packet +Gap +Error +(?P<rx_packet_gap_error>\d+)$")

        #     Control Word Error 0
        p23 = re.compile(r"^Control +Word +Error +(?P<rx_control_word_error>\d+)$")

        #     Frame Error 0
        p24 = re.compile(r"^Frame +Error +(?P<tx_frame_error>\d+)$")

        #     FIFO Over Flow 0
        p25 = re.compile(r"^FIFO +Over +Flow +(?P<tx_fifo_over_flow>\d+)$")

        #     Dip2 Error 0
        p26 = re.compile(r"^Dip2 +Error +(?P<tx_dip2_error>\d+)$")

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                port = group["port"]
                ret_dict.setdefault("port", {}).setdefault(port, {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                direction = group["direction"]
                if "received" not in ret_dict["port"][port]:
                    ret_dict["port"][port].setdefault("received", {})
                if direction == "Low":
                    low_high = "low_priority"
                else:
                    low_high = "high_priority"
                ret_dict["port"][port]["received"].setdefault(low_high, {})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                if "port" in ret_dict:
                    ret_dict["port"][port]["received"][low_high]["pkts"] = int(
                        group["rx_total_pkts"]
                    )
                    ret_dict["port"][port]["received"][low_high]["bytes"] = int(
                        group["rx_total_bytes"]
                    )
                else:
                    if "received" not in ret_dict["slot"][slot]["subslot"][subslot]:
                        ret_dict["slot"][slot]["subslot"][subslot].setdefault(
                            "received", {}
                        )
                    ret_dict["slot"][slot]["subslot"][subslot]["received"][
                        "pkts"
                    ] = int(group["rx_total_pkts"])
                    ret_dict["slot"][slot]["subslot"][subslot]["received"][
                        "bytes"
                    ] = int(group["rx_total_bytes"])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["port"][port]["received"][low_high]["dropped_pkts"] = int(
                    group["rx_dropped_pkts"]
                )
                ret_dict["port"][port]["received"][low_high]["dropped_bytes"] = int(
                    group["rx_dropped_bytes"]
                )
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict["port"][port]["received"][low_high]["errored_pkts"] = int(
                    group["rx_errored_pkts"]
                )
                ret_dict["port"][port]["received"][low_high]["errored_bytes"] = int(
                    group["rx_errored_bytes"]
                )
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                direction = group["direction"]
                if "transmitted" not in ret_dict["port"][port]:
                    ret_dict["port"][port].setdefault("transmitted", {})
                if direction == "Low":
                    low_high = "low_priority"
                else:
                    low_high = "high_priority"
                ret_dict["port"][port]["transmitted"].setdefault(low_high, {})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                if "port" in ret_dict:
                    ret_dict["port"][port]["transmitted"][low_high]["pkts"] = int(
                        group["tx_total_pkts"]
                    )
                    ret_dict["port"][port]["transmitted"][low_high]["bytes"] = int(
                        group["tx_total_bytes"]
                    )
                else:
                    if "transmitted" not in ret_dict["slot"][slot]["subslot"][subslot]:
                        ret_dict["slot"][slot]["subslot"][subslot].setdefault(
                            "transmitted", {}
                        )
                    ret_dict["slot"][slot]["subslot"][subslot]["transmitted"][
                        "pkts"
                    ] = int(group["tx_total_pkts"])
                    ret_dict["slot"][slot]["subslot"][subslot]["transmitted"][
                        "bytes"
                    ] = int(group["tx_total_bytes"])
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict["port"][port]["transmitted"][low_high]["dropped_pkts"] = int(
                    group["tx_dropped_pkts"]
                )
                ret_dict["port"][port]["transmitted"][low_high]["dropped_bytes"] = int(
                    group["tx_dropped_bytes"]
                )
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                slot = group["slot"]
                subslot = group["subslot"]
                ret_dict.setdefault("slot", {}).setdefault(slot, {})
                if "subslot" not in ret_dict["slot"][slot]:
                    ret_dict["slot"][slot].setdefault("subslot", {})
                ret_dict["slot"][slot]["subslot"].setdefault(subslot, {})
                ret_dict["slot"][slot]["subslot"][subslot]["name"] = group["name"]
                ret_dict["slot"][slot]["subslot"][subslot]["status"] = group["status"]
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                if "received" not in ret_dict["slot"][slot]["subslot"][subslot]:
                    ret_dict["slot"][slot]["subslot"][subslot].setdefault(
                        "received", {}
                    )
                ret_dict["slot"][slot]["subslot"][subslot]["received"][
                    "ipc_pkts"
                ] = int(group["rx_ipc_pkts"])
                ret_dict["slot"][slot]["subslot"][subslot]["received"][
                    "ipc_bytes"
                ] = int(group["rx_ipc_bytes"])
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                if "transmitted" not in ret_dict["slot"][slot]["subslot"][subslot]:
                    ret_dict["slot"][slot]["subslot"][subslot].setdefault(
                        "transmitted", {}
                    )
                ret_dict["slot"][slot]["subslot"][subslot]["transmitted"][
                    "ipc_pkts"
                ] = int(group["tx_ipc_pkts"])
                ret_dict["slot"][slot]["subslot"][subslot]["transmitted"][
                    "ipc_bytes"
                ] = int(group["tx_ipc_bytes"])
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot].setdefault("received", {})
                ret_dict["slot"][slot]["subslot"][subslot]["received"]["ipc_err"] = int(
                    group["rx_ipc_err"]
                )
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot].setdefault("transmitted", {})
                ret_dict["slot"][slot]["subslot"][subslot]["transmitted"][
                    "ipc_err"
                ] = int(group["tx_ipc_err"])
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                tx_rx_direction = group["tx_rx"]
                if tx_rx_direction == "RX":
                    new_direction = "received"
                else:
                    new_direction = "transmitted"
                ret_dict["slot"][slot]["subslot"][subslot][new_direction].setdefault(
                    "spi4_interrupt_counters", {}
                )
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["out_of_frame"] = int(group["out_of_frame"])
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["dip4_error"] = int(group["rx_dip4_error"])
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["disabled"] = int(group["rx_disbaled"])
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["loss_of_sync"] = int(group["rx_loss_of_sync"])
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["sequence_error"] = int(group["rx_sequence_error"])
                continue

            m = p20.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["burst_error"] = int(group["rx_burst_error"])
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["eop_abort"] = int(group["rx_eop_abort"])
                continue

            m = p22.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["packet_gap_error"] = int(group["rx_packet_gap_error"])
                continue

            m = p23.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["control_word_error"] = int(group["rx_control_word_error"])
                continue

            m = p24.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["frame_error"] = int(group["tx_frame_error"])
                continue

            m = p25.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["fifo_over_flow"] = int(group["tx_fifo_over_flow"])
                continue

            m = p26.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot"][slot]["subslot"][subslot][new_direction][
                    "spi4_interrupt_counters"
                ]["dip2_error"] = int(group["tx_dip2_error"])
                continue

        return ret_dict


class ShowPlatformHardwareQfpBqsMappingSchema(MetaParser):
    """Schema for show platform hardware qfp active bqs <x> ipm mapping
    show platform hardware qfp standby bqs <x> ipm mapping
    show platform hardware qfp active bqs <x> opm mapping
    show platform hardware qfp standby bqs <x> opm mapping"""

    schema = {
        "channel": {
            Any(): {
                Optional("interface"): str,
                "name": str,
                Optional("logical_channel"): int,
                Optional("drain_mode"): bool,
                Optional("port"): int,
                Optional("cfifo"): int,
            },
        }
    }


class ShowPlatformHardwareQfpBqsOpmMapping(ShowPlatformHardwareQfpBqsMappingSchema):
    """Parser for show platform hardware qfp active bqs <x> opm mapping
    show platform hardware qfp standby bqs <x> opm mapping"""

    cli_command = "show platform hardware qfp {status} bqs {slot} opm mapping"

    def cli(self, status, slot, output=None):
        if output is None:
            cmd = self.cli_command.format(status=status, slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Chan     Name                          Interface      LogicalChannel
        #  0       CC0 Low                       SPI0            0
        # 24       Peer-FP Low                   SPI0           24
        # 26       Nitrox Low                    SPI0           26
        # 28       HT Pkt Low                    HT              0
        # 38       HighNormal                    GPM             7
        # 55*      Drain Low                     GPM             0
        # * - indicates the drain mode bit is set for this channel
        p1 = re.compile(
            r"^(?P<number>\d+)(?P<drained>\*)? +(?P<name>[\w\-\s]+)"
            " +(?P<interface>[\w\d]+) +(?P<logical_channel>\d+)$"
        )

        # 32       Unmapped
        p2 = re.compile(r"^(?P<unmapped_number>\d+) +Unmapped$")

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group["interface"]
                number = group["number"]
                if group["drained"]:
                    drained = True
                else:
                    drained = False
                if "channel" not in ret_dict:
                    final_dict = ret_dict.setdefault("channel", {})
                final_dict = ret_dict["channel"].setdefault(number, {})
                final_dict.update({"interface": group["interface"].strip()})
                final_dict.update({"name": group["name"].strip()})
                final_dict.update({"logical_channel": int(group["logical_channel"])})
                final_dict.update({"drain_mode": drained})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group["unmapped_number"]
                if "channel" not in ret_dict:
                    ret_dict.setdefault("channel", {})
                ret_dict["channel"].setdefault(unmapped_number, {})
                ret_dict["channel"][unmapped_number].update({"name": "unmapped"})
                continue

        return ret_dict


class ShowPlatformHardwareQfpBqsIpmMapping(ShowPlatformHardwareQfpBqsMappingSchema):
    """Parser for show platform hardware qfp active bqs <x> ipm mapping
    show platform hardware qfp standby bqs <x> ipm mapping"""

    cli_command = "show platform hardware qfp {status} bqs {slot} ipm mapping"

    def cli(self, status, slot, output=None):
        if output is None:
            cmd = self.cli_command.format(status=status, slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Chan   Name                Interface      Port     CFIFO
        #  1     CC3 Low             SPI0           0        1
        # 13     Peer-FP Low         SPI0          12        3
        # 15     Nitrox Low          SPI0          14        1
        # 17     HT Pkt Low          HT             0        1
        # 21     CC4 Low             SPI0          16        1
        p1 = re.compile(
            r"^(?P<number>\d+) +(?P<name>[\w\-\s]+)"
            " +(?P<interface>[\w\d]+) +(?P<port>\d+)"
            " +(?P<cfifo>\d+)$"
        )

        # 32       Unmapped
        p2 = re.compile(r"^(?P<unmapped_number>\d+) +Unmapped$")

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                number = group["number"]
                final_dict = ret_dict.setdefault("channel", {}).setdefault(number, {})
                final_dict.update({"interface": group["interface"].strip()})
                final_dict.update({"name": group["name"].strip()})
                final_dict.update({"port": int(group["port"])})
                final_dict.update({"cfifo": int(group["cfifo"])})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group["unmapped_number"]
                if "channel" not in ret_dict:
                    ret_dict.setdefault("channel", {})
                ret_dict["channel"].setdefault(unmapped_number, {})
                ret_dict["channel"][unmapped_number].update({"name": "unmapped"})
                continue

        return ret_dict


class ShowPlatformHardwareSerdesSchema(MetaParser):
    """Schema for show platform hardware slot <x> serdes statistics
    show platform hardware slot <x> serdes statistics internal"""

    schema = {
        "link": {
            Any(): {
                Optional("from"): {
                    "pkts": {
                        Optional("total"): int,
                        Optional("high"): int,
                        Optional("low"): int,
                        Optional("dropped"): int,
                        Optional("errored"): int,
                        Optional("looped"): int,
                        Optional("bad"): int,
                    },
                    "bytes": {
                        Optional("total"): int,
                        Optional("high"): int,
                        Optional("low"): int,
                        Optional("dropped"): int,
                        Optional("errored"): int,
                        Optional("looped"): int,
                        Optional("bad"): int,
                    },
                    Optional("qstat_count"): int,
                    Optional("flow_ctrl_count"): int,
                },
                Optional("to"): {
                    "pkts": {
                        Optional("total"): int,
                        Optional("high"): int,
                        Optional("low"): int,
                        Optional("dropped"): int,
                        Optional("errored"): int,
                    },
                    Optional("bytes"): {
                        Optional("total"): int,
                        Optional("high"): int,
                        Optional("low"): int,
                        Optional("dropped"): int,
                        Optional("errored"): int,
                    },
                },
                Optional("local_tx_in_sync"): bool,
                Optional("local_rx_in_sync"): bool,
                Optional("remote_tx_in_sync"): bool,
                Optional("remote_rx_in_sync"): bool,
                Optional("errors"): {
                    "rx_process": int,
                    "rx_schedule": int,
                    "rx_statistics": int,
                    "rx_parity": int,
                    "tx_process": int,
                    "tx_schedule": int,
                    "tx_statistics": int,
                },
            },
        },
        Optional("serdes_exception_counts"): {
            Any(): {
                Optional("link"): {
                    Any(): {
                        "msgTypeError": int,
                        "msgEccError": int,
                        "chicoEvent": int,
                    },
                }
            },
        },
    }


class ShowPlatformHardwareSerdes(ShowPlatformHardwareSerdesSchema):
    """Parser for show platform hardware slot <x> serdes statistics"""

    cli_command = "show platform hardware slot {slot} serdes statistics"

    def cli(self, slot, output=None):
        if output is None:
            cmd = self.cli_command.format(slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # From Slot 1-Link B
        p1 = re.compile(r"^From +Slot +(?P<link>[\w\d\-\s]+)$")

        #   Pkts  High: 0          Low: 0          Bad: 0          Dropped: 0
        p2 = re.compile(
            r"^Pkts +High: +(?P<high>\d+) +Low: +(?P<low>\d+)( +Bad: +(?P<bad>\d+) +Dropped: +(?P<dropped>\d+))?$"
        )

        #   Bytes High: 0          Low: 0          Bad: 0          Dropped: 0
        p3 = re.compile(
            r"^Bytes +High: +(?P<high>\d+) +Low: +(?P<low>\d+) +Bad: +(?P<bad>\d+) +Dropped: +(?P<dropped>\d+)$"
        )

        #   Pkts  Looped: 0          Error: 0
        p4 = re.compile(r"^Pkts +Looped: +(?P<looped>\d+) +Error: +(?P<errored>\d+)$")

        #   Bytes Looped 0
        p5 = re.compile(r"^Bytes +Looped +(?P<looped>\d+)$")

        #   Qstat count: 0          Flow ctrl count: 3501
        p6 = re.compile(
            r"^Qstat +count: +(?P<qstat_count>\d+) +Flow +ctrl +count: +(?P<flow_ctrl_count>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                slot = group["link"]
                from_dict = (
                    ret_dict.setdefault("link", {})
                    .setdefault(slot, {})
                    .setdefault("from", {})
                )
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                if not group["bad"]:
                    to_dict = (
                        ret_dict["link"][slot]
                        .setdefault("to", {})
                        .setdefault("pkts", {})
                    )
                    to_dict.update({k: int(v) for k, v in group.items() if v})
                    continue

                pkts_dict = ret_dict["link"][slot]["from"].setdefault("pkts", {})
                pkts_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                bytes_dict = ret_dict["link"][slot]["from"].setdefault("bytes", {})
                bytes_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                pkts_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                bytes_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                from_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowPlatformHardwareSerdesInternal(ShowPlatformHardwareSerdesSchema):
    """Parser for show platform hardware slot <x> serdes statistics internal"""

    cli_command = "show platform hardware slot {slot} serdes statistics internal"

    def cli(self, slot, output=None):
        if output is None:
            cmd = self.cli_command.format(slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Network-Processor-0 Link:
        # RP/ESP Link:
        p1 = re.compile(r"^(?P<link>[\w\d\-\s/]+) +Link:$")

        #   Local TX in sync, Local RX in sync
        p2 = re.compile(r"^Local +TX +in +sync, +Local +RX +in +sync$")

        #   Remote TX in sync, Remote RX in sync
        p3 = re.compile(r"^Remote +TX +in +sync, +Remote +RX +in +sync$")

        #   To Network-Processor       Packets:    21763844  Bytes:  7343838083
        #   To Encryption Processor   Packets:           0  Bytes:           0
        #   To RP/ESP Packets: 1150522 Bytes: 166031138
        p4 = re.compile(
            r"^To +(?P<link_name_1>[\w\-\d\s/]+) +Packets: +(?P<to_packets>\d+) +Bytes: +(?P<to_bytes>\d+)$"
        )

        #   From Network-Processor     Packets:    21259012  Bytes:  7397920802
        #   From RP/ESP Packets: 4364008 Bytes: 697982854
        p5 = re.compile(
            r"^From +(?P<link_name_2>[\w\-\d\s/]+) +Packets: +(?P<from_packets>\d+) +Bytes: +(?P<from_bytes>\d+)$"
        )

        #     Drops                   Packets:           0  Bytes:           0
        p6 = re.compile(
            r"^Drops +Packets: +(?P<dropped_packets>\d+) +Bytes: +(?P<dropped_bytes>\d+)$"
        )

        #     Errors                  Packets:           0  Bytes:           0
        p7 = re.compile(
            r"^Errors +Packets: +(?P<errored_packets>\d+) +Bytes: +(?P<errored_bytes>\d+)$"
        )

        #     Errors:
        p8 = re.compile(r"^Errors:$")

        #     RX/TX process: 0/0, RX/TX schedule: 0/0
        p9 = re.compile(
            r"^RX/TX +process: +(?P<rx_process>\d+)/(?P<tx_process>\d+), +RX/TX +schedule: +(?P<rx_schedule>\d+)/(?P<tx_schedule>\d+)$"
        )

        #     RX/TX statistics: 0/0, RX parity: 0
        p10 = re.compile(
            r"^RX/TX +statistics: +(?P<rx_statistics>\d+)/(?P<tx_statistics>\d+), +RX +parity: +(?P<rx_parity>\d+)$"
        )

        # Serdes Exception Counts:
        p11 = re.compile(r"^Serdes +Exception +Counts:$")

        #   eqs/fc:
        #   idh-hi:
        #   spi link:
        p12 = re.compile(r"^(?P<link>[\w\d\-\s\/]+):$")

        #     link 0: msgTypeError: 5
        #     link 0: msgEccError: 5
        #     link 0: chicoEvent: 5
        #     link 1: msgTypeError: 1
        #     link 1: msgEccError: 1
        #     link 1: chicoEvent: 1
        #     link 2: msgTypeError: 3
        #     link 2: msgEccError: 3
        #     link 2: chicoEvent: 3
        p13 = re.compile(
            r"^link +(?P<link_number>\d+): +(?P<error_event>\w+): +(?P<count>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                link = group["link"]
                new_dict = ret_dict.setdefault("link", {}).setdefault(link, {})
                continue

            m = p2.match(line)
            if m:
                new_dict["local_tx_in_sync"] = True
                new_dict["local_rx_in_sync"] = True
                continue

            m = p3.match(line)
            if m:
                new_dict["remote_tx_in_sync"] = True
                new_dict["remote_rx_in_sync"] = True
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                to_not_from = True
                new_dict.setdefault("to", {}).setdefault("pkts", {})
                new_dict["to"].setdefault("bytes", {})
                new_dict["to"]["pkts"]["total"] = int(group["to_packets"])
                new_dict["to"]["bytes"]["total"] = int(group["to_bytes"])
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                to_not_from = False
                new_dict.setdefault("from", {}).setdefault("pkts", {})
                new_dict["from"].setdefault("bytes", {})
                new_dict["from"]["pkts"]["total"] = int(group["from_packets"])
                new_dict["from"]["bytes"]["total"] = int(group["from_bytes"])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                if to_not_from:
                    new_dict["to"]["pkts"]["dropped"] = int(group["dropped_packets"])
                    new_dict["to"]["bytes"]["dropped"] = int(group["dropped_bytes"])
                else:
                    new_dict["from"]["pkts"]["dropped"] = int(group["dropped_packets"])
                    new_dict["from"]["bytes"]["dropped"] = int(group["dropped_bytes"])
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                if to_not_from:
                    new_dict["to"]["pkts"]["errored"] = int(group["errored_packets"])
                    new_dict["to"]["bytes"]["errored"] = int(group["errored_bytes"])
                else:
                    new_dict["from"]["pkts"]["errored"] = int(group["errored_packets"])
                    new_dict["from"]["bytes"]["errored"] = int(group["errored_bytes"])
                continue

            m = p8.match(line)
            if m:
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                new_dict.setdefault("errors", {})
                new_dict["errors"].update({k: int(v) for k, v in group.items()})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                if "errors" in ret_dict["link"][link]:
                    new_dict["errors"].update({k: int(v) for k, v in group.items()})
                continue

            m = p11.match(line)
            if m:
                serdes_exception_counts = True
                ret_dict.setdefault("serdes_exception_counts", {})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                link = group["link"]
                ret_dict["serdes_exception_counts"].setdefault(link, {})
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                link_number = group["link_number"]
                error_event = group["error_event"]
                ret_dict["serdes_exception_counts"][link].setdefault(
                    "link", {}
                ).setdefault(link_number, {})
                ret_dict["serdes_exception_counts"][link]["link"][link_number][
                    error_event
                ] = int(group["count"])
                continue

        return ret_dict


class ShowPlatformHardwareModuleInterfaceStatusSchema(MetaParser):
    """Schema for show platform hardware subslot {id} module interface {intf} status"""

    schema = {
        "mac_status": {
            "hw_port": int,
            "speed": int,
            "duplex": str,
            "link": str,
            "link_en": str,
            "tx_pause": str,
            "rx_pause": str,
        },
        "l3_network": {
            "link": str,
            "link_config": str,
            "speed": str,
            "speed_config": str,
            "duplex": str,
            "duplex_config": str,
            "nego_config": str,
            "mtu": int,
            "rx_pause": str,
            "rx_pause_config": str,
            "tx_pause": str,
            "tx_pause_config": str,
        },
        "mac_filtering": str,
        "mac_addr": str,
        Optional("pve"): str,
        Optional("target_port"): int,
        Optional("nested_vlan"): str,
        Optional("is_trunk"): str,
        Optional("nested_vid"): int,
        Optional("td_profile"): int,
        Optional("sche_profile"): int,
        Optional("default_pri"): int,
        Optional("up_override"): str,
        Optional("trust_mode"): str,
        Optional("exp"): str,
        Optional("cos_bit"): str,
        Optional("exp_bit"): str,
        Optional("dscp_bit"): str,
        Optional("lp_profile"): int,
        Optional("lp_cos"): int,
        Optional("lp_tc"): int,
        Optional("hp_profile"): int,
        Optional("hp_cos"): int,
        Optional("hp_tc"): int,
        Optional("tx_queue"): int,
        Optional("tx_pause_xoff"): str,
        Optional("xoff_thres"): int,
        Optional("plim_thres"): int,
        Optional("buffer_size"): int,
        Optional("xon_thres"): int,
        Optional("lp_q_cos"): int,
        Optional("lp_q_tc"): int,
        Optional("lp_weight"): int,
        Optional("lp_sche_weight"): int,
        Optional("hp_q_cos"): int,
        Optional("hp_q_tc"): int,
        Optional("hp_bw"): int,
        Optional("hp_sche_weight"): int,
        Optional("port_tx_buffer"): int,
        Optional("q0_tx_buffer"): int,
        Optional("q1_tx_buffer"): int,
        Optional("q2_tx_buffer"): int,
        Optional("q3_tx_buffer"): int,
        Optional("q4_tx_buffer"): int,
        Optional("q5_tx_buffer"): int,
        Optional("q6_tx_buffer"): int,
        Optional("q7_tx_buffer"): int,
    }


class ShowPlatformHardwareModuleInterfaceStatus(
    ShowPlatformHardwareModuleInterfaceStatusSchema
):
    """Parser for show platform hardware subslot {id} module interface {intf} status"""

    cli_command = ["show platform hardware subslot {id} module interface {intf} status"]

    def cli(self, id=None, intf=None, output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command[0].format(id=id, intf=intf))

        # MAC Status: hw_port 0, speed 1000, duplex full, link Up, link_en Enable , tx_pause Enable, rx_pause Enable
        p1 = re.compile(
            r"^MAC Status: hw_port (?P<hw_port>\d+), +speed (?P<speed>\d+), +duplex (?P<duplex>\S+), link "
            + r"(?P<link>\S+), link_en (?P<link_en>\S+) , tx_pause (?P<tx_pause>\S+), rx_pause (?P<rx_pause>\S+)$"
        )

        # link Up(config Enable), speed 1000(config 1000), duplex full(config full), config force_up, mtu 1526
        p2 = re.compile(
            r"^link (?P<link>\S+)\(config (?P<link_config>\S+)\), +speed (?P<speed>\S+)\(config "
            + r"(?P<speed_config>\S+)\), duplex (?P<duplex>\S+)\(config (?P<duplex_config>\S+)\), "
            + r"config (?P<nego_config>\S+), mtu (?P<mtu>\d+)$"
        )

        # rx_pause On(config On), tx_pause On(config On)
        p3 = re.compile(
            r"^rx_pause (?P<rx_pause>\S+)\(config (?P<rx_pause_config>\S+)\), tx_pause"
            + r" (?P<tx_pause>\S+)\(config (?P<tx_pause_config>\S+)\)$"
        )

        # mac_filtering: Enable, mac: 0000.0000.0001
        p4 = re.compile(
            r"^mac_filtering: +(?P<mac_filtering>\S+), mac: (?P<mac_addr>\S+)$"
        )

        # PVE :enable, target port: 24, isTrunk:false
        p5 = re.compile(
            r"^PVE :+(?P<pve>\S+), target port: +(?P<target_port>\d+), isTrunk:(?P<is_trunk>\S+)$"
        )

        # nested vlan :enable, vlan: 2356
        p6 = re.compile(
            r"^nested vlan :+(?P<nested_vlan>\S+), vlan: (?P<nested_vid>\d+)$"
        )

        # tail-drop profile 0, sche_profile 2
        p7 = re.compile(
            r"^tail-drop profile +(?P<td_profile>\d+), sche_profile (?P<sche_profile>\d+)$"
        )

        # default priority 0, UP override True
        p8 = re.compile(
            r"^default priority +(?P<default_pri>\d+), UP override (?P<up_override>\S+)$"
        )

        # None Trust mode
        p9 = re.compile(r"^(?P<trust_mode>\S+) Trust mode$")

        # Exp Enable
        p10 = re.compile(r"^Exp (?P<exp>\S+)$")

        # cos_bit_vec: 0x00, exp_bit_vec: 0xc0, dscp_bit_vec: 0x0000000000000000
        p11 = re.compile(
            r"^cos_bit_vec: +(?P<cos_bit>\S+), exp_bit_vec: +(?P<exp_bit>\S+), dscp_bit_vec: +(?P<dscp_bit>\S+)$"
        )

        # LP Qos Profile: 104, Cos: 0, TC: 0.
        p12 = re.compile(
            r"^LP Qos Profile: +(?P<lp_profile>\d+), Cos: +(?P<lp_cos>\d+), TC: +(?P<lp_tc>\d+).$"
        )

        # HP Qos Profile: 105, Cos: 4, TC: 4.
        p13 = re.compile(
            r"^HP Qos Profile: +(?P<hp_profile>\d+), Cos: +(?P<hp_cos>\d+), TC: +(?P<hp_tc>\d+).$"
        )

        # SP Tx Queue: 7.
        p14 = re.compile(r"^SP Tx Queue: +(?P<tx_queue>\d+).$")

        # TX_PAUSE: disabled XOFF_THRES: 1024(plim threshold 99%, Buff-size: 1024),   XON_THRES: 128
        p15 = re.compile(
            r"^TX_PAUSE: +(?P<tx_pause_xoff>\S+) XOFF_THRES: +(?P<xoff_thres>\d+)\(plim threshold "
            + r"(?P<plim_thres>\d+)%, Buff-size: +(?P<buffer_size>\d+)\), +XON_THRES: +(?P<xon_thres>\d+)$"
        )

        # LP Queue cos:0 tc:0, config weight: 20, sche Weight: 255
        p16 = re.compile(
            r"^LP Queue cos:+(?P<lp_q_cos>\d+) tc:(?P<lp_q_tc>\d+), config weight: "
            + r"(?P<lp_weight>\d+), sche Weight: (?P<lp_sche_weight>\d+)$"
        )

        # HP Queue cos:4 tc:4, config bw: 100, sche Weight: 255
        p17 = re.compile(
            r"^HP Queue cos:+(?P<hp_q_cos>\d+) tc:(?P<hp_q_tc>\d+), config bw: "
            + r"(?P<hp_bw>\d+), sche Weight: (?P<hp_sche_weight>\d+)$"
        )

        # Port Tx buff: 0
        p18 = re.compile(r"^Port Tx buff: +(?P<port_tx_buffer>\d+)$")

        # Queue 0, tx buff 0
        p19 = re.compile(r"^Queue 0, tx buff +(?P<q0_tx_buffer>\d+)$")

        # Queue 1, tx buff 0
        p20 = re.compile(r"^Queue 1, tx buff +(?P<q1_tx_buffer>\d+)$")

        # Queue 2, tx buff 0
        p21 = re.compile(r"^Queue 2, tx buff +(?P<q2_tx_buffer>\d+)$")

        # Queue 3, tx buff 0
        p22 = re.compile(r"^Queue 3, tx buff +(?P<q3_tx_buffer>\d+)$")

        # Queue 4, tx buff 0
        p23 = re.compile(r"^Queue 4, tx buff +(?P<q4_tx_buffer>\d+)$")

        # Queue 5, tx buff 0
        p24 = re.compile(r"^Queue 5, tx buff +(?P<q5_tx_buffer>\d+)$")

        # Queue 6, tx buff 0
        p25 = re.compile(r"^Queue 6, tx buff +(?P<q6_tx_buffer>\d+)$")

        # Queue 7, tx buff 0
        p26 = re.compile(r"^Queue 7, tx buff +(?P<q7_tx_buffer>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # MAC Status: hw_port 0, speed 1000, duplex full, link Up, link_en Enable , tx_pause Enable, rx_pause Enable
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                dir_dict = ret_dict.setdefault("mac_status", {})
                dir_dict.update(
                    {
                        "hw_port": int(groups["hw_port"]),
                        "speed": int(groups["speed"]),
                        "duplex": groups["duplex"],
                        "link": groups["link"],
                        "link_en": groups["link_en"],
                        "tx_pause": groups["tx_pause"],
                        "rx_pause": groups["rx_pause"],
                    }
                )
                continue

            # link Up(config Enable), speed 1000(config 1000), duplex full(config full), config force_up, mtu 1526
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                dir_dict = ret_dict.setdefault("l3_network", {})
                dir_dict.update(
                    {
                        "link": groups["link"],
                        "link_config": groups["link_config"],
                        "speed": groups["speed"],
                        "speed_config": groups["speed_config"],
                        "duplex": groups["duplex"],
                        "duplex_config": groups["duplex_config"],
                        "nego_config": groups["nego_config"],
                        "mtu": int(groups["mtu"]),
                    }
                )
                continue

            # rx_pause On(config On), tx_pause On(config On)
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                dir_dict = ret_dict.setdefault("l3_network", {})
                dir_dict.update(
                    {
                        "rx_pause": groups["rx_pause"],
                        "rx_pause_config": groups["rx_pause_config"],
                        "tx_pause": groups["tx_pause"],
                        "tx_pause_config": groups["tx_pause_config"],
                    }
                )
                continue

            # mac_filtering: Enable, mac: 0000.0000.0001
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "mac_filtering": groups["mac_filtering"],
                        "mac_addr": groups["mac_addr"],
                    }
                )
                continue

            # PVE :enable, target port: 24, isTrunk:false
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "pve": groups["pve"],
                        "target_port": int(groups["target_port"]),
                        "is_trunk": groups["is_trunk"],
                    }
                )
                continue

            # nested vlan :enable, vlan: 2356
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "nested_vlan": groups["nested_vlan"],
                        "nested_vid": int(groups["nested_vid"]),
                    }
                )
                continue

            # tail-drop profile 0, sche_profile 2
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "td_profile": int(groups["td_profile"]),
                        "sche_profile": int(groups["sche_profile"]),
                    }
                )
                continue

            # default priority 0, UP override True
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "default_pri": int(groups["default_pri"]),
                        "up_override": groups["up_override"],
                    }
                )
                continue

            # None Trust mode
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"trust_mode": groups["trust_mode"]})
                continue

            # Exp Enable
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"exp": groups["exp"]})
                continue

            # cos_bit_vec: 0x00, exp_bit_vec: 0xc0, dscp_bit_vec: 0x0000000000000000
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "cos_bit": groups["cos_bit"],
                        "exp_bit": groups["exp_bit"],
                        "dscp_bit": groups["dscp_bit"],
                    }
                )
                continue

            # LP Qos Profile: 104, Cos: 0, TC: 0.
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "lp_profile": int(groups["lp_profile"]),
                        "lp_cos": int(groups["lp_cos"]),
                        "lp_tc": int(groups["lp_tc"]),
                    }
                )
                continue

            # HP Qos Profile: 105, Cos: 4, TC: 4.
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "hp_profile": int(groups["hp_profile"]),
                        "hp_cos": int(groups["hp_cos"]),
                        "hp_tc": int(groups["hp_tc"]),
                    }
                )
                continue

            # SP Tx Queue: 7.
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"tx_queue": int(groups["tx_queue"])})
                continue

            # TX_PAUSE: disabled XOFF_THRES: 1024(plim threshold 99%, Buff-size: 1024),   XON_THRES: 128
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "tx_pause_xoff": groups["tx_pause_xoff"],
                        "xoff_thres": int(groups["xoff_thres"]),
                        "plim_thres": int(groups["plim_thres"]),
                        "buffer_size": int(groups["buffer_size"]),
                        "xon_thres": int(groups["xon_thres"]),
                    }
                )
                continue

            # LP Queue cos:0 tc:0, config weight: 20, sche Weight: 255
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "lp_q_cos": int(groups["lp_q_cos"]),
                        "lp_q_tc": int(groups["lp_q_tc"]),
                        "lp_weight": int(groups["lp_weight"]),
                        "lp_sche_weight": int(groups["lp_sche_weight"]),
                    }
                )
                continue

            # HP Queue cos:4 tc:4, config bw: 100, sche Weight: 255
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "hp_q_cos": int(groups["hp_q_cos"]),
                        "hp_q_tc": int(groups["hp_q_tc"]),
                        "hp_bw": int(groups["hp_bw"]),
                        "hp_sche_weight": int(groups["hp_sche_weight"]),
                    }
                )
                continue

            # Port Tx buff: 0
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"port_tx_buffer": int(groups["port_tx_buffer"])})
                continue

            # Queue 0, tx buff 0
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"q0_tx_buffer": int(groups["q0_tx_buffer"])})
                continue

            # Queue 1, tx buff 0
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"q1_tx_buffer": int(groups["q1_tx_buffer"])})
                continue

            # Queue 2, tx buff 0
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"q2_tx_buffer": int(groups["q2_tx_buffer"])})
                continue

            # Queue 3, tx buff 0
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"q3_tx_buffer": int(groups["q3_tx_buffer"])})
                continue

                # Queue 4, tx buff 0
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"q4_tx_buffer": int(groups["q4_tx_buffer"])})
                continue

            # Queue 5, tx buff 0
            m = p24.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"q5_tx_buffer": int(groups["q5_tx_buffer"])})
                continue

            # Queue 6, tx buff 0
            m = p25.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"q6_tx_buffer": int(groups["q6_tx_buffer"])})
                continue

            # Queue 7, tx buff 0
            m = p26.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({"q7_tx_buffer": int(groups["q7_tx_buffer"])})
                continue

        return ret_dict


class ShowPlatformHardwareQfpBqsStatisticsChannelAllSchema(MetaParser):
    """Schema for show platform hardware qfp active bqs <x> ipm statistics channel all
    show platform hardware qfp standby bqs <x> ipm statistics channel all
    show platform hardware qfp active bqs <x> opm statistics channel all
    show platform hardware qfp standby bqs <x> opm statistics channel all"""

    schema = {
        "channel": {
            Any(): {
                "goodpkts": str,
                "goodbytes": str,
                "badpkts": str,
                "badbytes": str,
                Optional("comment"): str,
            },
        }
    }


class ShowPlatformHardwareQfpBqsStatisticsChannelAll(
    ShowPlatformHardwareQfpBqsStatisticsChannelAllSchema
):
    """Parser for show platform hardware qfp active bqs <x> ipm statistics channel all
    show platform hardware qfp standby bqs <x> ipm statistics channel all
    show platform hardware qfp active bqs <x> opm statistics channel all
    show platform hardware qfp standby bqs <x> opm statistics channel all"""

    cli_command = (
        "show platform hardware qfp {status} bqs {slot} {iotype} statistics channel all"
    )

    def cli(self, status="active", slot="0", iotype="ipm", output=None):
        if output is None:
            cmd = self.cli_command.format(status=status, slot=slot, iotype=iotype)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Chan   GoodPkts  GoodBytes    BadPkts   BadBytes
        # 1 - 0000000000 0000000000 0000000000 0000000000
        # 2 - 0000c40f64 016a5004b0 0000000000 0000000000
        p1 = re.compile(
            r"^(?P<channel>\d+) +- +(?P<goodpkts>\w+) +(?P<goodbytes>\w+) +(?P<badpkts>\w+) +(?P<badbytes>\w+)$"
        )

        #  0-55: OPM Channels
        # 56-59: Metapacket/Recycle Pools 0-3
        #    60: Reassembled Packets Sent to QED
        p2 = re.compile(r"^(?P<channel>\d+)-?(?P<end_channel>\d+)?: +(?P<comment>.+)$")

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                channel = int(group.pop("channel"))
                chan_dict = ret_dict.setdefault("channel", {}).setdefault(channel, {})
                chan_dict.update({k: v for k, v in group.items()})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                channel = int(group["channel"])
                comment = group["comment"]
                if group["end_channel"]:
                    end_channel = int(group["end_channel"])
                    for i in range(channel, end_channel + 1):
                        ret_dict["channel"][i].update({"comment": comment})
                else:
                    ret_dict["channel"][channel].update({"comment": comment})

                continue

        return ret_dict


class ShowPlatformHardwareQfpBqsMappingSchema(MetaParser):
    """Schema for show platform hardware qfp active bqs <x> ipm mapping
    show platform hardware qfp standby bqs <x> ipm mapping
    show platform hardware qfp active bqs <x> opm mapping
    show platform hardware qfp standby bqs <x> opm mapping"""

    schema = {
        "channel": {
            Any(): {
                Optional("interface"): str,
                "name": str,
                Optional("logical_channel"): int,
                Optional("drain_mode"): bool,
                Optional("port"): int,
                Optional("cfifo"): int,
            },
        }
    }


class ShowPlatformHardwareQfpBqsOpmMapping(ShowPlatformHardwareQfpBqsMappingSchema):
    """Parser for show platform hardware qfp active bqs <x> opm mapping
    show platform hardware qfp standby bqs <x> opm mapping"""

    cli_command = "show platform hardware qfp {status} bqs {slot} opm mapping"

    def cli(self, status, slot, output=None):
        if output is None:
            cmd = self.cli_command.format(status=status, slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Chan     Name                          Interface      LogicalChannel
        #  0       CC0 Low                       SPI0            0
        # 24       Peer-FP Low                   SPI0           24
        # 26       Nitrox Low                    SPI0           26
        # 28       HT Pkt Low                    HT              0
        # 38       HighNormal                    GPM             7
        # 55*      Drain Low                     GPM             0
        # * - indicates the drain mode bit is set for this channel
        p1 = re.compile(
            r"^(?P<number>\d+)(?P<drained>\*)? +(?P<name>[\w\-\s]+)"
            " +(?P<interface>[\w\d]+) +(?P<logical_channel>\d+)$"
        )

        # 32       Unmapped
        p2 = re.compile(r"^(?P<unmapped_number>\d+) +Unmapped$")

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group["interface"]
                number = group["number"]
                if group["drained"]:
                    drained = True
                else:
                    drained = False
                if "channel" not in ret_dict:
                    final_dict = ret_dict.setdefault("channel", {})
                final_dict = ret_dict["channel"].setdefault(number, {})
                final_dict.update({"interface": group["interface"].strip()})
                final_dict.update({"name": group["name"].strip()})
                final_dict.update({"logical_channel": int(group["logical_channel"])})
                final_dict.update({"drain_mode": drained})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group["unmapped_number"]
                if "channel" not in ret_dict:
                    ret_dict.setdefault("channel", {})
                ret_dict["channel"].setdefault(unmapped_number, {})
                ret_dict["channel"][unmapped_number].update({"name": "unmapped"})
                continue

        return ret_dict


class ShowPlatformHardwareQfpBqsIpmMapping(ShowPlatformHardwareQfpBqsMappingSchema):
    """Parser for show platform hardware qfp active bqs <x> ipm mapping
    show platform hardware qfp standby bqs <x> ipm mapping"""

    cli_command = "show platform hardware qfp {status} bqs {slot} ipm mapping"

    def cli(self, status, slot, output=None):
        if output is None:
            cmd = self.cli_command.format(status=status, slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Chan   Name                Interface      Port     CFIFO
        #  1     CC3 Low             SPI0           0        1
        # 13     Peer-FP Low         SPI0          12        3
        # 15     Nitrox Low          SPI0          14        1
        # 17     HT Pkt Low          HT             0        1
        # 21     CC4 Low             SPI0          16        1
        p1 = re.compile(
            r"^(?P<number>\d+) +(?P<name>[\w\-\s]+)"
            " +(?P<interface>[\w\d]+) +(?P<port>\d+)"
            " +(?P<cfifo>\d+)$"
        )

        # 32       Unmapped
        p2 = re.compile(r"^(?P<unmapped_number>\d+) +Unmapped$")

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                number = group["number"]
                final_dict = ret_dict.setdefault("channel", {}).setdefault(number, {})
                final_dict.update({"interface": group["interface"].strip()})
                final_dict.update({"name": group["name"].strip()})
                final_dict.update({"port": int(group["port"])})
                final_dict.update({"cfifo": int(group["cfifo"])})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group["unmapped_number"]
                if "channel" not in ret_dict:
                    ret_dict.setdefault("channel", {})
                ret_dict["channel"].setdefault(unmapped_number, {})
                ret_dict["channel"][unmapped_number].update({"name": "unmapped"})
                continue

        return ret_dict


class ShowPlatformHardwareQfpInterfaceIfnameStatisticsSchema(MetaParser):
    """Schema for show platform hardware qfp active interface if-name <interface> statistics
    show platform hardware qfp standby interface if-name <interface> statistics"""

    schema = {
        "qfp": {
            "active": {
                "interface": {
                    Any(): {
                        Optional("platform_handle"): int,
                        "receive_stats": {
                            Any(): {
                                "packets": int,
                                "octets": int,
                            },
                        },
                        "transmit_stats": {
                            Any(): {
                                "packets": int,
                                "octets": int,
                            },
                        },
                        "ingress_drop_stats": {
                            Optional(Any()): {
                                "packets": int,
                                "octets": int,
                            },
                        },
                        "egress_drop_stats": {
                            Optional(Any()): {
                                "packets": int,
                                "octets": int,
                            },
                        },
                    },
                }
            }
        }
    }


class ShowPlatformHardwareQfpInterfaceIfnameStatistics(
    ShowPlatformHardwareQfpInterfaceIfnameStatisticsSchema
):
    """Parser for show platform hardware qfp active interface if-name <interface> statistics
    show platform hardware qfp standby interface if-name <interface> statistics"""

    cli_command = (
        "show platform hardware qfp {status} interface if-name {interface} statistics"
    )

    def cli(self, status, interface, output=None):
        if output is None:
            cmd = self.cli_command.format(status=status, interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        current_stats = None
        final_dict = {}

        # Platform Handle 7
        p1 = re.compile(r"^Platform +Handle +(?P<platform_handle>\d+)$")

        # Receive Stats                             Packets        Octets
        # Transmit Stats                            Packets        Octets
        # Input Drop Stats                          Packets        Octets
        # Output Drop Stats                         Packets        Octets
        p2 = re.compile(r"^(?P<transmit_receive>[\w\s]+) +Stats +Packets +Octets$")

        #   FragmentedIpv6                             0               0
        #   Other
        p3 = re.compile(
            r"^(?P<stats>[\w\d]+) +(?P<packets>[\w\d]+) +(?P<octets>[\w\d]+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                converted_interface = Common.convert_intf_name(interface)
                final_dict = (
                    ret_dict.setdefault("qfp", {})
                    .setdefault("active", {})
                    .setdefault("interface", {})
                    .setdefault(converted_interface, {})
                )
                final_dict["platform_handle"] = int(group["platform_handle"])
                continue

            m = p2.match(line)
            if m:
                if not final_dict:
                    converted_interface = Common.convert_intf_name(interface)
                    final_dict = (
                        ret_dict.setdefault("qfp", {})
                        .setdefault("active", {})
                        .setdefault("interface", {})
                        .setdefault(converted_interface, {})
                    )

                group = m.groupdict()
                status = group["transmit_receive"]
                if "Receive" in status:
                    current_stats = "receive_stats"
                elif "Transmit" in status:
                    current_stats = "transmit_stats"
                elif "Input Drop" in status:
                    current_stats = "ingress_drop_stats"
                else:
                    current_stats = "egress_drop_stats"

                final_dict.setdefault(current_stats, {})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                stats = group["stats"]
                final_dict[current_stats].setdefault(stats, {})
                final_dict[current_stats][stats]["packets"] = int(group["packets"])
                final_dict[current_stats][stats]["octets"] = int(group["octets"])
                continue

        return ret_dict


class ShowPlatformHardwareQfpStatisticsDropSchema(MetaParser):
    """Schema for show platform hardware qfp active statistics drop
    show platform hardware qfp standby statistics drop"""

    schema = {
        "global_drop_stats": {
            Any(): {
                "packets": int,
                "octets": int,
            },
        }
    }


class ShowPlatformHardwareQfpStatisticsDrop(
    ShowPlatformHardwareQfpStatisticsDropSchema
):
    """Parser for show platform hardware qfp active statistics drop
    show platform hardware qfp standby statistics drop"""

    cli_command = [
        "show platform hardware qfp {status} statistics drop | exclude {exclude}",
        "show platform hardware qfp {status} statistics drop",
    ]

    def cli(self, status="active", exclude=None, output=None):
        if output is None:
            if exclude:
                cmd = self.cli_command[0].format(status=status, exclude=exclude)
            else:
                cmd = self.cli_command[1].format(status=status)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Global Drop Stats                         Packets                  Octets
        # -------------------------------------------------------------------------
        # Ipv4NoAdj                                       7                     296
        # Ipv4NoRoute                                   181                    7964
        p1 = re.compile(
            r"^(?P<global_drop_stats>\w+) +(?P<packets>\d+) +(?P<octets>\d+)$"
        )

        # Global Drop Stats                         Packets        Octets
        # ----------------------------------------------------------------
        #    The Global drop stats were all zero
        p2 = re.compile(r"The Global drop stats were all zero")

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            # Ipv4NoRoute                                   181                    7964
            if m:
                group = m.groupdict()
                global_drop_stats = group.pop("global_drop_stats")
                stats_dict = ret_dict.setdefault("global_drop_stats", {}).setdefault(
                    global_drop_stats, {}
                )
                stats_dict.update({k: int(v) for k, v in group.items()})
                continue
            # The Global drop stats were all zero
            m = p2.match(line)
            if m:
                ret_dict.setdefault("global_drop_stats", {})
                ret_dict["global_drop_stats"] = {"NA": {"packets": 0, "octets": 0}}

        return ret_dict


class ShowPlatformHardwareQfpStatisticsDropClear(
    ShowPlatformHardwareQfpStatisticsDropSchema
):
    """
    Parser for
        show platform hardware qfp active statistics drop clear
        show platform hardware qfp standby statistics drop clear
    """

    cli_command = "show platform hardware qfp {status} statistics drop clear"

    def cli(self, status, output=None):
        if output is None:
            cmd = self.cli_command.format(status=status)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Ipv4NoRoute              181                 7964
        # Note: The command output contains multiple such rows
        #       with different row headers, so we parse the
        #       row header as well
        p1 = re.compile(r"^(?P<drop_reason>\w+)\s+(?P<packets>\d+)\s+(?P<octets>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # Ipv4NoRoute              181                 7964
            # Note: The command output contains multiple such rows
            #       with different row headers, so we parse the
            #       row header as well
            m = p1.match(line)
            if m:
                group = m.groupdict()
                drop_reason = group.pop("drop_reason")
                stats_dict = ret_dict.setdefault("global_drop_stats", {}).setdefault(
                    drop_reason, {}
                )
                stats_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowPlatformHardwareQfpStatisticsDropHistorySchema(MetaParser):
    """Schema for show platform hardware qfp {status} statistics drop history"""

    schema = {
        "stats_cleared": bool,
        Optional("last_clear_time"): {
            "year": int,
            "month": str,
            "day": int,
            "hour": int,
            "minute": int,
            "second": int,
        },
        Optional("last_clear_lapsed_time"): {
            Optional("weeks"): int,
            Optional("days"): int,
            Optional("hours"): int,
            Optional("minutes"): int,
            "seconds": int,
        },
        "drops_seen": bool,
        Optional("drop_history"): {
            Any(): {
                "1m": {
                    "packets": int,
                },
                "5m": {
                    "packets": int,
                },
                "30m": {
                    "packets": int,
                },
                "all": {
                    "packets": int,
                },
            },
        },
    }


class ShowPlatformHardwareQfpStatisticsDropHistory(
    ShowPlatformHardwareQfpStatisticsDropHistorySchema
):
    """
    Parser for
        show platform hardware qfp {status} statistics drop history
    """

    cli_command = "show platform hardware qfp {status} statistics drop history"

    def cli(self, status, output=None):
        if output is None:
            cmd = self.cli_command.format(status=status)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Last clearing of QFP drops statistics : never
        p1_1 = re.compile(r"^Last clearing of QFP drops statistics : never$")

        # Last clearing of QFP drops statistics : Fri Jun  9 04:04:39 2023
        p1_2 = re.compile(
            r"^Last clearing of QFP drops statistics : \w+\s+(?P<month>\w+)"
            r"\s+(?P<day>\d+)\s+(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)"
            r"\s+(?P<year>\d+)$"
        )

        # (3w 2d 5h 10m 42s ago)
        # (2d 5h 10m 42s ago)
        # (5h 10m 42s ago)
        # (10m 42s ago)
        # (42s ago)
        p1_3 = re.compile(
            r"^\(((?P<weeks>\d+)w\s+)?((?P<days>\d+)d\s+)?((?P<hours>\d+)h\s+)?"
            r"((?P<minutes>\d+)m\s+)?(?P<seconds>\d+)s\s+ago\)$"
        )

        # The Global drop stats were all zero
        p2_1 = re.compile(r"^The Global drop stats were all zero$")

        # Ipv4NoAdj     0      199935      299897    299897
        p2_2 = re.compile(
            r"^(?P<reason>\w+)\s+(?P<packets_1m>\d+)\s+(?P<packets_5m>\d+)"
            r"\s+(?P<packets_30m>\d+)\s+(?P<packets_all>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Last clearing of QFP drops statistics : never
            m = p1_1.match(line)
            if m:
                ret_dict["stats_cleared"] = False
                continue

            # Last clearing of QFP drops statistics : Fri Jun  9 04:04:39 2023
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                last_clear_time = {
                    "year": int(group["year"]),
                    "month": group["month"],
                    "day": int(group["day"]),
                    "hour": int(group["hour"]),
                    "minute": int(group["minute"]),
                    "second": int(group["second"]),
                }
                ret_dict.update(
                    {"stats_cleared": True, "last_clear_time": last_clear_time}
                )
                continue

            # (3w 2d 5h 10m 42s ago)
            # (2d 5h 10m 42s ago)
            # (5h 10m 42s ago)
            # (10m 42s ago)
            # (42s ago)
            m = p1_3.match(line)
            if m:
                group = m.groupdict()
                lapsed_time = {}
                if group["weeks"] is not None:
                    lapsed_time["weeks"] = int(group["weeks"])
                if group["days"] is not None:
                    lapsed_time["days"] = int(group["days"])
                if group["hours"] is not None:
                    lapsed_time["hours"] = int(group["hours"])
                if group["minutes"] is not None:
                    lapsed_time["minutes"] = int(group["minutes"])
                lapsed_time["seconds"] = int(group["seconds"])
                ret_dict["last_clear_lapsed_time"] = lapsed_time
                continue

            # The Global drop stats were all zero
            m = p2_1.match(line)
            if m:
                ret_dict["drops_seen"] = False
                continue

            # Ipv4NoAdj     0      199935      299897    299897
            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["drops_seen"] = True
                reason = group["reason"]
                reason_dict = {
                    "1m": {"packets": int(group["packets_1m"])},
                    "5m": {"packets": int(group["packets_5m"])},
                    "30m": {"packets": int(group["packets_30m"])},
                    "all": {"packets": int(group["packets_all"])},
                }
                drop_history_dict = ret_dict.setdefault("drop_history", {})
                drop_history_dict[reason] = reason_dict
                continue

        return ret_dict


class ShowPlatformHardwareQfpStatisticsDropHistoryClear(
    ShowPlatformHardwareQfpStatisticsDropHistorySchema
):
    """
    Parser for
        show platform hardware qfp {status} statistics drop history clear
    """

    cli_command = "show platform hardware qfp {status} statistics drop history clear"

    def cli(self, status, output=None):
        if output is None:
            cmd = self.cli_command.format(status=status)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Last clearing of QFP drops statistics : never
        p1_1 = re.compile(r"^Last clearing of QFP drops statistics : never$")

        # Last clearing of QFP drops statistics : Fri Jun  9 04:04:39 2023
        p1_2 = re.compile(
            r"^Last clearing of QFP drops statistics : \w+\s+(?P<month>\w+)"
            r"\s+(?P<day>\d+)\s+(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)"
            r"\s+(?P<year>\d+)$"
        )

        # (3w 2d 5h 10m 42s ago)
        # (2d 5h 10m 42s ago)
        # (5h 10m 42s ago)
        # (10m 42s ago)
        # (42s ago)
        p1_3 = re.compile(
            r"^\(((?P<weeks>\d+)w\s+)?((?P<days>\d+)d\s+)?((?P<hours>\d+)h\s+)?"
            r"((?P<minutes>\d+)m\s+)?(?P<seconds>\d+)s\s+ago\)$"
        )

        # The Global drop stats were all zero
        p2_1 = re.compile(r"^The Global drop stats were all zero$")

        # Ipv4NoAdj     0      199935      299897    299897
        p2_2 = re.compile(
            r"^(?P<reason>\w+)\s+(?P<packets_1m>\d+)\s+(?P<packets_5m>\d+)"
            r"\s+(?P<packets_30m>\d+)\s+(?P<packets_all>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Last clearing of QFP drops statistics : never
            m = p1_1.match(line)
            if m:
                ret_dict["stats_cleared"] = False
                continue

            # Last clearing of QFP drops statistics : Fri Jun  9 04:04:39 2023
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                last_clear_time = {
                    "year": int(group["year"]),
                    "month": group["month"],
                    "day": int(group["day"]),
                    "hour": int(group["hour"]),
                    "minute": int(group["minute"]),
                    "second": int(group["second"]),
                }
                ret_dict.update(
                    {"stats_cleared": True, "last_clear_time": last_clear_time}
                )
                continue

            # (3w 2d 5h 10m 42s ago)
            # (2d 5h 10m 42s ago)
            # (5h 10m 42s ago)
            # (10m 42s ago)
            # (42s ago)
            m = p1_3.match(line)
            if m:
                group = m.groupdict()
                lapsed_time = {}
                if group["weeks"] is not None:
                    lapsed_time["weeks"] = int(group["weeks"])
                if group["days"] is not None:
                    lapsed_time["days"] = int(group["days"])
                if group["hours"] is not None:
                    lapsed_time["hours"] = int(group["hours"])
                if group["minutes"] is not None:
                    lapsed_time["minutes"] = int(group["minutes"])
                lapsed_time["seconds"] = int(group["seconds"])
                ret_dict["last_clear_lapsed_time"] = lapsed_time
                continue

            # The Global drop stats were all zero
            m = p2_1.match(line)
            if m:
                ret_dict["drops_seen"] = False
                continue

            # Ipv4NoAdj     0      199935      299897    299897
            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["drops_seen"] = True
                reason = group["reason"]
                reason_dict = {
                    "1m": {"packets": int(group["packets_1m"])},
                    "5m": {"packets": int(group["packets_5m"])},
                    "30m": {"packets": int(group["packets_30m"])},
                    "all": {"packets": int(group["packets_all"])},
                }
                drop_history_dict = ret_dict.setdefault("drop_history", {})
                drop_history_dict[reason] = reason_dict
                continue

        return ret_dict


# =======================================================================
# Parser for 'show platform hardware qfp active feature appqoe stats all,
# show platform hardware qfp active feature appqoe stats service-node status up'
# =======================================================================
class ShowPlatformHardwareQfpActiveFeatureAppqoeSchema(MetaParser):
    schema = {
        "feature": {
            Any(): {
                "global": {
                    Optional("ip_non_tcp_pkts"): int,
                    Optional("not_enabled"): int,
                    Optional("cft_handle_pkt"): int,
                    Optional("sdvt_divert_req_fail"): int,
                    Optional("syn_policer_rate"): int,
                    Optional("sn_data_pkts_processed"): int,
                    Optional("appqoe_srv_chain_non_tcp_bypass"): int,
                    Optional("appqoe_srv_chain_frag_bypass"): int,
                    Optional("appqoe_cvla_alloc_failure"): int,
                    Optional("appqoe_srv_chain_sn_unhealthy_bypass"): int,
                    Optional("appqoe_srv_chain_tcp_mid_flow_bypass"): int,
                    Optional("appqoe_lb_without_dre"): int,
                    Optional("appqoe_alloc_empty_ht_entry"): int,
                    Optional("appqoe_bulk_upd_mem_bm_no_sng"): int,
                    Optional("appqoe_srv_chain_transit_dre_bypass"): int,
                    Optional("appqoe_sn_data_pkts_processed"): int,
                    Optional("appqoe_svc_on_appqoe_vpn_drop"): int,
                    Optional("appqoe_sng_not_configured"): int,
                    Optional("appqoe_unknown_tlv_type"): int,
                    Optional("appqoe_sn_data_pkts_dropped"): int,
                    Optional("appqoe_reset_appnav_fo_data"): int,
                    Optional("appqoe_lb_without_caching"): int,
                    "sdvt_global_stats": {
                        Optional("remarking_persistent_for_htx_inj_flows"): int,
                        Optional("appnav_registration"): int,
                        Optional("control_decaps_could_not_find_flow_from_tuple"): int,
                        Optional("control_decaps_couldnt_find_sdvt_cft_fo"): int,
                        Optional("sdvt_decaps_couldnt_find_cft_instance_handle"): int,
                        Optional("exceeded_sdvt_syn_policer_limit"): int,
                        Optional("within_sdvt_syn_policer_limit"): int,
                    },
                },
                Optional("sng"): {
                    Any(): {
                        "sn_index": {
                            Any(): {
                                Optional("ip"): str,
                                Optional("oce_id"): int,
                                Optional("ocev6_id"): int,
                                Optional("del"): int,
                                Optional("key"): str,
                                Optional("id"): int,
                                Optional("ver"): int,
                                Optional("status"): int,
                                Optional("type"): int,
                                Optional("sng"): int,
                                Optional("appnav_stats"): {
                                    Optional("to_sn"): {"packets": int, "bytes": int},
                                    Optional("from_sn"): {"packets": int, "bytes": int},
                                },
                                "sdvt_count_stats": {
                                    Optional("active_connections"): int,
                                    Optional("decaps"): int,
                                    Optional("encaps"): int,
                                    Optional("packets_unmarked_in_ingress"): int,
                                    Optional("expired_connections"): int,
                                    Optional(
                                        "idle_timed_out_persistent_connections"
                                    ): int,
                                    Optional(
                                        "packets_unclassified_by_ingress_policy"
                                    ): int,
                                    Optional("decap_messages"): {
                                        "processed_control_messages": int,
                                        "delete_requests_recieved": int,
                                        "deleted_protocol_decision": int,
                                        Optional(
                                            "connections_passed_through_as_intermediate_node"
                                        ): int,
                                        Optional(
                                            "connections_dreopt_service_is_cleared"
                                        ): int,
                                    },
                                },
                                "sdvt_packet_stats": {
                                    Optional("divert"): {"packets": int, "bytes": int},
                                    Optional("reinject"): {
                                        "packets": int,
                                        "bytes": int,
                                    },
                                },
                                Optional(
                                    "sdvt_drop_cause_stats"
                                ): dict,  # This is here because not enough info in output shared
                                Optional(
                                    "sdvt_errors_stats"
                                ): dict,  # This is here because not enough info in output shared
                            }
                        }
                    }
                },
                "sn_index": {
                    Any(): {
                        Optional("ip"): str,
                        Optional("oce_id"): int,
                        Optional("ocev6_id"): int,
                        Optional("del"): int,
                        Optional("key"): str,
                        Optional("id"): int,
                        Optional("ver"): int,
                        Optional("status"): int,
                        Optional("type"): int,
                        Optional("sng"): int,
                        Optional("appnav_stats"): {
                            Optional("to_sn"): {"packets": int, "bytes": int},
                            Optional("from_sn"): {"packets": int, "bytes": int},
                        },
                        "sdvt_count_stats": {
                            Optional("active_connections"): int,
                            Optional("decaps"): int,
                            Optional("encaps"): int,
                            Optional("packets_unmarked_in_ingress"): int,
                            Optional("expired_connections"): int,
                            Optional("packets_unclassified_by_ingress_policy"): int,
                            Optional("idle_timed_out_persistent_connections"): int,
                            Optional("non_syn_divert_requests"): int,
                            Optional("decap_messages"): {
                                "processed_control_messages": int,
                                "delete_requests_recieved": int,
                                "deleted_protocol_decision": int,
                                Optional(
                                    "connections_passed_through_as_intermediate_node"
                                ): int,
                                Optional("connections_dreopt_service_is_cleared"): int,
                            },
                        },
                        "sdvt_packet_stats": {
                            Optional("divert"): {"packets": int, "bytes": int},
                            Optional("reinject"): {"packets": int, "bytes": int},
                        },
                        Optional(
                            "sdvt_drop_cause_stats"
                        ): dict,  # This is here because not enough info in output shared
                        Optional(
                            "sdvt_errors_stats"
                        ): dict,  # This is here because not enough info in output shared
                    }
                },
            }
        }
    }


class ShowPlatformHardwareQfpActiveFeatureAppqoe(
    ShowPlatformHardwareQfpActiveFeatureAppqoeSchema
):
    cli_command = [
        "show platform hardware qfp active feature appqoe stats all",
        "show platform hardware qfp active feature appqoe stats all",
        "show platform hardware qfp active feature appqoe stats sng {sng} all",
    ]

    def cli(self, sng="", output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            if sng:
                output = self.device.execute(self.cli_command[1].format(sng=sng))
            else:
                output = self.device.execute(self.cli_command[0])

        # APPQOE Feature Statistics:
        p1 = re.compile(r"^(?P<feature>\w+) +Feature +Statistics:$")

        # Global:
        p2 = re.compile(r"^Global:$")

        # SDVT Global stats:
        p3 = re.compile(r"^SDVT +Global +stats:$")

        # SN Index [0 (Green)]
        # SN Index [Default]
        p4 = re.compile(r"^SN +Index +\[(?P<index>[\s\S]+)\]$")

        # SNG: 3
        p4_1 = re.compile(r"^SNG: +(?P<sng_index>[\d]+)")

        # SDVT Count stats:
        # SDVT Packet stats:
        # SDVT Drop Cause stats:
        # SDVT Errors stats:
        p5 = re.compile(r"^(?P<sdvt_stats_type>SDVT +[\s\S]+ +stats):$")

        # decaps: Processed control messages from SN: 14200
        # decaps: delete requests received total: 14200
        # decaps: delete - protocol decision: 14200
        p6 = re.compile(r"^decaps: +(?P<decap_type>[\s\S]+): +(?P<value>\d+)$")

        # Divert packets/bytes: 743013/43313261
        # Reinject packets/bytes: 679010/503129551
        p7 = re.compile(
            r"^(?P<type>Divert|Reinject) +packets\/bytes: +(?P<packets>\d+)\/(?P<bytes>\d+)$"
        )

        # Divert packets / bytes 30342 / 23649159
        # Reinject packets / bytes 35694 / 21975547
        p7_1 = re.compile(
            r"^(?P<type>Divert|Reinject) +packets \/ bytes +(?P<packets>\d+) \/ (?P<bytes>\d+)$"
        )

        # ip-non-tcp-pkts: 0
        # not-enabled: 0
        # cft_handle_pkt:  0
        # sdvt_divert_req_fail:  0
        # syn_policer_rate: 800
        p8 = re.compile(r"^(?P<key>[\s\S]+): +(?P<value>\d+)$")

        # SN Index [0 (Green)], IP: 10.136.1.250, oce_id: 1243618816
        p9 = re.compile(
            r"^SN +Index +\[(?P<index>[\s\S]+)\], +IP: +(?P<ip>[\s\S]+), +oce_id: +(?P<oce_id>[\S]+)$"
        )

        # SNG: 3 SN Index [0 (Green)], IP: 10.136.1.250, oce_id: 1243618816
        p9_1 = re.compile(
            r"^SNG: +(?P<sng_index>[\d]+) +SN +Index +\[(?P<index>[\s\S]+)\], +IP: +(?P<ip>[\s\S]+), +oce_id: +(?P<oce_id>[\S]+)$"
        )

        # SNG: 1 SN Index [0 (Green)], IP: 26:126:0:252::1, oce_id: 1099779072, ocev6_id: 1099779136
        p9_2 = re.compile(
            r"^SNG: +(?P<sng_index>[\d]+) +SN +Index +\[(?P<index>[\s\S]+)\], +IP: +(?P<ip>[\s\S]+), +oce_id: +(?P<oce_id>[\s\S]+), +ocev6_id: +(?P<ocev6_id>[\S]+)$"
        )

        # del 0, key 0x0301, id 1, ver 1, status 1, type 3, sng 0
        p10 = re.compile(
            r"^del +(?P<del>[\s\S]+), key +(?P<key>[\s\S]+), id +(?P<id>[\s\S]+), ver +(?P<ver>[\s\S]+), status +(?P<status>[\s\S]+), type +(?P<type>[\s\S]+), sng +(?P<sng>[\S]+)$"
        )

        # APPNAV STATS: toSN 2662751642/2206742552009, fromSN 2715505607/2260448392656
        p11 = re.compile(
            r"^APPNAV STATS: +(?P<to_sn>[\S]+) +(?P<tosn_packets>[\d]+)\/(?P<tosn_bytes>\d+), +(?P<from_sn>[\S]+) +(?P<frmsn_packets>[\d]+)\/(?P<frmsn_bytes>\d+)$"
        )

        # APPNAV STATS: toSN 340233144 / 371163888500 fromSN 282458369 / 207930078958
        p11_1 = re.compile(
            r"^APPNAV STATS: +(?P<to_sn>[\S]+) +(?P<tosn_packets>[\d]+) \/ (?P<tosn_bytes>\d+) +(?P<from_sn>[\S]+) +(?P<frmsn_packets>[\d]+) \/ (?P<frmsn_bytes>\d+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # APPQOE Feature Statistics:
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                feature_name = groups["feature"].lower()
                feature_dict = ret_dict.setdefault("feature", {}).setdefault(
                    feature_name, {}
                )

                last_dict_ptr = feature_dict
                continue

            # Global:
            m = p2.match(line)
            if m:
                global_dict = feature_dict.setdefault("global", {})

                last_dict_ptr = global_dict
                continue

            # SDVT Global stats:
            m = p3.match(line)
            if m:
                sdvt_global_dict = global_dict.setdefault("sdvt_global_stats", {})

                last_dict_ptr = sdvt_global_dict
                continue

            # SN Index [0 (Green)]
            # SN Index [Default]
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                index_dict = feature_dict.setdefault("sn_index", {}).setdefault(
                    groups["index"], {}
                )

                last_dict_ptr = index_dict
                continue

            # SN Index [0 (Green)], IP: 10.136.1.250, oce_id: 1243618816
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                index_dict = feature_dict.setdefault("sn_index", {}).setdefault(
                    groups["index"], {}
                )
                index_dict.update({"ip": groups["ip"]})
                index_dict.update({"oce_id": int(groups["oce_id"])})
                last_dict_ptr = index_dict
                continue

            # SNG: 1 SN Index [0 (Green)], IP: 26:126:0:252::1, oce_id: 1099779072, ocev6_id: 1099779136
            m = p9_2.match(line)
            if m:
                groups = m.groupdict()
                index_dict = (
                    feature_dict.setdefault("sng", {})
                    .setdefault(groups["sng_index"], {})
                    .setdefault("sn_index", {})
                    .setdefault(groups["index"], {})
                )
                index_dict.update({"ip": groups["ip"]})
                index_dict.update({"oce_id": int(groups["oce_id"])})
                index_dict.update({"ocev6_id": int(groups["ocev6_id"])})
                last_dict_ptr = index_dict
                continue

            # SNG: 3 SN Index [0 (Green)], IP: 10.136.1.250, oce_id: 1243618816
            m = p9_1.match(line)
            if m:
                groups = m.groupdict()
                index_dict = (
                    feature_dict.setdefault("sng", {})
                    .setdefault(groups["sng_index"], {})
                    .setdefault("sn_index", {})
                    .setdefault(groups["index"], {})
                )
                index_dict.update({"ip": groups["ip"]})
                index_dict.update({"oce_id": int(groups["oce_id"])})
                last_dict_ptr = index_dict
                continue

            # del 0, key 0x0301, id 1, ver 1, status 1, type 3, sng 0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                index_dict.update({"del": int(groups["del"])})
                index_dict.update({"key": groups["key"]})
                index_dict.update({"id": int(groups["id"])})
                index_dict.update({"ver": int(groups["ver"])})
                index_dict.update({"status": int(groups["status"])})
                index_dict.update({"type": int(groups["type"])})
                index_dict.update({"sng": int(groups["sng"])})

                last_dict_ptr = index_dict
                continue

            # APPNAV STATS: toSN 2662751642/2206742552009, fromSN 2715505607/2260448392656
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                appnav_stats_dict = index_dict.setdefault("appnav_stats", {})
                to_sn_dict = appnav_stats_dict.setdefault("to_sn", {})
                to_sn_dict.update(
                    {
                        "packets": int(groups["tosn_packets"]),
                        "bytes": int(groups["tosn_bytes"]),
                    }
                )
                from_sn_dict = appnav_stats_dict.setdefault("from_sn", {})
                from_sn_dict.update(
                    {
                        "packets": int(groups["frmsn_packets"]),
                        "bytes": int(groups["frmsn_bytes"]),
                    }
                )

                last_dict_ptr = index_dict
                continue

            # APPNAV STATS: toSN 347654410 / 379373842122 fromSN 287567939 / 210800349282
            m = p11_1.match(line)
            if m:
                groups = m.groupdict()
                appnav_stats_dict = index_dict.setdefault("appnav_stats", {})
                to_sn_dict = appnav_stats_dict.setdefault("to_sn", {})
                to_sn_dict.update(
                    {
                        "packets": int(groups["tosn_packets"]),
                        "bytes": int(groups["tosn_bytes"]),
                    }
                )
                from_sn_dict = appnav_stats_dict.setdefault("from_sn", {})
                from_sn_dict.update(
                    {
                        "packets": int(groups["frmsn_packets"]),
                        "bytes": int(groups["frmsn_bytes"]),
                    }
                )

                last_dict_ptr = index_dict
                continue

            # SDVT Count stats
            # SDVT Packet stats
            # SDVT Drop Cause stats
            # SDVT Errors stats
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                sdvt_stats_type = groups["sdvt_stats_type"].replace(" ", "_").lower()
                sdvt_stats_type_dict = index_dict.setdefault(sdvt_stats_type, {})

                last_dict_ptr = sdvt_stats_type_dict
                continue

            # decaps: Processed control messages from SN: 14200
            # decaps: delete requests received total: 14200
            # decaps: delete - protocol decision: 14200
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                decap_messages_dict = sdvt_stats_type_dict.setdefault(
                    "decap_messages", {}
                )

                if "control messages" in groups["decap_type"]:
                    decap_messages_dict.update(
                        {"processed_control_messages": int(groups["value"])}
                    )

                elif "delete requests" in groups["decap_type"]:
                    decap_messages_dict.update(
                        {"delete_requests_recieved": int(groups["value"])}
                    )

                elif "protocol decision" in groups["decap_type"]:
                    decap_messages_dict.update(
                        {"deleted_protocol_decision": int(groups["value"])}
                    )

                last_dict_ptr = decap_messages_dict
                continue

            # Divert packets/bytes: 743013/43313261
            # Reinject packets/bytes: 679010/503129551
            m = p7.match(line)
            if m:
                groups = m.groupdict()

                if "Divert" in groups["type"]:
                    divert_reinject_dict = sdvt_stats_type_dict.setdefault("divert", {})
                elif "Reinject" in groups["type"]:
                    divert_reinject_dict = sdvt_stats_type_dict.setdefault(
                        "reinject", {}
                    )

                divert_reinject_dict.update(
                    {"packets": int(groups["packets"]), "bytes": int(groups["bytes"])}
                )

                last_dict_ptr = divert_reinject_dict
                continue

            # Divert packets / bytes 30342 / 23649159
            # Reinject packets / bytes 282348494 / 186944971512
            m = p7_1.match(line)
            if m:
                groups = m.groupdict()

                if "Divert" in groups["type"]:
                    divert_reinject_dict = sdvt_stats_type_dict.setdefault("divert", {})
                elif "Reinject" in groups["type"]:
                    divert_reinject_dict = sdvt_stats_type_dict.setdefault(
                        "reinject", {}
                    )

                divert_reinject_dict.update(
                    {"packets": int(groups["packets"]), "bytes": int(groups["bytes"])}
                )

                last_dict_ptr = divert_reinject_dict
                continue

            # ip-non-tcp-pkts: 0
            # not-enabled: 0
            # cft_handle_pkt:  0
            # sdvt_divert_req_fail:  0
            # syn_policer_rate: 800
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                key = (
                    groups["key"]
                    .replace("-", "_")
                    .replace(" ", "_")
                    .replace(":", "")
                    .lower()
                )
                last_dict_ptr.update({key: int(groups["value"])})
                continue

        return ret_dict


class ShowPlatformHardwareQfpActiveDatapathUtilSumSchema(MetaParser):
    schema = {
        "cpp": {
            Any(): {
                Any(): {
                    "pps": {"5_secs": int, "1_min": int, "5_min": int, "60_min": int},
                    "bps": {"5_secs": int, "1_min": int, "5_min": int, "60_min": int},
                },
                "processing": {
                    "load_pct": {
                        "5_secs": int,
                        "1_min": int,
                        "5_min": int,
                        "60_min": int,
                    }
                },
                Optional("crypto_io"): {
                    "crypto_load_pct": {
                        "5_secs": int,
                        "1_min": int,
                        "5_min": int,
                        "60_min": int,
                    },
                    "rx_load_pct": {
                        "5_secs": int,
                        "1_min": int,
                        "5_min": int,
                        "60_min": int,
                    },
                    "tx_load_pct": {
                        "5_secs": int,
                        "1_min": int,
                        "5_min": int,
                        "60_min": int,
                    },
                    "idle_pct": {
                        "5_secs": int,
                        "1_min": int,
                        "5_min": int,
                        "60_min": int,
                    },
                },
            }
        }
    }


class ShowPlatformHardwareQfpActiveDatapathUtilSum(
    ShowPlatformHardwareQfpActiveDatapathUtilSumSchema
):
    cli_command = ["show platform hardware qfp active datapath utilization summary"]

    def cli(self, output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command[0])

        # CPP 0:                     5 secs        1 min        5 min       60 min
        p1 = re.compile(
            r"^CPP (?P<cpp_num>\d)\: +(\d\s\S+) +(\d\s\S+) +(\d\s\S+) +(\d+\s\S+)$"
        )
        # Crypto/IO
        p2 = re.compile(r"^Crypto/IO$")
        # Input:     Total (pps)            2            2            1            0
        p3 = re.compile(
            r"^(?P<dir>\w+)\: +\S+ \((?P<type>\S+)\) +(?P<value_5s>\d+) +(?P<value_1m>\d+) +(?P<value_5m>\d+) +(?P<value_60m>\d+)$"
        )
        # (bps)         2928         1856         1056           88
        # Idle (pct)           43           35           35           75
        p4 = re.compile(
            r"^(Idle )?\((?P<type>bps|pct)\) +(?P<value_5s>\d+) +(?P<value_1m>\d+) +(?P<value_5m>\d+) +(?P<value_60m>\d+)$"
        )

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            #   CPP 0:                     5 secs        1 min        5 min       60 min
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                cpp_number = groups["cpp_num"].lower()
                feature_dict = ret_dict.setdefault("cpp", {}).setdefault(cpp_number, {})
                last_dict_ptr = feature_dict
                continue

            # Crypto/IO
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                feature_dict = feature_dict.setdefault("crypto_io", {})
                last_dict_ptr = feature_dict
                continue

            # Input:     Total (pps)            2            2            1            0
            # Processing: Load (pct)            0            0            0            0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                if groups["dir"].strip() in ["Crypto", "RX", "TX", "Idle"]:
                    key = "{a}_load_{b}".format(
                        a=groups["dir"].strip().lower(),
                        b=groups["type"].strip().lower(),
                    )
                    dir_dict = feature_dict.setdefault(key, {})
                    dir_dict.update({"5_secs": int(groups["value_5s"])})
                    dir_dict.update({"1_min": int(groups["value_1m"])})
                    dir_dict.update({"5_min": int(groups["value_5m"])})
                    dir_dict.update({"60_min": int(groups["value_60m"])})
                    last_dict_ptr = dir_dict
                    continue
                else:
                    dir_dict = feature_dict.setdefault(groups["dir"].lower(), {})
                    if "pct" in groups["type"]:
                        key = "load_" + groups["type"]
                    else:
                        key = groups["type"]
                    type_dict = dir_dict.setdefault(key, {})
                    type_dict.update({"5_secs": int(groups["value_5s"])})
                    type_dict.update({"1_min": int(groups["value_1m"])})
                    type_dict.update({"5_min": int(groups["value_5m"])})
                    type_dict.update({"60_min": int(groups["value_60m"])})
                    last_dict_ptr = type_dict
                    continue

            # (bps)         2928         1856         1056           88
            # Idle (pct)           43           35           35           75
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                if "pct" in groups["type"]:
                    key = "idle_{t}".format(t=groups["type"])
                    type_dict = feature_dict.setdefault(key, {})
                    type_dict.update({"5_secs": int(groups["value_5s"])})
                    type_dict.update({"1_min": int(groups["value_1m"])})
                    type_dict.update({"5_min": int(groups["value_5m"])})
                    type_dict.update({"60_min": int(groups["value_60m"])})
                    last_dict_ptr = type_dict
                else:
                    type_dict = dir_dict.setdefault(groups["type"], {})
                    type_dict.update({"5_secs": int(groups["value_5s"])})
                    type_dict.update({"1_min": int(groups["value_1m"])})
                    type_dict.update({"5_min": int(groups["value_5m"])})
                    type_dict.update({"60_min": int(groups["value_60m"])})
                    last_dict_ptr = type_dict
                    continue

        return ret_dict


# =======================================================================
# Schema for 'show platform hardware qfp active tcam resource-manager usage'
# =======================================================================
class ShowPlatformHardwareQfpActiveTcamResourceManagerUsageSchema(MetaParser):
    schema = {
        "qfp_tcam_usage_information": {
            Any(): {
                "name": str,
                "number_of_cells_per_entry": int,
                Optional("current_80_bit_entries_used"): int,
                Optional("current_160_bits_entries_used"): int,
                Optional("current_320_bits_entries_used"): int,
                "current_used_cell_entries": int,
                "current_free_cell_entries": int,
            },
            "total_tcam_cell_usage_information": {
                "name": str,
                "total_number_of_regions": int,
                "total_tcam_used_cell_entries": int,
                "total_tcam_free_cell_entries": int,
                "threshold_status": str,
            },
        }
    }


# =======================================================================
# Parser for 'show platform hardware qfp active tcam resource-manager usage'
# =======================================================================
class ShowPlatformHardwareQfpActiveTcamResourceManagerUsage(
    ShowPlatformHardwareQfpActiveTcamResourceManagerUsageSchema
):
    cli_command = ["show platform hardware qfp active tcam resource-manager usage"]

    def cli(self, output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command[0])

        # QFP TCAM Usage Information
        p1 = re.compile(r"^(?P<key>QFP TCAM Usage Information)$")

        # 80 Bit Region Information
        # Total TCAM Cell Usage Information
        p2 = re.compile(r"^(?P<num>\d+|Total TCAM)(?P<region>[\s\S]+)$")

        # Name                                : Leaf Region #1
        # Number of cells per entry           : 2
        # Current 160 bits entries used       : 19
        # Current used cell entries           : 38
        # Current free cell entries           : 4058
        p3 = re.compile(r"^(?P<key>[\s\S]+)\:(?P<value>[\s\S]+\S)$")

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # QFP TCAM Usage Information
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key1 = groups["key"].replace(" ", "_").lower()
                feature_dict = ret_dict.setdefault(key1, {})
                continue

            # 80 Bit Region Information
            # Total TCAM Cell Usage Information
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                reg = groups["region"].strip().replace(" ", "_").lower()
                reg_name = groups["num"].replace(" ", "_").lower() + "_" + reg
                region_hash = feature_dict.setdefault(reg_name, {})
                continue

            # Name                                : Leaf Region #1
            # Number of cells per entry           : 2
            # Current 160 bits entries used       : 19
            # Current used cell entries           : 38
            # Current free cell entries           : 4058
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                name = groups["key"].strip().replace(" ", "_").lower()
                val = groups["value"].strip()
                if name not in ["threshold_status", "name"]:
                    val = int(groups["value"])

                region_hash.update({name: val})
                continue

        return ret_dict


# =======================================================================
# Schema for 'show platform hardware throughput crypto'
# =======================================================================
class ShowPlatformHardwareThroughputCryptoSchema(MetaParser):
    schema = {
        "current_configured_crypto_throughput_level": str,
        "current_enforced_crypto_throughput_level": str,
        "default_crypto_throughput_level": str,
        "level": str,
        "reboot": str,
        "crypto_throughput": str,
        Optional("current_boot_level"): str,
    }


# ================================================================
# Parser for 'show platform hardware throughput crypto'
# ================================================================
class ShowPlatformHardwareThroughputCrypto(ShowPlatformHardwareThroughputCryptoSchema):
    """Parser for 'show platform hardware throughput crypto'"""

    cli_command = ["show platform hardware throughput crypto"]

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # Current configured crypto throughput level: T3
        p1 = re.compile(r"^Current configured crypto throughput level: (?P<level>.+)$")

        # Current enforced crypto throughput level: 10G
        p2 = re.compile(r"^Current enforced crypto throughput level: (?P<level>.+)$")

        # Default Crypto throughput level: 2.5G
        p3 = re.compile(r"^Default Crypto throughput level: (?P<level>.+)$")

        # Level is saved, reboot is not required
        p4 = re.compile(r"^Level is (?P<saved>[^,]+), reboot is (?P<reboot>.+)$")

        # Crypto Throughput is not throttled
        p5 = re.compile(r"^Crypto Throughput is (?P<throttled>.+)$")

        # Current boot level is network-premier
        p6 = re.compile(r"^Current boot level is (?P<level>.+)$")

        for line in out.splitlines():
            line = line.strip()
            # Current configured crypto throughput level: T3
            m = p1.match(line)
            if m:
                ret_dict["current_configured_crypto_throughput_level"] = m.groupdict()[
                    "level"
                ]
                continue

            # Current enforced crypto throughput level: 10G
            m = p2.match(line)
            if m:
                ret_dict["current_enforced_crypto_throughput_level"] = m.groupdict()[
                    "level"
                ]
                continue

            # Default Crypto throughput level: 2.5G
            m = p3.match(line)
            if m:
                ret_dict["default_crypto_throughput_level"] = m.groupdict()["level"]
                continue

            # Level is saved, reboot is not required
            m = p4.match(line)
            if m:
                ret_dict["level"] = m.groupdict()["saved"]
                ret_dict["reboot"] = m.groupdict()["reboot"]
                continue

            # Crypto Throughput is not throttled
            m = p5.match(line)
            if m:
                ret_dict["crypto_throughput"] = m.groupdict()["throttled"]
                continue

            # Current boot level is network-premier
            m = p6.match(line)
            if m:
                ret_dict["current_boot_level"] = m.groupdict()["level"]
                continue

        return ret_dict


# ==================================================================================
# Parser for 'show platform hardware qfp active feature sdwan datapath fec global" #
# ==================================================================================
class ShowPlatformHardwareQfpActiveFeatureSdwanDpFecGlobalSchema(MetaParser):
    schema = {
        Any(): {  # FEC Global Info
            "ses_chunk_head": int,
            "pak_chunk_head": int,
            "ses_add": int,
            "ses_del": int,
            "ses_alloc_fail": int,
            "ses_mem_req": int,
            "ses_mem_req_resp": int,
            "ses_mem_ret": int,
            "pkt_alloc": int,
            "pkt_free": int,
            "pkt_alloc_fail": int,
            "pak_mem_req": int,
            "pak_mem_req_resp": int,
            "pak_mem_ret": int,
            "win_seq_err": int,
            "mem_to_pkt_err": int,
            "fec_encap_err": int,
            "fec_decap_err": int,
            "fec_compute_err": int,
            "reconstruct_miss": int,
            "fec_recycle_err": int,
            "data_recycle_err": int,
        }
    }


class ShowPlatformHardwareQfpActiveFeatureSdwanDpFecGlobal(
    ShowPlatformHardwareQfpActiveFeatureSdwanDpFecGlobalSchema
):
    cli_command = "show platform hardware qfp active feature sdwan datapath fec global"

    def cli(self, output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if output is None:
            output = self.device.execute(self.cli_command)

        # FEC Global Info
        p1 = re.compile(r"^(?P<key>[A-Za-z\s]+)$")

        # "ses_chunk_head": int
        # "pak_chunk_head": int
        p2 = re.compile(r"^(?P<key>[a-z\_]+)\s+:\s+(?P<value>[\d\D]+)")

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # FEC Global Info
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = (
                    groups["key"]
                    .replace("-", "_")
                    .replace(" ", "_")
                    .replace(":", "")
                    .lower()
                )
                fec_dict = ret_dict.setdefault(key, {})
                continue
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                key = groups["key"]
                value = int(groups["value"], 16)
                fec_dict.update({key: value})
                continue

        return ret_dict


# ===========================================================================================
# Parser for 'show platform hardware qfp active feature sdwan datapath fec session summary' #
# ===========================================================================================
class ShowPlatformHardwareQfpActiveFeatureSdwanDpFecSessionSummarySchema(MetaParser):
    schema = {
        "tunnel": {
            str: {
                "flags": str,
                "tx_data": int,
                "tx_parity": int,
                "rx_data": int,
                "rx_parity": int,
                "reconstruct": int,
                Optional("tx_rx_wins"): {
                    str: {
                        "win_flags": str,
                        "count": int,
                        "isn": int,
                        "tos": int,
                        "parity_len": int,
                        "fec_len": int,
                        "fec_data": str,
                    }
                },
            }
        }
    }


class ShowPlatformHardwareQfpActiveFeatureSdwanDpFecSessionSummary(
    ShowPlatformHardwareQfpActiveFeatureSdwanDpFecSessionSummarySchema
):
    cli_command = (
        "show platform hardware qfp active feature sdwan datapath fec session summary"
    )

    def cli(self, output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if output is None:
            output = self.device.execute(self.cli_command)

        # 12345     0x123    100        2       200         3          1
        p1 = re.compile(
            r"^(?P<index>[\S]+)\s+(?P<flags>[\S]+)\s+(?P<tx_data>[\d]+)\s+(?P<tx_parity>[\d]+)\s+(?P<rx_data>[\d]+)\s+(?P<rx_parity>[\d]+)\s+(?P<reconstruct>[\d]+)$"
        )

        # 0     0X2     1     219329664 0     92        56        0xC85EAD30
        p2 = re.compile(
            r"^(?P<win_num>[\d]+)\s+(?P<win_flags>[\S]+)\s+(?P<count>[\d]+)\s+(?P<isn>[\d]+)\s+(?P<tos>[\d]+)\s+(?P<parity_len>[\d]+)\s+(?P<fec_len>[\d]+)\s+(?P<fec_data>[\S]+)$"
        )

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # 12345     0x123    100        2       200         3          1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                index_dict = ret_dict.setdefault("tunnel", {}).setdefault(
                    groups["index"], {}
                )
                del groups["index"]
                for key in groups.keys():
                    value = groups[key]
                    # Check is Mandatory as i am iterations through different key/values pairs
                    # of different types.
                    if groups[key].isnumeric():
                        value = int(groups[key])
                    index_dict.update({key: value})
                continue
            # 0     0X2     1     219329664 0     92        56        0xC85EAD30
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                wins_dict = index_dict.setdefault("tx_rx_wins", {})
                win_num_dict = wins_dict.setdefault(groups["win_num"], {})
                del groups["win_num"]
                for key in groups.keys():
                    value = groups[key]
                    # Check is Mandatory as i am iterations through different key/values pairs
                    # of different types.
                    if groups[key].isnumeric():
                        value = int(groups[key])
                    win_num_dict.update({key: value})
                continue

        return ret_dict


# =====================================
# Schema for:
#  * 'show platform hardware authentication status'
# =====================================
class ShowPlatformHardwareAuthenticationStatusSchema(MetaParser):
    """Schema for show platform hardware authentication status."""

    schema = {
        Optional("switch"): {
            int: {
                "mainboard_authentication": str,
                Optional("fru_authentication"): str,
                Optional("stack_cable_a_authentication"): str,
                Optional("stack_cable_b_authentication"): str,
                Optional("stack_adapter_a_authentication"): str,
                Optional("stack_adapter_b_authentication"): str,
            },
        },
        Optional("SUP0 Authentication"): str,
        Optional("Fan Tray Authentication"): str,
        Optional("Line Card:6 Authentication"): str,
        Optional("Line Card:1 Authentication"): str,
        Optional("SUP1 Authentication"): str,
        Optional("Line Card:5 Authentication"): str,
        Optional("Line Card:2 Authentication"): str,
        Optional("Line Card:7 Authentication"): str,
        Optional("Line Card 1 Authentication"): str,
        Optional("Line Card 2 Authentication"): str,
        Optional("Line Card 5 Authentication"): str,
        Optional("Line Card:4 Authentication"): str,
        Optional("Line Card 6 Authentication"): str,
        Optional("Fan Tray 1 Authentication"): str,
        Optional("Chassis Authentication"): str,
        Optional("SSD FRU Authentication"): str,
        Optional("SUP 0 Authentication"): str,
        Optional("SUP 1 Authentication"): str,
    }


# =====================================
# Parser for:
#  * 'show platform hardware authentication status'
# =====================================
class ShowPlatformHardwareAuthenticationStatus(
    ShowPlatformHardwareAuthenticationStatusSchema
):
    """Parser for show platform hardware authentication status"""

    cli_command = "show platform hardware authentication status"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # show platform hardware authentication status
        # SUP 0 Authentication:  pass
        # SUP 1 Authentication:  pass
        # Line Card 1 Authentication:  pass
        # Line Card 2 Authentication:  pass
        # Line Card 5 Authentication:  pass
        # Line Card 6 Authentication:  pass
        # Fan Tray 1 Authentication:  pass
        # Chassis Authentication: pass
        p0 = re.compile(
            "(Line\s+Card |SUP|Line\s+Card:|Fan\s+Tray|Chassis|SSD.+|SUP\s+|Fan\s+Tray )\d*\s*Authentication:\s+(?P<Slot>(pass|Not Available|fail))$"
        )

        # Switch 1:
        p1 = re.compile(r"^Switch\s+(?P<switch>\d+):$")

        # Mainboard Authentication:     Passed
        p2 = re.compile(
            r"^Mainboard Authentication:\s+(?P<mainboard_authentication>\w+(\s\w+)?)$"
        )

        # FRU Authentication:           Not Available
        p3 = re.compile(r"^FRU Authentication:\s+(?P<fru_authentication>\w+(\s\w+)?)$")

        # Stack Cable A Authentication: Passed
        p4 = re.compile(
            r"^Stack Cable A Authentication:\s+(?P<stack_cable_a_authentication>\w+(\s\w+)?)$"
        )

        # Stack Cable B Authentication: Passed
        p5 = re.compile(
            r"^Stack Cable B Authentication:\s+(?P<stack_cable_b_authentication>\w+(\s\w+)?)$"
        )

        # Stack Adapter A Authentication Passed
        p6 = re.compile(
            r"^Stack Adapter A (Authentication:|Authenticatio)\s+(?P<stack_adapter_a_authentication>[\s\w]+)$"
        )

        # Stack Adapter B Authentication Passed
        p7 = re.compile(
            r"^Stack Adapter B (Authentication:|Authenticatio)\s+(?P<stack_adapter_b_authentication>[\s\w]+)$"
        )

        for line in output.splitlines():
            Auth = []
            line = line.strip()
            Auth = line.split(": ")

            # show platform hardware authentication status
            # SUP 0 Authentication:  pass
            # SUP 1 Authentication:  pass
            # Line Card 1 Authentication:  pass
            # Line Card 2 Authentication:  pass
            # Line Card 5 Authentication:  pass
            # Line Card 6 Authentication:  pass
            # Fan Tray 1 Authentication:  pass
            # Chassis Authentication: pass
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict[Auth[0]] = group["Slot"]
                continue

            # Switch:1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group["switch"]
                switch_dict = ret_dict.setdefault("switch", {})
                switch_id_dict = switch_dict.setdefault(int(switch), {})
                continue

            # Mainboard Authentication:     Passed
            m = p2.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict["mainboard_authentication"] = group[
                    "mainboard_authentication"
                ]
                continue

            # FRU Authentication:           Not Available
            m = p3.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict["fru_authentication"] = group["fru_authentication"]
                continue

            # Stack Cable A Authentication: Passed
            m = p4.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict["stack_cable_a_authentication"] = group[
                    "stack_cable_a_authentication"
                ]
                continue

            # Stack Cable B Authentication: Passed
            m = p5.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict["stack_cable_b_authentication"] = group[
                    "stack_cable_b_authentication"
                ]
                continue

            # Stack Adapter A Authentication Passed
            m = p6.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict["stack_adapter_a_authentication"] = group[
                    "stack_adapter_a_authentication"
                ]
                continue

            # Stack Adapter B Authentication Passed
            m = p7.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict["stack_adapter_b_authentication"] = group[
                    "stack_adapter_b_authentication"
                ]
                continue

        return ret_dict


class ShowPlatformHardwareChassisFantrayDetailSwitchSchema(MetaParser):
    """
    Schema for show platform hardware chassis fantray detail switch {mode}
    """

    schema = {
        "fantray_details": {
            Any(): {"inlet_rpm": int, "outlet_rpm": int, "pwm": str},
        },
    }


class ShowPlatformHardwareChassisFantrayDetailSwitch(
    ShowPlatformHardwareChassisFantrayDetailSwitchSchema
):
    """Parser for show platform hardware chassis fantray detail switch {mode}"""

    cli_command = "show platform hardware chassis fantray detail switch {mode}"

    def cli(self, mode, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # FT1:
        p1 = re.compile("^(?P<fan_tray>.+)\:$")

        # Inlet:8330 RPM, Outlet:10015 RPM, PWM:30%
        p2 = re.compile(
            "^Inlet:(?P<inlet_rpm>\d+) +RPM\, +Outlet:(?P<outlet_rpm>\d+) +RPM\, PWM:(?P<pwm>\d+%)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # FT1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("fantray_details", {}).setdefault(
                    group["fan_tray"], {}
                )
                continue

            # Inlet:8330 RPM, Outlet:10015 RPM, PWM:30%
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict["inlet_rpm"] = int(group["inlet_rpm"])
                root_dict["outlet_rpm"] = int(group["outlet_rpm"])
                root_dict["pwm"] = group["pwm"]
                continue

        return ret_dict


class ShowPlatformHardwareChassisPowerSupplyDetailSwitchAllSchema(MetaParser):
    """
    Schema for show platform hardware chassis power-supply detail switch {mode} all
    """

    schema = {
        "power_supply_details": {
            Any(): {
                "input_voltage_volt": str,
                "output_voltage_volt": str,
                "input_power_watt": str,
                "output_power_watt": str,
                "input_current_amp": str,
                "output_current_amp": str,
                "temperature1_celsius": str,
                "temperature2_celsius": str,
                "temperature3_celsius": str,
                "fan_speed_1_rpm": str,
            },
        },
    }


class ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll(
    ShowPlatformHardwareChassisPowerSupplyDetailSwitchAllSchema
):
    """Parser for show platform hardware chassis power-supply detail switch {mode} all"""

    cli_command = "show platform hardware chassis power-supply detail switch {mode} all"

    def cli(self, mode, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command.format(mode=mode))
        else:
            output = output
        # initial variables
        ret_dict = {}

        # PS1:
        p1 = re.compile("^(?P<power_supply>.+)\:$")

        # Input Voltage   :       121.1250 V
        p2 = re.compile("^Input\s+Voltage\s+:\s+(?P<input_voltage_volt>\d+\.\d+) V$")

        # Output Voltage  :       12.0547 V
        p3 = re.compile("^Output\s+Voltage\s+:\s+(?P<output_voltage_volt>\d+\.\d+) V$")

        # Input Power     :       507.5000 W
        p4 = re.compile("^Input\s+Power\s+:\s+(?P<input_power_watt>\d+\.\d+) W$")

        # Output Power    :       0.0000 W
        p5 = re.compile("^Output\s+Power\s+:\s+(?P<output_power_watt>\d+\.\d+) W$")

        # Input Current   :       0.0000 A
        p6 = re.compile("^Input\s+Current\s+:\s+(?P<input_current_amp>\d+\.\d+) A$")

        # Output Current  :       0.0000 A
        p7 = re.compile("^Output\s+Current\s+:\s+(?P<output_current_amp>\d+\.\d+) A$")

        # Temperature1    :       0.0000 C
        p8 = re.compile("^Temperature1\s+:\s+(?P<temperature1_celsius>\d+\.\d+) C$")

        # Temperature2    :       0.0000 C
        p9 = re.compile("^Temperature2\s+:\s+(?P<temperature2_celsius>\d+\.\d+) C$")

        # Temperature3    :       0.0000 C
        p10 = re.compile("^Temperature3\s+:\s+(?P<temperature3_celsius>\d+\.\d+) C$")

        # Fan Speed 1     :       0.0000 RPM
        p11 = re.compile("^Fan\s+Speed\s+1\s+:\s+(?P<fan_speed_1_rpm>\d+\.\d+) RPM$")

        for line in output.splitlines():
            line = line.strip()

            # PS1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("power_supply_details", {}).setdefault(
                    group["power_supply"], {}
                )
                continue

            # Input Voltage   :       121.1250 V
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict["input_voltage_volt"] = group["input_voltage_volt"]
                continue

            # Output Voltage  :       12.0547 V
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict["output_voltage_volt"] = group["output_voltage_volt"]
                continue

            # Input Power     :       507.5000 W
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict["input_power_watt"] = group["input_power_watt"]
                continue

            # Output Power    :       0.0000 W
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict["output_power_watt"] = group["output_power_watt"]
                continue

            # Input Current   :       4.3359 A
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict["input_current_amp"] = group["input_current_amp"]
                continue

            # Output Current  :      39.5625 A
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict["output_current_amp"] = group["output_current_amp"]
                continue

            # Temperature1    :      38.0000 C
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict["temperature1_celsius"] = group["temperature1_celsius"]
                continue

            # Temperature2    :      62.0000 C
            m = p9.match(line)
            if m:
                group = m.groupdict()
                root_dict["temperature2_celsius"] = group["temperature2_celsius"]
                continue

            # Temperature3    :      55.0000 C
            m = p10.match(line)
            if m:
                group = m.groupdict()
                root_dict["temperature3_celsius"] = group["temperature3_celsius"]
                continue

            # Fan Speed 1     :   11488.0000 RPM
            m = p11.match(line)
            if m:
                group = m.groupdict()
                root_dict["fan_speed_1_rpm"] = group["fan_speed_1_rpm"]
                continue

        return ret_dict


class ShowPlatformHardwareQfpIpsecDropSchema(MetaParser):
    """
    Schema for show platform hardware qfp active feature ipsec data drop
    """

    schema = {
        "drops": {
            Any(): {"drop_type": int, "packets": int},
        }
    }


class ShowPlatformHardwareQfpIpsecDrop(ShowPlatformHardwareQfpIpsecDropSchema):
    """Parser for show platform hardware qfp active feature ipsec data drop"""

    cli_command = "show platform hardware qfp active feature ipsec data drop"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # 4  IN_US_V4_PKT_SA_NOT_FOUND_SPI                           67643
        p1 = re.compile(
            r"^(?P<drop_type>\d+).* +(?P<drop_name>[\w\_]+).* +(?P<packets>\d+)$"
        )

        master_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # 4  IN_US_V4_PKT_SA_NOT_FOUND_SPI                           67643
            m = p1.match(line)
            if m:
                group = m.groupdict()
                drop_dict = master_dict.setdefault("drops", {}).setdefault(
                    group["drop_name"], {}
                )
                drop_dict.update(
                    {
                        "drop_type": int(group["drop_type"]),
                        "packets": int(group["packets"]),
                    }
                )
                continue

        return master_dict


class ShowPlatformHardwareVoltageMarginSwitchSchema(MetaParser):
    """
    Schema for show platform hardware voltage margin switch {mode} rp active
    """

    schema = {
        "max_channels": int,
        "channels": {
            Any(): {
                "rail_name": str,
                "voltage_in_mv": float,
                "nominal_voltage": float,
                "min_margin": float,
                "percentage_change": float,
                "max_margin": float,
                "monitor": int,
            },
        },
    }


class ShowPlatformHardwareVoltageMarginSwitch(
    ShowPlatformHardwareVoltageMarginSwitchSchema
):
    """Parser for show platform hardware voltage margin switch {mode} rp active"""

    cli_command = "show platform hardware voltage margin switch {mode} rp active"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # max chnl 36
        p1 = re.compile("^max chnl\s+(?P<max_channels>\d+)$")

        # Channel  Rail Name         Voltage(mv)   Nominal Voltage  Min Margin  % Change  Max Margin  Monitor
        # 0        PVCCKRHV              1315.71        1300.00       -3.00        1.21        3.00       0
        p2 = re.compile(
            "^(?P<channels>\S+)\s+(?P<rail_name>\S+)\s+(?P<voltage_in_mv>[\d+\.]+)\s+(?P<nominal_voltage>[\d+\.]+)\s+(?P<min_margin>\S+)\s+(?P<percentage_change>\S+)\s+(?P<max_margin>\S+)\s+(?P<monitor>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["max_channels"] = int(group["max_channels"])

            # Channel  Rail Name         Voltage(mv)   Nominal Voltage  Min Margin  % Change  Max Margin  Monitor
            # 0        PVCCKRHV              1315.71        1300.00       -3.00        1.21        3.00       0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                channel_dict = ret_dict.setdefault("channels", {}).setdefault(
                    int(group["channels"]), {}
                )
                channel_dict["rail_name"] = group["rail_name"]
                channel_dict["voltage_in_mv"] = float(group["voltage_in_mv"])
                channel_dict["nominal_voltage"] = float(group["nominal_voltage"])
                channel_dict["min_margin"] = float(group["min_margin"])
                channel_dict["percentage_change"] = float(group["percentage_change"])
                channel_dict["max_margin"] = float(group["max_margin"])
                channel_dict["monitor"] = int(group["monitor"])
                continue
        return ret_dict


class ShowPlatformHardwareQfpActiveInfrastructureBqsStatusSchema(MetaParser):

    """
    Schema for show platform hardware qfp active infrastructure bqs status | include QOS|QFP
    """

    schema = {
        Any(): {
            Optional("total_qos_queue"): int,
            Optional("total_qos_schedule_nodes"): int,
        }
    }


class ShowPlatformHardwareQfpActiveInfrastructureBqsStatus(
    ShowPlatformHardwareQfpActiveInfrastructureBqsStatusSchema
):

    """Parser for show platform hardware qfp active infrastructure bqs status | include QOS|QFP"""

    cli_command = [
        "show platform hardware qfp active infrastructure bqs status | include QOS|QFP"
    ]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Initializes the Python dictionary variable
        parsed_dict = {}

        # QFP.0:
        p1 = re.compile(r"(?P<qfp_key>QFP\.\d+)")

        # # of QOS Queue Objects:                   1
        p2 = re.compile(
            r"^\#\s+of\s+QOS\s+Queue\s+Objects\:\s+(?P<total_qos_queue>\d+)"
        )

        ## of QOS Schedule Objects :               2
        p3 = re.compile(
            r"^\#\s+of\s+QOS\s+Schedule\s+Objects\s+\:\s+(?P<total_qos_schedule_nodes>\d+)"
        )

        key = "global"
        parsed_dict.setdefault(key, {})

        for line in output.splitlines():
            line = line.strip()

            # match QFP values
            m = p1.match(line)
            if m:
                group = m.groupdict()
                key = group["qfp_key"]
                parsed_dict.setdefault(key, {})
                continue

            # match queue
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[key]["total_qos_queue"] = int(group["total_qos_queue"])
                continue

            # match scheduling nodes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict[key]["total_qos_schedule_nodes"] = int(
                    group["total_qos_schedule_nodes"]
                )
                continue

        return parsed_dict


class ShowPlatformHardwareQfpActiveFeatureQosInterfaceHierarchyDetailSchema(MetaParser):

    """
    Schema for show platform hardware qfp active feature qos interface Te0/1/0 hierarchy detail | include subdev
    """

    schema = {Optional("subdev"): int}


class ShowPlatformHardwareQfpActiveFeatureQosInterfaceHierarchyDetail(
    ShowPlatformHardwareQfpActiveFeatureQosInterfaceHierarchyDetailSchema
):

    """
    Parser for show platform hardware qfp active feature qos interface Te0/1/0 hierarchy detail | include subdev
    """

    cli_command = [
        "show platform hardware qfp active feature qos interface {interface} hierarchy detail | include subdev"
    ]

    def cli(self, interface=None, output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command[0].format(interface=interface)
            )

        parsed_dict = {}

        # subdevice_id  : 1
        p1 = re.compile(r"subdevice_id\s+\:\s+(?P<subdev>\d+)")

        for line in output.splitlines():
            line = line.strip()

            # subdevice_id  : 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict["subdev"] = int(group["subdev"])
                continue

        return parsed_dict


# ============================================================================================
# Parser Schema for 'show platform hardware qfp active interface all statistics drop_summary'
# ============================================================================================


class ShowPlatformHardwareQfpActiveInterfaceAllStatisticsDropSummarySchema(MetaParser):
    """Schema for "show platform hardware qfp active interface all statistics drop_summary" """

    schema = {
        "drop_stats_summary": {
            Any(): {"rx_packets": int, "tx_packets": int},
        }
    }


# ======================================================================================
# Parser for 'show platform hardware qfp active interface all statistics drop_summary'
# ======================================================================================


class ShowPlatformHardwareQfpActiveInterfaceAllStatisticsDropSummary(
    ShowPlatformHardwareQfpActiveInterfaceAllStatisticsDropSummarySchema
):
    """parser for "show platform hardware qfp active interface all statistics drop_summary" """

    cli_command = (
        "show platform hardware qfp active interface all statistics drop_summary"
    )

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # GigabitEthernet0/0/0                                 16                   0
        p1 = re.compile(
            r"^(?P<intf_name>[a-zA-Z]+[\d/.]+)\s+(?P<rx_packets>\d+)\s+(?P<tx_packets>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/0                                 16                   0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_name = group.pop("intf_name")
                drop_stats_summary_dict = parsed_dict.setdefault(
                    "drop_stats_summary", {}
                ).setdefault(intf_name, {})

                drop_stats_summary_dict.update({k: int(v) for k, v in group.items()})
                continue

        return parsed_dict


# ==========================================================================================
# Parser Schema for 'show platform hardware qfp active infra punt stat type per | ex _0_'
# ==========================================================================================


class ShowPlatformHardwareQfpActiveInfraPuntStatTypePerSchema(MetaParser):
    """Schema for "show platform hardware qfp {status} statistics drop | exclude _0_" """

    schema = {
        "global_punt_cause": {
            "number_of_punt_causes": int,
            "number_of_inject_causes": int,
            Any(): {
                "counter_id": {
                    Any(): {
                        "cause_name": str,
                        "packet_received": int,
                        "packets_transmitted": int,
                    }
                }
            },
        }
    }


# ================================================================================
# Parser for 'show platform hardware qfp active infra punt stat type per | ex _0_'
# ================================================================================


class ShowPlatformHardwareQfpActiveInfraPuntStatTypePer(
    ShowPlatformHardwareQfpActiveInfraPuntStatTypePerSchema
):
    """parser for "show platform hardware qfp active infra punt stat type per | ex _0_" """

    cli_command = "show platform hardware qfp active infra punt stat type per | ex _0_"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # Number of punt causes =   160
        # Number of inject causes = 56
        p1 = re.compile(r"^(?P<name_of_cause>[A-Za-z ]+)=\s+(?P<no_of_causes>\d+)$")

        # Per Punt Cause Statistics
        # Per Inject Cause Statistics
        p2 = re.compile(r"^(?P<name_of_stats>Per+[A-Za-z ]+)$")

        # 003         Layer2 control and legacy                 3888454               3888454
        p3 = re.compile(
            r"^(?P<counter_id>\d+)\s+(?P<cause_name>([A-Za-z0-9_\/-<->]+ ?){5})\s+(?P<packet_received>\d+)\s+(?P<packets_transmitted>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Number of punt causes =   160
            m = p1.match(line)
            if m:
                group = m.groupdict()
                punt_cause_stats_dict = parsed_dict.setdefault("global_punt_cause", {})
                punt_cause_dict = punt_cause_stats_dict.setdefault(
                    group["name_of_cause"].lower().rstrip().replace(" ", "_"),
                    int(group["no_of_causes"]),
                )
                storage_dict = punt_cause_stats_dict
                continue

            # Per Punt Cause Statistics
            # Per Inject Cause Statistics
            m = p2.match(line)
            if m:
                group = m.groupdict()
                stats_name = group["name_of_stats"].lower().replace(" ", "_")
                stats_dict = storage_dict.setdefault(stats_name, {})
                continue

            # 003         Layer2 control and legacy                 3888454               3888454
            m = p3.match(line)
            if m:
                group = m.groupdict()
                counter_id = int(group.pop("counter_id"))
                name = (group.pop("cause_name")).rstrip().lower()
                punt_cause_dict = stats_dict.setdefault("counter_id", {}).setdefault(
                    counter_id, {}
                )
                punt_cause_dict["cause_name"] = name
                punt_cause_dict.update({k: int(v.rstrip()) for k, v in group.items()})
                continue

        return parsed_dict


# ======================================================================================
# Parser Schema for 'show platform hardware qfp active datapath infra sw-cio'
# ======================================================================================


class ShowPlatformHardwareQfpActiveDatapathInfraSwCioSchema(MetaParser):
    """Schema for "show platform hardware qfp active datapath infra sw-cio" """

    schema = {
        "infra_sw_cio": {
            "credits_usage": {
                "ids": {
                    int: {
                        "port": {
                            Any(): {
                                "wght": {
                                    Any(): {
                                        "global": int,
                                        "wrkr0": int,
                                        "wrkr1": int,
                                        "wrkr2": int,
                                        "wrkr3": int,
                                        "wrkr10": int,
                                        "wrkr11": int,
                                        "total": int,
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "core_utilization": {
                "preceding_secs": float,
                "id": {
                    int: {
                        "pp%": float,
                        "rx%": float,
                        "tm%": float,
                        "coff%": float,
                        "idle%": float,
                    }
                },
            },
        }
    }


# ================================================================================
# Parser for 'show platform hardware qfp active datapath infra sw-cio'
# ================================================================================


class ShowPlatformHardwareQfpActiveDatapathInfraSwCio(
    ShowPlatformHardwareQfpActiveDatapathInfraSwCioSchema
):
    """parser for "show platform hardware qfp active datapath infra sw-cio" """

    cli_command = "show platform hardware qfp active datapath infra sw-cio"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # Credits Usage:
        p1 = re.compile(r"^(?P<credits_usage>Credits\sUsage):$")

        # ID      Port  Wght  Global WRKR0  WRKR1  WRKR2  WRKR3  WRKR10  WRKR11  Total
        # 1      rcl0     4:   4999     0      0      0      0       0     121   5120
        p2 = re.compile(
            r"^(?P<id>\d+)\s+(?P<port>\w+)\s+(?P<wght>\d:+)\s+(?P<global>\d+)\s+(?P<wrkr0>\d+)\s+(?P<wrkr1>\d+)\s+(?P<wrkr2>\d+)\s+(?P<wrkr3>\d+)\s+(?P<wrkr10>\d+)\s+(?P<wrkr11>\d+)\s+(?P<total>\d+)$"
        )

        # Core Utilization over preceding 95292.2911 seconds
        p3 = re.compile(
            r"^Core\sUtilization\sover\spreceding\s(?P<preceding_secs>[0-9.]+)\sseconds$"
        )

        # ID:       0       1       2       3      10      11
        p4 = re.compile(
            r"^ID:\s+(?P<id0>\d+)\s+(?P<id1>\d+)\s+(?P<id2>\d+)\s+(?P<id3>\d+)\s+(?P<id10>\d+)\s+(?P<id11>\d+)$"
        )

        # % PP:    0.10    0.73    0.65    0.11    0.00    0.00
        p5 = re.compile(
            r"^%\sPP:\s+(?P<id0>[0-9.]+)\s+(?P<id1>[0-9.]+)\s+(?P<id2>[0-9.]+)\s+(?P<id3>[0-9.]+)\s+(?P<id10>[0-9.]+)\s+(?P<id11>[0-9.]+)$"
        )

        # % RX:    0.00    0.00    0.00    0.00    0.00    0.89
        p6 = re.compile(
            r"^%\sRX:\s+(?P<id0>[0-9.]+)\s+(?P<id1>[0-9.]+)\s+(?P<id2>[0-9.]+)\s+(?P<id3>[0-9.]+)\s+(?P<id10>[0-9.]+)\s+(?P<id11>[0-9.]+)$"
        )

        # % TM:    0.00    0.00    0.00    0.00    0.78    0.00
        p7 = re.compile(
            r"^%\sTM:\s+(?P<id0>[0-9.]+)\s+(?P<id1>[0-9.]+)\s+(?P<id2>[0-9.]+)\s+(?P<id3>[0-9.]+)\s+(?P<id10>[0-9.]+)\s+(?P<id11>[0-9.]+)$"
        )

        # % COFF:    0.00    0.00    0.00    0.00    0.00    0.00
        p8 = re.compile(
            r"^%\sCOFF:\s+(?P<id0>[0-9.]+)\s+(?P<id1>[0-9.]+)\s+(?P<id2>[0-9.]+)\s+(?P<id3>[0-9.]+)\s+(?P<id10>[0-9.]+)\s+(?P<id11>[0-9.]+)$"
        )

        # % IDLE:   99.90   99.27   99.35   99.89   99.22   99.11
        p9 = re.compile(
            r"^%\sIDLE:\s+(?P<id0>[0-9.]+)\s+(?P<id1>[0-9.]+)\s+(?P<id2>[0-9.]+)\s+(?P<id3>[0-9.]+)\s+(?P<id10>[0-9.]+)\s+(?P<id11>[0-9.]+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Credits Usage:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                infra_sw_cio_dict = parsed_dict.setdefault("infra_sw_cio", {})
                credits_dict = infra_sw_cio_dict.setdefault("credits_usage", {})
                continue

            # ID      Port  Wght  Global WRKR0  WRKR1  WRKR2  WRKR3  WRKR10  WRKR11  Total
            # 1      rcl0     4:   4999     0      0      0      0       0     121   5120
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ids = int(group.pop("id"))
                port = group.pop("port")
                wght = group.pop("wght")
                ids = credits_dict.setdefault("ids", {}).setdefault(ids, {})
                ports = ids.setdefault("port", {}).setdefault(port, {})
                wghts = ports.setdefault("wght", {}).setdefault(wght, {})
                wghts.update({k: int(v) for k, v in group.items()})
                continue

            # Core Utilization over preceding 95292.2911 seconds
            m = p3.match(line)
            if m:
                group = m.groupdict()
                core_utilization_dict = infra_sw_cio_dict.setdefault(
                    "core_utilization", {}
                )
                core_utilization_dict["preceding_secs"] = float(group["preceding_secs"])
                continue

            # ID:       0       1       2       3      10      11
            m = p4.match(line)
            if m:
                group = m.groupdict()
                core_utilization_id_dict = core_utilization_dict.setdefault("id", {})
                ids_list = [int(value) for value in group.values()]
                continue

            # % PP:    0.10    0.73    0.65    0.11    0.00    0.00
            m = p5.match(line)
            if m:
                group = m.groupdict()
                for index, value in enumerate(group.values()):
                    id_dict = core_utilization_id_dict.setdefault(ids_list[index], {})
                    id_dict["pp%"] = float(value)
                continue

            # % RX:    0.00    0.00    0.00    0.00    0.00    0.89
            m = p6.match(line)
            if m:
                group = m.groupdict()
                for index, value in enumerate(group.values()):
                    id_dict = core_utilization_id_dict.setdefault(ids_list[index], {})
                    id_dict["rx%"] = float(value)
                continue

            # % TM:    0.00    0.00    0.00    0.00    0.78    0.00
            m = p7.match(line)
            if m:
                group = m.groupdict()
                for index, value in enumerate(group.values()):
                    id_dict = core_utilization_id_dict.setdefault(ids_list[index], {})
                    id_dict["tm%"] = float(value)
                continue

            # % COFF:    0.00    0.00    0.00    0.00    0.00    0.00
            m = p8.match(line)
            if m:
                group = m.groupdict()
                for index, value in enumerate(group.values()):
                    id_dict = core_utilization_id_dict.setdefault(ids_list[index], {})
                    id_dict["coff%"] = float(value)
                continue

            # % IDLE:   99.90   99.27   99.35   99.89   99.22   99.11
            m = p9.match(line)
            if m:
                group = m.groupdict()
                for index, value in enumerate(group.values()):
                    id_dict = core_utilization_id_dict.setdefault(ids_list[index], {})
                    id_dict["idle%"] = float(value)
                continue

        return parsed_dict


# ======================================================================================
# Parser Schema for 'show platform hardware qfp active datapath infra sw-nic'
# ======================================================================================


class ShowPlatformHardwareQfpActiveDatapathInfraSwNicSchema(MetaParser):
    """Schema for "show platform hardware qfp active datapath infra sw-nic" """

    schema = {
        "infra_sw_nic": {
            "pmd_dict": {
                Any(): {
                    "device": str,
                    "rx": {
                        "rx_pkts": int,
                        "rx_bytes": int,
                        "rx_return": int,
                        "rx_badlen": int,
                        "pkts_burts": int,
                        "cycl_pkt": int,
                        "ext_cycl_pkt": int,
                        "total_ring_read": int,
                        "empty": int,
                    },
                    "tx": {
                        "tx_pkts": int,
                        "tx_bytes": int,
                        Optional("pri_0_pkts"): int,
                        Optional("pri_0_bytes"): int,
                        Optional("pkts_send"): int,
                    },
                    "total": {
                        "total_pkts_send": int,
                        "cycl_pkt": int,
                        "send": int,
                        "send_now": int,
                        "forced": int,
                        "poll": int,
                        "thd_poll": int,
                        "blocked": int,
                        "retries": int,
                        "mbuf_alloc_err": int,
                        "tx_queue_id": {
                            Any(): {"full": int, "current_index": int, "hiwater": int}
                        },
                    },
                }
            }
        }
    }


# ================================================================================
# Parser for 'show platform hardware qfp active datapath infra sw-nic'
# ================================================================================


class ShowPlatformHardwareQfpActiveDatapathInfraSwNic(
    ShowPlatformHardwareQfpActiveDatapathInfraSwNicSchema
):
    """parser for "show platform hardware qfp active datapath infra sw-nic" """

    cli_command = "show platform hardware qfp active datapath infra sw-nic"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # pmd 46813180 device fpe0
        p1 = re.compile(r"^pmd\s+(?P<pmd>\w+)\sdevice\s(?P<device>\w+)$")

        # RX: pkts 15254  bytes 1498020 return 0 badlen 0
        p2 = re.compile(
            r"^RX:\spkts\s(?P<rx_pkts>\d+)\s+bytes\s(?P<rx_bytes>\d+)\sreturn\s(?P<rx_return>\d+)\s+badlen\s(?P<rx_badlen>\d+)$"
        )

        # pkts/burst 1  cycl/pkt 938  ext_cycl/pkt 1390
        p3 = re.compile(
            r"^pkts/burst\s+(?P<pkts_burts>\d+)\s+cycl/pkt\s+(?P<cycl_pkt>\d+)\s+ext_cycl/pkt\s+(?P<ext_cycl_pkt>\d+)$"
        )

        # Total ring read 4322810273, empty 4322795019
        p4 = re.compile(
            r"^Total\s+ring\s+read\s+(?P<total_ring_read>\d+),\s+empty\s+(?P<empty>\d+)$"
        )

        # TX: pkts 2061  bytes 891639
        p5 = re.compile(r"TX:\s+pkts\s+(?P<tx_pkts>\d+)\s+bytes\s+(?P<tx_bytes>\d+)$")

        # pri-0: pkts 2068  bytes 892100
        p6 = re.compile(
            r"^pri-0:\s+pkts\s+(?P<pri_0_pkts>\d+)\s+bytes\s+(?P<pri_0_bytes>\d+)$"
        )

        # pkts/send 1
        p7 = re.compile(r"^pkts/send\s(?P<pkts_send>\d+)$")

        # Total: pkts/send 1  cycl/pkt 1717
        p8 = re.compile(
            r"^Total:\spkts/send\s+(?P<total_pkts_send>\d+)\s+cycl/pkt\s+(?P<cycl_pkt>\d+)$"
        )

        # send 2047  sendnow 0
        p9 = re.compile(r"^send\s(?P<send>\d+)\s+sendnow\s+(?P<send_now>\d+)$")

        # forced 2056  poll 0  thd_poll 0
        p10 = re.compile(
            r"^forced\s+(?P<forced>\d+)\s+poll\s+(?P<poll>\d+)\s+thd_poll\s+(?P<thd_poll>\d+)$"
        )

        # blocked 0  retries 0  mbuf alloc err 0
        p11 = re.compile(
            r"blocked\s+(?P<blocked>\d+)\s+retries\s+(?P<retries>\d+)\s+mbuf\s+alloc\s+err\s+(?P<mbuf_alloc_err>\d+)$"
        )

        # TX Queue 0: full 0  current index 0  hiwater 0
        p12 = re.compile(
            r"TX\s+Queue\s+(?P<tx_queue>\d+):\s+full\s+(?P<full>\d+)\s+current\s+index\s+(?P<current_index>\d+)\s+hiwater\s+(?P<hiwater>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # pmd 46813180 device fpe0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                infra_sw_nic_dict = parsed_dict.setdefault("infra_sw_nic", {})
                pmd_dict = infra_sw_nic_dict.setdefault("pmd_dict", {}).setdefault(
                    group["pmd"], {}
                )
                pmd_dict["device"] = group["device"]
                continue

            # RX: pkts 15254  bytes 1498020 return 0 badlen 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rx_dict = pmd_dict.setdefault("rx", {})
                rx_dict["rx_pkts"] = int(group["rx_pkts"])
                rx_dict["rx_bytes"] = int(group["rx_bytes"])
                rx_dict["rx_return"] = int(group["rx_return"])
                rx_dict["rx_badlen"] = int(group["rx_badlen"])
                continue

            # pkts/burst 1  cycl/pkt 938  ext_cycl/pkt 1390
            m = p3.match(line)
            if m:
                group = m.groupdict()
                rx_dict["pkts_burts"] = int(group["pkts_burts"])
                rx_dict["cycl_pkt"] = int(group["cycl_pkt"])
                rx_dict["ext_cycl_pkt"] = int(group["ext_cycl_pkt"])
                continue

            # Total ring read 4322810273, empty 4322795019
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rx_dict["total_ring_read"] = int(group["total_ring_read"])
                rx_dict["empty"] = int(group["empty"])
                continue

            # TX: pkts 2061  bytes 891639
            m = p5.match(line)
            if m:
                group = m.groupdict()
                tx_dict = pmd_dict.setdefault("tx", {})
                tx_dict["tx_pkts"] = int(group["tx_pkts"])
                tx_dict["tx_bytes"] = int(group["tx_bytes"])
                continue

            # pri-0: pkts 2061  bytes 891639
            m = p6.match(line)
            if m:
                group = m.groupdict()
                tx_dict["pri_0_pkts"] = int(group["pri_0_pkts"])
                tx_dict["pri_0_bytes"] = int(group["pri_0_bytes"])
                continue

            # pkts/send 1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                tx_dict["pkts_send"] = int(group["pkts_send"])
                continue

            # Total: pkts/send 1  cycl/pkt 1717
            m = p8.match(line)
            if m:
                group = m.groupdict()
                total_dict = pmd_dict.setdefault("total", {})
                total_dict["total_pkts_send"] = int(group["total_pkts_send"])
                total_dict["cycl_pkt"] = int(group["cycl_pkt"])
                continue

            # send 2047  sendnow 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                total_dict["send"] = int(group["send"])
                total_dict["send_now"] = int(group["send_now"])
                continue

            # forced 2056  poll 0  thd_poll 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                total_dict["forced"] = int(group["forced"])
                total_dict["poll"] = int(group["poll"])
                total_dict["thd_poll"] = int(group["thd_poll"])
                continue

            # blocked 0  retries 0  mbuf alloc err 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                total_dict["blocked"] = int(group["blocked"])
                total_dict["retries"] = int(group["retries"])
                total_dict["mbuf_alloc_err"] = int(group["mbuf_alloc_err"])
                continue

            # TX Queue 0: full 0  current index 0  hiwater 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                tx_queue_dict = total_dict.setdefault("tx_queue_id", {}).setdefault(
                    int(group["tx_queue"]), {}
                )
                tx_queue_dict["full"] = int(group["full"])
                tx_queue_dict["current_index"] = int(group["current_index"])
                tx_queue_dict["hiwater"] = int(group["hiwater"])
                continue

        return parsed_dict

# ===================================================================
# Parser Schema for 'show platform hardware qfp active system state'
# ===================================================================


class ShowPlatformHardwareQfpActiveSystemStateSchema(MetaParser):
    """Schema for "show platform hardware qfp active system state" """

    schema = {
        "cpp_ha_client_processes": {
            "total_processes": int,
            "registered_process": int,
            "client_processes": {
                "cpp_ha": str,
                "cpp_sp": str,
                "cpp_driver0": str,
                "fman_fp": str,
                "cpp_cp": str,
            },
            "platform_state": {"curr": str, "next": str},
            "ha_state": {
                "cpp": str,
                "dir": str,
                "role_state": {"curr": str, "next": str},
            },
            "client_state": str,
            "image": str,
            "load": {"load_count": int, "time": str},
            "active_threads": str,
            "stuck_threads": str,
            "fault_manager_flag": {
                "ignore_fault": str,
                "ignore_stuck_thread": str,
                "crashdump_in_progress": str,
            },
        }
    }

    
# ======================================================================================
# Parser for 'show platform hardware qfp active system state'
# ======================================================================================


class ShowPlatformHardwareQfpActiveSystemState(
    ShowPlatformHardwareQfpActiveSystemStateSchema
):
    """parser for "show platform hardware qfp active system state" """

    cli_command = "show platform hardware qfp active system state"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # CPP HA client processes registered (5 of 5)
        p1 = re.compile(
            r"^CPP\s+HA\s+client\s+processes\s+registered\s+\((?P<total_processes>\d+)\sof\s(?P<registered_process>\d+)\)$"
        )

        # cpp_ha : Initialized
        p2 = re.compile(r"^cpp_ha\s:\s+(?P<cpp_ha>\w+)$")

        # cpp_sp : Initialized
        p3 = re.compile(r"^cpp_sp\s:\s+(?P<cpp_sp>\w+)$")

        # cpp_driver0 : Initialized
        p4 = re.compile(r"^cpp_driver0\s:\s+(?P<cpp_driver0>\w+)$")

        # FMAN-FP : Initialized
        p5 = re.compile(r"^FMAN-FP\s:\s+(?P<fman_fp>\w+)$")

        # cpp_cp : Initialized
        p6 = re.compile(r"^cpp_cp\s:\s+(?P<cpp_cp>\w+)$")

        # Platform State: curr=ACTIVE_SOLO next=ACTIVE_SOLO
        p7 = re.compile(
            r"^Platform\s+State:\scurr=(?P<curr>[A-Z_]+)\snext=(?P<next>[A-Z_]+)$"
        )

        # HA State: CPP=0 dir=BOTH Role: curr=ACTIVE_SOLO next=ACTIVE_SOLO
        p8 = re.compile(
            r"^HA\sState:\s+CPP=(?P<cpp>\d+)\sdir=(?P<dir>\w+)\sRole:\scurr=(?P<curr>[A-Z_]+)\snext=(?P<next>[A-Z_]+)$"
        )

        # Client State: ENABLE
        p9 = re.compile(r"^Client\s+State:\s+(?P<client_state>\w+)$")

        # Image: /tmp/sw/fp/0/0/fp/mount/usr/cpp/bin/qfp-ucode-radium
        p10 = re.compile(r"^Image:\s+(?P<image>[a-z0-9\/-]+)$")

        # Load Cnt: 1 Time: Jun 23, 2022 07:21:15
        p11 = re.compile(
            r"^Load\s+Cnt:\s+(?P<load_count>\d+)\sTime:\s(?P<time>[A-Za-z0-9 :,]+)$"
        )

        # Active Threads: 0-3,10-11
        p12 = re.compile(r"^Active\s+Threads:\s+(?P<active_threads>[0-9-,]+)$")

        # Stuck Threads: 4-9
        p13 = re.compile(r"^Stuck\s+Threads:\s+(?P<stuck_threads>[0-9-]+)$")

        # ignore_fault:          FALSE
        p14 = re.compile(r"^ignore_fault:\s+(?P<ignore_fault>\w+)$")

        # ignore_stuck_thread:   FALSE
        p15 = re.compile(r"^ignore_stuck_thread:\s+(?P<ignore_stuck_thread>\w+)$")

        # crashdump_in_progress: FALSE
        p16 = re.compile(r"^crashdump_in_progress:\s+(?P<crashdump_in_progress>\w+)$")

        for line in output.splitlines():
            line = line.strip()

            # CPP HA client processes registered (5 of 5)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                cpp_ha_client_processes_dict = parsed_dict.setdefault(
                    "cpp_ha_client_processes", {}
                )
                cpp_ha_client_processes_dict["total_processes"] = int(
                    group["total_processes"]
                )
                cpp_ha_client_processes_dict["registered_process"] = int(
                    group["registered_process"]
                )
                continue

            # cpp_ha : Initialized
            m = p2.match(line)
            if m:
                group = m.groupdict()
                client_processes_dict = cpp_ha_client_processes_dict.setdefault(
                    "client_processes", {}
                )
                client_processes_dict["cpp_ha"] = group["cpp_ha"]
                continue

            # cpp_sp : Initialized
            m = p3.match(line)
            if m:
                group = m.groupdict()
                client_processes_dict["cpp_sp"] = group["cpp_sp"]
                continue

            # cpp_driver0 : Initialized
            m = p4.match(line)
            if m:
                group = m.groupdict()
                client_processes_dict["cpp_driver0"] = group["cpp_driver0"]
                continue

            # FMAN-FP : Initialized
            m = p5.match(line)
            if m:
                group = m.groupdict()
                client_processes_dict["fman_fp"] = group["fman_fp"]
                continue

            # cpp_cp : Initialized
            m = p6.match(line)
            if m:
                group = m.groupdict()
                client_processes_dict["cpp_cp"] = group["cpp_cp"]
                continue

            # Platform State: curr=ACTIVE_SOLO next=ACTIVE_SOLO
            m = p7.match(line)
            if m:
                group = m.groupdict()
                platform_state_dict = cpp_ha_client_processes_dict.setdefault(
                    "platform_state", {}
                )
                platform_state_dict["curr"] = group["curr"]
                platform_state_dict["next"] = group["next"]
                continue

            # HA State: CPP=0 dir=BOTH Role: curr=ACTIVE_SOLO next=ACTIVE_SOLO
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ha_state_dict = cpp_ha_client_processes_dict.setdefault("ha_state", {})
                ha_state_dict["cpp"] = group["cpp"]
                ha_state_dict["dir"] = group["dir"]
                role_state_dict = ha_state_dict.setdefault("role_state", {})
                role_state_dict["curr"] = group["curr"]
                role_state_dict["next"] = group["next"]
                continue

            # Client State: ENABLE
            m = p9.match(line)
            if m:
                group = m.groupdict()
                cpp_ha_client_processes_dict["client_state"] = group["client_state"]
                continue

            # Image: /tmp/sw/fp/0/0/fp/mount/usr/cpp/bin/qfp-ucode-radium
            m = p10.match(line)
            if m:
                group = m.groupdict()
                cpp_ha_client_processes_dict["image"] = group["image"]
                continue

            # Load Cnt: 1 Time: Jun 23, 2022 07:21:15
            m = p11.match(line)
            if m:
                group = m.groupdict()
                load_dict = cpp_ha_client_processes_dict.setdefault("load", {})
                load_dict["load_count"] = int(group["load_count"])
                load_dict["time"] = group["time"]
                continue

            # Active Threads: 0-3,10-11
            m = p12.match(line)
            if m:
                group = m.groupdict()
                cpp_ha_client_processes_dict["active_threads"] = group["active_threads"]
                continue

            # Stuck Threads: 4-9
            m = p13.match(line)
            if m:
                group = m.groupdict()
                cpp_ha_client_processes_dict["stuck_threads"] = group["stuck_threads"]
                continue

            # Fault Manager Flags:
            # ignore_fault:          FALSE
            m = p14.match(line)
            if m:
                group = m.groupdict()
                fault_manager_flag_dict = cpp_ha_client_processes_dict.setdefault(
                    "fault_manager_flag", {}
                )
                fault_manager_flag_dict["ignore_fault"] = group["ignore_fault"]
                continue

            # ignore_stuck_thread:   FALSE
            m = p15.match(line)
            if m:
                group = m.groupdict()
                fault_manager_flag_dict["ignore_stuck_thread"] = group[
                    "ignore_stuck_thread"
                ]
                continue

            # crashdump_in_progress: FALSE
            m = p16.match(line)
            if m:
                group = m.groupdict()
                fault_manager_flag_dict["crashdump_in_progress"] = group[
                    "crashdump_in_progress"
                ]
                continue

        return parsed_dict


# ======================================================================================
# Parser Schema for 'show platform hardware qfp active feature ipsec datapath drops all'
# ======================================================================================


class ShowPlatformHardwareQfpActiveFeatureIpsecDatapathDropsAllSchema(MetaParser):
    """Schema for "show platform hardware qfp active feature ipsec datapath drops all" """

    schema = {"drops": {Any(): {"drop_type": int, "packets": int}}}


# ================================================================================
# Parser for 'show platform hardware qfp active feature ipsec datapath drops all'
# ================================================================================


class ShowPlatformHardwareQfpActiveFeatureIpsecDatapathDropsAll(
    ShowPlatformHardwareQfpActiveFeatureIpsecDatapathDropsAllSchema
):
    """parser for "show platform hardware qfp active feature ipsec datapath drops all" """

    cli_command = "show platform hardware qfp active feature ipsec datapath drops all"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # 1  IN_V4_PKT_HIT_INVALID_SA                                    0                           67643
        p1 = re.compile(
            r"^(?P<drop_type>\d+).* +(?P<drop_name>[\w\_]+).* +(?P<packets>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # 1  IN_V4_PKT_HIT_INVALID_SA                                    0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                drop_dict = ret_dict.setdefault("drops", {}).setdefault(
                    group["drop_name"], {}
                )
                drop_dict.update(
                    {
                        "drop_type": int(group["drop_type"]),
                        "packets": int(group["packets"]),
                    }
                )
                continue

        return ret_dict


# ======================================================================================
# Parser Schema for 'show platform hardware qfp active datapath pmd ifdev'
# ======================================================================================


class ShowPlatformHardwareQfpActiveDatapathPmdIfdevSchema(MetaParser):
    """Schema for "show platform hardware qfp active datapath pmd ifdev" """

    schema = {
        "port": {
            Any(): {
                "port_name": str,
                "state_information": {
                    "bind_name": str,
                    "driver": str,
                    "mac_address": str,
                    "device": str,
                    "cio": {
                        "cio_state": str,
                        "if_type": int,
                        "uidb_index": int,
                        "module_id": int,
                        "flags": str,
                    },
                    "cio_events": {"enable": int, "disable": int},
                    "tx_drain": str,
                    "vdev_pause": str,
                    "admin_state": str,
                    "oper_state": str,
                    "link_state": {"up": int, "down": int},
                    "events": {
                        "remove": int,
                        "reset": int,
                        "link_up": int,
                        "link_down": int,
                        "bond_del": int,
                        "unknown": int,
                    },
                    "vdev_rmv_pendng": int,
                    "attach_attempts": int,
                },
                "attributes": {
                    "reconfigure": str,
                    "rx_offload_crc_strip": str,
                    "rx_offload_vlan_filter": str,
                    "rx_vlan_tag_insert": str,
                    "rx_vlan_tag_swap_": str,
                    "mac_filter_api": str,
                    "mc_promisc": str,
                    "set_mc_addr_api": str,
                    "pause_resume": str,
                },
                "configuration": {
                    "promiscuous": {"admin": str, "override": str, "multicast": str},
                    "mtu_config": {"mtu": int, "cur": int, "min": int, "max": int},
                    "trans_vlan": int,
                    "map_qid_num": int,
                    "map_qid_id": int,
                    "rx_ring_size": int,
                    "tx_ring_size": int,
                    "rx_active_q_num": int,
                    "rx_total_q_num": int,
                    "rx_cio_q_num": int,
                    "rx_desc_num": {"queue_0": int},
                    "tx_q_num": int,
                    "tx_desc_num": {"queue_0": int},
                    "num_vlans": int,
                },
            }
        }
    }


# ================================================================================
# Parser for 'show platform hardware qfp active datapath pmd ifdev'
# ================================================================================


class ShowPlatformHardwareQfpActiveDatapathPmdIfdev(
    ShowPlatformHardwareQfpActiveDatapathPmdIfdevSchema
):
    """parser for "show platform hardware qfp active datapath pmd ifdev" """

    cli_command = "show platform hardware qfp active datapath pmd ifdev"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # Port#0 - Name: fpe0
        p1 = re.compile(
            r"^Port#(?P<port_number>\d+)\s+\-\s+Name:\s+(?P<port_name>\w+)$"
        )

        # Bind name      : 0000:0b:10.0
        p2 = re.compile(r"^Bind\s+name\s+:\s(?P<bind_name>[0-9a-z:.]+)$")

        # Driver         : net_e1000_igb_vf
        p3 = re.compile(r"^Driver\s+:\s+(?P<driver>[0-9a-z_]+)$")

        # MAC Address    : f86b.d9c0.cbe0
        p4 = re.compile(r"MAC\s+Address\s+:\s+(?P<mac_address>([0-9a-fA-F].?){12})$")

        # Device         : RUNNING
        p5 = re.compile(r"^Device\s+:\s+(?P<device>\w+)$")

        # CIO State      : ENABLED, if_type 0, uidb_index 1023, module_id 65535, flags 0x1
        p6 = re.compile(
            r"^CIO\s+State\s+:\s+(?P<cio_state>\w+),\s+if_type\s+(?P<if_type>\d+),\s+uidb_index\s+(?P<uidb_index>\d+),\s+module_id\s+(?P<module_id>\d+),\s+flags\s+(?P<flags>\w+)$"
        )

        # CIO Events     : Enable 2, Disable 1
        p7 = re.compile(
            r"^CIO\s+Events\s+:\s+Enable\s(?P<enable>\d+),\s+Disable\s+(?P<disable>\d+)$"
        )

        # Tx_Drain       : FALSE
        p8 = re.compile(r"^Tx_Drain\s+:\s+(?P<tx_drain>\w+)$")

        # Vdev Pause     : Inactive
        p9 = re.compile(r"^Vdev\s+Pause\s+:\s+(?P<vdev_pause>\w+)$")

        # Admin State    : Up
        p10 = re.compile(r"^Admin\s+State\s+:\s+(?P<admin_state>\w+)$")

        # Oper State     : Up (Up)
        p11 = re.compile(r"^Oper\s+State\s+:\s+(?P<oper_state>\w+\s\(\w+\))$")

        # Link state chg : Up 1, Down 0
        p12 = re.compile(
            r"^Link\s+state\s+chg\s:\sUp\s(?P<up>\d+),\s+Down\s+(?P<down>\d+)$"
        )

        # Events         : Remove 0, Reset 1, Link up 0, Link dn 0
        p13 = re.compile(
            r"^Events\s+:\s+Remove\s+(?P<remove>\d+),\s+Reset\s+(?P<reset>\d+),\s+Link\s+up+\s(?P<link_up>\d+),\s+Link\s+dn\s+(?P<link_down>\d+)$"
        )

        # Events         : Bond del 0, Unknown 0
        p14 = re.compile(
            r"^Events\s+:\s+Bond\s+del\s+(?P<bond_del>\d+),\s+Unknown\s+(?P<unknown>\d+)$"
        )

        # Vdev Rmv Pendng: 0
        p15 = re.compile(r"^Vdev\s+Rmv\s+Pendng:\s+(?P<vdev_rmv_pendng>\d+)$")

        # Attach Attempts: 50
        p16 = re.compile(r"^Attach\s+Attempts:\s+(?P<attach_attempts>\d+)$")

        # Attributes
        # RECONFIGURE_SUPPORTED
        p17 = re.compile(r"^(?P<attribute_name>RECONFIGURE)_(?P<status>[A-Z]+)$")

        # RX_OFFLOAD_CRC_STRIP_SUPPORTED
        p18 = re.compile(
            r"^(?P<attribute_name>RX_OFFLOAD_CRC_STRIP)_(?P<status>[A-Z]+)$"
        )

        # RX_OFFLOAD_VLAN_FILTER_SUPPORTED
        p19 = re.compile(
            r"^(?P<attribute_name>RX_OFFLOAD_VLAN_FILTER)_(?P<status>[A-Z]+)$"
        )

        # RX_VLAN_TAG_INSERT_NEEDED
        p20 = re.compile(r"^(?P<attribute_name>RX_VLAN_TAG_INSERT)_(?P<status>[A-Z]+)$")

        # RX_VLAN_TAG_SWAP_NEEDED
        p21 = re.compile(r"^(?P<attribute_name>RX_VLAN_TAG_SWAP_)(?P<status>[A-Z]+)$")

        # MAC_FILTER_API_SUPPORTED
        p22 = re.compile(r"^(?P<attribute_name>MAC_FILTER_API)_(?P<status>[A-Z]+)$")

        # ALWAYS_MC_PROMISC
        p23 = re.compile(r"^(?P<status>[A-Z]+)_(?P<attribute_name>MC_PROMISC)$")

        # SET_MC_ADDR_API_SUPPORTED
        p24 = re.compile(r"^(?P<attribute_name>SET_MC_ADDR_API)_(?P<status>[A-Z]+)$")

        # PAUSE_RESUME_SUPPORTED
        p25 = re.compile(r"^(?P<attribute_name>PAUSE_RESUME)_(?P<status>[A-Z]+)$")

        # Configuration
        # Promiscuous    : Admin DISABLED, Override DISABLED, Multicast ENABLED
        p26 = re.compile(
            r"^Promiscuous\s+:\s+Admin\s+(?P<admin_status>\w+),\s+Override\s+(?P<override_status>\w+),\s+Multicast\s+(?P<multicast_status>\w+)$"
        )

        # MTU config     : 1526
        p27 = re.compile(r"^MTU\s+config\s+:\s+(?P<mtu>\d+)$")

        # cur/min/max  : 1500/68/65535
        p28 = re.compile(
            r"^cur\/min\/max\s+:\s+(?P<cur>\d+)/(?P<min>\d+)/(?P<max>\d+)$"
        )

        # Trans VLAN     : 0
        p29 = re.compile(r"^Trans\s+VLAN\s+:\s+(?P<trans_vlan>\d+)$")

        # Map QID Num    : 0
        p30 = re.compile(r"^Map\s+QID\s+Num\s+:\s+(?P<map_qid_num>\d+)$")

        # Map QID Id     : 0
        p31 = re.compile(r"^Map\s+QID\s+Id\s+:\s+(?P<map_qid_id>\d+)$")

        # Rx ring size   : 0
        p32 = re.compile(r"^Rx\s+ring\s+size\s+:\s+(?P<rx_ring_size>\d+)$")

        # Tx ring size   : 0
        p33 = re.compile(r"^Tx\s+ring\s+size\s+:\s+(?P<tx_ring_size>\d+)$")

        # Rx Active Q Num: 1
        p34 = re.compile(r"^Rx\s+Active\s+Q\s+Num:\s+(?P<rx_active_q_num>\d+)$")

        # Rx Total Q Num : 1
        p35 = re.compile(r"^Rx\s+Total\s+Q\s+Num\s+:\s+(?P<rx_total_q_num>\d+)$")

        # Rx CIO Q Num   : 1
        p36 = re.compile(r"^Rx\s+CIO\s+Q\s+Num\s+:\s+(?P<rx_cio_q_num>\d+)$")

        # Rx Desc Num
        # Tx Desc Num
        p37 = re.compile(r"^(?P<name>([A-Z][a-z]\s+[A-zZ][a-z]+\s+[A-Z][a-z]+))$")

        # Queue 0      : 1024
        p38 = re.compile(r"^Queue\s+0\s+:\s+(?P<queue0>\d+)$")

        # Tx Q Num       : 1
        p39 = re.compile(r"^Tx\s+Q\s+Num\s+:\s+(?P<tx_q_num>\d+)$")

        # Num VLANs      : 0
        p40 = re.compile(r"^Num\s+VLANs\s+:\s+(?P<num_vlans>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # Port#0 - Name: fpe0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                port_number = group["port_number"]
                port_dict = parsed_dict.setdefault("port", {}).setdefault(
                    port_number, {}
                )
                port_dict["port_name"] = group["port_name"]
                continue

            # State Information
            # Bind name      : 0000:0b:10.0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                state_info_dict = port_dict.setdefault("state_information", {})
                state_info_dict["bind_name"] = group["bind_name"]
                continue

            # Driver         : net_e1000_igb_vf
            m = p3.match(line)
            if m:
                group = m.groupdict()
                state_info_dict["driver"] = group["driver"]
                continue

            # MAC Address    : f86b.d9c0.cbe0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                state_info_dict["mac_address"] = group["mac_address"]
                continue

            # Device         : RUNNING
            m = p5.match(line)
            if m:
                group = m.groupdict()
                state_info_dict["device"] = group["device"]
                continue

            # CIO State      : ENABLED, if_type 0, uidb_index 1023, module_id 65535, flags 0x1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                cio_dict = state_info_dict.setdefault("cio", {})
                cio_dict["cio_state"] = group["cio_state"]
                cio_dict["if_type"] = int(group["if_type"])
                cio_dict["uidb_index"] = int(group["uidb_index"])
                cio_dict["module_id"] = int(group["uidb_index"])
                cio_dict["flags"] = group["flags"]
                continue

            # CIO Events     : Enable 2, Disable 1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                cio_events_dict = state_info_dict.setdefault("cio_events", {})
                cio_events_dict["enable"] = int(group["enable"])
                cio_events_dict["disable"] = int(group["disable"])
                continue

            # Tx_Drain       : FALSE
            m = p8.match(line)
            if m:
                group = m.groupdict()
                state_info_dict["tx_drain"] = group["tx_drain"]
                continue

            # Vdev Pause     : Inactive
            m = p9.match(line)
            if m:
                group = m.groupdict()
                state_info_dict["vdev_pause"] = group["vdev_pause"]
                continue

            # Admin State    : Up
            m = p10.match(line)
            if m:
                group = m.groupdict()
                state_info_dict["admin_state"] = group["admin_state"]
                continue

            # Oper State     : Up (Up)
            m = p11.match(line)
            if m:
                group = m.groupdict()
                state_info_dict["oper_state"] = group["oper_state"]
                continue

            # Link state chg : Up 1, Down 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                link_state_dict = state_info_dict.setdefault("link_state", {})
                link_state_dict["up"] = int(group["up"])
                link_state_dict["down"] = int(group["down"])
                continue

            # Events         : Remove 0, Reset 1, Link up 0, Link dn 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                events_dict = state_info_dict.setdefault("events", {})
                events_dict["remove"] = int(group["remove"])
                events_dict["reset"] = int(group["reset"])
                events_dict["link_up"] = int(group["link_up"])
                events_dict["link_down"] = int(group["link_down"])
                continue

            # Events         : Bond del 0, Unknown 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                events_dict["bond_del"] = int(group["bond_del"])
                events_dict["unknown"] = int(group["unknown"])
                continue

            # Vdev Rmv Pendng: 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                state_info_dict["vdev_rmv_pendng"] = int(group["vdev_rmv_pendng"])
                continue

            # Attach Attempts: 50
            m = p16.match(line)
            if m:
                group = m.groupdict()
                state_info_dict["attach_attempts"] = int(group["attach_attempts"])
                continue

            # Attributes
            # RECONFIGURE_SUPPORTED
            m = p17.match(line)
            if m:
                group = m.groupdict()
                attributes_dict = port_dict.setdefault("attributes", {})
                attributes_dict[group["attribute_name"].lower()] = group[
                    "status"
                ].lower()
                continue

            # RX_OFFLOAD_CRC_STRIP_SUPPORTED
            m = p18.match(line)
            if m:
                group = m.groupdict()
                attributes_dict[group["attribute_name"].lower()] = group[
                    "status"
                ].lower()
                continue

            # RX_OFFLOAD_VLAN_FILTER_SUPPORTED
            m = p19.match(line)
            if m:
                group = m.groupdict()
                attributes_dict[group["attribute_name"].lower()] = group[
                    "status"
                ].lower()
                continue

            # RX_VLAN_TAG_INSERT_NEEDED
            m = p20.match(line)
            if m:
                group = m.groupdict()
                attributes_dict[group["attribute_name"].lower()] = group[
                    "status"
                ].lower()
                continue

            # RX_VLAN_TAG_SWAP_NEEDED
            m = p21.match(line)
            if m:
                group = m.groupdict()
                attributes_dict[group["attribute_name"].lower()] = group[
                    "status"
                ].lower()
                continue

            # MAC_FILTER_API_SUPPORTED
            m = p22.match(line)
            if m:
                group = m.groupdict()
                attributes_dict[group["attribute_name"].lower()] = group[
                    "status"
                ].lower()
                continue

            # ALWAYS_MC_PROMISC
            m = p23.match(line)
            if m:
                group = m.groupdict()
                attributes_dict[group["attribute_name"].lower()] = group[
                    "status"
                ].lower()
                continue

            # SET_MC_ADDR_API_SUPPORTED
            m = p24.match(line)
            if m:
                group = m.groupdict()
                attributes_dict[group["attribute_name"].lower()] = group[
                    "status"
                ].lower()
                continue

            # PAUSE_RESUME_SUPPORTED
            m = p25.match(line)
            if m:
                group = m.groupdict()
                attributes_dict[group["attribute_name"].lower()] = group[
                    "status"
                ].lower()
                continue

            # Configuration
            # Promiscuous    : Admin DISABLED, Override DISABLED, Multicast ENABLED
            m = p26.match(line)
            if m:
                group = m.groupdict()
                configuration_dict = port_dict.setdefault("configuration", {})
                promiscuous_dict = configuration_dict.setdefault("promiscuous", {})
                promiscuous_dict["admin"] = group["admin_status"].lower()
                promiscuous_dict["override"] = group["override_status"].lower()
                promiscuous_dict["multicast"] = group["multicast_status"].lower()
                continue

            # MTU config     : 1526
            m = p27.match(line)
            if m:
                group = m.groupdict()
                mtu_config_dict = configuration_dict.setdefault("mtu_config", {})
                mtu_config_dict["mtu"] = int(group["mtu"])
                continue

            # cur/min/max  : 1500/68/65535
            m = p28.match(line)
            if m:
                group = m.groupdict()
                mtu_config_dict["cur"] = int(group["cur"])
                mtu_config_dict["min"] = int(group["min"])
                mtu_config_dict["max"] = int(group["max"])
                continue

            # Trans VLAN     : 0
            m = p29.match(line)
            if m:
                group = m.groupdict()
                configuration_dict["trans_vlan"] = int(group["trans_vlan"])
                continue

            # Map QID Num    : 0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                configuration_dict["map_qid_num"] = int(group["map_qid_num"])
                continue

            # Map QID Id     : 0
            m = p31.match(line)
            if m:
                group = m.groupdict()
                configuration_dict["map_qid_id"] = int(group["map_qid_id"])
                continue

            # Rx ring size   : 0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                configuration_dict["rx_ring_size"] = int(group["rx_ring_size"])
                continue

            # Tx ring size   : 0
            m = p33.match(line)
            if m:
                group = m.groupdict()
                configuration_dict["tx_ring_size"] = int(group["tx_ring_size"])
                continue

            # Rx Active Q Num: 1
            m = p34.match(line)
            if m:
                group = m.groupdict()
                configuration_dict["rx_active_q_num"] = int(group["rx_active_q_num"])
                continue

            # Rx Total Q Num : 1
            m = p35.match(line)
            if m:
                group = m.groupdict()
                configuration_dict["rx_total_q_num"] = int(group["rx_total_q_num"])
                continue

            # Rx CIO Q Num   : 1
            m = p36.match(line)
            if m:
                group = m.groupdict()
                configuration_dict["rx_cio_q_num"] = int(group["rx_cio_q_num"])
                continue

            # Rx Desc Num
            # Tx Desc Num
            m = p37.match(line)
            if m:
                group = m.groupdict()
                dict_name = (group["name"].lower()).replace(" ", "_")
                configuration_dict.setdefault(dict_name, {})
                continue

            # Queue 0      : 1024
            m = p38.match(line)
            if m:
                group = m.groupdict()
                desc_num_dict = configuration_dict.setdefault(dict_name, {})
                desc_num_dict["queue_0"] = int(group["queue0"])
                continue

            # Tx Q Num       : 1
            m = p39.match(line)
            if m:
                group = m.groupdict()
                configuration_dict["tx_q_num"] = int(group["tx_q_num"])
                continue

            # Num VLANs      : 0
            m = p40.match(line)
            if m:
                group = m.groupdict()
                configuration_dict["num_vlans"] = int(group["num_vlans"])
                continue

        return parsed_dict


# ==========================================================================================
# Parser Schema for 'show platform hardware throughput level'
# ==========================================================================================


class ShowPlatformHardwareThroughputLevelSchema(MetaParser):
    """Schema for "show platform hardware throughput level" """

    schema = {"curr_throughput_level": str}


# ================================================================================
# Parser for 'show platform hardware throughput level'
# ================================================================================


class ShowPlatformHardwareThroughputLevel(ShowPlatformHardwareThroughputLevelSchema):
    """parser for "show platform hardware throughput level" """

    cli_command = "show platform hardware throughput level"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # The current throughput level is unthrottled
        # The current throughput level is 1000000 kb/s
        p1 = re.compile(
            r"^The\s+current\s+throughput\s+level\s+is\s+(?P<curr_throughput_level>[a-z0-9 /]+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # The current throughput level is unthrottled
            # The current throughput level is 1000000 kb/s
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict["curr_throughput_level"] = group["curr_throughput_level"]
                continue

        return parsed_dict


# ==========================================================================================
# Parser Schema for 'show platform hardware qfp active datapath infra sw-distrib'
# ==========================================================================================


class ShowPlatformHardwareQfpActiveInfraDatapathInfraSwDistribSchema(MetaParser):
    """Schema for "show platform hardware qfp active datapath infra sw-distrib" """

    schema = {
        "sw_distrib": {
            "dist_mode": str,
            "inactive_ppes": str,
            "rx_stats": {
                "source_id": {
                    Any(): {
                        "name": str,
                        "pmask": str,
                        "port": {
                            Any(): {
                                "port_name": str,
                                "classifier": str,
                                "credit_error": str,
                                "pp": {
                                    Any(): {
                                        "flushes": str,
                                        "flushed": str,
                                        "spin": str,
                                        "sw_hash": str,
                                        Optional("coff_directed"): str,
                                        "total": str,
                                    }
                                },
                            }
                        },
                    }
                }
            },
        }
    }


# ================================================================================
# Parser for 'show platform hardware qfp active datapath infra sw-distrib'
# ================================================================================


class ShowPlatformHardwareQfpActiveInfraDatapathInfraSwDistrib(
    ShowPlatformHardwareQfpActiveInfraDatapathInfraSwDistribSchema
):
    """parser for "show platform hardware qfp active datapath infra sw-distrib" """

    cli_command = "show platform hardware qfp active datapath infra sw-distrib"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # Dist Mode: NSFBD
        p1 = re.compile(r"^Dist\s+Mode:\s(?P<dist_mode>\w+)$")

        # Inactive PPEs: 4-9
        p2 = re.compile(r"^Inactive\s+PPEs:\s(?P<inactive_ppes>[0-9-]+)$")

        # RX Stats
        p3 = re.compile(r"^(?P<stats>RX Stats)$")

        # Source  0: name   DST, pmask 0x3f0
        p4 = re.compile(
            r"^Source\s+(?P<source_id>\d+):\s+name\s+(?P<name>\w+),\s+pmask\s(?P<pmask>\w+)$"
        )

        # Port  4 (fpe0/GigabitEthernet0/0/0): Classifier: L4TUPLE, Credit Err:  -
        p5 = re.compile(
            r"^Port\s+(?P<port>\d+)\s+(?P<port_name>\([A-Za-z0-9_//)]+):\s+Classifier:\s+(?P<classifier>\w+),\s+Credit\s+Err:\s+(?P<credit_error>\S+)$"
        )

        #                 Flushes         Flushed            Spin         SW Hash   COFF Directed           Total
        # PP  0:           665518          665538               -          665538               -          665538
        p6 = re.compile(
            r"^PP\s+(?P<pp>[0-9-]+):\s+(?P<flushes>[0-9-]+)\s+(?P<flushed>[0-9-]+)\s+(?P<spin>[0-9-]+)\s+(?P<sw_hash>[0-9-]+)\s+(?P<coff_directed>[0-9-]+)\s+(?P<total>[0-9-]+)$"
        )

        #                  Flushes         Flushed            Spin         SW Hash           Total
        # PP  3:           306421          306421               -          306421          306421
        p7 = re.compile(
            r"^PP\s+(?P<pp>[0-9-]+):\s+(?P<flushes>[0-9-]+)\s+(?P<flushed>[0-9-]+)\s+(?P<spin>[0-9-]+)\s+(?P<sw_hash>[0-9-]+)\s+(?P<total>[0-9-]+)$"
        )

        #                 Flushes         Flushed            Spin         SW Hash         Unknown           Total
        # PP  0:           105241          124512               -          124512               -          124512
        p8 = re.compile(
            r"^PP\s+(?P<pp>[0-9-]+):\s+(?P<flushes>[0-9-]+)\s+(?P<flushed>[0-9-]+)\s+(?P<spin>[0-9-]+)\s+(?P<sw_hash>[0-9-]+)\s+(?P<unknown>[0-9-]+)\s+(?P<total>[0-9-]+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Dist Mode: NSFBD
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sw_distrib_dict = parsed_dict.setdefault("sw_distrib", {})
                sw_distrib_dict["dist_mode"] = group["dist_mode"]
                continue

            # Inactive PPEs: 4-9
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sw_distrib_dict["inactive_ppes"] = group["inactive_ppes"]
                continue

            # RX Stats
            m = p3.match(line)
            if m:
                group = m.groupdict()
                stats = (group["stats"].lower()).replace(" ", "_")
                stats_dict = sw_distrib_dict.setdefault(stats, {})
                continue

            # Source  0: name   DST, pmask 0x3f0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                source_id = group.pop("source_id")
                rx_source_dict = stats_dict.setdefault("source_id", {}).setdefault(
                    source_id, {}
                )
                rx_source_dict.update({k: v for k, v in group.items()})
                continue

            # Port  4 (fpe0/GigabitEthernet0/0/0): Classifier: L4TUPLE, Credit Err:  -
            m = p5.match(line)
            if m:
                group = m.groupdict()
                port_id = group.pop("port")
                port_dict = rx_source_dict.setdefault("port", {}).setdefault(
                    port_id, {}
                )
                port_dict.update({k: v for k, v in group.items()})
                continue

            #                 Flushes         Flushed            Spin         SW Hash   COFF Directed           Total
            # PP  0:           665518          665538               -          665538               -          665538
            m = p6.match(line)
            if m:
                group = m.groupdict()
                pp_id = group.pop("pp")
                pp_dict = port_dict.setdefault("pp", {}).setdefault(pp_id, {})
                pp_dict.update({k: v for k, v in group.items()})
                continue

            #                  Flushes         Flushed            Spin         SW Hash           Total
            # PP  3:           306421          306421               -          306421          306421
            m = p7.match(line)
            if m:
                group = m.groupdict()
                pp_id = group.pop("pp")
                pp_dict = port_dict.setdefault("pp", {}).setdefault(pp_id, {})
                pp_dict.update({k: v for k, v in group.items()})
                continue

            #                 Flushes         Flushed            Spin         SW Hash         Unknown           Total
            # PP  0:           105241          124512               -          124512               -          124512
            m = p8.match(line)
            if m:
                group = m.groupdict()
                pp_id = group.pop("pp")
                pp_dict = port_dict.setdefault("pp", {}).setdefault(pp_id, {})
                pp_dict.update({k: v for k, v in group.items()})
                continue

        return parsed_dict


# ======================================================================================
# Parser Schema for 'show platform hardware qfp active infrastructure exmem statistics'
# ======================================================================================


class ShowPlatformHardwareQfpActiveInfrastructureExmemStatisticsSchema(MetaParser):
    """Schema for "show platform hardware qfp active infrastructure exmem statistics" """

    schema = {
        "qfp_exmem_stats": {
            "type": {
                Any(): {
                    "qfp": int,
                    "total": int,
                    "inuse": int,
                    "free": int,
                    "lowest_free_water_mark": int,
                }
            }
        }
    }


# ===============================================================================
# Parser for 'show platform hardware qfp active infrastructure exmem statistics'
# ===============================================================================


class ShowPlatformHardwareQfpActiveInfrastructureExmemStatistics(
    ShowPlatformHardwareQfpActiveInfrastructureExmemStatisticsSchema
):
    """parser for "show platform hardware qfp active infrastructure exmem statistics" """

    cli_command = "show platform hardware qfp active infrastructure exmem statistics"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # Type: Name: DRAM, QFP: 0
        # Type: Name: IRAM, QFP: 0
        # Type: Name: SRAM, QFP: 0
        p1 = re.compile(r"^Type:\sName:\s(?P<type_name>\w+),\sQFP:\s(?P<qfp>\d+)$")

        # Total: 536870912
        p2 = re.compile(r"^Total:\s(?P<total>\d+)$")

        # InUse: 423936
        p3 = re.compile(r"^InUse:\s(?P<inuse>\d+)$")

        # Free: 1673216
        p4 = re.compile(r"^Free:\s(?P<free>\d+)$")

        # Lowest free water mark: 1673216
        p5 = re.compile(
            r"^Lowest\sfree\swater\smark:\s(?P<lowest_free_water_mark>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Type: Name: DRAM, QFP: 0
            # Type: Name: IRAM, QFP: 0
            # Type: Name: SRAM, QFP: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                type_name = group["type_name"].lower()
                qfp_exmem_stats_dict = parsed_dict.setdefault(
                    "qfp_exmem_stats", {}
                ).setdefault("type", {})
                type_dict = qfp_exmem_stats_dict.setdefault(type_name, {})
                type_dict["qfp"] = int(group["qfp"])
                continue

            # Total: 536870912
            m = p2.match(line)
            if m:
                group = m.groupdict()
                type_dict["total"] = int(group["total"])
                continue

            # InUse: 423936
            m = p3.match(line)
            if m:
                group = m.groupdict()
                type_dict["inuse"] = int(group["inuse"])
                continue

            # Free: 1673216
            m = p4.match(line)
            if m:
                group = m.groupdict()
                type_dict["free"] = int(group["free"])
                continue

            # Lowest free water mark: 1673216
            m = p5.match(line)
            if m:
                group = m.groupdict()
                type_dict["lowest_free_water_mark"] = int(
                    group["lowest_free_water_mark"]
                )
                continue

        return parsed_dict


# ================================================================================
# Parser Schema for 'show platform hardware iomd <slot> qos port <no> ingress queue stats'
#                   'show platform hardware iomd switch <switch_no> <slot> qos port <no> ingress queue stats'
# ================================================================================
class ShowPlatformHardwareIomdQosPortIngressQueueStatsSchema(MetaParser):
    """Schema for show platform hardware iomd <slot> qos port <no> ingress queue stats"""

    """
    mac-gen2#show platform hardware iomd 10/0 qos port 1 ingress queue stats
    DATA Port:1 StartingQueue:0  Enqueue Counters
    -------------------------------------------
    Queue Buffers Enqueue-TH0 Enqueue-TH1 Enqueue-TH2
    ----- ------- ----------- ----------- -----------
        0       0           0           0           0
        1     314           0           0  1606072000

    DATA Port:0 Drop Counters
    -------------------------------
    Queue Drop-TH0    Drop-TH1    Drop-TH2    SBufDrop    QebDrop
    ----- ----------- ----------- ----------- ----------- -----------
        0           0           0           0           0           0
        1           0           0  1605942200           0           0

    Note: Queuing stats are in bytes
    """
    schema = {
        "unit": str,
        "data_port": int,
        "startingqueue": int,
        "queue": {
            int: {
                "buffers": int,
                "enqueue_th0": int,
                "enqueue_th1": int,
                "enqueue_th2": int,
                "drop_th0": int,
                "drop_th1": int,
                "drop_th2": int,
                "sbufdrop": int,
                "qebdrop": int,
            }
        },
    }


# ================================================================================
# Parser for 'show platform hardware iomd <slot> qos port <no> ingress queue stats'
#            'show platform hardware iomd switch <switch_no> <slot> qos port <no> ingress queue stats'
# ================================================================================
class ShowPlatformHardwareIomdQosPortIngressQueueStats(
    ShowPlatformHardwareIomdQosPortIngressQueueStatsSchema
):
    """parser for "show platform hardware iomd <slot> qos port <no> ingress queue stats" """

    # i.e. show platform hardware iomd 1/0 qos port 24 ingress queue stats"
    cli_command = [
        "show platform hardware iomd {slot} qos port {port_no} ingress queue stats",
        "show platform hardware iomd switch {switch_no} {slot} qos port {port_no} ingress queue stats",
    ]

    def cli(self, slot, port_no, switch_no=None, output=None):
        if output is None:
            if not switch_no:
                cmd = self.cli_command[0].format(slot=slot, port_no=str(port_no))
            else:
                cmd = self.cli_command[1].format(
                    slot=slot, port_no=str(port_no), switch_no=switch_no
                )
            output = self.device.execute(cmd)

        ret_dict = {}

        """
        DATA Port:1 StartingQueue:0  Enqueue Counters
        """
        p1 = re.compile(
            r"^DATA Port:(?P<port_no>\d+)\s+StartingQueue:(?P<starting>\d+)\s+Enqueue Counters$"
        )

        """
        -------------------------------------------
        Queue Buffers Enqueue-TH0 Enqueue-TH1 Enqueue-TH2
        ----- ------- ----------- ----------- -----------
        0       0           0           0           0
        1     314           0           0  1606072000
        """
        p2 = re.compile(
            r"^(?P<queue>\d+)\s+(?P<buf>\d+)\s+(?P<en_th0>\d+)\s+(?P<en_th1>\d+)\s+(?P<en_th2>\d+)$"
        )

        """
        -------------------------------
        Queue Drop-TH0    Drop-TH1    Drop-TH2    SBufDrop    QebDrop
        ----- ----------- ----------- ----------- ----------- -----------
        0           0           0           0           0           0
        1           0           0  1605942200           0           0
        """
        p3 = re.compile(
            r"^(?P<queue>\d+)\s+(?P<dr_th0>\d+)\s+(?P<dr_th1>\d+)\s+(?P<dr_th2>\d+)\s+(?P<sbuf>\d+)\s+(?P<qeb>\d+)$"
        )

        """
        Note: Queuing stats are in bytes
        """
        p4 = re.compile(r"Note:\s+Queuing stats are in\s+(?P<unit>\S+)$")

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["data_port"] = int(group["port_no"])
                ret_dict["startingqueue"] = int(group["starting"])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("queue", dict())
                queue_no = int(group["queue"])
                ret_dict["queue"].setdefault(queue_no, dict())
                ret_dict["queue"][queue_no]["buffers"] = int(group["buf"])
                ret_dict["queue"][queue_no]["enqueue_th0"] = int(group["en_th0"])
                ret_dict["queue"][queue_no]["enqueue_th1"] = int(group["en_th1"])
                ret_dict["queue"][queue_no]["enqueue_th2"] = int(group["en_th2"])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("queue", dict())
                queue_no = int(group["queue"])
                ret_dict["queue"].setdefault(queue_no, dict())
                ret_dict["queue"][queue_no]["drop_th0"] = int(group["dr_th0"])
                ret_dict["queue"][queue_no]["drop_th1"] = int(group["dr_th1"])
                ret_dict["queue"][queue_no]["drop_th2"] = int(group["dr_th2"])
                ret_dict["queue"][queue_no]["sbufdrop"] = int(group["sbuf"])
                ret_dict["queue"][queue_no]["qebdrop"] = int(group["qeb"])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["unit"] = group["unit"].lower()
                continue

        return ret_dict


# ================================================================================
# Parser Schema for 'show platform hardware iomd <slot> portgroups'
#                   'show platform hardware iomd switch <switch_no> <slot> portgroups'
# ================================================================================
class ShowPlatformHardwareIomdPortgroupsSchema(MetaParser):
    """Schema for show platform hardware iomd <slot> portgroups"""

    """
    mac-gen2#show platform hardware iomd 10/0 portgroups
    Port  Interface                       Status    Interface  Group Max
    Group                                           Bandwith   Bandwidth


    1     TenGigabitEthernet10/0/2        up         10G
    1     TenGigabitEthernet10/0/3        up         10G
    1     TenGigabitEthernet10/0/4        up         10G
    1     TenGigabitEthernet10/0/5        up         10G
    1     TenGigabitEthernet10/0/6        up         10G       60G
    1     TenGigabitEthernet10/0/7        up         10G
    1     TenGigabitEthernet10/0/8        up         10G
    1     TenGigabitEthernet10/0/9        up         10G
    1     TenGigabitEthernet10/0/10       up         10G
    1     TenGigabitEthernet10/0/11       up         10G
    1     TenGigabitEthernet10/0/12       up         10G

    2     TenGigabitEthernet10/0/13       up         10G
    2     TenGigabitEthernet10/0/14       up         10G
    2     TenGigabitEthernet10/0/15       up         10G
    2     TenGigabitEthernet10/0/16       up         10G
    2     TenGigabitEthernet10/0/17       up         10G
    2     TenGigabitEthernet10/0/18       up         10G       60G
    2     TenGigabitEthernet10/0/19       down       10G
    """
    schema = {
        "portgroup": {
            int: {
                "intf": {
                    str: {
                        "status": str,
                        "intf_bw": str,
                        "group_max_bw": str,
                        "portgroup": int,
                    }
                }
            }
        }
    }


# ================================================================================
# Parser for 'show platform hardware iomd <slot> portgroups'
#            'show platform hardware iomd switch <switch_no> <slot> portgroups'
# ================================================================================
class ShowPlatformHardwareIomdPortgroups(ShowPlatformHardwareIomdPortgroupsSchema):
    """Parser for 'show platform hardware iomd <slot> portgroups'"""

    cli_command = [
        "show platform hardware iomd {slot} portgroups",
        "show platform hardware iomd switch {switch_no} {slot} portgroups",
    ]

    def cli(self, slot, switch_no=None, output=None):
        if output is None:
            if not switch_no:
                cmd = self.cli_command[0].format(slot=slot)
            else:
                cmd = self.cli_command[1].format(slot=slot, switch_no=switch_no)
            output = self.device.execute(cmd)

        ret_dict = {}
        group_bw_dict = {}

        # 1     TenGigabitEthernet10/0/18       up         10G       60G
        p1 = re.compile(
            r"^(?P<group>\d+)\s+(?P<intf>\S+)\s+(?P<status>\S+)\s+(?P<intf_bw>\S+)\s+(?P<group_bw>\S+)$"
        )

        # 1     TenGigabitEthernet10/0/1        up         10G
        p1_1 = re.compile(
            r"^(?P<group>\d+)\s+(?P<intf>\S+)\s+(?P<status>\S+)\s+(?P<intf_bw>\S+)$"
        )

        ## Pass1: Get group max bandwidth first
        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                ret_dict.setdefault("portgroup", dict())
                parsed = m.groupdict()
                group_no = int(parsed["group"])
                ret_dict["portgroup"].setdefault(group_no, dict())
                ret_dict["portgroup"][group_no].setdefault("intf", dict())

                intf_dict = dict()
                intf_dict["status"] = parsed["status"].lower()
                intf_dict["intf_bw"] = parsed["intf_bw"]
                intf_dict["group_max_bw"] = parsed["group_bw"]
                intf_dict["portgroup"] = group_no

                intf = parsed["intf"].lower()
                ret_dict["portgroup"][group_no]["intf"][intf] = intf_dict

                # for Pass2
                group_bw_dict[group_no] = parsed["group_bw"]

        ## Pass2:
        for line in output.splitlines():
            line = line.strip()

            m = p1_1.match(line)
            if m:
                ret_dict.setdefault("portgroup", dict())
                parsed = m.groupdict()
                group_no = int(parsed["group"])
                ret_dict["portgroup"].setdefault(group_no, dict())
                ret_dict["portgroup"][group_no].setdefault("intf", dict())

                intf_dict = dict()
                intf_dict["status"] = parsed["status"].lower()
                intf_dict["intf_bw"] = parsed["intf_bw"]
                intf_dict["portgroup"] = group_no
                if group_no in group_bw_dict:  # schema should fail if not found
                    intf_dict["group_max_bw"] = group_bw_dict[group_no]

                intf = parsed["intf"].lower()
                ret_dict["portgroup"][group_no]["intf"][intf] = intf_dict

        return ret_dict


# =============================================================
# Parser for 'show platform hardware crypto-device utilization'
# =============================================================


class ShowPlatformHardwareCryptoDeviceUtilizationSchema(MetaParser):
    """Schema for: show platform hardware crypto-device utilization"""

    schema = {
        "one_min_percent": int,
        "one_min_decrypt_pkt": int,
        "one_min_encrypt_pkt": int,
        "five_min_percent": int,
        "five_min_decrypt_pkt": int,
        "five_min_encrypt_pkt": int,
        "fifteen_min_percent": int,
        "fifteen_min_decrypt_pkt": int,
        "fifteen_min_encrypt_pkt": int,
    }


class ShowPlatformHardwareCryptoDeviceUtilization(
    ShowPlatformHardwareCryptoDeviceUtilizationSchema
):
    """Parser for: show platform hardware crypto-device utilization"""

    cli_command = "show platform hardware crypto-device utilization"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        # 1 min (percentage) : 2%
        # 5 min (percentage) : 2%
        # 15 min (percentage) : 2%
        p1 = re.compile(
            r"^\s*(?P<min_data>\d+) min \(percentage\) \: +(?P<min_percent>.*)\%"
        )

        # (decrypt pkt): 0
        p2 = re.compile(r"^\s*\(decrypt pkt\)\: +(?P<decrypt_pkt>.*)")

        # (encrypt pkt): 0
        p3 = re.compile(r"^\s*\(encrypt pkt\)\: +(?P<encrypt_pkt>.*)")

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # 1 min (percentage) : 2%
            # 5 min (percentage) : 2%
            # 15 min (percentage) : 2%
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                minutes = int(groups["min_data"])
                if minutes == 1:
                    ret_dict["one_min_percent"] = int(groups["min_percent"])
                if minutes == 5:
                    ret_dict["five_min_percent"] = int(groups["min_percent"])
                if minutes == 15:
                    ret_dict["fifteen_min_percent"] = int(groups["min_percent"])
                continue

            # (decrypt pkt): 0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                if minutes == 1:
                    ret_dict["one_min_decrypt_pkt"] = int(groups["decrypt_pkt"])
                if minutes == 5:
                    ret_dict["five_min_decrypt_pkt"] = int(groups["decrypt_pkt"])
                if minutes == 15:
                    ret_dict["fifteen_min_decrypt_pkt"] = int(groups["decrypt_pkt"])
                continue

            # (encrypt pkt): 0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                if minutes == 1:
                    ret_dict["one_min_encrypt_pkt"] = int(groups["encrypt_pkt"])
                if minutes == 5:
                    ret_dict["five_min_encrypt_pkt"] = int(groups["encrypt_pkt"])
                if minutes == 15:
                    ret_dict["fifteen_min_encrypt_pkt"] = int(groups["encrypt_pkt"])
                continue

        return ret_dict


# =============================================================
# Parser for 'show platform hardware qfp active classification feature tcam-usage'
# =============================================================


class ShowPlatformHardwareQfpActiveClassificationFeatureTcamUsageSchema(MetaParser):
    """Schema for: show platform hardware qfp active classification feature tcam-usage"""

    schema = {
        "client": {
            Any(): {
                "id": int,
                "one_sixty_bit_VMR": int,
                "three_twenty_bit_VMR": int,
                "total_cell": int,
                "total_percent": str,
            },
        },
    }


class ShowPlatformHardwareQfpActiveClassificationFeatureTcamUsage(
    ShowPlatformHardwareQfpActiveClassificationFeatureTcamUsageSchema
):
    """Parser for: show platform hardware qfp active classification feature tcam-usage"""

    cli_command = "show platform hardware qfp active classification feature tcam-usage"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}
        ret_dict["client"] = {}

        # nat           5   2           0           4           0
        p1 = re.compile(
            r"^\s*(?P<client>[\w\d]+)+\s*(?P<id>\d+)+\s*(?P<one_sixty_bit_VMR>\d+)+\s*(?P<three_twenty_bit_VMR>\d+)+\s*(?P<total_cell>\d+)+\s*(?P<total_percent>\d+)"
        )

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # nat           5   2           0           4           0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                client = groups["client"]
                ret_dict["client"][client] = {}
                ret_dict["client"][client]["id"] = int(groups["id"])
                ret_dict["client"][client]["one_sixty_bit_VMR"] = int(
                    groups["one_sixty_bit_VMR"]
                )
                ret_dict["client"][client]["three_twenty_bit_VMR"] = int(
                    groups["three_twenty_bit_VMR"]
                )
                ret_dict["client"][client]["total_cell"] = int(groups["total_cell"])
                ret_dict["client"][client]["total_percent"] = groups["total_percent"]
                continue

        return ret_dict


# =============================================================
# Schema for 'show platform hardware fpga switch {switch_num}'
# =============================================================
class ShowPlatformHardwareFpgaSwitchSchema(MetaParser):
    """Schema for show platform hardware fpga switch {switch_num}"""

    schema = {"register_address": {Any(): {"fpga_reg_desc": str, "value": str}}}


# =============================================================
# Parser for 'show platform hardware fpga switch {switch_num}'
# =============================================================
class ShowPlatformHardwareFpgaSwitch(ShowPlatformHardwareFpgaSwitchSchema):
    """Parser for show platform hardware fpga switch {switch_num}"""

    cli_command = "show platform hardware fpga switch {switch_num}"

    def cli(self, switch_num="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_num=switch_num))

        # Register Addr           FPGA Reg Description    Value
        # 0x000000f0         Common Platform Board ID     0x02705919
        p1 = re.compile(
            r"^(?P<register_address>[\w\d]+)\s+(?P<fpga_reg_desc>[\S\s]+)     (?P<value>[\w\d]+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                sub_dict = ret_dict.setdefault("register_address", {}).setdefault(
                    dict_val["register_address"], {}
                )
                sub_dict["fpga_reg_desc"] = dict_val["fpga_reg_desc"]
                sub_dict["value"] = dict_val["value"]
                continue

        return ret_dict


# ==================================================================
# Parser for 'show platform hardware qfp active feature nat66 datapath prefix'
# ==================================================================


class ShowPlatformHardwareQfpActiveFeatureNat66DatapathPrefixSchema(MetaParser):
    """Schema for show platform hardware qfp active feature nat66 datapath prefix"""

    schema = {
        "nat66_prefix": {
            "hasht": str,
            "max": int,
            "chunk": str,
            "hash_salt": int,
            "nat66_prefixes": {
                Any(): {
                    "hash": int,
                    "id": int,
                    "len": int,
                    "vrf": int,
                    "in": str,
                    "out": str,
                    "inc_csum": str,
                    "in2out": int,
                    "out2in": int,
                    "egress_ifh": str,
                    Optional("ra"): int,
                },
            },
            Optional("total_prefixes"): int,
        },
    }


class ShowPlatformHardwareQfpActiveFeatureNat66DatapathPrefix(
    ShowPlatformHardwareQfpActiveFeatureNat66DatapathPrefixSchema
):
    """Parser for show platform hardware qfp active feature nat66 datapath prefix"""

    cli_command = "show platform hardware qfp active feature nat66 datapath prefix"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # prefix hasht 0xe76da800 max 32 chunk 0xe8a23010 hash_salt 1588817540
        q1 = re.compile(
            r"^prefix +hasht +(?P<hasht>\S+) +max +(?P<max>\d+) +chunk +(?P<chunk>\S+) +hash_salt +(?P<hash_salt>\d+)$"
        )
        # NAT66 hash[1] id(1) len(112) vrf(1) in: fd62:1b53:affb:1201:0000:0000:0000:0000 out: 2001:4888:affb:1201:0000:0000:0000:0000 inc_csum: 0xb02c in2out: 25 out2in: 20 egress_ifh 0x0 ra 0
        q2_1 = re.compile(
            r"^NAT66 +hash\[(?P<hash>\d+)\] +id\((?P<id>\d+)\) +len\((?P<len>\d+)\) +vrf\((?P<vrf>\d+)\) +in: +(?P<in>\S+) +out: +(?P<out>\S+) +inc_csum: +(?P<inc_csum>\S+) +in2out: +(?P<in2out>\d+) +out2in: +(?P<out2in>\d+) +egress_ifh +(?P<egress_ifh>\S+) +ra +(?P<ra>\d+)$"
        )
        # NAT66 hash[1] id(1) len(112) vrf(1) in: fd62:1b53:affb:1201:0000:0000:0000:0000 out: 2001:4888:affb:1201:0000:0000:0000:0000 inc_csum: 0xb02c in2out: 25 out2in: 20 egress_ifh 0x0
        q2_2 = re.compile(
            r"^NAT66 +hash\[(?P<hash>\d+)\] +id\((?P<id>\d+)\) +len\((?P<len>\d+)\) +vrf\((?P<vrf>\d+)\) +in: +(?P<in>\S+) +out: +(?P<out>\S+) +inc_csum: +(?P<inc_csum>\S+) +in2out: +(?P<in2out>\d+) +out2in: +(?P<out2in>\d+) +egress_ifh +(?P<egress_ifh>\S+)$"
        )
        # Total Prefixes: 3
        q3 = re.compile(r"^Total +Prefixes: +(?P<total_prefixes>\d+)$")
        ret_dict = {}
        nat66_prefixes_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # prefix hasht 0xe76da800 max 32 chunk 0xe8a23010 hash_salt 1588817540
            m = q1.match(line)
            if m:
                group = m.groupdict()
                nat66_prefix_dict = ret_dict.setdefault("nat66_prefix", {})
                nat66_prefix_dict["hasht"] = group["hasht"]
                nat66_prefix_dict["max"] = int(group["max"])
                nat66_prefix_dict["chunk"] = group["chunk"]
                nat66_prefix_dict["hash_salt"] = int(group["hash_salt"])
                continue
            # NAT66 hash[1] id(1) len(112) vrf(1) in: fd62:1b53:affb:1201:0000:0000:0000:0000 out: 2001:4888:affb:1201:0000:0000:0000:0000 inc_csum: 0xb02c in2out: 25 out2in: 20 egress_ifh 0x0 ra 0
            m = q2_1.match(line)
            if m:
                group = m.groupdict()
                nat66_prefixes_dict = nat66_prefix_dict.setdefault(
                    "nat66_prefixes", {}
                ).setdefault(group["id"], {})
                nat66_prefixes_dict["hash"] = int(group["hash"])
                nat66_prefixes_dict["id"] = int(group["id"])
                nat66_prefixes_dict["len"] = int(group["len"])
                nat66_prefixes_dict["vrf"] = int(group["vrf"])
                nat66_prefixes_dict["in"] = group["in"]
                nat66_prefixes_dict["out"] = group["out"]
                nat66_prefixes_dict["inc_csum"] = group["inc_csum"]
                nat66_prefixes_dict["in2out"] = int(group["in2out"])
                nat66_prefixes_dict["out2in"] = int(group["out2in"])
                nat66_prefixes_dict["egress_ifh"] = group["egress_ifh"]
                nat66_prefixes_dict["ra"] = int(group["ra"])
                continue
            # NAT66 hash[1] id(1) len(112) vrf(1) in: fd62:1b53:affb:1201:0000:0000:0000:0000 out: 2001:4888:affb:1201:0000:0000:0000:0000 inc_csum: 0xb02c in2out: 25 out2in: 20 egress_ifh 0x0
            m = q2_2.match(line)
            if m:
                group = m.groupdict()
                nat66_prefixes_dict = nat66_prefix_dict.setdefault(
                    "nat66_prefixes", {}
                ).setdefault(group["id"], {})
                nat66_prefixes_dict["hash"] = int(group["hash"])
                nat66_prefixes_dict["id"] = int(group["id"])
                nat66_prefixes_dict["len"] = int(group["len"])
                nat66_prefixes_dict["vrf"] = int(group["vrf"])
                nat66_prefixes_dict["in"] = group["in"]
                nat66_prefixes_dict["out"] = group["out"]
                nat66_prefixes_dict["inc_csum"] = group["inc_csum"]
                nat66_prefixes_dict["in2out"] = int(group["in2out"])
                nat66_prefixes_dict["out2in"] = int(group["out2in"])
                nat66_prefixes_dict["egress_ifh"] = group["egress_ifh"]
                continue
            # Total Prefixes: 3
            m = q3.match(line)
            if m:
                group = m.groupdict()
                nat66_prefix_dict["total_prefixes"] = int(group["total_prefixes"])
                continue

        return ret_dict


class ShowPlatformHardwareQfpInterfaceIfnamepathSchema(MetaParser):
    """Parser for show platform hardware qfp {status} interface if-name {interface} path"""

    schema = {
        Optional("valid_flag"): int,
        Optional("baf_port"): int,
        Optional("input_uIDB"): int,
        Optional("esi_channel"): str,
        Optional("baf_header"): str,
    }


class ShowPlatformHardwareQfpInterfaceIfnamepath(
    ShowPlatformHardwareQfpInterfaceIfnamepathSchema
):
    """Parser for show platform hardware qfp {status} interface if-name {interface} path"""

    cli_command = (
        "show platform hardware qfp {status} interface if-name {interface} path"
    )

    def cli(self, status, interface, output=None):
        if output is None:
            cmd = self.cli_command.format(status=status, interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        # Valid flag 1
        p1 = re.compile(r"^\s*Valid\s+flag\s+(?P<valid_flag>\d+)$")

        # BAF Port
        p2 = re.compile(r"^\s*BAF\s+Port\s+(?P<baf_port>\d+)$")

        # Input uIDB
        p3 = re.compile(r"^\s*Input\s+uIDB\s+(?P<input_uidb>\d+)$")

        # ESI channel
        p4 = re.compile(r"^\s*ESI\s+channel\s+(?P<esi_channel>0x[a-fA-F\d]+)$")

        # BAF header
        p5 = re.compile(r"^\s*BAF\s+header\s+(?P<baf_header>0x[\da-fA-F]+)$")

        # initial return dictionary
        ret_dict = {}

        for line in out.splitlines():
            # Valid flag 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["valid_flag"] = int(group["valid_flag"])
                continue

            # BAF Port 8
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["baf_port"] = int(group["baf_port"])
                continue

            # Input uIDB 49
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["input_uIDB"] = int(group["input_uidb"])
                continue

            # ESI channel 0x8000007
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["esi_channel"] = group["esi_channel"]
                continue

            # BAF header 0x0
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                ret_dict["baf_header"] = group["baf_header"]

        return ret_dict


class ShowPlatformHardwareQfpInterfaceIfnamepathSchema(MetaParser):
    """Parser for show platform hardware qfp {status} interface if-name {interface} path"""

    schema = {
        Optional("valid_flag"): int,
        Optional("baf_port"): int,
        Optional("input_uIDB"): int,
        Optional("esi_channel"): str,
        Optional("baf_header"): str,
    }


class ShowPlatformHardwareQfpInterfaceIfnamepath(
    ShowPlatformHardwareQfpInterfaceIfnamepathSchema
):
    """Parser for show platform hardware qfp {status} interface if-name {interface} path"""

    cli_command = (
        "show platform hardware qfp {status} interface if-name {interface} path"
    )

    def cli(self, status, interface, output=None):
        if output is None:
            cmd = self.cli_command.format(status=status, interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        # Valid flag 1
        p1 = re.compile(r"^\s*Valid\s+flag\s+(?P<valid_flag>\d+)$")

        # BAF Port
        p2 = re.compile(r"^\s*BAF\s+Port\s+(?P<baf_port>\d+)$")

        # Input uIDB
        p3 = re.compile(r"^\s*Input\s+uIDB\s+(?P<input_uidb>\d+)$")

        # ESI channel
        p4 = re.compile(r"^\s*ESI\s+channel\s+(?P<esi_channel>0x[a-fA-F\d]+)$")

        # BAF header
        p5 = re.compile(r"^\s*BAF\s+header\s+(?P<baf_header>0x[\da-fA-F]+)$")

        # initial return dictionary
        ret_dict = {}

        for line in out.splitlines():
            # Valid flag 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["valid_flag"] = int(group["valid_flag"])
                continue

            # BAF Port 8
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["baf_port"] = int(group["baf_port"])
                continue

            # Input uIDB 49
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["input_uIDB"] = int(group["input_uidb"])
                continue

            # ESI channel 0x8000007
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["esi_channel"] = group["esi_channel"]
                continue

            # BAF header 0x0
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                ret_dict["baf_header"] = group["baf_header"]

        return ret_dict


# ============================================================================
#  Schema for
#  * 'show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free'
# ============================================================================


class ShowPlatformHardwareIomdMacsecPortSubportSchema(MetaParser):
    schema = {"device": {int: {"free_SA": int, "used_SA": int}}}


class ShowPlatformHardwareIomdMacsecPortSubport(
    ShowPlatformHardwareIomdMacsecPortSubportSchema
):

    """
    Parser for
    * 'show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free'
    """

    cli_command = "show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free"

    def cli(self, lc_no, port_no, sub_port1, sub_port2, output=None):
        if output is None:
            cmd = self.cli_command.format(
                lc_no=lc_no, port_no=port_no, sub_port1=sub_port1, sub_port2=sub_port2
            )
            output = self.device.execute(cmd)
        ret_dict = {}
        list_key_num = 1

        # Secy_Device SA Idx count: No of Free SA 507, Used SA 5
        p1 = re.compile(
            r"Secy_Device\s+SA\s+Idx\s+count:\s+No\s+of\s+Free\s+SA\s+(?P<free_SA>-?\d+),\s+Used\s+SA\s+(?P<used_SA>-?\d+)$"
        )

        for line in output.splitlines():
            # Secy_Device SA Idx count: No of Free SA 507, Used SA 5
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                list_index_dict = ret_dict
                list_index_dict = list_index_dict.setdefault("device", {})
                list_index_dict = list_index_dict.setdefault(list_key_num, {})
                list_index_dict["free_SA"] = int(match_dict["free_SA"])
                list_index_dict["used_SA"] = int(match_dict["used_SA"])
                list_key_num += 1
                continue

        return ret_dict


# ============================================================================
#  Schema for
#  * 'show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free'
# ============================================================================


class ShowPlatformHardwareIomdMacsecPortSubportSchema(MetaParser):
    schema = {"device": {int: {"free_SA": int, "used_SA": int}}}


class ShowPlatformHardwareIomdMacsecPortSubport(
    ShowPlatformHardwareIomdMacsecPortSubportSchema
):

    """
    Parser for
    * 'show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free'
    """

    cli_command = "show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free"

    def cli(self, lc_no, port_no, sub_port1, sub_port2, output=None):
        if output is None:
            cmd = self.cli_command.format(
                lc_no=lc_no, port_no=port_no, sub_port1=sub_port1, sub_port2=sub_port2
            )
            output = self.device.execute(cmd)
        ret_dict = {}
        list_key_num = 1

        # Secy_Device SA Idx count: No of Free SA 507, Used SA 5
        p1 = re.compile(
            r"Secy_Device\s+SA\s+Idx\s+count:\s+No\s+of\s+Free\s+SA\s+(?P<free_SA>-?\d+),\s+Used\s+SA\s+(?P<used_SA>-?\d+)$"
        )

        for line in output.splitlines():
            # Secy_Device SA Idx count: No of Free SA 507, Used SA 5
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                list_index_dict = ret_dict
                list_index_dict = list_index_dict.setdefault("device", {})
                list_index_dict = list_index_dict.setdefault(list_key_num, {})
                list_index_dict["free_SA"] = int(match_dict["free_SA"])
                list_index_dict["used_SA"] = int(match_dict["used_SA"])
                list_key_num += 1
                continue

        return ret_dict


# ============================================================================
#  Schema for
#  * 'show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free'
# ============================================================================


class ShowPlatformHardwareIomdMacsecPortSubportSchema(MetaParser):
    schema = {"device": {int: {"free_SA": int, "used_SA": int}}}


class ShowPlatformHardwareIomdMacsecPortSubport(
    ShowPlatformHardwareIomdMacsecPortSubportSchema
):

    """
    Parser for
    * 'show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free'
    """

    cli_command = "show platform hardware iomd {lc_no} macsec port {port_no} sub-port {sub_port1} {sub_port2} | i Free"

    def cli(self, lc_no, port_no, sub_port1, sub_port2, output=None):
        if output is None:
            cmd = self.cli_command.format(
                lc_no=lc_no, port_no=port_no, sub_port1=sub_port1, sub_port2=sub_port2
            )
            output = self.device.execute(cmd)
        ret_dict = {}
        list_key_num = 1

        # Secy_Device SA Idx count: No of Free SA 507, Used SA 5
        p1 = re.compile(
            r"Secy_Device\s+SA\s+Idx\s+count:\s+No\s+of\s+Free\s+SA\s+(?P<free_SA>-?\d+),\s+Used\s+SA\s+(?P<used_SA>-?\d+)$"
        )

        for line in output.splitlines():
            # Secy_Device SA Idx count: No of Free SA 507, Used SA 5
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                list_index_dict = ret_dict
                list_index_dict = list_index_dict.setdefault("device", {})
                list_index_dict = list_index_dict.setdefault(list_key_num, {})
                list_index_dict["free_SA"] = int(match_dict["free_SA"])
                list_index_dict["used_SA"] = int(match_dict["used_SA"])
                list_key_num += 1
                continue

        return ret_dict


