"""show_variables_boot.py

IOSXR parser for the following show command:
    * 'show variables boot'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional

# =======================================
# Schema for 'show variables boot'
# =======================================
class ShowVariablesBootSchema(MetaParser):
    """Schema for show variables boot"""

    schema = {
        'boot_variables': {
            'root': str,
            'platform': str,
            'boardtype': str,
            'cardtype': str,
            'iputype': str,
            'vmtype': str,
            'bigphysarea': str,
            'chassis_type': str,
            'intel_idle_max_cstate': int,
            'processor_max_cstate': int,
            'chassis_serial': str,
            'chassis_pid': str,
            'primary_console': str,
            Optional('secondary_console'): str,
            'prod': int,
            'pci': {
                'hpmemsize': str,
                'hpiosize': str
            }
        }
    }

# =====================================
# Parser for 'show variables boot'
# =====================================
class ShowVariablesBoot(ShowVariablesBootSchema):
    """Parser for show variables boot"""

    cli_command = 'show variables boot'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Initializes the Python dictionary variable
        parsed_dict = {}
        
        # root=/dev/panini_vol_grp/xr_lv68 platform=asr9k boardtype=RP cardtype=0x101014 iputype=0x02f52029 vmtype=xr-vm quiet virtvm bigphysarea="12M" chassis_type=0xef1015 intel_idle.max_cstate=0 processor.max_cstate=1 chassis_serial=FOC2412N8LP chassis_pid=ASR-9901 console=tty0 console=hvc0 prod=1 pci=hpmemsize=0M,hpiosize=0M
        p = re.compile(r'^root=(?P<root>[\w\/]+) +'
                       r'platform=(?P<platform>[\w]+) +'
                       r'boardtype=(?P<boardtype>[\w]+) +'
                       r'cardtype=(?P<cardtype>[\w]+) +'
                       r'iputype=(?P<iputype>[\w]+) +'
                       r'vmtype=(?P<vmtype>[\w -]+) +'
                       r'bigphysarea="?(?P<bigphysarea>[\w]+)"? +'
                       r'chassis_type=(?P<chassis_type>[\w]+) +'
                       r'intel_idle\.max_cstate=(?P<intel_idle_max_cstate>[\d]+) +'
                       r'processor\.max_cstate=(?P<processor_max_cstate>[\d]+) +'
                       r'chassis_serial=(?P<chassis_serial>[\w]+) +'
                       r'chassis_pid=(?P<chassis_pid>[\w-]+) +'
                       r'console=(?P<primary_console>[\w]+) +'
                       r'(console=(?P<secondary_console>[\w]+) +)?'
                       r'prod=(?P<prod>[\d]+) +'
                       r'pci=(?P<pci>hpmemsize=(?P<hpmemsize>[\w]+)\,\s*hpiosize=(?P<hpiosize>[\w]+))$')

        # Processes the matched patterns
        for line in out.splitlines():
            line = line.strip()
            
            # root=/dev/panini_vol_grp/xr_lv68 platform=asr9k boardtype=RP cardtype=0x101014 iputype=0x02f52029 vmtype=xr-vm quiet virtvm bigphysarea="12M" chassis_type=0xef1015 intel_idle.max_cstate=0 processor.max_cstate=1 chassis_serial=FOC2412N8LP chassis_pid=ASR-9901 console=tty0 console=hvc0 prod=1 pci=hpmemsize=0M,hpiosize=0M
            m = p.match(line)
            if m:
                group = m.groupdict()
                boot_variables_dict = parsed_dict.setdefault('boot_variables', {})
                boot_variables_dict['root'] = group['root']
                boot_variables_dict['platform'] = group['platform']
                boot_variables_dict['boardtype'] = group['boardtype']
                boot_variables_dict['cardtype'] = group['cardtype']
                boot_variables_dict['iputype'] = group['iputype']
                boot_variables_dict['vmtype'] = group['vmtype']
                boot_variables_dict['bigphysarea'] = group['bigphysarea']
                boot_variables_dict['chassis_type'] = group['chassis_type']
                boot_variables_dict['intel_idle_max_cstate'] = int(group['intel_idle_max_cstate'])
                boot_variables_dict['processor_max_cstate'] = int(group['processor_max_cstate'])
                boot_variables_dict['chassis_serial'] = group['chassis_serial']
                boot_variables_dict['chassis_pid'] = group['chassis_pid']
                boot_variables_dict['primary_console'] = group['primary_console']
                boot_variables_dict['secondary_console'] = group['secondary_console']
                boot_variables_dict['prod'] = int(group['prod'])
                pci_dict = boot_variables_dict.setdefault('pci', {})
                pci_dict['hpmemsize'] = group['hpmemsize']
                pci_dict['hpiosize'] = group['hpiosize']
                continue
        
        return parsed_dict    
                