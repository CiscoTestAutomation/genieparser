# ========================================================
# Parser for 'show hardware internal tctrl_usd dpll state'
# ========================================================

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
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
    
