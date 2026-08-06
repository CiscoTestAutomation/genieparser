''' show_inventory.py
IOSXR parsers for the following show commands:
    * show inventory raw
    * show inventory vendor-type
'''

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


class ShowInventoryRawSchema(MetaParser):
    """Schema for show inventory raw"""
    schema = {
        'module_name':
            {Any():
                {'descr': str,
                 'pid': str,
                 'vid': str,
                 'sn': str,
                },
            },
        }

class ShowInventoryRaw(ShowInventoryRawSchema):
    """Parser for show inventory raw"""

    cli_command = 'show inventory raw'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        inventory_dict = {}

        # NAME: "Rack 0", DESCR: "Cisco XRv9K Centralized Virtual Router"
        # NAME: "Rack 0", DESCR: "Cisco 8203 1RU System with 32x400GE QSFP56-DD & 12x100GE QSFP28"
        # NAME: "0/FT2-FAN_1_Speed", DESCR: "Fan Speed Sensor"
        # NAME: "0/FT4", DESCR: "Sherman Fan Module Reverse Airflow / exhaust, BLUE"
        # NAME: "Optics0/0/0/0-Tx Lane 0 Power", DESCR: "Power Sensor"
        p1 = re.compile(r'^NAME:\s+"(?P<module_name>[^"]+)",'
                        r'\s+DESCR:\s+"(?P<descr>[^"]+)"$')

        # PID: 8201-32FH         , VID: V00, SN: FOC2422NMRH
        # PID: 8202-32FH-M[FB]   , VID: N/A, SN: FLM252604RR
        # PID: N/A               , VID: N/A, SN: N/A
        # PID: PSU6.3KW-HV       , VID: V01, SN: DTM2339018G
        p2 = re.compile(r'^PID:\s+(?P<pid>[\w\/\.\-\[\]]+|N\/A)\s*,'
                        r' VID:\s+(?P<vid>[\w\/\-]+|N\/A)\s*,'
                        r' SN:\s+(?P<sn>[\w\/\-]+|N\/A)$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # NAME: "0/FT4", DESCR: "Sherman Fan Module Reverse Airflow / exhaust, BLUE"
            # NAME: "Optics0/0/0/0-Tx Lane 0 Power", DESCR: "Power Sensor"
            m = p1.match(line)
            if m:
                module_name = m.groupdict()['module_name']
                module_dict = inventory_dict.setdefault('module_name', {}).setdefault(module_name, {})
                module_dict['descr'] = m.groupdict()['descr']
                continue

            # PID: 8201-32FH         , VID: V00, SN: FOC2422NMRH
            # PID: 8202-32FH-M[FB]   , VID: N/A, SN: FLM252604RR
            m = p2.match(line)
            if m:
                module_dict.update({
                    "pid": m.groupdict()['pid'],
                    "vid": m.groupdict()['vid'],
                    "sn": m.groupdict()['sn']
                })

        return inventory_dict

class ShowInventoryVendorTypeSchema(MetaParser):
    """Schema for show inventory vendor-type"""
    schema = {
        'module_name':
            {Any():
                {'descr': str,
                 'pid': str,
                 'vid': str,
                 'sn': str,
                 'vendor_type': str,
                },
            },
        }

class ShowInventoryVendorType(ShowInventoryVendorTypeSchema):
    """Parser for show inventory vendor-type"""

    cli_command = 'show inventory vendor-type'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        inventory_dict = {}

        # NAME: "Rack 0", DESCR: "Cisco P200 64x800G OSFP 3RU Chassis"
        # NAME: "0/PM0", DESCR: "3000W AC/HVAC/HVDC Power Module with Port-side Air Intake"
        # NAME: "0/FT3", DESCR: "2RU Fan with Port-side Air Intake Ver3"
        # NAME: "EightHundredGigE0/0/0/7", DESCR: "Non-Cisco OSFP 2x400G FR4 Pluggable Optics Module"
        # NAME: "Optics0/0/0/8", DESCR: "Cisco OSFP 800G ZRP Pluggable Optics Module"
        p1 = re.compile(r'^NAME:\s+"(?P<module_name>[^"]+)",'
                        r'\s+DESCR:\s+"(?P<descr>[^"]+)"$')

        # PID: 8201-32FH         , VID: V00, SN: FOC2422NMRH
        # PID: 8202-32FH-M[FB]   , VID: N/A, SN: FLM252604RR
        # PID: N/A               , VID: N/A, SN: N/A
        # PID: EOLO-168HG-02-1T  , VID: 02, SN: UR4F270015
        # PID: OSFP-800G-DR8     , VID: V01 , SN: CGC29300681
        p2 = re.compile(r'^PID:\s+(?P<pid>[\w\/\.\-\[\]]+|N\/A)\s*,'
                        r' VID:\s+(?P<vid>[\w\/\-]+|N\/A)\s*,'
                        r' SN:\s+(?P<sn>[\w\/\-]+|N\/A)$')

        # Vendor Type: 1.3.6.1.4.1.9.12.3.1.9.155.5
        # Vendor Type: 1.3.6.1.4.1.9.12.3.1.9.2.882
        # Vendor Type: N/A
        p3 = re.compile(r'^Vendor Type:\s+(?P<vendor_type>[\w\.\-]+|N\/A)$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # NAME: "0/FT4", DESCR: "Sherman Fan Module Reverse Airflow / exhaust, BLUE"
            # NAME: "Optics0/0/0/0-Tx Lane 0 Power", DESCR: "Power Sensor"
            m = p1.match(line)
            if m:
                module_name = m.groupdict()['module_name']
                module_dict = inventory_dict.setdefault('module_name', {}).setdefault(module_name, {})
                module_dict['descr'] = m.groupdict()['descr']
                continue

            # PID: 8201-32FH         , VID: V00, SN: FOC2422NMRH
            # PID: 8202-32FH-M[FB]   , VID: N/A, SN: FLM252604RR
            m = p2.match(line)
            if m:
                module_dict.update({
                    "pid": m.groupdict()['pid'],
                    "vid": m.groupdict()['vid'],
                    "sn": m.groupdict()['sn']
                })
                continue

            # Vendor Type: 1.3.6.1.4.1.9.12.3.1.9.155.5
            # Vendor Type: 1.3.6.1.4.1.9.12.3.1.9.2.882
            m = p3.match(line)
            if m:
                module_dict['vendor_type'] = m.groupdict()['vendor_type']
                continue

        return inventory_dict
