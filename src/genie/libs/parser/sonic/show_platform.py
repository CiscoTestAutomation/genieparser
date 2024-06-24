"""
SONiC parsers for the following show commands:

    * show platform inventory
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowPlatformSchema(MetaParser):
    """
    Schema for
        * show platform inventory
    """
    schema = {
        'chassis': {
            Any(): {
                'name': str,
                'product_id': str,
                'version': str,
                'serial_num': str,
                'description': str,
            },
        },
        'rp': {
            Any(): {
                'name': str,
                'product_id': str,
                'version': str,
                'serial_num': str,
                'description': str,
            },
        },
        'power_supplies': {
            Any(): {
                'name': str,
                Optional('state'): str,
                Optional('product_id'): str,
                Optional('version'): str,
                Optional('serial_num'): str,
                Optional('description'): str,
            },
        },
        Optional('cooling_devices'): {
            Any(): {
                'name': str,
                Optional('state'): str,
                Optional('product_id'): str,
                Optional('version'): str,
                Optional('serial_num'): str,
            },
        },
        Optional('fpds'): {
            Any(): {
                'name': str,
                'version': str,
                'description': str,
            },
        }
    }


class ShowPlatformInventory(ShowPlatformSchema):
    """
    Parser for
        * show platform inventory
    """
    cli_command = "show platform inventory"

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)
        
        ret_dict = {}
    
        # CHASSIS             8201-32FH-O     0.33            FOC2217DTWE     Cisco 8201-32FH Open Network
        p1 = re.compile(r'^(?P<chassis>CHASSIS\d*?)\s+(?P<product_id>[a-zA-Z0-9@.\-]+)\s+(?P<version>[0-9]*\.[0-9]+)\s+(?P<serial_num>[A-Za-z0-9]+)\s+(?P<description>.*)(\s+)?$')

        # RP0                 8101-32FH-O     0.41            FLM2528059A     Cisco 8100 32x400G QSFPDD 1RU Fixed System w/o HBM, Open SW
        p2 = re.compile(r'^(?P<rp>RP\d*?)\s+(?P<product_id>[a-zA-Z0-9@.\-]+)\s+(?P<version>[0-9]*\.[0-9]+)\s+(?P<serial_num>[A-Za-z0-9]+)\s+(?P<description>.*)(\s+)?$')

        # PSU0            PSU2KW-ACPI     0.0             POG2416K01K     2000W AC Power Module with Port-side Air Intake
        p3 = re.compile(r'^(?P<psu>PSU\d*?)\s+(?P<product_id>[a-zA-Z0-9@.\-]+)\s+(?P<version>[0-9]*\.[0-9]+)\s+(?P<serial_num>[A-Za-z0-9]+)\s+(?P<description>.*)(\s+)?$')

        # fantray0            FAN-1RU-PE-V2   0.0             NCV26322018
        p4 = re.compile(r'^(?P<fantray>fantray\d*?)\s+(?P<product_id>[a-zA-Z0-9@.\-]+)\s+(?P<version>[0-9]*\.[0-9]+)\s+(?P<serial_num>[A-Za-z0-9]+)$')

        # PSU0 -- not present
        p5 = re.compile(r'^(?P<psu>PSU\d*?)\s+--\s+(?P<state>[\w\s]+)$')

        # fantray0 -- not present
        p6 = re.compile(r'^(?P<fantray>fantray\d*?)\s+--\s+(?P<state>[\w\s]+)$')

        # RP0/info.0                          0.1.1-0                         \_SB_.PCI0.SE0_.BR2A.BR3A.IOFP.INFO
        p7 = re.compile(r'^(?P<rp_info>RP\d+\/?info\.?\d+)\s+(?P<version>([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)-[A-Za-z0-9]+)\s+(?P<description>([\\_]+.*))(\s+)?$')

        for line in output.splitlines():
            line = line.strip()

            # CHASSIS             8201-32FH-O     0.33            FOC2217DTWE     Cisco 8201-32FH Open Network
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group['chassis']
                chassis_dict = ret_dict.setdefault('chassis', {}).setdefault(name, {})
                chassis_dict.update({
                    'name': name,
                    'product_id': group['product_id'],
                    'version': group['version'],
                    'serial_num': group['serial_num'],
                    'description': group['description'],  
                })
                continue
            
            # RP0                 8101-32FH-O     0.41            FLM2528059A     Cisco 8100 32x400G QSFPDD 1RU Fixed System w/o HBM, Open SW
            m = p2.match(line)
            if m:
                group = m.groupdict()
                name = group['rp']
                rp_dict = ret_dict.setdefault('rp', {}).setdefault(name, {})
                rp_dict.update({
                    'name': name,
                    'product_id': group['product_id'],
                    'version': group['version'],
                    'serial_num': group['serial_num'],
                    'description': group['description'],  
                })
                continue
            
            # PSU0            PSU2KW-ACPI     0.0             POG2416K01K     2000W AC Power Module with Port-side Air Intake
            m = p3.match(line)
            if m:
                group = m.groupdict()
                name = group['psu']
                psu_dict = ret_dict.setdefault('power_supplies', {}).setdefault(name, {})
                psu_dict.update({
                    'name': name,
                    'product_id': group['product_id'],
                    'version': group['version'],
                    'serial_num': group['serial_num'],
                    'description': group['description'],  
                })
                continue
            
            # fantray0            FAN-1RU-PE-V2   0.0             NCV26322018
            m = p4.match(line)
            if m:
                group = m.groupdict()
                name = group['fantray']
                fantray_dict = ret_dict.setdefault('cooling_devices', {}).setdefault(name, {})
                fantray_dict.update({
                    'name': name,
                    'product_id': group['product_id'],
                    'version': group['version'],
                    'serial_num': group['serial_num'],
                })
                continue
            
            # PSU0 -- not present
            m = p5.match(line)
            if m:
                group = m.groupdict()
                name = group['psu']
                psu_dict = ret_dict.setdefault('power_supplies', {}).setdefault(name, {})
                psu_dict.update({
                    'name': name,
                    'state': group['state'],
                })
                continue
            
            # fantray0 -- not present
            m = p6.match(line)
            if m:
                group = m.groupdict()
                name = group['fantray']
                fantray_dict = ret_dict.setdefault('cooling_devices', {}).setdefault(name, {})
                fantray_dict.update({
                    'name': name,
                    'state': group['state'],
                })
                continue
            
            # RP0/info.0                          0.1.1-0                         \_SB_.PCI0.SE0_.BR2A.BR3A.IOFP.INFO
            m = p7.match(line)
            if m:
                group = m.groupdict()
                rp_info = group['rp_info']
                rp_info_dict = ret_dict.setdefault('fpds', {}).setdefault(rp_info, {})
                rp_info_dict.update({
                    'name': name,
                    'version': group['version'],
                    'description': group['description'], 
                })
                continue

        return ret_dict
