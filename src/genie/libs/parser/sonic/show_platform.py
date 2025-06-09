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
                Optional('name'): str,
                Optional('product_id'): str,
                Optional('version'): str,
                Optional('serial_num'): str,
                Optional('description'): str,
                Optional('state'): str,
            },
        },
        Optional('line_cards'): {
            Any(): {
                Optional('name'): str,
                Optional('product_id'): str,
                Optional('version'): str,
                Optional('serial_num'): str,
                Optional('description'): str,
                Optional('state'): str,
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
                Optional('name'): str,
                Optional('state'): str,
                Optional('product_id'): str,
                Optional('version'): str,
                Optional('serial_num'): str,
                Optional('description'): str,
            },
        },
        Optional('fabric_cards'): {
            Any(): {
                Optional('name'): str,
                Optional('product_id'): str,
                Optional('version'): str,
                Optional('serial_num'): str,
                Optional('description'): str,
                Optional('state'): str,
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

        # RP1 -- not present
        p2_1 = re.compile(r'^(?P<rp>RP\d*?)\s+--\s+(?P<state>[\w\s]+)$')

        # PSU0            PSU2KW-ACPI     0.0             POG2416K01K     2000W AC Power Module with Port-side Air Intake
        # psutray0            8800-HV-TRAY    1.0                  FOC2549NLQG     Cisco 8800 Power Tray for AC/HVAC/HVDC Power Supply
        #PSU1            UCSC-PSU1-2300W A0                   DTM274202RX     UCS 2300W AC-DC High Line RSP02 Power Supply
        p3 = re.compile(r'^(?P<psu>(?:PSU|psutray)\d+)\s+(?P<product_id>[a-zA-Z0-9@.\- ]+?)\s+(?P<version>[A-Za-z0-9.\-]+)\s+(?P<serial_num>[A-Za-z0-9]+)\s+(?P<description>.+)$')

        #     psutray1.psu0   PSU6.3KW-20A-HV 1.0                  DTM255000NP     6.3KW AC/HVAC/HVDC Power Supply-20A
        p3_1 = re.compile(r'^(?P<psu_id>(PSU|psutray)?\d*\.(PSU|psu)\d*)\s+(?P<product_id>[a-zA-Z0-9@.\-]+)\s+(?P<version>[0-9]*\.[0-9]+)\s+(?P<serial_num>[A-Za-z0-9]+)\s+(?P<description>.*)(\s+)?$')

        # fantray0            FAN-1RU-PE-V2   0.0             NCV26322018
        # fantray0            8808-FAN        1.0                  FOC2553N1JK     Cisco 8808 Fan Tray
        p4 = re.compile(r'^(?P<fantray>fantray\d*?)\s+(?P<product_id>[a-zA-Z0-9@.\-]+)\s+(?P<version>[0-9]*\.[0-9]+)\s+(?P<serial_num>[A-Za-z0-9]+)(\s+(?P<description>.*)(\s*))?$')

        # PSU0 -- not present
        p5 = re.compile(r'^(?P<psu>(PSU|psutray)?\d*?)\s+--\s+(?P<state>[\w\s]+)$')

        # fantray0 -- not present
        p6 = re.compile(r'^(?P<fantray>fantray\d*?)\s+--\s+(?P<state>[\w\s]+)$')

        # RP0/info.0                          0.1.1-0                         \_SB_.PCI0.SE0_.BR2A.BR3A.IOFP.INFO
        p7 = re.compile(r'^(?P<rp_info>RP\d+\/?info\.?\d+(\.+\w+)?)\s+(?P<version>([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)-[A-Za-z0-9]+)\s+(?P<description>([\\_]+.*))(\s+)?$')

        # LC0/exeter                          1.6.0-206                            Exeter FPGA
        p7_1 = re.compile(r'^(?P<rp_info>LC\d+\/+\w+)\s+(?P<version>([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)-[A-Za-z0-9]+)\s+(?P<description>.*(\s*))$')

        # RP0/ft2/warmwell                    1.0.0-188                            Warmwell FPGA
        # RP0/kirkwall                        1.11.0-696                           Kirkwall FPGA
        p7_2 = re.compile(r'^(?P<rp_info>RP\d+\/+\w+(\/+\w+)?)\s+(?P<version>([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)-[A-Za-z0-9]+)\s+(?P<description>[\w\s]+)$')

        # LC0                 88-LC0-36FH-MO  0.32                 FOC2431NVH1     Cisco 8800 36x400GE QSFP56-DD Line Card with MACsec
        p8 = re.compile(r'^(?P<lc>LC\d*?)\s+(?P<product_id>[a-zA-Z0-9@.\-]+)\s+(?P<version>[0-9]*\.[0-9]+)\s+(?P<serial_num>[A-Za-z0-9]+)\s+(?P<description>.*)(\s+)?$')

        # LC5 -- not present
        p9 = re.compile(r'^(?P<lc>LC\d*?)\s+--\s+(?P<state>[\w\s]+)$')

        # LC6 Card type unknown; Board type unknown -- not initialized
        p10 = re.compile(r'^(?P<lc>LC\d*?)\s+Card type unknown+\; Board type unknown+ --\s+(?P<state>[\w\s]+)$')

        # FC0                 8808-FC0        1.0                  FOC2648NHKZ     Cisco 8808 Fabric Card for 14.4T Line Cards
        p11 = re.compile(r'^(?P<fc>FC\d*?)\s+(?P<product_id>[a-zA-Z0-9@.\-]+)\s+(?P<version>[0-9]*\.[0-9]+)\s+(?P<serial_num>[A-Za-z0-9]+)\s+(?P<description>.*)(\s+)?$')

        # FC1 -- not present
        p12 = re.compile(r'^(?P<fc>FC\d*?)\s+--\s+(?P<state>[\w\s]+)$')


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

            # RP1 -- not present
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                name = group['rp']
                lc_dict = ret_dict.setdefault('rp', {}).setdefault(name, {})
                lc_dict.update({
                    'name': name,
                    'state': group['state'],
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
            # fantray0            8808-FAN        1.0                  FOC2553N1JK     Cisco 8808 Fan Tray
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if group['description']:
                    name = group['fantray']
                    fantray_dict = ret_dict.setdefault('cooling_devices', {}).setdefault(name, {})
                    fantray_dict.update({
                        'name': name,
                        'product_id': group['product_id'],
                        'version': group['version'],
                        'serial_num': group['serial_num'],
                        'description': group['description']
                })
                else:
                    name = group['fantray']
                    fantray_dict = ret_dict.setdefault('cooling_devices', {}).setdefault(name, {})
                    fantray_dict.update({
                        'name': name,
                        'product_id': group['product_id'],
                        'version': group['version'],
                        'serial_num': group['serial_num'],
                    })
            
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
            m = p7.match(line) or p7_1.match(line) or p7_2.match(line)
            if m:
                group = m.groupdict()
                rp_info = group['rp_info']
                rp_info_dict = ret_dict.setdefault('fpds', {}).setdefault(rp_info, {})
                rp_info_dict.update({
                    'name': rp_info,
                    'version': group['version'],
                    'description': group['description'], 
                })
                continue

            # LC0                 88-LC0-36FH-MO  0.32                 FOC2431NVH1     Cisco 8800 36x400GE QSFP56-DD Line Card with MACsec
            m = p8.match(line)
            if m:
                group = m.groupdict()
                name = group['lc']
                lc_dict = ret_dict.setdefault('line_cards', {}).setdefault(name, {})
                lc_dict.update({
                    'name': name,
                    'product_id': group['product_id'],
                    'version': group['version'],
                    'serial_num': group['serial_num'],
                    'description': group['description'],  
                })
                continue

            # LC5 -- not present
            # LC6 Card type unknown; Board type unknown -- not initialized
            m = p9.match(line) or p10.match(line)
            if m:
                group = m.groupdict()
                name = group['lc']
                lc_dict = ret_dict.setdefault('line_cards', {}).setdefault(name, {})
                lc_dict.update({
                    'name': name,
                    'state': group['state'],
                })
                continue

            # FC0                 8808-FC0        1.0                  FOC2648NHKZ     Cisco 8808 Fabric Card for 14.4T Line Cards
            m = p11.match(line)
            if m:
                group = m.groupdict()
                name = group['fc']
                fc_dict = ret_dict.setdefault('fabric_cards', {}).setdefault(name, {})
                fc_dict.update({
                    'name': name,
                    'product_id': group['product_id'],
                    'version': group['version'],
                    'serial_num': group['serial_num'],
                    'description': group['description'],  
                })
                continue

            # LC5 -- not present
            m = p12.match(line)
            if m:
                group = m.groupdict()
                name = group['fc']
                fc_dict = ret_dict.setdefault('fabric_cards', {}).setdefault(name, {})
                fc_dict.update({
                    'name': name,
                    'state': group['state'],
                })
                continue

        return ret_dict
