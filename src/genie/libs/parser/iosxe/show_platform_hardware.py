"""show_platform_hardware.py

    * 'show platform hardware qfp active feature appqoe stats all'
    * 'show platform hardware qfp active datapath utilization summary'
    * 'show platform hardware qfp active datapath utilization'
    * 'show platform hardware qfp active tcam resource-manager usage'
    * 'show platform hardware throughput crypto'
    * 'show platform hardware throughput crypto'
    * 'show platform hardware authentication status'
    * 'show platform hardware chassis fantray detail switch {mode}'
    * 'show platform hardware chassis power-supply detail switch {mode} all'
    * 'show platform hardware qfp active infrastructure bqs status | include QOS|QFP'
    * 'show platform hardware qfp active infrastructure bqs schedule output default interface {interface}'
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
    * 'show platform hardware cpp active infrastructure exmem statistics user'
    * 'show platform hardware qfp active feature cts client interface'
    * 'show platform hardware cpp active feature firewall session create {session_context} {num_sessions}'
    * 'show platform hardware cpp active statistics drop'
    * 'show platform hardware cpp active system state'
    * 'show platform hardware qfp active feature ipsec state'
    * 'show platform hardware qfp active feature tcp stats detail'
    * 'show platform hardware qfp active classification class-group-manager class-group client cce all'
    * 'show platform hardware qfp active classification feature class-group ce_data cce {cce_id} interface {interface} input brief'
    * 'show platform hardware qfp active datapath infrastructure sw-hqf'
    * 'show platform hardware qfp active datapath infrastructure time basic'
    * 'show platform hardware qfp active interface if-name Port-channel1'
    * 'show platform hardware qfp active feature nat datapath stats'
    * 'show platform hardware cpp active feature nat datapath map'
    * 'show platform hardware qfp active feature bfd datapath session'
    * 'show platform hardware qfp active feature alg statistics sip l7data'
    * 'show platform hardware qfp active feature ipsec sa 3'
    * 'show platform hardware qfp active feature firewall memory'
    * 'show platform hardware qfp active feature alg statistics'
    * 'show platform hardware qfp active feature alg statistics dns'
    * 'show platform hardware qfp active feature alg statistics dns {clear} '
    * 'show platform hardware qfp active feature alg statistics smtp'
    * 'show platform hardware qfp active feature alg statistics smtp {clear}'
    * 'show platform hardware qfp active feature alg statistics sunrpc'
    * 'show platform hardware qfp active feature alg statistics sunrpc {clear}'
    * 'show platform hardware qfp active feature nat data stats'
    * 'show platform hardware qfp active feature alg statistics pop3'
    * 'show platform hardware qfp active feature alg statistics pop3 {clear}'
    * 'show platform hardware qfp active feature alg statistics msrpc'
    * 'show platform hardware qfp active feature alg statistics msrpc {clear}'
    * 'show platform hardware qa active fe alg sta sip clear'
    * 'show platform hardware qfp active feature firewall datapath scb any any any any any all any detail'
    * 'show platform hardware qfp active feature firewall drop'
    * 'show platform hardware qfp active feature firewall drop all'
    * 'show platform hardware qfp active feature firewall drop clear'
    * 'show platform hardware qfp active feature firewall drop verbose'
    * 'show platform hardware qfp active feature nat datapath edm'
    * 'show platform hardware qfp active feature evc client l2cp-actions interface {interface}'
    * 'show platform hardware qfp active feature firewall runtime'
    * 'show platform hardware qfp active feature firewall runtime | sec RST segment'
    * 'show platform hardware qfp active feature nat datapath gatein'
    * 'show platform hardware qfp active feature nat datapath gateout'
    * 'show platform hardware qfp active feature alg statistics sip'
    * 'show platform hardware qfp active feature td datapath statistics'
    * 'show platform hardware qfp active feature nat datapath time'
    * 'show platform hardware cpp active feature nat datapath pool'
    * 'show platform hardware subslot <subslot> module host-if status'
    * 'show platform hardware qfp active feature alg statistics login clear'
    * 'show platform hardware qfp active feature firewall zonepair 1'
    * 'show platform hardware qfp active feature ess session'
    * 'show platform hardware qfp <instance> feature firewall ucode scb a a a a a a a detail'
    * 'show platform hardware qfp active infrastructure punt statistics type per-cause clear'
    * 'show platform hardware cpp active feature nat datapath stats'
    * 'show platform hardware cpp active feature nat datapath bind'
    * 'show platform hardware qfp active feature nat datapath time'
"""
import re
import logging
from collections import OrderedDict
from sys import int_info
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional,ListOf, Use, And
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
            r" +QFP: +(?P<qfp>[\d\.]+)"
            r" +if_h: +(?P<if_h>\d+)"
            r" +Num Queues/Schedules: +(?P<num_queues>\d+)$"
        )

        #     Index 0 (Queue ID:0xa6, Name: GigabitEthernet1/0/7)
        p2 = re.compile(
            r"^Index +(?P<index>\d+)"
            r" +\(Queue +ID:(?P<queue_id>[\w\d]+),"
            r" +Name: +(?P<interf_name>[\w\d\/\.\-\:]+)\)$"
        )

        #       Software Control Info:
        #  PARQ Software Control Info:
        p3_1 = re.compile(r"^(PARQ +)?Software Control Info:$")

        #  (cache) queue id: 0x000000a6, wred: 0x88b16ac2, qlimit (bytes): 3281312
        #  (cache) queue id: 0x00000070, wred: 0xe73cfde0, qlimit (pkts ): 418
        p3_2 = re.compile(
            r"^\(cache\) +queue +id: +(?P<cache_queue_id>[\w\d]+),"
            r" +wred: +(?P<wred>[\w\d]+),"
            r" +qlimit +\((?P<type>bytes|pkts +)\): +(?P<qlimit>\d+)$"
        )

        #       parent_sid: 0x284, debug_name: GigabitEthernet1/0/7
        p4 = re.compile(
            r"^parent_sid: +(?P<parent_sid>[\w\d]+),"
            r" debug_name: +(?P<debug_name>[\w\d\/\.\-\:]+)$"
        )

        #       sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245728
        p5 = re.compile(
            r"^sw_flags: +(?P<sw_flags>[\w\d]+),"
            r" +sw_state: +(?P<sw_state>[\w\d]+),"
            r" +port_uidb: +(?P<port_uidb>\d+)$"
        )

        #       orig_min  : 0                   ,      min: 105000000
        p6 = re.compile(r"^orig_min +: +(?P<orig_min>\d+) +, +min: +(?P<min>\d+)$")

        #       min_qos   : 0                   , min_dflt: 0
        p7 = re.compile(
            r"^min_qos +: +(?P<min_qos>\d+) +, +min_dflt: +(?P<min_dflt>\d+)$"
        )

        #       orig_max  : 0                   ,      max: 0
        p8 = re.compile(r"^orig_max +: +(?P<orig_max>\d+) +, +max: +(?P<max>\d+)$")

        #       max_qos   : 0                   , max_dflt: 0
        p9 = re.compile(
            r"^max_qos +: +(?P<max_qos>\d+) +, +max_dflt: +(?P<max_dflt>\d+)$"
        )

        #       share     : 1
        p10 = re.compile(r"^share +: +(?P<share>\d+)$")

        #       plevel    : 0, priority: 65535
        p11 = re.compile(
            r"^plevel +: +(?P<plevel>\d+), +priority: +(?P<priority>\d+)$"
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
            r" +\(packets\): +(?P<tail_drops_packets>\d+)$"
        )

        #       total enqs  (bytes): 0                   ,          (packets): 0
        p14 = re.compile(
            r"^total +enqs +\(bytes\): +(?P<total_enqs_bytes>\d+) +,"
            r" +\(packets\): +(?P<total_enqs_packets>\d+)$"
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
            r" +\(packets\): +(?P<lic_throughput_oversub_drops_packets>\d+)$"
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
            r" +(?P<name>[\w\d\-]+),"
            r" +(?P<status>\w+)$"
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
            r" +(?P<interface>[\w\d]+) +(?P<logical_channel>\d+)$"
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
            r" +(?P<interface>[\w\d]+) +(?P<port>\d+)"
            r" +(?P<cfifo>\d+)$"
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
        Optional("mac_status"): {
            "hw_port": int,
            "speed": Or(int, str),
            "duplex": str,
            "link": str,
            "link_en": str,
            "tx_pause": str,
            "rx_pause": str,
        },
        Optional("l2_network"): {
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
        Optional("l3_network"): {
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
        Optional("mac_filtering"): str,
        Optional("mac_addr"): str,
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
        Optional("fc_mode"): str,
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
        Optional("vlan_mode"): str,
        Optional("native_vlan"): int,
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
        # MAC Status: lport 0, speed unknown, duplex unknown ...
        p1 = re.compile(
            r"^MAC Status: (hw_port|lport) (?P<hw_port>\d+), +speed "
            + r"(?P<speed>\d+|unknown), +duplex (?P<duplex>\S+), link "
            + r"(?P<link>\S+), link_en (?P<link_en>\S+) , tx_pause (?P<tx_pause>\S+), rx_pause (?P<rx_pause>\S+)$"
        )

        # L2_NETWORK or L3_NETWORK
        p1_5 = re.compile(r"^(?P<network_type>L2_NETWORK|L3_NETWORK)$")

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
        # TX_PAUSE: disabled XOFF_THRES: 1024(plim threshold 0%, Buff-size: 1024),   XON_THRES: 128, FC mode: 802.3X
        p15 = re.compile(
            r"^TX_PAUSE: +(?P<tx_pause_xoff>\S+) XOFF_THRES: +(?P<xoff_thres>\d+)\(plim threshold "
            + r"(?P<plim_thres>\d+)%, Buff-size: +(?P<buffer_size>\d+)\), +XON_THRES: +(?P<xon_thres>\d+)"
            + r"(, FC mode: +(?P<fc_mode>[\w\.]+))?$"
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

        # vlan mode tunnel, native vlan 2350
        # Vlan cfg: tunnel mode, native vlan 2350 (cfg 1)
        p27 = re.compile(r"[Vv]lan\s*(?:mode|cfg):?\s*(?P<mode>\w+)(?:\s+mode)?\s*,\s*native\s*vlan\s*(?P<vlan>\d+)")

        ret_dict = {}
        network_key = "l3_network"  # default to l3_network

        for line in output.splitlines():
            line = line.strip()
            # MAC Status: hw_port 0, speed 1000, duplex full, link Up, link_en Enable , tx_pause Enable, rx_pause Enable
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                dir_dict = ret_dict.setdefault("mac_status", {})
                speed_str = groups["speed"]
                speed_val = int(speed_str) if speed_str.isdigit() else speed_str
                dir_dict.update(
                    {
                        "hw_port": int(groups["hw_port"]),
                        "speed": speed_val,
                        "duplex": groups["duplex"],
                        "link": groups["link"],
                        "link_en": groups["link_en"],
                        "tx_pause": groups["tx_pause"],
                        "rx_pause": groups["rx_pause"],
                    }
                )
                continue

            # L2_NETWORK or L3_NETWORK
            m = p1_5.match(line)
            if m:
                groups = m.groupdict()
                # Set the network key based on detected type
                if groups["network_type"] == "L2_NETWORK":
                    network_key = "l2_network"
                else:
                    network_key = "l3_network"
                continue

            # link Up(config Enable), speed 1000(config 1000), duplex full(config full), config force_up, mtu 1526
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                dir_dict = ret_dict.setdefault(network_key, {})
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
                dir_dict = ret_dict.setdefault(network_key, {})
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
            # TX_PAUSE: disabled XOFF_THRES: 1024(plim threshold 0%, Buff-size: 1024),   XON_THRES: 128, FC mode: 802.3X
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                update_dict = {
                    "tx_pause_xoff": groups["tx_pause_xoff"],
                    "xoff_thres": int(groups["xoff_thres"]),
                    "plim_thres": int(groups["plim_thres"]),
                    "buffer_size": int(groups["buffer_size"]),
                    "xon_thres": int(groups["xon_thres"]),
                }
                if groups["fc_mode"]:
                    update_dict["fc_mode"] = groups["fc_mode"]
                ret_dict.update(update_dict)
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

            # vlan mode tunnel, native vlan 2350
            m = p27.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update(
                    {
                        "vlan_mode": groups["mode"],
                        "native_vlan": int(groups["vlan"]),
                    }
                )
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
            r" +(?P<interface>[\w\d]+) +(?P<logical_channel>\d+)$"
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
            r" +(?P<interface>[\w\d]+) +(?P<port>\d+)"
            r" +(?P<cfifo>\d+)$"
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
        Optional("SUP1 Authentication"): str,
        Optional("SUP 0 Authentication"): str,
        Optional("SUP 1 Authentication"): str,
        Optional("Fan Tray Authentication"): str,
        Optional("Fan Tray 1 Authentication"): str,
        Optional("Line Card:1 Authentication"): str,
        Optional("Line Card 1 Authentication"): str,
        Optional("Line Card:2 Authentication"): str,
        Optional("Line Card 2 Authentication"): str,
        Optional("Line Card:3 Authentication"): str,
        Optional("Line Card 3 Authentication"): str,
        Optional("Line Card:4 Authentication"): str,
        Optional("Line Card 4 Authentication"): str,
        Optional("Line Card:5 Authentication"): str,
        Optional("Line Card 5 Authentication"): str,
        Optional("Line Card:6 Authentication"): str,
        Optional("Line Card 6 Authentication"): str,
        Optional("Line Card:7 Authentication"): str,
        Optional("Line Card 7 Authentication"): str,
        Optional("Line Card:8 Authentication"): str,
        Optional("Line Card 8 Authentication"): str,
        Optional("Line Card:9 Authentication"): str,
        Optional("Line Card 9 Authentication"): str,
        Optional("Line Card:10 Authentication"): str,
        Optional("Line Card 10 Authentication"): str,
        Optional("Chassis Authentication"): str,
        Optional("SSD FRU Authentication"): str,
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
            r"(Line\s+Card |SUP|Line\s+Card:|Fan\s+Tray|Chassis|SSD.+|SUP\s+|Fan\s+Tray )\d*\s*Authentication:\s+(?P<Slot>(pass|Not Available|fail))$"
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
        p1 = re.compile(r"^(?P<fan_tray>.+)\:$")

        # Inlet:8330 RPM, Outlet:10015 RPM, PWM:30%
        p2 = re.compile(
            r"^Inlet:(?P<inlet_rpm>\d+) +RPM\, +Outlet:(?P<outlet_rpm>\d+) +RPM\, PWM:(?P<pwm>\d+%)$"
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
        p1 = re.compile(r"^(?P<power_supply>.+)\:$")

        # Input Voltage   :       121.1250 V
        p2 = re.compile(r"^Input\s+Voltage\s+:\s+(?P<input_voltage_volt>\d+\.\d+) V$")

        # Output Voltage  :       12.0547 V
        p3 = re.compile(r"^Output\s+Voltage\s+:\s+(?P<output_voltage_volt>\d+\.\d+) V$")

        # Input Power     :       507.5000 W
        p4 = re.compile(r"^Input\s+Power\s+:\s+(?P<input_power_watt>\d+\.\d+) W$")

        # Output Power    :       0.0000 W
        p5 = re.compile(r"^Output\s+Power\s+:\s+(?P<output_power_watt>\d+\.\d+) W$")

        # Input Current   :       0.0000 A
        p6 = re.compile(r"^Input\s+Current\s+:\s+(?P<input_current_amp>\d+\.\d+) A$")

        # Output Current  :       0.0000 A
        p7 = re.compile(r"^Output\s+Current\s+:\s+(?P<output_current_amp>\d+\.\d+) A$")

        # Temperature1    :       0.0000 C
        p8 = re.compile(r"^Temperature1\s+:\s+(?P<temperature1_celsius>\d+\.\d+) C$")

        # Temperature2    :       0.0000 C
        p9 = re.compile(r"^Temperature2\s+:\s+(?P<temperature2_celsius>\d+\.\d+) C$")

        # Temperature3    :       0.0000 C
        p10 = re.compile(r"^Temperature3\s+:\s+(?P<temperature3_celsius>\d+\.\d+) C$")

        # Fan Speed 1     :       0.0000 RPM
        p11 = re.compile(r"^Fan\s+Speed\s+1\s+:\s+(?P<fan_speed_1_rpm>\d+\.\d+) RPM$")

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
        p1 = re.compile(r"^max chnl\s+(?P<max_channels>\d+)$")

        # Channel  Rail Name         Voltage(mv)   Nominal Voltage  Min Margin  % Change  Max Margin  Monitor
        # 0        PVCCKRHV              1315.71        1300.00       -3.00        1.21        3.00       0
        p2 = re.compile(
            r"^(?P<channels>\S+)\s+(?P<rail_name>\S+)\s+(?P<voltage_in_mv>[\d+\.]+)\s+(?P<nominal_voltage>[\d+\.]+)\s+(?P<min_margin>\S+)\s+(?P<percentage_change>\S+)\s+(?P<max_margin>\S+)\s+(?P<monitor>\d+)$"
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
        # or
        # Register Addr	                  FPGA Reg Description	Register Value
        p0 = re.compile(r"^Register\s+Addr\s+.*$")

        # 0x000000f0         Common Platform Board ID     0x02705919
        p1 = re.compile(
            r"^(?P<register_address>[\w\d]+)\s+(?P<fpga_reg_desc>[\S\s]+)\s+(?P<value>[\w\d]+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                continue

            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                sub_dict = ret_dict.setdefault("register_address", {}).setdefault(
                    dict_val["register_address"], {}
                )
                sub_dict["fpga_reg_desc"] = dict_val["fpga_reg_desc"].strip()
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

class ShowPlatformHardwareFedeyescanSchema(MetaParser):
    """Schema for show platform hardware fed switch {mode} npu slot 1 port {port_num} eye_scan"""

    schema = {
        Optional('npu_pdsf_procagent_get_eye_common'): str,
        'eye_capture':{
            'veye_data': {
                Any(): Or(int,str),
                   'veye_values': {
                        Any(): Or(int,str),
                },
            },
        },
        'port': int,
        Optional('slot'): int,
        'cmd': str,
        'rc': str,
        Optional('rsn'): str,
        Optional('reason'): str,
   }

class ShowPlatformHardwareFedeyescan(ShowPlatformHardwareFedeyescanSchema):
    """
    show platform hardware fed switch {mode} npu slot 1 port {port_num} eye_scan
    """

    cli_command = ['show platform hardware fed {switch} {mode} npu slot 1 port {port_num} eye_scan',
                    'show platform hardware fed {mode} npu slot 1 port {port_num} eye_scan']

    def cli(self, mode, port_num, switch=None, output=None):

        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, mode=mode,port_num=port_num))
            else:
                output = self.device.execute(self.cli_command[1].format(mode=mode,port_num=port_num))

        ret_dict = {}

        #npu_pdsf_procagent_config_loopback : asic inst 0 port 39 mode 1 command 20
        p1 =  re.compile(r'^npu_pdsf_procagent_get_eye_common\s*\:\s*(?P<npu_pdsf_procagent_get_eye_common>.*)$')

        #"eye_capture": {
        p2 = re.compile (r'^\"eye_capture\"\:\s*\{$')

        #"veye_data": [
        p3 = re.compile(r'^\"veye_data\"\:\s*\[$')

        #"veye_values": [
        p4 = re.compile(r'^\"veye_values\"\:\s*\[$')

        # "serdes_id": 18,
        p5 = re.compile(r'^\"(?P<key>\w+)\"\:\s*(?P<value>.*)$')

        #64,
        p5_1 = re.compile(r'^(?P<value>[-]?\d+)\,$')

        # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
        p6 = re.compile(r'^Port +\= +(?P<port>\d+) +Slot +\= +(?P<slot>\d+) +cmd +\= +(?P<cmd>\([\s*\S]*\)) +rc +\= +(?P<rc>\w+) +reason +\=(?P<reason>.*)$')

        # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
        p7  =  re.compile(r'^Port +\= +(?P<port>\d+) +cmd +\= +(?P<cmd>\([\s*\S]*\)) +rc +\= +(?P<rc>\w+) +rsn +\= +(?P<rsn>.*)$')
        cnt = 0
        for line in output.splitlines():
            line = line.strip()

            #npu_pdsf_procagent_config_loopback : asic inst 0 port 39 mode 1 command 20
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['npu_pdsf_procagent_get_eye_common'] = group['npu_pdsf_procagent_get_eye_common']
                continue

            #"eye_capture": {
            m = p2.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('eye_capture', {})
                continue

            #"veye_data": [
            m = p3.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('eye_capture', {}).setdefault('veye_data',{})
                continue

            #"veye_values": [
            m = p4.match(line)
            if m:
                curr_dict = ret_dict.setdefault('eye_capture', {}).setdefault('veye_data',{}).setdefault('veye_values', {})
                continue

            # "serdes_id": 18,
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if  group['value'] == '{' or  group['value'] == '[':
                    continue
                else:
                    group['key'] = group['key'].lower()
                    group['value'] = group['value'].strip(',')
                    if group['value'].isdigit():
                        group['value'] = int(group['value'])
                    curr_dict.update({group['key']: group['value']})
                    continue

            #64,
            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                cnt  = cnt + 1
                key  = cnt
                curr_dict.update({key: group['value']})
                continue

            # Port = 40 Slot = 1 cmd = () rc = 0x16 reason = (null)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['slot'] = int(group['slot'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['reason'] = group['reason']
                continue

            # Port = 39 cmd = (prbs_stop unit 0 port 39 slot 1 serdes_level 1 polynomial 31) rc = 0x0 rsn = success
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = int(group['port'])
                ret_dict['cmd'] = group['cmd']
                ret_dict['rc'] = group['rc']
                ret_dict['rsn'] = group['rsn']
                continue

        return ret_dict

class ShowPlatformHardwareFedXcvrRegistersSchema(MetaParser):
    """Schema for show platform hardware fed switch {mode} npu slot 1 port {port_num} eye_scan"""

    schema = {
        'phy_reg_value_hex': str,
        'phy_reg_value_dec': int,

   }

class ShowPlatformHardwareFedXcvrRegisters(ShowPlatformHardwareFedXcvrRegistersSchema):
    """
    show platform hardware fed {switch} {mode} xcvr {local_port} {phy} {mode_1} {device_num} {page_number} {register} {bytes}
    """
    cli_command = 'show platform hardware fed switch {mode} xcvr {local_port} {phy} {mode_1} {device_num} {page_number} {register} {byte}'

    def cli(self, mode, local_port, phy, mode_1, device_num, page_number, register, byte, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode, local_port=local_port, phy=phy, mode_1=mode_1, device_num=device_num, page_number=page_number, register=register, byte=byte))


        ret_dict = {}

        # Phy Reg Value(Hex): FFFF
        p1 =  re.compile(r'^Phy +Reg +Value\(Hex\)\:\s*(?P<phy_reg_value_hex>.*)$')

        #"eye_capture": {
        p2 = re.compile (r'^\(Dec\)\:\s*(?P<phy_reg_value_dec>.*)$')

        for line in output.splitlines():
            line = line.strip()

            # Phy Reg Value(Hex): FFFF
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['phy_reg_value_hex'] = group['phy_reg_value_hex']
                continue

            #"eye_capture": {
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['phy_reg_value_dec'] = int(group['phy_reg_value_dec'])
                continue

        return ret_dict

class ShowPlatformHardwareFedSwitchActiveNpuSlotPortRecreateSchema(MetaParser):
    """Schema for show platform hardware fed switch {mode} npu slot 1 port {port_num} port-recreate"""

    schema = {
        'port': str,
        'operations': {
            Any(): str,
        },
   }

class ShowPlatformHardwareFedSwitchActiveNpuSlotPortRecreate(
    ShowPlatformHardwareFedSwitchActiveNpuSlotPortRecreateSchema):
    """
    show platform hardware fed switch {mode} npu slot 1 port {port_num} port-recreate
    """

    cli_command = ['show platform hardware fed {switch} {mode} npu slot 1 port {port_num} port-recreate',
                    'show platform hardware fed {mode} npu slot 1 port {port_num} port-recreate']


    def cli(self, mode, port_num, switch=None, output=None):

        if output is None:
            if  switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, mode=mode,port_num=port_num))
            else:
                output = self.device.execute(self.cli_command[1].format(mode=mode,port_num=port_num))

        ret_dict = {}

        #Deleting port 1/40
        p1 =  re.compile(r'^Deleting +port +(?P<port>.*)$')

        # creating port 1/40
        p2 = re.compile(r'^creating +port +(?P<port>.*)$')

        # Recreate successfull 1/40
        p3 = re.compile(r'^Recreate +successfull +(?P<port>.*)$')

        # , Enabling the port
        p4 = re.compile(r'^\, +Enabling +the +port$')

        for line in output.splitlines():
            line = line.strip()

            #Deleting port 1/40
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'] = group['port']
                curr_dict = ret_dict.setdefault('operations', {})
                curr_dict.update({'delete' : group['port']})
                continue

            # creating port 1/40
            m = p2.match(line)
            if m:
                group = m.groupdict()
                curr_dict.update({'create' : group['port']})
                continue

            # Recreate successfull 1/40
            m = p3.match(line)
            if m:
                group = m.groupdict()
                curr_dict.update({'recreate' : group['port']})
                continue

            # , Enabling the port
            m = p4.match(line)
            if m:
                curr_dict.update({'enable' : 'successful'})
                continue

        return ret_dict


class ShowPlatformHardwareCppActInfraExmemStatUserSchema(MetaParser):
    """Schema for show platform hardware cpp active infrastructure exmem statistics user"""
    schema = {
        'type': {
            str: {  # Type name, e.g., 'IRAM', 'GLOBAL', etc.
                'qfp': int,
                'users': {
                    str: {  # User-Name
                        'allocations': int,
                        'bytes_alloc': int,
                        'bytes_total': int,
                    }
                }
            }
        }
    }


class ShowPlatformHardwareCppActInfraExmemStatUser(ShowPlatformHardwareCppActInfraExmemStatUserSchema):
    """Parser for show platform hardware cpp active infrastructure exmem statistics user"""

    cli_command = 'show platform hardware cpp active infrastructure exmem statistics user'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Type: Name: IRAM, QFP: 0
        type_name_qfp_re = re.compile(r'^Type: Name: (?P<type_name>\S+), QFP: (?P<qfp>\d+)$')
        # Allocations  Bytes-Alloc  Bytes-Total  User-Name
        #-------------------------------------------------
        #    8            58228        62464        P/I
        allocations_re = re.compile(
            r'^(?P<allocations>\d+)\s+(?P<bytes_alloc>\d+)\s+(?P<bytes_total>\d+)\s+(?P<user_name>.+)$'
        )

        current_type = None

        for line in output.splitlines():
            line = line.strip()

            # Type: Name: IRAM, QFP: 0
            match = type_name_qfp_re.match(line)
            if match:
                type_name = match.group('type_name')
                qfp = int(match.group('qfp'))
                current_type = type_name

                # Initialize the type dictionary
                parsed_dict.setdefault('type', {})

                if current_type not in parsed_dict['type']:
                    parsed_dict['type'][current_type] = {
                        'qfp': qfp,
                        'users': {}
                    }
                continue

            # Allocations  Bytes-Alloc  Bytes-Total  User-Name
            #-------------------------------------------------
            #    8            58228        62464        P/I
            match = allocations_re.match(line)
            if match and current_type:
                user_name = match.group('user_name').strip()
                allocations = int(match.group('allocations'))
                bytes_alloc = int(match.group('bytes_alloc'))
                bytes_total = int(match.group('bytes_total'))

                # Populate the user data
                parsed_dict['type'][current_type]['users'][user_name] = {
                    'allocations': allocations,
                    'bytes_alloc': bytes_alloc,
                    'bytes_total': bytes_total
                }

        return parsed_dict


class ShowPlatformHardwareQfpActiveFeatureCtsClientInterfaceSchema(MetaParser):
    """Schema for show platform hardware qfp active feature cts client interface"""
    schema = {
        'interfaces': {
            Any(): {
                'enable': int,
                'policy': int,
                'trust': int,
                'propagate': int,
                'internal': int,
                'sgt': int,
                'sgt_caching_in': int,
                'sgt_caching_eg': int,
                'in_dbg': int,
                'in_err': int,
                'out_dbg': int,
                'out_err': int,
            }
        }
    }


class ShowPlatformHardwareQfpActiveFeatureCtsClientInterface(ShowPlatformHardwareQfpActiveFeatureCtsClientInterfaceSchema):
    """Parser for show platform hardware qfp active feature cts client interface"""

    cli_command = 'show platform hardware qfp active feature cts client interface'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Interface GigabitEthernet0/1/1(11):
        interface_regex = re.compile(r'^Interface\s+(?P<interface>\S+)\(\d+\):$')
        # Enable=1, Policy=0, Trust=1, Propagate=1, Internal=0
        attributes_regex = re.compile(
            r'Enable=(?P<enable>\d+),\s+Policy=(?P<policy>\d+),\s+Trust=(?P<trust>\d+),\s+'
            r'Propagate=(?P<propagate>\d+),\s+Internal=(?P<internal>\d+)'
        )
        # SGT=2, SGT_caching_in=1 SGT_caching_eg=0
        sgt_regex = re.compile(
            r'SGT=(?P<sgt>\d+),\s+SGT_caching_in=(?P<sgt_caching_in>\d+)\s+SGT_caching_eg=(?P<sgt_caching_eg>\d+)'
        )
        # IN_dbg/ IN_err=0/0, OUT_dbg/ OUT_err=0/0
        dbg_err_regex = re.compile(
            r'IN_dbg/\s+IN_err=(?P<in_dbg>\d+)/(?P<in_err>\d+),\s+OUT_dbg/\s+OUT_err=(?P<out_dbg>\d+)/(?P<out_err>\d+)'
        )

        current_interface = None

        for line in output.splitlines():
            line = line.strip()

            # Interface GigabitEthernet0/1/1(11):
            match = interface_regex.match(line)
            if match:
                current_interface = match.group('interface')
                if 'interfaces' not in parsed_dict:
                    parsed_dict['interfaces'] = {}
                parsed_dict['interfaces'][current_interface] = {}
                continue

            # Enable=1, Policy=0, Trust=1, Propagate=1, Internal=0
            match = attributes_regex.match(line)
            if match and current_interface:
                parsed_dict['interfaces'][current_interface].update({
                    'enable': int(match.group('enable')),
                    'policy': int(match.group('policy')),
                    'trust': int(match.group('trust')),
                    'propagate': int(match.group('propagate')),
                    'internal': int(match.group('internal')),
                })
                continue

            # SGT=2, SGT_caching_in=1 SGT_caching_eg=0
            match = sgt_regex.match(line)
            if match and current_interface:
                parsed_dict['interfaces'][current_interface].update({
                    'sgt': int(match.group('sgt')),
                    'sgt_caching_in': int(match.group('sgt_caching_in')),
                    'sgt_caching_eg': int(match.group('sgt_caching_eg')),
                })
                continue

            # IN_dbg/ IN_err=0/0, OUT_dbg/ OUT_err=0/0
            match = dbg_err_regex.match(line)
            if match and current_interface:
                parsed_dict['interfaces'][current_interface].update({
                    'in_dbg': int(match.group('in_dbg')),
                    'in_err': int(match.group('in_err')),
                    'out_dbg': int(match.group('out_dbg')),
                    'out_err': int(match.group('out_err')),
                })
                continue

        return parsed_dict


class ShowPlatformHardwareCppActiveFeatureFirewallSessionSchema(MetaParser):
    """Schema for show platform hardware cpp active feature firewall session create {session_context} {num_sessions}"""
    schema = {
        Optional('sessions'): {
            int: {
                'source_ip': str,
                'destination_ip': str,
                'source_port': int,
                'destination_port': int,
                'protocol': str,
                'status': str,
                'creation_time': str,
                'timeout': str,
            }
        },
        Optional('sessions_read'): int,
        Optional('return_code'): int,
    }


class ShowPlatformHardwareCppActiveFeatureFirewallSession(ShowPlatformHardwareCppActiveFeatureFirewallSessionSchema):
    """Parser for show platform hardware cpp active feature firewall session create {session_context} {num_sessions}"""

    cli_command = 'show platform hardware cpp active feature firewall session create {session_context} {num_sessions}'

    def cli(self, session_context, num_sessions, output=None):
        if output is None:
            cmd = self.cli_command.format(session_context=session_context, num_sessions=num_sessions)
            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Pattern for detailed session data
        #Session ID   Source IP     Destination IP   Source Port   Dest Port   Protocol   Status       Creation Time   Timeout
        #1            192.168.1.10  10.0.0.1         12345         80          TCP        Established  00:01:30        00:04:30
        session_pattern = re.compile(
            r'^(?P<session_id>\d+)\s+'
            r'(?P<source_ip>\S+)\s+'
            r'(?P<destination_ip>\S+)\s+'
            r'(?P<source_port>\d+)\s+'
            r'(?P<destination_port>\d+)\s+'
            r'(?P<protocol>\S+)\s+'
            r'(?P<status>\S+)\s+'
            r'(?P<creation_time>\S+)\s+'
            r'(?P<timeout>\S+)$'
        )
        
        # Pattern for simple summary format
        # Number of sessions read: 0
        sessions_read_pattern = re.compile(r'^Number of sessions read: (?P<sessions_read>\d+)$')
        
        # Return code: 4
        return_code_pattern = re.compile(r'^Return code: (?P<return_code>\d+)$')

        # Iterate over each line of the output
        for line in output.splitlines():
            line = line.strip()

            #Session ID   Source IP     Destination IP   Source Port   Dest Port   Protocol   Status       Creation Time   Timeout
            #1            192.168.1.10  10.0.0.1         12345         80          TCP        Established  00:01:30        00:04:30
            match = session_pattern.match(line)
            if match:
                group = match.groupdict()
                session_id = int(group['session_id'])

                # Use setdefault to avoid KeyError
                session_dict = parsed_dict.setdefault('sessions', {}).setdefault(session_id, {})

                # Populate the session dictionary
                session_dict.update({
                    'source_ip': group['source_ip'],
                    'destination_ip': group['destination_ip'],
                    'source_port': int(group['source_port']),
                    'destination_port': int(group['destination_port']),
                    'protocol': group['protocol'],
                    'status': group['status'],
                    'creation_time': group['creation_time'],
                    'timeout': group['timeout'],
                })
                continue
                
            # Try to match sessions read
            match = sessions_read_pattern.match(line)
            if match:
                parsed_dict['sessions_read'] = int(match.groupdict()['sessions_read'])
                continue
                
            # Try to match return code
            match = return_code_pattern.match(line)
            if match:
                parsed_dict['return_code'] = int(match.groupdict()['return_code'])
                continue

        return parsed_dict


class ShowPlatformHardwareCppActiveStatisticsDropSchema(MetaParser):
    """Schema for show platform hardware cpp active statistics drop"""
    schema = {
        'last_clearing': str,
        'global_drop_stats': {
            Any(): {
                 'packets': int,
                 'octets': int,
            }
        }
    }


class ShowPlatformHardwareCppActiveStatisticsDrop(ShowPlatformHardwareCppActiveStatisticsDropSchema):
    """Parser for show platform hardware cpp active statistics drop"""

    cli_command = 'show platform hardware cpp active statistics drop'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Last clearing of QFP drops statistics : never
        p1 = re.compile(r'^Last clearing of QFP drops statistics\s*:\s*(?P<last_clearing>.+)$')
        #-------------------------------------------------------------------------
        # Global Drop Stats                         Packets                  Octets
        #-------------------------------------------------------------------------
        # BadUidbIdx                                     59                   16702
        p2 = re.compile(r'^(?P<statistic>\S+)\s+(?P<packets>\d+)\s+(?P<octets>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Last clearing of QFP drops statistics : never
            m = p1.match(line)
            if m:
                parsed_dict['last_clearing'] = m.group('last_clearing')
                continue

            #-------------------------------------------------------------------------
            # Global Drop Stats                         Packets                  Octets
            #-------------------------------------------------------------------------
            # BadUidbIdx                                     59                   16702
            m = p2.match(line)
            if m:
                statistic = m.group('statistic')
                packets = int(m.group('packets'))
                octets = int(m.group('octets'))

                # Use setdefault to avoid key errors
                stats_dict = parsed_dict.setdefault('global_drop_stats', {})
                stats_dict[statistic] = {
                    'packets': packets,
                    'octets': octets
                }

        return parsed_dict
# ===============================================================
# Schema for 'show platform hardware qfp active feature ipsec state'
# ===============================================================

class ShowPlatformHardwareQfpActiveFeatureIpsecStateSchema(MetaParser):
    """Schema for show platform hardware qfp active feature ipsec state"""
    schema = {
        Optional('crypto_throughput_license_kbps_aggregate'): int,
        Optional('configured_throughput_successfully'):str,
        'message_counter': {
            Any(): {   #increasing index 0, 1, 2, 3, ...
                'type': str,
                'request': int,
                'reply_ok': int,
                'reply_error': int,
            }
        },
    }


# ===============================================================
# Parser for 'show platform hardware qfp active feature ipsec state'
# ===============================================================
class ShowPlatformHardwareQfpActiveFeatureIpsecState(ShowPlatformHardwareQfpActiveFeatureIpsecStateSchema):
    """Parser for show platform hardware qfp active feature ipsec state"""

    cli_command = 'show platform hardware qfp active feature ipsec state'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing
        # Define regex patterns
        #Crypto throughput license (kbps) (Aggregate): 10000
        p1 = re.compile(r'^Crypto throughput license \(kbps\) \(Aggregate\): (?P<crypto_throughput_license_kbps_aggregate>\d+)$')

        #Configured throughput sucessfully:unlimited
        p2 = re.compile(r'^Configured throughput sucessfully:(?P<configured_throughput_successfully>\S+)$')

        #  Type                  Request          Reply (OK)       Reply (Error)
        #  -----------------------------------------------------------------------
        #   Initialize            1                1                0
        p3 = re.compile(r'^(?P<type>\S+)\s+(?P<request>\d+)\s+(?P<reply_ok>\d+)\s+(?P<reply_error>\d+)$')



        # Parse each line of the output
        for line in output.splitlines():
            line = line.strip()

            # Match each pattern and populate the dictionary
            #Crypto throughput license (kbps) (Aggregate): 10000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['crypto_throughput_license_kbps_aggregate'] = int(group['crypto_throughput_license_kbps_aggregate'])
                continue

            #Configured throughput sucessfully:unlimited
            m = p2.match(line)
            if m:
                parsed_dict['configured_throughput_successfully'] = m.group('configured_throughput_successfully')
                continue

            #Message counter:
            #  Type                  Request          Reply (OK)       Reply (Error)
            #  -----------------------------------------------------------------------
            #   Initialize            1                1                0
            #   Initialize            5                5                0

            m = p3.match(line)
            if m:
                group = m.groupdict()
                message_counter_dict = parsed_dict.setdefault('message_counter', {})
                message_counter_index = len(message_counter_dict) + 1
                message = message_counter_dict.setdefault(message_counter_index, {})
                message['type'] = group['type']
                message['request'] = int(group['request'])
                message['reply_ok'] = int(group['reply_ok'])
                message['reply_error'] = int(group['reply_error'])
                continue
        return parsed_dict

 
class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightRoutesSchema(MetaParser):
    """Schema for:
    * 'show platform hardware fed switch active fwd-asic insight l2m_routes'
    * 'show platform hardware fed switch active fwd-asic insight l3m_routes'
    """

    schema = {
        "routes": {
            int: {
                "switch_cookie": int,
                "ip_version": int,
                "saddr": str,
                "gaddr": str,
                "mcg_gid": int,
                "mcg_cookie": str,
            }
        },
        "dev_ids": list,
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightRoutes(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightRoutesSchema):

    """Parser for:
    * 'show platform hardware fed switch active fwd-asic insight l2m_routes'
    * 'show platform hardware fed switch active fwd-asic insight l3m_routes'
    """

    cli_command = [
        "show platform hardware fed switch active fwd-asic insight l2m_routes",
        "show platform hardware fed switch active fwd-asic insight l3m_routes",
    ]

    def cli(self, route_type="l2m", output=None):
        if output is None:
            if route_type == "l2m":
                cmd = self.cli_command[0]
            elif route_type == "l3m":
                cmd = self.cli_command[1]
            else:
                raise ValueError("Invalid route_type. Use 'l2m' or 'l3m'.")
            output = self.device.execute(cmd)

        ret_dict = {}

        # Example pattern for l2m_routes or l3m_routes:
        # +------------+---------------+------------+-----------------+-----------+------------+----------------+
        # | switch-gid | switch-cookie | ip-version | saddr           | gaddr     | l2-mcg-gid | l2-mcg-cookie  |
        # +------------+---------------+------------+-----------------+-----------+------------+----------------+
        # | 103        |      103      | 4          | 255.255.255.255 | 232.0.0.1 | 26393      | urid:0x20::8a7 |
        # |            |               |            |                 |           |            |                |
        # +------------+---------------+------------+-----------------+-----------+------------+----------------+
        p1 = re.compile(
            r"^\|\s+(?P<switch_gid>\d+)\s+\|\s+(?P<switch_cookie>\d+)\s+\|\s+(?P<ip_version>\d+)\s+\|\s+(?P<saddr>\S+)\s+\|\s+(?P<gaddr>\S+)\s+\|\s+(?P<mcg_gid>\d+)\s+\|\s+(?P<mcg_cookie>\S+)\s+\|$"
        )

        # dev_id: 0
        # dev_id: 1
        # dev_id: 2
        # dev_id: 3
        p2 = re.compile(r"^dev_id:\s+(?P<dev_id>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # +------------+---------------+------------+-----------------+-----------+------------+----------------+
            # | switch-gid | switch-cookie | ip-version | saddr           | gaddr     | l2-mcg-gid | l2-mcg-cookie  |
            # +------------+---------------+------------+-----------------+-----------+------------+----------------+
            # | 103        |      103      | 4          | 255.255.255.255 | 232.0.0.1 | 26393      | urid:0x20::8a7 |
            # |            |               |            |                 |           |            |                |
            # +------------+---------------+------------+-----------------+-----------+------------+----------------+
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch_gid = int(group["switch_gid"])
                route_dict = ret_dict.setdefault("routes", {}).setdefault(switch_gid, {})

                route_dict.update({
                    "switch_cookie": int(group["switch_cookie"]),
                    "ip_version": int(group["ip_version"]),
                    "saddr": group["saddr"],
                    "gaddr": group["gaddr"],
                    "mcg_gid": int(group["mcg_gid"]),
                    "mcg_cookie": group["mcg_cookie"],
                })
                continue

            # dev_id: 0
            # dev_id: 1
            # dev_id: 2
            # dev_id: 3
            m = p2.match(line)
            if m:
                dev_id = int(m.group("dev_id"))
                dev_ids = ret_dict.setdefault("dev_ids", [])
                dev_ids.append(dev_id)
                continue
            
        return ret_dict
    
class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightGroupMembersSchema(MetaParser):
    """Schema for:
    * 'show platform hardware fed switch active fwd-asic insight l3m_group_members'
    * 'show platform hardware fed switch active fwd-asic insight l2m_group_members'
    """

    schema = {
        "group_members": {
            int: {
                "members": {
                    int: {
                        "type": str,
                        "l3_port_type": str,
                        "l2_dest_type": str,
                        "l2_dest_gid": int,
                        "member_gid": int,
                        "next_hop_gid": int,
                        "stack_port_oid": int,
                        "sysport_gid": int,
                    }
                }
            }
        }
    }


class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightGroupMembers(
    ShowPlatformHardwareFedSwitchActiveFwdAsicInsightGroupMembersSchema
):
    """Parser for:
    * 'show platform hardware fed switch active fwd-asic insight l3m_group_members'
    * 'show platform hardware fed switch active fwd-asic insight l2m_group_members'
    """

    cli_command = ["show platform hardware fed switch active fwd-asic insight {group_type}"]
    
    def cli(self, group_type, output=None):
        if output is None:
            cmd = self.cli_command[0].format(group_type=group_type)
            output = self.device.execute(cmd)
        
        ret_dict = {}

        # Example pattern for l3m_group_members or l2m_group_members:
        # +------------+-----+--------+--------------+--------------+-------------+-------------------+--------------+----------------+-------------+
        # | l3-mcg-gid | idx | type   | l3-port-type | l2-dest-type | l2-dest-gid | l3-mcg-member-gid | next-hop-gid | stack-port-oid | sysport-gid |
        # +------------+-----+--------+--------------+--------------+-------------+-------------------+--------------+----------------+-------------+
        # | 12345      | 1   | L3_AC  |     NONE     | DENSE_AC     | 54321       | 0                 | 0            | 0              | 128         |
        # |            |     |        |              |              |             |                   |              |                |             |
        # | 12345      | 2   | L3_MCG |     NONE     | NONE         | 0           | 65535             | 0            | 0              | 0           |
        # |            |     |        |              |              |             |                   |              |                |             |
        # +------------+-----+--------+--------------+--------------+-------------+-------------------+--------------+----------------+-------------+
        
        p1 = re.compile(
            r"^\|\s+(?P<gid>\d+)\s+\|\s+(?P<idx>\d+)\s+\|\s+(?P<type>\S+)\s+\|\s+(?P<l3_port_type>\S+)\s+\|\s+(?P<l2_dest_type>\S+)\s+\|\s+(?P<l2_dest_gid>\d+)\s+\|\s+(?P<member_gid>\d+)\s+\|\s+(?P<next_hop_gid>\d+)\s+\|\s+(?P<stack_port_oid>\d+)\s+\|\s+(?P<sysport_gid>\d+)\s+\|$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Example pattern for l3m_group_members or l2m_group_members:
            # +------------+-----+--------+--------------+--------------+-------------+-------------------+--------------+----------------+-------------+
            # | l3-mcg-gid | idx | type   | l3-port-type | l2-dest-type | l2-dest-gid | l3-mcg-member-gid | next-hop-gid | stack-port-oid | sysport-gid |
            # +------------+-----+--------+--------------+--------------+-------------+-------------------+--------------+----------------+-------------+
            # | 12345      | 1   | L3_AC  |     NONE     | DENSE_AC     | 54321       | 0                 | 0            | 0              | 128         |
            # |            |     |        |              |              |             |                   |              |                |             |
            # | 12345      | 2   | L3_MCG |     NONE     | NONE         | 0           | 65535             | 0            | 0              | 0           |
            # |            |     |        |              |              |             |                   |              |                |             |
            # +------------+-----+--------+--------------+--------------+-------------+-------------------+--------------+----------------+-------------+

            m = p1.match(line)
            if m:
                group = m.groupdict()
                gid = int(group["gid"])
                idx = int(group["idx"])
                group_dict = ret_dict.setdefault("group_members", {}).setdefault(gid, {})
                members_dict = group_dict.setdefault("members", {}).setdefault(idx, {})

                members_dict.update({
                    "type": group["type"],
                    "l3_port_type": group["l3_port_type"],
                    "l2_dest_type": group["l2_dest_type"],
                    "l2_dest_gid": int(group["l2_dest_gid"]),
                    "member_gid": int(group["member_gid"]),
                    "next_hop_gid": int(group["next_hop_gid"]),
                    "stack_port_oid": int(group["stack_port_oid"]),
                    "sysport_gid": int(group["sysport_gid"]),
                })

        return ret_dict


 

class ShowPlatformHardwareQfpActiveFeatureTcpStatsDetailSchema(MetaParser):
    """Schema for show platform hardware qfp active feature tcp stats detail"""
    schema = {
        'total_tcp_sessions': int,
        'tcp_packets_processed': int,
        'retransmissions': int,
        'tcp_segment_drops': {
            'out_of_order': int,
            'window_violation': int,
            'checksum_error': int,
        },
        'connection_attempts': {
            'successful': int,
            'failed': int,
        },
        'window_size_adjustments': int,
    }


class ShowPlatformHardwareQfpActiveFeatureTcpStatsDetail(ShowPlatformHardwareQfpActiveFeatureTcpStatsDetailSchema):
    """Parser for 'show platform hardware qfp active feature tcp stats detail'"""

    cli_command = 'show platform hardware qfp active feature tcp stats detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Total TCP Sessions: 150
        p1 = re.compile(r'^Total TCP Sessions: +(?P<total_tcp_sessions>\d+)$')
        # TCP Packets Processed: 12000
        p2 = re.compile(r'^TCP Packets Processed: +(?P<tcp_packets_processed>\d+)$')
        # Retransmissions: 50
        p3 = re.compile(r'^Retransmissions: +(?P<retransmissions>\d+)$')
        # TCP Segment Drops:
        p4 = re.compile(r'^TCP Segment Drops:$')
        # - Out of Order: 30
        p5 = re.compile(r'^.*Out of Order: +(?P<out_of_order>\d+)$')
        # - Window Violation: 20
        p6 = re.compile(r'^.*Window Violation: +(?P<window_violation>\d+)$')
        # - Checksum Error: 10
        p7 = re.compile(r'^.*Checksum Error: +(?P<checksum_error>\d+)$')
        # Connection Attempts:
        p8 = re.compile(r'^Connection Attempts:$')
        # - Successful: 145
        p9 = re.compile(r'^.*Successful: +(?P<successful>\d+)$')
        # - Failed: 5
        p10 = re.compile(r'^.*Failed: +(?P<failed>\d+)$')
        # Window Size Adjustments: 200
        p11 = re.compile(r'^Window Size Adjustments: +(?P<window_size_adjustments>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Total TCP Sessions: 150
            match = p1.match(line)
            if match:
                parsed_dict['total_tcp_sessions'] = int(match.group('total_tcp_sessions'))
                continue

            # TCP Packets Processed: 12000
            match = p2.match(line)
            if match:
                parsed_dict['tcp_packets_processed'] = int(match.group('tcp_packets_processed'))
                continue

            # Retransmissions: 50
            match = p3.match(line)
            if match:
                parsed_dict['retransmissions'] = int(match.group('retransmissions'))
                continue

            # TCP Segment Drops:
            match = p4.match(line)
            if match:
                parsed_dict.setdefault('tcp_segment_drops', {})
                continue

            # - Out of Order: 30
            match = p5.match(line)
            if match:
                parsed_dict['tcp_segment_drops']['out_of_order'] = int(match.group('out_of_order'))
                continue

            # - Window Violation: 20
            match = p6.match(line)
            if match:
                parsed_dict['tcp_segment_drops']['window_violation'] = int(match.group('window_violation'))
                continue

            # - Checksum Error: 10
            match = p7.match(line)
            if match:
                parsed_dict['tcp_segment_drops']['checksum_error'] = int(match.group('checksum_error'))
                continue

            # Connection Attempts:
            match = p8.match(line)
            if match:
                parsed_dict.setdefault('connection_attempts', {})
                continue

            # - Successful: 145
            match = p9.match(line)
            if match:
                parsed_dict['connection_attempts']['successful'] = int(match.group('successful'))
                continue

            # - Failed: 5
            match = p10.match(line)
            if match:
                parsed_dict['connection_attempts']['failed'] = int(match.group('failed'))
                continue

            # Window Size Adjustments: 200
            match = p11.match(line)
            if match:
                parsed_dict['window_size_adjustments'] = int(match.group('window_size_adjustments'))
                continue

        return parsed_dict

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightGroupsSchema(MetaParser):
    """Schema for:
    * 'show platform hardware fed switch active fwd-asic insight l3m_groups'
    * 'show platform hardware fed switch active fwd-asic insight l2m_groups'
    """

    schema = {
        "groups": {
            int: {
                "cookie": str,
                "num_members": int,
                "replication_paradigm": str,
                "egress_counter_id": int,
                "egress_counter_data": list,
            }
        }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightGroups(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightGroupsSchema):
    """Parser for:
    * 'show platform hardware fed switch active fwd-asic insight l3m_groups'
    * 'show platform hardware fed switch active fwd-asic insight l2m_groups'
    """

    cli_command = [
        "show platform hardware fed switch active fwd-asic insight l3m_groups",
        "show platform hardware fed switch active fwd-asic insight l2m_groups",
    ]

    def cli(self, group_type="l3m", output=None):
        if output is None:
            if group_type == "l3m":
                cmd = self.cli_command[0]
            elif group_type == "l2m":
                cmd = self.cli_command[1]
            else:
                raise ValueError("Invalid group_type. Use 'l3m' or 'l2m'.")
            output = self.device.execute(cmd)

        # Initialize the return dictionary
        ret_dict = {}

        # Example pattern for l3m_groups:
        # +------------+----------------+-------------+----------------------+-------------------+---------------------+
        # | l3-mcg-gid | l3-mcg-cookie  | num-members | replication-paradigm | egress-counter-id | egress-counter-data |
        # +------------+----------------+-------------+----------------------+-------------------+---------------------+
        # | 12345      | urid:0x30::abc | 3           |       INGRESS        | 0                 | [0,0]               |
        # +------------+----------------+-------------+----------------------+-------------------+---------------------+
    
        # Example pattern for l2m_groups:
        # +------------+----------------+-------------+----------------------+-------------------+---------------------+
        # | l2-mcg-gid | l2-mcg-cookie  | num-members | replication-paradigm | egress-counter-id | egress-counter-data |
        # +------------+----------------+-------------+----------------------+-------------------+---------------------+
        # | 26393      | urid:0x20::8a7 | 2           |       INGRESS        | 0                 | [0,0]               |
        # +------------+----------------+-------------+----------------------+-------------------+---------------------+

        p1 = re.compile(
            r"^\|\s+(?P<gid>\d+)\s+\|\s+(?P<cookie>\S+)\s+\|\s+(?P<num_members>\d+)\s+\|\s+(?P<replication_paradigm>\S+)\s+\|\s+(?P<egress_counter_id>\d+)\s+\|\s+\[(?P<egress_counter_data>[\d,]+)\]\s+\|$"
        )

        for line in output.splitlines():
            line = line.strip()


            # Example pattern for l3m_groups:
            # +------------+----------------+-------------+----------------------+-------------------+---------------------+
            # | l3-mcg-gid | l3-mcg-cookie  | num-members | replication-paradigm | egress-counter-id | egress-counter-data |
            # +------------+----------------+-------------+----------------------+-------------------+---------------------+
            # | 12345      | urid:0x30::abc | 3           |       INGRESS        | 0                 | [0,0]               |
            # +------------+----------------+-------------+----------------------+-------------------+---------------------+
        
            # Example pattern for l2m_groups:
            # +------------+----------------+-------------+----------------------+-------------------+---------------------+
            # | l2-mcg-gid | l2-mcg-cookie  | num-members | replication-paradigm | egress-counter-id | egress-counter-data |
            # +------------+----------------+-------------+----------------------+-------------------+---------------------+
            # | 26393      | urid:0x20::8a7 | 2           |       INGRESS        | 0                 | [0,0]               |
            # +------------+----------------+-------------+----------------------+-------------------+---------------------+

            m = p1.match(line)
            if m:
                group = m.groupdict()
                gid = int(group["gid"])
                group_dict = {
                    "cookie": group["cookie"],
                    "num_members": int(group["num_members"]),
                    "replication_paradigm": group["replication_paradigm"],
                    "egress_counter_id": int(group["egress_counter_id"]),
                    "egress_counter_data": [int(x) for x in group["egress_counter_data"].split(",")]
                }
                # Populate the dictionary
                ret_dict.setdefault("groups", {})[gid] = group_dict
            
        return ret_dict


class ShowPlatformHardwareQfpActiveClassificationSchema(MetaParser):
    """Schema for 'show platform hardware qfp active classification class-group-manager class-group client cce all"""

    schema = {
        'class_groups': {
            Any(): {
                'name': str,
            }
        }
    }


class ShowPlatformHardwareQfpActiveClassification(ShowPlatformHardwareQfpActiveClassificationSchema):
    """Parser for show platform hardware qfp active classification class-group-manager class-group client cce all"""

    cli_command = 'show platform hardware qfp active classification class-group-manager class-group client cce all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # class-group [CCE:7232096] classMapTest
        p1 = re.compile(r'^class-group \[CCE:(\d+)\] (\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # class-group [CCE:7232096] classMapTest
            match = p1.match(line)
            if match:
                cce_id = match.group(1)
                class_group_name = match.group(2)

                class_group_dict = parsed_dict.setdefault('class_groups', {})
                class_group_dict[cce_id] = {'name': class_group_name}

        return parsed_dict
    
   

class ShowPlatformHardwareQfpActiveClassificationCceInterfaceBriefSchema(MetaParser):
    """Schema for show platform hardware qfp active classification feature class-group ce_data cce {cce_id} interface {interface} input brief"""

    schema = {
        'qfp_classification_class_group': str,
        'class_group': {
            Optional('simple_ce_key'): {
                'number_of_fields': int,
                'cpp_idx': int,
                Optional('keys'): {
                    int: {
                        'name': str,
                        'key_pos': int,
                        'width': int,
                    }
                }
            }
        }
    }


class ShowPlatformHardwareQfpActiveClassificationCceInterfaceBrief(ShowPlatformHardwareQfpActiveClassificationCceInterfaceBriefSchema):
    """Parser for show platform hardware qfp active classification feature class-group ce_data cce {cce_id} interface {interface} input brief"""

    cli_command = 'show platform hardware qfp active classification feature class-group ce_data cce {cce_id} interface {interface} input brief'

    def cli(self, cce_id='', interface='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(cce_id=cce_id, interface=interface))

        # Initialize the parsed dictionary
        parsed_dict = {}

        # QFP classification class group SimpleCE
        p1 = re.compile(r'^QFP classification class group\s+(?P<qfp_class_group>\S+)$')
        
        # number of fields: 1,     cpp_idx: 0
        p2 = re.compile(r'^number of fields:\s+(?P<num_fields>\d+),\s+cpp_idx:\s+(?P<cpp_idx>\d+)$')
        
        # key(0): mpls_exp        key pos: 0,  width: 4
        p3 = re.compile(r'^key\((?P<key_index>\d+)\):\s+(?P<key_name>\S+)\s+key pos:\s+(?P<key_pos>\d+),\s+width:\s+(?P<width>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # QFP classification class group SimpleCE
            match = p1.match(line)
            if match:
                parsed_dict['qfp_classification_class_group'] = match.group('qfp_class_group')
                continue

            # number of fields: 1,     cpp_idx: 0
            match = p2.match(line)
            if match:
                class_group_dict = parsed_dict.setdefault('class_group', {}).setdefault('simple_ce_key', {})
                class_group_dict['number_of_fields'] = int(match.group(1))
                class_group_dict['cpp_idx'] = int(match.group(2))
                continue

            # key(0): mpls_exp        key pos: 0,  width: 4
            match = p3.match(line)
            if match:
                key_index = int(match.group(1))
                class_group_dict = parsed_dict.setdefault('class_group', {}).setdefault('simple_ce_key', {})
                keys_dict = class_group_dict.setdefault('keys', {})
                keys_dict[key_index] = {
                    'name': match.group(2),
                    'key_pos': int(match.group(3)),
                    'width': int(match.group(4)),
                }
                continue

        return parsed_dict



class ShowPlatformHardwareQfpActiveDatapathInfrastructureSwHqfSchema(MetaParser):
    """Schema for show platform hardware qfp active datapath infrastructure sw-hqf"""
    
    schema = {
        'name': str,
            Optional('hqf'): {
                int: {
                    'ipc': {
                        'send': int,
                        'fc': int,
                        'congested_cnt': int,
                    },
                    'recycle': {
                        'send_hi': int,
                        'send_lo': int,
                        'fc_hi': int,
                        'fc_lo': int,
                        'cong_hi': int,
                        'cong_lo': int,
                    },
                    'pkt': {
                        'send_hi': int,
                        'send_lo': int,
                        'fc_full_hi': int,
                        'fc_full_lo': int,
                        'cong_hi': int,
                        'cong_lo': int,
                    },
                    'aggr_send_stats': int,
                    'aggr_send_lo_state': int,
                    'aggr_send_hi_stats': int,
                    'max_tx_burst_sz_hi': int,
                    'max_tx_burst_sz_lo': int,
                    'gather_failed_to_alloc_b4q': int,
                    'ticks': int,
                    'max_ticks_accumulated': int,
                    'mpsc_stats': {
                        'count': int,
                        'enq': int,
                        'enq_spin': int,
                        'enq_post': int,
                        'enq_flush': int,
                        'sig_cnt': int,
                        'enq_cancel': int,
                        'deq': int,
                        'deq_wait': int,
                        'deq_fail': int,
                        'deq_cancel': int,
                        'deq_wait_timeout': int,
                    }
                }
            }
    }


class ShowPlatformHardwareQfpActiveDatapathInfrastructureSwHqf(ShowPlatformHardwareQfpActiveDatapathInfrastructureSwHqfSchema):
    """Parser for show platform hardware qfp active datapath infrastructure sw-hqf"""

    cli_command = 'show platform hardware qfp active datapath infrastructure sw-hqf'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing the output
        # Name                   : Pri1 Pri2 None / Inflight pkts
        p1 = re.compile(r'^Name\s+:\s+(?P<name>.+)$')
        # HQF[0] IPC: send 22624572 fc 0 congested_cnt 0
        p2 = re.compile(r'^HQF\[(?P<index>\d+)\]\s+IPC:\s+send\s+(?P<send>\d+)\s+fc\s+(?P<fc>\d+)\s+congested_cnt\s+(?P<congested_cnt>\d+)$')
        # HQF[0] recycle: send hi 0 send lo 6762623001
        p3 = re.compile(r'^HQF\[(?P<index>\d+)\]\s+recycle:\s+send\s+hi\s+(?P<send_hi>\d+)\s+send\s+lo\s+(?P<send_lo>\d+)$')
        # fc hi 0 fc lo 0
        p4 = re.compile(r'^fc\s+hi\s+(?P<fc_hi>\d+)\s+fc\s+lo\s+(?P<fc_lo>\d+)$')
        # cong hi 0 cong lo 0
        p5 = re.compile(r'^cong\s+hi\s+(?P<cong_hi>\d+)\s+cong\s+lo\s+(?P<cong_lo>\d+)$')
        # HQF[0] pkt: send hi 233619411 send lo 7565788702
        p6 = re.compile(r'^HQF\[(?P<index>\d+)\]\s+pkt:\s+send\s+hi\s+(?P<send_hi>\d+)\s+send\s+lo\s+(?P<send_lo>\d+)$')
        # fc/full hi 0 fc/full lo 0
        p7 = re.compile(r'^fc/full\s+hi\s+(?P<fc_full_hi>\d+)\s+fc/full\s+lo\s+(?P<fc_full_lo>\d+)$')
        # HQF[0] aggr send stats 14584654507 aggr send lo state 14351035183 
        p8 = re.compile(r'^HQF\[(?P<index>\d+)\]\s+aggr\s+send\s+stats\s+(?P<aggr_send_stats>\d+)\s+aggr\s+send\s+lo\s+state\s+(?P<aggr_send_lo_state>\d+)$')
        # aggr send hi stats 233619324
        p9 = re.compile(r'^aggr\s+send\s+hi\s+stats\s+(?P<aggr_send_hi_stats>\d+)$')
        # max_tx_burst_sz_hi 0 max_tx_burst_sz_lo 0
        p10 = re.compile(r'^max_tx_burst_sz_hi\s+(?P<max_tx_burst_sz_hi>\d+)\s+max_tx_burst_sz_lo\s+(?P<max_tx_burst_sz_lo>\d+)$')
        # HQF[0] gather: failed_to_alloc_b4q 0
        p11 = re.compile(r'^HQF\[(?P<index>\d+)\]\s+gather:\s+failed_to_alloc_b4q\s+(?P<failed_to_alloc_b4q>\d+)$')
        # HQF[0] ticks 106210219859, max ticks accumulated 2
        p12 = re.compile(r'^HQF\[(?P<index>\d+)\]\s+ticks\s+(?P<ticks>\d+),\s+max\s+ticks\s+accumulated\s+(?P<max_ticks_accumulated>\d+)$')
        # HQF[0] mpsc stats: count: 18446744060824649728
        p13 = re.compile(r'^HQF\[(?P<index>\d+)\]\s+mpsc\s+stats:\s+count:\s+(?P<count>\d+)$')
        # enq 1603618196 enq_spin 13412 enq_post 0 enq_flush 0
        p14 = re.compile(r'^enq\s+(?P<enq>\d+)\s+enq_spin\s+(?P<enq_spin>\d+)\s+enq_post\s+(?P<enq_post>\d+)\s+enq_flush\s+(?P<enq_flush>\d+)$')
        # sig_cnt:0 enq_cancel 0
        p15 = re.compile(r'^sig_cnt:(?P<sig_cnt>\d+)\s+enq_cancel\s+(?P<enq_cancel>\d+)$')
        # deq 14488520084 deq_wait 0 deq_fail 0 deq_cancel 0
        p16 = re.compile(r'^deq\s+(?P<deq>\d+)\s+deq_wait\s+(?P<deq_wait>\d+)\s+deq_fail\s+(?P<deq_fail>\d+)\s+deq_cancel\s+(?P<deq_cancel>\d+)$')
        # deq_wait_timeout 0
        p17 = re.compile(r'^deq_wait_timeout\s+(?P<deq_wait_timeout>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Match each line with the appropriate regex pattern
            # Name                   : Pri1 Pri2 None / Inflight pkts
            m = p1.match(line)
            if m:
                parsed_dict['name'] = m.group('name')
                continue
            
            # HQF[0] IPC: send 22624572 fc 0 congested_cnt 0
            m = p2.match(line)
            if m:
                index = int(m.group('index'))
                hqf_dict = parsed_dict.setdefault('hqf', {}).setdefault(index, {})
                hqf_dict['ipc'] = {
                    'send': int(m.group('send')),
                    'fc': int(m.group('fc')),
                    'congested_cnt': int(m.group('congested_cnt')),
                }
                continue
            
            # HQF[0] recycle: send hi 0 send lo 6762623001
            m = p3.match(line)
            if m:
                index = int(m.group('index'))
                hqf_dict = parsed_dict['hqf'][index]
                hqf_dict['recycle'] = {
                    'send_hi': int(m.group('send_hi')),
                    'send_lo': int(m.group('send_lo')),
                }
                continue
            
            # fc hi 0 fc lo 0
            m = p4.match(line)
            if m:
                hqf_dict['recycle'].update({
                    'fc_hi': int(m.group('fc_hi')),
                    'fc_lo': int(m.group('fc_lo')),
                })
                continue
            
            # cong hi 0 cong lo 0
            m = p5.match(line)
            if m:
                if 'recycle' in hqf_dict and 'cong_hi' not in hqf_dict['recycle']:
                    hqf_dict['recycle'].update({
                        'cong_hi': int(m.group('cong_hi')),
                        'cong_lo': int(m.group('cong_lo')),
                    })
                if 'pkt' in hqf_dict and 'cong_hi' not in hqf_dict['pkt']:
                    hqf_dict['pkt'].update({
                        'cong_hi': int(m.group('cong_hi')),
                        'cong_lo': int(m.group('cong_lo')),
                    })
                continue
            
            # HQF[0] pkt: send hi 233619411 send lo 7565788702
            m = p6.match(line)
            if m:
                index = int(m.group('index'))
                hqf_dict = parsed_dict['hqf'][index]
                hqf_dict['pkt'] = {
                    'send_hi': int(m.group('send_hi')),
                    'send_lo': int(m.group('send_lo')),
                }
                continue
            
            # fc/full hi 0 fc/full lo 0
            m = p7.match(line)
            if m:
                hqf_dict['pkt'].update({
                    'fc_full_hi': int(m.group('fc_full_hi')),
                    'fc_full_lo': int(m.group('fc_full_lo')),
                })
                continue
            
            # HQF[0] aggr send stats 14584654507 aggr send lo state 14351035183
            m = p8.match(line)
            if m:
                index = int(m.group('index'))
                hqf_dict = parsed_dict['hqf'][index]
                hqf_dict.update({
                    'aggr_send_stats': int(m.group('aggr_send_stats')),
                    'aggr_send_lo_state': int(m.group('aggr_send_lo_state')),
                })
                continue
            
            # aggr send hi stats 233619324
            m = p9.match(line)
            if m:
                hqf_dict.update({
                    'aggr_send_hi_stats': int(m.group('aggr_send_hi_stats')),
                })
                continue
            
            # max_tx_burst_sz_hi 0 max_tx_burst_sz_lo 0
            m = p10.match(line)
            if m:
                hqf_dict.update({
                    'max_tx_burst_sz_hi': int(m.group('max_tx_burst_sz_hi')),
                    'max_tx_burst_sz_lo': int(m.group('max_tx_burst_sz_lo')),
                })
                continue
            
            # HQF[0] gather: failed_to_alloc_b4q 0
            m = p11.match(line)
            if m:
                index = int(m.group('index'))
                hqf_dict = parsed_dict['hqf'][index]
                hqf_dict['gather_failed_to_alloc_b4q'] = int(m.group('failed_to_alloc_b4q'))
                continue
            
            # HQF[0] ticks 106210219859, max ticks accumulated 2
            m = p12.match(line)
            if m:
                index = int(m.group('index'))
                hqf_dict = parsed_dict['hqf'][index]
                hqf_dict.update({
                    'ticks': int(m.group('ticks')),
                    'max_ticks_accumulated': int(m.group('max_ticks_accumulated')),
                })
                continue
            
            # HQF[0] mpsc stats: count: 18446744060824649728
            m = p13.match(line)
            if m:
                index = int(m.group('index'))
                hqf_dict = parsed_dict['hqf'][index]
                hqf_dict['mpsc_stats'] = {
                    'count': int(m.group('count')),
                }
                continue
            
            # enq 1603618196 enq_spin 13412 enq_post 0 enq_flush 0
            m = p14.match(line)
            if m:
                hqf_dict['mpsc_stats'].update({
                    'enq': int(m.group('enq')),
                    'enq_spin': int(m.group('enq_spin')),
                    'enq_post': int(m.group('enq_post')),
                    'enq_flush': int(m.group('enq_flush')),
                })
                continue
            
            # sig_cnt:0 enq_cancel 0
            m = p15.match(line)
            if m:
                hqf_dict['mpsc_stats'].update({
                    'sig_cnt': int(m.group('sig_cnt')),
                    'enq_cancel': int(m.group('enq_cancel')),
                })
                continue
            
            # deq 14488520084 deq_wait 0 deq_fail 0 deq_cancel 0
            m = p16.match(line)
            if m:
                hqf_dict['mpsc_stats'].update({
                    'deq': int(m.group('deq')),
                    'deq_wait': int(m.group('deq_wait')),
                    'deq_fail': int(m.group('deq_fail')),
                    'deq_cancel': int(m.group('deq_cancel')),
                })
                continue
            
            # deq_wait_timeout 0
            m = p17.match(line)
            if m:
                hqf_dict['mpsc_stats'].update({
                    'deq_wait_timeout': int(m.group('deq_wait_timeout')),
                })
                continue

        return parsed_dict



class ShowPlatformHardwareQfpActiveDatapathInfrastructureTimeBasicSchema(MetaParser):
    """Schema for show platform hardware qfp active datapath infrastructure time basic"""
    schema = {
        'name': str,
        'timers_active': int,
        'timers_popped': int,
        'timers_new_thread_started': int,
        'timer_events_received': int,
        'sysup_time': int,
        'heartbeat_expected_seq': str,
        'time_hb_serial': int,
        'time_hb_errors': int,
        Optional('hb_input'): int,
        Optional('hb_output'): int,
        Optional('hb_tick_limit'): int,
        Optional('overflow'): int,
        Optional('pending'): int,
        Optional('ppe_timer_hb_max_tick'): int,
    }


class ShowPlatformHardwareQfpActiveDatapathInfrastructureTimeBasic(ShowPlatformHardwareQfpActiveDatapathInfrastructureTimeBasicSchema):
    """Parser for show platform hardware qfp active datapath infrastructure time basic"""

    cli_command = 'show platform hardware qfp active datapath infrastructure time basic'

    def cli(self, output=None):
        if output is None:
            # Execute the command on the device
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Define regex patterns for each line
        # timers active 46
        p1 = re.compile(r'^timers active (?P<timers_active>\d+)$')
        # timers popped 0
        p2 = re.compile(r'^timers popped (?P<timers_popped>\d+)$')
        # timers new thread started 1498569172
        p3 = re.compile(r'^timers new thread started (?P<timers_new_thread_started>-?\d+)$')
        # timer events received 1498569172
        p4 = re.compile(r'^timer events received (?P<timer_events_received>-?\d+)$')
        # sysup time 5056156016
        p5 = re.compile(r'^sysup time (?P<sysup_time>\d+)$')
        # heartbeat expected seq# 0x0
        p6 = re.compile(r'^heartbeat expected seq# (?P<heartbeat_expected_seq>0x[0-9a-fA-F]+)$')
        # time hb searial 0
        p7 = re.compile(r'^time hb searial (?P<time_hb_serial>\d+)$')
        # time hb errors 0
        p8 = re.compile(r'^time hb errors (?P<time_hb_errors>\d+)$')
        # HB input 316009849 output 316009691 tick limit 18
        p9 = re.compile(r'^HB input (?P<hb_input>\d+) output (?P<hb_output>\d+) tick limit (?P<hb_tick_limit>\d+)$')
        # overflow 1584  pending 158
        p10 = re.compile(r'^overflow (?P<overflow>\d+)  pending (?P<pending>\d+)$')
        # PPE timer HB max tick 1
        p11 = re.compile(r'^PPE timer HB max tick (?P<max_tick>\d+)$')

        #parsed_dict['name'] = 'Time Information'
        # Iterate over each line and match it with the corresponding regex pattern
        for line in output.splitlines():
            line = line.strip()
            if 'Time Information' in line:
                parsed_dict.setdefault('name', 'Time Information')
            # Match each line with the appropriate regex pattern
            # timers active 46
            m = p1.match(line)
            if m:
                parsed_dict['timers_active'] = int(m.group('timers_active'))
                continue
            
            # timers popped 0
            m = p2.match(line)
            if m:
                parsed_dict['timers_popped'] = int(m.group('timers_popped'))
                continue
            
            # timers new thread started 1498569172
            m = p3.match(line)
            if m:
                parsed_dict['timers_new_thread_started'] = int(m.group('timers_new_thread_started'))
                continue
            
            # timer events received 1498569172
            m = p4.match(line)
            if m:
                parsed_dict['timer_events_received'] = int(m.group('timer_events_received'))
                continue
            
            # sysup time 5056156016
            m = p5.match(line)
            if m:
                parsed_dict['sysup_time'] = int(m.group('sysup_time'))
                continue
            
            # heartbeat expected seq# 0x0
            m = p6.match(line)
            if m:
                parsed_dict['heartbeat_expected_seq'] = m.group('heartbeat_expected_seq')
                continue
            
            # time hb searial 0
            m = p7.match(line)
            if m:
                parsed_dict['time_hb_serial'] = int(m.group('time_hb_serial'))
                continue
            
            # time hb errors 0
            m = p8.match(line)
            if m:
                parsed_dict['time_hb_errors'] = int(m.group('time_hb_errors'))
                continue
            
            # HB input 316009849 output 316009691 tick limit 18
            m = p9.match(line)
            if m:
                parsed_dict['hb_input'] = int(m.group('hb_input'))
                parsed_dict['hb_output'] = int(m.group('hb_output'))
                parsed_dict['hb_tick_limit'] = int(m.group('hb_tick_limit'))
                continue
            
            # overflow 1584  pending 158
            m = p10.match(line)
            if m:
                parsed_dict['overflow'] = int(m.group('overflow'))
                parsed_dict['pending'] = int(m.group('pending'))
                continue
            
            # PPE timer HB max tick 1
            m = p11.match(line)
            if m:
                parsed_dict['ppe_timer_hb_max_tick'] = int(m.group('max_tick'))
                continue

        return parsed_dict

class ShowPlatformHardwarePortSchema(MetaParser):
    """Schema for show platform hardware port {port} ezman info"""
    schema = {
        'port': {
            str: {
                'admin_status': str,
                'operational_status': str,
                'link_status': str,
                'port_speed': str,
                'duplex': str,
                'mtu': int,
                'auto_negotiation': str,
                'flow_control': str,
                'mac_address': str,
                'crc_errors': int,
                'input_packets': int,
                'output_packets': int,
                'input_errors': int,
                'output_errors': int,
                'last_clear_counters': str,
                'temperature': str,
                'power_draw': float,
            }
        }
    }

class ShowPlatformHardwarePort(ShowPlatformHardwarePortSchema):
    """Parser for show platform hardware port {port} ezman info"""

    cli_command = 'show platform hardware port {port} ezman info'

    def cli(self, port='', output=None):
        if output is None:
            cmd = self.cli_command.format(port=port)
            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing the output

        # "Port: Gi1/0/1"
        p1 = re.compile(r'^Port:\s+(?P<port>\S+)$')

        # "Admin Status: up"
        p2 = re.compile(r'^Admin Status:\s+(?P<admin_status>\S+)$')

        # "Operational Status: down"
        p3 = re.compile(r'^Operational Status:\s+(?P<operational_status>\S+)$')

        # "Link Status: notconnect"
        p4 = re.compile(r'^Link Status:\s+(?P<link_status>\S+)$')

        # "Port Speed: 1000 Mbps"
        p5 = re.compile(r'^Port Speed:\s+(?P<port_speed>.+)$')

        # "Duplex: full"
        p6 = re.compile(r'^Duplex:\s+(?P<duplex>\S+)$')

        # "MTU: 1500"
        p7 = re.compile(r'^MTU:\s+(?P<mtu>\d+)$')

        # "Auto-Negotiation: enabled"
        p8 = re.compile(r'^Auto-Negotiation:\s+(?P<auto_negotiation>\S+)$')

        # "Flow Control: off"
        p9 = re.compile(r'^Flow Control:\s+(?P<flow_control>\S+)$')

        # "MAC Address: 00:1A:2B:3C:4D:5E"
        p10 = re.compile(r'^MAC Address:\s+(?P<mac_address>\S+)$')

        # "CRC Errors: 0"
        p11 = re.compile(r'^CRC Errors:\s+(?P<crc_errors>\d+)$')

        # "Input Packets: 123456"
        p12 = re.compile(r'^Input Packets:\s+(?P<input_packets>\d+)$')

        # "Output Packets: 654321"
        p13 = re.compile(r'^Output Packets:\s+(?P<output_packets>\d+)$')

        # "Input Errors: 3"
        p14 = re.compile(r'^Input Errors:\s+(?P<input_errors>\d+)$')

        # "Output Errors: 1"
        p15 = re.compile(r'^Output Errors:\s+(?P<output_errors>\d+)$')

        # "Last Clear Counters: 2024-06-01 14:22:11"
        p16 = re.compile(r'^Last Clear Counters:\s+(?P<last_clear_counters>.+)$')

        # "Temperature: 37.5 C"
        p17 = re.compile(r'^Temperature:\s+(?P<temperature>.+)$')

        # "Power Draw: 12.8"
        p18 = re.compile(r'^Power Draw:\s+(?P<power_draw>[\d\.]+)$')



        # Parse each line of the output
        for line in output.splitlines():
            line = line.strip()

            # "Port: Gi1/0/1"
            m = p1.match(line)
            if m:
                port = m.group('port')
                port_dict = parsed_dict.setdefault('port', {}).setdefault(port, {})
                continue

            # "Admin Status: up"
            m = p2.match(line)
            if m:
                port_dict['admin_status'] = m.group('admin_status')
                continue

            # "Operational Status: down"
            m = p3.match(line)
            if m:
                port_dict['operational_status'] = m.group('operational_status')
                continue

            # "Link Status: notconnect"
            m = p4.match(line)
            if m:
                port_dict['link_status'] = m.group('link_status')
                continue

            # "Port Speed: 1000 Mbps"
            m = p5.match(line)
            if m:
                port_dict['port_speed'] = m.group('port_speed')
                continue

            # "Duplex: full"
            m = p6.match(line)
            if m:
                port_dict['duplex'] = m.group('duplex')
                continue

            # "MTU: 1500"
            m = p7.match(line)
            if m:
                port_dict['mtu'] = int(m.group('mtu'))
                continue

            # "Auto-Negotiation: enabled"
            m = p8.match(line)
            if m:
                port_dict['auto_negotiation'] = m.group('auto_negotiation')
                continue

            # "Flow Control: off"
            m = p9.match(line)
            if m:
                port_dict['flow_control'] = m.group('flow_control')
                continue

            # "MAC Address: 00:1A:2B:3C:4D:5E"
            m = p10.match(line)
            if m:
                port_dict['mac_address'] = m.group('mac_address')
                continue

            # "CRC Errors: 0"
            m = p11.match(line)
            if m:
                port_dict['crc_errors'] = int(m.group('crc_errors'))
                continue

            # "Input Packets: 123456"
            m = p12.match(line)
            if m:
                port_dict['input_packets'] = int(m.group('input_packets'))
                continue

            # "Output Packets: 654321"
            m = p13.match(line)
            if m:
                port_dict['output_packets'] = int(m.group('output_packets'))
                continue

            # "Input Errors: 3"
            m = p14.match(line)
            if m:
                port_dict['input_errors'] = int(m.group('input_errors'))
                continue

            # "Output Errors: 1"
            m = p15.match(line)
            if m:
                port_dict['output_errors'] = int(m.group('output_errors'))
                continue

            # "Last Clear Counters: 2024-06-01 14:22:11"
            m = p16.match(line)
            if m:
                port_dict['last_clear_counters'] = m.group('last_clear_counters')
                continue

            # "Temperature: 37.5 C"
            m = p17.match(line)
            if m:
                port_dict['temperature'] = m.group('temperature')
                continue

            # "Power Draw: 12.8"
            m = p18.match(line)
            if m:
                port_dict['power_draw'] = float(m.group('power_draw'))
                continue

        return parsed_dict
class ShowPlatformHardwareQfpActiveFeatureBfdDatapathSessionSchema(MetaParser):
    """Schema for show platform hardware qfp active feature bfd datapath session"""

    schema = {
        'total_number_of_sessions': int,
        'sessions': {
            Any(): {
                'ld': int,
                'rd': int,
                'tx': int,
                'rx': int,
                'state': str,
                'pfcadm': str,
                'interface': str,
            }
        }
    }

class ShowPlatformHardwareQfpActiveFeatureBfdDatapathSession(ShowPlatformHardwareQfpActiveFeatureBfdDatapathSessionSchema):
    """Parser for show platform hardware qfp active feature bfd datapath session"""

    cli_command = 'show platform hardware qfp active feature bfd datapath session'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Total number of session: 1
        total_sessions_re = re.compile(r'^Total number of session: (?P<total>\d+)$')
        # 1    2    100    200    UP    3    GigabitEthernet0/0/0
        session_re = re.compile(
            r'^(?P<ld>\d+)\s+(?P<rd>\d+)\s+(?P<tx>\d+)\s+(?P<rx>\d+)\s+(?P<state>\w+)\s+(?P<pfcadm>\d+)\s+(?P<interface>\S+)$'
        )

        # Process each line of the output
        for line in output.splitlines():
            line = line.strip()

            # Total number of session: 1
            total_match = total_sessions_re.match(line)
            if total_match:
                parsed_dict['total_number_of_sessions'] = int(total_match.group('total'))
                continue

            # 1    2    100    200    UP    3    GigabitEthernet0/0/0
            session_match = session_re.match(line)
            if session_match:
                session_dict = session_match.groupdict()
                session_id = session_dict['ld']  # Using 'ld' as a unique key for sessions
                session_data = parsed_dict.setdefault('sessions', {}).setdefault(session_id, {})
                session_data.update({
                    'ld': int(session_dict['ld']),
                    'rd': int(session_dict['rd']),
                    'tx': int(session_dict['tx']),
                    'rx': int(session_dict['rx']),
                    'state': session_dict['state'],
                    'pfcadm': session_dict['pfcadm'],
                    'interface': session_dict['interface'],
                })
                continue
        return parsed_dict

class ShowPlatformHardwareQfpActiveFeatureIpsecSa3Schema(MetaParser):
    """Schema for show platform hardware qfp active feature ipsec sa 3"""
    schema = {
        'qfp_ipsec_sa_information': {
            'qfp_sa_id': int,
            'pal_sa_id': int,
            'qfp_spd_id': int,
            'qfp_sp_id': int,
            'qfp_spi': str,
            'crypto_ctx': str,
            'flags': str,
            'flags_details': ListOf(str),
            'flags_parsed': {str: str},
            'qos_group': str,
            'mtu': str,
            'mtu_adj': str,
            'ext_ar_window_size': int,
            'ext_ar_window_top': int,
            'sar_delta': int,
            'sar_window': str,
            'sibling_sa': str,
            'sp_ptr': str,
            'sbs_ptr': str,
            'local_endpoint': str,
            'remote_endpoint': str,
            'cgid_cid_fid_rid': str,
            'ivrf': int,
            'fvrf': int,
            'trans_udp_sport': int,
            'trans_udp_dport': int,
            'first_intf_name': str,
            'nat_fixup_src_port': int,
            'nat_fixup_ip': str
        }
    }

class ShowPlatformHardwareQfpActiveFeatureIpsecSa3(ShowPlatformHardwareQfpActiveFeatureIpsecSa3Schema):
    """Parser for:
        show platform hardware qfp active feature ipsec sa 3
    """
    cli_command = 'show platform hardware qfp active feature ipsec sa 3'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        # QFP sa  id: 12345
        p1 = re.compile(r'^QFP sa  id: (?P<qfp_sa_id>\d+)$')

        # pal sa id: 67890
        p2 = re.compile(r'^pal sa id: (?P<pal_sa_id>\d+)$')

        # QFP spd id: 23456
        p3 = re.compile(r'^QFP spd id: (?P<qfp_spd_id>\d+)$')

        # sp id: 78901
        p4 = re.compile(r'^QFP sp id: (?P<qfp_sp_id>\d+)$')

        # QFP spi: 0x12abc(456)
        p5 = re.compile(r'^QFP spi: (?P<qfp_spi>0x[0-9a-fA-F]+\(\d+\))$')

        # crypto ctx: 0x123abc
        p6 = re.compile(r'^crypto ctx: (?P<crypto_ctx>0x[0-9a-fA-F]+)$')

        #  flags: 0x1F (Details below)
        p7 = re.compile(r'^flags: (?P<flags>0x[0-9a-fA-F]+) \(Details below\)$')

        # FLAG1 FLAG2 VAL1:abc VAL2:def
        p8 = re.compile(r'^: (?P<details>.+)$')

        # qos_group: 0x2F
        p9 = re.compile(r'^qos_group: (?P<qos_group>0x[0-9a-fA-F]+)$')  # "qos_group"

        # mtu: 0x1000=0
        p10 = re.compile(r'^mtu: (?P<mtu>0x[0-9a-fA-F]+=0)$')

        # mtu_adj: 0x1100=0
        p11 = re.compile(r'^mtu_adj: (?P<mtu_adj>0x[0-9a-fA-F]+=0)$')

        #  ext_ar window_size: 50
        p12 = re.compile(r'^ext_ar window_size: (?P<ext_ar_window_size>\d+)$')

        # ext_ar window top: 10
        p13 = re.compile(r'^ext_ar window top: (?P<ext_ar_window_top>\d+)$')

        # sar_delta: 5
        p14 = re.compile(r'^sar_delta: (?P<sar_delta>\d+)$') 

        # sar_window: 0x1A2B
        p15 = re.compile(r'^sar_window: (?P<sar_window>0x[0-9a-fA-F]+)$')

        # sibling_sa: 0x3F4E
        p16 = re.compile(r'^sibling_sa: (?P<sibling_sa>0x[0-9a-fA-F]+)$') 

        # sp_ptr: 0x5A6B
        p17 = re.compile(r'^sp_ptr: (?P<sp_ptr>0x[0-9a-fA-F]+)$')

        # sbs_ptr: 0x7C8D
        p18 = re.compile(r'^sbs_ptr: (?P<sbs_ptr>0x[0-9a-fA-F]+)$')  

        # local endpoint: 192.168.1.1
        p19 = re.compile(r'^local endpoint: (?P<local_endpoint>[0-9.]+)$')  

        #  remote endpoint: 192.168.1.2
        p20 = re.compile(r'^remote endpoint: (?P<remote_endpoint>[0-9.]+)$') 

        # cgid.cid.fid.rid: 1.2.3.4
        p21 = re.compile(r'^cgid.cid.fid.rid: (?P<cgid_cid_fid_rid>[0-9.]+)$')  

        #  ivrf: 100
        p22 = re.compile(r'^ivrf: (?P<ivrf>\d+)$') 

        # fvrf: 200
        p23 = re.compile(r'^fvrf: (?P<fvrf>\d+)$')

        #  trans udp sport: 12345
        p24 = re.compile(r'^trans udp sport: (?P<trans_udp_sport>\d+)$')

        #  trans udp dport: 54321
        p25 = re.compile(r'^trans udp dport: (?P<trans_udp_dport>\d+)$')

        #  first intf name: Ethernet0/1
        p26 = re.compile(r'^first intf name: (?P<first_intf_name>.+)$')

        #  nat fixup src port: 9999
        p27 = re.compile(r'^nat fixup src port: (?P<nat_fixup_src_port>\d+)$')

        # nat fixup  ip: 10.0.0.1
        p28 = re.compile(r'^nat fixup  ip: (?P<nat_fixup_ip>[0-9.]+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            sa_dict = parsed_dict.setdefault('qfp_ipsec_sa_information', {})

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            sa_dict = parsed_dict.setdefault('qfp_ipsec_sa_information', {})

            # QFP sa  id: 12345
            m = p1.match(line)  
            if m:
                sa_dict['qfp_sa_id'] = int(m.group('qfp_sa_id'))
                continue

            # pal sa id: 67890
            m = p2.match(line)  
            if m:
                sa_dict['pal_sa_id'] = int(m.group('pal_sa_id'))
                continue

            # QFP spd id: 23456
            m = p3.match(line)  
            if m:
                sa_dict['qfp_spd_id'] = int(m.group('qfp_spd_id'))
                continue

            # QFP sp id: 78901
            m = p4.match(line)  
            if m:
                sa_dict['qfp_sp_id'] = int(m.group('qfp_sp_id'))
                continue

            # QFP spi: 0x12abc(456)
            m = p5.match(line)  
            if m:
                sa_dict['qfp_spi'] = m.group('qfp_spi')
                continue

            # crypto ctx: 0x123abc
            m = p6.match(line)  
            if m:
                sa_dict['crypto_ctx'] = m.group('crypto_ctx')
                continue

            # flags: 0x1F (Details below)
            m = p7.match(line)  
            if m:
                sa_dict['flags'] = m.group('flags')
                sa_dict['flags_details'] = []
                sa_dict['flags_parsed'] = {}
                continue

            # FLAG1 VAL1:abc FLAG2 VAL2:def
            m = p8.match(line)  
            if m:
                detail_line = m.group('details')
                sa_dict['flags_details'].append(detail_line)
                for part in detail_line.split():
                    if ':' in part:
                        k, v = part.split(':', 1)
                        sa_dict['flags_parsed'][k.strip()] = v.strip()
                    else:
                        sa_dict['flags_parsed'][part.strip()] = 'True'
                continue

            # qos_group: 0x2F
            m = p9.match(line)  
            if m:
                sa_dict['qos_group'] = m.group('qos_group')
                continue

            # mtu: 0x1000=0
            m = p10.match(line)  
            if m:
                sa_dict['mtu'] = m.group('mtu')
                continue

            # mtu_adj: 0x1100=0
            m = p11.match(line)  
            if m:
                sa_dict['mtu_adj'] = m.group('mtu_adj')
                continue

            # ext_ar window_size: 50
            m = p12.match(line)  
            if m:
                sa_dict['ext_ar_window_size'] = int(m.group('ext_ar_window_size'))
                continue

            # ext_ar window top: 10
            m = p13.match(line)  
            if m:
                sa_dict['ext_ar_window_top'] = int(m.group('ext_ar_window_top'))
                continue

            # sar_delta: 5
            m = p14.match(line)  
            if m:
                sa_dict['sar_delta'] = int(m.group('sar_delta'))
                continue

            # sar_window: 0x1A2B
            m = p15.match(line)  
            if m:
                sa_dict['sar_window'] = m.group('sar_window')
                continue

            # sibling_sa: 0x3F4E
            m = p16.match(line)  
            if m:
                sa_dict['sibling_sa'] = m.group('sibling_sa')
                continue

            # sp_ptr: 0x5A6B
            m = p17.match(line)  
            if m:
                sa_dict['sp_ptr'] = m.group('sp_ptr')
                continue

            # sbs_ptr: 0x7C8D
            m = p18.match(line)  
            if m:
                sa_dict['sbs_ptr'] = m.group('sbs_ptr')
                continue

            # local endpoint: 192.168.1.1
            m = p19.match(line)  
            if m:
                sa_dict['local_endpoint'] = m.group('local_endpoint')
                continue

            # remote endpoint: 192.168.1.2
            m = p20.match(line)  
            if m:
                sa_dict['remote_endpoint'] = m.group('remote_endpoint')
                continue

            # cgid.cid.fid.rid: 1.2.3.4
            m = p21.match(line)  
            if m:
                sa_dict['cgid_cid_fid_rid'] = m.group('cgid_cid_fid_rid')
                continue

            # ivrf: 100
            m = p22.match(line)  
            if m:
                sa_dict['ivrf'] = int(m.group('ivrf'))
                continue

            # fvrf: 200
            m = p23.match(line)  
            if m:
                sa_dict['fvrf'] = int(m.group('fvrf'))
                continue

            # trans udp sport: 12345
            m = p24.match(line)  
            if m:
                sa_dict['trans_udp_sport'] = int(m.group('trans_udp_sport'))
                continue

            # trans udp dport: 54321
            m = p25.match(line)  
            if m:
                sa_dict['trans_udp_dport'] = int(m.group('trans_udp_dport'))
                continue

            # first intf name: Ethernet0/1
            m = p26.match(line)  
            if m:
                sa_dict['first_intf_name'] = m.group('first_intf_name')
                continue

            # nat fixup src port: 9999
            m = p27.match(line)  
            if m:
                sa_dict['nat_fixup_src_port'] = int(m.group('nat_fixup_src_port'))
                continue

            # nat fixup  ip: 10.0.0.1
            m = p28.match(line)  
            if m:
                sa_dict['nat_fixup_ip'] = m.group('nat_fixup_ip')
                continue

        return parsed_dict


class ShowPlatformHardwareQfpActiveInterfaceIfNameSchema(MetaParser):
    schema = {
        "interface": {
            Any(): {
                "interface_state": str,
                "platform_interface_handle": int,
                "qfp_interface_handle": int,
                "rx_uidb": int,
                "tx_uidb": int,
                "channel": int,
                Optional("members"): ListOf(str),
                Optional("features"): ListOf(str),
                Optional("protocols"): {
                    Any(): {
                        Optional("cp_handle"): str,
                        Optional("dp_handle"): str,
                        Optional("features"): ListOf(str),
                    }
                },
                Optional("bundle"): {
                    "bundle_id": int,
                    "dps_addr": str,
                    "submap_table_addr": str,
                    "bundle_config_table_addr": str,
                    "load_balance_table_addr": str,
                    "link_config_table_addr": str,
                    "bucket": int,
                    "distribution_algorithm": str,
                    "member_links": ListOf(str),
                    "load_balance_table": {Any(): int},
                    "qos_mode": str,
                    "schedule_id": str,
                    "queue_id": str,
                    "vlan_autosense": str,
                }
            }
        }
    }


class ShowPlatformHardwareQfpActiveInterfaceIfName(ShowPlatformHardwareQfpActiveInterfaceIfNameSchema):
    cli_command = 'show platform hardware qfp active interface if-name {interface}'

    def cli(self, interface="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        ret_dict = {}
        current_interface = interface

        # Interface Name: GigabitEthernet0/0/0
        p1 = re.compile(r'^Interface Name: (?P<name>\S+)$')
        # Interface state: Up
        p2 = re.compile(r'^Interface state: (?P<state>\S+)$')
        # Platform interface handle: 12345
        p3 = re.compile(r'^Platform interface handle: (?P<handle>\d+)$')
        # QFP interface handle: 67890
        p4 = re.compile(r'^QFP interface handle: (?P<qfp_handle>\d+)$')
        #  Rx uidb: 100
        p5 = re.compile(r'^Rx uidb: (?P<rx_uidb>\d+)$')
        # Tx uidb: 200
        p6 = re.compile(r'^Tx uidb: (?P<tx_uidb>\d+)$')
        # Channel: 1
        p7 = re.compile(r'^Channel: (?P<channel>\d+)$')
        #  1  GigabitEthernet0/0/1
        p8 = re.compile(r'^\s*(\d+)\s+(?P<member>\S+)$')
        #  QoS (M) or  IPV6_OUTPUT_VFR (features can have or not have (M) marker)
        p9 = re.compile(r'^\s*(?P<feature>[A-Z0-9_]+)\s*(\(M\))?\s*$')
        # Features Bound to Interface numbered features like: 47 icmp_svr  
        p9a = re.compile(r'^\s*(?P<number>\d+)\s+(?P<feature>\S+)\s*$')
        # Protocol 1 - IPv4 or Protocol 0 - ipv4_input
        p10 = re.compile(r'^Protocol (?P<proto_id>\d+) - (?P<proto_name>\S+)$')
        # FIA handle - CP:0x1a2b3c DP:0x4d5e6f
        p11 = re.compile(r'^FIA handle - CP:(?P<cp>0x[0-9a-f]+)\s+DP:(?P<dp>0x[0-9a-f]+)$')
        # Idx:1 -> GigabitEthernet0/0/2
        p12 = re.compile(r'^\s+Idx:\d+\s+->\s+(?P<link>\S+)$')
        # bucket[0]=10
        p13 = re.compile(r'^\s+bucket\[(?P<idx>\d+)\]=(?P<val>\d+)$')
        # Bundle ID: 5
        p14 = re.compile(r'^\s+Bundle ID: (?P<id>\d+)$')
        #  DPS Addr: 0xabcdef
        p15 = re.compile(r'^\s+DPS Addr: (?P<addr>0x[0-9a-f]+)$')
        #  Submap Table Addr: 0x123456
        p16 = re.compile(r'^\s+Submap Table Addr: (?P<addr>0x[0-9a-f]+)$')
        #  Bundle Config Table Addr: 0x789abc
        p17 = re.compile(r'^\s+Bundle Config Table Addr: (?P<addr>0x[0-9a-f]+)$')
        #  Load Balance Table Addr: 0xdef123
        p18 = re.compile(r'^\s+Load Balance Table Addr: (?P<addr>0x[0-9a-f]+)$')
        #  Link Config Table Addr: 0x456789
        p19 = re.compile(r'^\s+Link Config Table Addr: (?P<addr>0x[0-9a-f]+)$')
        # Bucket: 3
        p20 = re.compile(r'^\s+Bucket: (?P<bucket>\d+)$')
        #  Distribution Algorithm: src-dst-ip
        p21 = re.compile(r'^\s+Distribution Algorithm: (?P<algo>\S+)$')
        #  QOS Mode: strict
        p22 = re.compile(r'^\s+QOS Mode: (?P<qos>\S+)$')
        #  Schedule ID: 0x1a2b
        p23 = re.compile(r'^\s+Schedule ID: (?P<sid>0x[0-9a-fA-F]+)$')
        #  Queue ID: 0x3c4d
        p24 = re.compile(r'^\s+Queue ID: (?P<qid>0x[0-9a-fA-F]+)$')
        #  VLAN AutoSense: Enabled
        p25 = re.compile(r'^\s+VLAN AutoSense: (?P<auto>\S+)$')

        feature_list = []
        protocol_name = None

        for line in output.splitlines():
            line = line.strip()

            # Interface Name: GigabitEthernet0/0/0
            m1 = p1.match(line)
            if m1: 
                interface_dict = ret_dict.setdefault("interface", {}).setdefault(m1.group("name"), {})
                continue

            # Interface state: Up
            m2 = p2.match(line)
            if m2:
                interface_dict["interface_state"] = m2.group("state")
                continue

            # Platform interface handle: 12345
            m3 = p3.match(line)
            if m3:
                interface_dict["platform_interface_handle"] = int(m3.group("handle"))
                continue

            # QFP interface handle: 67890
            m4 = p4.match(line)
            if m4:
                interface_dict["qfp_interface_handle"] = int(m4.group("qfp_handle"))
                continue

            # Rx uidb: 100
            m5 = p5.match(line)
            if m5:
                interface_dict["rx_uidb"] = int(m5.group("rx_uidb"))
                continue

            # Tx uidb: 200
            m6 = p6.match(line)
            if m6:
                interface_dict["tx_uidb"] = int(m6.group("tx_uidb"))
                continue

            # Channel: 1
            m7 = p7.match(line)
            if m7:
                interface_dict["channel"] = int(m7.group("channel"))
                continue

            # 1  GigabitEthernet0/0/1
            m8 = p8.match(line)
            if m8:
                members = interface_dict.setdefault("members", [])
                members.append(m8.group("member"))
                continue

 
            # Features Bound to Interface: numbered features like 47 icmp_svr
            m8a = p9a.match(line)
            if m8a:
                members = interface_dict.setdefault("members", [])
                members.append(m8a.group("feature"))
                continue

            # Protocol 1 - IPv4
            m9 = p10.match(line)
            if m9:
                protocol_name = m9.group("proto_name")
                proto_dict = interface_dict.setdefault("protocols", {}).setdefault(protocol_name, {})
                continue

            # FIA handle - CP:0x1a2b3c DP:0x4d5e6f
            m10 = p11.match(line)
            if m10 and protocol_name:
                proto_dict["cp_handle"] = m10.group("cp")
                proto_dict["dp_handle"] = m10.group("dp")
                continue

            # Features under protocols: IPV6_OUTPUT_VFR or QoS (M)
            m11 = p9.match(line)
            if m11 and protocol_name:
                feature_list = proto_dict.setdefault("features", [])
                feature_list.append(m11.group("feature").strip())
                continue

            # Bundle ID: 5
            m12 = p14.match(line)
            if m12:
                bundle = interface_dict.setdefault("bundle", {})
                bundle["bundle_id"] = int(m12.group("id"))
                continue

            # DPS Addr: 0xabcdef
            m13 = p15.match(line)
            if m13:
                bundle["dps_addr"] = m13.group("addr")
                continue

            # Submap Table Addr: 0x123456
            m14 = p16.match(line)
            if m14:
                bundle["submap_table_addr"] = m14.group("addr")
                continue

            # Bundle Config Table Addr: 0x789abc
            m15 = p17.match(line)
            if m15:
                bundle["bundle_config_table_addr"] = m15.group("addr")
                continue

            # Load Balance Table Addr: 0xdef123
            m16 = p18.match(line)
            if m16:
                bundle["load_balance_table_addr"] = m16.group("addr")
                continue

            # Link Config Table Addr: 0x456789
            m17 = p19.match(line)
            if m17:
                bundle["link_config_table_addr"] = m17.group("addr")
                continue

            # Bucket: 3
            m18 = p20.match(line)
            if m18:
                bundle["bucket"] = int(m18.group("bucket"))
                continue

            # Distribution Algorithm: src-dst-ip
            m19 = p21.match(line)
            if m19:
                bundle["distribution_algorithm"] = m19.group("algo")
                continue

            # Idx:1 -> GigabitEthernet0/0/2
            m20 = p12.match(line)
            if m20:
                links = bundle.setdefault("member_links", [])
                links.append(m20.group("link"))
                continue

            # bucket[0]=10
            m21 = p13.match(line)
            if m21:
                lbt = bundle.setdefault("load_balance_table", {})
                lbt[m21.group("idx")] = int(m21.group("val"))
                continue

            # QOS Mode: strict
            m22 = p22.match(line)
            if m22:
                bundle["qos_mode"] = m22.group("qos")
                continue

            # Schedule ID: 0x1a2b
            m23 = p23.match(line)
            if m23:
                bundle["schedule_id"] = m23.group("sid")
                continue

            # "Queue ID: 0x3c4d
            m24 = p24.match(line)
            if m24:
                bundle["queue_id"] = m24.group("qid")
                continue

            # VLAN AutoSense: Enabled
            m25 = p25.match(line)
            if m25:
                bundle["vlan_autosense"] = m25.group("auto")
                continue

        return ret_dict
    
    
class ShowPlatformHardwareQfpActiveFeatureNatDatapathStatsSchema(MetaParser):
    """Schema for show platform hardware qfp active feature nat datapath stats"""
    schema = {
        "counter": {
            Any(): int
        }
    }

class ShowPlatformHardwareQfpActiveFeatureNatDatapathStats(ShowPlatformHardwareQfpActiveFeatureNatDatapathStatsSchema):
    """Parser for show platform hardware qfp active feature nat datapath stats"""
    
    cli_command = "show platform hardware qfp active feature nat datapath stats"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the dictionary to store parsed data
        ret_dict = {}

        # Regex pattern to match counter names and their values
        # number_of_session   3
        # udp                 2 
        p1 = re.compile(r"^(?P<counter_name>[\w\-/\s]+)\s+(?P<value>\d+)$")

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Match each line with the regex
            m = p1.match(line)
            if m:
                group = m.groupdict()
                counter_name = group["counter_name"].strip().replace(" ", "_").lower()
                counter_value = int(group["value"])

                # Populate the dictionary with parsed counter data
                ret_dict.setdefault("counter", {})[counter_name] = counter_value
                
        return ret_dict

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSipL7dataSchema(MetaParser):
    '''Schema for show platform hardware qfp active feature alg statistics sip l7data'''
    schema = {
        'sip_info_pool_used_chunk_entries_number': int,
    }

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSipL7data(ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSipL7dataSchema):
    '''Parser for show platform hardware qfp active feature alg statistics sip l7data'''
    cli_command = 'show platform hardware qfp active feature alg statistics sip l7data'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed = {}

        # SIP info pool used chunk entries number: 0
        p1 = re.compile(r'^SIP info pool used chunk entries number:\s+(?P<value>\d+)$')

        # Parse each line
        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # SIP info pool used chunk entries number: 0
            m = p1.match(line)
            if m:
                parsed['sip_info_pool_used_chunk_entries_number'] = int(m.group('value'))
                continue

        return parsed


class ShowPlatformHardwareQfpActiveFeatureFirewallMemorySchema(MetaParser):
    """Schema for show platform hardware qfp active feature firewall memory"""
    schema = {
        'fw_memory_info': {
            'chunk_pool': {
                str: {
                    'allocated': int,
                    'total_free': int,
                    'init_num': int,
                    'low_wat': int,
                    'increment': int,
                    'elem_sz': int,
                }
            }
        },
        'total_history': {
            'chunk_pool': {
                str: {
                    'inuse': int,
                    'allocated': int,
                    'freed': int,
                    'alloc_fail': int,
                }
            }
        },
        'table_name': {
            str: {
                'address': str,
                'size': int,
            }
        },
        'fw_persona_timer_tbl': {
            'address': str,
            'entries': int,
            'num_tbls': int,
            'stagger': int,
        },
        'fw_persona_hostdb_mtx': {
            'lock_address': str,
        },
        'fw_persona_uncreated_sessions': int,
        'fw_persona_agg_age_sess_teardown': {
            'halfopen': int,
            'non_halfopen': int,
        },
        'fw_persona_hostdb_clear_session_stopped': int,
        'fw_total_number_of_thread': int,
        'number_of_cpu_complex': int,
    }

class ShowPlatformHardwareQfpActiveFeatureFirewallMemory(ShowPlatformHardwareQfpActiveFeatureFirewallMemorySchema):
    """Parser for show platform hardware qfp active feature firewall memory"""

    cli_command = 'show platform hardware qfp {rpname} feature firewall memory'


    def cli(self, rpname='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(rpname=rpname))


        parsed_dict = {}

        # BlockA 5 10 20 3 2 128
        p1 = re.compile(r'^(?P<chunk_pool>\w+)\s+(?P<allocated>\d+)\s+(?P<total_free>\d+)\s+'
                        r'(?P<init_num>\d+)\s+(?P<low_wat>\d+)\s+(?P<increment>\d+)\s+(?P<elem_sz>\d+)$')

        # BlockA 3 5 2 0
        p2 = re.compile(r'^(?P<chunk_pool>\w+)\s+(?P<inuse>\d+)\s+(?P<allocated>\d+)\s+'
                        r'(?P<freed>\d+)\s+(?P<alloc_fail>\d+)$')

        # TableX 0x1234abcd 1024
        p3 = re.compile(r'^(?P<table_name>\w+)\s+(?P<address>0x[0-9a-f]+)\s+(?P<size>\d+)$')

        # FW persona timer tbl address 0x1234abcd entries: 5 num_tbls 2 stagger 30
        p4 = re.compile(r'^FW persona timer tbl address (?P<address>0x[0-9a-f]+) entries: (?P<entries>\d+) '
                        r'num_tbls (?P<num_tbls>\d+) stagger (?P<stagger>\d+),$')

        # FW persona hostdb mtx (lock address): 0x5678efgh
        p5 = re.compile(r'^FW persona hostdb mtx \(lock address\): (?P<lock_address>0x[0-9a-f]+)$')

        # FW persona un-created sessions due to max session limit: 10
        p6 = re.compile(r'^FW persona un-created sessions due to max session limit:\s+(?P<uncreated_sessions>\d+)$')

        # FW persona agg-age sess teardown halfopen: 7, non-halfopen: 12
        p7 = re.compile(r'^FW persona agg-age sess teardown halfopen: (?P<halfopen>\d+), '
                        r'non-halfopen: (?P<non_halfopen>\d+)$')

        # FW persona number of times hostdb clear session stopped: 6
        p8 = re.compile(r'^FW persona number of times hostdb clear session stopped: (?P<clear_session_stopped>\d+)$')

        # FW total number of thread: 8, number of cpu complex: 2
        p9 = re.compile(r'^FW total number of thread: (?P<total_number_of_thread>\d+), '
                        r'number of cpu complex: (?P<number_of_cpu_complex>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # BlockA 5 10 20 3 2 128
            m = p1.match(line)
            if m:
                group = m.groupdict()
                chunk_pool = group.pop('chunk_pool')
                fw_mem = parsed_dict.setdefault('fw_memory_info', {}).setdefault('chunk_pool', {})
                fw_mem[chunk_pool] = {k: int(v) for k, v in group.items()}
                continue

            # BlockA 3 5 2 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                chunk_pool = group.pop('chunk_pool')
                hist = parsed_dict.setdefault('total_history', {}).setdefault('chunk_pool', {})
                hist[chunk_pool] = {k: int(v) for k, v in group.items()}
                continue

            # TableX 0x1234abcd 1024
            m = p3.match(line)
            if m:
                group = m.groupdict()
                table_name = group.pop('table_name')
                table_dict = parsed_dict.setdefault('table_name', {})
                table_dict[table_name] = {'address': group['address'], 'size': int(group['size'])}
                continue

            # FW persona timer tbl address 0x1234abcd entries: 5 num_tbls 2 stagger 30
            m = p4.match(line)
            if m:
                parsed_dict['fw_persona_timer_tbl'] = {
                    k: (int(v) if k != 'address' else v) for k, v in m.groupdict().items()
                }
                continue

            # FW persona hostdb mtx (lock address): 0x5678efgh
            m = p5.match(line)
            if m:
                parsed_dict['fw_persona_hostdb_mtx'] = {'lock_address': m.group('lock_address')}
                continue

            # FW persona un-created sessions due to max session limit: 10
            m = p6.match(line)
            if m:
                parsed_dict['fw_persona_uncreated_sessions'] = int(m.group('uncreated_sessions'))
                continue

            # FW persona agg-age sess teardown halfopen: 7, non-halfopen: 12
            m = p7.match(line)
            if m:
                parsed_dict['fw_persona_agg_age_sess_teardown'] = {
                    k: int(v) for k, v in m.groupdict().items()
                }
                continue

            #  FW persona number of times hostdb clear session stopped: 6
            m = p8.match(line)
            if m:
                parsed_dict['fw_persona_hostdb_clear_session_stopped'] = int(
                    m.group('clear_session_stopped')
                )
                continue

            # FW total number of thread: 8, number of cpu complex: 2
            m = p9.match(line)
            if m:
                parsed_dict['fw_total_number_of_thread'] = int(m.group('total_number_of_thread'))
                parsed_dict['number_of_cpu_complex'] = int(m.group('number_of_cpu_complex'))
                continue

        return parsed_dict

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSchema(MetaParser):
    """Schema for show platform hardware qfp active feature alg statistics"""
    schema = {
        'alg_counters': {
            Any(): {
                'cntrl_pkt': int,
                'parser_err_drop': int,
                'parser_no_act': int,
            }
        },
        'alg_chunk_pool': {
            Any(): {
                'used_entries': int,
                'free_entries': int,
            }
        },
        'common_alg_chunk_pool': {
            Any(): {
                'used_entries': int,
                'free_entries': int,
            }
        }
    }

class ShowPlatformHardwareQfpActiveFeatureAlgStatistics(ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSchema):
    """Parser for show platform hardware qfp active feature alg statistics"""

    cli_command = 'show platform hardware qfp active feature alg statistics'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # FTP         123      5         2
        p1 = re.compile(r'^(?P<alg>\S+)\s+(?P<cntrl_pkt>\d+)\s+(?P<parser_err_drop>\d+)\s+(?P<parser_no_act>\d+)$')

        # ftp-ctrl pool         15            10
        p2 = re.compile(r'^(?P<pool_name>[\S\s]+?)\s+(?P<used_entries>\d+)\s+(?P<free_entries>\d+)$')

        lines = output.splitlines()
        current_section = None

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if line.startswith('ALG counters:'):
                current_section = 'alg_counters'
                continue
            elif line.startswith('ALG chunk pool:'):
                current_section = 'alg_chunk_pool'
                continue
            elif line.startswith('Common ALG chunk pool:'):
                current_section = 'common_alg_chunk_pool'
                continue

            if 'ALG' in line or 'Pool-Name' in line or 'Used' in line:
                continue

            # # FTP         123      5         2
            if current_section == 'alg_counters':
                m = p1.match(line)  # Example match: "FTP  123  5  2"
                if m:
                    g = m.groupdict()
                    alg_dict = parsed_dict.setdefault('alg_counters', {})
                    alg_dict[g['alg']] = {
                        'cntrl_pkt': int(g['cntrl_pkt']),
                        'parser_err_drop': int(g['parser_err_drop']),
                        'parser_no_act': int(g['parser_no_act']),
                    }

            # ftp-ctrl pool         15            10
            elif current_section in ['alg_chunk_pool', 'common_alg_chunk_pool']:
                m = p2.match(line)  # Example match: "ftp-ctrl pool  15  10"
                if m:
                    g = m.groupdict()
                    pool_dict = parsed_dict.setdefault(current_section, {})
                    pool_dict[g['pool_name']] = {
                        'used_entries': int(g['used_entries']),
                        'free_entries': int(g['free_entries']),
                    }

        return parsed_dict

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsDnsSchema(MetaParser):
    '''Schema for show platform hardware qfp active feature alg statistics dns'''
    schema = {
            'dns_info_pool_used_chunk_entries_number': int,
            'dns_query': int,
            'dns_response': int,
            'other_msg': int,
            'create_chunk': int,
            'del_chunk': int,
            'format_err': int,
            'chunk_allocfail': int,
            'find_name_end_err': int,
            'create_txt_tokenerr': int,
            'create_binary_token_err': int,
            'parse_error': int,
            'name_overwritten_after_free': int,
            'invalid_protocol': int,
            'add_alg_state_fail': int,
            Optional("counters_cleared"): bool
    }

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsDns(ShowPlatformHardwareQfpActiveFeatureAlgStatisticsDnsSchema):
    '''Parser for show platform hardware qfp active feature alg statistics dns
       Parser for show platform hardware qfp active feature alg statistics dns {clear}'''
    cli_command = [ 'show platform hardware qfp active feature alg statistics dns'
                    'show platform hardware qfp active feature alg statistics dns {clear}']

    def cli(self, clear="", output=None):
        if output is None:
            if clear:
                cmd = self.cli_command[1].format(clear=clear)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        parsed = {}

        # DNS info pool used chunk entries number: 0
        p1 = re.compile(r'^DNS info pool used chunk entries number: +(?P<dns_info_pool_used_chunk_entries_number>\d+)$')
        # dns query:                             0
        p2 = re.compile(r'^dns query: +(?P<dns_query>\d+)$')
        # dns response:                          0
        p3 = re.compile(r'^dns response: +(?P<dns_response>\d+)$')
        # other msg:                             0
        p4 = re.compile(r'^other msg: +(?P<other_msg>\d+)$')
        # create chunk:                          0
        p5 = re.compile(r'^create chunk: +(?P<create_chunk>\d+)$')
        # del_chunk:                             0
        p6 = re.compile(r'^del_chunk: +(?P<del_chunk>\d+)$')
        # format err:                            0
        p7 = re.compile(r'^format err: +(?P<format_err>\d+)$')
        # chunk allocfail:                       0
        p8 = re.compile(r'^chunk allocfail: +(?P<chunk_allocfail>\d+)$')
        # find name end err:                     0
        p9 = re.compile(r'^find name end err: +(?P<find_name_end_err>\d+)$')
        #create txt tokenerr:                   0
        p10 = re.compile(r'^create txt tokenerr: +(?P<create_txt_tokenerr>\d+)$')
        # create binary token err:               0
        p11 = re.compile(r'^create binary token err: +(?P<create_binary_token_err>\d+)$')
        # parse error:                           0
        p12 = re.compile(r'^parse error: +(?P<parse_error>\d+)$')
        # name overwritten after free:           0
        p13 = re.compile(r'^name overwritten after free: +(?P<name_overwritten_after_free>\d+)$')
        # invalid protocol:                      0
        p14 = re.compile(r'^invalid protocol: +(?P<invalid_protocol>\d+)$')
        # add alg state fail:                    0
        p15 = re.compile(r'^add alg state fail: +(?P<add_alg_state_fail>\d+)$')
        # DNS ALG counters cleared after display.
        p16 = re.compile(r'^DNS ALG counters cleared after display.$')

        for line in output.splitlines():
            line = line.strip()

            # DNS info pool used chunk entries number: 0
            match = p1.match(line)
            if match:
                parsed['dns_info_pool_used_chunk_entries_number'] = int(match.group('dns_info_pool_used_chunk_entries_number'))
                continue

            # dns query:                             0
            match = p2.match(line)
            if match:
                parsed['dns_query'] = int(match.group('dns_query'))
                continue

            # dns response:                          0
            match = p3.match(line)
            if match:
                parsed['dns_response'] = int(match.group('dns_response'))
                continue

            # other msg:                             0
            match = p4.match(line)
            if match:
                parsed['other_msg'] = int(match.group('other_msg'))
                continue

            # create chunk:                          0
            match = p5.match(line)
            if match:
                parsed['create_chunk'] = int(match.group('create_chunk'))
                continue

            # del_chunk:                             0
            match = p6.match(line)
            if match:
                parsed['del_chunk'] = int(match.group('del_chunk'))
                continue

            # format err:                            0
            match = p7.match(line)
            if match:
                parsed['format_err'] = int(match.group('format_err'))
                continue

            # chunk allocfail:                       0
            match = p8.match(line)
            if match:
                parsed['chunk_allocfail'] = int(match.group('chunk_allocfail'))
                continue

            # find name end err:                     0
            match = p9.match(line)
            if match:
                parsed['find_name_end_err'] = int(match.group('find_name_end_err'))
                continue

            # create txt tokenerr:                   0
            match = p10.match(line)
            if match:
                parsed['create_txt_tokenerr'] = int(match.group('create_txt_tokenerr'))
                continue

            # create binary token err:               0
            match = p11.match(line)
            if match:
                parsed['create_binary_token_err'] = int(match.group('create_binary_token_err'))
                continue

            # parse error:                           0
            match = p12.match(line)
            if match:
                parsed['parse_error'] = int(match.group('parse_error'))
                continue

            # name overwritten after free:           0
            match = p13.match(line)
            if match:
                parsed['name_overwritten_after_free'] = int(match.group('name_overwritten_after_free'))
                continue

            # invalid protocol:                      0
            match = p14.match(line)
            if match:
                parsed['invalid_protocol'] = int(match.group('invalid_protocol'))
                continue

            # add alg state fail:                    0
            match = p15.match(line)
            if match:
                parsed['add_alg_state_fail'] = int(match.group('add_alg_state_fail'))
                continue

            # DNS ALG counters cleared after display.
            match = p16.match(line)
            if match:
                parsed['counters_cleared'] = True
                continue

        return parsed

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSmtpSchema(MetaParser):
    '''Schema for show platform hardware qfp active feature alg statistics smtp'''
    schema = {
        'total_packets_parsed': {
            'request': int,
            'response': int,
        },
        'total_packets_policy_inspected': {
            'request': int,
            'response': int,
        },
        'memory_management': {
            'scb': {
                'alloc': int,
                'free': int,
                'low_mem_req': int,
                'alloc_fail': int,
            },
            'command_element': {
                'alloc': int,
                'free': int,
                'low_mem_req': int,
            },
            'log_element': {
                'alloc': int,
                'free': int,
                'low_mem_req': int,
            },
            'mask_element': {
                'alloc': int,
                'free': int,
                'low_mem_req': int,
            },
        },
        'reset_session': {
            'cli_match': int,
            'no_smtp_engine': int,
            'failover_detect': int,
            'sw_error': int,
            'dirty_bit': {
                'new_session': int,
                'exist_session': int,
                'after_parse': int,
                'after_match': int,
            },
        },
        'abort_inspection_info': {
            'policy_not_exist': int,
            'retransmit_packet': int,
        },
        Optional("counters_cleared"): bool
    }

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSmtp(ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSmtpSchema):
    '''Parser for show platform hardware qfp active feature alg statistics smtp
       Parser for show platform hardware qfp active feature alg statistics smtp {clear}'''
    cli_command = [
                   'show platform hardware qfp active feature alg statistics smtp',
                   'show platform hardware qfp active feature alg statistics smtp {clear}'
                  ]

    def cli(self,
            clear="",
            output=None):

        if output is None:
            if clear:
                cmd = self.cli_command[1].format(clear=clear)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Initialize the parsed  dictionary
        parsed = {}   
        # Total packts parsed:
        p1 = re.compile(r'^Total packts parsed:$')
        # request: 12
        p2 = re.compile(r'^.*request: +(?P<request>\d+)$')
        # response: 13
        p3 = re.compile(r'^.*response: +(?P<response>\d+)$')
        # Total packets policy-inspected:
        p4 = re.compile(r'^Total packets policy-inspected:$')
        # Memory management:
        p5 = re.compile(r'^Memory management:$')
        # scb - alloc: 1, free: 1, low mem req: 0, alloc fail: 0
        p6 = re.compile(r'^.*scb - alloc: +(?P<alloc>\d+), free: +(?P<free>\d+), low mem req: +(?P<low_mem_req>\d+), alloc fail: +(?P<alloc_fail>\d+)$')
        # command element - alloc: 20, free: 20, low mem req: 0
        p7 = re.compile(r'^.*command element - alloc: +(?P<alloc>\d+), free: +(?P<free>\d+), low mem req: +(?P<low_mem_req>\d+)$')
        # log element - alloc: 1, free: 1, low mem req: 0
        p8 = re.compile(r'^.*log element - alloc: +(?P<alloc>\d+), free: +(?P<free>\d+), low mem req: +(?P<low_mem_req>\d+)$')
        # mask element - alloc: 3, free: 3, low mem req: 0
        p9 = re.compile(r'^.*mask element - alloc: +(?P<alloc>\d+), free: +(?P<free>\d+), low mem req: +(?P<low_mem_req>\d+)$')
        # Reset session:
        p10 = re.compile(r'^Reset session:$')
        # CLI match: 0
        p11 = re.compile(r'^.*CLI match: +(?P<cli_match>\d+)$')
        # no smtp engine: 0
        p12 = re.compile(r'^.*no smtp engine: +(?P<no_smtp_engine>\d+)$')
        # failover detect: 0
        p13 = re.compile(r'^.*failover detect: +(?P<failover_detect>\d+)$')
        # sw error: 0
        p14 = re.compile(r'^.*sw error: +(?P<sw_error>\d+)$')
        # dirty-bit - new session: 0, exist session: 0, after parse: 0, after match: 0
        p15 = re.compile(r'^.*dirty-bit - new session: +(?P<new_session>\d+), exist session: +(?P<exist_session>\d+), after parse: +(?P<after_parse>\d+), after match: +(?P<after_match>\d+)$')
        # Abort inspection info:
        p16 = re.compile(r'^Abort inspection info:$')
        # policy not-exist: 0
        p17 = re.compile(r'^.*policy not-exist: +(?P<policy_not_exist>\d+)$')
        # retransmit packet: 0
        p18 = re.compile(r'^.*retransmit packet: +(?P<retransmit_packet>\d+)$')
        # SMTP counters cleared
        p19 = re.compile(r'^SMTP counters cleared$')

        for line in output.splitlines():
            line = line.strip()

           #Total packts parsed:
            match = p1.match(line)
            if match:
                parsed.setdefault('total_packets_parsed', {})
                continue

            # request: 12
            match = p2.match(line)
            if match:
                if 'total_packets_policy_inspected' in parsed:
                    parsed['total_packets_policy_inspected']['request'] = int(match.group('request'))
                else:
                    parsed['total_packets_parsed']['request'] = int(match.group('request'))
                continue

            # response: 13
            match = p3.match(line)
            if match:
                if 'total_packets_policy_inspected' in parsed:
                    parsed['total_packets_policy_inspected']['response'] = int(match.group('response'))
                else:
                    parsed['total_packets_parsed']['response'] = int(match.group('response'))
                continue

            # Total packets policy-inspected:
            match = p4.match(line)
            if match:
                parsed.setdefault('total_packets_policy_inspected', {})
                continue

            # Memory management:
            match = p5.match(line)
            if match:
                parsed.setdefault('memory_management', {})
                continue

            # scb - alloc: 1, free: 1, low mem req: 0, alloc fail: 0
            match = p6.match(line)
            if match:
                parsed['memory_management'].setdefault('scb', {})
                parsed['memory_management']['scb']['alloc'] = int(match.group('alloc'))
                parsed['memory_management']['scb']['free'] = int(match.group('free'))
                parsed['memory_management']['scb']['low_mem_req'] = int(match.group('low_mem_req'))
                parsed['memory_management']['scb']['alloc_fail'] = int(match.group('alloc_fail'))
                continue

            # command element - alloc: 20, free: 20, low mem req: 0
            match = p7.match(line)
            if match:
                parsed['memory_management'].setdefault('command_element', {})
                parsed['memory_management']['command_element']['alloc'] = int(match.group('alloc'))
                parsed['memory_management']['command_element']['free'] = int(match.group('free'))
                parsed['memory_management']['command_element']['low_mem_req'] = int(match.group('low_mem_req'))
                continue

            # log element - alloc: 1, free: 1, low mem req: 0
            match = p8.match(line)
            if match:
                parsed['memory_management'].setdefault('log_element', {})
                parsed['memory_management']['log_element']['alloc'] = int(match.group('alloc'))
                parsed['memory_management']['log_element']['free'] = int(match.group('free'))
                parsed['memory_management']['log_element']['low_mem_req'] = int(match.group('low_mem_req'))
                continue

            # mask element - alloc: 3, free: 3, low mem req: 0
            match = p9.match(line)
            if match:
                parsed['memory_management'].setdefault('mask_element', {})
                parsed['memory_management']['mask_element']['alloc'] = int(match.group('alloc'))
                parsed['memory_management']['mask_element']['free'] = int(match.group('free'))
                parsed['memory_management']['mask_element']['low_mem_req'] = int(match.group('low_mem_req'))
                continue

            # Reset session:
            match = p10.match(line)
            if match:
                parsed.setdefault('reset_session', {})
                continue

            # CLI match: 0
            match = p11.match(line)
            if match:
                parsed['reset_session']['cli_match'] = int(match.group('cli_match'))
                continue

            # no smtp engine: 0
            match = p12.match(line)
            if match:
                parsed['reset_session']['no_smtp_engine'] = int(match.group('no_smtp_engine'))
                continue

            # failover detect: 0
            match = p13.match(line)
            if match:
                parsed['reset_session']['failover_detect'] = int(match.group('failover_detect'))
                continue

            # sw error: 0
            match = p14.match(line)
            if match:
                parsed['reset_session']['sw_error'] = int(match.group('sw_error'))
                continue

            # dirty-bit - new session: 0, exist session: 0, after parse: 0, after match: 0
            match = p15.match(line)
            if match:
                parsed['reset_session'].setdefault('dirty_bit', {})
                parsed['reset_session']['dirty_bit']['new_session'] = int(match.group('new_session'))
                parsed['reset_session']['dirty_bit']['exist_session'] = int(match.group('exist_session'))
                parsed['reset_session']['dirty_bit']['after_parse'] = int(match.group('after_parse'))
                parsed['reset_session']['dirty_bit']['after_match'] = int(match.group('after_match'))
                continue

            # Abort inspection info:
            match = p16.match(line)
            if match:
                parsed.setdefault('abort_inspection_info', {})
                continue

            # policy not-exist: 0
            match = p17.match(line)
            if match:
                parsed['abort_inspection_info']['policy_not_exist'] = int(match.group('policy_not_exist'))
                continue

            # retransmit packet: 0
            match = p18.match(line)
            if match:
                parsed['abort_inspection_info']['retransmit_packet'] = int(match.group('retransmit_packet'))
                continue

            # SMTP counters cleared
            match = p19.match(line)
            if match:
                parsed['counters_cleared'] = True
                continue

        return parsed

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSunrpcSchema(MetaParser):
    '''Schema for show platform hardware qfp active feature alg statistics sunrpc'''
    schema = {
        'global_info': {
            'total_pkts_passed_inspection': int,
            'call': int,
            'reply': int,
            'non_data': int,
            'procedures': {
                'get_port': int,
                'call_it': int,
                'dump': int,
                'other': int,
            },
            'rpcbind_v3_v4': int,
            'duplicate_xid': int,
            'vfred_packets': int
        },
        'drop_counters': {
            'total_dropped': int,
            'fatal_error': {
                'internal_sw_error': int,
            },
            'info': {
                'pkt_malformed': int,
                'pkt_too_short': int,
                'xid_mismatch': int,
                'rpc_ver_not_supported': int,
                'tcp_record_is_not_last_frag': int,
            },
            'packets_subject_to_policy_inspection': {
                'policy_not_exist': int,
                'policy_dirty_bit_set': int,
                'policy_mismatch': int,
            },
            Optional("counters_cleared"): bool
        },
	'memory_management': {
            'chunk': {
                'requested': int,
                'returned': int,
            },
            'l7_scb': {
                'allocated': int,
                'freed': int,
                'failed': int,
            },
            'l7_pkt': {
                'allocated': int,
                'freed': int,
                'failed': int,
            },
	},
	Optional("counters_cleared"): bool
    }

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSunrpc(ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSunrpcSchema):
    '''Parser for show platform hardware qfp active feature alg statistics sunrpc
       Parser for show platform hardware qfp active feature alg statistics sunrpc clear'''
    cli_command = [
                      'show platform hardware qfp active feature alg statistics sunrpc',
                      'show platform hardware qfp active feature alg statistics sunrpc {clear}'
                  ]

    def cli(self, clear="", output=None):

        if output is None:
            if clear:
                cmd = self.cli_command[1].format(clear=clear)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
  
        # Initialize the parsed dictionary
        parsed = {}

        # Global info:
        p1 = re.compile(r'^Global info:$')
        # Total pkts passed inspection:2
        p2 = re.compile(r'^\s*Total pkts passed inspection:\s*(?P<total_pkts_passed_inspection>\d+)$')
        # Call: 1
        p3 = re.compile(r'^\s*Call:\s*(?P<call>\d+)$')
        # Reply: 1
        p4 = re.compile(r'^\s*Reply:\s*(?P<reply>\d+)$')
        # Non Data: 0
        p5 = re.compile(r'^\s*Non Data:\s*(?P<non_data>\d+)$')
        # Procedures - GetPort: 1, CallIt: 0, Dump: 0, Other: 0
        p6 = re.compile(r'^\s*Procedures - GetPort:\s*(?P<get_port>\d+), CallIt:\s*(?P<call_it>\d+), Dump:\s*(?P<dump>\d+), Other:\s*(?P<other>\d+)$')
        # RPCBIND (V3/V4): 0
        p7 = re.compile(r'^\s*RPCBIND \(V3/V4\):\s*(?P<rpcbind_v3_v4>\d+)$')
        # Duplicate XID: 0
        p8 = re.compile(r'^\s*Duplicate XID:\s*(?P<duplicate_xid>\d+)$')
        # VFRed packets: 0
        p9 = re.compile(r'^\s*VFRed packets:\s*(?P<vfred_packets>\d+)$')
        # Drop counters:
        p10 = re.compile(r'^Drop counters:$')
        # Total dropped: 0
        p11 = re.compile(r'^\s*Total dropped:\s*(?P<total_dropped>\d+)$')
        # Fatal error:
        p12 = re.compile(r'^\s*Fatal error:$')
        # Internal SW error: 0
        p13 = re.compile(r'^\s*Internal SW error:\s*(?P<internal_sw_error>\d+)$')
        # Info:
        p14 = re.compile(r'^\s*Info:$')
        # Pkt malformed: 0
        p15 = re.compile(r'^\s*Pkt malformed:\s*(?P<pkt_malformed>\d+)$')
        # Pkt too short: 0
        p16 = re.compile(r'^\s*Pkt too short:\s*(?P<pkt_too_short>\d+)$')
        # XID mismatch: 0
        p17 = re.compile(r'^\s*XID mismatch:\s*(?P<xid_mismatch>\d+)$')
        # RPC ver not supported: 0
        p18 = re.compile(r'^\s*RPC ver not supported:\s*(?P<rpc_ver_not_supported>\d+)$')
        # TCP record is not last frag: 0
        p19 = re.compile(r'^\s*TCP record is not last frag:\s*(?P<tcp_record_is_not_last_frag>\d+)$')
        # Packets subject to policy inspection:
        p20 = re.compile(r'^\s*Packets subject to policy inspection:$')
        # Policy not-exist: 0
        p21 = re.compile(r'^\s*Policy not-exist:\s*(?P<policy_not_exist>\d+)$')
        # Policy dirty-bit set: 0
        p22 = re.compile(r'^\s*Policy dirty-bit set:\s*(?P<policy_dirty_bit_set>\d+)$')
        # Policy-mismatch: 0
        p23 = re.compile(r'^\s*Policy-mismatch:\s*(?P<policy_mismatch>\d+)$')
        p24 = re.compile(r'^SunRPC ALG counters cleared after display.$')
        # Memory management:
        p25 = re.compile(r'^Memory management:$')
        # Chunk -  requested: 0, returned: 0
        p26 = re.compile(r'^\s*Chunk -  requested:\s*(?P<requested>\d+), returned:\s*(?P<returned>\d+)$')
        # L7 scb - allocated: 1, freed: 0, failed: 0
        p27 = re.compile(r'^\s*L7 scb - allocated:\s*(?P<allocated>\d+), freed:\s*(?P<freed>\d+), failed:\s*(?P<failed>\d+)$')
        # L7 pkt - allocated: 0, freed: 0, failed: 0
        p28 = re.compile(r'^\s*L7 pkt - allocated:\s*(?P<allocated>\d+), freed:\s*(?P<freed>\d+), failed:\s*(?P<failed>\d+)$')
        # SunRPC ALG counters cleared after display.
        p29 = re.compile(r'^SunRPC ALG counters cleared after display.$')

        for line in output.splitlines():
            line = line.strip()
            # Global info:
            match = p1.match(line)
            if match:
                parsed.setdefault('global_info', {})
                continue

            # Total pkts passed inspection:2
            match = p2.match(line)
            if match:
                parsed['global_info']['total_pkts_passed_inspection'] = int(match.group('total_pkts_passed_inspection'))
                continue

            # Call: 1
            match = p3.match(line)
            if match:
                parsed['global_info']['call'] = int(match.group('call'))
                continue

            # Reply: 1
            match = p4.match(line)
            if match:
                parsed['global_info']['reply'] = int(match.group('reply'))
                continue

            # Non Data: 0
            match = p5.match(line)
            if match:
                parsed['global_info']['non_data'] = int(match.group('non_data'))
                continue

            # Procedures - GetPort: 1, CallIt: 0, Dump: 0, Other: 0
            match = p6.match(line)
            if match:
                parsed['global_info'].setdefault('procedures', {})
                parsed['global_info']['procedures']['get_port'] = int(match.group('get_port'))
                parsed['global_info']['procedures']['call_it'] = int(match.group('call_it'))
                parsed['global_info']['procedures']['dump'] = int(match.group('dump'))
                parsed['global_info']['procedures']['other'] = int(match.group('other'))
                continue

           # RPCBIND (V3/V4): 0
            match = p7.match(line)
            if match:
                parsed['global_info']['rpcbind_v3_v4'] = int(match.group('rpcbind_v3_v4'))
               #parsed['global_info']['rpcbind']['v3'] = 0
                #parsed['global_info']['rpcbind']['v4'] = 0
                continue

            # Duplicate XID: 0
            match = p8.match(line)
            if match:
                parsed['global_info']['duplicate_xid'] = int(match.group('duplicate_xid'))
                continue
      
            # VFRed packets: 0
            match = p9.match(line)
            if match:
                parsed['global_info']['vfred_packets'] = int(match.group('vfred_packets'))
                continue

            # Drop counters:
            match = p10.match(line)
            if match:
                parsed.setdefault('drop_counters', {})
                continue

            # Total dropped: 0
            match = p11.match(line)
            if match:
                parsed['drop_counters']['total_dropped'] = int(match.group('total_dropped'))
                continue
    
            # Fatal error:
            match = p12.match(line)
            if match:
                parsed['drop_counters'].setdefault('fatal_error', {})
                continue

            # Internal SW error: 0
            match = p13.match(line)
            if match:
                parsed['drop_counters']['fatal_error']['internal_sw_error'] = int(match.group('internal_sw_error'))
                continue

            # Info:
            match = p14.match(line)
            if match:
                parsed['drop_counters'].setdefault('info', {})
                continue

            # Pkt malformed: 0
            match = p15.match(line)
            if match:
                parsed['drop_counters']['info']['pkt_malformed'] = int(match.group('pkt_malformed'))
                continue

            # Pkt too short: 0
            match = p16.match(line)
            if match:
                parsed['drop_counters']['info']['pkt_too_short'] = int(match.group('pkt_too_short'))
                continue

            # XID mismatch: 0
            match = p17.match(line)
            if match:
                parsed['drop_counters']['info']['xid_mismatch'] = int(match.group('xid_mismatch'))
                continue

            # RPC ver not supported: 0
            match = p18.match(line)
            if match:
                parsed['drop_counters']['info']['rpc_ver_not_supported'] = int(match.group('rpc_ver_not_supported'))
                continue

            # TCP record is not last frag: 0
            match = p19.match(line)
            if match:
                parsed['drop_counters']['info']['tcp_record_is_not_last_frag'] = int(match.group('tcp_record_is_not_last_frag'))
                continue

            # Packets subject to policy inspection:
            match = p20.match(line)
            if match:
                parsed['drop_counters'].setdefault('packets_subject_to_policy_inspection', {})
                continue

            # Policy not-exist: 0
            match = p21.match(line)
            if match:
                parsed['drop_counters']['packets_subject_to_policy_inspection']['policy_not_exist'] = int(match.group('policy_not_exist'))
                continue

            # Policy dirty-bit set: 0
            match = p22.match(line)
            if match:
                parsed['drop_counters']['packets_subject_to_policy_inspection']['policy_dirty_bit_set'] = int(match.group('policy_dirty_bit_set'))
                continue

            # Policy-mismatch: 0
            match = p23.match(line)
            if match:
                parsed['drop_counters']['packets_subject_to_policy_inspection']['policy_mismatch'] = int(match.group('policy_mismatch'))
                continue

            # SunRPC ALG counters cleared after display.
            match = (p24.match(line) and p29.match(line))
            if match:
                parsed['counters_cleared'] = True
                continue

            # Memory management:
            match = p25.match(line)
            if match:
                parsed.setdefault('memory_management', {})
                continue
  
            # Chunk -  requested: 0, returned: 0
            match = p26.match(line)
            if match:
                parsed['memory_management'].setdefault('chunk', {})
                parsed['memory_management']['chunk']['requested'] = int(match.group('requested'))
                parsed['memory_management']['chunk']['returned'] = int(match.group('returned'))
                continue

            # L7 scb - allocated: 1, freed: 0, failed: 0
            match = p27.match(line)
            if match:
                parsed['memory_management'].setdefault('l7_scb', {})
                parsed['memory_management']['l7_scb']['allocated'] = int(match.group('allocated'))
                parsed['memory_management']['l7_scb']['freed'] = int(match.group('freed'))
                parsed['memory_management']['l7_scb']['failed'] = int(match.group('failed'))
                continue

            # L7 pkt - allocated: 0, freed: 0, failed: 0
            match = p28.match(line)
            if match:
                parsed['memory_management'].setdefault('l7_pkt', {})
                parsed['memory_management']['l7_pkt']['allocated'] = int(match.group('allocated'))
                parsed['memory_management']['l7_pkt']['freed'] = int(match.group('freed'))
                parsed['memory_management']['l7_pkt']['failed'] = int(match.group('failed'))
                continue
  
        return parsed

class ShowPlatformHardwareQfpActiveFeatureNatDataStatsSchema(MetaParser):
    """Schema for show platform hardware qfp active feature nat data stats"""
    schema = {
        'counters': {
            Any(): int,
        }
    }

class ShowPlatformHardwareQfpActiveFeatureNatDataStats(ShowPlatformHardwareQfpActiveFeatureNatDataStatsSchema):
    """Parser for show platform hardware qfp active feature nat data stats"""

    cli_command = 'show platform hardware qfp active feature nat data stats'

    def cli(self, output=None):
        if output is None:
            # Execute the command to get the output
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expression to capture the counter names and values
        # number_of_session                                                 0
        p1 = re.compile(r'^(?P<counter>\w+)\s+(?P<value>\d+$)')

        # Split the output into lines
        lines = output.splitlines()

        # Iterate over each line
        for line in lines:
            # Strip leading and trailing whitespace
            line = line.strip()
            # match counter and value
            # Counter                                                       Value
            # ------------------------------------------------------------------------
            # number_of_session                                                 0
            m = p1.match(line)
            if m:
                counter = m.group('counter')
                value = int(m.group('value'))
                parsed_dict.setdefault('counters', {}).setdefault(counter, value)
                continue
        return parsed_dict

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsPop3Schema(MetaParser):
    '''Schema for show platform hardware qfp active feature alg statistics pop3 '''
    schema = {
        'total_packets_parsed': {
            'request': int,
            'response': int,
        },
        'total_packets_policy_inspected': {
            'request': int,
        },
        'memory_management': {
            'scb': {
                'alloc': int,
                'free': int,
                'low_mem_req': int,
                'alloc_fail': int,
            },
        },
        'reset_session': {
            'cli_match': int,
            'no_pop3_engine': int,
            'dirty_bit': {
                'new_session': int,
                'exist_session': int,
                'after_parse': int,
                'after_match': int,
            },
        },
        'drop_packets_info': {
            'no_regex_table': int,
            'fragmented_packet': int,
            'command_pending': int,
        },
        'abort_inspection_info': {
            'policy_not_exist': int,
        },
        Optional("counters_cleared"): bool
    }

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsPop3(ShowPlatformHardwareQfpActiveFeatureAlgStatisticsPop3Schema):
    """
        Parser for show platform hardware qfp active feature alg statistics pop3
        Parser for show platform hardware qfp active feature alg statistics pop3 {clear}
        """
    cli_command = [
                       'show platform hardware qfp active feature alg statistics pop3',
                       'show platform hardware qfp active feature alg statistics pop3 {clear}'
                  ]


    def cli(self,clear="",output=None):

        if output is None:
            if clear:
                cmd = self.cli_command[1].format(clear=clear)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Total packets parsed:
        p1 = re.compile(r'^Total packets parsed:$')

        # request: 0
        p2 = re.compile(r'^.*request: +(?P<request>\d+)$')

        # response: 0
        p3 = re.compile(r'^.*response: +(?P<response>\d+)$')

        # Total packets policy-inspected:
        p4 = re.compile(r'^Total packets policy-inspected:$')

        # request: 0
        p5 = re.compile(r'^request:\s*(?P<request>\d+)$')

        # Memory management:
        p6 = re.compile(r'^Memory management:$')

        # scb - alloc 0, free 0, low mem req 0, alloc fail 0
        p7 = re.compile(r'^.*scb - alloc +(?P<alloc>\d+), free +(?P<free>\d+), low mem req +(?P<low_mem_req>\d+), alloc fail +(?P<alloc_fail>\d+)$')

        # Reset session:
        p8 = re.compile(r'^Reset session:$')

        # CLI match: 0
        p9 = re.compile(r'^.*CLI match: +(?P<cli_match>\d+)$')

        # no pop3 engine: 0
        p10 = re.compile(r'^.*no pop3 engine: +(?P<no_pop3_engine>\d+)$')

        # dirty-bit - new session: 0, exist session: 0, after parse: 0, after match: 0
        p11 = re.compile(r'^.*dirty-bit - new session: +(?P<new_session>\d+), exist session: +(?P<exist_session>\d+), after parse: +(?P<after_parse>\d+), after match: +(?P<after_match>\d+)$')

        # Drop packets info:
        p12 = re.compile(r'^Drop packets info:$')

        # no regex table: 0
        p13 = re.compile(r'^.*no regex table: +(?P<no_regex_table>\d+)$')

        # fragmented packet: 0
        p14 = re.compile(r'^.*fragmented packet: +(?P<fragmented_packet>\d+)$')

        # command pending: 0
        p15 = re.compile(r'^.*command pending: +(?P<command_pending>\d+)$')

        # Abort inspection info:
        p16 = re.compile(r'^Abort inspection info:$')

        # policy not-exist: 0
        p17 = re.compile(r'^.*policy not-exist: +(?P<policy_not_exist>\d+)$')

        # POP3 counters cleared
        p18 = re.compile(r'^POP3 counters cleared$')

        for line in output.splitlines():
            line = line.strip()

            # Total packets parsed:
            match = p1.match(line)
            if match:
                packets_dict = parsed_dict.setdefault('total_packets_parsed', {})
                continue

            # request: 0
            match = p2.match(line)
            if match:
                if 'total_packets_policy_inspected' in parsed_dict:
                    parsed_dict['total_packets_policy_inspected']['request'] = int(match.group('request'))
                else:
                    packets_dict['request'] = int(match.group('request'))
                continue

            # response: 0
            match = p3.match(line)
            if match:
                parsed_dict['total_packets_parsed']['response'] = int(match.group('response'))
                continue

            # Total packets policy-inspected:
            match = p4.match(line)
            if match:
                parsed_dict.setdefault('total_packets_policy_inspected', {})
                continue

            # Memory management:
            match = p6.match(line)
            if match:
                parsed_dict.setdefault('memory_management', {})
                mem_dict = parsed_dict['memory_management'].setdefault('scb', {})
                continue

            # scb - alloc 0, free 0, low mem req 0, alloc fail 0
            match = p7.match(line)
            if match:
                mem_dict['alloc'] = int(match.group('alloc'))
                mem_dict['free'] = int(match.group('free'))
                mem_dict['low_mem_req'] = int(match.group('low_mem_req'))
                mem_dict['alloc_fail'] = int(match.group('alloc_fail'))
                continue

            # Reset session:
            match = p8.match(line)
            if match:
                parsed_dict.setdefault('reset_session', {'cli_match': 0, 'no_pop3_engine': 0, 'dirty_bit': {'new_session': 0, 'exist_session': 0, 'after_parse': 0, 'after_match': 0}})
                parsed_dict['reset_session'].setdefault('dirty_bit', {})
                continue

            # CLI match: 0
            match = p9.match(line)
            if match:
                parsed_dict['reset_session']['cli_match'] = int(match.group('cli_match'))
                continue

            # no pop3 engine: 0
            match = p10.match(line)
            if match:
                parsed_dict['reset_session']['no_pop3_engine'] = int(match.group('no_pop3_engine'))
                continue

            # dirty-bit - new session: 0, exist session: 0, after parse: 0, after match: 0
            match = p11.match(line)
            if match:
                parsed_dict['reset_session']['dirty_bit']['new_session'] = int(match.group('new_session'))
                parsed_dict['reset_session']['dirty_bit']['exist_session'] = int(match.group('exist_session'))
                parsed_dict['reset_session']['dirty_bit']['after_parse'] = int(match.group('after_parse'))
                continue

            # Drop packets info:
            match = p12.match(line)
            if match:
                parsed_dict.setdefault('drop_packets_info', {'fragmented_packet': 0})
                continue

            # no regex table: 0
            match = p13.match(line)
            if match:
                parsed_dict['drop_packets_info']['no_regex_table'] = int(match.group('no_regex_table'))
                continue

            # fragmented packet: 0
            match = p14.match(line)
            if match:
                parsed_dict['drop_packets_info']['fragmented_packet'] = int(match.group('fragmented_packet'))
                continue

            # command pending: 0
            match = p15.match(line)
            if match:
                parsed_dict['drop_packets_info']['command_pending'] = int(match.group('command_pending'))
                continue

            # Abort inspection info:
            match = p16.match(line)
            if match:
                parsed_dict.setdefault('abort_inspection_info', {})
                continue

            # policy not-exist: 0
            match = p17.match(line)
            if match:
                parsed_dict['abort_inspection_info']['policy_not_exist'] = int(match.group('policy_not_exist'))
                continue

            # POP3 counters cleared
            match = p18.match(line)
            if match:
                parsed_dict['counters_cleared'] = True
                continue

        return parsed_dict

class ShowPlatformHardwareQfpActiveFeatureFirewallClientStatisticsSchema(MetaParser):
    '''Schema for show platform hardware qfp active feature firewall client statistics'''
    schema = {
        'zonepair_entry_count': int,
        'filler_block_count': int,
        'action_block_count': int,
        'l7_params_block_count': int,
        'statistics_table_count': int,
        'statistics_block_count': int,
        'class_name_table_entry_count': int,
        'number_of_vrf_interfaces_with_zone': int,
        'number_of_zoned_interfaces': int,
        'number_of_zones': int,
        'number_of_zone_pairs_with_policy': int,
        'number_of_avc_policy': int,
        'inspect_parameter_map_count': int,
        'multi_tenancy': str,
        'pending_multi_tenancy': str,
        'vrf_related_objects': {
            'vrf_parameter_map_count': int,
            'vrf_parameter_map_binding_count': int,
            'vrf_stats': int,
            'vrf_drop_stats': int,
        },
        'zone_related_objects': {
            'zone_parameter_map_count': int,
            'zone_parameter_map_binding_count': int,
        },
        'scb_pool': {
            'number_of_entries': int,
            'entry_limit': int,
            'size': int,
            'number_of_additions': int,
        },
        'synflood_hostdb_pool': {
            'number_of_entries': int,
            'entry_limit': int,
            'size': int,
            'number_of_additions': int,
        },
        'session_teardown_pool': {
            'number_of_entries': int,
            'entry_limit': int,
            'size': int,
            'number_of_additions': int,
        },
        'syncookie_destination_pool': {
            'number_of_entries': int,
            'entry_limit': int,
            'size': int,
            'number_of_additions': int,
        },
        'errors': {
            'failed_to_zero_global_drop_stats': int,
            'failed_to_allocate_drop_stats': int,
            'failed_to_zero_global_resource_stats': int,
            'failed_to_allocate_resource_stats': int,
            'failed_to_walk_vrf_domains': int,
            'failed_to_re_enable_firewall': int,
            'failed_to_disable_firewall': int,
            'failed_to_allocate_clear_command_buffer': int,
            'failed_to_send_clear_session_ipc': int,
        }
    }

class ShowPlatformHardwareQfpActiveFeatureFirewallClientStatistics(ShowPlatformHardwareQfpActiveFeatureFirewallClientStatisticsSchema):
    '''Parser for show platform hardware qfp active feature firewall client statistics'''
    cli_command = 'show platform hardware qfp active feature firewall client statistics'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        parsed = {}

        #Zonepair table entry count: 1
        p1 = re.compile(r'^Zonepair table entry count: +(?P<zonepair_entry_count>\d+)$')

        #Filler block count: 2
        p2 = re.compile(r'^Filler block count: +(?P<filler_block_count>\d+)$')

        #Action block count: 2
        p3 = re.compile(r'^Action block count: +(?P<action_block_count>\d+)$')

        #L7 params block count: 0
        p4 = re.compile(r'^L7 params block count: +(?P<l7_params_block_count>\d+)$')

        #Statistics table count: 2
        p5 = re.compile(r'^Statistics table count: +(?P<statistics_table_count>\d+)$')

        #Statistics block count: 8
        p6 = re.compile(r'^Statistics block count: +(?P<statistics_block_count>\d+)$')

        #Class name table entry count: 2
        p7 = re.compile(r'^Class name table entry count: +(?P<class_name_table_entry_count>\d+)$')

        #Number of vrf interfaces with zone: 0
        p8 = re.compile(r'^Number of vrf interfaces with zone: +(?P<number_of_vrf_interfaces_with_zone>\d+)$')

        #Number of zoned interfaces: 2
        p9 = re.compile(r'^Number of zoned interfaces: +(?P<number_of_zoned_interfaces>\d+)$')

        #Number of zones: 2
        p10 = re.compile(r'^Number of zones: +(?P<number_of_zones>\d+)$')

        #Number of zone pairs with policy: 1
        p11 = re.compile(r'^Number of zone pairs with policy: +(?P<number_of_zone_pairs_with_policy>\d+)$')

        #Number of AVC policy: 0
        p12 = re.compile(r'^Number of AVC policy: +(?P<number_of_avc_policy>\d+)$')

        #Inspect parameter map count: 1
        p13 = re.compile(r'^Inspect parameter map count: +(?P<inspect_parameter_map_count>\d+)$')

        #Multi-tenancy: No
        p14 = re.compile(r'^Multi-tenancy: +(?P<multi_tenancy>\w+)$')

        #Pending Multi-tenancy: No
        p15 = re.compile(r'^Pending Multi-tenancy: +(?P<pending_multi_tenancy>\w+)$')

        #VRF related objects:
        p16 = re.compile(r'^VRF related objects:$')

        #VRF-ParameterMap count: 1,
        p17 = re.compile(r'^\s*VRF-ParameterMap count: +(?P<vrf_parameter_map_count>\d+),$')

        #VRF-ParameterMap Binding count: 0,
        p18 = re.compile(r'^\s*VRF-ParameterMap Binding count: +(?P<vrf_parameter_map_binding_count>\d+),$')

        #VRF stats: 1,
        p19 = re.compile(r'^\s*VRF stats: +(?P<vrf_stats>\d+),$')

        #VRF drop stats: 1
        p20 = re.compile(r'^\s*VRF drop stats: +(?P<vrf_drop_stats>\d+)$')

        #Zone related objects:
        p21 = re.compile(r'^Zone related objects:$')

        #Zone-ParameterMap count: 0,
        p22 = re.compile(r'^\s*Zone-ParameterMap count: +(?P<zone_parameter_map_count>\d+),$')

        #Zone-ParameterMap Binding count: 0
        p23 = re.compile(r'^\s*Zone-ParameterMap Binding count: +(?P<zone_parameter_map_binding_count>\d+)$')

        #SCB pool:
        p24 = re.compile(r'^(?P<pool_name>.+ pool):$')

        #number of entries: 16384,
        p25 = re.compile(r'^\s*number of entries: +(?P<number_of_entries>\d+),$')

        #entry limit: 1048576,
        p26 = re.compile(r'^\s*entry limit: +(?P<entry_limit>\d+),$')

        #size: 8913728,
        p27 = re.compile(r'^\s*size: +(?P<size>\d+),$')

        #size: 11072, number of additions: 0
        p28 = re.compile(r'^\s*size: +(?P<size>\d+), number of additions: +(?P<number_of_additions>\d+)$')

        #number of additions: 0
        p29 = re.compile(r'^\s*number of additions: +(?P<number_of_additions>\d+)$')

        #entry limit: 0, size: 983872,
        p30 = re.compile(r'^\s*entry limit: +(?P<entry_limit>\d+), size: +(?P<size>\d+),$')

        #Errors:
        p31 = re.compile(r'^Errors:$')

        #Failed to zero global drop stats: 0,
        p32 = re.compile(r'^\s*Failed to zero global drop stats: +(?P<failed_to_zero_global_drop_stats>\d+),$')

        #Failed to allocate drop stats: 0,
        p33 = re.compile(r'^\s*Failed to allocate drop stats: +(?P<failed_to_allocate_drop_stats>\d+),$')

        #Failed to zero global resource stats: 0,
        p34 = re.compile(r'^\s*Failed to zero global resource stats: +(?P<failed_to_zero_global_resource_stats>\d+),$')

        #Failed to allocate resource stats: 0,
        p35 = re.compile(r'^\s*Failed to allocate resource stats: +(?P<failed_to_allocate_resource_stats>\d+),$')

        #Failed to walk vrf domains: 0,
        p36 = re.compile(r'^\s*Failed to walk vrf domains: +(?P<failed_to_walk_vrf_domains>\d+),$')

        #Failed to re-enable firewall: 0,
        p37 = re.compile(r'^\s*Failed to re-enable firewall: +(?P<failed_to_re_enable_firewall>\d+),$')

        #Failed to disable firewall: 0,
        p38 = re.compile(r'^\s*Failed to disable firewall: +(?P<failed_to_disable_firewall>\d+),$')

        #Failed to allocate clear command buffer: 0,
        p39 = re.compile(r'^\s*Failed to allocate clear command buffer: +(?P<failed_to_allocate_clear_command_buffer>\d+),$')

        #Failed to send clear session IPC: 0
        p40 = re.compile(r'^\s*Failed to send clear session IPC: +(?P<failed_to_send_clear_session_ipc>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #Zonepair table entry count: 1
            m = p1.match(line)
            if m:
                parsed['zonepair_entry_count'] = int(m.group('zonepair_entry_count'))
                continue

            #Filler block count: 2
            m = p2.match(line)
            if m:
                parsed['filler_block_count'] = int(m.group('filler_block_count'))
                continue

            #Action block count: 2
            m = p3.match(line)
            if m:
                parsed['action_block_count'] = int(m.group('action_block_count'))
                continue

            #L7 params block count: 0
            m = p4.match(line)
            if m:
                parsed['l7_params_block_count'] = int(m.group('l7_params_block_count'))
                continue

            #Statistics table count: 2
            m = p5.match(line)
            if m:
                parsed['statistics_table_count'] = int(m.group('statistics_table_count'))
                continue

            #Statistics block count: 8
            m = p6.match(line)
            if m:
                parsed['statistics_block_count'] = int(m.group('statistics_block_count'))
                continue

            #Class name table entry count: 2
            m = p7.match(line)
            if m:
                parsed['class_name_table_entry_count'] = int(m.group('class_name_table_entry_count'))
                continue

            #Number of vrf interfaces with zone: 0
            m = p8.match(line)
            if m:
                parsed['number_of_vrf_interfaces_with_zone'] = int(m.group('number_of_vrf_interfaces_with_zone'))
                continue

            #Number of zoned interfaces: 2
            m = p9.match(line)
            if m:
                parsed['number_of_zoned_interfaces'] = int(m.group('number_of_zoned_interfaces'))
                continue

            #Number of zones: 2
            m = p10.match(line)
            if m:
                parsed['number_of_zones'] = int(m.group('number_of_zones'))
                continue

            #Number of zone pairs with policy: 1
            m = p11.match(line)
            if m:
                parsed['number_of_zone_pairs_with_policy'] = int(m.group('number_of_zone_pairs_with_policy'))
                continue

            #Number of AVC policy: 0
            m = p12.match(line)
            if m:
                parsed['number_of_avc_policy'] = int(m.group('number_of_avc_policy'))
                continue

            #Inspect parameter map count: 1
            m = p13.match(line)
            if m:
                parsed['inspect_parameter_map_count'] = int(m.group('inspect_parameter_map_count'))
                continue

            #Multi-tenancy: No
            m = p14.match(line)
            if m:
                parsed['multi_tenancy'] = m.group('multi_tenancy')
                continue

            #Pending Multi-tenancy: No
            m = p15.match(line)
            if m:
                parsed['pending_multi_tenancy'] = m.group('pending_multi_tenancy')
                continue

            #VRF related objects:
            m = p16.match(line)
            if m:
                continue

            #VRF-ParameterMap count: 1,
            m = p17.match(line)
            if m:
                vrf_related_objects = parsed.setdefault('vrf_related_objects', {})
                vrf_related_objects['vrf_parameter_map_count'] = int(m.group('vrf_parameter_map_count'))
                continue

            #VRF-ParameterMap Binding count: 0,
            m = p18.match(line)
            if m:
                vrf_related_objects['vrf_parameter_map_binding_count'] = int(m.group('vrf_parameter_map_binding_count'))
                continue

            #VRF stats: 1,
            m = p19.match(line)
            if m:
                vrf_related_objects['vrf_stats'] = int(m.group('vrf_stats'))
                continue

            #VRF drop stats: 1
            m = p20.match(line)
            if m:
                vrf_related_objects['vrf_drop_stats'] = int(m.group('vrf_drop_stats'))
                continue

            #Zone related objects:
            m = p21.match(line)
            if m:
                continue

            #Zone-ParameterMap count: 0,
            m = p22.match(line)
            if m:
                zone_related_objects = parsed.setdefault('zone_related_objects', {})
                zone_related_objects['zone_parameter_map_count'] = int(m.group('zone_parameter_map_count'))
                continue

            #Zone-ParameterMap Binding count: 0
            m = p23.match(line)
            if m:
                zone_related_objects['zone_parameter_map_binding_count'] = int(m.group('zone_parameter_map_binding_count'))
                continue

            #SCB pool:
            m = p24.match(line)
            if m:
                current_section = m.group('pool_name').rstrip(':').lower().replace(' ', '_')
                parsed[current_section] = {}
                continue
            if current_section and current_section.endswith('_pool'):

                #number of entries: 16384,
                m = p25.match(line)
                if m:
                    parsed[current_section]['number_of_entries'] = int(m.group('number_of_entries'))
                    continue

                #entry limit: 0, size: 983872,
                m = p30.match(line)
                if m:
                    parsed[current_section]['entry_limit'] = int(m.group('entry_limit'))
                    parsed[current_section]['size'] = int(m.group('size'))
                    continue

                #entry limit: 1048576,
                m = p26.match(line)
                if m:
                    parsed[current_section]['entry_limit'] = int(m.group('entry_limit'))
                    continue

                #size: 11072, number of additions: 0
                m = p28.match(line)
                if m:
                    parsed[current_section]['size'] = int(m.group('size'))
                    parsed[current_section]['number_of_additions'] = int(m.group('number_of_additions'))
                    continue

                #size: 8913728,
                m = p27.match(line)
                if m:
                    parsed[current_section]['size'] = int(m.group('size'))
                    continue

                #number of additions: 0
                m = p29.match(line)
                if m:
                    parsed[current_section]['number_of_additions'] = int(m.group('number_of_additions'))
                    continue

            #Errors:
            m = p31.match(line)
            if m:
                errors = parsed.setdefault('errors', {})
                continue

            #Failed to zero global drop stats: 0,
            m = p32.match(line)
            if m:
                errors['failed_to_zero_global_drop_stats'] = int(m.group('failed_to_zero_global_drop_stats'))
                continue

            #Failed to allocate drop stats: 0,
            m = p33.match(line)
            if m:
                errors['failed_to_allocate_drop_stats'] = int(m.group('failed_to_allocate_drop_stats'))
                continue

            #Failed to zero global resource stats: 0,
            m = p34.match(line)
            if m:
                errors['failed_to_zero_global_resource_stats'] = int(m.group('failed_to_zero_global_resource_stats'))
                continue

            #Failed to allocate resource stats: 0,
            m = p35.match(line)
            if m:
                errors['failed_to_allocate_resource_stats'] = int(m.group('failed_to_allocate_resource_stats'))
                continue

            #Failed to walk vrf domains: 0,
            m = p36.match(line)
            if m:
                errors['failed_to_walk_vrf_domains'] = int(m.group('failed_to_walk_vrf_domains'))
                continue

            #Failed to re-enable firewall: 0,
            m = p37.match(line)
            if m:
                errors['failed_to_re_enable_firewall'] = int(m.group('failed_to_re_enable_firewall'))
                continue

            #Failed to disable firewall: 0,
            m = p38.match(line)
            if m:
                errors['failed_to_disable_firewall'] = int(m.group('failed_to_disable_firewall'))
                continue

            #Failed to allocate clear command buffer: 0,
            m = p39.match(line)
            if m:
                errors['failed_to_allocate_clear_command_buffer'] = int(m.group('failed_to_allocate_clear_command_buffer'))
                continue

            #Failed to send clear session IPC: 0
            m = p40.match(line)
            if m:
                errors['failed_to_send_clear_session_ipc'] = int(m.group('failed_to_send_clear_session_ipc'))
                continue

        return parsed

# ============================
# Schema for 'show platform hardware qfp active feature alg statistics msrpc'
# ============================
class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsMsrpcSchema(MetaParser):
    """Schema for show platform hardware qfp active feature alg statistics msrpc"""
    
    schema = {
        'msrpc_total_packets': int,
        'msrpc_tolerance_switch': str,
        'msrpc_non_data_packets': int,
        'msrpc_bind_packets': int,
        'msrpc_bind_ack_packets': int,
        'msrpc_alter_ctx_packets': int,
        'msrpc_alter_ctx_resp_packets': int,
        'msrpc_request_packets': int,
        'msrpc_response_packets': int,
        'msrpc_number_of_epm_sessions': int,
        'msrpc_number_of_isystem_sessions': int,
        'msrpc_number_of_tokens_created': int,
        'msrpc_bad_order_packets': int,
        'msrpc_bad_uuid_packets': int,
        'msrpc_malformed_packets': int,
        'msrpc_non_standard_packets': int,
        'msrpc_vfred_packets': int,
        'msrpc_vtcp_packets': int,
        'msrpc_internal_errors': int,
        'msrpc_chunk_requests': int,
        'msrpc_mem_creation_fail_scb': int,
        'msrpc_scb_allocated': int,
        'msrpc_scb_freed': int,
        'msrpc_extended_tokens_failed': int,
        'msrpc_extended_tokens_allocated': int,
        'msrpc_extended_tokens_freed': int,
        Optional("counters_cleared"): bool
    }


# ============================
# Parser for 'show platform hardware qfp active feature alg statistics msrpc'
# ============================
class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsMsrpc(ShowPlatformHardwareQfpActiveFeatureAlgStatisticsMsrpcSchema):
    """Parser for show platform hardware qfp active feature alg statistics msrpc
       Parser for show platform hardware qfp active feature alg statistics msrpc clear"""
    
    cli_command = [
                      'show platform hardware qfp active feature alg statistics msrpc',
                      'show platform hardware qfp active feature alg statistics msrpc {clear}'
                  ]
    
    def cli(self, clear="", output=None):
        if output is None:
            if clear:
                cmd = self.cli_command[1].format(clear=clear)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
            
        # Initialize the parsed dictionary
        parsed_dict = {}
        
        # MSRPC total packets: 8
        p1 = re.compile(r'^MSRPC\s+total\s+packets\s*:\s*(?P<msrpc_total_packets>\d+)')
        
        # MSRPC Tolerance Switch: OFF
        p2 = re.compile(r'^MSRPC\s+Tolerance\s+Switch\s*:\s*(?P<msrpc_tolerance_switch>\S+)')
        
        # MSRPC non data packets: 4
        p3 = re.compile(r'^MSRPC\s+non\s+data\s+packets\s*:\s*(?P<msrpc_non_data_packets>\d+)')
        
        # MSRPC BIND packets: 1
        p4 = re.compile(r'^MSRPC\s+BIND\s+packets\s*:\s*(?P<msrpc_bind_packets>\d+)')
        
        # MSRPC BIND_ACK packets: 1
        p5 = re.compile(r'^MSRPC\s+BIND_ACK\s+packets\s*:\s*(?P<msrpc_bind_ack_packets>\d+)')
        
        # MSRPC ALTER_CTX packets: 0
        p6 = re.compile(r'^MSRPC\s+ALTER_CTX\s+packets\s*:\s*(?P<msrpc_alter_ctx_packets>\d+)')
        
        # MSRPC ALTER_CTX_RESP packets: 0
        p7 = re.compile(r'^MSRPC\s+ALTER_CTX_RESP\s+packets\s*:\s*(?P<msrpc_alter_ctx_resp_packets>\d+)')
        
        # MSRPC REQUEST packets: 1
        p8 = re.compile(r'^MSRPC\s+REQUEST\s+packets\s*:\s*(?P<msrpc_request_packets>\d+)')
        
        # MSRPC RESPONSE packets: 1
        p9 = re.compile(r'^MSRPC\s+RESPONSE\s+packets\s*:\s*(?P<msrpc_response_packets>\d+)')
        
        # MSRPC Number of EPM sessions: 1
        p10 = re.compile(r'^MSRPC\s+Number\s+of\s+EPM\s+sessions\s*:\s*(?P<msrpc_number_of_epm_sessions>\d+)')
        
        # MSRPC Number of iSystem sessions: 0
        p11 = re.compile(r'^MSRPC\s+Number\s+of\s+iSystem\s+sessions\s*:\s*(?P<msrpc_number_of_isystem_sessions>\d+)')
        
        # MSRPC Number of tokens created: 1
        p12 = re.compile(r'^MSRPC\s+Number\s+of\s+tokens\s+created\s*:\s*(?P<msrpc_number_of_tokens_created>\d+)')
        
        # MSRPC bad order packets: 0
        p13 = re.compile(r'^MSRPC\s+bad\s+order\s+packets\s*:\s*(?P<msrpc_bad_order_packets>\d+)')
        
        # MSRPC bad uuid packets: 0
        p14 = re.compile(r'^MSRPC\s+bad\s+uuid\s+packets\s*:\s*(?P<msrpc_bad_uuid_packets>\d+)')
        
        # MSRPC malformed packets: 0
        p15 = re.compile(r'^MSRPC\s+malformed\s+packets\s*:\s*(?P<msrpc_malformed_packets>\d+)')
        
        # MSRPC non standard packets: 0
        p16 = re.compile(r'^MSRPC\s+non\s+standard\s+packets\s*:\s*(?P<msrpc_non_standard_packets>\d+)')
        
        # MSRPC VFRed packets: 0
        p17 = re.compile(r'^MSRPC\s+VFRed\s+packets\s*:\s*(?P<msrpc_vfred_packets>\d+)')
        
        # MSRPC vTCP packets: 0
        p18 = re.compile(r'^MSRPC\s+vTCP\s+packets\s*:\s*(?P<msrpc_vtcp_packets>\d+)')
        
        # MSRPC internal errors: 0
        p19 = re.compile(r'^MSRPC\s+internal\s+errors\s*:\s*(?P<msrpc_internal_errors>\d+)')
        
        # MSRPC chunk requests: 0
        p20 = re.compile(r'^MSRPC\s+chunk\s+requests\s*:\s*(?P<msrpc_chunk_requests>\d+)')
        
        # MSRPC mem creation fail (scb): 0
        p21 = re.compile(r'^MSRPC\s+mem\s+creation\s+fail\s+\(scb\)\s*:\s*(?P<msrpc_mem_creation_fail_scb>\d+)')
        
        # MSRPC scb allocated: 1
        p22 = re.compile(r'^MSRPC\s+scb\s+allocated\s*:\s*(?P<msrpc_scb_allocated>\d+)')
        
        # MSRPC scb freed: 0
        p23 = re.compile(r'^MSRPC\s+scb\s+freed\s*:\s*(?P<msrpc_scb_freed>\d+)')
        
        # MSRPC extended tokens failed: 0
        p24 = re.compile(r'^MSRPC\s+extended\s+tokens\s+failed\s*:\s*(?P<msrpc_extended_tokens_failed>\d+)')
        
        # MSRPC extended tokens allocated: 0
        p25 = re.compile(r'^MSRPC\s+extended\s+tokens\s+allocated\s*:\s*(?P<msrpc_extended_tokens_allocated>\d+)')
        
        # MSRPC extended tokens freed: 0
        p26 = re.compile(r'^MSRPC\s+extended\s+tokens\s+freed\s*:\s*(?P<msrpc_extended_tokens_freed>\d+)')
        
        # MSRPC ALG counters cleared after display.
        p27 = re.compile(r'^MSRPC ALG counters cleared after display.$')

        for line in output.splitlines():
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # MSRPC total packets: 8
            m = p1.match(line)
            if m:
                parsed_dict['msrpc_total_packets'] = int(m.groupdict()['msrpc_total_packets'])
                continue

            # MSRPC Tolerance Switch: OFF     
            m = p2.match(line)
            if m:
                parsed_dict['msrpc_tolerance_switch'] = m.groupdict()['msrpc_tolerance_switch']
                continue

            # MSRPC non data packets: 4
            m = p3.match(line)
            if m:
                parsed_dict['msrpc_non_data_packets'] = int(m.groupdict()['msrpc_non_data_packets'])
                continue

            # MSRPC BIND packets: 1
            m = p4.match(line)
            if m:
                parsed_dict['msrpc_bind_packets'] = int(m.groupdict()['msrpc_bind_packets'])
                continue

            # MSRPC BIND_ACK packets: 1
            m = p5.match(line)
            if m:
                parsed_dict['msrpc_bind_ack_packets'] = int(m.groupdict()['msrpc_bind_ack_packets'])
                continue

            # MSRPC ALTER_CTX packets: 0
            m = p6.match(line)
            if m:
                parsed_dict['msrpc_alter_ctx_packets'] = int(m.groupdict()['msrpc_alter_ctx_packets'])
                continue

            #MSRPC ALTER_CTX_RESP packets: 0
            m = p7.match(line)
            if m:
                parsed_dict['msrpc_alter_ctx_resp_packets'] = int(m.groupdict()['msrpc_alter_ctx_resp_packets'])
                continue

            # MSRPC REQUEST packets: 1   
            m = p8.match(line)
            if m:
                parsed_dict['msrpc_request_packets'] = int(m.groupdict()['msrpc_request_packets'])
                continue

            # MSRPC RESPONSE packets: 1
            m = p9.match(line)
            if m:
                parsed_dict['msrpc_response_packets'] = int(m.groupdict()['msrpc_response_packets'])
                continue

            # MSRPC Number of EPM sessions: 1
            m = p10.match(line)
            if m:
                parsed_dict['msrpc_number_of_epm_sessions'] = int(m.groupdict()['msrpc_number_of_epm_sessions'])
                continue

            # MSRPC Number of iSystem sessions: 0
            m = p11.match(line)
            if m:
                parsed_dict['msrpc_number_of_isystem_sessions'] = int(m.groupdict()['msrpc_number_of_isystem_sessions'])
                continue

            # MSRPC Number of tokens created: 1
            m = p12.match(line)
            if m:
                parsed_dict['msrpc_number_of_tokens_created'] = int(m.groupdict()['msrpc_number_of_tokens_created'])
                continue

            # MSRPC bad order packets: 0
            m = p13.match(line)
            if m:
                parsed_dict['msrpc_bad_order_packets'] = int(m.groupdict()['msrpc_bad_order_packets'])
                continue

            # MSRPC bad uuid packets: 0
            m = p14.match(line)
            if m:
                parsed_dict['msrpc_bad_uuid_packets'] = int(m.groupdict()['msrpc_bad_uuid_packets'])
                continue

            # MSRPC malformed packets: 0
            m = p15.match(line)
            if m:
                parsed_dict['msrpc_malformed_packets'] = int(m.groupdict()['msrpc_malformed_packets'])
                continue

            # MSRPC non standard packets: 0
            m = p16.match(line)
            if m:
                parsed_dict['msrpc_non_standard_packets'] = int(m.groupdict()['msrpc_non_standard_packets'])
                continue

            # MSRPC VFRed packets: 0      
            m = p17.match(line)
            if m:
                parsed_dict['msrpc_vfred_packets'] = int(m.groupdict()['msrpc_vfred_packets'])
                continue

            # MSRPC vTCP packets: 0   
            m = p18.match(line)
            if m:
                parsed_dict['msrpc_vtcp_packets'] = int(m.groupdict()['msrpc_vtcp_packets'])
                continue

            # MSRPC internal errors: 0
            m = p19.match(line)
            if m:
                parsed_dict['msrpc_internal_errors'] = int(m.groupdict()['msrpc_internal_errors'])
                continue

            # MSRPC chunk requests: 0
            m = p20.match(line)
            if m:
                parsed_dict['msrpc_chunk_requests'] = int(m.groupdict()['msrpc_chunk_requests'])
                continue

            # MSRPC mem creation fail (scb): 0
            m = p21.match(line)
            if m:
                parsed_dict['msrpc_mem_creation_fail_scb'] = int(m.groupdict()['msrpc_mem_creation_fail_scb'])
                continue

            # MSRPC scb allocated: 1
            m = p22.match(line)
            if m:
                parsed_dict['msrpc_scb_allocated'] = int(m.groupdict()['msrpc_scb_allocated'])
                continue

            # MSRPC scb freed: 0
            m = p23.match(line)
            if m:
                parsed_dict['msrpc_scb_freed'] = int(m.groupdict()['msrpc_scb_freed'])
                continue

            # MSRPC extended tokens failed: 0
            m = p24.match(line)
            if m:
                parsed_dict['msrpc_extended_tokens_failed'] = int(m.groupdict()['msrpc_extended_tokens_failed'])
                continue

            # MSRPC extended tokens allocated: 0
            m = p25.match(line)
            if m:
                parsed_dict['msrpc_extended_tokens_allocated'] = int(m.groupdict()['msrpc_extended_tokens_allocated'])
                continue

            # MSRPC extended tokens freed: 0
            m = p26.match(line)
            if m:
                parsed_dict['msrpc_extended_tokens_freed'] = int(m.groupdict()['msrpc_extended_tokens_freed'])
                continue

            # MSRPC ALG counters cleared after display.
            m = p27.match(line)
            if m:
                parsed_dict['counters_cleared'] = True
                continue

        return parsed_dict

# ================================================================================
# Parser for 'show platform hardware qfp active feature firewall drop clear'
# ================================================================================
class ShowPlatformHardwareQfpActiveFeatureFirewallDropClearSchema(MetaParser):
    """Schema for show platform hardware qfp active feature firewall drop clear"""
    schema =  { 
        Optional("drop_reasons"): str,
        Optional("packets"): int,
        "status": str 
        }
class ShowPlatformHardwareQfpActiveFeatureFirewallDropClear(ShowPlatformHardwareQfpActiveFeatureFirewallDropClearSchema):
    """Parser for:
       show platform hardware qfp active feature firewall drop clear"""

    cli_command = 'show platform hardware qfp active feature firewall drop clear'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        result = {}
    
        #Packet rcvd in SCB close state            7
        p1 = re.compile(r'^(?P<drop_reason>.+?)\s{2,}(?P<packets>\d+)$')

        #All drop counts cleared.
        p2 = re.compile(r'^(?P<status>All drop counts cleared\.)$')

        for line in output.splitlines():
            line = line.strip()
            
            #Packet rcvd in SCB close state            7
            m = p1.match(line)
            if m:
                result['drop_reasons'] = m.group('drop_reason').strip()
                result['packets'] = int(m.group('packets'))
                continue
            
            # All drop counts cleared.
            m = p2.match(line)
            if m:
                result['status'] = m.group('status')
                continue

        return result

# ==========================================================================================================
# Parser for 'show platform hardware qfp active feature firewall datapath scb any any any any any all any'
# ==========================================================================================================
#    
class ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbAnyAnyAnyAnyAnyAllAnySchema(MetaParser):
     
        schema = {
            'sessions': {
                Any(): {
                    'src_ip': str,
                    'src_port': int,
                    'dst_ip': str,
                    'dst_port': int,
                    'protocol': str,
                    'protocol_desc': str,
                    'flags': str
                }
            }
        }
     
class ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbAnyAnyAnyAnyAnyAllAny(ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbAnyAnyAnyAnyAnyAllAnySchema):
    """Parser for:
       show platform hardware qfp active feature firewall datapath scb any any any any any all any"""
    
    cli_command = 'show platform hardware qfp active feature firewall datapath scb any any any any any all any'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        result = {}

        #Session ID:0x00000004 192.168.32.1 11001 192.168.132.1 0 proto 6 (-global-:0:-global-:0) (0x1:tcp)	[sc]
        #+-Session ID:0x00000003 192.168.32.1 0 192.168.132.1 41902 proto 6 (-global-:0:-global-:0) (0x2e:ftp data)	[id]
        p1 =  re.compile(
                r'^(?:\+\-)?Session ID:0x(?P<session_id>[0-9a-fA-F]+)\s+'
                r'(?P<src_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<src_port>\d+)\s+'
                r'(?P<dst_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<dst_port>\d+)\s+'
                r'proto\s+(?P<protocol>\d+)\s+'
                r'\([^)]+\)\s+\(0x[0-9a-fA-F]+:(?P<proto_desc>[^)]+)\)\s+'
                r'\[(?P<flags>\w+)\]$'
            )

        for line in output.splitlines():
            line = line.strip()

            #Session ID:0x00000004 192.168.32.1 11001 192.168.132.1 0 proto 6 (-global-:0:-global-:0) (0x1:tcp)	[sc]
            #+-Session ID:0x00000003 192.168.32.1 0 192.168.132.1 41902 proto 6 (-global-:0:-global-:0) (0x2e:ftp data)	[id]
            m = p1.match(line)
            if m:
                session_id = m.group('session_id')
                src_ip = m.group('src_ip')  
                src_port = int(m.group('src_port'))
                dst_ip = m.group('dst_ip')
                dst_port = int(m.group('dst_port'))
                protocol = m.group('protocol')
                protocol_desc = m.group('proto_desc')
                flags = m.group('flags')
                session_id_dict =  result.setdefault('sessions', {}).setdefault(session_id, {})
                session_id_dict['src_ip'] = src_ip
                session_id_dict['src_port'] = src_port
                session_id_dict['dst_ip'] = dst_ip
                session_id_dict['dst_port'] = dst_port
                session_id_dict['protocol'] = protocol
                session_id_dict['protocol_desc'] = protocol_desc
                session_id_dict['flags'] = flags
                continue
        return result

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSipClearSchema(MetaParser):
    """Schema for show platform hardware qfp active feature alg statistics sip clear"""

    schema = {
        'sip_info_pool_used_chunk_entries_number': int,
        'receive': {
            'register': {
                'count': int,
                '200_ok': int
            },
            'invite': {
                'count': int,
                '200_ok': int,
                'rexmit_invite': int
            },
            'update': {
                'count': int,
                '200_ok': int
            },
            'bye': {
                'count': int,
                '200_ok': int
            },
            'subscribe': {
                'count': int,
                '200_ok': int
            },
            'refer': {
                'count': int,
                '200_ok': int
            },
            'prack': {
                'count': int,
                '200_ok': int
            },
            'trying': int,
            'ringing': int,
            'ack': int,
            'info': int,
            'cancel': int,
            'sess_prog': int,
            'message': int,
            'notify': int,
            'publish': int,
            'options': int,
            '1xx': int,
            '2xx': int,
            'other_req': int,
            'other_ok': int,
            '3xx_6xx': int
        },
        'events': {
            'null_dport': int,
            'media_port_zero': int,
            'malform_media': int,
            'no_content_length': int,
            'cr_trunk_chnls': int,
            'del_trunk_chnls': int,
            'start_trunk_timer': int,
            'restart_trunk_timer': int,
            'stop_trunk_timer': int,
            'trunk_timer_timeout': int,
            'cr_dbl_entry': int,
            'del_dbl_entry': int,
            'cr_dbl_cfg_entry': int,
            'del_dbl_cfg_entry': int,
            'start_dbl_trig_tmr': int,
            'restart_dbl_trig_tmr': int,
            'stop_dbl_trig_tmr': int,
            'dbl_trig_timeout': int,
            'start_dbl_blk_tmr': int,
            'restart_dbl_blk_tmr': int,
            'stop_dbl_blk_tmr': int,
            'dbl_blk_tmr_timeout': int,
            'start_dbl_idle_tmr': int,
            'restart_dbl_idle_tmr': int,
            'stop_dbl_idle_tmr': int,
            'dbl_idle_tmr_timeout': int,
            'media_addr_zero': int,
            'need_more_data': int,
            'sip_pkt_alloc': int,
            'sip_pkt_free': int,
            'sip_msg_alloc': int,
            'sip_msg_free': int
        },
        'errors': {
            'create_token_err': int,
            'add_portlist_err': int,
            'invalid_offset': int,
            'invalid_pktlen': int,
            'free_magic': int,
            'double_free': int,
            'sess_retmem_failed': int,
            'sess_malloc_failed': int,
            'pkt_retmem_failed': int,
            'pkt_malloc_failed': int,
            'msg_retmem_failed': int,
            'msg_malloc_failed': int,
            'bad_format': int,
            'invalid_proto': int,
            'add_alg_state_fail': int,
            'no_call_id': int,
            'parse_sip_hdr_fail': int,
            'parse_sdp_fail': int,
            'error_new_chnl': int,
            'huge_size': int,
            'create_failed': int,
            'not_sip_msg': int
        },
        'writeback_errors': {
            'offset_err': int,
            'pa_err': int,
            'no_info': int
        },
        'dos_errors': {
            'dbl_retmem_failed': int,
            'dbl_malloc_failed': int,
            'dblcfg_retm_failed': int,
            'dblcfg_malloc_failed': int,
            'session_wlock_ovflw': int,
            'global_wlock_ovflw': int,
            'blacklisted': int
        },
        Optional('sip_alg_counters_cleared'): str
    }


class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSipClear(ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSipClearSchema):
    """Parser for show platform hardware qfp active feature alg statistics sip clear"""

    cli_command = 'show platform hardware qfp active feature alg statistics sip clear'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # SIP info pool used chunk entries number: 1
        p1 = re.compile(r'^SIP info pool used chunk entries number:\s+(?P<number>\d+)$')

        # Register:           0 -> 200-OK:            0
        p2 = re.compile(r'^Register:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Invite:             1 -> 200-OK:            0   Rexmit-invite           1
        p3 = re.compile(r'^Invite:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)\s+Rexmit-invite\s+(?P<rexmit>\d+)$')

        # Update:             0 -> 200-OK:            0
        p4 = re.compile(r'^Update:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Bye:                0 -> 200-OK:            0
        p5 = re.compile(r'^Bye:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Subscribe:          0 -> 200-OK:            0
        p6 = re.compile(r'^Subscribe:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Refer:              0 -> 200-OK:            0
        p7 = re.compile(r'^Refer:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Prack:              0 -> 200-OK:            0
        p8 = re.compile(r'^Prack:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Trying:             0    Ringing:           0    Ack:                   0
        p9 = re.compile(r'^Trying:\s+(?P<trying>\d+)\s+Ringing:\s+(?P<ringing>\d+)\s+Ack:\s+(?P<ack>\d+)$')

        # Info:               0    Cancel:            0    Sess Prog:             0
        p10 = re.compile(r'^Info:\s+(?P<info>\d+)\s+Cancel:\s+(?P<cancel>\d+)\s+Sess Prog:\s+(?P<sess_prog>\d+)$')

        # Message:            0    Notify:            0
        p11 = re.compile(r'^Message:\s+(?P<message>\d+)\s+Notify:\s+(?P<notify>\d+)$')

        # Publish:            0    Options:           0
        p12 = re.compile(r'^Publish:\s+(?P<publish>\d+)\s+Options:\s+(?P<options>\d+)$')

        # 1xx:                0    2xx:               0
        p13 = re.compile(r'^1xx:\s+(?P<one_xx>\d+)\s+2xx:\s+(?P<two_xx>\d+)$')

        # OtherReq:           0    OtherOk:           0    3xx-6xx:               0
        p14 = re.compile(r'^OtherReq:\s+(?P<other_req>\d+)\s+OtherOk:\s+(?P<other_ok>\d+)\s+3xx-6xx:\s+(?P<three_six_xx>\d+)$')

        # Events section patterns
        # Null dport:                   0   Media Port Zero:                0
        p15 = re.compile(r'^Null dport:\s+(?P<null_dport>\d+)\s+Media Port Zero:\s+(?P<media_port_zero>\d+)$')

        # Malform Media:                0   No Content Length:              0
        p16 = re.compile(r'^Malform Media:\s+(?P<malform_media>\d+)\s+No Content Length:\s+(?P<no_content_length>\d+)$')

        # Cr Trunk Chnls:               1   Del Trunk Chnls:                0
        p17 = re.compile(r'^Cr Trunk Chnls:\s+(?P<cr_trunk_chnls>\d+)\s+Del Trunk Chnls:\s+(?P<del_trunk_chnls>\d+)$')

        # start trunk timer:            1   restart trunk timer:            0
        p18 = re.compile(r'^start trunk timer:\s+(?P<start_trunk_timer>\d+)\s+restart trunk timer:\s+(?P<restart_trunk_timer>\d+)$')

        # stop trunk timer:             0   trunk timer timeout:            0
        p19 = re.compile(r'^stop trunk timer:\s+(?P<stop_trunk_timer>\d+)\s+trunk timer timeout:\s+(?P<trunk_timer_timeout>\d+)$')

        # Cr dbl entry:                 0   Del dbl entry:                  0
        p20 = re.compile(r'^Cr dbl entry:\s+(?P<cr_dbl_entry>\d+)\s+Del dbl entry:\s+(?P<del_dbl_entry>\d+)$')

        # Cr dbl cfg entry:             0   Del dbl cfg entry:              0
        p21 = re.compile(r'^Cr dbl cfg entry:\s+(?P<cr_dbl_cfg_entry>\d+)\s+Del dbl cfg entry:\s+(?P<del_dbl_cfg_entry>\d+)$')

        # start dbl trig tmr:           0   restart dbl trig tmr:           0
        p22 = re.compile(r'^start dbl trig tmr:\s+(?P<start_dbl_trig_tmr>\d+)\s+restart dbl trig tmr:\s+(?P<restart_dbl_trig_tmr>\d+)$')

        # stop dbl trig tmr:            0   dbl trig timeout:               0
        p23 = re.compile(r'^stop dbl trig tmr:\s+(?P<stop_dbl_trig_tmr>\d+)\s+dbl trig timeout:\s+(?P<dbl_trig_timeout>\d+)$')

        # start dbl blk tmr:            0   restart dbl blk tmr:            0
        p24 = re.compile(r'^start dbl blk tmr:\s+(?P<start_dbl_blk_tmr>\d+)\s+restart dbl blk tmr:\s+(?P<restart_dbl_blk_tmr>\d+)$')

        # stop dbl blk tmr:             0   dbl blk tmr timeout:            0
        p25 = re.compile(r'^stop dbl blk tmr:\s+(?P<stop_dbl_blk_tmr>\d+)\s+dbl blk tmr timeout:\s+(?P<dbl_blk_tmr_timeout>\d+)$')

        # start dbl idle tmr:           0   restart dbl idle tmr:           0
        p26 = re.compile(r'^start dbl idle tmr:\s+(?P<start_dbl_idle_tmr>\d+)\s+restart dbl idle tmr:\s+(?P<restart_dbl_idle_tmr>\d+)$')

        # stop dbl idle tmr:            0   dbl idle tmr timeout:           0
        p27 = re.compile(r'^stop dbl idle tmr:\s+(?P<stop_dbl_idle_tmr>\d+)\s+dbl idle tmr timeout:\s+(?P<dbl_idle_tmr_timeout>\d+)$')

        # Media Addr Zero:              0   Need More Data:                 0
        p28 = re.compile(r'^Media Addr Zero:\s+(?P<media_addr_zero>\d+)\s+Need More Data:\s+(?P<need_more_data>\d+)$')

        # SIP PKT Alloc:                2   SIP PKT Free:                   2
        p29 = re.compile(r'^SIP PKT Alloc:\s+(?P<sip_pkt_alloc>\d+)\s+SIP PKT Free:\s+(?P<sip_pkt_free>\d+)$')

        # SIP MSG Alloc:                0   SIP MSG Free:                   0
        p30 = re.compile(r'^SIP MSG Alloc:\s+(?P<sip_msg_alloc>\d+)\s+SIP MSG Free:\s+(?P<sip_msg_free>\d+)$')

        # Errors section patterns
        # Create Token Err:             0    Add portlist Err:              0
        p31 = re.compile(r'^Create Token Err:\s+(?P<create_token_err>\d+)\s+Add portlist Err:\s+(?P<add_portlist_err>\d+)$')

        # Invalid Offset:               0    Invalid Pktlen:                0
        p32 = re.compile(r'^Invalid Offset:\s+(?P<invalid_offset>\d+)\s+Invalid Pktlen:\s+(?P<invalid_pktlen>\d+)$')

        # Free Magic:                   0    Double Free:                   0
        p33 = re.compile(r'^Free Magic:\s+(?P<free_magic>\d+)\s+Double Free:\s+(?P<double_free>\d+)$')

        # Sess Retmem Failed:           0    Sess Malloc Failed             0
        p34 = re.compile(r'^Sess Retmem Failed:\s+(?P<sess_retmem_failed>\d+)\s+Sess Malloc Failed\s+(?P<sess_malloc_failed>\d+)$')

        # Pkt Retmem Failed:            0    Pkt Malloc Failed:             0
        p35 = re.compile(r'^Pkt Retmem Failed:\s+(?P<pkt_retmem_failed>\d+)\s+Pkt Malloc Failed:\s+(?P<pkt_malloc_failed>\d+)$')

        # Msg Retmem Failed:            0    Msg Malloc Failed:             0
        p36 = re.compile(r'^Msg Retmem Failed:\s+(?P<msg_retmem_failed>\d+)\s+Msg Malloc Failed:\s+(?P<msg_malloc_failed>\d+)$')

        # Bad Format:                   0    Invalid Proto:                 0
        p37 = re.compile(r'^Bad Format:\s+(?P<bad_format>\d+)\s+Invalid Proto:\s+(?P<invalid_proto>\d+)$')

        # Add ALG state Fail:           0    No Call-id:                    0
        p38 = re.compile(r'^Add ALG state Fail:\s+(?P<add_alg_state_fail>\d+)\s+No Call-id:\s+(?P<no_call_id>\d+)$')

        # Parse SIP Hdr Fail:           0    Parse SDP Fail:                0
        p39 = re.compile(r'^Parse SIP Hdr Fail:\s+(?P<parse_sip_hdr_fail>\d+)\s+Parse SDP Fail:\s+(?P<parse_sdp_fail>\d+)$')

        # Error New Chnl:               0    Huge Size:                     0
        p40 = re.compile(r'^Error New Chnl:\s+(?P<error_new_chnl>\d+)\s+Huge Size:\s+(?P<huge_size>\d+)$')

        # Create Failed:                0    Not SIP Msg:                   0
        p41 = re.compile(r'^Create Failed:\s+(?P<create_failed>\d+)\s+Not SIP Msg:\s+(?P<not_sip_msg>\d+)$')

        # Writeback Errors section patterns
        # Offset Err:                   0    PA Err:                        0
        p42 = re.compile(r'^Offset Err:\s+(?P<offset_err>\d+)\s+PA Err:\s+(?P<pa_err>\d+)$')

        # No Info:                      0
        p43 = re.compile(r'^No Info:\s+(?P<no_info>\d+)$')

        # DoS Errors section patterns
        # Dbl Retmem Failed:            0    Dbl Malloc Failed:             0
        p44 = re.compile(r'^Dbl Retmem Failed:\s+(?P<dbl_retmem_failed>\d+)\s+Dbl Malloc Failed:\s+(?P<dbl_malloc_failed>\d+)$')

        # DblCfg Retm Failed:           0    DblCfg Malloc Failed:          0
        p45 = re.compile(r'^DblCfg Retm Failed:\s+(?P<dblcfg_retm_failed>\d+)\s+DblCfg Malloc Failed:\s+(?P<dblcfg_malloc_failed>\d+)$')

        # Session wlock ovflw:          0    Global wlock ovflw:            0
        p46 = re.compile(r'^Session wlock ovflw:\s+(?P<session_wlock_ovflw>\d+)\s+Global wlock ovflw:\s+(?P<global_wlock_ovflw>\d+)$')

        # Blacklisted:                  0
        p47 = re.compile(r'^Blacklisted:\s+(?P<blacklisted>\d+)$')

        # SIP ALG counters cleared after display.
        p48 = re.compile(r'^SIP ALG counters cleared after display\.$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # SIP info pool used chunk entries number: 1
            m = p1.match(line)
            if m:
                parsed_dict['sip_info_pool_used_chunk_entries_number'] = int(m.group('number'))
                continue

            # Register:           0 -> 200-OK:            0
            m = p2.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                register_dict = receive_dict.setdefault('register', {})
                register_dict['count'] = int(m.group('count'))
                register_dict['200_ok'] = int(m.group('ok'))
                continue

            # Invite:             1 -> 200-OK:            0   Rexmit-invite           1
            m = p3.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                invite_dict = receive_dict.setdefault('invite', {})
                invite_dict['count'] = int(m.group('count'))
                invite_dict['200_ok'] = int(m.group('ok'))
                invite_dict['rexmit_invite'] = int(m.group('rexmit'))
                continue

            # Update:             0 -> 200-OK:            0
            m = p4.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                update_dict = receive_dict.setdefault('update', {})
                update_dict['count'] = int(m.group('count'))
                update_dict['200_ok'] = int(m.group('ok'))
                continue

            # Bye:                0 -> 200-OK:            0
            m = p5.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                bye_dict = receive_dict.setdefault('bye', {})
                bye_dict['count'] = int(m.group('count'))
                bye_dict['200_ok'] = int(m.group('ok'))
                continue

            # Subscribe:          0 -> 200-OK:            0
            m = p6.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                subscribe_dict = receive_dict.setdefault('subscribe', {})
                subscribe_dict['count'] = int(m.group('count'))
                subscribe_dict['200_ok'] = int(m.group('ok'))
                continue

            # Refer:              0 -> 200-OK:            0
            m = p7.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                refer_dict = receive_dict.setdefault('refer', {})
                refer_dict['count'] = int(m.group('count'))
                refer_dict['200_ok'] = int(m.group('ok'))
                continue

            # Prack:              0 -> 200-OK:            0
            m = p8.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                prack_dict = receive_dict.setdefault('prack', {})
                prack_dict['count'] = int(m.group('count'))
                prack_dict['200_ok'] = int(m.group('ok'))
                continue

            # Trying:             0    Ringing:           0    Ack:                   0
            m = p9.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['trying'] = int(m.group('trying'))
                receive_dict['ringing'] = int(m.group('ringing'))
                receive_dict['ack'] = int(m.group('ack'))
                continue

            # Info:               0    Cancel:            0    Sess Prog:             0
            m = p10.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['info'] = int(m.group('info'))
                receive_dict['cancel'] = int(m.group('cancel'))
                receive_dict['sess_prog'] = int(m.group('sess_prog'))
                continue

            # Message:            0    Notify:            0
            m = p11.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['message'] = int(m.group('message'))
                receive_dict['notify'] = int(m.group('notify'))
                continue

            # Publish:            0    Options:           0
            m = p12.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['publish'] = int(m.group('publish'))
                receive_dict['options'] = int(m.group('options'))
                continue

            # 1xx:                0    2xx:               0
            m = p13.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['1xx'] = int(m.group('one_xx'))
                receive_dict['2xx'] = int(m.group('two_xx'))
                continue

            # OtherReq:           0    OtherOk:           0    3xx-6xx:               0
            m = p14.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['other_req'] = int(m.group('other_req'))
                receive_dict['other_ok'] = int(m.group('other_ok'))
                receive_dict['3xx_6xx'] = int(m.group('three_six_xx'))
                continue

            # Events section
            # Null dport:                   0   Media Port Zero:                0
            m = p15.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['null_dport'] = int(m.group('null_dport'))
                events_dict['media_port_zero'] = int(m.group('media_port_zero'))
                continue

            # Malform Media:                0   No Content Length:              0
            m = p16.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['malform_media'] = int(m.group('malform_media'))
                events_dict['no_content_length'] = int(m.group('no_content_length'))
                continue

            # Cr Trunk Chnls:               1   Del Trunk Chnls:                0
            m = p17.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['cr_trunk_chnls'] = int(m.group('cr_trunk_chnls'))
                events_dict['del_trunk_chnls'] = int(m.group('del_trunk_chnls'))
                continue

            # start trunk timer:            1   restart trunk timer:            0
            m = p18.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['start_trunk_timer'] = int(m.group('start_trunk_timer'))
                events_dict['restart_trunk_timer'] = int(m.group('restart_trunk_timer'))
                continue

            # stop trunk timer:             0   trunk timer timeout:            0
            m = p19.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['stop_trunk_timer'] = int(m.group('stop_trunk_timer'))
                events_dict['trunk_timer_timeout'] = int(m.group('trunk_timer_timeout'))
                continue

            # Cr dbl entry:                 0   Del dbl entry:                  0
            m = p20.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['cr_dbl_entry'] = int(m.group('cr_dbl_entry'))
                events_dict['del_dbl_entry'] = int(m.group('del_dbl_entry'))
                continue

            # Cr dbl cfg entry:             0   Del dbl cfg entry:              0
            m = p21.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['cr_dbl_cfg_entry'] = int(m.group('cr_dbl_cfg_entry'))
                events_dict['del_dbl_cfg_entry'] = int(m.group('del_dbl_cfg_entry'))
                continue

            # start dbl trig tmr:           0   restart dbl trig tmr:           0
            m = p22.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['start_dbl_trig_tmr'] = int(m.group('start_dbl_trig_tmr'))
                events_dict['restart_dbl_trig_tmr'] = int(m.group('restart_dbl_trig_tmr'))
                continue

            # stop dbl trig tmr:            0   dbl trig timeout:               0
            m = p23.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['stop_dbl_trig_tmr'] = int(m.group('stop_dbl_trig_tmr'))
                events_dict['dbl_trig_timeout'] = int(m.group('dbl_trig_timeout'))
                continue

            # start dbl blk tmr:            0   restart dbl blk tmr:            0
            m = p24.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['start_dbl_blk_tmr'] = int(m.group('start_dbl_blk_tmr'))
                events_dict['restart_dbl_blk_tmr'] = int(m.group('restart_dbl_blk_tmr'))
                continue

            # stop dbl blk tmr:             0   dbl blk tmr timeout:            0
            m = p25.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['stop_dbl_blk_tmr'] = int(m.group('stop_dbl_blk_tmr'))
                events_dict['dbl_blk_tmr_timeout'] = int(m.group('dbl_blk_tmr_timeout'))
                continue

            # start dbl idle tmr:           0   restart dbl idle tmr:           0
            m = p26.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['start_dbl_idle_tmr'] = int(m.group('start_dbl_idle_tmr'))
                events_dict['restart_dbl_idle_tmr'] = int(m.group('restart_dbl_idle_tmr'))
                continue

            # stop dbl idle tmr:            0   dbl idle tmr timeout:           0
            m = p27.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['stop_dbl_idle_tmr'] = int(m.group('stop_dbl_idle_tmr'))
                events_dict['dbl_idle_tmr_timeout'] = int(m.group('dbl_idle_tmr_timeout'))
                continue

            # Media Addr Zero:              0   Need More Data:                 0
            m = p28.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['media_addr_zero'] = int(m.group('media_addr_zero'))
                events_dict['need_more_data'] = int(m.group('need_more_data'))
                continue

            # SIP PKT Alloc:                2   SIP PKT Free:                   2
            m = p29.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['sip_pkt_alloc'] = int(m.group('sip_pkt_alloc'))
                events_dict['sip_pkt_free'] = int(m.group('sip_pkt_free'))
                continue

            # SIP MSG Alloc:                0   SIP MSG Free:                   0
            m = p30.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['sip_msg_alloc'] = int(m.group('sip_msg_alloc'))
                events_dict['sip_msg_free'] = int(m.group('sip_msg_free'))
                continue

            # Errors section
            # Create Token Err:             0    Add portlist Err:              0
            m = p31.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['create_token_err'] = int(m.group('create_token_err'))
                errors_dict['add_portlist_err'] = int(m.group('add_portlist_err'))
                continue

            # Invalid Offset:               0    Invalid Pktlen:                0
            m = p32.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['invalid_offset'] = int(m.group('invalid_offset'))
                errors_dict['invalid_pktlen'] = int(m.group('invalid_pktlen'))
                continue

            # Free Magic:                   0    Double Free:                   0
            m = p33.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['free_magic'] = int(m.group('free_magic'))
                errors_dict['double_free'] = int(m.group('double_free'))
                continue

            # Sess Retmem Failed:           0    Sess Malloc Failed             0
            m = p34.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['sess_retmem_failed'] = int(m.group('sess_retmem_failed'))
                errors_dict['sess_malloc_failed'] = int(m.group('sess_malloc_failed'))
                continue

            # Pkt Retmem Failed:            0    Pkt Malloc Failed:             0
            m = p35.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['pkt_retmem_failed'] = int(m.group('pkt_retmem_failed'))
                errors_dict['pkt_malloc_failed'] = int(m.group('pkt_malloc_failed'))
                continue

            # Msg Retmem Failed:            0    Msg Malloc Failed:             0
            m = p36.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['msg_retmem_failed'] = int(m.group('msg_retmem_failed'))
                errors_dict['msg_malloc_failed'] = int(m.group('msg_malloc_failed'))
                continue

            # Bad Format:                   0    Invalid Proto:                 0
            m = p37.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['bad_format'] = int(m.group('bad_format'))
                errors_dict['invalid_proto'] = int(m.group('invalid_proto'))
                continue

            # Add ALG state Fail:           0    No Call-id:                    0
            m = p38.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['add_alg_state_fail'] = int(m.group('add_alg_state_fail'))
                errors_dict['no_call_id'] = int(m.group('no_call_id'))
                continue

            # Parse SIP Hdr Fail:           0    Parse SDP Fail:                0
            m = p39.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['parse_sip_hdr_fail'] = int(m.group('parse_sip_hdr_fail'))
                errors_dict['parse_sdp_fail'] = int(m.group('parse_sdp_fail'))
                continue

            # Error New Chnl:               0    Huge Size:                     0
            m = p40.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['error_new_chnl'] = int(m.group('error_new_chnl'))
                errors_dict['huge_size'] = int(m.group('huge_size'))
                continue

            # Create Failed:                0    Not SIP Msg:                   0
            m = p41.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['create_failed'] = int(m.group('create_failed'))
                errors_dict['not_sip_msg'] = int(m.group('not_sip_msg'))
                continue

            # Writeback Errors section
            # Offset Err:                   0    PA Err:                        0
            m = p42.match(line)
            if m:
                writeback_errors_dict = parsed_dict.setdefault('writeback_errors', {})
                writeback_errors_dict['offset_err'] = int(m.group('offset_err'))
                writeback_errors_dict['pa_err'] = int(m.group('pa_err'))
                continue

            # No Info:                      0
            m = p43.match(line)
            if m:
                writeback_errors_dict = parsed_dict.setdefault('writeback_errors', {})
                writeback_errors_dict['no_info'] = int(m.group('no_info'))
                continue

            # DoS Errors section
            # Dbl Retmem Failed:            0    Dbl Malloc Failed:             0
            m = p44.match(line)
            if m:
                dos_errors_dict = parsed_dict.setdefault('dos_errors', {})
                dos_errors_dict['dbl_retmem_failed'] = int(m.group('dbl_retmem_failed'))
                dos_errors_dict['dbl_malloc_failed'] = int(m.group('dbl_malloc_failed'))
                continue

            # DblCfg Retm Failed:           0    DblCfg Malloc Failed:          0
            m = p45.match(line)
            if m:
                dos_errors_dict = parsed_dict.setdefault('dos_errors', {})
                dos_errors_dict['dblcfg_retm_failed'] = int(m.group('dblcfg_retm_failed'))
                dos_errors_dict['dblcfg_malloc_failed'] = int(m.group('dblcfg_malloc_failed'))
                continue

            # Session wlock ovflw:          0    Global wlock ovflw:            0
            m = p46.match(line)
            if m:
                dos_errors_dict = parsed_dict.setdefault('dos_errors', {})
                dos_errors_dict['session_wlock_ovflw'] = int(m.group('session_wlock_ovflw'))
                dos_errors_dict['global_wlock_ovflw'] = int(m.group('global_wlock_ovflw'))
                continue

            # Blacklisted:                  0
            m = p47.match(line)
            if m:
                dos_errors_dict = parsed_dict.setdefault('dos_errors', {})
                dos_errors_dict['blacklisted'] = int(m.group('blacklisted'))
                continue

            # SIP ALG counters cleared after display.
            m = p48.match(line)
            if m:
                parsed_dict['sip_alg_counters_cleared'] = 'SIP ALG counters cleared after display.'
                continue

        return parsed_dict

class ShowPlatformHardwareQfpActiveFeatureTdDatapathStatisticsSchema(MetaParser):
    """Schema for show platform hardware qfp active feature td datapath statistics"""
    schema = {
        'pool_usage': {
            'vtcp_info_alloc': {
                'alloc': int,
                'free': int,
                'fail': int
            },
            'pkt_buf_alloc': {
                'alloc': int,
                'free': int,
                'fail': int
            },
            'buf_size_alloc': {
                'alloc': int,
                'free': int
            }
        },
        'receive': {
            'alg_proc_csum': int,
            'off_csum': int,
            'lisp_seg': int,
            'out_of_order': int,
            'retrans': int,
            'overlap': int,
            'dup_ack': int
        },
        'send': {
            'rx_ack': int,
            'rst': int,
            'hold_rst': int,
            'tx_hold_rexmit': int,
            'tx_rexmit': int,
            'tx_seg': int
        },
        'events_errors': {
            'tcp_fixup_drop': int,
            'invalid_sync': int,
            'invalid_opt': int,
            'tcp_invalid_rx': int,
            'invalid_tx': int,
            'pkt_err': int,
            'mem_err': int,
            'pa_err': int,
            'hex_limit': int,
            Optional('tcp_flag_noack'): int,
            Optional('punt_err'): int,
            Optional('l2_not_supported'): int,
            Optional('first_pkt_non_syn'): int
        }
    }
class ShowPlatformHardwareQfpActiveFeatureTdDatapathStatistics(
    ShowPlatformHardwareQfpActiveFeatureTdDatapathStatisticsSchema
):
    """Parser for show platform hardware qfp active feature td datapath statistics"""

    cli_command = 'show platform hardware qfp active feature td datapath statistics'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # vtcp info alloc: 2 free: 0 fail: 0
        p1 = re.compile(r'^vtcp info alloc:\s+(?P<alloc>\d+)\s+free:\s+(?P<free>\d+)\s+fail:\s+(?P<fail>\d+)$')

        # pkt buf alloc: 0 free: 0 fail: 0
        p2 = re.compile(r'^pkt buf alloc:\s+(?P<alloc>\d+)\s+free:\s+(?P<free>\d+)\s+fail:\s+(?P<fail>\d+)$')

        # buf size alloc: 0 free: 0
        p3 = re.compile(r'^buf size alloc:\s+(?P<alloc>\d+)\s+free:\s+(?P<free>\d+)$')

        # alg_proc_csum: 0 off_csum: 0 lisp_seg: 0
        p4 = re.compile(r'^alg_proc_csum:\s+(?P<alg_proc_csum>\d+)\s+off_csum:\s+(?P<off_csum>\d+)\s+lisp_seg:\s+(?P<lisp_seg>\d+)$')

        # out of order: 0 retrans: 0 overlap: 0
        p5 = re.compile(r'^out of order:\s+(?P<out_of_order>\d+)\s+retrans:\s+(?P<retrans>\d+)\s+overlap:\s+(?P<overlap>\d+)$')

        # dup ack: 3
        p6 = re.compile(r'^dup ack:\s+(?P<dup_ack>\d+)$')

        # rx ack: 0 rst: 0 hold_rst: 0
        p7 = re.compile(r'^rx ack:\s+(?P<rx_ack>\d+)\s+rst:\s+(?P<rst>\d+)\s+hold_rst:\s+(?P<hold_rst>\d+)$')

        # tx_hold_rexmit: 0 tx_rexmit: 0 tx_seg: 0
        p8 = re.compile(r'^tx_hold_rexmit:\s+(?P<tx_hold_rexmit>\d+)\s+tx_rexmit:\s+(?P<tx_rexmit>\d+)\s+tx_seg:\s+(?P<tx_seg>\d+)$')

        # tcp_fixup_drop: 0 invalid_sync: 0 invalid_opt: 0
        p9 = re.compile(r'^tcp_fixup_drop:\s+(?P<tcp_fixup_drop>\d+)\s+invalid_sync:\s+(?P<invalid_sync>\d+)\s+invalid_opt:\s+(?P<invalid_opt>\d+)$')

        # tcp_invalid_rx: 0 invalid_tx: 0 pkt_err: 0
        p10 = re.compile(r'^tcp_invalid_rx:\s+(?P<tcp_invalid_rx>\d+)\s+invalid_tx:\s+(?P<invalid_tx>\d+)\s+pkt_err:\s+(?P<pkt_err>\d+)$')

        # mem_err: 0 pa_err: 0 hex_limit: 0
        p11 = re.compile(r'^mem_err:\s+(?P<mem_err>\d+)\s+pa_err:\s+(?P<pa_err>\d+)\s+hex_limit:\s+(?P<hex_limit>\d+)$')

        # tcp_flag_noack: 0 punt_err: 0 L2_not_supported 0
        # tcp_flag_noack: 0  punt_err: 0 (variant with extra spaces and no L2_not_supported)
        p12 = re.compile(r'^tcp_flag_noack:\s+(?P<tcp_flag_noack>\d+)\s+punt_err:\s+(?P<punt_err>\d+)(?:\s+L2_not_supported\s+(?P<l2_not_supported>\d+))?$')

        # first_pkt_non_syn: 0
        p13 = re.compile(r'^first_pkt_non_syn:\s+(?P<first_pkt_non_syn>\d+)$')

        # l2_not_supported: 0  (separate line if present)
        p14 = re.compile(r'^l2_not_supported:\s+(?P<l2_not_supported>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # vtcp info alloc: 2 free: 0 fail: 0
            m = p1.match(line)
            if m:
                parsed_dict.setdefault('pool_usage', {})['vtcp_info_alloc'] = {k: int(v) for k, v in m.groupdict().items()}
                continue

            # pkt buf alloc: 0 free: 0 fail: 0
            m = p2.match(line)
            if m:
                parsed_dict['pool_usage']['pkt_buf_alloc'] = {k: int(v) for k, v in m.groupdict().items()}
                continue

            # buf size alloc: 0 free: 0
            m = p3.match(line)
            if m:
                parsed_dict['pool_usage']['buf_size_alloc'] = {k: int(v) for k, v in m.groupdict().items()}
                continue

            # alg_proc_csum: 0 off_csum: 0 lisp_seg: 0
            m = p4.match(line)
            if m:
                parsed_dict.setdefault('receive', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # out of order: 0 retrans: 0 overlap: 0
            m = p5.match(line)
            if m:
                parsed_dict['receive'].update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # dup ack: 3
            m = p6.match(line)
            if m:
                parsed_dict['receive']['dup_ack'] = int(m.group('dup_ack'))
                continue

            # rx ack: 0 rst: 0 hold_rst: 0
            m = p7.match(line)
            if m:
                parsed_dict.setdefault('send', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # tx_hold_rexmit: 0 tx_rexmit: 0 tx_seg: 0
            m = p8.match(line)
            if m:
                parsed_dict['send'].update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # tcp_fixup_drop: 0 invalid_sync: 0 invalid_opt: 0
            m = p9.match(line)
            if m:
                parsed_dict.setdefault('events_errors', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # tcp_invalid_rx: 0 invalid_tx: 0 pkt_err: 0
            m = p10.match(line)
            if m:
                parsed_dict['events_errors'].update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # mem_err: 0 pa_err: 0 hex_limit: 0
            m = p11.match(line)
            if m:
                parsed_dict['events_errors'].update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # tcp_flag_noack: 0 punt_err: 0 L2_not_supported 0
            # tcp_flag_noack: 0  punt_err: 0 (variant with extra spaces and no L2_not_supported)
            m = p12.match(line)
            if m:
                parsed_dict['events_errors'].update({
                    'tcp_flag_noack': int(m.group('tcp_flag_noack')),
                    'punt_err': int(m.group('punt_err'))
                })
                # Only add l2_not_supported if it's present in the match
                if m.group('l2_not_supported') is not None:
                    parsed_dict['events_errors']['l2_not_supported'] = int(m.group('l2_not_supported'))
                continue

            # first_pkt_non_syn: 0
            m = p13.match(line)
            if m:
                parsed_dict['events_errors']['first_pkt_non_syn'] = int(m.group('first_pkt_non_syn'))
                continue

            # l2_not_supported: 0  (separate line if present)
            m = p14.match(line)
            if m:
                parsed_dict['events_errors']['l2_not_supported'] = int(m.group('l2_not_supported'))
                continue

        return parsed_dict

# =======================================================
# Schema for 'show platform hardware qfp active feature firewall datapath scb any any any any any all any detail'
# =======================================================

class ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbDetailSchema(MetaParser):
    '''Schema for show platform hardware qfp active feature firewall datapath scb any any any any any all any detail'''
    schema = {
        'sessions': {
            Any(): {
                'session_id': str,
                'src_ip': str,
                'src_port': int,
                'dst_ip': str,
                'dst_port': int,
                'protocol': int,
                'vrf_src': str,
                'vrf_dst': str,
                'protocol_name': str,
                'flags': str,
                'pscb': str,
                'key1_flags': str,
                'bucket': int,
                'prev': str,
                'next': str,
                'fw_flags': ListOf(str),
                Optional('vrf_flags'): ListOf(str),
                'protocol_state': ListOf(str),
                'icmp_error_count': int,
                'ureachable_arrived': str,
                'scb_state': str,
                'nxt_timeout': int,
                'refcnt': int,
                'nbar_verdict_count': int,
                'ha_nak_cnt': int,
                'rg': int,
                'hostdb': str,
                'l7': str,
                'stats': str,
                'child': str,
                'octets_in': int,
                'packets_in': int,
                'octets_out': int,
                'packets_out': int,
                'cl6_word': str,
                'l7_proto': str,
                'l7_ooo_drop': str,
                'root_scb': str,
                'act_blk': str,
                'ingress_intf': str,
                'ingress_intf_id': int,
                'egress_intf': str,
                'egress_intf_id': int,
                Optional('current_time'): int,
                Optional('create_tstamp'): int,
                Optional('last_access'): int,
                Optional('now'): int,
                Optional('csec_left'): str,
                'nat_out_local_addr': str,
                'nat_out_local_port': int,
                'nat_in_global_addr': str,
                'nat_in_global_port': int,
                'ip6_addr1': str,
                'ip6_addr2': str,
                'key_ip4_addr1': str,
                'key_ip4_port1': int,
                'key_ip4_addr2': str,
                'key_ip4_port2': int,
                'syncookie_fixup': str,
                'halfopen_linkage': ListOf(str),
                'cxsc_cft_fid': str,
                'tw_timer': ListOf(str),
                'domain_ab1': str,
                'l4_per_filter_stats': str,
                'avc_class_id': str,
                'sgt': int,
                'dgt': int,
                'nat_handles': ListOf(str),
                'flowdb_in2out': str,
                'flowdb_in2out_alloc_epoch': int,
                'flowdb_out2in': str,
                'flowdb_out2in_alloc_epoch': int,
                'ppe_tid': int,
                'icmp_err_time': int,
                'utd_context_id': int,
                'classification_epoch_scb': str,
                'classification_epoch_actblk': str,
                'avc_class_stats': str,
                'vpn_id_src': int,
                'vpn_id_dst': int,
                'zone_pair': str,
                'zone_class': str,
                Optional('timer_info'): {
                    'bucket': int,
                    'flags': str,
                    'func': int,
                    'idx': int,
                    'wheel': str,
                    'timer_status': str,
                    'num_buckets': int,
                    'cur': int,
                    'mask': str,
                    'gran': int,
                    'flag': str,
                    'ticks': int,
                }
            }
        }
    }


class ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbDetail(ShowPlatformHardwareQfpActiveFeatureFirewallDatapathScbDetailSchema):
    '''Parser for show platform hardware qfp active feature firewall datapath scb any any any any any all any detail'''

    cli_command = 'show platform hardware qfp active feature firewall datapath scb any any any any any all any detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed = {}

        # Regex patterns
        # Session ID:0x00000001 10.1.1.2 10001 20.1.1.2 20001 proto 17 (-global-:0:-global-:0) (0x2:udp)	[sc]
        # Session ID:0x0000001D 2001:1::1 128 2001:2::2 1428 proto 58 (0:0) (0x3:icmp)	[sd] 1879183652
        p1 = re.compile(r'^Session ID:(?P<session_id>0x[0-9a-fA-F]+)\s+(?P<src_ip>\S+)\s+(?P<src_port>\d+)\s+(?P<dst_ip>\S+)\s+(?P<dst_port>\d+)\s+proto\s+(?P<protocol>\d+)\s+\((?P<vrf_info>[^)]+)\)\s+\((?P<protocol_hex>0x[0-9a-fA-F]+):(?P<protocol_name>[^)]+)\)\s+\[(?P<flags>[^\]]+)\](?:\s+(?P<extra>\d+))?$')

        # pscb : 0x9d00320,  key1_flags: 0x00000000
        p2 = re.compile(r'^\s*pscb\s*:\s*(?P<pscb>0x[0-9a-fA-F]+),\s*key1_flags:\s*(?P<key1_flags>0x[0-9a-fA-F]+)$')

        # bucket : 35444, prev 0x0, next 0x0    fw_flags: 0x00000004 0x2041b841,
        p3 = re.compile(r'^\s*bucket\s*:\s*(?P<bucket>\d+),\s*prev\s+(?P<prev>0x[0-9a-fA-F]+),\s*next\s+(?P<next>0x[0-9a-fA-F]+)\s*fw_flags:\s*(?P<fw_flags>.+),$')

        # bucket : 42876, prev 0x0, next 0x0 (alternative format without fw_flags)
        p3a = re.compile(r'^\s*bucket\s*:\s*(?P<bucket>\d+),\s*prev\s+(?P<prev>0x[0-9a-fA-F]+),\s*next\s+(?P<next>0x[0-9a-fA-F]+)$')

        # fw_flags: 0x00000004 0x2041b861, (standalone fw_flags line)
        p3b = re.compile(r'^\s*fw_flags:\s*(?P<fw_flags>.+),$')

        # VRF1-rsrc-limit
        p4 = re.compile(r'^\s*(?P<vrf_flags>VRF\d+-[^,\s]+(?:\s+[^,\s]+)*)$')

        # Root Protocol-UDP Alert Proto-State:Resp-Init No-halfopen-list Active-cnt Session-db Max-session
        p5 = re.compile(r'^\s*(?P<protocol_state>Root\s+Protocol-\S+.*?)$')

        # icmp_error count 0 ureachable arrived: no
        p6 = re.compile(r'^\s*icmp_error count\s+(?P<icmp_error_count>\d+)\s+ureachable arrived:\s+(?P<ureachable_arrived>\S+)$')

        # scb state: active, nxt_timeout: 6000, refcnt: 1 NBAR verdict count 0
        p7 = re.compile(r'^\s*scb state:\s+(?P<scb_state>\S+),\s*nxt_timeout:\s+(?P<nxt_timeout>\d+),\s*refcnt:\s+(?P<refcnt>\d+)\s+NBAR verdict count\s+(?P<nbar_verdict_count>\d+)$')

        # scb state: active, nxt_timeout: 6000, refcnt: 1 (alternative format without NBAR verdict count)
        p7a = re.compile(r'^\s*scb state:\s+(?P<scb_state>\S+),\s*nxt_timeout:\s+(?P<nxt_timeout>\d+),\s*refcnt:\s+(?P<refcnt>\d+)$')

        # ha nak cnt: 0, rg: 0
        p8 = re.compile(r'^\s*ha nak cnt:\s+(?P<ha_nak_cnt>\d+),\s*rg:\s+(?P<rg>\d+)$')

        # hostdb: 0x0, L7: 0x0, stats: 0xb2c7480, child: 0x0
        p9 = re.compile(r'^\s*hostdb:\s+(?P<hostdb>0x[0-9a-fA-F]+),\s*L7:\s+(?P<l7>0x[0-9a-fA-F]+),\s*stats:\s+(?P<stats>0x[0-9a-fA-F]+),\s*child:\s+(?P<child>0x[0-9a-fA-F]+)$')

        # octets:     1000    packets:         10    octets:     0   packets:     0
        p10 = re.compile(r'^\s*octets:\s+(?P<octets_in>\d+)\s+packets:\s+(?P<packets_in>\d+)\s+octets:\s+(?P<octets_out>\d+)\s+packets:\s+(?P<packets_out>\d+)$')

        # cl6 word 1:    0x00000000 proto: 0002: l7 ooo drop 0x010 l7_prot 0x2 - udp
        p11 = re.compile(r'^\s*cl6 word 1:\s+(?P<cl6_word>0x[0-9a-fA-F]+)\s+proto:\s+(?P<proto>\d+):\s+l7 ooo drop\s+(?P<l7_ooo_drop>0x[0-9a-fA-F]+)\s+l7_prot\s+(?P<l7_prot>0x[0-9a-fA-F]+)\s+-\s+(?P<l7_proto>\S+)$')

        # icmp seq:     17721047137 proto: 0003: l7 ooo drop 0x010 l7_prot 0x3 - icmp
        p11a = re.compile(r'^\s*icmp seq:\s+\d+\s+proto:\s+(?P<proto>\d+):\s+l7 ooo drop\s+(?P<l7_ooo_drop>0x[0-9a-fA-F]+)\s+l7_prot\s+(?P<l7_prot>0x[0-9a-fA-F]+)\s+-\s+(?P<l7_proto>\S+)$')

        # icmp seq:     17721047137 proto: 0003: l7 ooo drop 0x010 (without l7_prot)
        p11b = re.compile(r'^\s*icmp seq:\s+\d+\s+proto:\s+(?P<proto>\d+):\s+l7 ooo drop\s+(?P<l7_ooo_drop>0x[0-9a-fA-F]+)$')

        # root scb: 0x0 act_blk: 0xb2bf400
        p12 = re.compile(r'^\s*root scb:\s+(?P<root_scb>0x[0-9a-fA-F]+)\s+act_blk:\s+(?P<act_blk>0x[0-9a-fA-F]+)$')

        # ingress/egress intf: GigabitEthernet0/0/2 (1021), GigabitEthernet0/0/4 (65525)
        p13 = re.compile(r'^\s*ingress/egress intf:\s+(?P<ingress_intf>\S+)\s+\((?P<ingress_intf_id>\d+)\),\s+(?P<egress_intf>\S+)\s+\((?P<egress_intf_id>\d+)\)$')

        # current time 414144656200 create tstamp: 401211845026 last access: 403012409726 now 414144657011 csec left
        p14 = re.compile(r'^\s*current time\s+(?P<current_time>\d+)\s+create tstamp:\s+(?P<create_tstamp>\d+)\s+last access:\s+(?P<last_access>\d+)\s+now\s+(?P<now>\d+)\s+(?P<csec_left>.+)$')

        # nat_out_local_addr:port: 0.0.0.0:0
        p15 = re.compile(r'^\s*nat_out_local_addr:port:\s+(?P<nat_out_local_addr>[^:]+):(?P<nat_out_local_port>\d+)$')

        # nat_in_global_addr:port: 0.0.0.0:0
        p16 = re.compile(r'^\s*nat_in_global_addr:port:\s+(?P<nat_in_global_addr>[^:]+):(?P<nat_in_global_port>\d+)$')

        # ip6: addr1 :: addr2 ::
        p17 = re.compile(r'^\s*ip6:\s+addr1\s+(?P<ip6_addr1>\S+)\s+addr2\s+(?P<ip6_addr2>\S+)$')

        # key ip4: addr1 10.1.1.2:10001 addr2 20.1.1.2:20001
        p18 = re.compile(r'^\s*key ip4:\s+addr1\s+(?P<key_ip4_addr1>[^:]+):(?P<key_ip4_port1>\d+)\s+addr2\s+(?P<key_ip4_addr2>[^:]+):(?P<key_ip4_port2>\d+)$')

        # syncookie fixup: 0x0,  halfopen linkage: 0x0 0x0
        p19 = re.compile(r'^\s*syncookie fixup:\s+(?P<syncookie_fixup>0x[0-9a-fA-F]+),\s*halfopen linkage:\s+(?P<halfopen_linkage>.+)$')

        # cxsc_cft_fid: 0x00000000
        p20 = re.compile(r'^\s*cxsc_cft_fid:\s+(?P<cxsc_cft_fid>0x[0-9a-fA-F]+)$')

        # tw timer: 0x00000000 0x00000000 0x00000000 0x01adc101
        p21 = re.compile(r'^\s*tw timer:\s+(?P<tw_timer>.+)$')

        # domain_ab1 0x8468d470 l4 per filter stats 0x0 avc class id 0x0  SGT: 0 DGT: 0
        p22 = re.compile(r'^\s*domain_ab1\s+(?P<domain_ab1>0x[0-9a-fA-F]+)\s+l4 per filter stats\s+(?P<l4_per_filter_stats>0x[0-9a-fA-F]+)\s+avc class id\s+(?P<avc_class_id>0x[0-9a-fA-F]+)\s+SGT:\s+(?P<sgt>\d+)\s+DGT:\s+(?P<dgt>\d+)$')

        # domain_ab1 0x7045ab10 l4 per filter stats 0x0 avc class id 0 SGT: 0 DGT: 0 (alternative format with integer avc class id)
        p22a = re.compile(r'^\s*domain_ab1\s+(?P<domain_ab1>0x[0-9a-fA-F]+)\s+l4 per filter stats\s+(?P<l4_per_filter_stats>0x[0-9a-fA-F]+)\s+avc class id\s+(?P<avc_class_id>\d+)\s+SGT:\s+(?P<sgt>\d+)\s+DGT:\s+(?P<dgt>\d+)$')

        # NAT handles 0x00000000 0x00000000
        p23 = re.compile(r'^\s*NAT handles\s+(?P<nat_handles>.+)$')

        # FlowDB in2out 0x00000000 alloc_epoch 0 out2in 0x00000000 alloc_epoch 0 ppe tid 0
        p24 = re.compile(r'^\s*FlowDB in2out\s+(?P<flowdb_in2out>0x[0-9a-fA-F]+)\s+alloc_epoch\s+(?P<flowdb_in2out_alloc_epoch>\d+)\s+out2in\s+(?P<flowdb_out2in>0x[0-9a-fA-F]+)\s+alloc_epoch\s+(?P<flowdb_out2in_alloc_epoch>\d+)\s+ppe tid\s+(?P<ppe_tid>\d+)$')

        # icmp_err_time 0 utd_context_id 0, classification epoch scb: 0x1 actblk :0x1 avc class stats 0x0
        p25 = re.compile(r'^\s*icmp_err_time\s+(?P<icmp_err_time>\d+)\s+utd_context_id\s+(?P<utd_context_id>\d+),\s+classification epoch scb:\s+(?P<classification_epoch_scb>0x[0-9a-fA-F]+)\s+actblk\s+:(?P<classification_epoch_actblk>0x[0-9a-fA-F]+)\s+avc class stats\s+(?P<avc_class_stats>0x[0-9a-fA-F]+)$')

        # icmp_err_time 0 utd_context_id 0, action block epoch 0x1 avc class stats 0x0, VPN id src 65535, dst 65535
        p25a = re.compile(r'^\s*icmp_err_time\s+(?P<icmp_err_time>\d+)\s+utd_context_id\s+(?P<utd_context_id>\d+),\s+action block epoch\s+(?P<classification_epoch_scb>0x[0-9a-fA-F]+)\s+avc class stats\s+(?P<avc_class_stats>0x[0-9a-fA-F]+),\s+VPN id src\s+(?P<vpn_id_src>\d+),\s+dst\s+(?P<vpn_id_dst>\d+)$')

        # icmp_err_time 0 utd_context_id 0, action block epoch 0x1 avc class stats 0x0 (without VPN)
        p25b = re.compile(r'^\s*icmp_err_time\s+(?P<icmp_err_time>\d+)\s+utd_context_id\s+(?P<utd_context_id>\d+),\s+action block epoch\s+(?P<classification_epoch_scb>0x[0-9a-fA-F]+)\s+avc class stats\s+(?P<avc_class_stats>0x[0-9a-fA-F]+)$')

        # VPN id src 65535, dst 65535
        p26 = re.compile(r'^\s*VPN id src\s+(?P<vpn_id_src>\d+),\s+dst\s+(?P<vpn_id_dst>\d+)$')

        # zone pair in-out class nested_cmap
        p27 = re.compile(r'^\s*zone pair\s+(?P<zone_pair>\S+)\s+class\s+(?P<zone_class>\S+)$')

        # Timer information parsing
        # bucket 6909 flags 0x00000001 func 1 idx 0 wheel 0x0a48d020
        p28 = re.compile(r'^\s*bucket\s+(?P<bucket>\d+)\s+flags\s+(?P<flags>0x[0-9a-fA-F]+)\s+func\s+(?P<func>\d+)\s+idx\s+(?P<idx>\d+)\s+wheel\s+(?P<wheel>0x[0-9a-fA-F]+)$')

        # Timer within range
        p29 = re.compile(r'^\s*(?P<timer_status>Timer within range)$')

        # num buckets 131072 cur 2033 mask 0x1ffff gran 160 flag 0x0 ticks 0
        p30 = re.compile(r'^\s*num buckets\s+(?P<num_buckets>\d+)\s+cur\s+(?P<cur>\d+)\s+mask\s+(?P<mask>0x[0-9a-fA-F]+)\s+gran\s+(?P<gran>\d+)\s+flag\s+(?P<flag>0x[0-9a-fA-F]+)\s+ticks\s+(?P<ticks>\d+)$')

        current_session = None

        for line in output.splitlines():
            line = line.strip()

            # Skip header lines
            if line.startswith('[s=session') or not line:
                continue

            # Parse session header
            # Session ID:0x00000001 10.1.1.2 10001 20.1.1.2 20001 proto 17 (-global-:0:-global-:0) (0x2:udp)	[sc]
            # Session ID:0x0000001D 2001:1::1 128 2001:2::2 1428 proto 58 (0:0) (0x3:icmp)	[sd] 1879183652
            m = p1.match(line)
            if m:
                group = m.groupdict()
                session_key = group['session_id']
                current_session = session_key

                # Parse VRF info - handle both formats
                vrf_info = group['vrf_info']
                if ':' in vrf_info and vrf_info.count(':') >= 3:
                    # Format: -global-:0:-global-:0
                    vrf_parts = vrf_info.split(':')
                    vrf_src = vrf_parts[0]
                    vrf_dst = vrf_parts[2] if len(vrf_parts) > 2 else vrf_parts[0]
                else:
                    # Format: 0:0 or similar
                    vrf_src = vrf_info.split(':')[0] if ':' in vrf_info else vrf_info
                    vrf_dst = vrf_info.split(':')[1] if ':' in vrf_info else vrf_info

                parsed.setdefault('sessions', {})[session_key] = {
                    'session_id': group['session_id'],
                    'src_ip': group['src_ip'],
                    'src_port': int(group['src_port']),
                    'dst_ip': group['dst_ip'],
                    'dst_port': int(group['dst_port']),
                    'protocol': int(group['protocol']),
                    'vrf_src': vrf_src,
                    'vrf_dst': vrf_dst,
                    'protocol_name': group['protocol_name'],
                    'flags': group['flags']
                }
                continue

            if not current_session:
                continue

            # Parse pscb and key1_flags
            # pscb : 0x9d00320,  key1_flags: 0x00000000
            m = p2.match(line)
            if m:
                parsed['sessions'][current_session]['pscb'] = m.group('pscb')
                parsed['sessions'][current_session]['key1_flags'] = m.group('key1_flags')
                continue

            # Parse bucket information
            # bucket : 35444, prev 0x0, next 0x0    fw_flags: 0x00000004 0x2041b841,
            m = p3.match(line)
            if m:
                parsed['sessions'][current_session]['bucket'] = int(m.group('bucket'))
                parsed['sessions'][current_session]['prev'] = m.group('prev')
                parsed['sessions'][current_session]['next'] = m.group('next')
                parsed['sessions'][current_session]['fw_flags'] = m.group('fw_flags').split()
                continue

            # Parse alternative bucket format without fw_flags
            # bucket : 42876, prev 0x0, next 0x0
            m = p3a.match(line)
            if m:
                parsed['sessions'][current_session]['bucket'] = int(m.group('bucket'))
                parsed['sessions'][current_session]['prev'] = m.group('prev')
                parsed['sessions'][current_session]['next'] = m.group('next')
                continue

            # Parse standalone fw_flags line
            # fw_flags: 0x00000004 0x2041b861,
            m = p3b.match(line)
            if m:
                parsed['sessions'][current_session]['fw_flags'] = m.group('fw_flags').split()
                continue

            # Parse VRF flags
            # VRF1-rsrc-limit
            m = p4.match(line)
            if m:
                parsed['sessions'][current_session]['vrf_flags'] = m.group('vrf_flags').split()
                continue

            # Parse protocol state
            # Root Protocol-UDP Alert Proto-State:Resp-Init No-halfopen-list Active-cnt Session-db Max-session
            m = p5.match(line)
            if m:
                parsed['sessions'][current_session]['protocol_state'] = m.group('protocol_state').split()
                continue

            # Parse ICMP error
            # icmp_error count 0 ureachable arrived: no
            m = p6.match(line)
            if m:
                parsed['sessions'][current_session]['icmp_error_count'] = int(m.group('icmp_error_count'))
                parsed['sessions'][current_session]['ureachable_arrived'] = m.group('ureachable_arrived')
                continue

            # Parse SCB state
            # scb state: active, nxt_timeout: 6000, refcnt: 1 NBAR verdict count 0
            m = p7.match(line)
            if m:
                parsed['sessions'][current_session]['scb_state'] = m.group('scb_state')
                parsed['sessions'][current_session]['nxt_timeout'] = int(m.group('nxt_timeout'))
                parsed['sessions'][current_session]['refcnt'] = int(m.group('refcnt'))
                parsed['sessions'][current_session]['nbar_verdict_count'] = int(m.group('nbar_verdict_count'))
                continue

            # Parse alternative SCB state without NBAR verdict count
            # scb state: active, nxt_timeout: 6000, refcnt: 1
            m = p7a.match(line)
            if m:
                parsed['sessions'][current_session]['scb_state'] = m.group('scb_state')
                parsed['sessions'][current_session]['nxt_timeout'] = int(m.group('nxt_timeout'))
                parsed['sessions'][current_session]['refcnt'] = int(m.group('refcnt'))
                parsed['sessions'][current_session]['nbar_verdict_count'] = 0  # Default value
                continue

            # Parse HA NAK
            # ha nak cnt: 0, rg: 0
            m = p8.match(line)
            if m:
                parsed['sessions'][current_session]['ha_nak_cnt'] = int(m.group('ha_nak_cnt'))
                parsed['sessions'][current_session]['rg'] = int(m.group('rg'))
                continue

            # Parse hostdb
            # hostdb: 0x0, L7: 0x0, stats: 0xb2c7480, child: 0x0
            m = p9.match(line)
            if m:
                parsed['sessions'][current_session]['hostdb'] = m.group('hostdb')
                parsed['sessions'][current_session]['l7'] = m.group('l7')
                parsed['sessions'][current_session]['stats'] = m.group('stats')
                parsed['sessions'][current_session]['child'] = m.group('child')
                continue

            # Parse octets
            # octets:     1000    packets:         10    octets:     0   packets:     0
            m = p10.match(line)
            if m:
                parsed['sessions'][current_session]['octets_in'] = int(m.group('octets_in'))
                parsed['sessions'][current_session]['packets_in'] = int(m.group('packets_in'))
                parsed['sessions'][current_session]['octets_out'] = int(m.group('octets_out'))
                parsed['sessions'][current_session]['packets_out'] = int(m.group('packets_out'))
                continue

            # Parse cl6 word
            # cl6 word 1:    0x00000000 proto: 0002: l7 ooo drop 0x010 l7_prot 0x2 - udp
            m = p11.match(line)
            if m:
                parsed['sessions'][current_session]['cl6_word'] = m.group('cl6_word')
                parsed['sessions'][current_session]['l7_ooo_drop'] = m.group('l7_ooo_drop')
                parsed['sessions'][current_session]['l7_proto'] = m.group('l7_proto')
                continue

            # Parse icmp seq (alternative format)
            # icmp seq:     17721047137 proto: 0003: l7 ooo drop 0x010 l7_prot 0x3 - icmp
            m = p11a.match(line)
            if m:
                # Set cl6_word to a default value for ICMP sessions without explicit cl6_word
                parsed['sessions'][current_session]['cl6_word'] = '0x00000000'
                parsed['sessions'][current_session]['l7_ooo_drop'] = m.group('l7_ooo_drop')
                parsed['sessions'][current_session]['l7_proto'] = m.group('l7_proto')
                continue

            # Parse icmp seq without l7_prot
            # icmp seq:     17721047137 proto: 0003: l7 ooo drop 0x010
            m = p11b.match(line)
            if m:
                parsed['sessions'][current_session]['cl6_word'] = '0x00000000'
                parsed['sessions'][current_session]['l7_ooo_drop'] = m.group('l7_ooo_drop')
                # Derive l7_proto from protocol number
                proto = int(m.group('proto'))
                if proto == 3:
                    parsed['sessions'][current_session]['l7_proto'] = 'icmp'
                elif proto == 2:
                    parsed['sessions'][current_session]['l7_proto'] = 'udp'
                elif proto == 1:
                    parsed['sessions'][current_session]['l7_proto'] = 'tcp'
                else:
                    parsed['sessions'][current_session]['l7_proto'] = f'proto_{proto}'
                continue

            # Parse root scb
            # root scb: 0x0 act_blk: 0xb2bf400
            m = p12.match(line)
            if m:
                parsed['sessions'][current_session]['root_scb'] = m.group('root_scb')
                parsed['sessions'][current_session]['act_blk'] = m.group('act_blk')
                continue

            # Parse interfaces
            # ingress/egress intf: GigabitEthernet0/0/2 (1021), GigabitEthernet0/0/4 (65525)
            m = p13.match(line)
            if m:
                parsed['sessions'][current_session]['ingress_intf'] = m.group('ingress_intf')
                parsed['sessions'][current_session]['ingress_intf_id'] = int(m.group('ingress_intf_id'))
                parsed['sessions'][current_session]['egress_intf'] = m.group('egress_intf')
                parsed['sessions'][current_session]['egress_intf_id'] = int(m.group('egress_intf_id'))
                continue

            # Parse time information
            # current time 414144656200 create tstamp: 401211845026 last access: 403012409726 now 414144657011 csec left
            m = p14.match(line)
            if m:
                parsed['sessions'][current_session]['current_time'] = int(m.group('current_time'))
                parsed['sessions'][current_session]['create_tstamp'] = int(m.group('create_tstamp'))
                parsed['sessions'][current_session]['last_access'] = int(m.group('last_access'))
                parsed['sessions'][current_session]['now'] = int(m.group('now'))
                parsed['sessions'][current_session]['csec_left'] = m.group('csec_left')
                continue

            # Parse NAT out
            # nat_out_local_addr:port: 0.0.0.0:0
            m = p15.match(line)
            if m:
                parsed['sessions'][current_session]['nat_out_local_addr'] = m.group('nat_out_local_addr')
                parsed['sessions'][current_session]['nat_out_local_port'] = int(m.group('nat_out_local_port'))
                continue

            # Parse NAT in
            # nat_in_global_addr:port: 0.0.0.0:0
            m = p16.match(line)
            if m:
                parsed['sessions'][current_session]['nat_in_global_addr'] = m.group('nat_in_global_addr')
                parsed['sessions'][current_session]['nat_in_global_port'] = int(m.group('nat_in_global_port'))
                continue

            # Parse IP6
            # ip6: addr1 :: addr2 ::
            m = p17.match(line)
            if m:
                parsed['sessions'][current_session]['ip6_addr1'] = m.group('ip6_addr1')
                parsed['sessions'][current_session]['ip6_addr2'] = m.group('ip6_addr2')
                continue

            # Parse key IP4
            # key ip4: addr1 10.1.1.2:10001 addr2 20.1.1.2:20001
            m = p18.match(line)
            if m:
                parsed['sessions'][current_session]['key_ip4_addr1'] = m.group('key_ip4_addr1')
                parsed['sessions'][current_session]['key_ip4_port1'] = int(m.group('key_ip4_port1'))
                parsed['sessions'][current_session]['key_ip4_addr2'] = m.group('key_ip4_addr2')
                parsed['sessions'][current_session]['key_ip4_port2'] = int(m.group('key_ip4_port2'))
                continue

            # Parse syncookie
            # syncookie fixup: 0x0,  halfopen linkage: 0x0 0x0
            m = p19.match(line)
            if m:
                parsed['sessions'][current_session]['syncookie_fixup'] = m.group('syncookie_fixup')
                parsed['sessions'][current_session]['halfopen_linkage'] = m.group('halfopen_linkage').split()
                continue

            # Parse cxsc
            # cxsc_cft_fid: 0x00000000
            m = p20.match(line)
            if m:
                parsed['sessions'][current_session]['cxsc_cft_fid'] = m.group('cxsc_cft_fid')
                continue

            # Parse tw timer
            # tw timer: 0x00000000 0x00000000 0x00000000 0x01adc101
            m = p21.match(line)
            if m:
                parsed['sessions'][current_session]['tw_timer'] = m.group('tw_timer').split()
                continue

            # Parse domain_ab1
            # domain_ab1 0x8468d470 l4 per filter stats 0x0 avc class id 0x0  SGT: 0 DGT: 0
            m = p22.match(line)
            if m:
                parsed['sessions'][current_session]['domain_ab1'] = m.group('domain_ab1')
                parsed['sessions'][current_session]['l4_per_filter_stats'] = m.group('l4_per_filter_stats')
                parsed['sessions'][current_session]['avc_class_id'] = m.group('avc_class_id')
                parsed['sessions'][current_session]['sgt'] = int(m.group('sgt'))
                parsed['sessions'][current_session]['dgt'] = int(m.group('dgt'))
                continue

            # Parse alternative domain_ab1 format with integer avc class id
            # domain_ab1 0x7045ab10 l4 per filter stats 0x0 avc class id 0 SGT: 0 DGT: 0
            m = p22a.match(line)
            if m:
                parsed['sessions'][current_session]['domain_ab1'] = m.group('domain_ab1')
                parsed['sessions'][current_session]['l4_per_filter_stats'] = m.group('l4_per_filter_stats')
                parsed['sessions'][current_session]['avc_class_id'] = m.group('avc_class_id')
                parsed['sessions'][current_session]['sgt'] = int(m.group('sgt'))
                parsed['sessions'][current_session]['dgt'] = int(m.group('dgt'))
                continue

            # Parse NAT handles
            # NAT handles 0x00000000 0x00000000
            m = p23.match(line)
            if m:
                parsed['sessions'][current_session]['nat_handles'] = m.group('nat_handles').split()
                continue

            # Parse FlowDB
            # FlowDB in2out 0x00000000 alloc_epoch 0 out2in 0x00000000 alloc_epoch 0 ppe tid 0
            m = p24.match(line)
            if m:
                parsed['sessions'][current_session]['flowdb_in2out'] = m.group('flowdb_in2out')
                parsed['sessions'][current_session]['flowdb_in2out_alloc_epoch'] = int(m.group('flowdb_in2out_alloc_epoch'))
                parsed['sessions'][current_session]['flowdb_out2in'] = m.group('flowdb_out2in')
                parsed['sessions'][current_session]['flowdb_out2in_alloc_epoch'] = int(m.group('flowdb_out2in_alloc_epoch'))
                parsed['sessions'][current_session]['ppe_tid'] = int(m.group('ppe_tid'))
                continue

            # Parse classification
            # icmp_err_time 0 utd_context_id 0, classification epoch scb: 0x1 actblk :0x1 avc class stats 0x0
            m = p25.match(line)
            if m:
                parsed['sessions'][current_session]['icmp_err_time'] = int(m.group('icmp_err_time'))
                parsed['sessions'][current_session]['utd_context_id'] = int(m.group('utd_context_id'))
                parsed['sessions'][current_session]['classification_epoch_scb'] = m.group('classification_epoch_scb')
                parsed['sessions'][current_session]['classification_epoch_actblk'] = m.group('classification_epoch_actblk')
                parsed['sessions'][current_session]['avc_class_stats'] = m.group('avc_class_stats')
                continue

            # Parse alternative classification with VPN info
            # icmp_err_time 0 utd_context_id 0, action block epoch 0x1 avc class stats 0x0, VPN id src 65535, dst 65535
            m = p25a.match(line)
            if m:
                parsed['sessions'][current_session]['icmp_err_time'] = int(m.group('icmp_err_time'))
                parsed['sessions'][current_session]['utd_context_id'] = int(m.group('utd_context_id'))
                parsed['sessions'][current_session]['classification_epoch_scb'] = m.group('classification_epoch_scb')
                parsed['sessions'][current_session]['classification_epoch_actblk'] = '0x0'  # Default
                parsed['sessions'][current_session]['avc_class_stats'] = m.group('avc_class_stats')
                parsed['sessions'][current_session]['vpn_id_src'] = int(m.group('vpn_id_src'))
                parsed['sessions'][current_session]['vpn_id_dst'] = int(m.group('vpn_id_dst'))
                continue

            # Parse alternative classification without VPN info
            # icmp_err_time 0 utd_context_id 0, action block epoch 0x1 avc class stats 0x0
            m = p25b.match(line)
            if m:
                parsed['sessions'][current_session]['icmp_err_time'] = int(m.group('icmp_err_time'))
                parsed['sessions'][current_session]['utd_context_id'] = int(m.group('utd_context_id'))
                parsed['sessions'][current_session]['classification_epoch_scb'] = m.group('classification_epoch_scb')
                parsed['sessions'][current_session]['classification_epoch_actblk'] = '0x0'  # Default
                parsed['sessions'][current_session]['avc_class_stats'] = m.group('avc_class_stats')
                continue

            # Parse VPN ID
            # VPN id src 65535, dst 65535
            m = p26.match(line)
            if m:
                parsed['sessions'][current_session]['vpn_id_src'] = int(m.group('vpn_id_src'))
                parsed['sessions'][current_session]['vpn_id_dst'] = int(m.group('vpn_id_dst'))
                continue

            # Parse zone pair
            # zone pair in-out class nested_cmap
            m = p27.match(line)
            if m:
                parsed['sessions'][current_session]['zone_pair'] = m.group('zone_pair')
                parsed['sessions'][current_session]['zone_class'] = m.group('zone_class')
                continue

            # Parse timer bucket
            # bucket 6909 flags 0x00000001 func 1 idx 0 wheel 0x0a48d020
            m = p28.match(line)
            if m:
                timer_info = parsed['sessions'][current_session].setdefault('timer_info', {})
                timer_info['bucket'] = int(m.group('bucket'))
                timer_info['flags'] = m.group('flags')
                timer_info['func'] = int(m.group('func'))
                timer_info['idx'] = int(m.group('idx'))
                timer_info['wheel'] = m.group('wheel')
                continue

            # Parse timer status
            # Timer within range
            m = p29.match(line)
            if m:
                if 'timer_info' in parsed['sessions'][current_session]:
                    parsed['sessions'][current_session]['timer_info']['timer_status'] = m.group('timer_status')
                continue

            # Parse timer details
            #num buckets 131072 cur 2033 mask 0x1ffff gran 160 flag 0x0 ticks 0
            m = p30.match(line)
            if m:
                if 'timer_info' in parsed['sessions'][current_session]:
                    timer_info = parsed['sessions'][current_session]['timer_info']
                    timer_info['num_buckets'] = int(m.group('num_buckets'))
                    timer_info['cur'] = int(m.group('cur'))
                    timer_info['mask'] = m.group('mask')
                    timer_info['gran'] = int(m.group('gran'))
                    timer_info['flag'] = m.group('flag')
                    timer_info['ticks'] = int(m.group('ticks'))
                continue

        # Add default values for any missing required fields
        for session_id, session_data in parsed.get('sessions', {}).items():
            # Set default values for missing fields
            if 'zone_pair' not in session_data:
                session_data['zone_pair'] = 'unknown'
            if 'zone_class' not in session_data:
                session_data['zone_class'] = 'unknown'
            if 'vpn_id_src' not in session_data:
                session_data['vpn_id_src'] = 65535
            if 'vpn_id_dst' not in session_data:
                session_data['vpn_id_dst'] = 65535
            if 'classification_epoch_actblk' not in session_data:
                session_data['classification_epoch_actblk'] = '0x0'

        return parsed

class ShowPlatformHardwareQfpActiveFeatureFirewallDropSchema(MetaParser):
    """Schema for show platform hardware qfp active feature firewall drop
                  show platform hardware qfp active feature firewall drop all
                  show platform hardware qfp active feature firewall drop clear
                  show platform hardware qfp active feature firewall drop verbose"""
    schema = {
            str: int
    }

class ShowPlatformHardwareQfpActiveFeatureFirewallDrop(ShowPlatformHardwareQfpActiveFeatureFirewallDropSchema):
    """Parser for show platform hardware qfp active feature firewall drop
                  show platform hardware qfp active feature firewall drop all
                  show platform hardware qfp active feature firewall drop clear
                  show platform hardware qfp active feature firewall drop verbose"""

    cli_command = [
                  'show platform hardware qfp active feature firewall drop',
                  'show platform hardware qfp active feature firewall drop {actions}'
                  ]

    def cli(self, actions="", output=None):
        if output is None:
            if actions:
                cmd = self.cli_command[1].format(actions=actions)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        parsed_dict = {}

        #-------------------------------------------------------------------------------
        #Drop Reason                                                             Packets
        #-------------------------------------------------------------------------------
        #Policy drop:classify result                                                  10

        p1 = re.compile(r'^(?P<drop_reason>.+?)\s{2,}(?P<packets>\d+)$')

        # Split the output into lines
        lines = output.splitlines()

        # Iterate over each line
        for line in lines:
            line = line.strip()
            # Skip the header lines
            if line.startswith('Drop Reason') or line.startswith('---') or line.startswith('All drop counts cleared.'):
                continue

            #-------------------------------------------------------------------------------
            #Drop Reason                                                             Packets
            #-------------------------------------------------------------------------------
            #Policy drop:classify result                                                  10

            m = p1.match(line)
            if m:
                drop_reason = m.group("drop_reason").strip()
                packets = int(m.group("packets"))
                parsed_dict[drop_reason] = packets

        return parsed_dict
            
# =============================================================================================
# Schema for 'show platform hardware qfp active feature nat datapath edm'
# =============================================================================================
class ShowPlatformHardwareQfpActiveFeatureNatDatapathEdmSchema(MetaParser):
    """Schema for show platform hardware qfp active feature nat datapath edm"""
    schema = {
        "bit_stats": {
            "firstword": int,
            "scan": int,
            "scanread": int,
        },
        "tcp_alg_ports": ListOf(int),
        "udp_alg_ports": ListOf(int),
    }

# =============================================================================================
# Parser for 'show platform hardware qfp active feature nat datapath edm'
# =============================================================================================
class ShowPlatformHardwareQfpActiveFeatureNatDatapathEdm(ShowPlatformHardwareQfpActiveFeatureNatDatapathEdmSchema):
    """Parser for show platform hardware qfp active feature nat datapath edm"""
    
    cli_command = "show platform hardware qfp active feature nat datapath edm"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the dictionary to store parsed data
        ret_dict = {}

        # Regex patterns to match the different sections
        # Bit stats: 1stword 1360962 scan 43888 scanread 4140272
        p1 = re.compile(r"^Bit stats:\s+1stword\s+(?P<firstword>\d+)\s+scan\s+(?P<scan>\d+)\s+scanread\s+(?P<scanread>\d+)$")
        
        # TCP ALG Ports: 2000 5060 1723 1720 139 137 135 389 111 8554 53 554 21 514 513 512
        p2 = re.compile(r"^TCP ALG Ports:\s+(?P<ports>[\d\s]+)$")
        
        # UDP ALG Ports: 5060 1719 1718 138 137 111 8554 69 53 554 496
        p3 = re.compile(r"^UDP ALG Ports:\s+(?P<ports>[\d\s]+)$")

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Match bit stats line
            m = p1.match(line)
            if m:
                group = m.groupdict()
                bit_stats_dict = ret_dict.setdefault("bit_stats", {})
                bit_stats_dict["firstword"] = int(group["firstword"])
                bit_stats_dict["scan"] = int(group["scan"])
                bit_stats_dict["scanread"] = int(group["scanread"])
                continue

            # Match TCP ALG Ports line
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ports_str = group["ports"].strip()
                tcp_ports = [int(port) for port in ports_str.split()]
                ret_dict["tcp_alg_ports"] = tcp_ports
                continue

            # Match UDP ALG Ports line
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ports_str = group["ports"].strip()
                udp_ports = [int(port) for port in ports_str.split()]
                ret_dict["udp_alg_ports"] = udp_ports
                continue
                
        return ret_dict

# =======================================================
# Schema for 'show platform hardware qfp active feature evc client l2cp-actions interface {interface}'
# =======================================================
class ShowPlatformHardwareQfpActiveFeatureEvcClientL2cpActionsInterfaceSchema(MetaParser):
    """Schema for show platform hardware qfp active feature evc client l2cp-actions interface {interface}"""
    
    schema = {
        "efp_l2cp_actions": {
            Any(): str  # Protocol name mapped to action (Drop, Fwrd, etc.)
        }
    }


# =======================================================
# Parser for 'show platform hardware qfp active feature evc client l2cp-actions interface {interface}'
# =======================================================
class ShowPlatformHardwareQfpActiveFeatureEvcClientL2cpActionsInterface(
    ShowPlatformHardwareQfpActiveFeatureEvcClientL2cpActionsInterfaceSchema
):
    """Parser for show platform hardware qfp active feature evc client l2cp-actions interface {interface}"""

    cli_command = "show platform hardware qfp active feature evc client l2cp-actions interface {interface}"

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # Initialize the dictionary to store parsed data
        ret_dict = {}

        # Regex patterns to match the different L2CP protocol actions
        # VTP           : Drop
        p1 = re.compile(r"^\s*(?P<protocol>\w+)\s*:\s*(?P<action>\w+)\s*$")

        for line in output.splitlines():
            line = line.strip()

            # Skip header lines
            if line == "EFP L2CP actions" or not line:
                continue

            # Match protocol and action lines
            # VTP           : Drop
            m = p1.match(line)
            if m:
                group = m.groupdict()
                protocol = group["protocol"]
                action = group["action"]

                # Store in the efp_l2cp_actions dictionary
                efp_dict = ret_dict.setdefault("efp_l2cp_actions", {})
                efp_dict[protocol] = action
                continue

        return ret_dict

# ========================================================================
# Schema for 'show platform hardware qfp active feature firewall runtime'
# ========================================================================

class ShowPlatformHardwareQfpActiveFeatureFirewallRuntimeSchema(MetaParser):
    '''Schema for show platform hardware qfp active feature firewall runtime'''
    schema = {
        'global': {
            Any(): {
                'value': str,
                Optional('ha_state'): str,
                Optional('fw_configured'): str,
                Optional('init_done'): str,
                Optional('init_requested'): str,
                Optional('syslog_deployed'): str,
                Optional('salt'): int,
                Optional('global_simultaneous_packets_per_session'): int,
                Optional('default_simultaneous_packets_per_session'): int,
                Optional('half_open'): str,
            }
        },
        Optional('teardowns'): int,
        Optional('pam_cce'): str,
        Optional('num_zp_with_policy'): int,
        Optional('high_priority_recycle_queue_address'): str,
        Optional('low_priority_recycle_queue_address'): str,
        Optional('lock_upgrades'): int,
        Optional('half_open_aggressive_aging'): int,
        Optional('num_ack_exceeds_limit'): int,
        Optional('num_rst_exceeds_limit'): int,
        Optional('unknown_vrf_limit_exceeds'): int,
        Optional('syncookie_over_rate_cnt'): int,
        Optional('fw_tcp_session_termination'): {
            'halfopen': {
                'rst_sent': int,
                'blocked': int,
            },
            'idle': {
                'rst_sent': int,
                'blocked': int,
            },
            'halfclose': {
                'rst_sent': int,
                'blocked': int,
            }
        },
        Optional('nat_caching'): {
            'nat_registration': int,
            'nat_unregistration': int,
            'too_many_nat_sessions': int,
            'cant_register_with_nat': int,
            'invalid_nat_session': int,
            'no_nat_session_caching': int,
            'nat_cached_session': int,
        },
        Optional('l2_firewall'): {
            'l2_unknown_encap': int,
            'l2_skip_tcp_pkt': int,
            'timer_stop_failed': int,
        },
        Optional('vrf_global_action_block'): {
            'l7_inspection_disable_flags': str,
            'total_sessions': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
                'aggr_age_high_watermark': int,
                'aggr_age_low_watermark': int,
                'num_times_enter_aggr_age': int,
                'aggr_age_period': str,
            },
            'tcp_syn_cookie': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
            },
            'total_half_open_sessions': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
                'aggr_age_high_watermark': int,
                'aggr_age_low_watermark': int,
                'num_times_enter_aggr_age': int,
                'aggr_age_period': str,
            },
            'tcp_half_open_sessions': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
            },
            'udp_half_open_sessions': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
            },
            'icmp_half_open_sessions': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
            },
            'domain_flags': str,
        },
        Optional('box_action_block'): {
            'l7_inspection_disable_flags': str,
            'total_sessions': {
                'current_count': int,
                'aggr_age_high_watermark': int,
                'aggr_age_low_watermark': int,
                'num_times_enter_aggr_age': int,
                'aggr_age_period': str,
            },
            'tcp_syn_cookie': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
            },
            'total_half_open_sessions': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
                'aggr_age_high_watermark': int,
                'aggr_age_low_watermark': int,
                'num_times_enter_aggr_age': int,
                'aggr_age_period': str,
            },
            'tcp_half_open_sessions': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
            },
            'udp_half_open_sessions': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
            },
            'icmp_half_open_sessions': {
                'max_limit': int,
                'current_count': int,
                'exceed': int,
            },
            'domain_flags': str,
        },
        Optional('fw_persona_alert_rlimit'): int,
        Optional('fw_persona_backpressure'): str,
        Optional('invalid_rg_exceeds_max'): int,
        Optional('invalid_ha_message_version'): int,
        Optional('rii_hash_table'): {
            'address': str,
            'size': int,
        },
        Optional('vrf_action_table'): {
            'address': str,
            'size': int,
        },
        Optional('avc_stats_table_index_out_of_range'): int,
        Optional('vrf_id_name_table'): {
            Any(): {
                'id': int,
                'name': str,
                'vrf_namehash': str,
                'ipv4': int,
                'ipv6': int,
            }
        },
        Optional('fw_persona_address'): str,
        Optional('vpn_zone_table'): {
            'address': str,
            'size': int,
        }
    }

class ShowPlatformHardwareQfpActiveFeatureFirewallRuntime(ShowPlatformHardwareQfpActiveFeatureFirewallRuntimeSchema):
    '''Parser for show platform hardware qfp active feature firewall runtime'''

    cli_command = 'show platform hardware qfp active feature firewall runtime'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed = {}
        # global 0x020001a1:
        p1 = re.compile(r'^global(?P<num>\d*)\s+(?P<value>0x[0-9a-fA-F]+):$')


        # HA state                               Allow-New-Sess
        p2 = re.compile(r'^\s*HA state\s+(?P<ha_state>\S+)$')

        # FW Configured                          (0x00000020)
        p3 = re.compile(r'^\s*FW Configured\s+\((?P<fw_configured>0x[0-9a-fA-F]+)\)$')

        # Init Done                              (0x00000080)
        p4 = re.compile(r'^\s*Init Done\s+\((?P<init_done>0x[0-9a-fA-F]+)\)$')

        # Init Requested                         (0x00000100)
        p5 = re.compile(r'^\s*Init Requested\s+\((?P<init_requested>0x[0-9a-fA-F]+)\)$')

        # Syslog Deployed                        (0x02000000)
        p6 = re.compile(r'^\s*Syslog Deployed\s+\((?P<syslog_deployed>0x[0-9a-fA-F]+)\)$')

        # Salt                                   196
        p7 = re.compile(r'^\s*Salt\s+(?P<salt>\d+)$')

        # Global number of simultaneous packet per session allowed  0
        p8 = re.compile(r'^\s*Global number of simultaneous packet per session allowed\s+(?P<global_simultaneous>\d+)$')

        # Default number of simultaneous packet per session allowed 25
        p9 = re.compile(r'^\s*Default number of simultaneous packet per session allowed\s+(?P<default_simultaneous>\d+)$')

        # half-open                              (0x00000080)
        p10 = re.compile(r'^\s*half-open\s+\((?P<half_open>0x[0-9a-fA-F]+)\)$')

        # teardowns 0, pam_cce 0x0 00000000
        p11 = re.compile(r'^teardowns\s+(?P<teardowns>\d+),\s+pam_cce\s+(?P<pam_cce>\S+\s+\S+)$')

        # num zp with policy                       1
        p12 = re.compile(r'^num zp with policy\s+(?P<num_zp>\d+)$')

        # High priority recycle queue address      0x846519c0
        p13 = re.compile(r'^High priority recycle queue address\s+(?P<high_priority>0x[0-9a-fA-F]+)$')

        # Low priority recycle queue address       0x846519d0
        p14 = re.compile(r'^Low priority recycle queue address\s+(?P<low_priority>0x[0-9a-fA-F]+)$')

        # Lock upgrades                                   190
        p15 = re.compile(r'^Lock upgrades\s+(?P<lock_upgrades>\d+)$')

        # Half open aggressive aging:              1
        p16 = re.compile(r'^Half open aggressive aging:\s+(?P<half_open_aging>\d+)$')

        # Num of ACK exceeds limit(5):             0
        p17 = re.compile(r'^Num of ACK exceeds limit\(\d+\):\s+(?P<ack_exceeds>\d+)$')

        # Num of RST exceeds limit(5)              0
        p18 = re.compile(r'^Num of RST exceeds limit\(\d+\)\s+(?P<rst_exceeds>\d+)$')

        # Unknown VRF limit exceeds                0
        p19 = re.compile(r'^Unknown VRF limit exceeds\s+(?P<unknown_vrf>\d+)$')

        # syncookie over rate cnt                  0
        p20 = re.compile(r'^syncookie over rate cnt\s+(?P<syncookie_rate>\d+)$')

        # fw tcp session termination RST segment control:
        p21 = re.compile(r'^fw tcp session termination RST segment control:$')

        # halfopen:  RST sent 0, blocked 0
        p22 = re.compile(r'^\s*halfopen:\s+RST sent\s+(?P<rst_sent>\d+),\s+blocked\s+(?P<blocked>\d+)$')

        # idle:      RST sent 0, blocked 0
        p23 = re.compile(r'^\s*idle:\s+RST sent\s+(?P<rst_sent>\d+),\s+blocked\s+(?P<blocked>\d+)$')

        # halfclose: RST sent 0, blocked 0
        p24 = re.compile(r'^\s*halfclose:\s+RST sent\s+(?P<rst_sent>\d+),\s+blocked\s+(?P<blocked>\d+)$')

        # NAT caching:
        p25 = re.compile(r'^NAT caching:$')

        # NAT registration                         100
        p26 = re.compile(r'^NAT registration\s+(?P<nat_registration>\d+)$')

        # NAT unregistration                       100
        p27 = re.compile(r'^NAT unregistration\s+(?P<nat_unregistration>\d+)$')

        # Too many nat sessions                    0
        p28 = re.compile(r'^Too many nat sessions\s+(?P<too_many_nat>\d+)$')

        # Can't register with NAT                0
        p29 = re.compile(r'^\s*Can\'t register with NAT\s+(?P<cant_register>\d+)$')

        # Invalid nat session                    0
        p30 = re.compile(r'^\s*Invalid nat session\s+(?P<invalid_nat>\d+)$')

        # No NAT session caching                 0
        p31 = re.compile(r'^\s*No NAT session caching\s+(?P<no_nat_caching>\d+)$')

        # NAT cached session                     0
        p32 = re.compile(r'^\s*NAT cached session\s+(?P<nat_cached>\d+)$')

        # L2 Firewall:
        p33 = re.compile(r'^L2 Firewall:$')

        # L2 unknown encap                       0
        p34 = re.compile(r'^\s*L2 unknown encap\s+(?P<l2_unknown>\d+)$')

        # L2 skip tcp pkt                        0
        p35 = re.compile(r'^\s*L2 skip tcp pkt\s+(?P<l2_skip>\d+)$')

        # Timer stop failed                      0
        p36 = re.compile(r'^\s*Timer stop failed\s+(?P<timer_stop>\d+)$')

        # VRF Global Action Block:
        p37 = re.compile(r'^VRF Global Action Block:$')

        # Box Action Block:
        p38 = re.compile(r'^Box Action Block:$')

        # L7 Inspection disable flags: 0x0
        p39 = re.compile(r'^\s*L7 Inspection disable flags:\s+(?P<l7_flags>0x[0-9a-fA-F]+)$')

        # Total Sessions:
        p40 = re.compile(r'^\s*Total Sessions:$')

        # max limit: 4294967295, current count: 0, exceed: 0
        p41 = re.compile(r'^\s*max limit:\s+(?P<max_limit>\d+),\s+current count:\s+(?P<current_count>\d+),\s+exceed:\s+(?P<exceed>\d+)$')

        # aggr-age high watermark: 4294967295, low watermark: 0
        p42 = re.compile(r'^\s*aggr-age high watermark:\s+(?P<high_watermark>\d+),\s+low watermark:\s+(?P<low_watermark>\d+)$')

        # num of times enter aggr-age: 0, aggr-age period: off
        p43 = re.compile(r'^\s*num of times enter aggr-age:\s+(?P<num_times>\d+),\s+aggr-age period:\s+(?P<period>\S+)$')

        # TCP SYN Cookie:
        p44 = re.compile(r'^\s*TCP SYN Cookie:$')

        # max limit: 4294967295, current count: 0, exceed: 0
        p45 = re.compile(r'^\s*max limit:\s+(?P<max_limit>\d+),\s+current count:\s+(?P<current_count>\d+),\s+exceed:\s+(?P<exceed>\d+)$')

        # Total Half Open Sessions:
        p46 = re.compile(r'^\s*Total Half Open Sessions:$')

        # TCP Half Open Sessions:
        p47 = re.compile(r'^\s*TCP Half Open Sessions:$')

        # UDP Half Open Sessions:
        p48 = re.compile(r'^\s*UDP Half Open Sessions:$')

        # ICMP Half Open Sessions:
        p49 = re.compile(r'^\s*ICMP Half Open Sessions:$')

        # max limit: 4294967295, current count: 0, exceed: 0
        p50 = re.compile(r'^\s*max limit:\s+(?P<max_limit>\d+),\s+current count:\s+(?P<current_count>\d+),\s+exceed:\s+(?P<exceed>\d+)$')

        # Domain flags: 0x0
        p51 = re.compile(r'^\s*Domain flags:\s+(?P<domain_flags>0x[0-9a-fA-F]+)$')

        # Current count::
        p52 = re.compile(r'^\s*Current count::$')

        # Total Sessions                         0
        p53 = re.compile(r'^\s*Total Sessions\s+(?P<current_count>\d+)$')

        # FW persona alert_rlimit: 0, backpressure: 0x0
        p54 = re.compile(r'^FW persona alert_rlimit:\s+(?P<alert_rlimit>\d+),\s+backpressure:\s+(?P<backpressure>0x[0-9a-fA-F]+)$')

        # Invalid RG (exceeds max RG): 0
        p55 = re.compile(r'^Invalid RG \(exceeds max RG\):\s+(?P<invalid_rg>\d+)$')

        # Invalid HA message version: 0
        p56 = re.compile(r'^Invalid HA message version:\s+(?P<invalid_ha>\d+)$')

        # RII Hash Table:  address 0xc7335810  size 128
        p57 = re.compile(r'^RII Hash Table:\s+address\s+(?P<address>0x[0-9a-fA-F]+)\s+size\s+(?P<size>\d+)$')

        # VRF Action Table Addr 0x0xc80ab800, Size 4096
        p58 = re.compile(r'^VRF Action Table Addr\s+(?P<address>0x[0-9a-fA-Fx]+),\s+Size\s+(?P<size>\d+)$')

        # AVC stats table index out-of-range 0
        p59 = re.compile(r'^AVC stats table index out-of-range\s+(?P<avc_stats>\d+)$')

        # VRF ID-Name Table:
        p60 = re.compile(r'^VRF ID-Name Table:$')

        # VRF:(id=1:name=Mgmt-intf)
        p61 = re.compile(r'^\s*VRF:\(id=(?P<id>\d+):name=(?P<name>[^)]+)\)$')

        # vrf_namehash 712b9b92383e5f4 ipv4 1, ipv6 65535
        p62 = re.compile(r'^\s*vrf_namehash\s+(?P<vrf_namehash>\S+)\s+ipv4\s+(?P<ipv4>\d+),\s+ipv6\s+(?P<ipv6>\d+)$')

        # fw_persona: 0x846519e0 vpn zone table address: 0xc873b400, size 65536
        p63 = re.compile(r'^fw_persona:\s+(?P<persona_address>0x[0-9a-fA-F]+)\s+vpn zone table address:\s+(?P<vpn_address>0x[0-9a-fA-F]+),\s+size\s+(?P<vpn_size>\d+)$')

        current_global = None
        current_section = None
        current_subsection = None
        current_vrf_entry = None

        for line in output.splitlines():
            line = line.strip()

            # Parse global sections
            # global 0x624001a1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                global_key = f"global{group['num']}" if group['num'] else 'global'
                current_global = global_key
                parsed.setdefault('global', {})[current_global] = {'value': group['value']}
                continue

            # Parse HA state
            # HA state                               Allow-New-Sess
            m = p2.match(line)
            if m and current_global:
                parsed['global'][current_global]['ha_state'] = m.group('ha_state')
                continue

            # Parse FW Configured
            # FW Configured                          (0x00000020)
            m = p3.match(line)
            if m and current_global:
                parsed['global'][current_global]['fw_configured'] = m.group('fw_configured')
                continue

            # Parse Init Done
            # Init Done                              (0x00000080)
            m = p4.match(line)
            if m and current_global:
                parsed['global'][current_global]['init_done'] = m.group('init_done')
                continue

            # Parse Init Requested
            # Init Requested                         (0x00000100)
            m = p5.match(line)
            if m and current_global:
                parsed['global'][current_global]['init_requested'] = m.group('init_requested')
                continue

            # Parse Syslog Deployed
            # Syslog Deployed                        (0x02000000)
            m = p6.match(line)
            if m and current_global:
                parsed['global'][current_global]['syslog_deployed'] = m.group('syslog_deployed')
                continue

            # Parse Salt
            # Salt                                   30
            m = p7.match(line)
            if m and current_global:
                parsed['global'][current_global]['salt'] = int(m.group('salt'))
                continue

            # Parse Global simultaneous packets
            # Global number of simultaneous packet per session allowed  0
            m = p8.match(line)
            if m and current_global:
                parsed['global'][current_global]['global_simultaneous_packets_per_session'] = int(m.group('global_simultaneous'))
                continue

            # Parse Default simultaneous packets
            # Default number of simultaneous packet per session allowed 25
            m = p9.match(line)
            if m and current_global:
                parsed['global'][current_global]['default_simultaneous_packets_per_session'] = int(m.group('default_simultaneous'))
                continue

            # Parse half-open
            # half-open                              (0x00000080)
            m = p10.match(line)
            if m and current_global:
                parsed['global'][current_global]['half_open'] = m.group('half_open')
                continue

            # Parse teardowns and pam_cce
            # teardowns 0, pam_cce 0x0 00000000
            m = p11.match(line)
            if m:
                parsed['teardowns'] = int(m.group('teardowns'))
                parsed['pam_cce'] = m.group('pam_cce')
                continue

            # Parse num zp with policy
            # num zp with policy                       1
            m = p12.match(line)
            if m:
                parsed['num_zp_with_policy'] = int(m.group('num_zp'))
                continue

            # Parse High priority recycle queue address
            # High priority recycle queue address      0x820dbbd0
            m = p13.match(line)
            if m:
                parsed['high_priority_recycle_queue_address'] = m.group('high_priority')
                continue

            # Parse Low priority recycle queue address
            # Low priority recycle queue address       0x820dbbe0
            m = p14.match(line)
            if m:
                parsed['low_priority_recycle_queue_address'] = m.group('low_priority')
                continue

            # Parse Lock upgrades
            # Lock upgrades                            190
            m = p15.match(line)
            if m:
                parsed['lock_upgrades'] = int(m.group('lock_upgrades'))
                continue

            # Parse Half open aggressive aging
            # Half open aggressive aging:              1
            m = p16.match(line)
            if m:
                parsed['half_open_aggressive_aging'] = int(m.group('half_open_aging'))
                continue

            # Parse Num of ACK exceeds limit
            # Num of ACK exceeds limit(5):             0
            m = p17.match(line)
            if m:
                parsed['num_ack_exceeds_limit'] = int(m.group('ack_exceeds'))
                continue

            # Parse Num of RST exceeds limit
            # Num of RST exceeds limit(5)              0
            m = p18.match(line)
            if m:
                parsed['num_rst_exceeds_limit'] = int(m.group('rst_exceeds'))
                continue

            # Parse Unknown VRF limit exceeds
            # Unknown VRF limit exceeds                0
            m = p19.match(line)
            if m:
                parsed['unknown_vrf_limit_exceeds'] = int(m.group('unknown_vrf'))
                continue

            # Parse syncookie over rate cnt
            # syncookie over rate cnt                  0
            m = p20.match(line)
            if m:
                parsed['syncookie_over_rate_cnt'] = int(m.group('syncookie_rate'))
                continue

            # Parse fw tcp session termination
            # fw tcp session termination RST segment control:
            m = p21.match(line)
            if m:
                current_section = 'fw_tcp_session_termination'
                parsed[current_section] = {}
                continue

            # Parse halfopen RST
            # halfopen:  RST sent 0, blocked 0
            m = p22.match(line)
            if m and current_section == 'fw_tcp_session_termination':
                parsed[current_section]['halfopen'] = {
                    'rst_sent': int(m.group('rst_sent')),
                    'blocked': int(m.group('blocked'))
                }
                continue

            # Parse idle RST
            # idle:      RST sent 0, blocked 0
            m = p23.match(line)
            if m and current_section == 'fw_tcp_session_termination':
                parsed[current_section]['idle'] = {
                    'rst_sent': int(m.group('rst_sent')),
                    'blocked': int(m.group('blocked'))
                }
                continue

            # Parse halfclose RST
            # halfclose: RST sent 0, blocked 0
            m = p24.match(line)
            if m and current_section == 'fw_tcp_session_termination':
                parsed[current_section]['halfclose'] = {
                    'rst_sent': int(m.group('rst_sent')),
                    'blocked': int(m.group('blocked'))
                }
                continue

            # Parse NAT caching section
            # NAT caching:
            m = p25.match(line)
            if m:
                current_section = 'nat_caching'
                parsed[current_section] = {}
                continue

            # Parse NAT registration
            # NAT registration                         100
            m = p26.match(line)
            if m and current_section == 'nat_caching':
                parsed[current_section]['nat_registration'] = int(m.group('nat_registration'))
                continue

            # Parse NAT unregistration
            # NAT unregistration                       100
            m = p27.match(line)
            if m and current_section == 'nat_caching':
                parsed[current_section]['nat_unregistration'] = int(m.group('nat_unregistration'))
                continue

            # Parse Too many nat sessions
            # Too many nat sessions                    0
            m = p28.match(line)
            if m and current_section == 'nat_caching':
                parsed[current_section]['too_many_nat_sessions'] = int(m.group('too_many_nat'))
                continue

            # Parse Can't register with NAT
            # Can't register with NAT                0
            m = p29.match(line)
            if m and current_section == 'nat_caching':
                parsed[current_section]['cant_register_with_nat'] = int(m.group('cant_register'))
                continue

            # Parse Invalid nat session
            # Invalid nat session                    0
            m = p30.match(line)
            if m and current_section == 'nat_caching':
                parsed[current_section]['invalid_nat_session'] = int(m.group('invalid_nat'))
                continue

            # Parse No NAT session caching
            # No NAT session caching                 0
            m = p31.match(line)
            if m and current_section == 'nat_caching':
                parsed[current_section]['no_nat_session_caching'] = int(m.group('no_nat_caching'))
                continue

            # Parse NAT cached session
            # NAT cached session                     0
            m = p32.match(line)
            if m and current_section == 'nat_caching':
                parsed[current_section]['nat_cached_session'] = int(m.group('nat_cached'))
                continue

            # Parse L2 Firewall section
            # L2 Firewall:
            m = p33.match(line)
            if m:
                current_section = 'l2_firewall'
                parsed[current_section] = {}
                continue

            # Parse L2 unknown encap
            # L2 unknown encap                       0
            m = p34.match(line)
            if m and current_section == 'l2_firewall':
                parsed[current_section]['l2_unknown_encap'] = int(m.group('l2_unknown'))
                continue

            # Parse L2 skip tcp pkt
            # L2 skip tcp pkt                        0
            m = p35.match(line)
            if m and current_section == 'l2_firewall':
                parsed[current_section]['l2_skip_tcp_pkt'] = int(m.group('l2_skip'))
                continue

            # Parse Timer stop failed
            # Timer stop failed                      0
            m = p36.match(line)
            if m and current_section == 'l2_firewall':
                parsed[current_section]['timer_stop_failed'] = int(m.group('timer_stop'))
                continue

            # Parse VRF Global Action Block
            # VRF Global Action Block:
            m = p37.match(line)
            if m:
                current_section = 'vrf_global_action_block'
                parsed[current_section] = {}
                current_subsection = None
                continue

            # Parse Box Action Block
            # Box Action Block:
            m = p38.match(line)
            if m:
                current_section = 'box_action_block'
                parsed[current_section] = {}
                current_subsection = None
                continue

            # Parse L7 Inspection disable flags
            # L7 Inspection disable flags: 0x0
            m = p39.match(line)
            if m and current_section in ['vrf_global_action_block', 'box_action_block']:
                parsed[current_section]['l7_inspection_disable_flags'] = m.group('l7_flags')
                continue

            # Parse Total Sessions
            # Total Sessions:
            m = p40.match(line)
            if m and current_section in ['vrf_global_action_block', 'box_action_block']:
                current_subsection = 'total_sessions'
                parsed[current_section][current_subsection] = {}
                continue

            # Parse session limits
            # max limit: 4294967295, current count: 0, exceed: 0
            m = p41.match(line)
            if m and current_subsection == 'total_sessions':
                parsed[current_section][current_subsection].update({
                    'max_limit': int(m.group('max_limit')),
                    'current_count': int(m.group('current_count')),
                    'exceed': int(m.group('exceed'))
                })
                continue

            # Parse aggr-age watermark
            # aggr-age high watermark: 4294967295, low watermark: 0
            m = p42.match(line)
            if m and current_subsection in ['total_sessions', 'total_half_open_sessions']:
                parsed[current_section][current_subsection].update({
                    'aggr_age_high_watermark': int(m.group('high_watermark')),
                    'aggr_age_low_watermark': int(m.group('low_watermark'))
                })
                continue

            # Parse aggr-age period
            # num of times enter aggr-age: 0, aggr-age period: off
            m = p43.match(line)
            if m and current_subsection in ['total_sessions', 'total_half_open_sessions']:
                parsed[current_section][current_subsection].update({
                    'num_times_enter_aggr_age': int(m.group('num_times')),
                    'aggr_age_period': m.group('period')
                })
                continue

            # Parse TCP SYN Cookie
            # TCP SYN Cookie:
            m = p44.match(line)
            if m and current_section in ['vrf_global_action_block', 'box_action_block']:
                current_subsection = 'tcp_syn_cookie'
                parsed[current_section][current_subsection] = {}
                continue

            # Parse syn cookie limits
            # max limit: 4294967295, current count: 0, exceed: 0
            m = p45.match(line)
            if m and current_subsection == 'tcp_syn_cookie':
                parsed[current_section][current_subsection].update({
                    'max_limit': int(m.group('max_limit')),
                    'current_count': int(m.group('current_count')),
                    'exceed': int(m.group('exceed'))
                })
                continue

            # Parse Total Half Open Sessions
            # Total Half Open Sessions:
            m = p46.match(line)
            if m and current_section in ['vrf_global_action_block', 'box_action_block']:
                current_subsection = 'total_half_open_sessions'
                parsed[current_section][current_subsection] = {}
                continue

            # Parse TCP Half Open Sessions
            # TCP Half Open Sessions:
            m = p47.match(line)
            if m and current_section in ['vrf_global_action_block', 'box_action_block']:
                current_subsection = 'tcp_half_open_sessions'
                parsed[current_section][current_subsection] = {}
                continue

            # Parse UDP Half Open Sessions
            # UDP Half Open Sessions:
            m = p48.match(line)
            if m and current_section in ['vrf_global_action_block', 'box_action_block']:
                current_subsection = 'udp_half_open_sessions'
                parsed[current_section][current_subsection] = {}
                continue

            # Parse ICMP Half Open Sessions
            # ICMP Half Open Sessions:
            m = p49.match(line)
            if m and current_section in ['vrf_global_action_block', 'box_action_block']:
                current_subsection = 'icmp_half_open_sessions'
                parsed[current_section][current_subsection] = {}
                continue

            # Parse half open limits
            # max limit: 4294967295, current count: 0, exceed: 0
            m = p50.match(line)
            if m and current_subsection in ['tcp_half_open_sessions', 'udp_half_open_sessions', 'icmp_half_open_sessions', 'total_half_open_sessions']:
                parsed[current_section][current_subsection].update({
                    'max_limit': int(m.group('max_limit')),
                    'current_count': int(m.group('current_count')),
                    'exceed': int(m.group('exceed'))
                })
                continue

            # Parse Domain flags
            # Domain flags: 0x0
            m = p51.match(line)
            if m and current_section in ['vrf_global_action_block', 'box_action_block']:
                parsed[current_section]['domain_flags'] = m.group('domain_flags')
                continue

            # Parse Current count
            # Current count::
            m = p52.match(line)
            if m and current_section == 'box_action_block':
                current_subsection = 'total_sessions'
                parsed[current_section][current_subsection] = {}
                continue

            # Parse Box total sessions
            # Total Sessions                      0
            m = p53.match(line)
            if m and current_section == 'box_action_block' and current_subsection == 'total_sessions':
                parsed[current_section][current_subsection]['current_count'] = int(m.group('current_count'))
                continue

            # Parse FW persona
            # FW persona alert_rlimit: 0, backpressure: 0x0
            m = p54.match(line)
            if m:
                parsed['fw_persona_alert_rlimit'] = int(m.group('alert_rlimit'))
                parsed['fw_persona_backpressure'] = m.group('backpressure')
                continue

            # Parse Invalid RG
            # Invalid RG (exceeds max RG): 0
            m = p55.match(line)
            if m:
                parsed['invalid_rg_exceeds_max'] = int(m.group('invalid_rg'))
                continue

            # Parse Invalid HA message version
            # Invalid HA message version: 0
            m = p56.match(line)
            if m:
                parsed['invalid_ha_message_version'] = int(m.group('invalid_ha'))
                continue

            # Parse RII Hash Table
            # RII Hash Table:  address 0x40b8ec10  size 128
            m = p57.match(line)
            if m:
                parsed['rii_hash_table'] = {
                    'address': m.group('address'),
                    'size': int(m.group('size'))
                }
                continue

            # Parse VRF Action Table
            # VRF Action Table Addr 0x0x43abb000, Size 4096
            m = p58.match(line)
            if m:
                parsed['vrf_action_table'] = {
                    'address': m.group('address'),
                    'size': int(m.group('size'))
                }
                continue

            # Parse AVC stats
            # AVC stats table index out-of-range 0
            m = p59.match(line)
            if m:
                parsed['avc_stats_table_index_out_of_range'] = int(m.group('avc_stats'))
                continue

            # Parse VRF ID-Name Table
            # VRF ID-Name Table:
            m = p60.match(line)
            if m:
                current_section = 'vrf_id_name_table'
                parsed[current_section] = {}
                continue

            # Parse VRF entry
            # VRF:(id=3:name=green)
            m = p61.match(line)
            if m and current_section == 'vrf_id_name_table':
                vrf_key = f"vrf_{m.group('id')}"
                current_vrf_entry = vrf_key
                parsed[current_section][vrf_key] = {
                    'id': int(m.group('id')),
                    'name': m.group('name')
                }
                continue

            # Parse VRF hash
            # vrf_namehash 9f27410725ab8cc8 ipv4 3, ipv6 503316483
            m = p62.match(line)
            if m and current_vrf_entry and current_section == 'vrf_id_name_table':
                parsed[current_section][current_vrf_entry].update({
                    'vrf_namehash': m.group('vrf_namehash'),
                    'ipv4': int(m.group('ipv4')),
                    'ipv6': int(m.group('ipv6'))
                })
                continue

            # Parse fw_persona and vpn zone table
            # fw_persona: 0x820dbbf0 vpn zone table address: 0x42b07400, size 65536
            m = p63.match(line)
            if m:
                parsed['fw_persona_address'] = m.group('persona_address')
                parsed['vpn_zone_table'] = {
                    'address': m.group('vpn_address'),
                    'size': int(m.group('vpn_size'))
                }
                continue

        return parsed
 
# ===============================================================
# Schema for:
#  * 'show platform hardware qfp active feature nat datapath gatein'
#  * 'show platform hardware qfp active feature nat datapath gateout'
# ===============================================================
class ShowPlatformHardwareQfpActiveFeatureNatDatapathGateSchema(MetaParser):
    """Schema for:
    * 'show platform hardware qfp active feature nat datapath gatein'
    * 'show platform hardware qfp active feature nat datapath gateout'
    """
    
    schema = {
        'gatekeeper_status': str,
        Optional('entries'): {
            Any(): {  # sip address as key
                'sip': str,
                'vrf': int,
                'cnt': int,
                'ts': str,
                'idx': int,
            }
        }
    }

# ===============================================================
# Parser for:
#  * 'show platform hardware qfp active feature nat datapath gatein'
#  * 'show platform hardware qfp active feature nat datapath gateout'
# ===============================================================
class ShowPlatformHardwareQfpActiveFeatureNatDatapathGate(ShowPlatformHardwareQfpActiveFeatureNatDatapathGateSchema):
    """Parser for:
    * 'show platform hardware qfp active feature nat datapath gatein'
    * 'show platform hardware qfp active feature nat datapath gateout'
    """
    
    cli_command = [
        'show platform hardware qfp active feature nat datapath {direction}',
    ]
    
    def cli(self, direction='gatein', output=None):
        if output is None:
            if direction in ['gatein', 'gateout']:
                cmd = self.cli_command[0].format(direction=direction)
            else:
                cmd = self.cli_command[0].format(direction='gatein')  # default to gatein
            out = self.device.execute(cmd)
        else:
            out = output
            
        # Initial return dictionary
        parsed_dict = {}
        
        # Gatekeeper on
        p1 = re.compile(r'^Gatekeeper\s+(?P<status>\w+)$')
        
        # sip 203.0.113.231 vrf 0 cnt 1 ts 0x17ba3f idx 74
        p2 = re.compile(r'^sip\s+(?P<sip>\S+)\s+vrf\s+(?P<vrf>\d+)\s+cnt\s+(?P<cnt>\d+)\s+ts\s+(?P<ts>0x[a-fA-F0-9]+)\s+idx\s+(?P<idx>\d+)$')
        
        gatekeeper_status = None
        entries_found = False
        
        for line in out.splitlines():
            line = line.strip()
            
            # Gatekeeper on
            m = p1.match(line)
            if m:
                gatekeeper_status = m.groupdict()['status']
                continue
                
            # sip 203.0.113.231 vrf 0 cnt 1 ts 0x17ba3f idx 74
            m = p2.match(line)
            if m:
                entries_found = True
                group = m.groupdict()
                sip = group['sip']
                
                # Only add gatekeeper_status when we have actual entries
                if gatekeeper_status is not None and 'gatekeeper_status' not in parsed_dict:
                    parsed_dict['gatekeeper_status'] = gatekeeper_status
                
                entries = parsed_dict.setdefault('entries', {})
                entry = entries.setdefault(sip, {})
                
                entry['sip'] = sip
                entry['vrf'] = int(group['vrf'])
                entry['cnt'] = int(group['cnt'])
                entry['ts'] = group['ts']
                entry['idx'] = int(group['idx'])
                continue            

        return parsed_dict

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsLoginClearSchema(MetaParser):
    """Schema for:
    * 'show platform hardware qfp active feature alg statistics login clear'
    """
    schema = {
        Optional('alg_statistics'): {
            'status': str,  
            Optional('message'): str,  # Error message or status message
            Optional('feature'): str,  # ALG feature name
           }
    }

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsLoginClear(ShowPlatformHardwareQfpActiveFeatureAlgStatisticsLoginClearSchema):
    """Parser for show platform hardware qfp active feature alg statistics login clear"""

    cli_command = [
        'show platform hardware qfp active feature alg statistics login clear'
    ]

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # This ALG doesn't support displaying statistics.
        p1  = re.compile(r"This ALG doesn't support displaying statistics\.")

        for line in out.splitlines():
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # This ALG doesn't support displaying statistics.
            m = p1.match(line)
            if m:
                ret_dict['alg_statistics'] = {
                    'status': 'not_supported',
                    'message': line,
                    'feature': 'login'
                }
                continue

        return ret_dict

class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSipSchema(MetaParser):
    """Schema for show platform hardware qfp active feature alg statistics sip"""

    schema = {
        'sip_info_pool_used_chunk_entries_number': int,
        'receive': {
            'register': {
                'count': int,
                '200_ok': int
            },
            'invite': {
                'count': int,
                '200_ok': int,
                'rexmit_invite': int
            },
            'update': {
                'count': int,
                '200_ok': int
            },
            'bye': {
                'count': int,
                '200_ok': int
            },
            'subscribe': {
                'count': int,
                '200_ok': int
            },
            'refer': {
                'count': int,
                '200_ok': int
            },
            'prack': {
                'count': int,
                '200_ok': int
            },
            'trying': int,
            'ringing': int,
            'ack': int,
            'info': int,
            'cancel': int,
            'sess_prog': int,
            'message': int,
            'notify': int,
            'publish': int,
            'options': int,
            '1xx': int,
            '2xx': int,
            'other_req': int,
            'other_ok': int,
            '3xx_6xx': int
        },
        'events': {
            'null_dport': int,
            'media_port_zero': int,
            'malform_media': int,
            'no_content_length': int,
            'cr_trunk_chnls': int,
            'del_trunk_chnls': int,
            'start_trunk_timer': int,
            'restart_trunk_timer': int,
            'stop_trunk_timer': int,
            'trunk_timer_timeout': int,
            'cr_dbl_entry': int,
            'del_dbl_entry': int,
            'cr_dbl_cfg_entry': int,
            'del_dbl_cfg_entry': int,
            'start_dbl_trig_tmr': int,
            'restart_dbl_trig_tmr': int,
            'stop_dbl_trig_tmr': int,
            'dbl_trig_timeout': int,
            'start_dbl_blk_tmr': int,
            'restart_dbl_blk_tmr': int,
            'stop_dbl_blk_tmr': int,
            'dbl_blk_tmr_timeout': int,
            'start_dbl_idle_tmr': int,
            'restart_dbl_idle_tmr': int,
            'stop_dbl_idle_tmr': int,
            'dbl_idle_tmr_timeout': int,
            'media_addr_zero': int,
            'need_more_data': int,
            'sip_pkt_alloc': int,
            'sip_pkt_free': int,
            'sip_msg_alloc': int,
            'sip_msg_free': int
        },
        'errors': {
            'create_token_err': int,
            'add_portlist_err': int,
            'invalid_offset': int,
            'invalid_pktlen': int,
            'free_magic': int,
            'double_free': int,
            'sess_retmem_failed': int,
            'sess_malloc_failed': int,
            'pkt_retmem_failed': int,
            'pkt_malloc_failed': int,
            'msg_retmem_failed': int,
            'msg_malloc_failed': int,
            'bad_format': int,
            'invalid_proto': int,
            'add_alg_state_fail': int,
            'no_call_id': int,
            'parse_sip_hdr_fail': int,
            'parse_sdp_fail': int,
            'error_new_chnl': int,
            'huge_size': int,
            'create_failed': int,
            'not_sip_msg': int
        },
        'writeback_errors': {
            'offset_err': int,
            'pa_err': int,
            'no_info': int
        },
        'dos_errors': {
            'dbl_retmem_failed': int,
            'dbl_malloc_failed': int,
            'dblcfg_retm_failed': int,
            'dblcfg_malloc_failed': int,
            'session_wlock_ovflw': int,
            'global_wlock_ovflw': int,
            'blacklisted': int
        }
    }


class ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSip(ShowPlatformHardwareQfpActiveFeatureAlgStatisticsSipSchema):
    """Parser for show platform hardware qfp active feature alg statistics sip"""

    cli_command = 'show platform hardware qfp active feature alg statistics sip'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # SIP info pool used chunk entries number: 1
        p1 = re.compile(r'^SIP info pool used chunk entries number:\s+(?P<number>\d+)$')

        # Register:           0 -> 200-OK:            0
        p2 = re.compile(r'^Register:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Invite:             1 -> 200-OK:            0   Rexmit-invite           1
        p3 = re.compile(r'^Invite:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)\s+Rexmit-invite\s+(?P<rexmit>\d+)$')

        # Update:             0 -> 200-OK:            0
        p4 = re.compile(r'^Update:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Bye:                0 -> 200-OK:            0
        p5 = re.compile(r'^Bye:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Subscribe:          0 -> 200-OK:            0
        p6 = re.compile(r'^Subscribe:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Refer:              0 -> 200-OK:            0
        p7 = re.compile(r'^Refer:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Prack:              0 -> 200-OK:            0
        p8 = re.compile(r'^Prack:\s+(?P<count>\d+)\s+->\s+200-OK:\s+(?P<ok>\d+)$')

        # Trying:             0    Ringing:           0    Ack:                   0
        p9 = re.compile(r'^Trying:\s+(?P<trying>\d+)\s+Ringing:\s+(?P<ringing>\d+)\s+Ack:\s+(?P<ack>\d+)$')

        # Info:               0    Cancel:            0    Sess Prog:             0
        p10 = re.compile(r'^Info:\s+(?P<info>\d+)\s+Cancel:\s+(?P<cancel>\d+)\s+Sess Prog:\s+(?P<sess_prog>\d+)$')

        # Message:            0    Notify:            0
        p11 = re.compile(r'^Message:\s+(?P<message>\d+)\s+Notify:\s+(?P<notify>\d+)$')

        # Publish:            0    Options:           0
        p12 = re.compile(r'^Publish:\s+(?P<publish>\d+)\s+Options:\s+(?P<options>\d+)$')

        # 1xx:                0    2xx:               0
        p13 = re.compile(r'^1xx:\s+(?P<one_xx>\d+)\s+2xx:\s+(?P<two_xx>\d+)$')

        # OtherReq:           0    OtherOk:           0    3xx-6xx:               0
        p14 = re.compile(r'^OtherReq:\s+(?P<other_req>\d+)\s+OtherOk:\s+(?P<other_ok>\d+)\s+3xx-6xx:\s+(?P<three_six_xx>\d+)$')

        # Events section patterns
        # Null dport:                   0   Media Port Zero:                0
        p15 = re.compile(r'^Null dport:\s+(?P<null_dport>\d+)\s+Media Port Zero:\s+(?P<media_port_zero>\d+)$')

        # Malform Media:                0   No Content Length:              0
        p16 = re.compile(r'^Malform Media:\s+(?P<malform_media>\d+)\s+No Content Length:\s+(?P<no_content_length>\d+)$')

        # Cr Trunk Chnls:               1   Del Trunk Chnls:                0
        p17 = re.compile(r'^Cr Trunk Chnls:\s+(?P<cr_trunk_chnls>\d+)\s+Del Trunk Chnls:\s+(?P<del_trunk_chnls>\d+)$')

        # start trunk timer:            1   restart trunk timer:            0
        p18 = re.compile(r'^start trunk timer:\s+(?P<start_trunk_timer>\d+)\s+restart trunk timer:\s+(?P<restart_trunk_timer>\d+)$')

        # stop trunk timer:             0   trunk timer timeout:            0
        p19 = re.compile(r'^stop trunk timer:\s+(?P<stop_trunk_timer>\d+)\s+trunk timer timeout:\s+(?P<trunk_timer_timeout>\d+)$')

        # Cr dbl entry:                 0   Del dbl entry:                  0
        p20 = re.compile(r'^Cr dbl entry:\s+(?P<cr_dbl_entry>\d+)\s+Del dbl entry:\s+(?P<del_dbl_entry>\d+)$')

        # Cr dbl cfg entry:             0   Del dbl cfg entry:              0
        p21 = re.compile(r'^Cr dbl cfg entry:\s+(?P<cr_dbl_cfg_entry>\d+)\s+Del dbl cfg entry:\s+(?P<del_dbl_cfg_entry>\d+)$')

        # start dbl trig tmr:           0   restart dbl trig tmr:           0
        p22 = re.compile(r'^start dbl trig tmr:\s+(?P<start_dbl_trig_tmr>\d+)\s+restart dbl trig tmr:\s+(?P<restart_dbl_trig_tmr>\d+)$')

        # stop dbl trig tmr:            0   dbl trig timeout:               0
        p23 = re.compile(r'^stop dbl trig tmr:\s+(?P<stop_dbl_trig_tmr>\d+)\s+dbl trig timeout:\s+(?P<dbl_trig_timeout>\d+)$')

        # start dbl blk tmr:            0   restart dbl blk tmr:            0
        p24 = re.compile(r'^start dbl blk tmr:\s+(?P<start_dbl_blk_tmr>\d+)\s+restart dbl blk tmr:\s+(?P<restart_dbl_blk_tmr>\d+)$')

        # stop dbl blk tmr:             0   dbl blk tmr timeout:            0
        p25 = re.compile(r'^stop dbl blk tmr:\s+(?P<stop_dbl_blk_tmr>\d+)\s+dbl blk tmr timeout:\s+(?P<dbl_blk_tmr_timeout>\d+)$')

        # start dbl idle tmr:           0   restart dbl idle tmr:           0
        p26 = re.compile(r'^start dbl idle tmr:\s+(?P<start_dbl_idle_tmr>\d+)\s+restart dbl idle tmr:\s+(?P<restart_dbl_idle_tmr>\d+)$')

        # stop dbl idle tmr:            0   dbl idle tmr timeout:           0
        p27 = re.compile(r'^stop dbl idle tmr:\s+(?P<stop_dbl_idle_tmr>\d+)\s+dbl idle tmr timeout:\s+(?P<dbl_idle_tmr_timeout>\d+)$')

        # Media Addr Zero:              0   Need More Data:                 0
        p28 = re.compile(r'^Media Addr Zero:\s+(?P<media_addr_zero>\d+)\s+Need More Data:\s+(?P<need_more_data>\d+)$')

        # SIP PKT Alloc:                2   SIP PKT Free:                   2
        p29 = re.compile(r'^SIP PKT Alloc:\s+(?P<sip_pkt_alloc>\d+)\s+SIP PKT Free:\s+(?P<sip_pkt_free>\d+)$')

        # SIP MSG Alloc:                0   SIP MSG Free:                   0
        p30 = re.compile(r'^SIP MSG Alloc:\s+(?P<sip_msg_alloc>\d+)\s+SIP MSG Free:\s+(?P<sip_msg_free>\d+)$')

        # Errors section patterns
        # Create Token Err:             0    Add portlist Err:              0
        p31 = re.compile(r'^Create Token Err:\s+(?P<create_token_err>\d+)\s+Add portlist Err:\s+(?P<add_portlist_err>\d+)$')

        # Invalid Offset:               0    Invalid Pktlen:                0
        p32 = re.compile(r'^Invalid Offset:\s+(?P<invalid_offset>\d+)\s+Invalid Pktlen:\s+(?P<invalid_pktlen>\d+)$')

        # Free Magic:                   0    Double Free:                   0
        p33 = re.compile(r'^Free Magic:\s+(?P<free_magic>\d+)\s+Double Free:\s+(?P<double_free>\d+)$')

        # Sess Retmem Failed:           0    Sess Malloc Failed             0
        p34 = re.compile(r'^Sess Retmem Failed:\s+(?P<sess_retmem_failed>\d+)\s+Sess Malloc Failed\s+(?P<sess_malloc_failed>\d+)$')

        # Pkt Retmem Failed:            0    Pkt Malloc Failed:             0
        p35 = re.compile(r'^Pkt Retmem Failed:\s+(?P<pkt_retmem_failed>\d+)\s+Pkt Malloc Failed:\s+(?P<pkt_malloc_failed>\d+)$')

        # Msg Retmem Failed:            0    Msg Malloc Failed:             0
        p36 = re.compile(r'^Msg Retmem Failed:\s+(?P<msg_retmem_failed>\d+)\s+Msg Malloc Failed:\s+(?P<msg_malloc_failed>\d+)$')

        # Bad Format:                   0    Invalid Proto:                 0
        p37 = re.compile(r'^Bad Format:\s+(?P<bad_format>\d+)\s+Invalid Proto:\s+(?P<invalid_proto>\d+)$')

        # Add ALG state Fail:           0    No Call-id:                    0
        p38 = re.compile(r'^Add ALG state Fail:\s+(?P<add_alg_state_fail>\d+)\s+No Call-id:\s+(?P<no_call_id>\d+)$')

        # Parse SIP Hdr Fail:           0    Parse SDP Fail:                0
        p39 = re.compile(r'^Parse SIP Hdr Fail:\s+(?P<parse_sip_hdr_fail>\d+)\s+Parse SDP Fail:\s+(?P<parse_sdp_fail>\d+)$')

        # Error New Chnl:               0    Huge Size:                     0
        p40 = re.compile(r'^Error New Chnl:\s+(?P<error_new_chnl>\d+)\s+Huge Size:\s+(?P<huge_size>\d+)$')

        # Create Failed:                0    Not SIP Msg:                   0
        p41 = re.compile(r'^Create Failed:\s+(?P<create_failed>\d+)\s+Not SIP Msg:\s+(?P<not_sip_msg>\d+)$')

        # Writeback Errors section patterns
        # Offset Err:                   0    PA Err:                        0
        p42 = re.compile(r'^Offset Err:\s+(?P<offset_err>\d+)\s+PA Err:\s+(?P<pa_err>\d+)$')

        # No Info:                      0
        p43 = re.compile(r'^No Info:\s+(?P<no_info>\d+)$')

        # DoS Errors section patterns
        # Dbl Retmem Failed:            0    Dbl Malloc Failed:             0
        p44 = re.compile(r'^Dbl Retmem Failed:\s+(?P<dbl_retmem_failed>\d+)\s+Dbl Malloc Failed:\s+(?P<dbl_malloc_failed>\d+)$')

        # DblCfg Retm Failed:           0    DblCfg Malloc Failed:          0
        p45 = re.compile(r'^DblCfg Retm Failed:\s+(?P<dblcfg_retm_failed>\d+)\s+DblCfg Malloc Failed:\s+(?P<dblcfg_malloc_failed>\d+)$')

        # Session wlock ovflw:          0    Global wlock ovflw:            0
        p46 = re.compile(r'^Session wlock ovflw:\s+(?P<session_wlock_ovflw>\d+)\s+Global wlock ovflw:\s+(?P<global_wlock_ovflw>\d+)$')

        # Blacklisted:                  0
        p47 = re.compile(r'^Blacklisted:\s+(?P<blacklisted>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # SIP info pool used chunk entries number: 1
            m = p1.match(line)
            if m:
                parsed_dict['sip_info_pool_used_chunk_entries_number'] = int(m.group('number'))
                continue

            # Register:           0 -> 200-OK:            0
            m = p2.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                register_dict = receive_dict.setdefault('register', {})
                register_dict['count'] = int(m.group('count'))
                register_dict['200_ok'] = int(m.group('ok'))
                continue

            # Invite:             1 -> 200-OK:            0   Rexmit-invite           1
            m = p3.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                invite_dict = receive_dict.setdefault('invite', {})
                invite_dict['count'] = int(m.group('count'))
                invite_dict['200_ok'] = int(m.group('ok'))
                invite_dict['rexmit_invite'] = int(m.group('rexmit'))
                continue

            # Update:             0 -> 200-OK:            0
            m = p4.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                update_dict = receive_dict.setdefault('update', {})
                update_dict['count'] = int(m.group('count'))
                update_dict['200_ok'] = int(m.group('ok'))
                continue

            # Bye:                0 -> 200-OK:            0
            m = p5.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                bye_dict = receive_dict.setdefault('bye', {})
                bye_dict['count'] = int(m.group('count'))
                bye_dict['200_ok'] = int(m.group('ok'))
                continue

            # Subscribe:          0 -> 200-OK:            0
            m = p6.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                subscribe_dict = receive_dict.setdefault('subscribe', {})
                subscribe_dict['count'] = int(m.group('count'))
                subscribe_dict['200_ok'] = int(m.group('ok'))
                continue

            # Refer:              0 -> 200-OK:            0
            m = p7.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                refer_dict = receive_dict.setdefault('refer', {})
                refer_dict['count'] = int(m.group('count'))
                refer_dict['200_ok'] = int(m.group('ok'))
                continue

            # Prack:              0 -> 200-OK:            0
            m = p8.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                prack_dict = receive_dict.setdefault('prack', {})
                prack_dict['count'] = int(m.group('count'))
                prack_dict['200_ok'] = int(m.group('ok'))
                continue

            # Trying:             0    Ringing:           0    Ack:                   0
            m = p9.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['trying'] = int(m.group('trying'))
                receive_dict['ringing'] = int(m.group('ringing'))
                receive_dict['ack'] = int(m.group('ack'))
                continue

            # Info:               0    Cancel:            0    Sess Prog:             0
            m = p10.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['info'] = int(m.group('info'))
                receive_dict['cancel'] = int(m.group('cancel'))
                receive_dict['sess_prog'] = int(m.group('sess_prog'))
                continue

            # Message:            0    Notify:            0
            m = p11.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['message'] = int(m.group('message'))
                receive_dict['notify'] = int(m.group('notify'))
                continue

            # Publish:            0    Options:           0
            m = p12.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['publish'] = int(m.group('publish'))
                receive_dict['options'] = int(m.group('options'))
                continue

            # 1xx:                0    2xx:               0
            m = p13.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['1xx'] = int(m.group('one_xx'))
                receive_dict['2xx'] = int(m.group('two_xx'))
                continue

            # OtherReq:           0    OtherOk:           0    3xx-6xx:               0
            m = p14.match(line)
            if m:
                receive_dict = parsed_dict.setdefault('receive', {})
                receive_dict['other_req'] = int(m.group('other_req'))
                receive_dict['other_ok'] = int(m.group('other_ok'))
                receive_dict['3xx_6xx'] = int(m.group('three_six_xx'))
                continue

            # Events section
            # Null dport:                   0   Media Port Zero:                0
            m = p15.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['null_dport'] = int(m.group('null_dport'))
                events_dict['media_port_zero'] = int(m.group('media_port_zero'))
                continue

            # Malform Media:                0   No Content Length:              0
            m = p16.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['malform_media'] = int(m.group('malform_media'))
                events_dict['no_content_length'] = int(m.group('no_content_length'))
                continue

            # Cr Trunk Chnls:               1   Del Trunk Chnls:                0
            m = p17.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['cr_trunk_chnls'] = int(m.group('cr_trunk_chnls'))
                events_dict['del_trunk_chnls'] = int(m.group('del_trunk_chnls'))
                continue

            # start trunk timer:            1   restart trunk timer:            0
            m = p18.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['start_trunk_timer'] = int(m.group('start_trunk_timer'))
                events_dict['restart_trunk_timer'] = int(m.group('restart_trunk_timer'))
                continue

            # stop trunk timer:             0   trunk timer timeout:            0
            m = p19.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['stop_trunk_timer'] = int(m.group('stop_trunk_timer'))
                events_dict['trunk_timer_timeout'] = int(m.group('trunk_timer_timeout'))
                continue

            # Cr dbl entry:                 0   Del dbl entry:                  0
            m = p20.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['cr_dbl_entry'] = int(m.group('cr_dbl_entry'))
                events_dict['del_dbl_entry'] = int(m.group('del_dbl_entry'))
                continue

            # Cr dbl cfg entry:             0   Del dbl cfg entry:              0
            m = p21.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['cr_dbl_cfg_entry'] = int(m.group('cr_dbl_cfg_entry'))
                events_dict['del_dbl_cfg_entry'] = int(m.group('del_dbl_cfg_entry'))
                continue

            # start dbl trig tmr:           0   restart dbl trig tmr:           0
            m = p22.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['start_dbl_trig_tmr'] = int(m.group('start_dbl_trig_tmr'))
                events_dict['restart_dbl_trig_tmr'] = int(m.group('restart_dbl_trig_tmr'))
                continue

            # stop dbl trig tmr:            0   dbl trig timeout:               0
            m = p23.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['stop_dbl_trig_tmr'] = int(m.group('stop_dbl_trig_tmr'))
                events_dict['dbl_trig_timeout'] = int(m.group('dbl_trig_timeout'))
                continue

            # start dbl blk tmr:            0   restart dbl blk tmr:            0
            m = p24.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['start_dbl_blk_tmr'] = int(m.group('start_dbl_blk_tmr'))
                events_dict['restart_dbl_blk_tmr'] = int(m.group('restart_dbl_blk_tmr'))
                continue

            # stop dbl blk tmr:             0   dbl blk tmr timeout:            0
            m = p25.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['stop_dbl_blk_tmr'] = int(m.group('stop_dbl_blk_tmr'))
                events_dict['dbl_blk_tmr_timeout'] = int(m.group('dbl_blk_tmr_timeout'))
                continue

            # start dbl idle tmr:           0   restart dbl idle tmr:           0
            m = p26.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['start_dbl_idle_tmr'] = int(m.group('start_dbl_idle_tmr'))
                events_dict['restart_dbl_idle_tmr'] = int(m.group('restart_dbl_idle_tmr'))
                continue

            # stop dbl idle tmr:            0   dbl idle tmr timeout:           0
            m = p27.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['stop_dbl_idle_tmr'] = int(m.group('stop_dbl_idle_tmr'))
                events_dict['dbl_idle_tmr_timeout'] = int(m.group('dbl_idle_tmr_timeout'))
                continue

            # Media Addr Zero:              0   Need More Data:                 0
            m = p28.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['media_addr_zero'] = int(m.group('media_addr_zero'))
                events_dict['need_more_data'] = int(m.group('need_more_data'))
                continue

            # SIP PKT Alloc:                2   SIP PKT Free:                   2
            m = p29.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['sip_pkt_alloc'] = int(m.group('sip_pkt_alloc'))
                events_dict['sip_pkt_free'] = int(m.group('sip_pkt_free'))
                continue

            # SIP MSG Alloc:                0   SIP MSG Free:                   0
            m = p30.match(line)
            if m:
                events_dict = parsed_dict.setdefault('events', {})
                events_dict['sip_msg_alloc'] = int(m.group('sip_msg_alloc'))
                events_dict['sip_msg_free'] = int(m.group('sip_msg_free'))
                continue

            # Errors section
            # Create Token Err:             0    Add portlist Err:              0
            m = p31.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['create_token_err'] = int(m.group('create_token_err'))
                errors_dict['add_portlist_err'] = int(m.group('add_portlist_err'))
                continue

            # Invalid Offset:               0    Invalid Pktlen:                0
            m = p32.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['invalid_offset'] = int(m.group('invalid_offset'))
                errors_dict['invalid_pktlen'] = int(m.group('invalid_pktlen'))
                continue

            # Free Magic:                   0    Double Free:                   0
            m = p33.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['free_magic'] = int(m.group('free_magic'))
                errors_dict['double_free'] = int(m.group('double_free'))
                continue

            # Sess Retmem Failed:           0    Sess Malloc Failed             0
            m = p34.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['sess_retmem_failed'] = int(m.group('sess_retmem_failed'))
                errors_dict['sess_malloc_failed'] = int(m.group('sess_malloc_failed'))
                continue

            # Pkt Retmem Failed:            0    Pkt Malloc Failed:             0
            m = p35.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['pkt_retmem_failed'] = int(m.group('pkt_retmem_failed'))
                errors_dict['pkt_malloc_failed'] = int(m.group('pkt_malloc_failed'))
                continue

            # Msg Retmem Failed:            0    Msg Malloc Failed:             0
            m = p36.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['msg_retmem_failed'] = int(m.group('msg_retmem_failed'))
                errors_dict['msg_malloc_failed'] = int(m.group('msg_malloc_failed'))
                continue

            # Bad Format:                   0    Invalid Proto:                 0
            m = p37.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['bad_format'] = int(m.group('bad_format'))
                errors_dict['invalid_proto'] = int(m.group('invalid_proto'))
                continue

            # Add ALG state Fail:           0    No Call-id:                    0
            m = p38.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['add_alg_state_fail'] = int(m.group('add_alg_state_fail'))
                errors_dict['no_call_id'] = int(m.group('no_call_id'))
                continue

            # Parse SIP Hdr Fail:           0    Parse SDP Fail:                0
            m = p39.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['parse_sip_hdr_fail'] = int(m.group('parse_sip_hdr_fail'))
                errors_dict['parse_sdp_fail'] = int(m.group('parse_sdp_fail'))
                continue

            # Error New Chnl:               0    Huge Size:                     0
            m = p40.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['error_new_chnl'] = int(m.group('error_new_chnl'))
                errors_dict['huge_size'] = int(m.group('huge_size'))
                continue

            # Create Failed:                0    Not SIP Msg:                   0
            m = p41.match(line)
            if m:
                errors_dict = parsed_dict.setdefault('errors', {})
                errors_dict['create_failed'] = int(m.group('create_failed'))
                errors_dict['not_sip_msg'] = int(m.group('not_sip_msg'))
                continue

            # Writeback Errors section
            # Offset Err:                   0    PA Err:                        0
            m = p42.match(line)
            if m:
                writeback_errors_dict = parsed_dict.setdefault('writeback_errors', {})
                writeback_errors_dict['offset_err'] = int(m.group('offset_err'))
                writeback_errors_dict['pa_err'] = int(m.group('pa_err'))
                continue

            # No Info:                      0
            m = p43.match(line)
            if m:
                writeback_errors_dict = parsed_dict.setdefault('writeback_errors', {})
                writeback_errors_dict['no_info'] = int(m.group('no_info'))
                continue

            # DoS Errors section
            # Dbl Retmem Failed:            0    Dbl Malloc Failed:             0
            m = p44.match(line)
            if m:
                dos_errors_dict = parsed_dict.setdefault('dos_errors', {})
                dos_errors_dict['dbl_retmem_failed'] = int(m.group('dbl_retmem_failed'))
                dos_errors_dict['dbl_malloc_failed'] = int(m.group('dbl_malloc_failed'))
                continue

            # DblCfg Retm Failed:           0    DblCfg Malloc Failed:          0
            m = p45.match(line)
            if m:
                dos_errors_dict = parsed_dict.setdefault('dos_errors', {})
                dos_errors_dict['dblcfg_retm_failed'] = int(m.group('dblcfg_retm_failed'))
                dos_errors_dict['dblcfg_malloc_failed'] = int(m.group('dblcfg_malloc_failed'))
                continue

            # Session wlock ovflw:          0    Global wlock ovflw:            0
            m = p46.match(line)
            if m:
                dos_errors_dict = parsed_dict.setdefault('dos_errors', {})
                dos_errors_dict['session_wlock_ovflw'] = int(m.group('session_wlock_ovflw'))
                dos_errors_dict['global_wlock_ovflw'] = int(m.group('global_wlock_ovflw'))
                continue

            # Blacklisted:                  0
            m = p47.match(line)
            if m:
                dos_errors_dict = parsed_dict.setdefault('dos_errors', {})
                dos_errors_dict['blacklisted'] = int(m.group('blacklisted'))
                continue

        return parsed_dict

# ======================================================================
# Schema for 'show platform hardware qfp active datapath utilization'
# ======================================================================
class ShowPlatformHardwareQfpActiveDatapathUtilizationSchema(MetaParser):
    schema = {
        "cpp": {
            Any(): {
                "subdev": {
                    Any(): {
                        "input": {
                            "priority": {
                                "pps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                },
                                "bps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                }
                            },
                            "non_priority": {
                                "pps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                },
                                "bps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                }
                            },
                            "total": {
                                "pps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                },
                                "bps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                }
                            }
                        },
                        "output": {
                            "priority": {
                                "pps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                },
                                "bps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                }
                            },
                            "non_priority": {
                                "pps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                },
                                "bps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                }
                            },
                            "total": {
                                "pps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                },
                                "bps": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                }
                            }
                        },
                        "processing": {
                            "load_pct": {
                                "5_secs": int,
                                "1_min": int,
                                "5_min": int,
                                "60_min": int
                            }
                        },
                        Optional("crypto_io"): {
                            "crypto": {
                                "load_pct": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                }
                            },
                            "rx": {
                                "load_pct": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                }
                            },
                            "tx": {
                                "load_pct": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                },
                                "idle_pct": {
                                    "5_secs": int,
                                    "1_min": int,
                                    "5_min": int,
                                    "60_min": int
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# ======================================================================
# Parser for 'show platform hardware qfp active datapath utilization'
# ======================================================================
class ShowPlatformHardwareQfpActiveDatapathUtilization(
    ShowPlatformHardwareQfpActiveDatapathUtilizationSchema
):
    cli_command = ["show platform hardware qfp active datapath utilization"]

    def cli(self, output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command[0])

        # CPP 0: Subdev 0            5 secs        1 min        5 min       60 min
        p1 = re.compile(
            r"^\s*CPP (?P<cpp_num>\d+): Subdev (?P<subdev>\d+)\s+"
            r"(?P<time_5s>\d+)\s+secs\s+"
            r"(?P<time_1m>\d+)\s+min\s+"
            r"(?P<time_5m>\d+)\s+min\s+"
            r"(?P<time_60m>\d+)\s+min$"
        )
        
        # Input:  Priority (pps)            0            0            0            0
        # Output: Priority (pps)            0            0            0            0
        # Non-Priority (pps)            2            3            3            1
        # Total (pps)            2            3            3            1
        p2 = re.compile(
            r"^(?P<direction>Input|Output):\s+(?P<priority>Priority|Non-Priority|Total)\s+\((?P<unit>pps|bps)\)\s+"
            r"(?P<val_5s>\d+)\s+"
            r"(?P<val_1m>\d+)\s+"
            r"(?P<val_5m>\d+)\s+"
            r"(?P<val_60m>\d+)$"
        )
        
        # Non-Priority (pps)            2            3            3            1  (line without Input:/Output:)
        # Total (pps)            2            3            3            1  (line without Input:/Output:)
        p2b = re.compile(
            r"^\s+(?P<priority>Non-Priority|Total)\s+\((?P<unit>pps|bps)\)\s+"
            r"(?P<val_5s>\d+)\s+"
            r"(?P<val_1m>\d+)\s+"
            r"(?P<val_5m>\d+)\s+"
            r"(?P<val_60m>\d+)$"
        )
        
        # (bps)         1040         1552         1552          752
        p3 = re.compile(
            r"^\s*\((?P<unit>bps)\)\s+"
            r"(?P<val_5s>\d+)\s+"
            r"(?P<val_1m>\d+)\s+"
            r"(?P<val_5m>\d+)\s+"
            r"(?P<val_60m>\d+)$"
        )
        
        # Processing: Load (pct)            1            1            1            1
        p4 = re.compile(
            r"^Processing:\s+Load\s+\((?P<unit>pct)\)\s+"
            r"(?P<val_5s>\d+)\s+"
            r"(?P<val_1m>\d+)\s+"
            r"(?P<val_5m>\d+)\s+"
            r"(?P<val_60m>\d+)$"
        )
        
        # Crypto/IO
        p5 = re.compile(r"^Crypto/IO$")
        
        # Crypto: Load (pct)            0            0            0            0
        # RX: Load (pct)            0            0            0            0
        # TX: Load (pct)            1            1            1            6
        p6 = re.compile(
            r"^\s+(?P<crypto_type>Crypto|RX|TX):\s+Load\s+\((?P<unit>pct)\)\s+"
            r"(?P<val_5s>\d+)\s+"
            r"(?P<val_1m>\d+)\s+"
            r"(?P<val_5m>\d+)\s+"
            r"(?P<val_60m>\d+)$"
        )
        
        # Idle (pct)           98           98           98           93
        p7 = re.compile(
            r"^\s+Idle\s+\((?P<unit>pct)\)\s+"
            r"(?P<val_5s>\d+)\s+"
            r"(?P<val_1m>\d+)\s+"
            r"(?P<val_5m>\d+)\s+"
            r"(?P<val_60m>\d+)$"
        )

        ret_dict = {}
        current_cpp = None
        current_subdev = None
        current_direction = None
        current_priority = None
        crypto_io_section = False
        
        for line in output.splitlines():
            if not line.strip():
                continue
            
            # CPP 0: Subdev 0            5 secs        1 min        5 min       60 min
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                current_cpp = groups["cpp_num"]
                current_subdev = groups["subdev"]
                crypto_io_section = False
                
                cpp_dict = ret_dict.setdefault("cpp", {}).setdefault(current_cpp, {})
                subdev_dict = cpp_dict.setdefault("subdev", {}).setdefault(current_subdev, {})
                continue
            
            # Crypto/IO
            m = p5.match(line)
            if m:
                crypto_io_section = True
                continue
            
            # Input:  Priority (pps)            0            0            0            0
            # Output: Priority (pps)            0            0            0            0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                current_direction = groups["direction"].lower()
                current_priority = groups["priority"].lower().replace("-", "_")
                unit = groups["unit"]
                
                if current_cpp and current_subdev:
                    subdev_dict = ret_dict["cpp"][current_cpp]["subdev"][current_subdev]
                    dir_dict = subdev_dict.setdefault(current_direction, {})
                    prio_dict = dir_dict.setdefault(current_priority, {})
                    unit_dict = prio_dict.setdefault(unit, {})
                    
                    unit_dict.update({
                        "5_secs": int(groups["val_5s"]),
                        "1_min": int(groups["val_1m"]),
                        "5_min": int(groups["val_5m"]),
                        "60_min": int(groups["val_60m"])
                    })
                continue
            
            # Non-Priority (pps)            2            3            3            1  (line without Input:/Output:)
            # Total (pps)            2            3            3            1  (line without Input:/Output:)
            m = p2b.match(line)
            if m:
                groups = m.groupdict()
                current_priority = groups["priority"].lower().replace("-", "_")
                unit = groups["unit"]
                
                if current_cpp and current_subdev and current_direction:
                    subdev_dict = ret_dict["cpp"][current_cpp]["subdev"][current_subdev]
                    dir_dict = subdev_dict.setdefault(current_direction, {})
                    prio_dict = dir_dict.setdefault(current_priority, {})
                    unit_dict = prio_dict.setdefault(unit, {})
                    
                    unit_dict.update({
                        "5_secs": int(groups["val_5s"]),
                        "1_min": int(groups["val_1m"]),
                        "5_min": int(groups["val_5m"]),
                        "60_min": int(groups["val_60m"])
                    })
                continue
            
            # (bps)         1040         1552         1552          752
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                unit = groups["unit"]
                
                if current_cpp and current_subdev and current_direction and current_priority:
                    subdev_dict = ret_dict["cpp"][current_cpp]["subdev"][current_subdev]
                    dir_dict = subdev_dict[current_direction]
                    prio_dict = dir_dict[current_priority]
                    unit_dict = prio_dict.setdefault(unit, {})
                    
                    unit_dict.update({
                        "5_secs": int(groups["val_5s"]),
                        "1_min": int(groups["val_1m"]),
                        "5_min": int(groups["val_5m"]),
                        "60_min": int(groups["val_60m"])
                    })
                continue
            
            # Processing: Load (pct)            1            1            1            1
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                unit = groups["unit"]
                
                if current_cpp and current_subdev:
                    subdev_dict = ret_dict["cpp"][current_cpp]["subdev"][current_subdev]
                    proc_dict = subdev_dict.setdefault("processing", {})
                    load_dict = proc_dict.setdefault("load_" + unit, {})
                    
                    load_dict.update({
                        "5_secs": int(groups["val_5s"]),
                        "1_min": int(groups["val_1m"]),
                        "5_min": int(groups["val_5m"]),
                        "60_min": int(groups["val_60m"])
                    })
                continue
            
            # Crypto: Load (pct)            0            0            0            0
            # RX: Load (pct)            0            0            0            0
            # TX: Load (pct)            1            1            1            6
            m = p6.match(line)
            if m and crypto_io_section:
                groups = m.groupdict()
                crypto_type = groups["crypto_type"].lower()
                unit = groups["unit"]
                
                if current_cpp and current_subdev:
                    subdev_dict = ret_dict["cpp"][current_cpp]["subdev"][current_subdev]
                    crypto_dict = subdev_dict.setdefault("crypto_io", {})
                    type_dict = crypto_dict.setdefault(crypto_type, {})
                    load_dict = type_dict.setdefault("load_" + unit, {})
                    
                    load_dict.update({
                        "5_secs": int(groups["val_5s"]),
                        "1_min": int(groups["val_1m"]),
                        "5_min": int(groups["val_5m"]),
                        "60_min": int(groups["val_60m"])
                    })
                continue
            
            # Idle (pct)           98           98           98           93
            m = p7.match(line)
            if m and crypto_io_section:
                groups = m.groupdict()
                unit = groups["unit"]
                
                if current_cpp and current_subdev:
                    subdev_dict = ret_dict["cpp"][current_cpp]["subdev"][current_subdev]
                    crypto_dict = subdev_dict.setdefault("crypto_io", {})
                    # Idle goes under TX
                    tx_dict = crypto_dict.setdefault("tx", {})
                    idle_dict = tx_dict.setdefault("idle_" + unit, {})
                    
                    idle_dict.update({
                        "5_secs": int(groups["val_5s"]),
                        "1_min": int(groups["val_1m"]),
                        "5_min": int(groups["val_5m"]),
                        "60_min": int(groups["val_60m"])
                    })
                continue
        return ret_dict

# ========================================================================
# Schema for 'show platform hardware qfp active feature firewall runtime | sec RST segment'
# ========================================================================

class ShowPlatformHardwareQfpActiveFeatureFirewallRuntimeRstSegmentSchema(MetaParser):
    '''Schema for show platform hardware qfp active feature firewall runtime | sec RST segment'''
    schema = {
        'fw_tcp_session_termination': {
            'halfopen': {
                'rst_sent': int,
                'blocked': int,
            },
            'idle': {
                'rst_sent': int,
                'blocked': int,
            },
            'halfclose': {
                'rst_sent': int,
                'blocked': int,
            }
        }
    }

class ShowPlatformHardwareQfpActiveFeatureFirewallRuntimeRstSegment(ShowPlatformHardwareQfpActiveFeatureFirewallRuntimeRstSegmentSchema):
    '''Parser for show platform hardware qfp active feature firewall runtime | sec RST segment'''

    cli_command = 'show platform hardware qfp active feature firewall runtime | sec RST segment'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed = {}

        # fw tcp session termination RST segment control:
        p1 = re.compile(r'^fw tcp session termination RST segment control:$')

        # halfopen:  RST sent 0, blocked 0
        p2 = re.compile(r'^\s*halfopen:\s+RST sent\s+(?P<rst_sent>\d+),\s+blocked\s+(?P<blocked>\d+)$')

        # idle:      RST sent 0, blocked 0
        p3 = re.compile(r'^\s*idle:\s+RST sent\s+(?P<rst_sent>\d+),\s+blocked\s+(?P<blocked>\d+)$')

        # halfclose: RST sent 0, blocked 0
        p4 = re.compile(r'^\s*halfclose:\s+RST sent\s+(?P<rst_sent>\d+),\s+blocked\s+(?P<blocked>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # fw tcp session termination RST segment control:
            m = p1.match(line)
            if m:
                fw_tcp_dict = parsed.setdefault('fw_tcp_session_termination', {})
                continue

            # halfopen:  RST sent 0, blocked 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                halfopen_dict = fw_tcp_dict.setdefault('halfopen', {})
                halfopen_dict['rst_sent'] = int(group['rst_sent'])
                halfopen_dict['blocked'] = int(group['blocked'])
                continue

            # idle:      RST sent 0, blocked 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                idle_dict = fw_tcp_dict.setdefault('idle', {})
                idle_dict['rst_sent'] = int(group['rst_sent'])
                idle_dict['blocked'] = int(group['blocked'])
                continue

            # halfclose: RST sent 0, blocked 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                halfclose_dict = fw_tcp_dict.setdefault('halfclose', {})
                halfclose_dict['rst_sent'] = int(group['rst_sent'])
                halfclose_dict['blocked'] = int(group['blocked'])
                continue

        return parsed

class ShowPlatformHardwareCppActiveSystemStateSchema(MetaParser):
    """Schema for show platform hardware cpp active system state"""
    schema = {
        'cpp_ha': str,
        'cpp_cp': str,
        'cpp_sp': str,
        'fman_fp': str,
        'cpp_driver0': str,
        'platform_state': {
            'curr': str,
            'next': str
        },
        'ha_state': {
            'cpp': int,
            'dir': str,
            'role': {
                'curr': str,
                'next': str
            }
        },
        'client_state': str,
        'image': str,
        'load_cnt': int,
        'time': str,
        'active_threads': str,
        'fault_manager_flags': {
            'ignore_fault': str,
            'ignore_stuck_thread': str,
            'crashdump_in_progress': str
        }
    }

class ShowPlatformHardwareCppActiveSystemState(ShowPlatformHardwareCppActiveSystemStateSchema):
    """Parser for show platform hardware cpp active system state"""

    cli_command = "show platform hardware cpp active system state"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the dictionary to store parsed data
        ret_dict = {}

        # cpp_cp : Initialized
        # cpp_sp : Initialized
        # FMAN-FP : Initialized
        # cpp_driver0 : Initialized
        p1 = re.compile(r'^(?P<component>\w+(?:-\w+)*)\s*:\s*(?P<status>\w+)\s*$')
        
        # Platform State: curr=ACTIVE_SOLO next=ACTIVE_SOLO
        p2 = re.compile(r'^Platform State:\s*curr=(?P<curr>\S+)\s*next=(?P<next>\S+)\s*$')
        
        # HA State: CPP=0 dir=BOTH Role: curr=ACTIVE_SOLO next=ACTIVE_SOLO
        p3 = re.compile(r'^HA State:\s*CPP=(?P<cpp>\d+)\s*dir=(?P<dir>\S+)\s*Role:\s*curr=(?P<curr>\S+)\s*next=(?P<next>\S+)\s*$')
        
        # Client State: ENABLE
        p4 = re.compile(r'^Client State:\s*(?P<state>\S+)\s*$')
        
        # Image: /tmp/sw/fp/0/0/fp/mount/usr/cpp/bin/qfp-ucode-fugazi
        p5 = re.compile(r'^Image:\s*(?P<image>\S+)\s*$')
        
        # Load Cnt: 1 Time: Sep 04, 2025 01:36:17
        p6 = re.compile(r'^Load Cnt:\s*(?P<load_cnt>\d+)\s*Time:\s*(?P<time>.*)\s*$')
        
        # Active Threads: 0-15
        p7 = re.compile(r'^Active Threads:\s*(?P<threads>.*)\s*$')
        
        # Fault Manager Flags:
        p8 = re.compile(r'^Fault Manager Flags:\s*$')
        
        # ignore_fault:          FALSE
        # ignore_stuck_thread:   FALSE
        # crashdump_in_progress: FALSE
        p9 = re.compile(r'^\s*(?P<flag_name>\w+):\s*(?P<flag_value>\w+)\s*$')

        fault_manager_section = False

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue
        
            # Fault Manager Flags:
            m = p8.match(line)
            if m:
                fault_manager_section = True
                ret_dict['fault_manager_flags'] = {}
                continue

            # Component status lines (cpp_cp, cpp_sp, FMAN-FP, cpp_driver0)
            if not fault_manager_section:
                m = p1.match(line)
                if m:
                    component = m.group('component').lower().replace('-', '_')
                    status = m.group('status')
                    ret_dict[component] = status
                    continue

            # Platform State: curr=ACTIVE_SOLO next=ACTIVE_SOLO
            m = p2.match(line)
            if m:
                ret_dict['platform_state'] = {
                    'curr': m.group('curr'),
                    'next': m.group('next')
                }
                continue

            # HA State: CPP=0 dir=BOTH Role: curr=ACTIVE_SOLO next=ACTIVE_SOLO
            m = p3.match(line)
            if m:
                ret_dict['ha_state'] = {
                    'cpp': int(m.group('cpp')),
                    'dir': m.group('dir'),
                    'role': {
                        'curr': m.group('curr'),
                        'next': m.group('next')
                    }
                }
                continue

            # Client State: ENABLE
            m = p4.match(line)
            if m:
                ret_dict['client_state'] = m.group('state')
                continue

            # Image: /tmp/sw/fp/0/0/fp/mount/usr/cpp/bin/qfp-ucode-fugazi
            m = p5.match(line)
            if m:
                ret_dict['image'] = m.group('image')
                continue

            # Load Cnt: 1 Time: Sep 04, 2025 01:36:17
            m = p6.match(line)
            if m:
                ret_dict['load_cnt'] = int(m.group('load_cnt'))
                ret_dict['time'] = m.group('time').strip()
                continue

            # Active Threads: 0-15
            m = p7.match(line)
            if m:
                ret_dict['active_threads'] = m.group('threads').strip()
                continue

            # Flag lines under Fault Manager Flags
            if fault_manager_section:
                m = p9.match(line)
                if m:
                    flag_name = m.group('flag_name')
                    flag_value = m.group('flag_value')
                    ret_dict['fault_manager_flags'][flag_name] = flag_value
                    continue
                
        return ret_dict

# ==============================================
# Schema for:
#  * 'show platform hardware qfp active feature firewall zonepair {id}'
# ==============================================
class ShowPlatformHardwareQfpActiveFeatureFirewallZonepairSchema(MetaParser):
    """Schema for show platform hardware qfp active feature firewall zonepair {id}"""

    schema = {
        'zonepair': {
            'name': str,
            'id': int,
            'source_zone': {
                'name': str,
                'id': int,
            },
            'destination_zone': {
                'name': str,
                'id': int,
            },
            'class_group': {
                'name': str,
                'id': int,
            },
            'lookup_data': {
                'sw': ListOf(str),
                'hw': ListOf(str),
            },
            'classes': ListOf({
                'name': str,
                'id': int,
                'number_of_protocols': int,
                Optional('protocols'): ListOf(int),
                'maxever_number_of_packet_per_flow': int,
                'addresses': {
                    'filler_block': str,
                    'action_block': str,
                    'stats_table': str,
                    Optional('stats_blocks'): ListOf(str),
                },
                'result': ListOf(str),
                'filler_block': {
                    'sw': str,
                    'hw': str,
                },
                Optional('action_block_hw'): str,
            })
        }
    }


# ==============================================
# Parser for:
#  * 'show platform hardware qfp active feature firewall zonepair {id}'
# ==============================================
class ShowPlatformHardwareQfpActiveFeatureFirewallZonepair(ShowPlatformHardwareQfpActiveFeatureFirewallZonepairSchema):
    """Parser for show platform hardware qfp active feature firewall zonepair {id}"""

    cli_command = 'show platform hardware qfp active feature firewall zonepair {id}'

    def cli(self, id='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(id=id))

        parsed_dict = {}
        current_class = None

        # Regex patterns
        # Zonepair name:zp-ge000-ge003 | id:1
        p1 = re.compile(r'^Zonepair name:(?P<name>\S+) \| id:(?P<id>\d+)$')
        # Source zone name:ge0-0-0 | id:2
        p2 = re.compile(r'^Source zone name:(?P<name>\S+) \| id:(?P<id>\d+)$')
        # Destination zone name:ge0-0-3 | id:1
        p3 = re.compile(r'^Destination zone name:(?P<name>\S+) \| id:(?P<id>\d+)$')
        # Class group name:policy1 | id:14841376
        p4 = re.compile(r'^Class group name:(?P<name>\S+) \| id:(?P<id>\d+)$')
        # lookup data in sw: 0x00010003, 0x00084441
        p5 = re.compile(r'^lookup data in sw: (?P<data>[\w, x]+)$')
        # lookup data in hw: 0x00010003, 0x00084441
        p6 = re.compile(r'^lookup data in hw: (?P<data>[\w, x]+)$')
        # Class name:c-ftp-tcp | id:13549553
        p7 = re.compile(r'^Class name:(?P<name>\S+) \| id:(?P<id>\d+)$')
        # Number of Protocols: 4
        p8 = re.compile(r'^Number of Protocols: (?P<num>\d+)$')
        # Protocols: 1, 2, 4, 18
        p9 = re.compile(r'^Protocols: (?P<protocols>[\d, ]+)$')
        # Maxever number of packet per flow: 25
        p10 = re.compile(r'^Maxever number of packet per flow: (?P<num>\d+)$')
        # Filler block/Action block/Stats table addresses: 0x8967f400, 0x8d70f400, 0x898d7400
        p11 = re.compile(r'^Filler block\/Action block\/Stats table addresses: (?P<filler>\w+), (?P<action>\w+), (?P<stats>\w+)$')
        # Stats blocks addresses: 0x8d716c00, 0x8d716c40, 0x8d716c80, 0x8d716cc0
        p12 = re.compile(r'^Stats blocks addresses: (?P<stats_blocks>[\w, ]+)$')
        # Result: 0x08000000, 0x8967f400
        p13 = re.compile(r'^Result: (?P<result>[\w, x]+)$')
        # Filler block in sw: 0x8d70f400898d7400
        p14 = re.compile(r'^Filler block in sw: (?P<block>\w+)$')
        # Filler block in hw: 0x0000000c00000000
        p15 = re.compile(r'^Filler block in hw: (?P<block>[\w]+)$')
        # Action block in hw:
        p16 = re.compile(r'^Action block in hw:(?P<block>.*)$')

        for line in output.splitlines():
            line = line.strip()

            # Zonepair name:zp-ge000-ge003 | id:1
            m = p1.match(line)
            if m:
                parsed_dict['zonepair'] = {
                    'name': m.group('name'),
                    'id': int(m.group('id')),
                }
                continue

            # Source zone name:ge0-0-0 | id:2
            m = p2.match(line)
            if m:
                parsed_dict['zonepair']['source_zone'] = {
                    'name': m.group('name'),
                    'id': int(m.group('id'))
                }
                continue

            # Destination zone name:ge0-0-3 | id:1
            m = p3.match(line)
            if m:
                parsed_dict['zonepair']['destination_zone'] = {
                    'name': m.group('name'),
                    'id': int(m.group('id'))
                }
                continue

            # Class group name:policy1 | id:14841376
            m = p4.match(line)
            if m:
                parsed_dict['zonepair']['class_group'] = {
                    'name': m.group('name'),
                    'id': int(m.group('id'))
                }
                continue

            # lookup data in sw: 0x00010003, 0x00084441
            m = p5.match(line)
            if m:
                parsed_dict['zonepair'].setdefault('lookup_data', {})
                parsed_dict['zonepair']['lookup_data']['sw'] = [x.strip() for x in m.group('data').split(',')]
                continue

            # lookup data in hw: 0x00010003, 0x00084441
            m = p6.match(line)
            if m:
                parsed_dict['zonepair'].setdefault('lookup_data', {})
                parsed_dict['zonepair']['lookup_data']['hw'] = [x.strip() for x in m.group('data').split(',')]
                continue

            # Class name:c-ftp-tcp | id:13549553
            m = p7.match(line)
            if m:
                parsed_dict['zonepair'].setdefault('classes', [])
                current_class = {
                    'name': m.group('name'),
                    'id': int(m.group('id')),
                }
                parsed_dict['zonepair']['classes'].append(current_class)
                continue

            # Number of Protocols: 4
            m = p8.match(line)
            if m and current_class:
                current_class['number_of_protocols'] = int(m.group('num'))
                continue

            # Protocols: 1, 2, 4, 18
            m = p9.match(line)
            if m and current_class:
                current_class['protocols'] = [int(x.strip()) for x in m.group('protocols').split(',')]
                continue

            # Maxever number of packet per flow: 25
            m = p10.match(line)
            if m and current_class:
                current_class['maxever_number_of_packet_per_flow'] = int(m.group('num'))
                continue

            # Filler block/Action block/Stats table addresses: 0x8967f400, 0x8d70f400, 0x898d7400
            m = p11.match(line)
            if m and current_class:
                current_class['addresses'] = {
                    'filler_block': m.group('filler'),
                    'action_block': m.group('action'),
                    'stats_table': m.group('stats')
                }
                continue

            # Stats blocks addresses: 0x8d716c00, 0x8d716c40, 0x8d716c80, 0x8d716cc0
            m = p12.match(line)
            if m and current_class:
                current_class['addresses']['stats_blocks'] = [x.strip() for x in m.group('stats_blocks').split(',')]
                continue

            # Result: 0x08000000, 0x8967f400
            m = p13.match(line)
            if m and current_class:
                current_class['result'] = [x.strip() for x in m.group('result').split(',')]
                continue

            # Filler block in sw: 0x8d70f400898d7400
            m = p14.match(line)
            if m and current_class:
                current_class.setdefault('filler_block', {})
                current_class['filler_block']['sw'] = m.group('block')
                continue

            # Filler block in hw: 0x0000000c00000000
            m = p15.match(line)
            if m and current_class:
                current_class.setdefault('filler_block', {})
                current_class['filler_block']['hw'] = m.group('block')
                continue

            # Action block HW
            m = p16.match(line)
            if m and current_class and m.group('block') and m.group('block').strip():
                current_class['action_block_hw'] = m.group('block').strip()
                continue

        return parsed_dict

# ==============================
# Schema for ShowPlatformHardwareQfpActiveInfrastructureBqsScheduleOutputDefault
# ==============================
class ShowPlatformHardwareQfpActiveInfrastructureBqsScheduleOutputDefaultSchema(MetaParser):
    """Schema for show platform hardware qfp active infrastructure bqs schedule output default interface {interface}"""

    schema = {
        Any(): {
            "if_h": int,
            "qfp": str,
            "num_queues_schedules": int,
            Optional("schedule_specifics"): {
                Optional("index"): {
                    Any(): {
                        "sid": str,
                        "name": str,
                        "parq_software_control_info": {
                            "sid": str,
                            "parent_sid": str,
                            "evfc_fc_id": str,
                            "fc_sid": str,
                            "obj_id": str,
                            "parent_obj_id": str,
                            "debug_name": str,
                            "num_entries_active": int,
                            Optional("total_children_act_inact"): str,
                            "num_children_max": int,
                            "presize_hint": int,
                            "sw_flags": str,
                            "sw_state": str,
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
                            "service_fragment": str,
                            "port_uidb": int,
                            "priority": int,
                            "defer_obj_refcnt": int,
                        },
                    },
                },
            },
        },
    }


# ==============================
# Parser for ShowPlatformHardwareQfpActiveInfrastructureBqsScheduleOutputDefault
# ==============================
class ShowPlatformHardwareQfpActiveInfrastructureBqsScheduleOutputDefault(ShowPlatformHardwareQfpActiveInfrastructureBqsScheduleOutputDefaultSchema):
    """Parser for show platform hardware qfp active infrastructure bqs schedule output default interface {interface}"""

    cli_command = [
        "show platform hardware qfp active infrastructure bqs schedule output default interface {interface}",
    ]

    def cli(self, interface="", output=None):
        if output is None:
            cmd = self.cli_command[0].format(interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Interface: GigabitEthernet1 QFP: 0.0 if_h: 6 Num Queues/Schedules: 1
        p1 = re.compile(
            r"^Interface: +(?P<intf_name>[\w\d\/\.\-\:]+)"
            r" +QFP: +(?P<qfp>[\d\.]+)"
            r" +if_h: +(?P<if_h>\d+)"
            r" +Num Queues/Schedules: +(?P<num_queues>\d+)$"
        )

        # Schedule specifics:
        p2 = re.compile(r"^Schedule specifics:$")

        # Index 0 (SID:0x8b, Name: GigabitEthernet1)
        p3 = re.compile(
            r"^Index +(?P<index>\d+)"
            r" +\(SID:(?P<sid>[\w\d]+),"
            r" +Name: +(?P<name>[\w\d\/\.\-\:]+)\)$"
        )

        # PARQ Software Control Info:
        p4 = re.compile(r"^PARQ Software Control Info:$")

        # sid: 0x8b, parent_sid: 0x8a
        p5 = re.compile(
            r"^sid: +(?P<sid>[\w\d]+), +parent_sid: +(?P<parent_sid>[\w\d]+)$"
        )

        # evfc_fc_id: 0xffff, fc_sid: 0xfffff
        p6 = re.compile(
            r"^evfc_fc_id: +(?P<evfc_fc_id>[\w\d]+), +fc_sid: +(?P<fc_sid>[\w\d]+)$"
        )

        # obj_id: 0x12, parent_obj_id: 0x11, debug_name: GigabitEthernet1
        p7 = re.compile(
            r"^obj_id: +(?P<obj_id>[\w\d]+), +parent_obj_id: +(?P<parent_obj_id>[\w\d]+), +debug_name: +(?P<debug_name>[\w\d\/\.\-\:]+)$"
        )

        # num_entries (active): 1, total_children (act/inact): , num_children (max): 1
        p8 = re.compile(
            r"^num_entries +\(active\): +(?P<num_entries_active>\d+), +total_children +\(act/inact\): +(?P<total_children>.*?), +num_children +\(max\): +(?P<num_children_max>\d+)$"
        )

        # presize_hint: 0
        p9 = re.compile(r"^presize_hint: +(?P<presize_hint>\d+)$")

        # sw_flags: 0x0802002a, sw_state: 0x00000801
        p10 = re.compile(
            r"^sw_flags: +(?P<sw_flags>[\w\d]+), +sw_state: +(?P<sw_state>[\w\d]+)$"
        )

        # orig_min  : 0                   ,      min: 0
        p11 = re.compile(r"^orig_min +: +(?P<orig_min>\d+) +, +min: +(?P<min>\d+)$")

        # min_qos   : 0                   , min_dflt: 1050000000
        p12 = re.compile(
            r"^min_qos +: +(?P<min_qos>\d+) +, +min_dflt: +(?P<min_dflt>\d+)$"
        )

        # orig_max  : 0                   ,      max: 1050000000
        p13 = re.compile(r"^orig_max +: +(?P<orig_max>\d+) +, +max: +(?P<max>\d+)$")

        # max_qos   : 0                   , max_dflt: 1050000000
        p14 = re.compile(
            r"^max_qos +: +(?P<max_qos>\d+) +, +max_dflt: +(?P<max_dflt>\d+)$"
        )

        # share     : 105
        p15 = re.compile(r"^share +: +(?P<share>\d+)$")

        # plevel: 0, service_fragment: False, port_uidb: 65530
        p16 = re.compile(
            r"^plevel: +(?P<plevel>\d+), +service_fragment: +(?P<service_fragment>\w+), +port_uidb: +(?P<port_uidb>\d+)$"
        )

        # priority: 0, defer_obj_refcnt: 0
        p17 = re.compile(
            r"^priority: +(?P<priority>\d+), +defer_obj_refcnt: +(?P<defer_obj_refcnt>\d+)$"
        )

        current_interface = None
        current_index = None
        in_schedule_specifics = False

        for line in out.splitlines():
            line = line.strip()

            # Interface: GigabitEthernet1 QFP: 0.0 if_h: 6 Num Queues/Schedules: 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_interface = group["intf_name"]
                ret_dict.setdefault(current_interface, {})
                ret_dict[current_interface]["if_h"] = int(group["if_h"])
                ret_dict[current_interface]["qfp"] = group["qfp"]
                ret_dict[current_interface]["num_queues_schedules"] = int(group["num_queues"])
                continue

            # Schedule specifics:
            m = p2.match(line)
            if m and current_interface:
                in_schedule_specifics = True
                ret_dict[current_interface].setdefault("schedule_specifics", {})
                continue

            # Index 0 (SID:0x8b, Name: GigabitEthernet1)
            m = p3.match(line)
            if m and current_interface and in_schedule_specifics:
                group = m.groupdict()
                current_index = group["index"]
                ret_dict[current_interface]["schedule_specifics"].setdefault("index", {})
                ret_dict[current_interface]["schedule_specifics"]["index"].setdefault(current_index, {})
                ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["sid"] = group["sid"]
                ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["name"] = group["name"]
                continue

            # PARQ Software Control Info:
            m = p4.match(line)
            if m and current_interface and current_index:
                ret_dict[current_interface]["schedule_specifics"]["index"][current_index].setdefault("parq_software_control_info", {})
                continue

            # sid: 0x8b, parent_sid: 0x8a
            m = p5.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["sid"] = group["sid"]
                control_info["parent_sid"] = group["parent_sid"]
                continue

            # evfc_fc_id: 0xffff, fc_sid: 0xfffff
            m = p6.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["evfc_fc_id"] = group["evfc_fc_id"]
                control_info["fc_sid"] = group["fc_sid"]
                continue

            # obj_id: 0x12, parent_obj_id: 0x11, debug_name: GigabitEthernet1
            m = p7.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["obj_id"] = group["obj_id"]
                control_info["parent_obj_id"] = group["parent_obj_id"]
                control_info["debug_name"] = group["debug_name"]
                continue

            # num_entries (active): 1, total_children (act/inact): , num_children (max): 1
            m = p8.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["num_entries_active"] = int(group["num_entries_active"])
                if group["total_children"].strip():
                    control_info["total_children_act_inact"] = group["total_children"].strip()
                control_info["num_children_max"] = int(group["num_children_max"])
                continue

            # presize_hint: 0
            m = p9.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["presize_hint"] = int(group["presize_hint"])
                continue

            # sw_flags: 0x0802002a, sw_state: 0x00000801
            m = p10.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["sw_flags"] = group["sw_flags"]
                control_info["sw_state"] = group["sw_state"]
                continue

            # orig_min  : 0                   ,      min: 0
            m = p11.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["orig_min"] = int(group["orig_min"])
                control_info["min"] = int(group["min"])
                continue

            # min_qos   : 0                   , min_dflt: 1050000000
            m = p12.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["min_qos"] = int(group["min_qos"])
                control_info["min_dflt"] = int(group["min_dflt"])
                continue

            # orig_max  : 0                   ,      max: 1050000000
            m = p13.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["orig_max"] = int(group["orig_max"])
                control_info["max"] = int(group["max"])
                continue

            # max_qos   : 0                   , max_dflt: 1050000000
            m = p14.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["max_qos"] = int(group["max_qos"])
                control_info["max_dflt"] = int(group["max_dflt"])
                continue

            # share     : 105
            m = p15.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["share"] = int(group["share"])
                continue

            # plevel: 0, service_fragment: False, port_uidb: 65530
            m = p16.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["plevel"] = int(group["plevel"])
                control_info["service_fragment"] = group["service_fragment"]
                control_info["port_uidb"] = int(group["port_uidb"])
                continue

            # priority: 0, defer_obj_refcnt: 0
            m = p17.match(line)
            if m and current_interface and current_index:
                group = m.groupdict()
                control_info = ret_dict[current_interface]["schedule_specifics"]["index"][current_index]["parq_software_control_info"]
                control_info["priority"] = int(group["priority"])
                control_info["defer_obj_refcnt"] = int(group["defer_obj_refcnt"])
                continue

        return ret_dict


class ShowPlatformHardwareQfpActiveFeatureEssSessionSchema(MetaParser):
    """Schema for show platform hardware qfp active feature ess session"""
    schema = {
        'current_number_sessions': int,
        'current_number_tc_flow': int,
        'feature_type_legend': str,
        Optional('sessions'): {
            int: {
                'type': str,
                'segment1': str,
                'seg_type1': str,
                'segment2': str,
                'seg_type2': str,
                'feature': str,
                'other': str,
            }
        }
    }

class ShowPlatformHardwareQfpActiveFeatureEssSession(ShowPlatformHardwareQfpActiveFeatureEssSessionSchema):
    """Parser for show platform hardware qfp active feature ess session"""

    cli_command = 'show platform hardware qfp active feature ess session'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Current number sessions: 1
        p1 = re.compile(r'^Current number sessions: (?P<sessions>\d+)$')

        # Current number TC flow: 0
        p2 = re.compile(r'^Current number TC flow: (?P<tc_flow>\d+)$')

        # Feature Type: A=Accounting D=Policing(DRL) F=FFR M=DSCP Marking L=L4redirect P=Portbundle T=TC
        p3 = re.compile(r'^Feature Type: (?P<legend>.+)$')

        # Session data line
        #   4325392     PPP 0x0042001000001008    ETHER 0x0042001000002009   L2TPV3 -------
        p4 = re.compile(r'^\s*(?P<session>\d+)\s+(?P<type>\S+)\s+(?P<segment1>\S+)\s+(?P<seg_type1>\S+)\s+(?P<segment2>\S+)\s+(?P<seg_type2>\S+)\s+(?P<feature>\S+)\s*(?P<other>\S*)$')

        # Iterate over each line of the output
        for line in output.splitlines():
            line = line.strip()

            # Current number sessions: 1
            m = p1.match(line)
            if m:
                parsed_dict['current_number_sessions'] = int(m.groupdict()['sessions'])
                continue

            # Current number TC flow: 0
            m = p2.match(line)
            if m:
                parsed_dict['current_number_tc_flow'] = int(m.groupdict()['tc_flow'])
                continue

            # Feature Type: A=Accounting D=Policing(DRL) F=FFR M=DSCP Marking L=L4redirect P=Portbundle T=TC
            m = p3.match(line)
            if m:
                parsed_dict['feature_type_legend'] = m.groupdict()['legend']
                continue

            # Session data line
            #   4325392     PPP 0x0042001000001008    ETHER 0x0042001000002009   L2TPV3 -------
            m = p4.match(line)
            if m:
                group = m.groupdict()
                session_id = int(group['session'])

                # Use setdefault to avoid KeyError
                session_dict = parsed_dict.setdefault('sessions', {}).setdefault(session_id, {})

                # Populate the session dictionary
                session_dict.update({
                    'type': group['type'],
                    'segment1': group['segment1'],
                    'seg_type1': group['seg_type1'],
                    'segment2': group['segment2'],
                    'seg_type2': group['seg_type2'],
                    'feature': group['feature'],
                    'other': group['other'] if group['other'] else '-------',
                })
                continue

        return parsed_dict

class ShowPlatformHardwareQfpActiveFeatureFirewallUcodeZonepairSchema(MetaParser):
    """Schema for show platform hardware qfp active feature firewall ucode zonepair"""
    schema = {
        'zonepair': {
            'zp': str,
            'key': str,
            'flag': str,
            'flag_details': {
                Optional('policy_valid'): str,
                Optional('policy_l7_chk'): str,
                Optional('policy_logging'): str,
                Optional('policy_fw_int'): str,
                Optional('policy_ips'): str,
                Optional('policy_urlf'): str,
            },
            Optional('tcam_region'): str,
            Optional('tcam_cmd'): str,
        }
    }


class ShowPlatformHardwareQfpActiveFeatureFirewallUcodeZonepair(ShowPlatformHardwareQfpActiveFeatureFirewallUcodeZonepairSchema):
    """Parser for show platform hardware qfp active feature firewall ucode zonepair"""

    cli_command =  "show platform hardware qfp active feature firewall ucode zonepair {zone1} {zone2}"

    def cli(self, zone1="1", zone2="1", output=None):
        if output is None:
            cmd = self.cli_command.format(zone1=zone1, zone2=zone2)
            output = self.device.execute(cmd)

        # Initialize the return dictionary
        parsed = {}

        # zp:(1 z1z1) key(1->1)
        p1 = re.compile(r'^zp:\((?P<zp>[\d\s\w]+)\)\s+key\((?P<key>[\d\-\>]+)\)\s*$')

        # flag: 0x3
        p2 = re.compile(r'^flag:\s+(?P<flag>0x[\da-fA-F]+)\s*$')

        # Policy Valid    (0x00000001)
        # Policy L7 CHK   (0x00000002)
        p3 = re.compile(r'^\s*(?P<flag_name>Policy\s+[\w\s]+)\s+\((?P<flag_value>0x[\da-fA-F]+)\)\s*$')

        # tcam region: 0xff7fc30  tcam cmd: 0x25800000
        p4 = re.compile(r'^tcam\s+region:\s+(?P<tcam_region>0x[\da-fA-F]+)\s+tcam\s+cmd:\s+(?P<tcam_cmd>0x[\da-fA-F]+)\s*$')

        # Flag name to schema key mapping
        flag_map = {
            'Policy Valid': 'policy_valid',
            'Policy L7 CHK': 'policy_l7_chk',
            'Policy Logging': 'policy_logging',
            'Policy FW INT': 'policy_fw_int',
            'Policy IPS': 'policy_ips',
            'Policy URLF': 'policy_urlf',
        }

        for line in output.splitlines():
            line = line.strip()

            # zp:(1 z1z1) key(1->1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed.setdefault('zonepair', {})
                parsed['zonepair']['zp'] = group['zp']
                parsed['zonepair']['key'] = group['key']
                continue

            # flag: 0x3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed['zonepair']['flag'] = group['flag']
                parsed['zonepair'].setdefault('flag_details', {})
                continue

            # Policy Valid    (0x00000001)
            # Policy L7 CHK   (0x00000002)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                flag_name = group['flag_name'].strip()
                if flag_name in flag_map:
                    schema_key = flag_map[flag_name]
                    parsed['zonepair']['flag_details'][schema_key] = group['flag_value']
                continue

            # tcam region: 0xff7fc30  tcam cmd: 0x25800000
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parsed['zonepair']['tcam_region'] = group['tcam_region']
                parsed['zonepair']['tcam_cmd'] = group['tcam_cmd']
                continue

        return parsed
 
# ==============================================
# Schema for 'show platform hardware subslot <subslot > module host-if status'
# ==============================================
class ShowPlatformHardwareSubslotModuleHostIfStatusSchema(MetaParser):
    """Schema for show platform hardware subslot <subslot> module host-if status"""

    schema = {
        'npu_global_info': {
            'cp_mac': str,
            'ffp_mac': str,
            'fc_mac': str,
            'module_mac': str,
            'dsp_mac': str,
            'tx_priority': str,
            'cp_vlan_id': str,
            'ffp_lp_vlan_id': str,
            'ffp_hp1_vlan_id': str,
            'ffp_hp2_vlan_id': str,
            'fc_vlan_id': str,
            'max_mtu': int
        }
    }


# ==============================================
# Parser for 'show platform hardware subslot <subslot> module host-if status'
# ==============================================
class ShowPlatformHardwareSubslotModuleHostIfStatus(
    ShowPlatformHardwareSubslotModuleHostIfStatusSchema
):
    """Parser for show platform hardware subslot <subslot> module host-if status"""

    cli_command = [
        "show platform hardware subslot {subslot} module host-if status"
    ]

    def cli(self, subslot=None, output=None):
        """
        Parse the output from show platform hardware subslot <x/x> module host-if status

        Args:
            subslot (str): Subslot identifier (e.g., '0/1')
            output (str): CLI output to parse

        Returns:
            dict: Parsed data structure
        """
        if output is None:
            if subslot is None:
                raise ValueError("subslot argument is required when output is not provided")
            output = self.device.execute(self.cli_command[0].format(subslot=subslot))

        # Initialize return dictionary
        ret_dict = {}

        # NPU global_info:
        p1 = re.compile(r'^NPU global_info:\s*$')

        # CP_MAC:     0x6c.8b.d3.d7.f7.0e
        p2 = re.compile(r'^CP_MAC:\s+(?P<cp_mac>\S+)\s*$')

        # FFP_MAC:    0x6c.8b.d3.d7.f7.0e
        p3 = re.compile(r'^FFP_MAC:\s+(?P<ffp_mac>\S+)\s*$')

        # FC_MAC: 0x6c.8b.d3.d7.f7.0e
        p4 = re.compile(r'^FC_MAC:\s+(?P<fc_mac>\S+)\s*$')

        # Module_MAC: 0xec.1d.8b.fe.34.e2
        p5 = re.compile(r'^Module_MAC:\s+(?P<module_mac>\S+)\s*$')

        # DSP_MAC:    N/A
        p6 = re.compile(r'^DSP_MAC:\s+(?P<dsp_mac>\S+)\s*$')

        # TX PRIORITY:  0x03
        p7 = re.compile(r'^TX PRIORITY:\s+(?P<tx_priority>\S+)\s*$')

        # CP VLAN ID:    0xc9 0x2f
        p8 = re.compile(r'^CP VLAN ID:\s+(?P<cp_vlan_id>.+)\s*$')

        # FFP LP VLAN ID:  0x29 0x2e
        p9 = re.compile(r'^FFP LP VLAN ID:\s+(?P<ffp_lp_vlan_id>.+)\s*$')

        # FFP HP1 VLAN ID: 0x89 0x2e
        p10 = re.compile(r'^FFP HP1 VLAN ID:\s+(?P<ffp_hp1_vlan_id>.+)\s*$')

        # FFP HP2 VLAN ID: 0xa9 0x2e
        p11 = re.compile(r'^FFP HP2 VLAN ID:\s+(?P<ffp_hp2_vlan_id>.+)\s*$')

        # FC VLAN ID: 0xe9 0x2e
        p12 = re.compile(r'^FC VLAN ID:\s+(?P<fc_vlan_id>.+)\s*$')

        # Max MTU 10240
        p13 = re.compile(r'^Max MTU\s+(?P<max_mtu>\d+)\s*$')

        for line in output.splitlines():
            line = line.strip()

            # NPU global_info:
            m = p1.match(line)
            if m:
                npu_info_dict = ret_dict.setdefault('npu_global_info', {})
                continue

            # CP_MAC:     0x6c.8b.d3.d7.f7.0e
            m = p2.match(line)
            if m:
                npu_info_dict['cp_mac'] = m.groupdict()['cp_mac']
                continue

            # FFP_MAC:    0x6c.8b.d3.d7.f7.0e
            m = p3.match(line)
            if m:
                npu_info_dict['ffp_mac'] = m.groupdict()['ffp_mac']
                continue

            # FC_MAC: 0x6c.8b.d3.d7.f7.0e
            m = p4.match(line)
            if m:
                npu_info_dict['fc_mac'] = m.groupdict()['fc_mac']
                continue

            # Module_MAC: 0xec.1d.8b.fe.34.e2
            m = p5.match(line)
            if m:
                npu_info_dict['module_mac'] = m.groupdict()['module_mac']
                continue

            # DSP_MAC:    N/A
            m = p6.match(line)
            if m:
                npu_info_dict['dsp_mac'] = m.groupdict()['dsp_mac']
                continue

            # TX PRIORITY:  0x03
            m = p7.match(line)
            if m:
                npu_info_dict['tx_priority'] = m.groupdict()['tx_priority']
                continue

            # CP VLAN ID:    0xc9 0x2f
            m = p8.match(line)
            if m:
                npu_info_dict['cp_vlan_id'] = m.groupdict()['cp_vlan_id'].strip()
                continue

            # FFP LP VLAN ID:  0x29 0x2e
            m = p9.match(line)
            if m:
                npu_info_dict['ffp_lp_vlan_id'] = m.groupdict()['ffp_lp_vlan_id'].strip()
                continue

            # FFP HP1 VLAN ID: 0x89 0x2e
            m = p10.match(line)
            if m:
                npu_info_dict['ffp_hp1_vlan_id'] = m.groupdict()['ffp_hp1_vlan_id'].strip()
                continue

            # FFP HP2 VLAN ID: 0xa9 0x2e
            m = p11.match(line)
            if m:
                npu_info_dict['ffp_hp2_vlan_id'] = m.groupdict()['ffp_hp2_vlan_id'].strip()
                continue

            # FC VLAN ID: 0xe9 0x2e
            m = p12.match(line)
            if m:
                npu_info_dict['fc_vlan_id'] = m.groupdict()['fc_vlan_id'].strip()
                continue

            # Max MTU 10240
            m = p13.match(line)
            if m:
                npu_info_dict['max_mtu'] = int(m.groupdict()['max_mtu'])
                continue

        return ret_dict
 
# ========================================================================
# Schema for 'show platform hardware subslot {subslot} module interface {interface} statistics'
# ========================================================================
class ShowPlatformHardwareSubslotModuleInterfaceStatisticsSchema(MetaParser):
    """Schema for show platform hardware subslot {subslot} module interface {interface} statistics"""

    schema = {
        "hqf_queue_stats": {
            Any(): {
                "throttles": int,
                "enables": int,
                "throttle_refresh": int,
                "enable_refresh": int,
                "throttled": int,
                "tx_packets": int,
                "tx_bytes": int,
                "tx_total_drops": int,
                "tx_queue_drops": int,
                "rx_packets": int,
                "rx_bytes": int,
                "rx_total_drops": int,
                "rx_queue_drops": int,
                "max_queue_depth": int,
                "queue_overflow": int,
                "queue_depth": int,
            }
        }
    }


# ========================================================================
# Parser for 'show platform hardware subslot {subslot} module interface {interface} statistics'
# ========================================================================
class ShowPlatformHardwareSubslotModuleInterfaceStatistics(
    ShowPlatformHardwareSubslotModuleInterfaceStatisticsSchema
):
    """Parser for show platform hardware subslot {subslot} module interface {interface} statistics"""

    cli_command = "show platform hardware subslot {subslot} module interface {interface} statistics"

    def cli(self, subslot, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(subslot=subslot, interface=interface))

        # Initialize the dictionary to store parsed data
        ret_dict = {}

        # HQF queue stats     LP                    HP1                   HP2
        # Throttles           0                     0                     0
        # Enables             0                     0                     0
        # Throttle refresh    0                     0                     0
        # Enable refresh      42                    42                    42
        # Throttled           0                     0                     0
        # Tx Packets          18753                 0                     69
        # Tx Bytes            1015174               0                     1208
        # Tx Total Drops      0                     0                     0
        # Tx Queue Drops      0                     0                     0
        # Rx Packets          18489                 0                     0
        # Rx Bytes            1405224               0                     0
        # Rx Total Drops      0                     0                     0
        # Rx Queue Drops      0                     0                     0
        # Max Queue Depth     114                   0                     24
        # Queue Overflow      0                     0                     0
        # Queue Depth         0                     0                     0

        # Regex patterns to match the statistics
        p_header = re.compile(r"^HQF queue stats\s+LP\s+HP1\s+HP2\s*$")
        p_stats = re.compile(r"^(?P<stat_name>[\w\s]+)\s+(?P<lp>\d+)\s+(?P<hp1>\d+)\s+(?P<hp2>\d+)\s*$")

        found_header = False
        
        for line in output.splitlines():
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue

            # Match header line
            if p_header.match(line):
                found_header = True
                continue

            # Match statistics lines
            if found_header:
                m = p_stats.match(line)
                if m:
                    group = m.groupdict()
                    stat_name = group["stat_name"].strip().lower().replace(" ", "_")
                    lp_val = int(group["lp"])
                    hp1_val = int(group["hp1"])
                    hp2_val = int(group["hp2"])

                    # Initialize the HQF queue stats structure if not present
                    if "hqf_queue_stats" not in ret_dict:
                        ret_dict["hqf_queue_stats"] = {
                            "lp": {},
                            "hp1": {},
                            "hp2": {}
                        }

                    # Store the values in the appropriate queue sections
                    ret_dict["hqf_queue_stats"]["lp"][stat_name] = lp_val
                    ret_dict["hqf_queue_stats"]["hp1"][stat_name] = hp1_val
                    ret_dict["hqf_queue_stats"]["hp2"][stat_name] = hp2_val

        return ret_dict

class ShowPlatformHardwareQfpActiveFeatureNatDatapathPoolSchema(MetaParser):
    """Schema for show platform hardware qfp active feature nat datapath pool"""
    schema = {
        'pool_info': {
            'pool_id': int,
            'type': int,
            'addroute': int,
            'mask': str,
            'allocated': int,
            'misses': int,
            'rotary_idx': str,
            'ahash_sz': int,
            'size': int,
            'max_pat_hash_size': int,
            'next': str,
            'hash_index': str,
            'hilo_ports': str,
            'pool_mem': str,
            'flags': str,
            'pool_name': str,
            'pat_wl': int,
            'no_ports_wl': int,
            'num_maps': int,
            'num_overload_maps': int,
            'vrf': str,
            'port_used': {
                'tcp': int,
                'udp': int
            }
        },
        'conf_block_info': {
            Any(): {
                'start': str,
                'end': str,
                'flags': str,
                'next': str,
                'prev': str
            }
        },
        'alloced_addr_info': {
            'addr': str,
            'secondary_addr': str,
            'refcnt': int,
            'flags': str,
            'vrfid': int,
            'next': str,
            'pat_index': int
        }
    }

class ShowPlatformHardwareQfpActiveFeatureNatDatapathPool(ShowPlatformHardwareQfpActiveFeatureNatDatapathPoolSchema):
    """Parser for show platform hardware qfp active feature nat datapath pool"""
    cli_command = 'show platform hardware qfp active feature nat datapath pool'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Regex patterns
        # pool_id 4 type 1 addroute 0 mask 0xffffff00 allocated 1 misses 0 rotary idx 0x0 ahash sz 4 size 1  max_pat_hash_size 1 next 0x0 hash_index 0x78, hilo ports 0x0  pool mem 0xb93fcd0 flags 0x0 pool_name: xyz pat_wl 0 no_ports_wl 0 num_maps 1 num_overload_maps 1 vrf 0x0 port_used tcp 0 udp 0
        p1 = re.compile(r'^pool_id +(?P<pool_id>\d+) +type +(?P<type>\d+) +addroute +(?P<addroute>\d+) +'
                        r'mask +(?P<mask>[\w]+) +allocated +(?P<allocated>\d+) +misses +(?P<misses>\d+) +'
                        r'rotary idx +(?P<rotary_idx>[\w]+) +ahash sz +(?P<ahash_sz>\d+) +size +(?P<size>\d+) +'
                        r'max_pat_hash_size +(?P<max_pat_hash_size>\d+) +next +(?P<next>[\w]+) +'
                        r'hash_index +(?P<hash_index>[\w]+), +hilo ports +(?P<hilo_ports>[\w]+) +'
                        r'pool mem +(?P<pool_mem>[\w]+) +flags +(?P<flags>[\w]+) +pool_name: +(?P<pool_name>[\w]+) +'
                        r'pat_wl +(?P<pat_wl>\d+) +no_ports_wl +(?P<no_ports_wl>\d+) +num_maps +(?P<num_maps>\d+) +'
                        r'num_overload_maps +(?P<num_overload_maps>\d+) +vrf +(?P<vrf>[\w]+) +'
                        r'port_used +tcp +(?P<tcp>\d+) +udp +(?P<udp>\d+)$')

        # Conf block info
        # TCP PAT block info
        # UDP PAT block info
        # ICMP PAT block info
        # GRE PAT block info
        p2 = re.compile(r'^(?P<block_type>Conf|TCP PAT|UDP PAT|ICMP PAT|GRE PAT) block info$')

        # start 42.0.0.3 end 42.0.0.3 flags 0x1 next 0x0 prev 0x0
        p3 = re.compile(r'^start +(?P<start>[\d\.]+) +end +(?P<end>[\d\.]+) +flags +(?P<flags>[\w]+) +next +(?P<next>[\w]+) +prev +(?P<prev>[\w]+)$')

        # Alloced addr info
        # addr 42.0.0.3 0.0.0.0 refcnt 4 flags 0x1 vrfid 0 next 0x0 pat_index 0
        p4 = re.compile(r'^addr +(?P<addr>[\d\.]+) +(?P<secondary_addr>[\d\.]+) +refcnt +(?P<refcnt>\d+) +flags +(?P<flags>[\w]+) +vrfid +(?P<vrfid>\d+) +next +(?P<next>[\w]+) +pat_index +(?P<pat_index>\d+)$')

        block_type = None

        for line in output.splitlines():
            line = line.strip()

            # Match pool information
            # pool_id 4 type 1 addroute 0 mask 0xffffff00 allocated 1 misses 0 rotary idx 0x0 ahash sz 4 size 1  max_pat_hash_size 1 next 0x0 hash_index 0x78, hilo ports 0x0  pool mem 0xb93fcd0 flags 0x0 pool_name: xyz pat_wl 0 no_ports_wl 0 num_maps 1 num_overload_maps 1 vrf 0x0 port_used tcp 0 udp 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                pool_info = ret_dict.setdefault('pool_info', {})

                # Integer fields - values that should be converted to integers
                integer_fields = [
                    'pool_id', 'type', 'addroute', 'allocated', 'misses', 'ahash_sz', 
                    'size', 'max_pat_hash_size', 'pat_wl', 'no_ports_wl', 'num_maps', 
                    'num_overload_maps', 'tcp', 'udp'
                ]

                # String fields - values that should remain as strings
                string_fields = [
                    'mask', 'rotary_idx', 'hash_index', 'hilo_ports', 'pool_mem', 
                    'flags', 'pool_name', 'vrf', 'next'
                ]

                # Add integer fields to pool_info
                for field in integer_fields:
                    if field in group and field not in ['tcp', 'udp']:  # tcp/udp handled separately
                        pool_info[field] = int(group[field])

                # Add string fields to pool_info
                for field in string_fields:
                    if field in group:
                        pool_info[field] = group[field]

                # Add tcp and udp as part of port_used structure
                pool_info['port_used'] = {
                    'tcp': int(group['tcp']),
                    'udp': int(group['udp'])
                }
                continue

            # Conf block info
            # TCP PAT block info
            # UDP PAT block info
            # ICMP PAT block info
            # GRE PAT block info
            m = p2.match(line)
            if m:
                block_type = m.group('block_type').lower().replace(' ', '_')  # Normalize block type
                ret_dict.setdefault('conf_block_info', {}).setdefault(block_type, {})
                continue

            # Match block details
            # start 42.0.0.3 end 42.0.0.3 flags 0x1 next 0x0 prev 0x0
            m = p3.match(line)
            if m and block_type:
                group = m.groupdict()
                ret_dict['conf_block_info'][block_type].update({k: v for k, v in group.items()})
                continue

            # Match allocated address info
            # Alloced addr info
            # addr 42.0.0.3 0.0.0.0 refcnt 4 flags 0x1 vrfid 0 next 0x0 pat_index 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                alloced_addr_info = ret_dict.setdefault('alloced_addr_info', {})

                # Integer fields that should be converted to integers
                integer_fields = ['refcnt', 'vrfid', 'pat_index']

                # String fields that should remain as strings
                string_fields = ['addr', 'secondary_addr', 'flags', 'next']

                # Add integer fields to alloced_addr_info
                for field in integer_fields:
                    if field in group:
                        alloced_addr_info[field] = int(group[field])

                # Add string fields to alloced_addr_info
                for field in string_fields:
                    if field in group:
                        alloced_addr_info[field] = group[field]

                continue

        return ret_dict

class ShowPlatformHardwareQfpNatDatapathSessDumpSchema(MetaParser):
    """Schema for show platform hardware qfp active feature nat datapath sess-dump"""
    schema = {
        'sessions': {
            str: {  # Session ID
                'io': str,
                'oo': str,
                'io_port': str,
                'oo_port': str,
                'it': str,
                'ot': str,
                'it_port': str,
                'ot_port': str,
                'protocol': int,
                'vrf': int,
                'tableid': int,
                'bck': str,
                'in_if': int,
                'out_if': int,
                'ref': int,
                'flags': str,
                'ext_flags': str,
                'in_pkts': int,
                'in_bytes': str,
                'out_pkts': int,
                'out_bytes': int,
                'flowdb_in2out_fh': str,
                'flowdb_out2in_fh': str,
                'rg': int,
            }
        }
    }

class ShowPlatformHardwareQfpNatDatapathSessDump(ShowPlatformHardwareQfpNatDatapathSessDumpSchema):
    """Parser for show platform hardware qfp active feature nat datapath sess-dump"""

    cli_command = 'show platform hardware qfp active feature nat datapath sess-dump'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expression for parsing the lines
        #id 0xa6a21d0 io 62.0.0.3 oo 180.100.1.191 io 24632 oo 24634 it 42.0.0.3 ot 180.100.1.191 it 24632 ot 24634 pro 17 vrf 0 tableid 0 bck 195 in_if 0 out_if 0 ref 1 flags 0x0 ext_flags 0x0 in_pkts 100 in_bytes 10800 out_pkts 0 out_bytes 0 flowdb in2out fh 0x0 flowdb out2in fh 0x0 rg 0
        p1 = re.compile(
            r'^id\s+(?P<id>\S+) '
            r'io\s+(?P<io>\S+) '
            r'oo\s+(?P<oo>\S+) '
            r'io\s+(?P<io_port>\S+) '
            r'oo\s+(?P<oo_port>\S+) '
            r'it\s+(?P<it>\S+) '
            r'ot\s+(?P<ot>\S+) '
            r'it\s+(?P<it_port>\S+) '
            r'ot\s+(?P<ot_port>\S+) '
            r'pro\s+(?P<protocol>\d+) '
            r'vrf\s+(?P<vrf>\d+) '
            r'tableid\s+(?P<tableid>\d+) '
            r'bck\s+(?P<bck>\S+) '
            r'in_if\s+(?P<in_if>\d+) '
            r'out_if\s+(?P<out_if>\d+) '
            r'ref\s+(?P<ref>\d+) '
            r'flags\s+(?P<flags>\S+) '
            r'ext_flags\s+(?P<ext_flags>\S+) '
            r'in_pkts\s+(?P<in_pkts>\d+) '
            r'in_bytes\s+(?P<in_bytes>\S+) '
            r'out_pkts\s+(?P<out_pkts>\d+) '
            r'out_bytes\s+(?P<out_bytes>\d+) '
            r'flowdb in2out fh\s+(?P<flowdb_in2out_fh>\S+) '
            r'flowdb out2in fh\s+(?P<flowdb_out2in_fh>\S+) '
            r'rg\s+(?P<rg>\d+)'
        )

        # Parse each line of the output
        for line in output.splitlines():
            line = line.strip()

            # Match the regular expression
            # id 0xa6a21d0 io 62.0.0.3 oo 180.100.1.191 io 24632 oo 24634 it 42.0.0.3 ot 180.100.1.191 it 24632 ot 24634 pro 17 vrf 0 tableid 0 bck 195 in_if 0 out_if 0 ref 1 flags 0x0 ext_flags 0x0 in_pkts 100 in_bytes 10800 out_pkts 0 out_bytes 0 flowdb in2out fh 0x0 flowdb out2in fh 0x0 rg 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                session_id = groups['id']
                session_dict = parsed_dict.setdefault('sessions', {}).setdefault(session_id, {})
                session_dict['io'] = groups['io']
                session_dict['oo'] = groups['oo']
                session_dict['io_port'] = groups['io_port']
                session_dict['oo_port'] = groups['oo_port']
                session_dict['it'] = groups['it']
                session_dict['ot'] = groups['ot']
                session_dict['it_port'] = groups['it_port']
                session_dict['ot_port'] = groups['ot_port']
                session_dict['protocol'] = int(groups['protocol'])
                session_dict['vrf'] = int(groups['vrf'])
                session_dict['tableid'] = int(groups['tableid'])
                session_dict['bck'] = groups['bck']
                session_dict['in_if'] = int(groups['in_if'])
                session_dict['out_if'] = int(groups['out_if'])
                session_dict['ref'] = int(groups['ref'])
                session_dict['flags'] = groups['flags']
                session_dict['ext_flags'] = groups['ext_flags']
                session_dict['in_pkts'] = int(groups['in_pkts'])
                session_dict['in_bytes'] = groups['in_bytes']
                session_dict['out_pkts'] = int(groups['out_pkts'])
                session_dict['out_bytes'] = int(groups['out_bytes'])
                session_dict['flowdb_in2out_fh'] = groups['flowdb_in2out_fh']
                session_dict['flowdb_out2in_fh'] = groups['flowdb_out2in_fh']
                session_dict['rg'] = int(groups['rg'])

        return parsed_dict
      
# ================================================================
# Schema for 'show platform hardware qfp active feature nat datapath time'
# ================================================================
class ShowPlatformHardwareQfpActiveFeatureNatDatapathTimeSchema(MetaParser):
    """Schema for show platform hardware qfp active feature nat datapath time"""
    schema = {
        "timeouts": {
            "default": int,
            "tcp": int,
            "tcp_pptp": int,
            "udp": int,
            "finrst": int,
            "syn": int,
            "dns": int,
            "icmp": int,
            "skinny": int,
            "icmp_error": int,
            "esp": int,
            "rmap_entry": int,
            "nonpat_bind": int,
        },
        "sage_bck": int,
        "bage_bck": int,
        "sysup": int,
        "dtl_pend": int,
        "sage": int,
        "sage_last": int,
        "sage_restarted": int,
        "sage_proc": int,
        "sage_not_proc": int,
        "health_age": int,
    }

# ================================================================
# Parser for 'show platform hardware qfp active feature nat datapath time'
# ================================================================
class ShowPlatformHardwareQfpActiveFeatureNatDatapathTime(ShowPlatformHardwareQfpActiveFeatureNatDatapathTimeSchema):
    cli_command = "show platform hardware qfp active feature nat datapath time"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # Timeouts: default 86400; TCP 86400; TCP PPTP 86400; UDP 300; FINRST 60; SYN 60; DNS 60; ICMP 60; Skinny 60; ICMP error 60; ESP 300; rmap entry 3600; nonpat bind 1200
        p1 = re.compile(
            r"Timeouts: default (?P<default>\d+); TCP (?P<tcp>\d+); TCP PPTP (?P<tcp_pptp>\d+); UDP (?P<udp>\d+); FINRST (?P<finrst>\d+); SYN (?P<syn>\d+); DNS (?P<dns>\d+); ICMP (?P<icmp>\d+); Skinny (?P<skinny>\d+); ICMP error (?P<icmp_error>\d+); ESP (?P<esp>\d+); rmap entry (?P<rmap_entry>\d+); nonpat bind (?P<nonpat_bind>\d+)"
        )

        # sage_bck 6060560 bage_bck 168336 sysup 795244
        p2 = re.compile(r"sage_bck (?P<sage_bck>\d+) bage_bck (?P<bage_bck>\d+) sysup (?P<sysup>\d+)")

        # dtl_pend 0 sage 378832 sage_last 300011 sage_restarted: 0
        p3 = re.compile(r"dtl_pend (?P<dtl_pend>\d+) sage (?P<sage>\d+) sage_last (?P<sage_last>\d+) sage_restarted: (?P<sage_restarted>\d+)")

        # sage_proc: 378785 sage_not_proc: 47 health_age: 1
        p4 = re.compile(r"sage_proc: (?P<sage_proc>\d+) sage_not_proc: (?P<sage_not_proc>\d+) health_age: (?P<health_age>\d+)")

        for line in output.splitlines():
            line = line.strip()

            # Timeouts: default 86400; TCP 86400; TCP PPTP 86400; UDP 300; FINRST 60; SYN 60; DNS 60; ICMP 60; Skinny 60; ICMP error 60; ESP 300; rmap entry 3600; nonpat bind 1200
            m = p1.match(line)
            if m:
                parsed_dict["timeouts"] = {k: int(v) for k, v in m.groupdict().items()}
                continue

            # sage_bck 6060560 bage_bck 168336 sysup 795244
            m = p2.match(line)
            if m:
                parsed_dict.update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # dtl_pend 0 sage 378832 sage_last 300011 sage_restarted: 0
            m = p3.match(line)
            if m:
                parsed_dict.update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # sage_proc: 378785 sage_not_proc: 47 health_age: 1
            m = p4.match(line)
            if m:
                parsed_dict.update({k: int(v) for k, v in m.groupdict().items()})
                continue

        return parsed_dict


# ============================================================================================================
# Schema for 'show platform hardware qfp <instance> feature firewall ucode scb a a a a a a a detail'
# ============================================================================================================

class ShowPlatformHardwareQfpActiveFeatureFirewallUcodeScbDetailSchema(MetaParser):
    """Schema for show platform hardware qfp <instance> feature firewall ucode scb a a a a a a a detail"""
    
    schema = {
        'sessions': {
            Any(): {
                'session_id': str,
                'src_ip': str,
                'src_port': int,
                'dst_ip': str,
                'dst_port': int,
                'protocol': int,
                'vrf_pair': str,
                'protocol_name': str,
                'flags': str,
                'timing_info': int,
                'pscb': str,
                'key1_flags': str,
                'bucket': int,
                'prev': str,
                'next': str,
                'fw_flags': ListOf(str),
                Optional('vrf_flags'): ListOf(str),
                'protocol_state': ListOf(str),
                'icmp_error_count': int,
                'ureachable_arrived': str,
                'scb_state': str,
                'nxt_timeout': int,
                'refcnt': int,
                'ha_nak_cnt': int,
                'rg': int,
                'hostdb': str,
                'l7': str,
                'stats': str,
                'child': str,
                'isn_in': str,
                'last_ack_in': str,
                'next_seq_in': str,
                'wnd_size_in': int,
                'wnd_scale_in': int,
                'isn_out': str,
                'last_ack_out': str,
                'next_ack_out': str,
                'wnd_size_out': int,
                'wnd_scale_out': int,
                'tcp_flags': str,
                Optional('tcp_flag_desc'): str,
                'proto_num': str,
                'l7_ooo_drop': str,
                'root_scb': str,
                'act_blk': str,
                'ingress_intf': str,
                'ingress_intf_id': int,
                'egress_intf': str,
                'egress_intf_id': int,
                'current_time': int,
                'create_tstamp': int,
                'last_access': int,
                'nat_out_local_addr': str,
                'nat_out_local_port': int,
                'nat_in_global_addr': str,
                'nat_in_global_port': int,
                'syncookie_fixup': str,
                'halfopen_linkage': ListOf(str),
                'cxsc_cft_fid': str,
                'tw_timer': ListOf(str),
                'packets_per_session': int,
                Optional('timer_info'): {
                    Optional('bucket'): int,
                    Optional('flags'): str,
                    Optional('func'): int,
                    Optional('idx'): int,
                    Optional('wheel'): str,
                    'timer_status': str,
                    'num_buckets': int,
                    'cur': int,
                    'mask': str,
                    'gran': int,
                    'flag': str,
                    'ticks': int,
                },
                'sgt': int,
                'dgt': int,
                'nat_handles': ListOf(str),
                'flowdb_in2out': str,
                'flowdb_in2out_alloc_epoch': int,
                'flowdb_out2in': str,
                'flowdb_out2in_alloc_epoch': int,
                'ppe_tid': int,
                'icmp_err_time': int,
                'utd_context_id': int,
                'avc_class_stats': str,
                'vpn_id_src': int,
                'vpn_id_dst': int,
            }
        }
    }

# ============================================================================================================
# Parser for 'show platform hardware qfp <instance> feature firewall ucode scb a a a a a a a detail'
# ============================================================================================================

class ShowPlatformHardwareQfpActiveFeatureFirewallUcodeScbDetail(ShowPlatformHardwareQfpActiveFeatureFirewallUcodeScbDetailSchema):
    """Parser for show platform hardware qfp <instance> feature firewall ucode scb a a a a a a a detail"""

    cli_command = 'show platform hardware qfp {instance} feature firewall ucode scb a a a a a a a detail'

    def cli(self, instance='active', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(instance=instance))

        parsed_dict = {}

        # Session ID:0x00C31BAA 2002::1 46583 4002::1 80 proto 6 (2:2) (0x1:tcp)	[sd] 1879179108
        p1 = re.compile(r'^Session ID:(?P<session_id>0x[0-9a-fA-F]+)\s+(?P<src_ip>[^\s]+)\s+(?P<src_port>\d+)\s+(?P<dst_ip>[^\s]+)\s+(?P<dst_port>\d+)\s+proto\s+(?P<protocol>\d+)\s+\((?P<vrf_pair>[^)]+)\)\s+\((?P<protocol_hex>0x[0-9a-fA-F]+):(?P<protocol_name>[^)]+)\)\s+\[(?P<flags>[^\]]+)\]\s+(?P<timing_info>\d+)$')

        # pscb : 0x8025a40,  key1_flags: 0x00000030
        p2 = re.compile(r'^\s*pscb\s*:\s*(?P<pscb>0x[0-9a-fA-F]+),\s*key1_flags:\s*(?P<key1_flags>0x[0-9a-fA-F]+)$')

        # bucket : 2382, prev 0x0, next 0x0
        p3 = re.compile(r'^\s*bucket\s*:\s*(?P<bucket>\d+),\s*prev\s+(?P<prev>0x[0-9a-fA-F]+),\s*next\s+(?P<next>0x[0-9a-fA-F]+)$')

        # fw_flags: 0x00000004 0x24401821,
        p4 = re.compile(r'^\s*fw_flags:\s*(?P<fw_flags>(?:0x[0-9a-fA-F]+\s*)+),$')

        # VRF1-rsrc-limit
        p5 = re.compile(r'^\s*(?P<vrf_flags>VRF\d+[-\w]*(?:\s+[-\w]+)*)$')

        # Root Protocol-TCP Alert Proto-State:SYN-sent Session-db Half-open Max-session
        p6 = re.compile(r'^\s*(?P<protocol_state>Root\s+Protocol-[^\s]+(?:\s+[^\s]+)*)$')

        # icmp_error count 0 ureachable arrived: no
        p7 = re.compile(r'^\s*icmp_error\s+count\s+(?P<icmp_error_count>\d+)\s+ureachable\s+arrived:\s+(?P<ureachable_arrived>yes|no)$')

        # scb state: open, nxt_timeout: 3000, refcnt: 1
        p8 = re.compile(r'^\s*scb\s+state:\s+(?P<scb_state>\w+),\s*nxt_timeout:\s+(?P<nxt_timeout>\d+),\s*refcnt:\s+(?P<refcnt>\d+)$')

        # ha nak cnt: 0,  rg: 0
        p9 = re.compile(r'^\s*ha\s+nak\s+cnt:\s+(?P<ha_nak_cnt>\d+),\s*rg:\s+(?P<rg>\d+)$')

        # hostdb: 0x303c9230, L7: 0x0, stats: 0x2aecf240, child: 0x0
        p10 = re.compile(r'^\s*hostdb:\s+(?P<hostdb>0x[0-9a-fA-F]+),\s*L7:\s+(?P<l7>0x[0-9a-fA-F]+),\s*stats:\s+(?P<stats>0x[0-9a-fA-F]+),\s*child:\s+(?P<child>0x[0-9a-fA-F]+)$')

        # isn:         00000000 last ack:        00000000 next seq:          00000001 wnd_size:          1879741492
        p11 = re.compile(r'^\s*isn:\s+(?P<isn>[0-9a-fA-F]+)\s+last\s+ack:\s+(?P<last_ack>[0-9a-fA-F]+)\s+next\s+seq:\s+(?P<next_seq>[0-9a-fA-F]+)\s+wnd_size:\s+(?P<wnd_size>\d+)$')

        # wnd_scale:         0
        p12 = re.compile(r'^\s*wnd_scale:\s+(?P<wnd_scale>\d+)$')

        # isn:         00000000    last ack:        00000000    next ack:        00000000 wnd_size:          1879741492
        p13 = re.compile(r'^\s*isn:\s+(?P<isn>[0-9a-fA-F]+)\s+last\s+ack:\s+(?P<last_ack>[0-9a-fA-F]+)\s+next\s+ack:\s+(?P<next_ack>[0-9a-fA-F]+)\s+wnd_size:\s+(?P<wnd_size>\d+)$')

        # tcp flags:     0x00000000 :  : proto: 0001: l7 ooo drop 0x010
        p14 = re.compile(r'^\s*tcp\s+flags:\s+(?P<tcp_flags>0x[0-9a-fA-F]+)\s+:\s*(?P<tcp_flag_desc>[^:]*):\s*proto:\s+(?P<proto>\d+):\s+l7\s+ooo\s+drop\s+(?P<l7_ooo_drop>0x[0-9a-fA-F]+)$')

        # root scb: 0x0 act_blk: 0x2aec7200
        p15 = re.compile(r'^\s*root\s+scb:\s+(?P<root_scb>0x[0-9a-fA-F]+)\s+act_blk:\s+(?P<act_blk>0x[0-9a-fA-F]+)$')

        # ingress/egress intf: GigabitEthernet0/1/1 (1014), vasileft1 (65514)
        p16 = re.compile(r'^\s*ingress/egress\s+intf:\s+(?P<ingress_intf>[^\s\(]+)\s+\((?P<ingress_intf_id>\d+)\),\s+(?P<egress_intf>[^\s\(]+)\s+\((?P<egress_intf_id>\d+)\)$')

        # current time 258769226801 create tstamp: 258572084136 last access: 258572084136
        p17 = re.compile(r'^\s*current\s+time\s+(?P<current_time>\d+)\s+create\s+tstamp:\s+(?P<create_tstamp>\d+)\s+last\s+access:\s+(?P<last_access>\d+)$')

        # nat_out_local_addr:port: 0.0.0.0:0
        p18 = re.compile(r'^\s*nat_out_local_addr:port:\s+(?P<addr>[\d\.]+):(?P<port>\d+)$')

        # nat_in_global_addr:port: 0.0.0.0:0
        p19 = re.compile(r'^\s*nat_in_global_addr:port:\s+(?P<addr>[\d\.]+):(?P<port>\d+)$')

        # syncookie fixup: 0x0,  halfopen linkage: 0x2f025978 0x2f025c38
        p20 = re.compile(r'^\s*syncookie\s+fixup:\s+(?P<syncookie_fixup>0x[0-9a-fA-F]+),\s*halfopen\s+linkage:\s+(?P<halfopen_linkage>(?:0x[0-9a-fA-F]+\s*)+)$')

        # cxsc_cft_fid: 0x00000000
        p21 = re.compile(r'^\s*cxsc_cft_fid:\s+(?P<cxsc_cft_fid>0x[0-9a-fA-F]+)$')

        # tw timer: 0x00000000 0x00000000 0x00000000 0x01d43129
        p22 = re.compile(r'^\s*tw\s+timer:\s+(?P<tw_timer>(?:0x[0-9a-fA-F]+\s*)+)$')

        # Packets/session: 25     SGT: 0 DGT: 0, NAT handles 0x00000000 0x00000000
        p23 = re.compile(r'^\s*Packets/session:\s+(?P<packets_per_session>\d+)\s+SGT:\s+(?P<sgt>\d+)\s+DGT:\s+(?P<dgt>\d+),\s+NAT\s+handles\s+(?P<nat_handles>(?:0x[0-9a-fA-F]+\s*)+)$')

        # Packets/session: 25 (standalone)
        p23a = re.compile(r'^\s*Packets/session:\s+(?P<packets_per_session>\d+)\s*$')

        # bucket 7521 flags 0x00000001 func 1 idx 6 wheel 0x30999940
        p24 = re.compile(r'^\s*bucket\s+(?P<bucket>\d+)\s+flags\s+(?P<flags>0x[0-9a-fA-F]+)\s+func\s+(?P<func>\d+)\s+idx\s+(?P<idx>\d+)\s+wheel\s+(?P<wheel>0x[0-9a-fA-F]+)$')

        # Timer within range
        p25 = re.compile(r'^\s*(?P<timer_status>Timer\s+within\s+range)$')

        # num buckets 131072 cur 4574 mask 0x1ffff gran 160 flag 0x0 ticks 0
        p26 = re.compile(r'^\s*num\s+buckets\s+(?P<num_buckets>\d+)\s+cur\s+(?P<cur>\d+)\s+mask\s+(?P<mask>0x[0-9a-fA-F]+)\s+gran\s+(?P<gran>\d+)\s+flag\s+(?P<flag>0x[0-9a-fA-F]+)\s+ticks\s+(?P<ticks>\d+)$')

        # SGT: 0 DGT: 0, NAT handles 0x00000000 0x00000000
        p27 = re.compile(r'^\s*SGT:\s+(?P<sgt>\d+)\s+DGT:\s+(?P<dgt>\d+),\s+NAT\s+handles\s+(?P<nat_handles>(?:0x[0-9a-fA-F]+\s*)+)$')

        # FlowDB in2out 0x00000000 alloc_epoch 0 out2in 0x00000000 alloc_epoch 0 ppe tid 0
        p28 = re.compile(r'^\s*FlowDB\s+in2out\s+(?P<flowdb_in2out>0x[0-9a-fA-F]+)\s+alloc_epoch\s+(?P<flowdb_in2out_alloc_epoch>\d+)\s+out2in\s+(?P<flowdb_out2in>0x[0-9a-fA-F]+)\s+alloc_epoch\s+(?P<flowdb_out2in_alloc_epoch>\d+)\s+ppe\s+tid\s+(?P<ppe_tid>\d+)$')

        # icmp_err_time 0 utd_context_id 0, avc class stats 0x0, VPN id src 65535, dst 65535
        p29 = re.compile(r'^\s*icmp_err_time\s+(?P<icmp_err_time>\d+)\s+utd_context_id\s+(?P<utd_context_id>\d+),\s+avc\s+class\s+stats\s+(?P<avc_class_stats>0x[0-9a-fA-F]+),\s+VPN\s+id\s+src\s+(?P<vpn_id_src>\d+),\s+dst\s+(?P<vpn_id_dst>\d+)$')

        current_session = None
        current_session_dict = None
        in_wnd_processing = False
        wnd_direction = None

        for line in output.splitlines():
            line = line.strip()
            if not line or line.startswith('[s=session'):
                continue

            # Session ID:0x00C31BAA 2002::1 46583 4002::1 80 proto 6 (2:2) (0x1:tcp)	[sd] 1879179108
            m = p1.match(line)
            if m:
                group = m.groupdict()
                session_id = group['session_id']
                current_session = session_id
                
                sessions_dict = parsed_dict.setdefault('sessions', {})
                current_session_dict = sessions_dict.setdefault(session_id, {})
                
                current_session_dict['session_id'] = session_id
                current_session_dict['src_ip'] = group['src_ip']
                current_session_dict['src_port'] = int(group['src_port'])
                current_session_dict['dst_ip'] = group['dst_ip']
                current_session_dict['dst_port'] = int(group['dst_port'])
                current_session_dict['protocol'] = int(group['protocol'])
                current_session_dict['vrf_pair'] = group['vrf_pair']
                current_session_dict['protocol_name'] = group['protocol_name']
                current_session_dict['flags'] = group['flags']
                current_session_dict['timing_info'] = int(group['timing_info'])
                in_wnd_processing = False
                continue

            if not current_session_dict:
                continue

            # pscb : 0x8025a40,  key1_flags: 0x00000030
            m = p2.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['pscb'] = group['pscb']
                current_session_dict['key1_flags'] = group['key1_flags']
                continue

            # bucket : 2382, prev 0x0, next 0x0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['bucket'] = int(group['bucket'])
                current_session_dict['prev'] = group['prev']
                current_session_dict['next'] = group['next']
                continue

            # fw_flags: 0x00000004 0x24401821,
            m = p4.match(line)
            if m:
                fw_flags = m.group('fw_flags').rstrip(',').split()
                current_session_dict['fw_flags'] = fw_flags
                continue

            # VRF1-rsrc-limit
            m = p5.match(line)
            if m:
                vrf_flags = m.group('vrf_flags').split()
                current_session_dict['vrf_flags'] = vrf_flags
                continue

            # Root Protocol-TCP Alert Proto-State:SYN-sent Session-db Half-open Max-session
            m = p6.match(line)
            if m:
                protocol_state = m.group('protocol_state').split()
                current_session_dict['protocol_state'] = protocol_state
                continue

            # icmp_error count 0 ureachable arrived: no
            m = p7.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['icmp_error_count'] = int(group['icmp_error_count'])
                current_session_dict['ureachable_arrived'] = group['ureachable_arrived']
                continue

            # scb state: open, nxt_timeout: 3000, refcnt: 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['scb_state'] = group['scb_state']
                current_session_dict['nxt_timeout'] = int(group['nxt_timeout'])
                current_session_dict['refcnt'] = int(group['refcnt'])
                continue

            # ha nak cnt: 0,  rg: 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['ha_nak_cnt'] = int(group['ha_nak_cnt'])
                current_session_dict['rg'] = int(group['rg'])
                continue

            # hostdb: 0x303c9230, L7: 0x0, stats: 0x2aecf240, child: 0x0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['hostdb'] = group['hostdb']
                current_session_dict['l7'] = group['l7']
                current_session_dict['stats'] = group['stats']
                current_session_dict['child'] = group['child']
                continue

            # isn:         00000000 last ack:        00000000 next seq:          00000001 wnd_size:          1879741492
            m = p11.match(line)
            if m:
                group = m.groupdict()
                if not in_wnd_processing:
                    # First isn line is for inbound
                    current_session_dict['isn_in'] = group['isn']
                    current_session_dict['last_ack_in'] = group['last_ack']
                    current_session_dict['next_seq_in'] = group['next_seq']
                    current_session_dict['wnd_size_in'] = int(group['wnd_size'])
                    wnd_direction = 'in'
                    in_wnd_processing = True
                continue

            # wnd_scale:         0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                if wnd_direction == 'in':
                    current_session_dict['wnd_scale_in'] = int(group['wnd_scale'])
                elif wnd_direction == 'out':
                    current_session_dict['wnd_scale_out'] = int(group['wnd_scale'])
                continue

            # isn:         00000000    last ack:        00000000    next ack:        00000000 wnd_size:          1879741492
            m = p13.match(line)
            if m:
                group = m.groupdict()
                if in_wnd_processing:
                    # Second isn line is for outbound
                    current_session_dict['isn_out'] = group['isn']
                    current_session_dict['last_ack_out'] = group['last_ack']
                    current_session_dict['next_ack_out'] = group['next_ack']
                    current_session_dict['wnd_size_out'] = int(group['wnd_size'])
                    wnd_direction = 'out'
                continue

            # tcp flags:     0x00000000 :  : proto: 0001: l7 ooo drop 0x010
            m = p14.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['tcp_flags'] = group['tcp_flags']
                # Only add tcp_flag_desc if it has content (not empty string)
                if group['tcp_flag_desc'].strip():
                    current_session_dict['tcp_flag_desc'] = group['tcp_flag_desc']
                current_session_dict['proto_num'] = group['proto']
                current_session_dict['l7_ooo_drop'] = group['l7_ooo_drop']
                continue

            # root scb: 0x0 act_blk: 0x2aec7200
            m = p15.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['root_scb'] = group['root_scb']
                current_session_dict['act_blk'] = group['act_blk']
                continue

            # ingress/egress intf: GigabitEthernet0/1/1 (1014), vasileft1 (65514)
            m = p16.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['ingress_intf'] = group['ingress_intf']
                current_session_dict['ingress_intf_id'] = int(group['ingress_intf_id'])
                current_session_dict['egress_intf'] = group['egress_intf']
                current_session_dict['egress_intf_id'] = int(group['egress_intf_id'])
                continue

            # current time 258769226801 create tstamp: 258572084136 last access: 258572084136
            m = p17.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['current_time'] = int(group['current_time'])
                current_session_dict['create_tstamp'] = int(group['create_tstamp'])
                current_session_dict['last_access'] = int(group['last_access'])
                continue

            # nat_out_local_addr:port: 0.0.0.0:0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['nat_out_local_addr'] = group['addr']
                current_session_dict['nat_out_local_port'] = int(group['port'])
                continue

            # nat_in_global_addr:port: 0.0.0.0:0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['nat_in_global_addr'] = group['addr']
                current_session_dict['nat_in_global_port'] = int(group['port'])
                continue

            # syncookie fixup: 0x0,  halfopen linkage: 0x2f025978 0x2f025c38
            m = p20.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['syncookie_fixup'] = group['syncookie_fixup']
                halfopen_linkage = group['halfopen_linkage'].split()
                current_session_dict['halfopen_linkage'] = halfopen_linkage
                continue

            # cxsc_cft_fid: 0x00000000
            m = p21.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['cxsc_cft_fid'] = group['cxsc_cft_fid']
                continue

            # tw timer: 0x00000000 0x00000000 0x00000000 0x01d43129
            m = p22.match(line)
            if m:
                tw_timer = m.group('tw_timer').split()
                current_session_dict['tw_timer'] = tw_timer
                continue

            # Packets/session: 25     SGT: 0 DGT: 0, NAT handles 0x00000000 0x00000000
            m = p23.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['packets_per_session'] = int(group['packets_per_session'])
                current_session_dict['sgt'] = int(group['sgt'])
                current_session_dict['dgt'] = int(group['dgt'])
                nat_handles = group['nat_handles'].split()
                current_session_dict['nat_handles'] = nat_handles
                continue

            # Packets/session: 25 (standalone)
            m = p23a.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['packets_per_session'] = int(group['packets_per_session'])
                continue

            # bucket 7521 flags 0x00000001 func 1 idx 6 wheel 0x30999940
            m = p24.match(line)
            if m:
                group = m.groupdict()
                timer_info = current_session_dict.setdefault('timer_info', {})
                timer_info['bucket'] = int(group['bucket'])
                timer_info['flags'] = group['flags']
                timer_info['func'] = int(group['func'])
                timer_info['idx'] = int(group['idx'])
                timer_info['wheel'] = group['wheel']
                continue

            # Timer within range
            m = p25.match(line)
            if m:
                timer_info = current_session_dict.setdefault('timer_info', {})
                timer_info['timer_status'] = m.group('timer_status')
                continue

            # num buckets 131072 cur 4574 mask 0x1ffff gran 160 flag 0x0 ticks 0
            m = p26.match(line)
            if m:
                group = m.groupdict()
                timer_info = current_session_dict.setdefault('timer_info', {})
                timer_info['num_buckets'] = int(group['num_buckets'])
                timer_info['cur'] = int(group['cur'])
                timer_info['mask'] = group['mask']
                timer_info['gran'] = int(group['gran'])
                timer_info['flag'] = group['flag']
                timer_info['ticks'] = int(group['ticks'])
                continue

            # SGT: 0 DGT: 0, NAT handles 0x00000000 0x00000000
            m = p27.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['sgt'] = int(group['sgt'])
                current_session_dict['dgt'] = int(group['dgt'])
                nat_handles = group['nat_handles'].split()
                current_session_dict['nat_handles'] = nat_handles
                continue

            # FlowDB in2out 0x00000000 alloc_epoch 0 out2in 0x00000000 alloc_epoch 0 ppe tid 0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['flowdb_in2out'] = group['flowdb_in2out']
                current_session_dict['flowdb_in2out_alloc_epoch'] = int(group['flowdb_in2out_alloc_epoch'])
                current_session_dict['flowdb_out2in'] = group['flowdb_out2in']
                current_session_dict['flowdb_out2in_alloc_epoch'] = int(group['flowdb_out2in_alloc_epoch'])
                current_session_dict['ppe_tid'] = int(group['ppe_tid'])
                continue

            # icmp_err_time 0 utd_context_id 0, avc class stats 0x0, VPN id src 65535, dst 65535
            m = p29.match(line)
            if m:
                group = m.groupdict()
                current_session_dict['icmp_err_time'] = int(group['icmp_err_time'])
                current_session_dict['utd_context_id'] = int(group['utd_context_id'])
                current_session_dict['avc_class_stats'] = group['avc_class_stats']
                current_session_dict['vpn_id_src'] = int(group['vpn_id_src'])
                current_session_dict['vpn_id_dst'] = int(group['vpn_id_dst'])
                continue

        return parsed_dict

# ================================================================
# Schema for 'show platform hardware qfp active infrastructure punt statistics type per-cause clear'
# ================================================================
class ShowPlatformHardwareQfpActiveInfrastructurePuntStatisticsTypePerCauseClearSchema(MetaParser):
    """Schema for show platform hardware qfp active infrastructure punt statistics type per-cause clear"""
    schema = {
        'global_per_cause_statistics': {
            'number_of_punt_causes': int,
            'per_punt_cause_statistics': {
                Any(): {
                    'counter_id': str,
                    'punt_cause_name': str,
                    'packets_received': int,
                    'packets_transmitted': int,
                }
            }
        },
        Optional('per_inject_cause_statistics'): {
            'number_of_inject_causes': int,
            'per_inject_cause_statistics': {
                Any(): {
                    'counter_id': str,
                    'inject_cause_name': str,
                    'packets_received': int,
                    'packets_transmitted': int,
                }
            }
        }
    }

# ================================================================
# Parser for 'show platform hardware qfp active infrastructure punt statistics type per-cause clear'
# ================================================================
class ShowPlatformHardwareQfpActiveInfrastructurePuntStatisticsTypePerCauseClear(ShowPlatformHardwareQfpActiveInfrastructurePuntStatisticsTypePerCauseClearSchema):
    """Parser for show platform hardware qfp active infrastructure punt statistics type per-cause clear"""
    cli_command = 'show platform hardware qfp active infrastructure punt statistics type per-cause clear'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        current_section = None

        # Global Per Cause Statistics
        p1 = re.compile(r'^Global\s+Per\s+Cause\s+Statistics\s*$')

        # Number of punt causes =   165
        p2 = re.compile(r'^Number\s+of\s+punt\s+causes\s*=\s+(?P<punt_causes>\d+)\s*$')

        # Per Punt Cause Statistics
        p3 = re.compile(r'^Per\s+Punt\s+Cause\s+Statistics\s*$')

        # 003         Layer2 control and legacy                 859                   859
        p4 = re.compile(r'^(?P<counter_id>\d+)\s+(?P<punt_cause_name>[^\s].*?)\s{2,}(?P<packets_received>\d+)\s+(?P<packets_transmitted>\d+)\s*$')

        # Number of inject causes = 56
        p5 = re.compile(r'^Number\s+of\s+inject\s+causes\s*=\s+(?P<inject_causes>\d+)\s*$')

        # Per Inject Cause Statistics
        p6 = re.compile(r'^Per\s+Inject\s+Cause\s+Statistics\s*$')

        # 005         QFP <->RP keepalive                       303                   0
        p7 = re.compile(r'^(?P<counter_id>\d+)\s+(?P<inject_cause_name>[^\s].*?)\s{2,}(?P<packets_received>\d+)\s+(?P<packets_transmitted>\d+)\s*$')

        for line in output.splitlines():
            line = line.strip()

            # Skip empty lines and header lines
            if not line or line.startswith('Counter ID') or line.startswith('Packets') or '---' in line:
                continue

            # Global Per Cause Statistics
            m = p1.match(line)
            if m:
                current_section = 'global'
                parsed_dict['global_per_cause_statistics'] = {}
                continue

            # Number of punt causes =   165
            m = p2.match(line)
            if m:
                parsed_dict['global_per_cause_statistics']['number_of_punt_causes'] = int(m.group('punt_causes'))
                continue

            # Per Punt Cause Statistics
            m = p3.match(line)
            if m:
                current_section = 'punt_stats'
                parsed_dict['global_per_cause_statistics']['per_punt_cause_statistics'] = {}
                continue

            # Number of inject causes = 56
            m = p5.match(line)
            if m:
                if 'per_inject_cause_statistics' not in parsed_dict:
                    parsed_dict['per_inject_cause_statistics'] = {}
                parsed_dict['per_inject_cause_statistics']['number_of_inject_causes'] = int(m.group('inject_causes'))
                continue

            # Per Inject Cause Statistics
            m = p6.match(line)
            if m:
                current_section = 'inject_stats'
                parsed_dict['per_inject_cause_statistics']['per_inject_cause_statistics'] = {}
                continue

            # Parse punt cause statistics lines
            if current_section == 'punt_stats':
                # 003         Layer2 control and legacy                 859                   859
                m = p4.match(line)
                if m:
                    groups = m.groupdict()
                    counter_id = groups['counter_id']
                    punt_cause_name = groups['punt_cause_name'].strip()
                    
                    parsed_dict['global_per_cause_statistics']['per_punt_cause_statistics'][counter_id] = {
                        'counter_id': counter_id,
                        'punt_cause_name': punt_cause_name,
                        'packets_received': int(groups['packets_received']),
                        'packets_transmitted': int(groups['packets_transmitted'])
                    }
                    continue

            # Parse inject cause statistics lines
            if current_section == 'inject_stats':
                # 005         QFP <->RP keepalive                       303                   0
                m = p7.match(line)
                if m:
                    groups = m.groupdict()
                    counter_id = groups['counter_id']
                    inject_cause_name = groups['inject_cause_name'].strip()
                    
                    parsed_dict['per_inject_cause_statistics']['per_inject_cause_statistics'][counter_id] = {
                        'counter_id': counter_id,
                        'inject_cause_name': inject_cause_name,
                        'packets_received': int(groups['packets_received']),
                        'packets_transmitted': int(groups['packets_transmitted'])
                    }
                    continue

        return parsed_dict

# ===============================================================
# ===============================================================
class ShowPlatformHardwareCppActiveFeatureNatDatapathTimeSchema(MetaParser):
    """Schema for show platform hardware cpp active feature nat datapath time"""

    schema = {
        'timeouts': {
            'default': int,
            'tcp': int,
            'tcp_pptp': int,
            'udp': int,
            'finrst': int,
            'syn': int,
            'dns': int,
            'icmp': int,
            'skinny': int,
            'icmp_error': int,
            'esp': int,
            'rmap_entry': int,
            'nonpat_bind': int,
        },
        'counters': {
            'sage_bck': int,
            'bage_bck': int,
            'sysup': int,
            'dtl_pend': int,
        }
    }

# ===============================================================
# Parser for 'show platform hardware cpp active feature nat datapath time'
# ===============================================================
class ShowPlatformHardwareCppActiveFeatureNatDatapathTime(ShowPlatformHardwareCppActiveFeatureNatDatapathTimeSchema):
    """Parser for show platform hardware cpp active feature nat datapath time"""

    cli_command = 'show platform hardware cpp active feature nat datapath time'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize return dictionary
        ret_dict = {}

        # Timeouts: default 86400; TCP 86400; TCP PPTP 86400; UDP 300; FINRST 60; SYN 60; DNS 60; ICMP 60; Skinny 60; ICMP error 60; ESP 300; rmap entry 3600; nonpat bind 1200
        p1 = re.compile(r'^Timeouts:\s+default\s+(?P<default>\d+);\s+TCP\s+(?P<tcp>\d+);\s+TCP\s+PPTP\s+(?P<tcp_pptp>\d+);\s+UDP\s+(?P<udp>\d+);\s+FINRST\s+(?P<finrst>\d+);\s+SYN\s+(?P<syn>\d+);\s+DNS\s+(?P<dns>\d+);\s+ICMP\s+(?P<icmp>\d+);\s+Skinny\s+(?P<skinny>\d+);\s+ICMP\s+error\s+(?P<icmp_error>\d+);\s+ESP\s+(?P<esp>\d+);\s+rmap\s+entry\s+(?P<rmap_entry>\d+);\s+nonpat\s+bind\s+(?P<nonpat_bind>\d+)$')

        # sage_bck 29514720 bage_bck 933496 sysup 3334980
        p2 = re.compile(r'^sage_bck\s+(?P<sage_bck>\d+)\s+bage_bck\s+(?P<bage_bck>\d+)\s+sysup\s+(?P<sysup>\d+)$')

        # dtl_pend 0
        p3 = re.compile(r'^dtl_pend\s+(?P<dtl_pend>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Timeouts: default 86400; TCP 86400; TCP PPTP 86400; UDP 300; FINRST 60; SYN 60; DNS 60; ICMP 60; Skinny 60; ICMP error 60; ESP 300; rmap entry 3600; nonpat bind 1200
            m = p1.match(line)
            if m:
                timeouts = ret_dict.setdefault('timeouts', {})
                timeouts['default'] = int(m.groupdict()['default'])
                timeouts['tcp'] = int(m.groupdict()['tcp'])
                timeouts['tcp_pptp'] = int(m.groupdict()['tcp_pptp'])
                timeouts['udp'] = int(m.groupdict()['udp'])
                timeouts['finrst'] = int(m.groupdict()['finrst'])
                timeouts['syn'] = int(m.groupdict()['syn'])
                timeouts['dns'] = int(m.groupdict()['dns'])
                timeouts['icmp'] = int(m.groupdict()['icmp'])
                timeouts['skinny'] = int(m.groupdict()['skinny'])
                timeouts['icmp_error'] = int(m.groupdict()['icmp_error'])
                timeouts['esp'] = int(m.groupdict()['esp'])
                timeouts['rmap_entry'] = int(m.groupdict()['rmap_entry'])
                timeouts['nonpat_bind'] = int(m.groupdict()['nonpat_bind'])
                continue

            # sage_bck 29514720 bage_bck 933496 sysup 3334980
            m = p2.match(line)
            if m:
                counters = ret_dict.setdefault('counters', {})
                counters['sage_bck'] = int(m.groupdict()['sage_bck'])
                counters['bage_bck'] = int(m.groupdict()['bage_bck'])
                counters['sysup'] = int(m.groupdict()['sysup'])
                continue

            # dtl_pend 0
            m = p3.match(line)
            if m:
                counters = ret_dict.setdefault('counters', {})
                counters['dtl_pend'] = int(m.groupdict()['dtl_pend'])
                continue

        return ret_dict

# =======================================================================
# Schema for 'show platform hardware cpp active feature nat datapath bind'
# =======================================================================
class ShowPlatformHardwareCppActiveFeatureNatDatapathBindSchema(MetaParser):
    """Schema for show platform hardware cpp active feature nat datapath bind"""

    schema = {
        "bind_longest_chain": int,
        "avg_non_zero_bucket_len": int,
        "non_zero_bkts": int
    }


# =======================================================================
# Parser for 'show platform hardware cpp active feature nat datapath bind'
# =======================================================================
class ShowPlatformHardwareCppActiveFeatureNatDatapathBind(ShowPlatformHardwareCppActiveFeatureNatDatapathBindSchema):
    """Parser for show platform hardware cpp active feature nat datapath bind"""

    cli_command = "show platform hardware cpp active feature nat datapath bind"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Bind longest chain 0 avg non-zero bucket len 0 non-zero bkts 0
        p1 = re.compile(
            r"^Bind\s+longest\s+chain\s+(?P<longest_chain>\d+)\s+"
            r"avg\s+non-zero\s+bucket\s+len\s+(?P<avg_len>\d+)\s+"
            r"non-zero\s+bkts\s+(?P<non_zero_bkts>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Bind longest chain 0 avg non-zero bucket len 0 non-zero bkts 0
            m = p1.match(line)
            if m:
                parsed_dict['bind_longest_chain'] = int(m.group('longest_chain'))
                parsed_dict['avg_non_zero_bucket_len'] = int(m.group('avg_len'))
                parsed_dict['non_zero_bkts'] = int(m.group('non_zero_bkts'))
                break

        return parsed_dict

class ShowPlatformHardwareCppActiveFeatureNatDatapathPoolSchema(MetaParser):
    """Schema for show platform hardware cpp active feature nat datapath pool"""
    schema = {
        'pools': {
            Any(): {  # pool_id as key
                'pool_id': int,
                'type': int,
                'addroute': int,
                'mask': str,
                'allocated': int,
                'misses': int,
                'rotary_idx': str,
                'ahash_sz': int,
                'size': int,
                'max_pat_hash_size': int,
                'next': str,
                'hash_index': str,
                'hilo_ports': str,
                'pool_mem': str,
                'flags': str,
                'pool_name': str,
                'pat_wl': int,
                'no_ports_wl': int,
                'num_maps': int,
                'num_overload_maps': int,
                'vrf': str,
                'port_used': {
                    'tcp': int,
                    'udp': int
                },
                'conf_block_info': {
                    'start': str,
                    'end': str,
                    'flags': str,
                    'next': str,
                    'prev': str
                },
                Optional('tcp_pat_block_info'): {
                    'start': str,
                    'end': str,
                    'flags': str,
                    'next': str,
                    'prev': str
                },
                Optional('udp_pat_block_info'): {
                    'start': str,
                    'end': str,
                    'flags': str,
                    'next': str,
                    'prev': str
                },
                Optional('icmp_pat_block_info'): {
                    'start': str,
                    'end': str,
                    'flags': str,
                    'next': str,
                    'prev': str
                },
                Optional('gre_pat_block_info'): {
                    'start': str,
                    'end': str,
                    'flags': str,
                    'next': str,
                    'prev': str
                },
                'alloced_addr_info': {
                    'addr': str,
                    'secondary_addr': str,
                    'refcnt': int,
                    'flags': str,
                    'vrfid': int,
                    'next': str,
                    'pat_index': int
                }
            }
        }
    }


class ShowPlatformHardwareCppActiveFeatureNatDatapathPool(ShowPlatformHardwareCppActiveFeatureNatDatapathPoolSchema):
    """Parser for show platform hardware cpp active feature nat datapath pool"""
    cli_command = 'show platform hardware cpp active feature nat datapath pool'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # pool_id 6 type 1 addroute 0 mask 0xffffff00 allocated 1 misses 0 rotary idx 0x0 ahash sz 24 size 24  max_pat_hash_size 1 next 0x0 hash_index 0x36, hilo ports 0x0  pool mem 0x36cb5c30 flags 0x0 pool_name: 120-pool pat_wl 0 no_ports_wl 0 num_maps 1 num_overload_maps 1 vrf 0x0 port_used tcp 0 udp 0
        p1 = re.compile(r'^pool_id\s+(?P<pool_id>\d+)\s+type\s+(?P<type>\d+)\s+addroute\s+(?P<addroute>\d+)\s+'
                        r'mask\s+(?P<mask>0x[0-9a-fA-F]+)\s+allocated\s+(?P<allocated>\d+)\s+misses\s+(?P<misses>\d+)\s+'
                        r'rotary\s+idx\s+(?P<rotary_idx>0x[0-9a-fA-F]+)\s+ahash\s+sz\s+(?P<ahash_sz>\d+)\s+size\s+(?P<size>\d+)\s+'
                        r'max_pat_hash_size\s+(?P<max_pat_hash_size>\d+)\s+next\s+(?P<next>0x[0-9a-fA-F]+)\s+'
                        r'hash_index\s+(?P<hash_index>0x[0-9a-fA-F]+),\s+hilo\s+ports\s+(?P<hilo_ports>0x[0-9a-fA-F]+)\s+'
                        r'pool\s+mem\s+(?P<pool_mem>0x[0-9a-fA-F]+)\s+flags\s+(?P<flags>0x[0-9a-fA-F]+)\s+pool_name:\s+(?P<pool_name>[\w-]+)\s+'
                        r'pat_wl\s+(?P<pat_wl>\d+)\s+no_ports_wl\s+(?P<no_ports_wl>\d+)\s+num_maps\s+(?P<num_maps>\d+)\s+'
                        r'num_overload_maps\s+(?P<num_overload_maps>\d+)\s+vrf\s+(?P<vrf>0x[0-9a-fA-F]+)\s+'
                        r'port_used\s+tcp\s+(?P<tcp>\d+)\s+udp\s+(?P<udp>\d+)$')

        # Conf block info
        p2 = re.compile(r'^Conf\s+block\s+info$')

        # TCP PAT block info
        p3 = re.compile(r'^\s*TCP\s+PAT\s+block\s+info$')

        # UDP PAT block info
        p4 = re.compile(r'^\s*UDP\s+PAT\s+block\s+info$')

        # ICMP PAT block info
        p5 = re.compile(r'^\s*ICMP\s+PAT\s+block\s+info$')

        # GRE PAT block info
        p6 = re.compile(r'^\s*GRE\s+PAT\s+block\s+info$')

        # start 120.100.1.1 end 120.100.1.24 flags 0x0 next 0x0 prev 0x0
        p7 = re.compile(r'^start\s+(?P<start>[\d\.]+)\s+end\s+(?P<end>[\d\.]+)\s+flags\s+(?P<flags>0x[0-9a-fA-F]+)\s+'
                        r'next\s+(?P<next>0x[0-9a-fA-F]+)\s+prev\s+(?P<prev>0x[0-9a-fA-F]+)$')

        # Alloced addr info
        p8 = re.compile(r'^Alloced\s+addr\s+info$')

        # addr 120.100.1.1 0.0.0.0 refcnt 5 flags 0x1 vrfid 0 next 0x0 pat_index 0
        p9 = re.compile(r'^addr\s+(?P<addr>[\d\.]+)\s+(?P<secondary_addr>[\d\.]+)\s+refcnt\s+(?P<refcnt>\d+)\s+'
                        r'flags\s+(?P<flags>0x[0-9a-fA-F]+)\s+vrfid\s+(?P<vrfid>\d+)\s+next\s+(?P<next>0x[0-9a-fA-F]+)\s+'
                        r'pat_index\s+(?P<pat_index>\d+)$')

        current_pool_id = None
        current_block_type = None

        for line in output.splitlines():
            line = line.strip()

            # pool_id 6 type 1 addroute 0 mask 0xffffff00 allocated 1 misses 0 rotary idx 0x0 ahash sz 24 size 24  max_pat_hash_size 1 next 0x0 hash_index 0x36, hilo ports 0x0  pool mem 0x36cb5c30 flags 0x0 pool_name: 120-pool pat_wl 0 no_ports_wl 0 num_maps 1 num_overload_maps 1 vrf 0x0 port_used tcp 0 udp 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                pool_id = group['pool_id']
                current_pool_id = pool_id

                # Initialize pools dictionary if not exists
                if 'pools' not in ret_dict:
                    ret_dict['pools'] = {}

                pool_info = ret_dict['pools'].setdefault(pool_id, {})

                # Integer fields - values that should be converted to integers
                integer_fields = [
                    'pool_id', 'type', 'addroute', 'allocated', 'misses', 'ahash_sz', 
                    'size', 'max_pat_hash_size', 'pat_wl', 'no_ports_wl', 'num_maps', 
                    'num_overload_maps', 'tcp', 'udp'
                ]

                # String fields - values that should remain as strings
                string_fields = [
                    'mask', 'rotary_idx', 'hash_index', 'hilo_ports', 'pool_mem', 
                    'flags', 'pool_name', 'vrf', 'next'
                ]

                # Add integer fields to pool_info
                for field in integer_fields:
                    if field in group and field not in ['tcp', 'udp']:  # tcp/udp handled separately
                        pool_info[field] = int(group[field])

                # Add string fields to pool_info
                for field in string_fields:
                    if field in group:
                        pool_info[field] = group[field]

                # Add tcp and udp as part of port_used structure
                pool_info['port_used'] = {
                    'tcp': int(group['tcp']),
                    'udp': int(group['udp'])
                }
                continue

            # Conf block info
            m = p2.match(line)
            if m:
                current_block_type = 'conf_block_info'
                continue

            # TCP PAT block info
            m = p3.match(line)
            if m:
                current_block_type = 'tcp_pat_block_info'
                continue

            # UDP PAT block info
            m = p4.match(line)
            if m:
                current_block_type = 'udp_pat_block_info'
                continue

            # ICMP PAT block info
            m = p5.match(line)
            if m:
                current_block_type = 'icmp_pat_block_info'
                continue

            # GRE PAT block info
            m = p6.match(line)
            if m:
                current_block_type = 'gre_pat_block_info'
                continue

            # start 120.100.1.1 end 120.100.1.24 flags 0x0 next 0x0 prev 0x0
            m = p7.match(line)
            if m and current_pool_id and current_block_type:
                group = m.groupdict()
                if 'pools' in ret_dict and current_pool_id in ret_dict['pools']:
                    ret_dict['pools'][current_pool_id][current_block_type] = {
                        'start': group['start'],
                        'end': group['end'],
                        'flags': group['flags'],
                        'next': group['next'],
                        'prev': group['prev']
                    }
                continue

            # Alloced addr info
            m = p8.match(line)
            if m:
                current_block_type = 'alloced_addr_info'
                continue

            # addr 120.100.1.1 0.0.0.0 refcnt 5 flags 0x1 vrfid 0 next 0x0 pat_index 0
            m = p9.match(line)
            if m and current_pool_id:
                group = m.groupdict()
                if 'pools' in ret_dict and current_pool_id in ret_dict['pools']:
                    ret_dict['pools'][current_pool_id]['alloced_addr_info'] = {
                        'addr': group['addr'],
                        'secondary_addr': group['secondary_addr'],
                        'refcnt': int(group['refcnt']),
                        'flags': group['flags'],
                        'vrfid': int(group['vrfid']),
                        'next': group['next'],
                        'pat_index': int(group['pat_index'])
                    }
                continue

        return ret_dict

# Schema for 'show platform hardware cpp active feature nat datapath map'
class ShowPlatformHardwareCppActiveFeatureNatDatapathMapSchema(MetaParser):
    """Schema for show platform hardware cpp active feature nat datapath map"""

    schema = {
        'interface_map_table': {
            'start': str,
            'end': str,
        },
        'edm_maps': int,
        'mappings': {
            Any(): {
                'mapping_id': int,
                'pool_id': int,
                'if_handle': str,
                'match_type': int,
                'source_type': int,
                'domain': int,
                'proto': int,
                'local_ip': str,
                'local_port': int,
                'global_ip': str,
                'global_port': int,
                'flags': str,
                'refcount': int,
                'cp_mapping_id': int,
                'next': str,
                'hashidx': int,
                'vrfid': int,
                'vrf_tableid': str,
                'rg': int,
                'pap_enabled': int,
                'egress_ifh': str,
            }
        }
    }


# Parser for 'show platform hardware cpp active feature nat datapath map'
class ShowPlatformHardwareCppActiveFeatureNatDatapathMap(ShowPlatformHardwareCppActiveFeatureNatDatapathMapSchema):
    """Parser for show platform hardware cpp active feature nat datapath map"""

    cli_command = "show platform hardware cpp active feature nat datapath map"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the dictionary to store parsed data
        ret_dict = {}

        # I/f Map Table
        p1 = re.compile(r'^I/f Map Table$')

        # I/f Map Table End
        p2 = re.compile(r'^I/f Map Table End$')

        # edm maps 0
        p3 = re.compile(r'^edm maps (?P<count>\d+)$')

        # mapping id 1 pool_id 5 if_handle 0x0 match_type 0 source_type 0 domain 0 proto 0 Local IP 0.0.0.0, Local Port 0 Global IP 0.0.0.0 Global Port 0 Flags 0x100 refcount 3 cp_mapping_id 5 next 0x0 hashidx 50 vrfid 0 vrf_tableid 0x0 rg 0 pap_enabled 0 egress_ifh 0x0
        p4 = re.compile(r'^mapping id (?P<mapping_id>\d+) pool_id (?P<pool_id>\d+) if_handle (?P<if_handle>\S+) match_type (?P<match_type>\d+) source_type (?P<source_type>\d+) domain (?P<domain>\d+) proto (?P<proto>\d+) Local IP (?P<local_ip>\S+), Local Port (?P<local_port>\d+) Global IP (?P<global_ip>\S+) Global Port (?P<global_port>\d+) Flags (?P<flags>\S+) refcount (?P<refcount>\d+) cp_mapping_id (?P<cp_mapping_id>\d+) next (?P<next>\S+) hashidx (?P<hashidx>\d+) vrfid (?P<vrfid>\d+) vrf_tableid (?P<vrf_tableid>\S+) rg (?P<rg>\d+) pap_enabled (?P<pap_enabled>\d+) egress_ifh (?P<egress_ifh>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # I/f Map Table
            m = p1.match(line)
            if m:
                ret_dict.setdefault('interface_map_table', {})['start'] = 'I/f Map Table'
                continue

            # I/f Map Table End
            m = p2.match(line)
            if m:
                ret_dict.setdefault('interface_map_table', {})['end'] = 'I/f Map Table End'
                continue

            # edm maps 0
            m = p3.match(line)
            if m:
                ret_dict['edm_maps'] = int(m.groupdict()['count'])
                continue

            # mapping id 1 pool_id 5 if_handle 0x0 match_type 0 source_type 0 domain 0 proto 0 Local IP 0.0.0.0, Local Port 0 Global IP 0.0.0.0 Global Port 0 Flags 0x100 refcount 3 cp_mapping_id 5 next 0x0 hashidx 50 vrfid 0 vrf_tableid 0x0 rg 0 pap_enabled 0 egress_ifh 0x0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                mapping_id = groups['mapping_id']

                mappings_dict = ret_dict.setdefault('mappings', {})
                mapping_dict = mappings_dict.setdefault(mapping_id, {})

                mapping_dict['mapping_id'] = int(groups['mapping_id'])
                mapping_dict['pool_id'] = int(groups['pool_id'])
                mapping_dict['if_handle'] = groups['if_handle']
                mapping_dict['match_type'] = int(groups['match_type'])
                mapping_dict['source_type'] = int(groups['source_type'])
                mapping_dict['domain'] = int(groups['domain'])
                mapping_dict['proto'] = int(groups['proto'])
                mapping_dict['local_ip'] = groups['local_ip']
                mapping_dict['local_port'] = int(groups['local_port'])
                mapping_dict['global_ip'] = groups['global_ip']
                mapping_dict['global_port'] = int(groups['global_port'])
                mapping_dict['flags'] = groups['flags']
                mapping_dict['refcount'] = int(groups['refcount'])
                mapping_dict['cp_mapping_id'] = int(groups['cp_mapping_id'])
                mapping_dict['next'] = groups['next']
                mapping_dict['hashidx'] = int(groups['hashidx'])
                mapping_dict['vrfid'] = int(groups['vrfid'])
                mapping_dict['vrf_tableid'] = groups['vrf_tableid']
                mapping_dict['rg'] = int(groups['rg'])
                mapping_dict['pap_enabled'] = int(groups['pap_enabled'])
                mapping_dict['egress_ifh'] = groups['egress_ifh']
                continue

        return ret_dict

class ShowPlatformHardwareCppActiveFeatureNatDatapathStatsSchema(MetaParser):
    """Schema for show platform hardware cpp active feature nat datapath stats"""

    schema = {
        'nat_stats': {
            'non_extended': int,
            'entry_timeouts': int,
            'statics': int,
            'static_net': int,
            'hits': int,
            'flowdb_hits': int,
            'misses': int,
            'nat_rx_pkts': int,
            'nat_tx_pkts': int,
            'nat_unmarked_pkts': int,
            'nat_stick_rx_pkts': int,
            'nat_stick_i2o_pkts': int,
            'nat_stick_o2i_pkts': int,
            'nat_res_port_in2out': int,
            'nat_res_port_out2in': int,
            'non_natted_in2out': int,
            'nat_bypass': int,
            'non_natted_out2in': int,
            'ipv4_nat_stick_forus_hits_pkts': int,
            'ipv4_nat_stick_hit_sb': int,
            'ipv4_nat_stick_ha_ar_pkts': int,
            'ipv4_nat_stick_ha_tcp_fin': int,
            'ipv4_nat_stick_failed_ha_pkts': int,
            'ipv4_nat_alg_bind_pkts': int,
            'cgn_dest_log_timeouts': int,
            'ipv4_nat_alg_sd_not_found': int,
            'ipv4_nat_alg_sd_tail_not_found': int,
        },
        'proxy_stats': {
            'ipc_retry_fail': int,
            'cfg_rcvd': int,
            'cfg_rsp': int,
        },
        'session_summary': {
            'total_sessions': int,
            'udp_sessions': int,
            'tcp_sessions': int,
            'icmp_sessions': int,
        }
    }


class ShowPlatformHardwareCppActiveFeatureNatDatapathStats(ShowPlatformHardwareCppActiveFeatureNatDatapathStatsSchema):
    """Parser for show platform hardware cpp active feature nat datapath stats"""

    cli_command = 'show platform hardware cpp active feature nat datapath stats'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing the output
        # non_extended 0 entry_timeouts 0 statics 0 static net 0 hits 0 flowdb_hits 0 misses 0
        p1 = re.compile(r'^non_extended (?P<non_extended>\d+) entry_timeouts (?P<entry_timeouts>\d+) statics (?P<statics>\d+) static net (?P<static_net>\d+) hits (?P<hits>\d+) flowdb_hits (?P<flowdb_hits>\d+) misses (?P<misses>\d+)$')

        # nat_rx_pkts 306 nat_tx_pkts 324 nat_unmarked_pkts 0
        p2 = re.compile(r'^nat_rx_pkts (?P<nat_rx_pkts>\d+) nat_tx_pkts (?P<nat_tx_pkts>\d+) nat_unmarked_pkts (?P<nat_unmarked_pkts>\d+)$')

        # nat_stick_rx_pkts 0 nat_stick_i2o_pkts 0 nat_stick_o2i_pkts 0
        p3 = re.compile(r'^nat_stick_rx_pkts (?P<nat_stick_rx_pkts>\d+) nat_stick_i2o_pkts (?P<nat_stick_i2o_pkts>\d+) nat_stick_o2i_pkts (?P<nat_stick_o2i_pkts>\d+)$')

        # nat_res_port_in2out 0 nat_res_port_out2in 0
        p4 = re.compile(r'^nat_res_port_in2out (?P<nat_res_port_in2out>\d+) nat_res_port_out2in (?P<nat_res_port_out2in>\d+)$')

        # non_natted_in2out 0 nat_bypass 0 non_natted_out2in 0
        p5 = re.compile(r'^non_natted_in2out (?P<non_natted_in2out>\d+) nat_bypass (?P<nat_bypass>\d+) non_natted_out2in (?P<non_natted_out2in>\d+)$')

        # ipv4_nat_stick_forus_hits_pkts 0 ipv4_nat_stick_hit_sb 0
        p6 = re.compile(r'^ipv4_nat_stick_forus_hits_pkts (?P<ipv4_nat_stick_forus_hits_pkts>\d+) ipv4_nat_stick_hit_sb (?P<ipv4_nat_stick_hit_sb>\d+)$')

        # ipv4_nat_stick_ha_ar_pkts 0 ipv4_nat_stick_ha_tcp_fin 0 ipv4_nat_stick_failed_ha_pkts 0
        p7 = re.compile(r'^ipv4_nat_stick_ha_ar_pkts (?P<ipv4_nat_stick_ha_ar_pkts>\d+) ipv4_nat_stick_ha_tcp_fin (?P<ipv4_nat_stick_ha_tcp_fin>\d+) ipv4_nat_stick_failed_ha_pkts (?P<ipv4_nat_stick_failed_ha_pkts>\d+)$')

        # ipv4_nat_alg_bind_pkts 0  cgn_dest_log_timeouts 0
        p8 = re.compile(r'^ipv4_nat_alg_bind_pkts (?P<ipv4_nat_alg_bind_pkts>\d+)\s+cgn_dest_log_timeouts (?P<cgn_dest_log_timeouts>\d+)$')

        # ipv4_nat_alg_sd_not_found 0 ipv4_nat_alg_sd_tail_not_found 0
        p9 = re.compile(r'^ipv4_nat_alg_sd_not_found (?P<ipv4_nat_alg_sd_not_found>\d+) ipv4_nat_alg_sd_tail_not_found (?P<ipv4_nat_alg_sd_tail_not_found>\d+)$')

        # ipc_retry_fail 0 cfg_rcvd 52 cfg_rsp 56
        p10 = re.compile(r'^\s*ipc_retry_fail (?P<ipc_retry_fail>\d+) cfg_rcvd (?P<cfg_rcvd>\d+) cfg_rsp (?P<cfg_rsp>\d+)$')

        # Number of sess 8 udp 6 tcp 1 icmp 1
        p11 = re.compile(r'^Number of sess (?P<total_sessions>\d+) udp (?P<udp_sessions>\d+) tcp (?P<tcp_sessions>\d+) icmp (?P<icmp_sessions>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Skip empty lines and header lines
            if not line or line.startswith('Proxy stats:'):
                continue

            # non_extended 0 entry_timeouts 0 statics 0 static net 0 hits 0 flowdb_hits 0 misses 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if 'nat_stats' not in parsed_dict:
                    parsed_dict.setdefault('nat_stats', {})
                parsed_dict['nat_stats'].update({
                    'non_extended': int(group['non_extended']),
                    'entry_timeouts': int(group['entry_timeouts']),
                    'statics': int(group['statics']),
                    'static_net': int(group['static_net']),
                    'hits': int(group['hits']),
                    'flowdb_hits': int(group['flowdb_hits']),
                    'misses': int(group['misses'])
                })
                continue

            # nat_rx_pkts 306 nat_tx_pkts 324 nat_unmarked_pkts 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if 'nat_stats' not in parsed_dict:
                    parsed_dict['nat_stats'] = {}
                parsed_dict['nat_stats'].update({
                    'nat_rx_pkts': int(group['nat_rx_pkts']),
                    'nat_tx_pkts': int(group['nat_tx_pkts']),
                    'nat_unmarked_pkts': int(group['nat_unmarked_pkts'])
                })
                continue

            # nat_stick_rx_pkts 0 nat_stick_i2o_pkts 0 nat_stick_o2i_pkts 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if 'nat_stats' not in parsed_dict:
                    parsed_dict['nat_stats'] = {}
                parsed_dict['nat_stats'].update({
                    'nat_stick_rx_pkts': int(group['nat_stick_rx_pkts']),
                    'nat_stick_i2o_pkts': int(group['nat_stick_i2o_pkts']),
                    'nat_stick_o2i_pkts': int(group['nat_stick_o2i_pkts'])
                })
                continue

            # nat_res_port_in2out 0 nat_res_port_out2in 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if 'nat_stats' not in parsed_dict:
                    parsed_dict['nat_stats'] = {}
                parsed_dict['nat_stats'].update({
                    'nat_res_port_in2out': int(group['nat_res_port_in2out']),
                    'nat_res_port_out2in': int(group['nat_res_port_out2in'])
                })
                continue

            # non_natted_in2out 0 nat_bypass 0 non_natted_out2in 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if 'nat_stats' not in parsed_dict:
                    parsed_dict['nat_stats'] = {}
                parsed_dict['nat_stats'].update({
                    'non_natted_in2out': int(group['non_natted_in2out']),
                    'nat_bypass': int(group['nat_bypass']),
                    'non_natted_out2in': int(group['non_natted_out2in'])
                })
                continue

            # ipv4_nat_stick_forus_hits_pkts 0 ipv4_nat_stick_hit_sb 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if 'nat_stats' not in parsed_dict:
                    parsed_dict['nat_stats'] = {}
                parsed_dict['nat_stats'].update({
                    'ipv4_nat_stick_forus_hits_pkts': int(group['ipv4_nat_stick_forus_hits_pkts']),
                    'ipv4_nat_stick_hit_sb': int(group['ipv4_nat_stick_hit_sb'])
                })
                continue

            # ipv4_nat_stick_ha_ar_pkts 0 ipv4_nat_stick_ha_tcp_fin 0 ipv4_nat_stick_failed_ha_pkts 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if 'nat_stats' not in parsed_dict:
                    parsed_dict['nat_stats'] = {}
                parsed_dict['nat_stats'].update({
                    'ipv4_nat_stick_ha_ar_pkts': int(group['ipv4_nat_stick_ha_ar_pkts']),
                    'ipv4_nat_stick_ha_tcp_fin': int(group['ipv4_nat_stick_ha_tcp_fin']),
                    'ipv4_nat_stick_failed_ha_pkts': int(group['ipv4_nat_stick_failed_ha_pkts'])
                })
                continue

            # ipv4_nat_alg_bind_pkts 0  cgn_dest_log_timeouts 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if 'nat_stats' not in parsed_dict:
                    parsed_dict['nat_stats'] = {}
                parsed_dict['nat_stats'].update({
                    'ipv4_nat_alg_bind_pkts': int(group['ipv4_nat_alg_bind_pkts']),
                    'cgn_dest_log_timeouts': int(group['cgn_dest_log_timeouts'])
                })
                continue

            # ipv4_nat_alg_sd_not_found 0 ipv4_nat_alg_sd_tail_not_found 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if 'nat_stats' not in parsed_dict:
                    parsed_dict['nat_stats'] = {}
                parsed_dict['nat_stats'].update({
                    'ipv4_nat_alg_sd_not_found': int(group['ipv4_nat_alg_sd_not_found']),
                    'ipv4_nat_alg_sd_tail_not_found': int(group['ipv4_nat_alg_sd_tail_not_found'])
                })
                continue

            # ipc_retry_fail 0 cfg_rcvd 52 cfg_rsp 56
            m = p10.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['proxy_stats'] = {
                    'ipc_retry_fail': int(group['ipc_retry_fail']),
                    'cfg_rcvd': int(group['cfg_rcvd']),
                    'cfg_rsp': int(group['cfg_rsp'])
                }
                continue

            # Number of sess 8 udp 6 tcp 1 icmp 1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['session_summary'] = {
                    'total_sessions': int(group['total_sessions']),
                    'udp_sessions': int(group['udp_sessions']),
                    'tcp_sessions': int(group['tcp_sessions']),
                    'icmp_sessions': int(group['icmp_sessions'])
                }
                continue

        return parsed_dict
