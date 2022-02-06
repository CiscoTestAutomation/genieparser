''' show_environment.py

IOSXR parsers for the following show commands:
    * 'admin show environment power-supply'
    * 'admin show environment power-supply location {location}'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

# =========================
# Parser for:
# 'admin show environment power-supply'
# 'admin show environment power-supply location {location}'
# =========================

class AdminShowEnvironmentPowerSupplySchema(MetaParser):
    """Schema for 'admin show environment power-supply'"""
    schema = {
        'rack': {
            Any(): { # rack_id number
                'power_shelves_type': str,
                'power_budget_strict_mode': str,
                Optional('power_budget_enforcement'): str,
                Optional('power_redundancy_mode'): str,
                'total_power_capacity': str,
                'usable_power_capacity': str,
                'protected_suppply_capacity': str,
                'protected_suppply_available': str,
                'worst_case_power_used': str,
                'worst_case_power_available': str,
                'slot' : {                    
                    Any(): { # slot_types: {psm: power_supply_module, ft:fan_tray, rsp:rsp, lc:line_card oc: other_card, FC: fabric_card}
                        Optional('total_power_draw'): str, # total power for every slot of the same type
                        Optional('total_power_supply'): str, # total power for every slot of the same type
                        Any(): {  # slot number
                            'full_slot' : str, # full slot location: R/S/I
                            Optional('power_supply'): str,
                            Optional('capacity'): str,
                            Optional('status'): str,
                            Optional('power_draw'): str,
                            Optional('voltage'): str,
                            Optional('current'): str,
                            Optional("worst_case_power_used"): str,
                        }
                    }
                }
            }
        }
    }


class AdminShowEnvironmentPowerSupply(AdminShowEnvironmentPowerSupplySchema):
    """Parser for 'admin show environment power-supply'"""

    cli_command = ['admin show environment power-supply', 'admin show environment power-supply location {location}']

    def cli(self, output=None, location=None):
        if output is None:
            if location is None:
                cmd = self.cli_command[0]
            elif location:
                cmd = self.cli_command[1].format(location=location)
            if cmd:
                out = self.device.execute(cmd)
            else:
                return
        else:
            out = output

        # return simple dict if not out        
        if not out:
            return

        # Init vars
        return_dict = {}
        return_dict['rack'] = {}

        # R/S/I   Modules         Capacity        Status
        # R/S/I           Power Supply    Voltage         Current
        # R/S/I           Power Draw      Voltage         Current
        p1 = re.compile(r'^\S+\s+(?P<section>Modules|Power Supply|Power Draw)'
                         '(?P<section_keys>\s+\S+\s+\S+)$')

        # 0/PS0/M0/*
        # 0/PM0/*
        # 0/PS0/*
        p2 = re.compile(r'^(?P<psm_location>'
                            '(?P<rack_id>\d+)\/(?=PS|PM)'
                            '(?P<slot_id>[^\/\s]+(?:\/[^\/]+)?)\/\*)$')

        # host    PM      4400            Ok
        # host    PM      2200            Ok(Feeder A is missing)
        p3 = re.compile(r'^host\s+PM\s+(?P<psm_capacity>\d+)'
                         '\s+(?P<psm_status>.*?)$')

        # 0/PS0/M0/*       922.3          54.9            16.8
        # 0/PS0/*          922.3          54.9            16.8
        # 0/PM0/*          922.3          54.9            16.8
        p4 = re.compile(r'^(?P<psm_location>'
                            '(?P<rack_id>\d+)\/(?=PS|PM)'
                            '(?P<slot_id>[^\/\s]+(?:\/[^\/]+)?)'
                         '\/\*)'
                         '\s+(?P<psm_power_supply>[\d\.]+)'
                         '\s+(?P<psm_voltage>[\d\.]+)'
                         '\s+(?P<psm_current>[\d\.]+)$')

        # 0/RSP0/*         223.8          54.6             4.1
        # 0/FT0/*         142.2          54.7             2.6
        # 0/0/*         322.1          54.6             5.9
        # 0/0/*         320 **
        # 0/RSP0/*         205 **
        p5 = re.compile(r'^(?P<other_slot_location>'
                            '(?P<rack_id>\d+)\/(?!PM|PS)'
                            '(?P<slot_id>[^\/\s]+)'
                         '\/[^\/\s]+)'
                         '\s+(?P<other_slot_power_draw>[\d\.]+)'
                         '(?:\s+(?P<other_slot_voltage>[\d\.]+)| \*)'
                         '(?:\s+(?P<other_slot_current>[\d\.]+)|\*)$')

        # Power Shelves Type: DC
        p6 = re.compile(r'^Power Shelves Type: (?P<power_shelves_type>.*?)$')

        # Power Budget Strict Mode: Disabled 
        p7 = re.compile(r'^Power Budget Strict Mode: (?P<power_budget_strict_mode>.*?)$')

        # Power Budget Enforcement: Enabled 
        p8 = re.compile(r'^Power Budget Enforcement: (?P<power_budget_enforcement>.*?)$')

        # Power Redundancy Mode: N + 1 
        p9 = re.compile(r'^Power Redundancy Mode: (?P<power_redundancy_mode>.*?)$')

        # Total Power Capacity:                           13200W
        p10 = re.compile(r'^Total Power Capacity:\s+(?P<total_power_capacity>[\dW]+)$')

        # Usable Power Capacity:                          13200W
        p11 = re.compile(r'^Usable Power Capacity:\s+(?P<usable_power_capacity>[\dW]+)$')

        # Supply Failure Protected Capacity:              4400W
        # N+1 Supply Failure Protected Capacity:          8800W
        p12 = re.compile(r'^(?:N\+1 )?Supply Failure Protected Capacity:\s+(?P<protected_suppply_capacity>[\dW]+)$')

        # Worst Case Power Used:                          5980W
        p13 = re.compile(r'^Worst Case Power Used:\s+(?P<worst_case_power_used>[\dW]+)$')

        # Worst Case Power Available:             7220W
        p14 = re.compile(r'^Worst Case Power Available:\s+(?P<worst_case_power_available>[\dW]+)$')

        # Supply Protected Capacity Available:     330W
        # N+1 Supply Protected Capacity Available:        2820W
        p15 = re.compile(r'^(?:N\+1 )?Supply Protected Capacity Available:\s+(?P<protected_suppply_available>[\dW]+)$')

        # Total:  2709.8
        # Total:  322.3
        # Total:  448.4
        # Total:  2830.0
        p16 = re.compile(r'^Total:\s+(?P<total_power>[\d\.]+)$')

        # 0/0/CPU0                                                        320
        # 0/RSP0/CPU0                                                     205
        # 0/FT1/SP                                                        600
        p17 = re.compile(r'^(?P<other_slot_location>(?P<rack_id>\d+)\/(?!PM|PS)'
                          '(?P<slot_id>[^\/\s]+)\/[^\/\s]+)'
                          '\s+(?P<worst_case_power_used>[\d\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            # R/S/I   Modules         Capacity        Status
            # R/S/I           Power Supply    Voltage         Current
            # R/S/I           Power Draw      Voltage         Current
            m = p1.match(line)
            if m:
                # Parse section
                section = m.groupdict()['section']
                if section in ('Modules', 'Power Supply'):
                    slot_type = "PSM"
                elif section in ('Power Draw',):
                    slot_type = "other_slot"
                    #psm: power_supply_module, ft:fan_tray, rsp:rsp, oc: other_card, FC: fabric_card
                continue

            # 0/PS0/M0/*
            # 0/PS0/M2/*
            # 0/PS1/M0/*
            # 0/PS1/M2/*
            m = p2.match(line)
            if m:
                # Parse PSM rack_id, slot, full_slot
                if slot_type == "PSM":
                    group_dict = m.groupdict()
                    psm_location = group_dict['psm_location']
                    rack_id = group_dict['rack_id']
                    slot_id = group_dict['slot_id']
                    return_dict['rack'].setdefault(rack_id, {}).setdefault("slot", {}).setdefault(slot_type, {}).setdefault(slot_id, {}).setdefault("full_slot", psm_location)
                    continue

            # host    PM      4400            Ok
            # host    PM      2200            Ok(Feeder A is missing)
            m = p3.match(line)
            if m:
                # Parse psm capacity, status
                if slot_type == "PSM":
                    group_dict = m.groupdict()
                    psm_capacity = group_dict['psm_capacity']
                    psm_status = group_dict['psm_status']
                    return_dict['rack'][rack_id]["slot"][slot_type][slot_id]["capacity"] = psm_capacity
                    return_dict['rack'][rack_id]["slot"][slot_type][slot_id]["status"] = psm_status
                    continue

            # 0/PS0/M0/*       922.3          54.9            16.8
            # 0/PS0/M2/*       880.0          55.0            16.0
            # 0/PS1/M0/*       473.0          55.0             8.6
            # 0/PS1/M2/*       434.5          55.0             7.9
            # 0/PS0/*          922.3          54.9            16.8
            # 0/PS2/*          880.0          55.0            16.0
            # 0/PS4/*          473.0          55.0             8.6
            # 0/PS6/*          434.5          55.0             7.9
            # 0/PM0/*          922.3          54.9            16.8
            # 0/PM2/*          880.0          55.0            16.0
            # 0/PM4/*          473.0          55.0             8.6
            # 0/PM6/*          434.5          55.0             7.9
            m = p4.match(line)
            if m:
                # Parse psm: psm_location, rack_id, slot_id, psm_power_supply, psm_voltage, psm_current
                if slot_type == "PSM":
                    group_dict = m.groupdict()
                    psm_location = group_dict['psm_location']
                    rack_id = group_dict['rack_id']
                    slot_id = group_dict['slot_id']
                    psm_power_supply = group_dict['psm_power_supply']
                    psm_voltage = group_dict['psm_voltage']
                    psm_current = group_dict['psm_current']
                    return_dict['rack'][rack_id]["slot"][slot_type][slot_id]["power_supply"] = psm_power_supply
                    return_dict['rack'][rack_id]["slot"][slot_type][slot_id]["voltage"] = psm_voltage
                    return_dict['rack'][rack_id]["slot"][slot_type][slot_id]["current"] = psm_current
                    continue

            # 0/RSP0/*         223.8          54.6             4.1
            # 0/RSP1/*         224.6          54.8             4.1
            # 0/FT0/*          142.2          54.7             2.6
            # 0/FT1/*          180.1          54.6             3.3
            # 0/0/*            322.1          54.6             5.9
            # 0/1/*            318.4          54.9             5.8
            # 0/4/*            545.0          54.5            10.0
            # 0/5/*            550.0          55.0            10.0
            # 0/6/*            544.5          55.0             9.9
            # 0/7/*            550.0          55.0            10.0
            # 0/0/*         320 **
            # 0/1/*         320 **
            # 0/4/*         320 **
            # 0/5/*         320 **
            # 0/RSP0/*         205 **
            # 0/RSP1/*         205 **
            m = p5.match(line)
            if m:
                # Parse slot_id: other_slot_location, rack_id, slot_id, other_slot_power_draw, other_slot_voltage, other_slot_current
                if slot_type != "PSM":
                    group_dict = m.groupdict()
                    other_slot_location = group_dict['other_slot_location']
                    rack_id = group_dict['rack_id']
                    slot_id = group_dict['slot_id']
                    other_slot_power_draw = group_dict['other_slot_power_draw']
                    other_slot_voltage = group_dict['other_slot_voltage']
                    other_slot_current = group_dict['other_slot_current']
                    if slot_id.startswith("RSP"):
                        slot_type = "RSP"
                    elif slot_id.startswith("FT"):
                        slot_type = "FAN"
                    elif slot_id.startswith("FC"):
                        slot_type = "FC"
                    else:
                        slot_type = "LC"
                    return_dict['rack'].setdefault(rack_id, {}).setdefault("slot", {}).setdefault(slot_type, {}).setdefault(slot_id, {}).setdefault("full_slot", other_slot_location)
                    return_dict['rack'][rack_id]["slot"][slot_type][slot_id]["power_draw"] = other_slot_power_draw
                    if other_slot_voltage:
                        return_dict['rack'][rack_id]["slot"][slot_type][slot_id]["voltage"] = other_slot_voltage
                    if other_slot_current:
                        return_dict['rack'][rack_id]["slot"][slot_type][slot_id]["current"] = other_slot_current
                    continue

            # Power Shelves Type: DC
            m = p6.match(line)
            if m:
                # Parse power_shelves_type
                group_dict = m.groupdict()
                power_shelves_type = group_dict['power_shelves_type']
                return_dict['rack'].setdefault(rack_id, {}).setdefault("power_shelves_type", power_shelves_type)
                continue

           # Power Budget Strict Mode: Disabled 
            m = p7.match(line)
            if m:
                # Parse power_budget_strict_mode
                group_dict = m.groupdict()
                power_budget_strict_mode = group_dict['power_budget_strict_mode']
                return_dict['rack'].setdefault(rack_id, {}).setdefault("power_budget_strict_mode", power_budget_strict_mode)
                continue

            # Power Budget Enforcement: Enabled 
            m = p8.match(line)
            if m:
                # Parse power_budget_enforcement
                group_dict = m.groupdict()
                power_budget_enforcement = group_dict['power_budget_enforcement']
                return_dict['rack'].setdefault(rack_id, {}).setdefault("power_budget_enforcement", power_budget_enforcement)
                continue

            # Power Redundancy Mode: N + 1 
            m = p9.match(line)
            if m:
                # Parse power_redundancy_mode
                group_dict = m.groupdict()
                power_redundancy_mode = group_dict['power_redundancy_mode']
                return_dict['rack'].setdefault(rack_id, {}).setdefault("power_redundancy_mode", power_redundancy_mode)
                continue

           # Total Power Capacity:                           13200W
            m = p10.match(line)
            if m:
                # Parse total_power_capacity
                group_dict = m.groupdict()
                total_power_capacity = group_dict['total_power_capacity']
                return_dict['rack'].setdefault(rack_id, {}).setdefault("total_power_capacity", total_power_capacity)
                continue

            # Usable Power Capacity:                          13200W
            m = p11.match(line)
            if m:
                # Parse usable_power_capacity
                group_dict = m.groupdict()
                usable_power_capacity = group_dict['usable_power_capacity']
                return_dict['rack'].setdefault(rack_id, {}).setdefault("usable_power_capacity", usable_power_capacity)
                continue

            # Supply Failure Protected Capacity:              4400W
            # N+1 Supply Failure Protected Capacity:          8800W
            m = p12.match(line)
            if m:
                # Parse protected_suppply_capacity
                group_dict = m.groupdict()
                protected_suppply_capacity = group_dict['protected_suppply_capacity']
                return_dict['rack'].setdefault(rack_id, {}).setdefault("protected_suppply_capacity", protected_suppply_capacity)
                continue

            # Worst Case Power Used:                          5980W
            m = p13.match(line)
            if m:
                # Parse worst_case_power_used
                group_dict = m.groupdict()
                worst_case_power_used = group_dict['worst_case_power_used']
                return_dict['rack'].setdefault(rack_id, {}).setdefault("worst_case_power_used", worst_case_power_used)
                continue

            # Worst Case Power Available:             7220W
            m = p14.match(line)
            if m:
                # Parse worst_case_power_available
                group_dict = m.groupdict()
                worst_case_power_available = group_dict['worst_case_power_available']
                return_dict['rack'].setdefault(rack_id, {}).setdefault("worst_case_power_available", worst_case_power_available)    
                continue

            # N+1 Supply Protected Capacity Available:        2820W
            # Supply Protected Capacity Available:     330W
            m = p15.match(line)
            if m:
                # Parse protected_suppply_available
                group_dict = m.groupdict()
                protected_suppply_available = group_dict['protected_suppply_available']
                return_dict['rack'].setdefault(rack_id, {}).setdefault("protected_suppply_available", protected_suppply_available)
                continue

            # Total:  2709.8
            # Total:  322.3
            # Total:  448.4
            # Total:  2830.0
            m = p16.match(line)
            if m:
                # Parse total_power
                group_dict = m.groupdict()
                total_power = group_dict['total_power']
                if "rack_id" in locals():
                    if slot_type == "PSM":
                        return_dict['rack'].setdefault(rack_id, {}).setdefault("slot", {}).setdefault(slot_type, {}).setdefault('total_power_supply', total_power)
                    else:
                        return_dict['rack'].setdefault(rack_id, {}).setdefault("slot", {}).setdefault(slot_type, {}).setdefault('total_power_draw', total_power)
                continue

            # 0/0/CPU0                                                        320
            # 0/RSP0/CPU0                                                     205
            # 0/FT1/SP                                                        600
            m = p17.match(line)
            if m:
                # Parse slot_id: other_slot_location, rack_id, slot_id, worst_case_power_used
                if slot_type != "PSM":
                    group_dict = m.groupdict()
                    other_slot_location = group_dict['other_slot_location']
                    rack_id = group_dict['rack_id']
                    slot_id = group_dict['slot_id']
                    worst_case_power_used = group_dict['worst_case_power_used']
                    if slot_id.startswith("RSP"):
                        slot_type = "RSP"
                    elif slot_id.startswith("FT"):
                        slot_type = "FAN"
                    elif slot_id.startswith("FC"):
                        slot_type = "FC"
                    else:
                        slot_type = "LC"
                    return_dict['rack'].setdefault(rack_id, {}).setdefault("slot", {}).setdefault(slot_type, {}).setdefault(slot_id, {}).setdefault("full_slot", other_slot_location)
                    if worst_case_power_used:
                        return_dict['rack'][rack_id]["slot"][slot_type][slot_id]["worst_case_power_used"] = worst_case_power_used
                    continue

        return return_dict