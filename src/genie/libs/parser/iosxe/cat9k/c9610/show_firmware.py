''' show_firmware.py

IOSXE parsers for the following show commands:

    * show firmware version all
    * show firmware version [switch {switch_num}] fantray

'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowFirmwareVersionAllSchema(MetaParser):
    """
    Schema for show firmware version all
    """
    schema = {
        Optional('slot'): {
            Any(): {  
                Any(): {  
                    'device_name': str, 
                    Optional('current_firmware_version'): str,
                    Optional('bundled_firmware_version'): str,
                    Optional('mismatch'): str,
                    Optional('components'): {
                        Any(): {
                            'current_firmware_version': str,
                            'bundled_firmware_version': str,
                            'mismatch': str
                        }
                    }
                }
            }
        }
    }

class ShowFirmwareVersionAll(ShowFirmwareVersionAllSchema):
    """
    Parser for show firmware version all
    """

    cli_command = 'show firmware version all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # 6    Supervisor Rommon (Active)    17.18.1r              N/A                 N/A
        p1 = re.compile(r'^\s*(?P<slot>\S+)\s+(?P<device_name>.*?)\s+(?P<current>\S+)\s+(?P<bundled>\S+)\s+(?P<mismatch>\S+)\s*$')
        
        # Sup IOFPGA                  25060231              25060231            No
        p2 = re.compile(r'^\s+(?P<component_name>.*?)\s+(?P<current>\S+)\s+(?P<bundled>\S+)\s+(?P<mismatch>\S+)\s*$')
        
        # 6    Supervisor (Active)
        p3 = re.compile(r'^\s*(?P<slot>\S+)\s+(?P<device_name>.*?)\s*$')

        current_slot = None
        current_device_key = None
        device_counter = {}  # To track multiple devices per slot
        
        for line in output.splitlines():
            line = line.rstrip()
            
            # Skip header lines, separators, and empty lines
            if (line.startswith('Slot') or line.startswith('-----') or 
                line.startswith('Current') or line.startswith('===')):
                continue
                
            # Skip empty lines
            if not line.strip():
                continue
                
            # Skip power supply lines
            if 'Power Supply' in line:
                continue
            
            # Sup IOFPGA                  25060231              25060231            No
            m2 = p2.match(line)
            if m2 and current_slot and current_device_key and len(line) - len(line.lstrip()) > 4:
                component_name = m2.group('component_name').strip()
                current = m2.group('current')
                bundled = m2.group('bundled')
                mismatch = m2.group('mismatch')
                
                if 'components' not in ret_dict['slot'][current_slot][current_device_key]:
                    ret_dict['slot'][current_slot][current_device_key]['components'] = {}
                
                ret_dict['slot'][current_slot][current_device_key]['components'][component_name] = {
                    'current_firmware_version': current,
                    'bundled_firmware_version': bundled,
                    'mismatch': mismatch
                }
                continue
            
            # 6    Supervisor Rommon (Active)    17.18.1r              N/A                 N/A
            m1 = p1.match(line)
            if m1:
                slot = m1.group('slot')
                device_name = m1.group('device_name').strip()
                current = m1.group('current')
                bundled = m1.group('bundled')
                mismatch = m1.group('mismatch')
                
                # Initialize slot structure
                if 'slot' not in ret_dict:
                    ret_dict['slot'] = {}
                if slot not in ret_dict['slot']:
                    ret_dict['slot'][slot] = {}
                    device_counter[slot] = 0
                
                # Create unique device key
                device_counter[slot] += 1
                device_key = str(device_counter[slot])
                
                ret_dict['slot'][slot][device_key] = {
                    'device_name': device_name,
                    'current_firmware_version': current,
                    'bundled_firmware_version': bundled,
                    'mismatch': mismatch
                }
                
                current_slot = slot
                current_device_key = device_key
                continue
            
            # 6    Supervisor (Active)
            m3 = p3.match(line)
            if m3:
                slot = m3.group('slot')
                device_name = m3.group('device_name').strip()
                
                # Initialize slot structure
                if 'slot' not in ret_dict:
                    ret_dict['slot'] = {}
                if slot not in ret_dict['slot']:
                    ret_dict['slot'][slot] = {}
                    device_counter[slot] = 0
                
                # Create unique device key
                device_counter[slot] += 1
                device_key = str(device_counter[slot])
                
                ret_dict['slot'][slot][device_key] = {
                    'device_name': device_name
                }
                
                current_slot = slot
                current_device_key = device_key
                continue

        return ret_dict

class ShowFirmwareVersionFantraySchema(MetaParser):
    """
    Schema for show firmware version [switch {switch_num}] fantray
    """
    schema = {
        'fantray': {
            Any(): {
                'device_name': str,
                'current_firmware_version': str,
                'bundled_firmware_version': str,
                'mismatch': str
            }
        }
    }

class ShowFirmwareVersionFantray(ShowFirmwareVersionFantraySchema):
    """
    Parser for show firmware version [switch {switch_num}] fantray
    """

    cli_command = [
        'show firmware version switch {switch_num} fantray',
        'show firmware version fantray'
    ]

    def cli(self, switch_num=None, output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[0].format(switch_num=switch_num)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        fantray_dict = {}

        # FT1  Fantray  25010624  25010624  No
        p1 = re.compile(
            r'^(?P<slot>FT\d+)\s+(?P<device_name>\S+)\s+(?P<current>\S+)\s+(?P<bundled>\S+)\s+(?P<mismatch>\S+)$'
        )

        for line in output.splitlines():
            line = line.strip()
            
            # FT1  Fantray  25010624  25010624  No
            m = p1.match(line)
            if m:
                slot = m.group('slot')
                fantray_dict[slot] = {
                    'device_name': m.group('device_name'),
                    'current_firmware_version': m.group('current'),
                    'bundled_firmware_version': m.group('bundled'),
                    'mismatch': m.group('mismatch')
                }

        if fantray_dict:
            ret_dict['fantray'] = fantray_dict

        return ret_dict
