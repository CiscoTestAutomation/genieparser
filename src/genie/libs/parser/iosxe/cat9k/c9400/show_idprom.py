'''show_idprom.py
IOSXE parsers for the following show commands:
    * show idprom all 
'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or 

# ==========================
# Schema for:
#  * 'show idprom all'
# ==========================
class ShowIdpromSchema(MetaParser):
    schema = {
        'idprom': {
            'midplane': {
                Optional('controller_type'): int,
                Optional('hardware_revision'): str,
                Optional('top_assy_part_number'): str,
                Optional('top_assy_revision'): str,
                Optional('deviation_number'): str,
                Optional('pcb_serial_number'): str,
                Optional('chassis_serial_number'): str,
                Optional('rma_test_history'): str,
                Optional('rma_number'): str,
                Optional('rma_history'): str,
                Optional('clei_code'): str,
                Optional('eci_number'): str,
                Optional('pid'): str,
                Optional('vid'): str,
                Optional('chassis_mac_address'): str
            },
            'supervisor': {
                Any(): {
                    Optional('controller_type'): int,
                    Optional('hardware_revision'): str,
                    Optional('top_assy_part_number'): str,
                    Optional('top_assy_revision'): str,
                    Optional('deviation_number'): str,
                    Optional('pcb_serial_number'): str,
                    Optional('rma_test_history'): str,
                    Optional('rma_number'): str,
                    Optional('rma_history'): str,
                    Optional('clei_code'): str,
                    Optional('eci_number'): str,
                    Optional('pid'): str,
                    Optional('vid'): str,
                    Optional('manufacturing_test_data'): str,
                    Optional('base_mac_address'): str,
                    Optional('field_diagnostics_data'): str,
                    Optional('environment_monitor_data'): str,
                    Optional('max_power_requirement_watts'): int,
                    Optional('typical_power_requirement_watts'): int
                }
            },
            'module': {
                Any(): {
                    Optional('controller_type'): int,
                    Optional('hardware_revision'): str,
                    Optional('top_assy_part_number'): str,
                    Optional('top_assy_revision'): str,
                    Optional('deviation_number'): str,
                    Optional('pcb_serial_number'): str,
                    Optional('rma_test_history'): str,
                    Optional('rma_number'): str,
                    Optional('rma_history'): str,
                    Optional('clei_code'): str,
                    Optional('eci_number'): str,
                    Optional('pid'): str,
                    Optional('vid'): str,
                    Optional('manufacturing_test_data'): str,
                    Optional('base_mac_address'): str,
                    Optional('field_diagnostics_data'): str,
                    Optional('environment_monitor_data'): str,
                    Optional('max_power_requirement_watts'): int,
                    Optional('typical_power_requirement_watts'): int
                }
            },
            'fantray': {
                Optional('controller_type'): int,
                Optional('hardware_revision'): str,
                Optional('top_assy_part_number'): str,
                Optional('top_assy_revision'): str,
                Optional('deviation_number'): str,
                Optional('pcb_serial_number'): str,
                Optional('chassis_serial_number'): str,
                Optional('rma_test_history'): str,
                Optional('rma_number'): str,
                Optional('rma_history'): str,
                Optional('clei_code'): str,
                Optional('eci_number'): str,
                Optional('pid'): str,
                Optional('vid'): str,
                Optional('manufacturing_test_data'): str,
                Optional('field_diagnostics_data'): str,
                Optional('environment_monitor_data'): str
            },
            'power_supply': {
                Any(): {
                    Optional('controller_type'): int,
                    Optional('hardware_revision'): str,
                    Optional('top_assy_part_number'): str,
                    Optional('top_assy_revision'): str,
                    Optional('deviation_number'): str,
                    Optional('pcb_serial_number'): str,
                    Optional('rma_test_history'): str,
                    Optional('rma_number'): str,
                    Optional('rma_history'): str,
                    Optional('clei_code'): str,
                    Optional('eci_number'): str,
                    Optional('pid'): str,
                    Optional('vid'): str,
                    Optional('power_supply_type'): str,
                    Optional('manufacturing_test_data'): str,
                    Optional('field_diagnostics_data'): str,
                    Optional('environment_monitor_data'): str,
                    Optional('max_power_output_at_220v'): int,
                    Optional('max_power_output_at_110v'): int
                }
            }
        }
    }

class ShowIdprom(ShowIdpromSchema):
    cli_command = ['show idprom all']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
            
        # initial variables
        ret_dict = {}
        
        # Midplane Idprom:
        p1 = re.compile(r'^Midplane +Idprom:$')
        
        #Supervisor 1 Idprom:
        p2 = re.compile(r'^Supervisor +(?P<number>\d+) +Idprom:$')
        
        #Module 1 Idprom:
        p3 = re.compile(r'^Module +(?P<number>\d+) +Idprom:$')
        
        #Fan Tray Idprom:
        p4 = re.compile(r'^Fan +Tray +Idprom:$')
        
        #Power Supply 1 Idprom:
        p5 = re.compile(r'^Power +Supply +(?P<number>\d+) +Idprom:$')

        #Controller Type          : 3232
        p6 = re.compile(r'^Controller +Type *: +(?P<controller_type>\S[\S ]*)$')
        
        #Hardware Revision        : 1.0
        p7 = re.compile(r'^Hardware +Revision *: +(?P<hardware_revision>\S[\S ]*)$')
        
        #Top Assy. Part Number    : 68-05859-01
        p8 = re.compile(r'^Top +Assy\. +Part +Number *: +(?P<top_assy_part_number>\S[\S ]*)$')
        
        #Top Assy. Revision       : B0
        p9 = re.compile(r'^Top +Assy\. +Revision *: +(?P<top_assy_revision>\S[\S ]*)$')
        
        #Deviation Number         : 0
        p10 = re.compile(r'^Deviation +Number *: +(?P<deviation_number>\d+)$')
        
        #PCB Serial Number        : FXS22410260
        p11 = re.compile(r'^PCB +Serial +Number *: +(?P<pcb_serial_number>\S[\S ]*)$')
        
        #Chassis Serial Number    : FXS2250Q63W
        p12 = re.compile(r'^Chassis +Serial +Number *: +(?P<chassis_serial_number>\S[\S ]*)$')
        
        #RMA Test History         : 00
        p13 = re.compile(r'^RMA +Test +History *: +(?P<rma_test_history>\S[\S ]*)$')
        
        #RMA Number               : 0-0-0-0
        p14 = re.compile(r'^RMA +Number *: +(?P<rma_number>\S[\S ]*)$')
        
        #RMA History              : 00
        p15 = re.compile(r'^RMA +History *: +(?P<rma_history>\S[\S ]*)$')
        
        #CLEI Code                : INM5T00ARA
        p16 = re.compile(r'^CLEI +Code *: +(?P<clei_code>\S[\S ]*)$')

        
        #ECI Number               : 472475
        p17 = re.compile(r'^ECI +Number *: +(?P<eci_number>\S[\S ]*)$')
    
        #Product Identifier (PID) : C9404R  
        p18= re.compile(r'^Product +Identifier +\(PID\) *: +(?P<pid>\S[\S ]*)$')
        
        #Version Identifier (VID) : V01 
        p19 = re.compile(r'^Version +Identifier +\(VID\) *: +(?P<vid>\S[\S ]*)$')
        
        #Chassis MAC Address      : 70ea.1aff.0300
        p20 = re.compile(r'^Chassis +MAC +Address *: +(?P<chassis_mac_address>\S[\S ]*)$')
        
        #Manufacturing Test Data  : 00 00 00 00 00 00 00 00
        p21 = re.compile(r'^Manufacturing +Test +Data *: +(?P<manufacturing_test_data>\S[\S ]*)$')
        
        #Base MAC Address         : D4 E8 80 38 58 C4 
        p22 = re.compile(r'^Base +MAC +Address *: +(?P<base_mac_address>\S[\S ]*)$')
        
        #Field Diagnostics Data   : 00 00 00 00 00 00 00 00 
        p23 = re.compile(r'^Field +Diagnostics +Data *: +(?P<field_diagnostics_data>\S[\S ]*)$')
        
        #Environment Monitor Data : 06 00 00 00 12 01 90 00 
        p24 = re.compile(r'^Environment +Monitor +Data *: +(?P<environment_monitor_data>\S[\S ]*)$')
        
        #Max Power Requirement    : 400 Watts
        p25 = re.compile(r'^Max +Power +Requirement *: +(?P<max_power_requirement_watts>\d+) +Watts$')
        
        #Typical Power Requirement: 288 Watts
        p26 = re.compile(r'^Typical +Power +Requirement *: +(?P<typical_power_requirement_watts>\d+) +Watts$')
        
        #Max Power Output at 220V : 3200 Watts
        p27 = re.compile(r'^Max +Power +Output +at +220V *: +(?P<max_power_output_at_220v>\d+) +Watts$')
        
        #Max Power Output at 110V : 1570 Watts
        p28 = re.compile(r'^Max +Power +Output +at +110V *: +(?P<max_power_output_at_110v>\d+) +Watts$')
        
        #Power Supply Type        : AC
        p29 = re.compile(r'^Power +Supply +Type *: +(?P<power_supply_type>\S[\S ]*)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Midplane Idprom:
            
            m = p1.match(line)
            if m:
                idprom_dict = ret_dict.setdefault('idprom', {}).setdefault('midplane', {})
                continue
            
            #Supervisor 1 Idprom:
            
            m = p2.match(line)
            if m:
                idprom_dict = ret_dict.setdefault('idprom', {}).setdefault('supervisor', {}).setdefault(m.group('number'), {})
                continue
            
            #Module 1 Idprom:
            
            m = p3.match(line)
            if m:
                idprom_dict = ret_dict.setdefault('idprom', {}).setdefault('module', {}).setdefault(m.group('number'), {})
                continue
            
            #Fan Tray Idprom:
            
            m = p4.match(line)
            if m:
                idprom_dict = ret_dict.setdefault('idprom', {}).setdefault('fantray', {})
                continue
            
            #Power Supply 1 Idprom:
            
            m = p5.match(line)
            if m:
                idprom_dict = ret_dict.setdefault('idprom', {}).setdefault('power_supply', {}).setdefault(m.group('number'), {})
                continue

            # Controller Type          : 3232
            m = p6.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'controller_type' : int(group['controller_type'])})
                continue
            
            # Hardware Revision        : 1.0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'hardware_revision' : group['hardware_revision']})
                continue
            
            # Top Assy. Part Number    : 68-05859-01
            m = p8.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'top_assy_part_number' : group['top_assy_part_number']})
                continue
            
            # Top Assy. Revision       : B0  
            m = p9.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'top_assy_revision' : group['top_assy_revision']})
                continue

            # Deviation Number         : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'deviation_number' : group['deviation_number']})
                continue
            
            # PCB Serial Number        : FXS22410260
            m = p11.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'pcb_serial_number' : group['pcb_serial_number']})
                continue

            # Chassis Serial Number    : FXS2250Q63W
            m = p12.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'chassis_serial_number' : group['chassis_serial_number']})
                continue

            # RMA Test History         : 00
            m = p13.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'rma_test_history' : group['rma_test_history']})
                continue

            # RMA Number               : 0-0-0-0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'rma_number' : group['rma_number']})
                continue

            # RMA History              : 00
            m = p15.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'rma_history' : group['rma_history']})
                continue

            # CLEI Code                : INM5T00ARA
            m = p16.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'clei_code' : group['clei_code']})
                continue

            # ECI Number               : 472475
            m = p17.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'eci_number' : group['eci_number']})
                continue

            # Product Identifier (PID) : C9404R
            m = p18.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'pid' : group['pid']})
                continue

            # Version Identifier (VID) : V01 
            m = p19.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'vid' : group['vid']})
                continue
            
            # Chassis MAC Address      : 70ea.1aff.0300
            m = p20.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'chassis_mac_address' : group['chassis_mac_address']})
                continue

            # Manufacturing Test Data  : 00 00 00 00 00 00 00 00
            m = p21.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'manufacturing_test_data' : group['manufacturing_test_data']})
                continue

            # Base MAC Address         : 70 6D 15 73 28 40 
            m = p22.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'base_mac_address' : group['base_mac_address']})
                continue

            #Environment Monitor Data : 06 00 00 00 03 E0 41 00 
	        #                           D6 
            m = p23.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'field_diagnostics_data' : group['field_diagnostics_data']})
                continue
            
            # Field Diagnostics Data   : 00 00 00 00 00 00 00 00
            m = p24.match(line)
            if m:
                group = m.groupdict()
                environment_monitor_data = group['environment_monitor_data']
                if 'environment_monitor_data' in idprom_dict.keys():
                    if len(idprom_dict['environment_monitor_data']) > len (environment_monitor_data):
                        pass
                    else:
                        idprom_dict.update({'environment_monitor_data' : environment_monitor_data})

                else:
                    idprom_dict.update({'environment_monitor_data' : environment_monitor_data})
                continue    
            
            # Max Power Requirement    : 65 Watts
            m = p25.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'max_power_requirement_watts' : int(group['max_power_requirement_watts'])})
                continue

            # Typical Power Requirement: 145 Watts
            m = p26.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'typical_power_requirement_watts' : int(group['typical_power_requirement_watts'])})
                continue
            
            # Max Power Output at 220V : 3200 Watts
            m = p27.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'max_power_output_at_220v' : int(group['max_power_output_at_220v'])})
                continue
            
            # Max Power Output at 110V : 1570 Watts
            m = p28.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'max_power_output_at_110v' : int(group['max_power_output_at_110v'])})
                continue

            # Power Supply Type        : AC
            m = p29.match(line)
            if m:
                group = m.groupdict()
                idprom_dict.update({'power_supply_type' : group['power_supply_type']})
                continue

        return ret_dict
