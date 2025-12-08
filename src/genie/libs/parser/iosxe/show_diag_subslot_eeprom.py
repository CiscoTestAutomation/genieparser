'''show_diag_subslot_eeprom.py

IOSXE parsers for the following show commands:

    * show diag subslot {subslot} eeprom detail
    * show diag subslot {subslot} eeprom
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or


class ShowDiagSubslotEepromDetailSchema(MetaParser):
    """Schema for 'show diag subslot {subslot} eeprom detail'"""
    
    schema = {
        'spa_eeprom_data': {
            Any(): {  # subslot like '0/1'
                'eeprom_version': int,
                'compatible_type': str,
                'controller_type': int,
                'hardware_revision': str,
                'pcb_part_number': str,
                'deviation_number': int,
                'fab_version': str,
                'fab_part_number': str,
                'pcb_serial_number': str,
                'rma_test_history': str,
                'rma_number': str,
                'rma_history': str,
                'product_identifier_pid': str,
                'version_identifier_vid': str,
                'clei_code': str,
                'top_assy_part_number': str,
                'board_revision': str,
                'environment_monitor_data': str,
                'base_mac_address': str,
                'mac_address_block_size': int,
                'platform_features': str,
                Optional('manufacturing_test_data'): str,
            }
        },
        Optional('eeprom_data'): {
            Any(): {  # slot/bay/daughter_board like 'slot_0_bay_1_daughter_board_1'
                'eeprom_version': int,
                'compatible_type': str,
                'controller_type': int,
                'hardware_revision': str,
                'pcb_part_number': str,
                'board_revision': str,
                'fab_version': str,
                'fab_part_number': str,
                'deviation_number': int,
                'pcb_serial_number': str,
                'rma_test_history': str,
                'rma_number': str,
                'rma_history': str,
                'product_identifier_pid': str,
                'version_identifier_vid': str,
                'clei_code': str,
                'top_assy_part_number': str,
                'environment_monitor_data': str,
                'base_mac_address': str,
                'mac_address_block_size': int,
                'platform_features': str,
                Optional('manufacturing_test_data'): str,
            }
        }
    }


class ShowDiagSubslotEepromDetail(ShowDiagSubslotEepromDetailSchema):
    """Parser for 'show diag subslot {subslot} eeprom detail'"""
    
    cli_command = 'show diag subslot {subslot} eeprom detail'
    
    def cli(self, subslot=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(subslot=subslot))
        
        ret_dict = {}
        current_dict = None
        current_section = None
        
        # SPA EEPROM data for subslot 0/1:
        p1 = re.compile(r'^SPA EEPROM data for subslot (?P<subslot>\d+/\d+):$')
        
        # EEPROM data for slot 0 bay 1 daughter board 1
        p2 = re.compile(r'^EEPROM data for slot (?P<slot>\d+) bay (?P<bay>\d+) daughter board (?P<daughter_board>\d+)$')
        
        # EEPROM version           : 4
        p3 = re.compile(r'^\s*EEPROM version\s+:\s+(?P<eeprom_version>\d+)$')
        
        # Compatible Type          : 0xFF
        p4 = re.compile(r'^\s*Compatible Type\s+:\s+(?P<compatible_type>\S+)$')
        
        # Controller Type          : 1923
        p5 = re.compile(r'^\s*Controller Type\s+:\s+(?P<controller_type>\d+)$')
        
        # Hardware Revision        : 1.0
        p6 = re.compile(r'^\s*Hardware Revision\s+:\s+(?P<hardware_revision>\S+)$')
        
        # PCB Part Number          : 73-14506-06
        p7 = re.compile(r'^\s*PCB Part Number\s+:\s+(?P<pcb_part_number>\S+)$')
        
        # Deviation Number         : 0
        p8 = re.compile(r'^\s*Deviation Number\s+:\s+(?P<deviation_number>\d+)$')
        
        # Fab Version              : 04
        p9 = re.compile(r'^\s*Fab Version\s+:\s+(?P<fab_version>\S+)$')
        
        # Fab Part Number          : 28-10841-04
        p10 = re.compile(r'^\s*Fab Part Number\s+:\s+(?P<fab_part_number>\S+)$')
        
        # PCB Serial Number        : FOC21131QPE
        p11 = re.compile(r'^\s*PCB Serial Number\s+:\s+(?P<pcb_serial_number>\S+)$')
        
        # RMA Test History         : 00
        p12 = re.compile(r'^\s*RMA Test History\s+:\s+(?P<rma_test_history>\S+)$')
        
        # RMA Number               : 0-0-0-0
        p13 = re.compile(r'^\s*RMA Number\s+:\s+(?P<rma_number>[\d\-]+)$')
        
        # RMA History              : 00
        p14 = re.compile(r'^\s*RMA History\s+:\s+(?P<rma_history>\S+)$')
        
        # Product Identifier (PID) : NIM-4MFT-T1/E1
        p15 = re.compile(r'^\s*Product Identifier \(PID\)\s+:\s+(?P<product_identifier_pid>\S+)$')
        
        # Version Identifier (VID) : V04
        p16 = re.compile(r'^\s*Version Identifier \(VID\)\s+:\s+(?P<version_identifier_vid>\S+)$')
        
        # CLEI Code                : IP9IAWACAB
        p17 = re.compile(r'^\s*CLEI Code\s+:\s+(?P<clei_code>\S+)$')
        
        # Top Assy. Part Number    : 800-38530-06
        p18 = re.compile(r'^\s*Top Assy\. Part Number\s+:\s+(?P<top_assy_part_number>\S+)$')
        
        # Board Revision           : A0
        p19 = re.compile(r'^\s*Board Revision\s+:\s+(?P<board_revision>\S+)$')
        
        # Environment Monitor Data : 40 02 61 43 00 07
        p20 = re.compile(r'^\s*Environment Monitor Data\s+:\s+(?P<environment_monitor_data>[\w\s]+)$')
        
        # Base MAC Address         : 88 90 8D DD C5 9A
        p21 = re.compile(r'^\s*Base MAC Address\s+:\s+(?P<base_mac_address>[\w\s]+)$')
        
        # MAC Address block size   : 2
        p22 = re.compile(r'^\s*MAC Address block size\s+:\s+(?P<mac_address_block_size>\d+)$')
        
        # Platform features        : 02 01 01 07 01 00 00 00
        #                           01 01 00
        p23 = re.compile(r'^\s*Platform features\s+:\s+(?P<platform_features>[\w\s]+)$')
        p23_cont = re.compile(r'^\s+(?P<platform_features_cont>[\w\s]+)$')
        # Additional pattern for non-indented hex continuation (like "01 03 00")
        p23_cont_hex = re.compile(r'^(?P<platform_features_cont>[\dA-Fa-f\s]+)$')
        
        # Manufacturing Test Data  : 00 00 00 00 00 00 00 00
        p24 = re.compile(r'^\s*Manufacturing Test Data\s+:\s+(?P<manufacturing_test_data>[\w\s]+)$')
        
        platform_features_buffer = None
        
        for line in output.splitlines():
            line = line.rstrip()
            
            # SPA EEPROM data for subslot 0/1:
            m = p1.match(line)
            if m:
                subslot = m.group('subslot')
                spa_dict = ret_dict.setdefault('spa_eeprom_data', {})
                current_dict = spa_dict.setdefault(subslot, {})
                current_section = 'spa'
                platform_features_buffer = None
                continue
            
            # EEPROM data for slot 0 bay 1 daughter board 1
            m = p2.match(line)
            if m:
                slot = m.group('slot')
                bay = m.group('bay')
                daughter_board = m.group('daughter_board')
                key = f"slot_{slot}_bay_{bay}_daughter_board_{daughter_board}"
                eeprom_dict = ret_dict.setdefault('eeprom_data', {})
                current_dict = eeprom_dict.setdefault(key, {})
                current_section = 'eeprom'
                platform_features_buffer = None
                continue
            
            if current_dict is None:
                continue
            
            # EEPROM version           : 4
            m = p3.match(line)
            if m:
                current_dict['eeprom_version'] = int(m.group('eeprom_version'))
                continue
            
            # Compatible Type          : 0xFF
            m = p4.match(line)
            if m:
                current_dict['compatible_type'] = m.group('compatible_type')
                continue
            
            # Controller Type          : 1923
            m = p5.match(line)
            if m:
                current_dict['controller_type'] = int(m.group('controller_type'))
                continue
            
            # Hardware Revision        : 1.0
            m = p6.match(line)
            if m:
                current_dict['hardware_revision'] = m.group('hardware_revision')
                continue
            
            # PCB Part Number          : 73-14506-06
            m = p7.match(line)
            if m:
                current_dict['pcb_part_number'] = m.group('pcb_part_number')
                continue
            
            # Deviation Number         : 0
            m = p8.match(line)
            if m:
                current_dict['deviation_number'] = int(m.group('deviation_number'))
                continue
            
            # Fab Version              : 04
            m = p9.match(line)
            if m:
                current_dict['fab_version'] = m.group('fab_version')
                continue
            
            # Fab Part Number          : 28-10841-04
            m = p10.match(line)
            if m:
                current_dict['fab_part_number'] = m.group('fab_part_number')
                continue
            
            # PCB Serial Number        : FOC21131QPE
            m = p11.match(line)
            if m:
                current_dict['pcb_serial_number'] = m.group('pcb_serial_number')
                continue
            
            # RMA Test History         : 00
            m = p12.match(line)
            if m:
                current_dict['rma_test_history'] = m.group('rma_test_history')
                continue
            
            # RMA Number               : 0-0-0-0
            m = p13.match(line)
            if m:
                current_dict['rma_number'] = m.group('rma_number')
                continue
            
            # RMA History              : 00
            m = p14.match(line)
            if m:
                current_dict['rma_history'] = m.group('rma_history')
                continue
            
            # Product Identifier (PID) : NIM-4MFT-T1/E1
            m = p15.match(line)
            if m:
                current_dict['product_identifier_pid'] = m.group('product_identifier_pid')
                continue
            
            # Version Identifier (VID) : V04
            m = p16.match(line)
            if m:
                current_dict['version_identifier_vid'] = m.group('version_identifier_vid')
                continue
            
            # CLEI Code                : IP9IAWACAB
            m = p17.match(line)
            if m:
                current_dict['clei_code'] = m.group('clei_code')
                continue
            
            # Top Assy. Part Number    : 800-38530-06
            m = p18.match(line)
            if m:
                current_dict['top_assy_part_number'] = m.group('top_assy_part_number')
                continue
            
            # Board Revision           : A0
            m = p19.match(line)
            if m:
                current_dict['board_revision'] = m.group('board_revision')
                continue
            
            # Environment Monitor Data : 40 02 61 43 00 07
            m = p20.match(line)
            if m:
                current_dict['environment_monitor_data'] = m.group('environment_monitor_data').strip()
                continue
            
            # Base MAC Address         : 88 90 8D DD C5 9A
            m = p21.match(line)
            if m:
                current_dict['base_mac_address'] = m.group('base_mac_address').strip()
                continue
            
            # MAC Address block size   : 2
            m = p22.match(line)
            if m:
                current_dict['mac_address_block_size'] = int(m.group('mac_address_block_size'))
                continue
            
            # Platform features        : 02 01 01 07 01 00 00 00
            m = p23.match(line)
            if m:
                platform_features_buffer = m.group('platform_features').strip()
                continue
            
            # Platform features continuation line
            if platform_features_buffer is not None:
                m = p23_cont.match(line) or p23_cont_hex.match(line)
                if m:
                    platform_features_buffer += " " + m.group('platform_features_cont').strip()
                    continue
                else:
                    # Not a continuation line, save the platform features
                    current_dict['platform_features'] = platform_features_buffer
                    platform_features_buffer = None
            
            # Manufacturing Test Data  : 00 00 00 00 00 00 00 00
            m = p24.match(line)
            if m:
                current_dict['manufacturing_test_data'] = m.group('manufacturing_test_data').strip()
                platform_features_buffer = None
                continue
        
        # Handle case where platform_features is the last field
        if platform_features_buffer is not None and current_dict is not None:
            current_dict['platform_features'] = platform_features_buffer
        
        return ret_dict

class ShowDiagSubslotEepromSchema(MetaParser):
    """Schema for 'show diag subslot {subslot} eeprom'"""
    
    schema = {
        'spa_eeprom_data': {
            Any(): {  # subslot like '1/0'
                'product_identifier_pid': str,
                'version_identifier_vid': str,
                'pcb_serial_number': str,
                'hardware_revision': str,
                'clei_code': str,
            }
        }
    }

class ShowDiagSubslotEeprom(ShowDiagSubslotEepromSchema):
    """Parser for 'show diag subslot {subslot} eeprom'"""
    
    cli_command = 'show diag subslot {subslot} eeprom'
    
    def cli(self, subslot=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(subslot=subslot))
        
        ret_dict = {}
        
        # SPA EEPROM data for subslot 1/0:
        p1 = re.compile(r'^SPA EEPROM data for subslot (?P<subslot>\d+/\d+):$')
        
        # Product Identifier (PID) : SM-X-ES3-24-P
        p2 = re.compile(r'^\s*Product Identifier \(PID\)\s+:\s+(?P<product_identifier_pid>\S+)$')
        
        # Version Identifier (VID) : V01
        p3 = re.compile(r'^\s*Version Identifier \(VID\)\s+:\s+(?P<version_identifier_vid>\S+)$')
        
        # PCB Serial Number        : FOC21484UY5
        p4 = re.compile(r'^\s*PCB Serial Number\s+:\s+(?P<pcb_serial_number>\S+)$')
        
        # Hardware Revision        : 1.0
        p5 = re.compile(r'^\s*Hardware Revision\s+:\s+(?P<hardware_revision>\S+)$')
        
        # CLEI Code                : IP3CAAECAA
        p6 = re.compile(r'^\s*CLEI Code\s+:\s+(?P<clei_code>\S+)$')
        
        current_dict = None
        
        for line in output.splitlines():
            line = line.rstrip()
            
            # SPA EEPROM data for subslot 1/0:
            m = p1.match(line)
            if m:
                subslot = m.group('subslot')
                spa_dict = ret_dict.setdefault('spa_eeprom_data', {})
                current_dict = spa_dict.setdefault(subslot, {})
                continue
            
            if current_dict is None:
                continue
            
            # Product Identifier (PID) : SM-X-ES3-24-P
            m = p2.match(line)
            if m:
                current_dict['product_identifier_pid'] = m.group('product_identifier_pid')
                continue
            
            # Version Identifier (VID) : V01
            m = p3.match(line)
            if m:
                current_dict['version_identifier_vid'] = m.group('version_identifier_vid')
                continue
            
            # PCB Serial Number        : FOC21484UY5
            m = p4.match(line)
            if m:
                current_dict['pcb_serial_number'] = m.group('pcb_serial_number')
                continue
            
            # Hardware Revision        : 1.0
            m = p5.match(line)
            if m:
                current_dict['hardware_revision'] = m.group('hardware_revision')
                continue
            
            # CLEI Code                : IP3CAAECAA
            m = p6.match(line)
            if m:
                current_dict['clei_code'] = m.group('clei_code')
                continue
        
        return ret_dict
