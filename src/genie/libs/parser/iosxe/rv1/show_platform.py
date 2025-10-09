""" show_platform.py

IOSXE revision 1 parsers for the following show commands:

    * 'show inventory'
    * 'show platform'
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
        p1_8 = re.compile(r"^Slot \d Linecard|Slot \d Supervisor|Slot \d Router$")

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
                if m1_1:
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
                if "Chassis" in name or 'xx Stack' in name:
                    main_dict = (
                        ret_dict.setdefault("main", {})
                        .setdefault("chassis", {})
                        .setdefault(pid, {})
                    )
                    main_dict["name"] = name
                    main_dict["descr"] = descr
                    main_dict["pid"] = pid
                    main_dict["vid"] = vid
                    main_dict["sn"] = sn
                    continue

                if "Supervisor" in name:
                    main_dict = (
                        ret_dict.setdefault("main", {})
                        .setdefault("supervisor", {})
                        .setdefault(pid, {})
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

                if iface_name:
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