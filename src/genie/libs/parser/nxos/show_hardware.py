"""NXOS parsers for the following show commands:

    * 'show hardware internal tctrl_usd dpll state'
    * 'show hardware internal errors all'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    ListOf, \
    Optional


class ShowHardwareInternalTctrlUsdDpllStateSchema(MetaParser):
    """Schema for show hardware internal tctrl_usd dpll state"""

    schema = {
        "dpll_hw_state": {
            "inst": {
                Any(): {
                    "dpll": {
                        Any(): {
                            "dpll_mon_status" : str,
                            "lock": str,
                            "ho": str,
                            "step_time_in_progress": str,
                            "flhit": str,
                            "pslhit": str,
                            "dpll": {
                                Any(): {
                                    "mode": str,
                                    "refId": str,
                                }
                            },
                            Optional("nco_assist_pair_hw_lock_status"): str,
                            "psl": {
                                Any(): {
                                    "bandwidth": int,
                                    "var_bw": int,
                                    "pullinrange": int
                                }
                            }
                        }
                    }
                }
            },
            "refclk": {
                Any(): {
                    "measured_freq": int,
                    "freq_err": str
                }
            }
        }
    }


class ShowHardwareInternalTctrlUsdDpllState(ShowHardwareInternalTctrlUsdDpllStateSchema):
    """Parser for show hardware internal tctrl_usd dpll state"""

    cli_command = 'show hardware internal tctrl_usd dpll state'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)


        # ------------------------ INST:0 DPLL 0 ------------------------
        p0 = re.compile(r'^\-+\s+INST:(?P<inst>\d+)\s+DPLL\s+(?P<dpll>\d+)\s+\-+$')

        # dpll_mon_status_0 (0x0118): 0x02: in Holdover
        # dpll_mon_status_0 (0x0110): 0x02: in Holdover
        p1 = re.compile(r'^dpll_mon_status_\d+\s+(?P<dpll_mon_status>[\(\w\)\s\:]+)$')

        # lock: No
        p2 = re.compile(r'^lock:\s+(?P<lock>\w+)$')

        # ho: Yes
        p3 = re.compile(r'^ho:\s+(?P<ho>\w+)$')

        # step_time in progress No
        p4 = re.compile(r'^step_time in progress+\s+(?P<step_time_in_progress>\w+)$')

        # flhit No
        p5 = re.compile(r'^flhit\s+(?P<flhit>\w+)$')

        # pslhit No
        p6 = re.compile(r'^pslhit\s+(?P<pslhit>\w+)$')

        # dpll 0 mode Automatic mode(3) refId INVALID(15)
        p7 = re.compile(r'^dpll\s+\d+\s+mode\s+(?P<mode>\w+)\s+\w+\(\d+\)\s+refId\s+(?P<refId>\w+)\(\-?\d+\)$')

        # NCO Assist Pair HW lock status: Ref Failed(4)
        p8 = re.compile(r'^NCO Assist Pair HW lock status:\s+(?P<nco_assist_pair_hw_lock_status>[\s\w\(\d\)]+)$')

        # PSL 885 Bandwidth 7 Var BW 79 PullInRange 0
        # PSL     7500    Bandwidth 7     Var BW 135      PullInRange 0
        p9 = re.compile(r'^PSL\s+(?P<psl>\d+)\s+\w+\s+(?P<bandwidth>\d+)\s+\w+\s+\w+\s+(?P<var_bw>\d+)\s+\w+\s+(?P<pullinrange>\d+)$')

        # ZL30XXX_REF0P(0) : 7743 NA
        # ZL30XXX_REF0P(0)        :         0             NA
        p10 = re.compile(r'^(?P<refclk>\w+\(\d+\))\s+\:\s+(?P<measured_freq>\d+)\s+(?P<freq_err>(\w+|\d+\.\d+|\-\d+\.\d+))$')

        # Final dict
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # ------------------------ INST:0 DPLL 0 ------------------------   
            m = p0.match(line)
            if m:
                groups = m.groupdict()
                dpll = int(groups['dpll'])
                inst = int(groups['inst'])
                result_dict = ret_dict.setdefault('dpll_hw_state', {}).setdefault('inst', {}).setdefault(inst,{})\
                    .setdefault('dpll',{}).setdefault(dpll,{})
                continue

            # dpll_mon_status_0 (0x0118): 0x02: in Holdover
            # dpll_mon_status_0 (0x0110): 0x02: in Holdover   
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                result_dict['dpll_mon_status'] = groups['dpll_mon_status']
                continue

            # lock: No    
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                result_dict['lock'] = groups['lock']
                continue

            # ho: Yes
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                result_dict['ho'] = groups['ho']
                continue

            # step_time in progress No    
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                result_dict['step_time_in_progress'] = groups['step_time_in_progress']
                continue

            # flhit No    
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                result_dict['flhit'] = groups['flhit']
                continue

            # pslhit No      
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                result_dict['pslhit'] = groups['pslhit']
                continue

            # dpll 0 mode Automatic mode(3) refId INVALID(15)    
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                result_dict = ret_dict.setdefault('dpll_hw_state', {}).setdefault('inst', {}).setdefault(inst,{})\
                    .setdefault('dpll',{}).setdefault(dpll,{}).setdefault('dpll',{}).setdefault(dpll,{})
                result_dict['mode'] = groups['mode']
                result_dict['refId'] = groups['refId']
                continue
            
            # NCO Assist Pair HW lock status: Ref Failed(4)
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                result_dict = ret_dict.setdefault('dpll_hw_state', {}).setdefault('inst', {}).setdefault(inst,{})\
                    .setdefault('dpll',{}).setdefault(dpll,{})
                result_dict['nco_assist_pair_hw_lock_status'] = groups['nco_assist_pair_hw_lock_status']
                continue
            
            # PSL 885 Bandwidth 7 Var BW 79 PullInRange 0
            # PSL     7500    Bandwidth 7     Var BW 135      PullInRange 0
            m =p9.match(line)
            if m:
                groups = m.groupdict()
                psl = int(groups['psl'])
                result_dict = ret_dict.setdefault('dpll_hw_state', {}).setdefault('inst', {}).setdefault(inst,{})\
                    .setdefault('dpll',{}).setdefault(dpll,{}).setdefault('psl',{}).setdefault(psl,{})
                result_dict['bandwidth'] = int(groups['bandwidth'])
                result_dict['var_bw'] = int(groups['var_bw'])
                result_dict['pullinrange'] = int(groups['pullinrange'])
                continue
            
            # ZL30XXX_REF0P(0) : 7743 NA
            # ZL30XXX_REF0P(0)        :         0             NA
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                refclk = groups['refclk']
                result_dict = ret_dict.setdefault('dpll_hw_state', {}).setdefault('refclk',{}).setdefault(refclk,{})
                result_dict['measured_freq'] = int(groups['measured_freq'])
                result_dict['freq_err'] = groups['freq_err']
                continue
                  
        return ret_dict
    
class ShowHardwareInternalErrorsAllSchema(MetaParser):
    """Schema for show hardware internal errors all"""

    schema = {
        'slot': {
            Any(): {
                'device_records': ListOf({
                    'device': str,
                    'role': str,
                    'mod': int,
                    Optional('last_cleared'): str,
                    Optional('category'): str,
                    'instance': {
                        Any(): {
                            'counter': {
                                Any(): {
                                    'name': str,
                                    'value': int,
                                    'ports': str,
                                }
                            }
                        }
                    }
                })
            }
        }
    }


class ShowHardwareInternalErrorsAll(ShowHardwareInternalErrorsAllSchema):
    """Parser for show hardware internal errors all"""

    cli_command = 'show hardware internal errors all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        slot = None
        device_record = None
        instance = None

        # slot  1
        p1 = re.compile(r'^slot\s+(?P<slot>\d+)$')

        # A11-EK-64# show hardware internal errors all
        # A11-EK-64#
        p2 = re.compile(
            r'^\S+#(?:\s+(?:sh|show) hardware internal errors all)?$'
        )

        # | Device:Sacramento Xbar ASIC   Role:MAC                     Mod: 1    |
        p3 = re.compile(
            r'^\|\s*Device:(?P<device>[^\r\n]+?)\s{2,}Role:'
            r'(?P<role>\S+)\s+Mod:\s*(?P<mod>\d+)\s*\|$'
        )

        # | Last cleared @ Thu Oct  1 14:59:35 2026
        p4 = re.compile(
            r'^\|\s*Last cleared @ (?P<last_cleared>[^\r\n]+)$'
        )

        # | Device Statistics Category :: ERROR
        p5 = re.compile(
            r'^\|\s*Device Statistics Category\s*::\s*'
            r'(?P<category>\S+)$'
        )

        # Instance:0
        p6 = re.compile(r'^Instance:(?P<instance>\d+)$')

        # |------------------------------------------------------------------------|
        p7 = re.compile(r'^\|[-]+\|$')

        # ID       Name       Value       Ports
        p8 = re.compile(r'^ID\s+Name\s+Value\s+Ports$')

        # --       ----       -----       -----
        p9 = re.compile(r'^--\s+----+\s+----+\s+----+$')

        # 196623      Interface Inbound Errors (CRC,len,Algn Err)   0000000000000013  1,17,61 -
        p10 = re.compile(
            r'^(?P<id>\d+)\s+(?P<name>[^\r\n]+?)\s{2,}'
            r'(?P<value>\d{16})\s+(?P<ports>\S[^\r\n]*)$'
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # slot  1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                slot = int(groups['slot'])
                ret_dict.setdefault('slot', {}).setdefault(
                    slot, {'device_records': []}
                )
                device_record = None
                instance = None
                continue

            # A11-EK-64# show hardware internal errors all
            m = p2.match(line)
            if m:
                continue

            if slot is None:
                continue

            slot_dict = ret_dict['slot'][slot]

            # | Device:Sacramento Xbar ASIC   Role:MAC                     Mod: 1    |
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                device_record = {
                    'device': groups['device'].strip(),
                    'role': groups['role'],
                    'mod': int(groups['mod']),
                    'instance': {},
                }
                slot_dict['device_records'].append(device_record)
                instance = None
                continue

            # | Last cleared @ Thu Oct  1 14:59:35 2026
            m = p4.match(line)
            if m and device_record is not None:
                groups = m.groupdict()
                device_record['last_cleared'] = groups['last_cleared']
                continue

            # | Device Statistics Category :: ERROR
            m = p5.match(line)
            if m and device_record is not None:
                groups = m.groupdict()
                device_record['category'] = groups['category']
                continue

            # Instance:0
            m = p6.match(line)
            if m and device_record is not None:
                groups = m.groupdict()
                instance = int(groups['instance'])
                device_record['instance'].setdefault(
                    instance, {'counter': {}}
                )
                continue

            # |------------------------------------------------------------------------|
            m = p7.match(line)
            if m:
                continue

            # ID       Name       Value       Ports
            m = p8.match(line)
            if m:
                continue

            # --       ----       -----       -----
            m = p9.match(line)
            if m:
                continue

            if instance is None:
                continue

            # 196623      Interface Inbound Errors (CRC,len,Algn Err)   0000000000000013  1,17,61 -
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                entry_id = int(groups['id'])
                entry_dict = device_record['instance'][instance][
                    'counter'
                ].setdefault(
                    entry_id, {}
                )
                entry_dict['name'] = groups['name'].strip()
                entry_dict['value'] = int(groups['value'])
                entry_dict['ports'] = groups['ports']
                continue

        return ret_dict
