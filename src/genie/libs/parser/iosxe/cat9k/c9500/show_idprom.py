'''show_idprom.py

IOSXE parser for 9500X for the following show commands:

    * show idprom tan 
'''

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or

import re

# ==========================
# Schema for:
#  * 'show idprom tan'
# ==========================
class ShowIdpromTanSchema(MetaParser):
    """Schema for:
        show idprom tan
         """

    schema = {
        'module': {
            Any(): {
                'module_num': int,
                'part_num': str,
                'revision_num': Or(int, str),
            },
        },
        'power_supply': {
            Any(): {
                'power_supply_num': int,
                'part_num': str,
                'revision_num': Or(int, str),
            },
        },
        'fantray': {
            Any(): {
                'fantray_num': int,
                'part_num': str,
                'revision_num': Or(int, str),
            },
        },
    }

class ShowIdpromTan(ShowIdpromTanSchema):
    """Parser for:
        show idprom tan
         """

    cli_command = ['show idprom tan']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Module 1 Idprom:
        p1 = re.compile(r"^Module\s+(?P<module_num>\d+)\s+Idprom:$")
        # Power Supply 0 Idprom:
        p2 = re.compile(r"^Power\s+Supply\s+(?P<power_supply_num>\d+)\s+Idprom:$")
        # Fantray 1 Idprom:
        p3 = re.compile(r"^Fantray\s+(?P<fantray_num>\d+)\s+Idprom:$")
        # Top Assy. Part Number           : 68-101195-01
        p4 = re.compile(r"^Top\s+Assy.\s+Part\s+Number\s+:\s+(?P<part_num>\d+-\d+-\d+)$")
        # Top Assy. Revision       : A0
        p5 = re.compile(r"^Top\s+Assy.\s+Revision\s+:\s+(?P<revision_num>\w+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Module 1 Idprom:
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                module_var = int(dict_val['module_num'])
                module_group = ret_dict.setdefault('module', {})
                sw_dict = ret_dict['module'].setdefault(module_var, {})
                sw_dict['module_num'] = int(module_var)
                continue

            # Power Supply 0 Idprom:
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                power_supply_var = int(dict_val['power_supply_num'])
                switch_group = ret_dict.setdefault('power_supply', {})
                sw_dict = ret_dict['power_supply'].setdefault(power_supply_var, {})
                sw_dict['power_supply_num'] = int(power_supply_var)
                continue

            # Fantray 0 Idprom:
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                fantray_var = int(dict_val['fantray_num'])
                switch_group = ret_dict.setdefault('fantray', {})
                sw_dict = ret_dict['fantray'].setdefault(fantray_var, {})
                sw_dict['fantray_num'] = int(fantray_var)
                continue

            # Top Assy. Part Number           : 68-101195-01
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                part_num_var = dict_val['part_num']
                sw_dict['part_num'] = part_num_var
                continue

            # Top Assy. Revision Number       : 31
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                revision_part_num = dict_val['revision_num']
                try:
                    sw_dict['revision_num'] = int(revision_part_num)
                except ValueError:
                    sw_dict['revision_num'] = revision_part_num
                continue


        return ret_dict 