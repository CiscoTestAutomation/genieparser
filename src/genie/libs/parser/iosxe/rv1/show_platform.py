""" show_platform.py

IOSXE revision 1 parsers for the following show commands:

    * 'show inventory'
    * 'show platform'
    * show platform software infrastructure thread fastpath
"""

import re
import logging

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And, ListOf
from genie.libs.parser.utils.common import Common, INTERFACE_ABBREVIATION_MAPPING_TABLE

# pyATS
from pyats.utils.exceptions import SchemaTypeError

log = logging.getLogger(__name__)

class ShowProcessesCpuPlatformSortedSchema(MetaParser):
    """Schema for show processes cpu platform sorted"""
    schema = {
        Optional('cpu_utilization'): {
            Optional('five_sec_cpu_total'): float,
            Optional('one_min_cpu'): float,
            Optional('five_min_cpu'): float,
            Optional('core'): {
                Any(): {
                    'core_cpu_util_five_secs': float,
                    'core_cpu_util_one_min': float,
                    'core_cpu_util_five_min': float,
                },
            }
        },
        Optional('sort'): {
            Any(): {
                'ppid': int,
                'five_sec_cpu': float,
                'one_min_cpu': float,
                'five_min_cpu': float,
                'status': str,
                'size': int,
                'process': str,
            },
        }
    }

class ShowProcessesCpuPlatformSorted(ShowProcessesCpuPlatformSortedSchema):
    """Parser for show processes cpu platform sorted"""

    cli_command = ['show processes cpu platform sorted', 'show processes cpu platform sorted | exclude {exclude}']
    exclude = ['five_min_cpu', 'nonzero_cpu_processes', 'zero_cpu_processes', 'invoked',
               'runtime', 'usecs', 'five_sec_cpu', 'one_min_cpu']

    def cli(self, exclude=None, output=None):
        if output is None:
            if exclude:
                self.cli_command = self.cli_command[1].format(exclude=exclude)
            else:
                self.cli_command = self.cli_command[0]
            output = self.device.execute(self.cli_command)
        # initial return dictionary
        ret_dict = {}
        index = 0

        # initial regexp pattern

        # CPU utilization for five seconds: 43%, one minute: 44%, five minutes: 44%
        p1 = re.compile(r'^CPU +utilization +for +five +seconds: +(?P<five_sec_cpu_total>[\d\%]+),'
                        r' +one +minute: +(?P<one_min_cpu>[\d\%]+),'
                        r' +five +minutes: +(?P<five_min_cpu>[\d\%]+)$')

        # Core 0: CPU utilization for five seconds:  6%, one minute: 11%, five minutes: 11%
        p2 = re.compile(r'^(?P<core>[\w\s]+): +CPU +utilization +for'
                        r' +five +seconds: +(?P<core_cpu_util_five_secs>\d+\%+),'
                        r' +one +minute: +(?P<core_cpu_util_one_min>[\d+\%]+),'
                        r' +five +minutes: +(?P<core_cpu_util_five_min>[\d+\%]+)$')

        # 21188   21176    599%    600%    599%  R           478632  ucode_pkt_PPE0
        p3 = re.compile(r'^(?P<pid>\d+) +(?P<ppid>\d+)'
                        r' +(?P<five_sec_cpu>[\d\%]+) +(?P<one_min_cpu>[\d\%]+)'
                        r' +(?P<five_min_cpu>[\d\%]+) +(?P<status>[\w]+)'
                        r' +(?P<size>\d+) +(?P<process>.*)$')

        for line in output.splitlines():
            line = line.strip()

            # CPU utilization for five seconds:  2%, one minute:  5%, five minutes: 22%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('cpu_utilization', {})
                ret_dict['cpu_utilization']['five_sec_cpu_total'] = float(re.search(r'\d+', group['five_sec_cpu_total']).group())/100
                ret_dict['cpu_utilization']['one_min_cpu'] = float(re.search(r'\d+', group['one_min_cpu']).group())/100
                ret_dict['cpu_utilization']['five_min_cpu'] = float(re.search(r'\d+', group['five_min_cpu']).group())/100
                continue

            # Core 0: CPU utilization for five seconds:  2%, one minute:  8%, five minutes: 18%
            m = p2.match(line)
            if m:
                group = m.groupdict()
                core = group.pop('core')
                if 'cpu_utilization' not in ret_dict:
                    ret_dict.setdefault('cpu_utilization', {})
                ret_dict['cpu_utilization'].setdefault('core', {}).setdefault(core, {})
                ret_dict['cpu_utilization']['core'][core]['core_cpu_util_five_secs'] = float(re.search(r'\d+', group['core_cpu_util_five_secs']).group())/100
                ret_dict['cpu_utilization']['core'][core]['core_cpu_util_one_min'] = float(re.search(r'\d+', group['core_cpu_util_one_min']).group())/100
                ret_dict['cpu_utilization']['core'][core]['core_cpu_util_five_min'] = float(re.search(r'\d+', group['core_cpu_util_five_min']).group())/100

            #    Pid    PPid    5Sec    1Min    5Min  Status        Size  Name
            # --------------------------------------------------------------------------------
            #      1       0      0%      0%      0%  S          1863680  init
            #      2       0      0%      0%      0%  S                0  kthreadd
            #      3       2      0%      0%      0%  S                0  migration/0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('sort', {}).setdefault(index, {})
                ret_dict['sort'][index]['ppid'] = int(group['ppid'])
                ret_dict['sort'][index]['five_sec_cpu'] = float(re.search(r'\d+', group['five_sec_cpu']).group())/100
                ret_dict['sort'][index]['one_min_cpu'] = float(re.search(r'\d+', group['one_min_cpu']).group())/100
                ret_dict['sort'][index]['five_min_cpu'] = float(re.search(r'\d+', group['five_min_cpu']).group())/100
                ret_dict['sort'][index]['status'] = group['status']
                ret_dict['sort'][index]['size'] = int(group['size'])
                ret_dict['sort'][index]['process'] = group['process']
                index += 1
                continue

        return ret_dict


# =====================
# Schema for:
#   * 'show inventory'
# =====================
class ShowInventorySchema(MetaParser):
    """Schema for:
    * 'show inventory'

    Revision 1:
    Added 'sp' section
    """

    schema = {
        Optional("main"): {
            Optional("swstack"): bool,
            Optional(Any()): {
                Any(): {
                    Optional("name"): str,
                    Optional("descr"): str,
                    Optional("pid"): str,
                    Optional("vid"): str,
                    Optional("sn"): str,
                },
            },
        },
        Optional("slot"): {
            Any(): {
                Optional("rp"): {
                    Any(): {
                        Optional("name"): str,
                        Optional("descr"): str,
                        Optional("pid"): str,
                        Optional("vid"): str,
                        Optional("sn"): str,
                        Optional("swstack_power"): str,
                        Optional("swstack_power_sn"): str,
                        Optional("subslot"): {
                            Any(): {
                                Any(): {
                                    Optional("name"): str,
                                    Optional("descr"): str,
                                    Optional("pid"): str,
                                    Optional("vid"): str,
                                    Optional("sn"): str,
                                },
                            },
                        },
                    },
                },
                Optional("lc"): {
                    Any(): {
                        Optional("name"): str,
                        Optional("descr"): str,
                        Optional("pid"): str,
                        Optional("vid"): str,
                        Optional("sn"): str,
                        Optional("swstack_power"): str,
                        Optional("swstack_power_sn"): str,
                        Optional("subslot"): {
                            Any(): {
                                Any(): {
                                    Optional("name"): str,
                                    Optional("descr"): str,
                                    Optional("pid"): str,
                                    Optional("vid"): str,
                                    Optional("sn"): str,
                                },
                            },
                        },
                    },
                },
                Optional("sp"): {
                    Any(): {
                        Optional("name"): str,
                        Optional("descr"): str,
                        Optional("pid"): str,
                        Optional("vid"): str,
                        Optional("sn"): str,
                    },
                },
                Optional("pluggable", description='Interface pluggable module'): {
                    Any(description='Interface name (brief)'): {
                        Optional("name", description='Interface name (expanded)'): str,
                        Optional("descr"): str,
                        Optional("pid"): str,
                        Optional("vid"): str,
                        Optional("sn"): str,
                    }
                },
                Optional("other"): {
                    Any(): {
                        Optional("name"): str,
                        Optional("descr"): str,
                        Optional("pid"): str,
                        Optional("vid"): str,
                        Optional("sn"): str,
                        Optional("swstack_power"): str,
                        Optional("swstack_power_sn"): str,
                        Optional("subslot"): {
                            Any(): {
                                Any(): {
                                    Optional("name"): str,
                                    Optional("descr"): str,
                                    Optional("pid"): str,
                                    Optional("vid"): str,
                                    Optional("sn"): str,
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ====================
# Parser for:
#   * 'show inventory'
# ====================
class ShowInventory(ShowInventorySchema):
    """Parser for:
    * 'show inventory'
    """

    cli_command = ["show inventory"]

    def cli(self, output=None):

        if output is None:
            # Build command
            cmd = self.cli_command[0]
            # Execute command
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        name = descr = slot = subslot = pid = ""
        slot_dict = None
        asr900_rp = False

        # NAME: "Switch 1", DESCR: "WS-C3850-24P-E"
        # NAME: "StackPort5/2", DESCR: "StackPort5/2"
        # NAME: "Switch 5 - Power Supply A", DESCR: "Switch 5 - Power Supply A"
        # NAME: "subslot 0/0 transceiver 2", DESCR: "GE T"
        # NAME: "NIM subslot 0/0", DESCR: "Front Panel 3 ports Gigabitethernet Module"
        # NAME: "Modem 0 on Cellular0/2/0", DESCR: "Sierra Wireless EM7455/EM7430"
        # NAME: "1", DESCR: "WS-C3560CX-12PC-S"
        # NAME: "Fo1/1/1", DESCR: "QSFP 40G SR BD SFP"
        p1 = re.compile(r"^NAME: +\"(?P<name>.*)\"," r" +DESCR: +\"(?P<descr>.*)\"$")

        # Switch 1
        # Switch 1 Chassis
        p1_1 = re.compile(r"^Switch +(?P<slot>(\S+))( Chassis)?$")

        # Power Supply Module 0
        # Power Supply Module 1
        # Switch 1 - Power Supply B
        p1_2 = re.compile(r"^(Switch (?P<slot>\d+) - )?Power Supply (Module )?(?P<subslot>[\d\w]+)$")

        # SPA subslot 0/0
        # IM subslot 0/1
        # NIM subslot 0/0
        p1_3 = re.compile(r"^(SPA|IM|NIM|PVDM) +subslot +(?P<slot>(\d+))/(?P<subslot>(\d+))$")

        # subslot 0/0 transceiver 0
        p1_4 = re.compile(r"^subslot +(?P<slot>(\d+))\/(?P<subslot>(.*))")

        # StackPort1/1
        p1_5 = re.compile(r"^StackPort(?P<slot>(\d+))/(?P<subslot>(\d+))$")

        # Fan Tray
        p1_6 = re.compile(r"^Fan +Tray|\d+$")

        # Modem 0 on Cellular0/2/0
        p1_7 = re.compile(r"^Modem +(?P<modem>\S+) +on +Cellular(?P<slot>\d+)\/(?P<subslot>.*)$")

        # Slot 2 Linecard
        # Slot 3 Supervisor
        # Switch 1 Slot 1 Linecard
        # Switch 2 Slot 4 Supervisor
        p1_8 = re.compile(r"^(?:Switch +\d+ +)?Slot +\d+ +(?:Linecard|Supervisor|Router)$")

        # Supervisor
        p1_9 = re.compile(r"^Supervisor$")

        # Switch 1 FRU Uplink Module 1
        p1_10 = re.compile(r'^Switch (?P<slot>\d+) FRU Uplink Module (?P<subslot>\d+)$')

        # PID: ASR-920-24SZ-IM   , VID: V01  , SN: CAT1902V19M
        # PID: SFP-10G-LR        , VID: CSCO , SN: CD180456291
        # PID: A900-IMA3G-IMSG   , VID: V01  , SN: FOC2204PAP1
        # PID: SFP-GE-T          , VID: V02  , SN: MTC2139029X
        # PID: ISR4331-3x1GE     , VID: V01  , SN:
        # PID: ISR4331/K9        , VID:      , SN: FDO21520TGH
        # PID: ISR4331/K9        , VID:      , SN:
        # PID: , VID: 1.0  , SN: 1162722191
        # PID: WS-C3560CX-12PC-S , VID: V03  , SN: FOC2419L9KY
        p2 = re.compile(
            r"^PID: +(?P<pid>[\S\s]+)? *, +VID:(?: +(?P<vid>(\S+)))? *,"
            r" +SN:(?: +(?P<sn>(\S+)))?$"
        )
        for line in out.splitlines():
            line = line.strip()

            # NAME: "Switch 1", DESCR: "WS-C3850-24P-E"
            # NAME: "StackPort5/2", DESCR: "StackPort5/2"
            # NAME: "Switch 5 - Power Supply A", DESCR: "Switch 5 - Power Supply A"
            # NAME: "subslot 0/0 transceiver 2", DESCR: "GE T"
            # NAME: "NIM subslot 0/0", DESCR: "Front Panel 3 ports Gigabitethernet Module"
            # NAME: "Modem 0 on Cellular0/2/0", DESCR: "Sierra Wireless EM7455/EM7430"
            # NAME: "1", DESCR: "WS-C3560CX-12PC-S"
            m = p1.match(line)

            if m:
                group = m.groupdict()
                name = group["name"].strip()
                descr = group["descr"].strip()

                if 'xx Stack' in name:
                    main_dict = ret_dict.setdefault('main', {})
                    main_dict['swstack'] = True

                # ------------------------------------------------------------------
                # Define slot_dict
                # ------------------------------------------------------------------

                # Switch 1
                m1_1 = p1_1.match(name)
                if m1_1 and "Chassis" not in name:
                    slot = m1_1.groupdict()["slot"]
                    # Create slot_dict
                    slot_dict = ret_dict.setdefault("slot", {}).setdefault(slot, {})

                # ------------------------------------------------------------------
                # Define subslot
                # ------------------------------------------------------------------

                # Power Supply Module 0
                # Switch 1 - Power Supply B
                m1_2 = p1_2.match(name)
                if m1_2:
                    slot = m1_2.groupdict()["slot"]
                    subslot = m1_2.groupdict()["subslot"]

                    if slot is None:
                        slot = f"P{subslot}"

                    # Create slot_dict
                    slot_dict = ret_dict.setdefault("slot", {}).setdefault(slot, {})

                m = (
                    # SPA subslot 0/0
                    # IM subslot 0/1
                    # NIM subslot 0/0
                    p1_3.match(name)
                    # subslot 0/0 transceiver 0
                    or p1_4.match(name)
                    # StackPort1/1
                    or p1_5.match(name)
                    # Modem 0 on Cellular0/2/0
                    or p1_7.match(name)
                    # Switch 1 FRU Uplink Module 1
                    or p1_10.match(name)
                )
                if m:
                    group = m.groupdict()
                    slot = group["slot"]
                    subslot = group["subslot"]
                    # Creat slot_dict
                    slot_dict = ret_dict.setdefault("slot", {}).setdefault(slot, {})
                else:
                    subslot = None

                # Fan Tray
                m1_6 = p1_6.match(name)
                if m1_6:
                    slot = name.replace(" ", "_")
                    # Create slot_dict
                    slot_dict = ret_dict.setdefault("slot", {}).setdefault(slot, {})

                # Slot 2 Linecard
                # Slot 3 Supervisor
                m1_8 = p1_8.match(name)
                if m1_8:
                    slot = name.replace(" ", "_")
                    # Create slot_dict
                    slot_dict = ret_dict.setdefault("slot", {}).setdefault(slot, {})
                    continue

                # Supervisor
                m1_9 = p1_9.match(name)
                if m1_9:
                    slot = '1'
                    slot_dict = ret_dict.setdefault("slot", {}).setdefault(slot, {})

                # go to next line
                continue

            # PID: ASR-920-24SZ-IM   , VID: V01  , SN: CAT1902V19M
            # PID: SFP-10G-LR        , VID: CSCO , SN: CD180456291
            # PID: A900-IMA3G-IMSG   , VID: V01  , SN: FOC2204PAP1
            # PID: SFP-GE-T          , VID: V02  , SN: MTC2139029X
            # PID: ISR4331-3x1GE     , VID: V01  , SN:
            # PID: ISR4331/K9        , VID:      , SN: FDO21520TGH
            # PID: ISR4331/K9        , VID:      , SN:
            # PID: EM7455/EM7430     , VID: 1.0  , SN: 355813070074072
            # PID: WS-C3560CX-12PC-S , VID: V03  , SN: FOC2419L9KY
            # PID: C9300-24U         , VID: V02  , SN: FJC2309S08T
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group.get("pid"):
                    pid = group["pid"].strip(" ")
                else:
                    pid = ""
                vid = group["vid"] or ""
                sn = group["sn"] or ""

                # NAME: "Chassis", DESCR: "Cisco ASR1006 Chassis"
                # NAME: "c93xx Stack", DESCR: "c93xx Stack"
                # NAME: "Switch 1 Chassis", DESCR: "Cisco C9550-48L4CD Chassis"
                # NAME: "Switch 2 Chassis", DESCR: "Cisco C9550-48L4CD Chassis"
                if "Chassis" in name or 'xx Stack' in name:
                    sw_match = re.match(r"^Switch\s+(?P<sid>\d+)", name)
                    key = f"switch_{sw_match.group('sid')}" if sw_match else pid
                    main_dict = (
                        ret_dict.setdefault("main", {})
                        .setdefault("chassis", {})
                        .setdefault(key, {})
                    )
                    main_dict["name"] = name
                    main_dict["descr"] = descr
                    main_dict["pid"] = pid
                    main_dict["vid"] = vid
                    main_dict["sn"] = sn
                    continue

                if "Supervisor" in name:
                    # NAME: "Switch 1 Slot 1 Supervisor"
                    # NAME: "Switch 2 Slot 1 Supervisor"
                    sw_match = re.match(r"^Switch\s+(?P<sid>\d+)", name)
                    key = f"switch_{sw_match.group('sid')}" if sw_match else pid
                    main_dict = (
                        ret_dict.setdefault("main", {})
                        .setdefault("supervisor", {})
                        .setdefault(key, {})
                    )
                    main_dict["name"] = name
                    main_dict["descr"] = descr
                    main_dict["pid"] = pid
                    main_dict["vid"] = vid
                    main_dict["sn"] = sn
                    continue

                if "Expansion Module" in name:
                    main_dict = (
                        ret_dict.setdefault("main", {})
                        .setdefault("expansion_module", {})
                        .setdefault(pid, {})
                    )
                    main_dict["name"] = name
                    main_dict["descr"] = descr
                    main_dict["pid"] = pid
                    main_dict["vid"] = vid
                    main_dict["sn"] = sn
                    continue

                if "cpu" in name or "usb" in name:
                    main_dict = (
                        ret_dict.setdefault("main", {})
                        .setdefault(name, {})
                        .setdefault(pid, {})
                    )
                    main_dict["name"] = name
                    main_dict["descr"] = descr
                    main_dict["pid"] = pid
                    main_dict["vid"] = vid
                    main_dict["sn"] = sn
                    continue

                interface_names = INTERFACE_ABBREVIATION_MAPPING_TABLE['generic'].values()

                # try to convert the interface name
                # e.g. Fo1/1/1 -> FortyGigabitEthernet
                try:
                    iface_name = Common.convert_intf_name(name)
                except Exception:
                    iface_name = None

                # slot_dict may still be unset if no slot-defining inventory
                # name preceded this pluggable entry; skip rather than raise
                # UnboundLocalError.
                if iface_name and slot_dict is not None:
                    for interface in interface_names:
                        if interface in iface_name:
                            other_dict = (
                                slot_dict.setdefault("pluggable", {})
                                .setdefault(name, {})
                            )
                            other_dict["name"] = iface_name
                            other_dict["descr"] = descr
                            other_dict["pid"] = pid
                            other_dict["vid"] = vid
                            other_dict["sn"] = sn
                            break

                    # if we matched an interface name, continue to next line
                    if interface in iface_name:
                        continue

                # PID: STACK-T1-50CM     , VID: V01  , SN: LCC1921G250
                if "STACK" in pid:
                    main_dict = ret_dict.setdefault("main", {})
                    main_dict["swstack"] = True

                if ("ASR-9") in pid and ("PWR" not in pid) and ("FAN" not in pid):
                    rp_dict = (
                        ret_dict.setdefault("slot", {})
                        .setdefault("0", {})
                        .setdefault("rp", {})
                        .setdefault(pid, {})
                    )
                    rp_dict["name"] = name
                    rp_dict["descr"] = descr
                    rp_dict["pid"] = pid
                    rp_dict["vid"] = vid
                    rp_dict["sn"] = sn
                    asr900_rp = True

                # Ensure name, slot have been previously parsed
                if not name or not slot:
                    continue

                # NAME: "Switch 1 FRU Uplink Module 1", DESCR: "8x10G Uplink Module"
                # PID: C9300-NM-8X       , VID: V03  , SN: FJZ27110T4E
                if 'Uplink Module' in name:
                    if subslot is not None:
                        lc_dict = slot_dict.setdefault("lc", {}).setdefault(pid, {}).\
                            setdefault('subslot', {}).setdefault(subslot, {}).setdefault(pid, {})
                    else:
                        lc_dict = slot_dict.setdefault("lc", {}).setdefault(pid, {})
                    lc_dict["name"] = name
                    lc_dict["descr"] = descr
                    lc_dict["pid"] = pid
                    lc_dict["vid"] = vid
                    lc_dict["sn"] = sn
                    continue

                # PID: ASR1000-RP2       , VID: V02  , SN: JAE153408NJ
                # PID: ASR1000-RP2       , VID: V03  , SN: JAE1703094H
                # PID: WS-C3850-24P-E    , VID: V01  , SN: FCW1932D0LB
                if ("RP" in pid) or ("WS-C" in pid) or ("R" in name) or p1_1.search(name):
                    rp_dict = slot_dict.setdefault("rp", {}).setdefault(pid, {})
                    rp_dict["name"] = name
                    rp_dict["descr"] = descr
                    rp_dict["pid"] = pid
                    rp_dict["vid"] = vid
                    rp_dict["sn"] = sn
                    continue

                if "ESP" in pid:
                    rp_dict = slot_dict.setdefault("sp", {}).setdefault(pid, {})
                    rp_dict["name"] = name
                    rp_dict["descr"] = descr
                    rp_dict["pid"] = pid
                    rp_dict["vid"] = vid
                    rp_dict["sn"] = sn

                # PID: ASR1000-SIP40     , VID: V02  , SN: JAE200609WP
                # PID: ISR4331/K9        , VID:      , SN: FDO21520TGH
                # PID: ASR1002-X         , VID: V07, SN: FOX1111P1M1
                # PID: ASR1002-HX        , VID:      , SN:
                elif (
                    ("SIP" in pid)
                    or ("-X" in pid)
                    or ("-HX" in pid)
                    or ("-LC" in pid)
                    or ("module" in name and not ("module F" in name))
                ) and ("subslot" not in name):

                    lc_dict = slot_dict.setdefault("lc", {}).setdefault(pid, {})
                    lc_dict["name"] = name
                    lc_dict["descr"] = descr
                    lc_dict["pid"] = pid
                    lc_dict["vid"] = vid
                    lc_dict["sn"] = sn

                # PID: SP7041-E          , VID: E    , SN: MTC164204VE
                # PID: SFP-GE-T          , VID: V02  , SN: MTC2139029X
                # PID: EM7455/EM7430     , VID: 1.0  , SN: 355813070074072
                elif subslot:
                    if "STACK" in pid:
                        try:
                            rp_dict
                        except NameError:
                            stack_dict = slot_dict.setdefault("other", {}).setdefault(
                                pid, {}
                            )
                            subslot_dict = (
                                stack_dict.setdefault("subslot", {})
                                .setdefault(subslot, {})
                                .setdefault(pid, {})
                            )
                        else:
                            subslot_dict = (
                                rp_dict.setdefault("subslot", {})
                                .setdefault(subslot, {})
                                .setdefault(pid, {})
                            )

                    elif asr900_rp:
                        subslot_dict = (
                            rp_dict.setdefault("subslot", {})
                            .setdefault(subslot, {})
                            .setdefault(pid, {})
                        )
                    elif 'Power' in name:
                        subslot_dict = (
                            slot_dict.setdefault("other", {}).setdefault(pid, {})
                            .setdefault('subslot', {})
                            .setdefault(subslot, {})
                            .setdefault(pid, {})
                        )
                    else:
                        if "lc" not in slot_dict:
                            lc_dict = slot_dict.setdefault("lc", {}).setdefault(pid, {})
                        subslot_dict = (
                            lc_dict.setdefault("subslot", {})
                            .setdefault(subslot, {})
                            .setdefault(pid, {})
                        )
                    subslot_dict["name"] = name
                    subslot_dict["descr"] = descr
                    subslot_dict["pid"] = pid
                    subslot_dict["vid"] = vid
                    subslot_dict["sn"] = sn

                # PID: ASR1006-PWR-AC    , VID: V01  , SN: ART1210Q049
                # PID: ASR1006-PWR-AC    , VID: V01  , SN: ART1210Q04C
                # PID: ASR-920-FAN-M     , VID: V01  , SN: CAT1903V028
                else:
                    other_dict = slot_dict.setdefault("other", {}).setdefault(pid, {})
                    other_dict["name"] = name
                    other_dict["descr"] = descr
                    other_dict["pid"] = pid
                    other_dict["vid"] = vid
                    other_dict["sn"] = sn

                # Reset to avoid overwrite
                name = descr = slot = subslot = ""
                continue

        return ret_dict


# =====================
# Schema for:
#   * 'show platform'
# =====================
class ShowPlatformSchema(MetaParser):
    """Schema for show platform"""

    schema = {
        Optional("main"): {
            Optional("switch_mac_address"): str,
            Optional("mac_persistency_wait_time"): str,
            Optional("chassis"): str,
            Optional("swstack"): bool,
        },
        "slot": {
            Any(): {
                Optional("rp"): {
                    Any(): {
                        Optional("sn"): str,
                        Optional("state"): str,
                        Optional("num_of_ports"): str,
                        Optional("mac_address"): str,
                        Optional("hw_ver"): str,
                        Optional("sw_ver"): str,
                        Optional("swstack_role"): str,
                        Optional("swstack_priority"): str,
                        Optional("ports"): str,
                        Optional("role"): str,
                        Optional("name"): str,
                        Optional("slot"): str,
                        Optional("priority"): str,
                        Optional("insert_time"): str,
                        Optional("fw_ver"): str,
                        Optional("cpld_ver"): str,
                    }
                },
                Optional("lc"): {
                    Any(): {
                        Optional("cpld_ver"): str,
                        Optional("fw_ver"): str,
                        Optional("insert_time"): str,
                        Optional("name"): str,
                        Optional("slot"): str,
                        Optional("state"): str,
                        Optional("subslot"): {
                            Any(): {
                                Any(): {
                                    Optional("insert_time"): str,
                                    Optional("name"): str,
                                    Optional("state"): str,
                                    Optional("subslot"): str,
                                }
                            }
                        },
                    }
                },
                Optional("sp"): {
                    Any(): {
                        Optional("cpld_ver"): str,
                        Optional("fw_ver"): str,
                        Optional("insert_time"): str,
                        Optional("name"): str,
                        Optional("slot"): str,
                        Optional("state"): str,
                    }
                },
                Optional("other"): {
                    Any(): {
                        Optional("cpld_ver"): str,
                        Optional("sn"): str,
                        Optional("fw_ver"): str,
                        Optional("insert_time"): str,
                        Optional("name"): str,
                        Optional("mac_address"): str,
                        Optional("hw_ver"): str,
                        Optional("sw_ver"): str,
                        Optional("slot"): str,
                        Optional("ports"): str,
                        Optional("state"): str,
                        Optional("subslot"): {
                            Any(): {
                                Any(): {
                                    Optional("insert_time"): str,
                                    Optional("name"): str,
                                    Optional("state"): str,
                                    Optional("subslot"): str,
                                }
                            }
                        },
                    }
                },
            }
        },
    }


# =====================
# Parser for:
#   * 'show platofrm'
# =====================
class ShowPlatform(ShowPlatformSchema):
    """Parser for show platform
    parser class - implements detail parsing mechanisms for cli output.
    """

    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = "show platform"
    exclude = ["insert_time"]

    def cli(self, output=None):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        platform_dict = {}
        sub_dict = {}

        # ----------      C3850    -------------

        # Switch/Stack Mac Address : 0057.d2ff.e71b - Local Mac Address
        p1 = re.compile(
            r"^[Ss]witch\/[Ss]tack +[Mm]ac +[Aa]ddress +\: +"
            r"(?P<switch_mac_address>[\w\.]+) *(?P<local>[\w\s\-]+)?$"
        )

        # Mac persistency wait time: Indefinite
        p2 = re.compile(
            r"^[Mm]ac +persistency +wait +time\: +(?P<mac_persistency_wait_time>[\w\.\:]+)$"
        )

        # Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver.
        # ------  -----   ---------             -----------  --------------  -------       --------
        #  1       32     WS-C3850-24P-E        FCW1947C0HH  0057.d2ff.e71b  V07           16.6.1
        #  1       32     C9200-24P             JAD2310213C  dc8c.37ff.ad21  V01           17.05.01
        #  1       32     C9200-24P             JAD2310213C  dc8c.37ff.ad21  V01           2021-03-03_18.
        #  1       24     N/A                   N/A          0ccf.1ab0.0000  N/A           N/A 
        p3 = re.compile(
            r"^(?P<switch>\d+) +(?P<ports>\d+) +(?P<model>[\w\-\/]+) +(?P<serial_no>[\w\/]+) +(?P<mac_address>[\w\.\:]+) +(?P<hw_ver>[\w+\/]+) +(?P<sw_ver>[\s\S]+)$"
        )

        #                                     Current
        # Switch#   Role        Priority      State
        # -------------------------------------------
        # *1       Active          3          Ready
        p4 = re.compile(
            r"^\*?(?P<switch>\d+) +(?P<role>\w+) +"
            r"(?P<priority>\d+) +(?P<state>[\w\s]+)$"
        )

        # ----------      ASR1K    -------------
        # Chassis type: ASR1006
        # Chassis type: ASR-903
        p5 = re.compile(r"^[Cc]hassis +type: +(?P<chassis>\S+)$")

        # Slot      Type                State                 Insert time (ago)
        # --------- ------------------- --------------------- -----------------
        # 0         ASR1000-SIP40       ok                    00:33:53
        # 0/0       SPA-1XCHSTM1/OC3    ok                    2d00h
        # F0                            ok, active            00:09:23
        # P1        Unknown             N/A                   never
        # 1/0       SM-X-E2-20UXF       admin down            00:00:03
        # F0        C8500-20X6C         init, active          00:01:37
        #  0/3      A900-IMA16D         out of service        never
        p6 = re.compile(
            r"^(?P<slot>[\w]+)(\/)?(?P<subslot>\d+)?\s*(?P<name>[\w\-_+\/]+)?\s*"
            r"(?P<state>(ok|unknown|admin down|ok, active|N\/A|ok, standby|init, active|out of service"
            r"|ps, fail|empty|incompatible|inserted|fail|disabled|booting|init, standby))\s*"
            r"(?P<insert_time>([\w\.\:]+|N\/A))$"
        )

        # 4                             unknown               2d00h
        p6_1 = re.compile(
            r"^(?P<slot>\w+) +(?P<state>\w+(\, \w+)?) +(?P<insert_time>[\w\.\:]+)$"
        )

        # This is a sub parser for the Type / PID
        # ASR1000-SIP40
        # ASR1000-ESP200
        # ASR1000-MIP100
        p6_2 = re.compile(r"^ASR\d+-(\d+T\S+|SIP\d+|MIP\d+|ESP|X)|ISR|C9|C82|C83")

        # Slot      CPLD Version        Firmware Version
        # --------- ------------------- ---------------------------------------
        # 0         00200800            16.2(1r)
        p7 = re.compile(
            r"^(?P<slot>\w+) +(?P<cpld_version>\d+|N\/A) +(?P<fireware_ver>[\w\.\(\)\/]+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # Switch/Stack Mac Address : 0057.d2ff.e71b - Local Mac Address
            m = p1.match(line)
            if m:
                if "main" not in platform_dict:
                    platform_dict["main"] = {}
                platform_dict["main"]["switch_mac_address"] = m.groupdict()[
                    "switch_mac_address"
                ]
                platform_dict["main"]["swstack"] = True
                continue

            # Mac persistency wait time: Indefinite
            m = p2.match(line)
            if m:
                if "main" not in platform_dict:
                    platform_dict["main"] = {}
                platform_dict["main"]["mac_persistency_wait_time"] = m.groupdict()[
                    "mac_persistency_wait_time"
                ].lower()
                continue

            # Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver.
            # ------  -----   ---------             -----------  --------------  -------       --------
            #  1       32     WS-C3850-24P-E        FCW1947C0HH  0057.d2ff.e71b  V07           16.6.1
            #  1       32     C9200-24P             JAD2310213C  dc8c.37ff.ad21  V01           17.05.01
            #  1       32     C9200-24P             JAD2310213C  dc8c.37ff.ad21  V01           2021-03-03_18.
            m = p3.match(line)
            if m:
                slot = m.groupdict()["switch"]
                model = m.groupdict()["model"]
                if "slot" not in platform_dict:
                    platform_dict["slot"] = {}
                if slot not in platform_dict["slot"]:
                    platform_dict["slot"][slot] = {}

                if (
                    "WS-C" in model
                    or "C9500" in model
                    or "C9300" in model
                    or "C9200" in model
                    or "IE-32" in model
                    or "IE-33" in model
                    or "IE-34" in model
                    or "IE-35" in model
                    or "IE-93" in model
                    or "IE-31" in model
                    or "1783" in model
                    or "C9350" in model
                ):
                    lc_type = "rp"
                else:
                    lc_type = "other"

                if lc_type not in platform_dict["slot"][slot]:
                    platform_dict["slot"][slot][lc_type] = {}
                if model not in platform_dict["slot"][slot][lc_type]:
                    platform_dict["slot"][slot][lc_type][model] = {}
                platform_dict["slot"][slot][lc_type][model]["hw_ver"] = m.groupdict()[
                    "hw_ver"
                ]
                platform_dict["slot"][slot][lc_type][model][
                    "mac_address"
                ] = m.groupdict()["mac_address"]
                platform_dict["slot"][slot][lc_type][model]["name"] = model
                platform_dict["slot"][slot][lc_type][model]["ports"] = m.groupdict()[
                    "ports"
                ]
                platform_dict["slot"][slot][lc_type][model]["slot"] = slot
                platform_dict["slot"][slot][lc_type][model]["sn"] = m.groupdict()[
                    "serial_no"
                ]
                platform_dict["slot"][slot][lc_type][model]["sw_ver"] = m.groupdict()[
                    "sw_ver"
                ]
                continue

            #                                     Current
            # Switch#   Role        Priority      State
            # -------------------------------------------
            # *1       Active          3          Ready
            m = p4.match(line)
            if m:
                slot = m.groupdict()["switch"]
                if "slot" not in platform_dict:
                    continue
                if slot not in platform_dict["slot"]:
                    continue

                for key, value in platform_dict["slot"][slot].items():
                    for key, last in value.items():
                        last["swstack_priority"] = m.groupdict()["priority"]
                        last["swstack_role"] = m.groupdict()["role"]
                        last["state"] = m.groupdict()["state"]
                continue

            # Chassis type: ASR1006
            # Chassis type: ASR-903
            m = p5.match(line)
            if m:
                if "main" not in platform_dict:
                    platform_dict["main"] = {}
                platform_dict["main"]["chassis"] = m.groupdict()["chassis"]
                continue

            # Slot      Type                State                 Insert time (ago)
            # --------- ------------------- --------------------- -----------------
            # 0         ASR1000-SIP40       ok                    00:33:53
            #  0/0      SPA-1XCHSTM1/OC3    ok                    2d00h
            # 0         C8200-1N-4T         ok                    00:32:26
            #  0/3      A900-IMA16D         out of service        never
            m = p6.match(line)
            if m:
                slot = m.groupdict()["slot"]
                subslot = m.groupdict()["subslot"]
                name = m.groupdict()["name"]
                if name:

                    # subslot
                    if subslot:
                        try:
                            # no-slot-type output:
                            # Slot      Type                State                 Insert time (ago)

                            # --------- ------------------- --------------------- -----------------

                            # 0/2      A900-IMA8Z          ok                    1w4d

                            if "slot" not in platform_dict:
                                platform_dict["slot"] = {}
                            if slot not in platform_dict["slot"]:
                                platform_dict["slot"][slot] = {}
                            # if slot not in platform_dict['slot']:
                            #     continue

                            slot_items = platform_dict["slot"][slot].items()

                            # for no-slot-type output
                            if not slot_items:
                                if p6_2.match(name):
                                    if "R" in slot:
                                        lc_type = "rp"
                                    elif re.match(r"^\d+", slot):
                                        lc_type = "lc"
                                    elif re.match(r"^F\d+", slot):
                                        lc_type = "sp"
                                    else:
                                        lc_type = "other"
                                elif re.match(r"^ASR\d+-RP\d+", name):
                                    lc_type = "rp"
                                elif re.match(r"^CSR\d+V", name):
                                    if "R" in slot:
                                        lc_type = "rp"
                                    else:
                                        lc_type = "other"
                                else:
                                    lc_type = "other"

                                if lc_type not in platform_dict["slot"][slot]:
                                    platform_dict["slot"][slot][lc_type] = {}

                                if name not in platform_dict["slot"][slot][lc_type]:
                                    platform_dict["slot"][slot][lc_type][name] = {}
                                sub_dict = platform_dict["slot"][slot][lc_type][name]
                                sub_dict["slot"] = slot

                            # Add subslot
                            for key, value in slot_items:
                                for key, last in value.items():
                                    if "subslot" not in last:
                                        last["subslot"] = {}
                                    if subslot not in last["subslot"]:
                                        last["subslot"][subslot] = {}
                                    if name not in last["subslot"][subslot]:
                                        last["subslot"][subslot][name] = {}
                                    sub_dict = last["subslot"][subslot][name]
                            sub_dict["subslot"] = subslot

                        # KeyError: 'slot'
                        except Exception:
                            continue
                    else:
                        if "slot" not in platform_dict:
                            platform_dict["slot"] = {}
                        if slot not in platform_dict["slot"]:
                            platform_dict["slot"][slot] = {}
                        if p6_2.match(name):
                            if "R" in slot:
                                lc_type = "rp"
                            elif re.match(r"^\d+", slot):
                                lc_type = "lc"
                            elif re.match(r"^F\d+", slot):
                                lc_type = "sp"
                            else:
                                lc_type = "other"
                        elif re.match(r"^ASR\d+-RP\d+", name):
                            lc_type = "rp"
                        elif re.match(r"^CSR\d+V", name):
                            if "R" in slot:
                                lc_type = "rp"
                            else:
                                lc_type = "other"
                        else:
                            lc_type = "other"

                        if lc_type not in platform_dict["slot"][slot]:
                            platform_dict["slot"][slot][lc_type] = {}

                        if name not in platform_dict["slot"][slot][lc_type]:
                            platform_dict["slot"][slot][lc_type][name] = {}
                        sub_dict = platform_dict["slot"][slot][lc_type][name]
                        sub_dict["slot"] = slot

                    sub_dict["name"] = name
                    sub_dict["state"] = m.groupdict()["state"].strip()
                    sub_dict["insert_time"] = m.groupdict()["insert_time"]
                    continue

            # Slot      CPLD Version        Firmware Version
            # --------- ------------------- ---------------------------------------
            # 0         00200800            16.2(1r)
            m = p7.match(line)
            if m:
                fw_ver = m.groupdict()["fireware_ver"]
                cpld_ver = m.groupdict()["cpld_version"]
                slot = m.groupdict()["slot"]

                if "slot" not in platform_dict:
                    continue
                if slot not in platform_dict["slot"]:
                    continue

                for key, value in platform_dict["slot"][slot].items():
                    for key, last in value.items():
                        last["cpld_ver"] = m.groupdict()["cpld_version"]
                        last["fw_ver"] = m.groupdict()["fireware_ver"]
                continue

            # 4                             unknown               2d00h
            m = p6_1.match(line)
            if m:
                slot = m.groupdict()["slot"]
                if "slot" not in platform_dict:
                    platform_dict["slot"] = {}
                if slot not in platform_dict["slot"]:
                    platform_dict["slot"][slot] = {}

                if "other" not in platform_dict["slot"][slot]:
                    platform_dict["slot"][slot]["other"] = {}
                    platform_dict["slot"][slot]["other"][""] = {}
                platform_dict["slot"][slot]["other"][""]["slot"] = slot
                platform_dict["slot"][slot]["other"][""]["name"] = ""
                platform_dict["slot"][slot]["other"][""]["state"] = m.groupdict()[
                    "state"
                ]
                platform_dict["slot"][slot]["other"][""]["insert_time"] = m.groupdict()[
                    "insert_time"
                ]
                continue

        return platform_dict

class ShowPlatformHostAccessTableIntfSchema(MetaParser):
    """Schema for show platform host-access-table <intf>"""

    schema = {
        'current_feature': str,
        'default': str,
        Optional('vlan'): {
            int: ListOf({
                'src_address': str,
                'access_mode': str,
                'feature': str,
                'type': str,
            }),
        },
    }

class ShowPlatformHostAccessTableIntf(ShowPlatformHostAccessTableIntfSchema):
    """Parser for show platform host-access-table <intf>"""

    cli_command = 'show platform host-access-table {intf}'

    def cli(self, intf=None, output=None):
        if output is None:
            cmd = self.cli_command.format(intf=intf)
            output = self.device.execute(cmd)

        # 001b.0c18.918d       100         permit         dot1x        dynamic
        p1 = re.compile(r"^(?P<src_address>\S+)\s+(?P<vlan_id>\d+)\s+(?P<access_mode>\w+)\s+(?P<feature>\S+)\s+(?P<type>\w+)$")
        
        # Current feature:  dot1x
        p2 = re.compile(r"^Current\s+feature:\s+(?P<current_feature>\S+)$")

        # Default            ask
        p3 = re.compile(r"^Default\s+(?P<default>\w+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 001b.0c18.918d       100         permit         dot1x        dynamic
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan_dict = ret_dict.setdefault('vlan', {}).setdefault(int(group['vlan_id']), [])
                vlan_dict.append({
                    'src_address': group['src_address'],
                    'access_mode': group['access_mode'],
                    'feature': group['feature'],
                    'type': group['type']
                })
                continue

            # Current feature:  dot1x
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['current_feature'] = group['current_feature']
                continue

            # Default            ask
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['default'] = group['default']
                continue

        return ret_dict

class ShowPlatformSoftwareInfrastructureThreadFastpathSchema(MetaParser):
    """Schema for show platform software infrastructure thread fastpath"""
    schema = {
        "syspage_index": int,
        "packet_stats": {
            "min_packet_received": int,
            "max_packet_received": int
        },
        "message_stats": {
            "min_message_sent": int,
            "max_message_sent": int,
            "total_message_received": int,
            "total_message_sent": int
        },
        "runtime_stats": {
            "min_clock_runtime_msec": int,
            "max_clock_runtime_msec": int,
            "min_cpu_runtime_msec": int,
            "max_cpu_runtime_msec": int
        },
        "fastpath_stats": {
            "fastpath_invocation": int,
            "epoll_timeout": int,
            "epoll_intr": int,
            "fastpath_triggered_by_ios": int,
            "wakeup": int,
            "fastpath_top_epoll_error": int,
            "second_level_epoll_error": int,
            "special_ipc_request": int
        },
        "file_descriptors": {
            "mstr_efd": int,
            "fastpath_wakeup_fd": int,
            "rd_efd": {
                "fd": int,
                "epoll_add_failed": int,
                "epoll_del_failed": int
            },
            "rd_hdlr_efd": {
                "fd": int,
                "epoll_add_failed": int,
                "epoll_del_failed": int
            },
            "wr_efd": {
                "fd": int,
                "epoll_add_failed": int,
                "epoll_del_failed": int
            }
        },
        "event_stats": {
            "wakeup_efd_ready": int,
            "rd_efd_ready": int,
            "rd_efd_processed": int,
            "rd_hdlr_efd_ready": int,
            "rd_hdlr_efd_processed": int,
            "wr_efd_ready": int,
            "wr_efd_processed": int
        },
        "ios_stats": {
            "ios_triggered_by_fastpath": int,
            "ios_triggered_by_packet": int,
            "ios_scheduler_wakeup": int
        },
        "data_path_stats": {
            "console_data_path_invocation": int,
            "stdout_data_path_invocation": int,
            "chasfs_process_thread_event": int,
            "tipc_process_thread_event": int
        },
        "memory_stats": {
            "memory_allocation_failures": int,
            "read_paused": int,
            "read_pause_cleared": int,
            "read_disabled": int,
            "read_disable_cleared": int
        },
        "current_state": {
            "read_paused": str,
            "read_disabled": str
        },
        "utilization": {
            "5_seconds": {
                "clock_percent": int,
                "cpu_percent": int
            },
            "1_min": {
                "clock_percent": int,
                "cpu_percent": int
            },
            "5_min": {
                "clock_percent": int,
                "cpu_percent": int
            }
        },
        "mutex_stats": {
            "max_acquire_time_msec": int,
            "timestamp": str
        }
    }


class ShowPlatformSoftwareInfrastructureThreadFastpath(ShowPlatformSoftwareInfrastructureThreadFastpathSchema):
    """Parser for show platform software infrastructure thread fastpath"""
    cli_command = "show platform software infrastructure thread fastpath"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Syspage index for the Fastpath thread: 6
        p1 = re.compile(r"^\s*Syspage index for the Fastpath thread\s*:\s*(?P<idx>\d+)$")

        # 1 minimum packet received, 216 maximum packet received
        p2 = re.compile(r"^\s*(?P<min>\d+)\s+minimum packet received,\s+(?P<max>\d+)\s+maximum packet received$")

        # 1 minimum message sent, 1 maximum message sent
        p3 = re.compile(r"^\s*(?P<min>\d+)\s+minimum message sent,\s+(?P<max>\d+)\s+maximum message sent$")

        # 14458 total message received, 2 total message sent
        p4 = re.compile(r"^\s*(?P<recv>\d+)\s+total message received,\s+(?P<sent>\d+)\s+total message sent$")

        # 0 msec minimum clock runtime, 5 msec maximum clock runtime
        p5 = re.compile(r"^\s*(?P<min>\d+)\s+msec minimum clock runtime,\s+(?P<max>\d+)\s+msec maximum clock runtime$")

        # 0 msec minimum cpu runtime, 5 msec maximum cpu runtime
        p6 = re.compile(r"^\s*(?P<min>\d+)\s+msec minimum cpu runtime,\s+(?P<max>\d+)\s+msec maximum cpu runtime$")

        # 20413 fastpath invocation, 9062 epoll timeout, 0 epoll intr
        p7 = re.compile(r"^\s*(?P<inv>\d+)\s+fastpath invocation,\s+(?P<timeout>\d+)\s+epoll timeout,\s+(?P<intr>\d+)\s+epoll intr$")

        # 48 fastpath triggered by IOS thread, 13 wakeup
        p8 = re.compile(r"^\s*(?P<trig>\d+)\s+fastpath triggered by IOS thread,\s+(?P<wakeup>\d+)\s+wakeup$")

        # 0 fastpath top epoll error, 0 second level epoll error
        p9 = re.compile(r"^\s*(?P<top>\d+)\s+fastpath top epoll error,\s+(?P<second>\d+)\s+second level epoll error$")

        # 0 special IPC request
        p10 = re.compile(r"^\s*(?P<cnt>\d+)\s+special IPC request$")

        # mstr_efd 9, fastpath_wakeup_fd 7
        p11 = re.compile(r"^\s*mstr_efd\s+(?P<mstr>\d+),\s+fastpath_wakeup_fd\s+(?P<wakeup>\d+)$")

        # rd_efd 10 (epoll add failed 0, epoll del failed 0)
        p12 = re.compile(r"^\s*rd_efd\s+(?P<fd>\d+)\s+\(epoll add failed\s+(?P<add>\d+),\s+epoll del failed\s+(?P<del>\d+)\)$")

        # rd_hdlr_efd 11 (epoll add failed 0, epoll del failed 0)
        p13 = re.compile(r"^\s*rd_hdlr_efd\s+(?P<fd>\d+)\s+\(epoll add failed\s+(?P<add>\d+),\s+epoll del failed\s+(?P<del>\d+)\)$")

        # wr_efd 12 (epoll add failed 0, epoll del failed 0)
        p14 = re.compile(r"^\s*wr_efd\s+(?P<fd>\d+)\s+\(epoll add failed\s+(?P<add>\d+),\s+epoll del failed\s+(?P<del>\d+)\)$")

        # 13 wakeup_efd_ready
        p15 = re.compile(r"^\s*(?P<val>\d+)\s+wakeup_efd_ready$")

        # 7607 rd_efd_ready, 7607 rd_efd_processed
        p16 = re.compile(r"^\s*(?P<ready>\d+)\s+rd_efd_ready,\s+(?P<proc>\d+)\s+rd_efd_processed$")

        # 3738 rd_hdlr_efd_ready, 3738 rd_hdlr_efd_processed
        p17 = re.compile(r"^\s*(?P<ready>\d+)\s+rd_hdlr_efd_ready,\s+(?P<proc>\d+)\s+rd_hdlr_efd_processed$")

        # 2 wr_efd_ready, 2 wr_efd_processed
        p18 = re.compile(r"^\s*(?P<ready>\d+)\s+wr_efd_ready,\s+(?P<proc>\d+)\s+wr_efd_processed$")

        # 15930 IOS triggered by fastpath thread
        p19 = re.compile(r"^\s*(?P<val>\d+)\s+IOS triggered by fastpath thread$")

        # 27691 IOS triggered by packet thread
        p20 = re.compile(r"^\s*(?P<val>\d+)\s+IOS triggered by packet thread$")

        # 43504 IOS scheduler thread wakeup
        p21 = re.compile(r"^\s*(?P<val>\d+)\s+IOS scheduler thread wakeup$")

        # 845 console data path invocation
        p22 = re.compile(r"^\s*(?P<val>\d+)\s+console data path invocation$")

        # 0 stdout data path invocation
        p23 = re.compile(r"^\s*(?P<val>\d+)\s+stdout data path invocation$")

        # 2535 chasfs process thread event invocation
        p24 = re.compile(r"^\s*(?P<val>\d+)\s+chasfs process thread event invocation$")

        # 0 tipc process thread event invocation
        p25 = re.compile(r"^\s*(?P<val>\d+)\s+tipc process thread event invocation$")

        # 0 memory allocation failures, 0 read paused, 0 read pause cleared
        p26 = re.compile(r"^\s*(?P<memfail>\d+)\s+memory allocation failures,\s+(?P<rpaused>\d+)\s+read paused,\s+(?P<rpauseclr>\d+)\s+read pause cleared$")

        # 0 read disabled, 0 read disable cleared
        p27 = re.compile(r"^\s*(?P<rdis>\d+)\s+read disabled,\s+(?P<rdisclr>\d+)\s+read disable cleared$")

        # Current state: read paused: no, read disabled: no
        p28 = re.compile(r"^\s*Current state:\s*read paused:\s*(?P<rpaused>\S+),\s*read disabled:\s*(?P<rdis>\S+)$")

        # Clock/CPU utilization with 5 seconds 0%/0%, 1 min 0%/0%, 5 min 0%/0%
        p29 = re.compile(r"^\s*Clock/CPU utilization with 5 seconds\s+(?P<s5c>\d+)%/(?P<s5u>\d+)%,\s*1 min\s+(?P<m1c>\d+)%/(?P<m1u>\d+)%,\s*5 min\s+(?P<m5c>\d+)%/(?P<m5u>\d+)%$")

        # Maximum mutex acquire time: 11937 msec at *Apr 14 18:15:50.475
        p30 = re.compile(r"^\s*Maximum mutex acquire time\s*:\s*(?P<msec>\d+)\s+msec\s+at\s+(?P<ts>.+)$")

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Syspage index for the Fastpath thread: 6
            m = p1.match(line)
            if m:
                ret_dict["syspage_index"] = int(m.group("idx"))
                continue

            # 1 minimum packet received, 216 maximum packet received
            m = p2.match(line)
            if m:
                pkt = ret_dict.setdefault("packet_stats", {})
                pkt["min_packet_received"] = int(m.group("min"))
                pkt["max_packet_received"] = int(m.group("max"))
                continue

            # 1 minimum message sent, 1 maximum message sent
            m = p3.match(line)
            if m:
                msg = ret_dict.setdefault("message_stats", {})
                msg["min_message_sent"] = int(m.group("min"))
                msg["max_message_sent"] = int(m.group("max"))
                continue

            # 14458 total message received, 2 total message sent
            m = p4.match(line)
            if m:
                msg = ret_dict.setdefault("message_stats", {})
                msg["total_message_received"] = int(m.group("recv"))
                msg["total_message_sent"] = int(m.group("sent"))
                continue

            # 0 msec minimum clock runtime, 5 msec maximum clock runtime
            m = p5.match(line)
            if m:
                run = ret_dict.setdefault("runtime_stats", {})
                run["min_clock_runtime_msec"] = int(m.group("min"))
                run["max_clock_runtime_msec"] = int(m.group("max"))
                continue

            # 0 msec minimum cpu runtime, 5 msec maximum cpu runtime
            m = p6.match(line)
            if m:
                run = ret_dict.setdefault("runtime_stats", {})
                run["min_cpu_runtime_msec"] = int(m.group("min"))
                run["max_cpu_runtime_msec"] = int(m.group("max"))
                continue

            # 20413 fastpath invocation, 9062 epoll timeout, 0 epoll intr
            m = p7.match(line)
            if m:
                fps = ret_dict.setdefault("fastpath_stats", {})
                fps["fastpath_invocation"] = int(m.group("inv"))
                fps["epoll_timeout"] = int(m.group("timeout"))
                fps["epoll_intr"] = int(m.group("intr"))
                continue

            # 48 fastpath triggered by IOS thread, 13 wakeup
            m = p8.match(line)
            if m:
                fps = ret_dict.setdefault("fastpath_stats", {})
                fps["fastpath_triggered_by_ios"] = int(m.group("trig"))
                fps["wakeup"] = int(m.group("wakeup"))
                continue

            # 0 fastpath top epoll error, 0 second level epoll error
            m = p9.match(line)
            if m:
                fps = ret_dict.setdefault("fastpath_stats", {})
                fps["fastpath_top_epoll_error"] = int(m.group("top"))
                fps["second_level_epoll_error"] = int(m.group("second"))
                continue

            # 0 special IPC request
            m = p10.match(line)
            if m:
                fps = ret_dict.setdefault("fastpath_stats", {})
                fps["special_ipc_request"] = int(m.group("cnt"))
                continue

            # mstr_efd 9, fastpath_wakeup_fd 7
            m = p11.match(line)
            if m:
                fds = ret_dict.setdefault("file_descriptors", {})
                fds["mstr_efd"] = int(m.group("mstr"))
                fds["fastpath_wakeup_fd"] = int(m.group("wakeup"))
                continue

            # rd_efd 10 (epoll add failed 0, epoll del failed 0)
            m = p12.match(line)
            if m:
                fds = ret_dict.setdefault("file_descriptors", {})
                rd = fds.setdefault("rd_efd", {})
                rd["fd"] = int(m.group("fd"))
                rd["epoll_add_failed"] = int(m.group("add"))
                rd["epoll_del_failed"] = int(m.group("del"))
                continue

            # rd_hdlr_efd 11 (epoll add failed 0, epoll del failed 0)
            m = p13.match(line)
            if m:
                fds = ret_dict.setdefault("file_descriptors", {})
                rd = fds.setdefault("rd_hdlr_efd", {})
                rd["fd"] = int(m.group("fd"))
                rd["epoll_add_failed"] = int(m.group("add"))
                rd["epoll_del_failed"] = int(m.group("del"))
                continue

            # wr_efd 12 (epoll add failed 0, epoll del failed 0)
            m = p14.match(line)
            if m:
                fds = ret_dict.setdefault("file_descriptors", {})
                wr = fds.setdefault("wr_efd", {})
                wr["fd"] = int(m.group("fd"))
                wr["epoll_add_failed"] = int(m.group("add"))
                wr["epoll_del_failed"] = int(m.group("del"))
                continue

            # 13 wakeup_efd_ready
            m = p15.match(line)
            if m:
                ev = ret_dict.setdefault("event_stats", {})
                ev["wakeup_efd_ready"] = int(m.group("val"))
                continue

            # 7607 rd_efd_ready, 7607 rd_efd_processed
            m = p16.match(line)
            if m:
                ev = ret_dict.setdefault("event_stats", {})
                ev["rd_efd_ready"] = int(m.group("ready"))
                ev["rd_efd_processed"] = int(m.group("proc"))
                continue

            # 3738 rd_hdlr_efd_ready, 3738 rd_hdlr_efd_processed
            m = p17.match(line)
            if m:
                ev = ret_dict.setdefault("event_stats", {})
                ev["rd_hdlr_efd_ready"] = int(m.group("ready"))
                ev["rd_hdlr_efd_processed"] = int(m.group("proc"))
                continue

            # 2 wr_efd_ready, 2 wr_efd_processed
            m = p18.match(line)
            if m:
                ev = ret_dict.setdefault("event_stats", {})
                ev["wr_efd_ready"] = int(m.group("ready"))
                ev["wr_efd_processed"] = int(m.group("proc"))
                continue

            # 15930 IOS triggered by fastpath thread
            m = p19.match(line)
            if m:
                ios = ret_dict.setdefault("ios_stats", {})
                ios["ios_triggered_by_fastpath"] = int(m.group("val"))
                continue

            # 27691 IOS triggered by packet thread
            m = p20.match(line)
            if m:
                ios = ret_dict.setdefault("ios_stats", {})
                ios["ios_triggered_by_packet"] = int(m.group("val"))
                continue

            # 43504 IOS scheduler thread wakeup
            m = p21.match(line)
            if m:
                ios = ret_dict.setdefault("ios_stats", {})
                ios["ios_scheduler_wakeup"] = int(m.group("val"))
                continue

            # 845 console data path invocation
            m = p22.match(line)
            if m:
                dp = ret_dict.setdefault("data_path_stats", {})
                dp["console_data_path_invocation"] = int(m.group("val"))
                continue

            # 0 stdout data path invocation
            m = p23.match(line)
            if m:
                dp = ret_dict.setdefault("data_path_stats", {})
                dp["stdout_data_path_invocation"] = int(m.group("val"))
                continue

            # 2535 chasfs process thread event invocation
            m = p24.match(line)
            if m:
                dp = ret_dict.setdefault("data_path_stats", {})
                dp["chasfs_process_thread_event"] = int(m.group("val"))
                continue

            # 0 tipc process thread event invocation
            m = p25.match(line)
            if m:
                dp = ret_dict.setdefault("data_path_stats", {})
                dp["tipc_process_thread_event"] = int(m.group("val"))
                continue

            # 0 memory allocation failures, 0 read paused, 0 read pause cleared
            m = p26.match(line)
            if m:
                mem = ret_dict.setdefault("memory_stats", {})
                mem["memory_allocation_failures"] = int(m.group("memfail"))
                mem["read_paused"] = int(m.group("rpaused"))
                mem["read_pause_cleared"] = int(m.group("rpauseclr"))
                continue

            # 0 read disabled, 0 read disable cleared
            m = p27.match(line)
            if m:
                mem = ret_dict.setdefault("memory_stats", {})
                mem["read_disabled"] = int(m.group("rdis"))
                mem["read_disable_cleared"] = int(m.group("rdisclr"))
                continue

            # Current state: read paused: no, read disabled: no
            m = p28.match(line)
            if m:
                st = ret_dict.setdefault("current_state", {})
                st["read_paused"] = m.group("rpaused")
                st["read_disabled"] = m.group("rdis")
                continue

            # Clock/CPU utilization with 5 seconds 0%/0%, 1 min 0%/0%, 5 min 0%/0%
            m = p29.match(line)
            if m:
                util = ret_dict.setdefault("utilization", {})
                sec5 = util.setdefault("5_seconds", {})
                sec5["clock_percent"] = int(m.group("s5c"))
                sec5["cpu_percent"] = int(m.group("s5u"))
                min1 = util.setdefault("1_min", {})
                min1["clock_percent"] = int(m.group("m1c"))
                min1["cpu_percent"] = int(m.group("m1u"))
                min5 = util.setdefault("5_min", {})
                min5["clock_percent"] = int(m.group("m5c"))
                min5["cpu_percent"] = int(m.group("m5u"))
                continue

            # Maximum mutex acquire time: 11937 msec at *Apr 14 18:15:50.475
            m = p30.match(line)
            if m:
                mtx = ret_dict.setdefault("mutex_stats", {})
                mtx["max_acquire_time_msec"] = int(m.group("msec"))
                mtx["timestamp"] = m.group("ts")
                continue

        return ret_dict
