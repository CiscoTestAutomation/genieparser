""" show_platform.py

IOSXE revision 1 parsers for the following show commands:

    * 'show inventory'

"""
import re
import logging

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And
from genie.libs.parser.utils.common import Common, INTERFACE_ABBREVIATION_MAPPING_TABLE

# pyATS
from pyats.utils.exceptions import SchemaTypeError

log = logging.getLogger(__name__)
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
        # NAME: "1", DESCR: "IE-4000-16T4G-E"
        p1 = re.compile(r"^NAME: +\"(?P<name>.*)\"," r" +DESCR: +\"(?P<descr>.*)\"$")

        # Switch 1
        # Switch 1 Chassis
        p1_1 = re.compile(r"^Switch +(?P<slot>\d+)(?: +Chassis)?$")
        # Power Supply Module 0
        # Power Supply Module 1
        # Switch 1 - Power Supply B
        # Switch 2 Power Supply Module 1
        p1_2 =  re.compile(r"^(?:Switch +(?P<switch>\d+) - |Switch +(?P<switch2>\d+) +)?Power Supply (Module )?(?P<subslot>[\d\w]+)$")
        # SPA subslot 0/0
        # IM subslot 0/1
        # NIM subslot 0/0
        p1_3 = re.compile(r"^(SPA|IM|NIM|PVDM) +subslot +(?P<slot>(\d+))/(?P<subslot>(\d+))$")

        # subslot 0/0 transceiver 0
        p1_4 = re.compile(r"^subslot +(?P<slot>(\d+))\/(?P<subslot>(.*))")

        # StackPort1/1
        p1_5 = re.compile(r"^StackPort(?P<slot>(\d+))/(?P<subslot>(\d+))$")

        # Fan Tray
        # Switch 1 Fan Tray
        p1_6 = re.compile(r"^(?:Switch +(?P<switch>\d+) +)?Fan +Tray(?: +(?P<subslot>\d+))?$")

        # Modem 0 on Cellular0/2/0
        p1_7 = re.compile(r"^Modem +(?P<modem>\S+) +on +Cellular(?P<slot>\d+)\/(?P<subslot>.*)$")

        # Slot 2 Linecard
        # Slot 3 Supervisor
        # Switch 1 Slot 2 Linecard
        p1_8 =  re.compile(r"^(?:Switch +(?P<switch>\d+) +)?(?:Slot +)?(?P<slot>\d+)\s*(?P<type>Linecard|Supervisor|Router)$")
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

                if name.isdigit():
                    slot = name
                    slot_dict = ret_dict.setdefault("slot", {}).setdefault(slot, {})
                    continue

                # ------------------------------------------------------------------
                # Define slot_dict
                # ------------------------------------------------------------------

                # Switch 1
                # Switch 1 Chassis
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
                # Switch 2 Power Supply Module 1
                m1_2 = p1_2.match(name)
                if m1_2:
                    group = m1_2.groupdict()
                    # Prefer 'switch' from 'Switch 1 - Power Supply A'
                    slot = group.get("switch") or group.get("switch2")
                    subslot = group["subslot"]

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
                # Switch 2 Fan Tray
                m1_6 = p1_6.match(name)
                if m1_6:
                    slot = name.replace(" ", "_")
                    # Create slot_dict
                    slot_dict = ret_dict.setdefault("slot", {}).setdefault(slot, {})

                # Slot 2 Linecard
                # Slot 3 Supervisor
                m1_8 = p1_8.match(name)
                if m1_8:
                    slot = m1_8.group("slot")
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

                elif name.isdigit():
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
                    slot_dict = ret_dict.setdefault("slot", {}).setdefault(name, {})
                    continue

                if "Supervisor" in name:
                    main_dict = (
                        ret_dict.setdefault("main", {})
                        .setdefault("supervisor", {})
                        .setdefault(slot, {})
                        #.setdefault(pid, {})
                    )
                    main_dict["name"] = name
                    main_dict["descr"] = descr
                    main_dict["pid"] = pid
                    main_dict["vid"] = vid
                    main_dict["sn"] = sn
                    rp_dict = (
                        ret_dict.setdefault("slot", {})
                        .setdefault(slot, {}) 
                        .setdefault("rp", {})
                        .setdefault(pid, {})
                    )
                    rp_dict["name"] = name
                    rp_dict["descr"] = descr
                    rp_dict["pid"] = pid
                    rp_dict["vid"] = vid
                    rp_dict["sn"] = sn
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
    
class ShowEnvironmentAllSchema(MetaParser):
    """Schema for show environment all
                  show environment all | include {include} """

    schema = {
        Optional('critical_alarms'): int,
        Optional('major_alarms'): int,
        Optional('minor_alarms'): int,
        'sensor_list': {
            Any(): {
                'slot': {
                    Any(): {
                        'sensor': {
                            Any(): {
                                'state': str,
                                'reading': str,
                                Optional('threshold'): {
                                    'minor': int,
                                    'major': int,
                                    'critical': int,
                                    'shutdown': int,
                                    'unit': str,
                                }
                            }
                        }
                    }
                }
            }
        },
        'switch': {
            Any(): {
                'power_supply': {
                    'slot': {
                        Any(): {
                            'model_no': str,
                            'type': str,
                            'capacity': str,
                            'status': str,
                            'fan_1_state': str,
                            'fan_2_state': str,
                        }
                    },
                    'current_configuration_mode': str,
                    'current_operating_state': str,
                    'currently_active': int,
                    'currently_available': int,
                },
                'fantray': {
                    'status': str,
                    'power_consumed_by_fantray_watts': int,
                    'fantray_airflow_direction': str,
                    'fantray_beacon_led': str,
                    'fantray_status_led': str,
                    'system': str,
                },
            },
        },
    }


class ShowEnvironmentAll(ShowEnvironmentAllSchema):
    """Parser for show environment all
                  show environment all | include {include}"""

    cli_command = [
        'show environment all', 'show environment all | include {include}'
    ]

    def cli(self, include='', output=None):
        if not output:
            if include:
                cmd = self.cli_command[1].format(include=include)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Number of Critical alarms:  0
        p1 = re.compile(
            r'^Number +of +Critical +alarms: +(?P<critic_alarms>\d+)$')

        # Number of Major alarms:     0
        p2 = re.compile(r'^Number +of +Major +alarms: +(?P<maj_alarms>\d+)$')

        # Number of Minor alarms:     0
        p3 = re.compile(r'^Number +of +Minor +alarms: +(?P<min_alarms>\d+)$')

        # Sensor List:  Environmental Monitoring
        p4 = re.compile(r'Sensor\s+List:\s+(?P<sensor_list>.+)')

        # Sensor           Location          State          Reading           Threshold(Minor,Major,Critical,Shutdown)
        # Temp: Coretemp   Chassis1-R0       Normal            46 Celsius                (107,117,123,125)(Celsius)
        # Temp: UADP       Chassis1-R0       Normal            54 Celsius                (107,117,123,125)(Celsius)
        # V1: VX1          Chassis1-R0       Normal            871 mV                    na
        # V1: VX2          Chassis1-R0       Normal            1498 mV                   na
        # V1: VX3          Chassis1-R0       Normal            1055 mV                   na
        # V1: VX4          Chassis1-R0       Normal            852 mV                    na
        # V1: VX5          Chassis1-R0       Normal            1507 mV                   na
        # V1: VX6          Chassis1-R0       Normal            1301 mV                   na
        # V1: VX7          Chassis1-R0       Normal            1005 mV                   na
        p5 = re.compile(
            r'(?P<sensor_name>\S+(:\s+\S+)?)\s+(?P<slot>\S+[0-9])\s+(?P<state>\S+)\s+(?P<reading>\d+\s+\S+(\s+(AC|DC))?)\s+(\((?P<minor>\d+\s*),(?P<major>\d+\s*),(?P<critical>\d+\s*),(?P<shutdown>\d+\s*)\)\((?P<unit>\S+)\))?'
        )

        # Switch:1
        p6 = re.compile(r'^Switch:(?P<switch>\d+)')

        # Power                                                       Fan States
        # Supply  Model No              Type  Capacity  Status        1     2
        # ------  --------------------  ----  --------  ------------  -----------
        # PS1     C9400-PWR-3200AC      ac    3200 W    active        good  good
        # PS2     C9400-PWR-3200AC      ac    n.a.      faulty        good  good
        p7 = re.compile(
            r'(?P<ps_slot>PS\S+)\s+(?P<model_no>\S+)\s+(?P<type>\S+)\s+(?P<capacity>\S+(\s+\S+)?)\s+(?P<status>\S+)\s+(?P<fan_1_state>\S+)\s+(?P<fan_2_state>\S+)$'
        )

        # PS Current Configuration Mode : Combined
        # PS Current Operating State    : Combined
        # Power supplies currently active    : 1
        # Power supplies currently available : 1
        p8 = re.compile(
            r'(PS|Power supplies)\s+(?P<ps_key>.+)\s+:\s+(?P<ps_value>\S+)')

        # Switch 1:
        p9 = re.compile(r'^Switch +(?P<switch>\d+)')

        # Fantray : good
        # Power consumed by Fantray : 540 Watts
        # Fantray airflow direction : side-to-side
        # Fantray beacon LED: off
        # Fantray status LED: green
        # SYSTEM : GREEN
        p10 = re.compile(
            r'(?P<fantray_key>((.+)?Fantray(.+)?)|SYSTEM)(\s+)?:\s+(?P<fantray_value>(\S+)|(\d+\s+Watts))'
        )

        for line in output.splitlines():
            line = line.strip()

            # Number of Critical alarms:  0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['critical_alarms'] = int(group['critic_alarms'])
                continue

            # Number of Major alarms:     0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['major_alarms'] = int(group['maj_alarms'])
                continue

            # Number of Minor alarms:     0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['minor_alarms'] = int(group['min_alarms'])
                continue

            # Sensor List:  Environmental Monitoring
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sensor_dict = ret_dict.setdefault('sensor_list',
                                                  {}).setdefault(
                                                      group['sensor_list'], {})
                continue

            #  Sensor           Location          State          Reading           Threshold(Minor,Major,Critical,Shutdown)
            #  Temp: Coretemp   R0                Normal            48 Celsius          	(107,117,123,125)(Celsius)
            #  Temp: UADP       R0                Normal            56 Celsius          	(107,117,123,125)(Celsius)
            #  V1: VX1          R0                Normal            869 mV               	na
            #  Temp:    inlet   R0                Normal            32 Celsius          	(56 ,66 ,96 ,98 )(Celsius)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                sensor_name = group.pop('sensor_name')
                slot = group.pop('slot')
                fin_dict = sensor_dict.setdefault('slot', {}).setdefault(slot, {}).\
                    setdefault('sensor', {}).setdefault(sensor_name, {})

                fin_dict['state'] = group['state']
                fin_dict['reading'] = group['reading']
                if group['minor']:
                    fin_dict.setdefault('threshold', {})
                    for key in [
                            'minor', 'major', 'critical', 'shutdown', 'unit'
                    ]:
                        fin_dict['threshold'][key] = int(
                            group[key]) if key != 'unit' else group[key]
                continue

            # Switch:1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                sw_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})

            # Power                                                       Fan States
            # Supply  Model No              Type  Capacity  Status        1     2
            # ------  --------------------  ----  --------  ------------  -----------
            # PS1     C9400-PWR-3200AC      ac    3200 W    active        good  good
            # PS2     C9400-PWR-3200AC      ac    n.a.      faulty        good  good
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ps_slot = group.pop('ps_slot')
                ps_dict = sw_dict.setdefault('power_supply', {})
                ps_slot_dict = ps_dict.setdefault('slot',
                                                  {}).setdefault(ps_slot, {})
                ps_slot_dict.update({k: v for k, v in group.items()})

            # PS Current Configuration Mode : Combined
            # PS Current Operating State    : Combined
            # Power supplies currently active    : 1
            # Power supplies currently available : 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ps_key = group['ps_key'].strip().lower().replace(' ', '_')
                if 'active' in ps_key or 'available' in ps_key:
                    ps_value = int(group['ps_value'])
                else:
                    ps_value = group['ps_value']
                ps_dict.setdefault(ps_key, ps_value)

            # Switch 1:
            m = p9.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                sw_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})

            # Fantray : good
            # Power consumed by Fantray : 540 Watts
            # Fantray airflow direction : side-to-side
            # Fantray beacon LED: off
            # Fantray status LED: green
            # SYSTEM : GREEN
            m = p10.match(line)
            if m:
                group = m.groupdict()
                fantray_key = group['fantray_key'].strip().lower().replace(
                    ' ', '_')
                if 'power_consumed' in fantray_key:
                    fantray_value = int(group['fantray_value'])
                    fantray_key += '_watts'
                else:
                    fantray_value = group['fantray_value']
                if 'fantray' == fantray_key:
                    sw_dict.setdefault('fantray',
                                        {}).setdefault('status', fantray_value)
                else:
                    sw_dict.setdefault('fantray',
                                        {}).setdefault(fantray_key,
                                                       fantray_value)

        return ret_dict
