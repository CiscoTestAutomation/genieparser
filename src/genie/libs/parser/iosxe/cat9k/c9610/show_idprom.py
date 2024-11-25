'''show_idprom.py

IOSXE parsers for the following show commands:

    * show idprom all eeprom
'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or


class ShowIdpromEepromSchema(MetaParser):
    """Schema for 'show idprom all eeprom'"""
    schema = {
        'midplane': {
            'pid': str,
            'vid': str,
            'pcb_serial_number': str,
            'top_assy_revision': str,
            'hardware_revision': str,
            Optional('clei_code'): str
        },
        'power_fan_module': {
            Any(): {
                'pid': str,
                'vid': str,
                'pcb_serial_number': str,
                'top_assy_revision': str,
                'hardware_revision': str,
                Optional('clei_code'): str
            }
        },
        'slot': {
            Any(): {
                'pid': str,
                'vid': str,
                'pcb_serial_number': str,
                'top_assy_revision': str,
                'hardware_revision': str,
                Optional('clei_code'): str
            }
        },
        'spa': {
            Any(): {
                'pid': str,
                'vid': str,
                'pcb_serial_number': str,
                'top_assy_revision': str,
                'hardware_revision': str,
                'clei_code': str
            }
        }
    }

class ShowIdpromEeprom(ShowIdpromEepromSchema):
    """Parser for 'show idprom all eeprom'"""
    cli_command = 'show idprom all eeprom'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # MIDPLANE EEPROM data:
        p1 = re.compile(r'^MIDPLANE EEPROM data:$')

        # Power/Fan Module P5 EEPROM data:
        p2 = re.compile(r'^Power/Fan Module P(?P<number>\d+) EEPROM data:$')

        # Slot R0 EEPROM data:
        p3 = re.compile(r'^Slot R(?P<number>\d+) EEPROM data:$')

        # SPA EEPROM data for subslot 1/0:
        p4 = re.compile(r'^SPA EEPROM data for subslot (?P<slot>\d+/\d+):$')

        # Product Identifier (PID) : C9610R
        p5 = re.compile(r'^Product Identifier \(PID\) *: +(?P<pid>\S+)$')

        # Version Identifier (VID) : V00
        p6 = re.compile(r'^Version Identifier \(VID\) *: +(?P<vid>\S+)$')

        # PCB Serial Number        : FOC28101LZB
        p7 = re.compile(r'^PCB Serial Number *: +(?P<pcb_serial_number>\S+)$')

        # Top Assy. Revision       : 18
        p8 = re.compile(r'^Top Assy\. Revision *: +(?P<top_assy_revision>\S+)$')

        # Hardware Revision        : 0.2
        p9 = re.compile(r'^Hardware Revision *: +(?P<hardware_revision>\S+)$')

        # CLEI Code                :
        p10 = re.compile(r'^CLEI Code *: +(?P<clei_code>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # MIDPLANE EEPROM data:
            m = p1.match(line)
            if m:
                eeprom_dict = ret_dict.setdefault('midplane', {})
                continue
            
            # Power/Fan Module P5 EEPROM data:
            m = p2.match(line)
            if m:
                eeprom_dict = ret_dict.setdefault('power_fan_module', {}).setdefault(int(m.group('number')), {})
                continue
            
            # Slot R0 EEPROM data:
            m = p3.match(line)
            if m:
                eeprom_dict = ret_dict.setdefault('slot', {}).setdefault(int(m.group('number')), {})
                continue
            
            # SPA EEPROM data for subslot 1/0:
            m = p4.match(line)
            if m:
                eeprom_dict = ret_dict.setdefault('spa', {}).setdefault(m.group('slot'), {})
                continue
            
            # Product Identifier (PID) : C9610R
            m = p5.match(line)
            if m:
                eeprom_dict['pid'] = m.group('pid')
                continue

            # Version Identifier (VID) : V00
            m = p6.match(line)
            if m:
                eeprom_dict['vid'] = m.group('vid')
                continue
            
            # PCB Serial Number        : FOC28101LZB
            m = p7.match(line)
            if m:
                eeprom_dict['pcb_serial_number'] = m.group('pcb_serial_number')
                continue
            
            # Top Assy. Revision       : 18
            m = p8.match(line)
            if m:
                eeprom_dict['top_assy_revision'] = m.group('top_assy_revision')
                continue
            
            # Hardware Revision        : 0.2
            m = p9.match(line)
            if m:
                eeprom_dict['hardware_revision'] = m.group('hardware_revision')
                continue
            
            # CLEI Code                :
            m = p10.match(line)
            if m:
                eeprom_dict['clei_code'] = m.group('clei_code')
                continue
        
        return ret_dict
