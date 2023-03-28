'''show_idprom.py

IOSXE parsers for the following show commands:

    * show idprom all 
	* show idprom interface {interface}
'''

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

import re


# ==========================
# Schema for:
#  * 'show idprom all'
# ==========================
class ShowIdpromSchema(MetaParser):
    
    """
    Schema for:
        show idprom all

    """

    schema = {
        'switch': {
            Any() : {
                'module_idprom' : {
                    Any(): {
                        'controller_type' : str,
                        'hardware_revision' : str,
                        'top_assy_part_number' : str,
                        'top_assy_revision': str,
                        'pcb_part_number': str,
                        'board_revision' : str,
                        'deviation_number' : int,
                        'pcb_serial_number' : str,
                        'rma_test_history' : str,
                        'rma_number' : str,
                        'rma_history' : str,
                        'clei_code' : str,
                        'pid' : str,
                        'vid' : str,
                        'manufacturing_test_data': str,
                        'base_mac_address': str,
                        'environment_monitor_data' : str,
                        'max_power_requirement_watts' : int,
                        'typical_power_requirement_watts' : int,

                    }
                },

                'power_supply_idprom':{
                    Any(): {
                        'controller_type' : str,
                        'hardware_revision' : str,
                        'top_assy_part_number' : str,
                        'top_assy_revision': str,
                        'deviation_number' : int,

                        'pcb_serial_number' : str,
                        'rma_test_history' : str,
                        'rma_number' : str,
                        'rma_history' : str,
                        'clei_code' : str,
                        'pid' : str,
                        'vid' : str,
                        'manufacturing_test_data': str,
                        'field_diagnostics_data' : str,
                        'environment_monitor_data' : str,

                        'max_power_output_watts' : int
                    }                    
                } ,

                'fantray_idprom' : {
                   Any(): {
                        'controller_type' : str,
                        'hardware_revision' : str,
                        'top_assy_part_number' : str,
                        'top_assy_revision': str,
                        'deviation_number' : int,

                        'pcb_serial_number' : str,
                        'clei_code' : str,
                        'pid' : str,
                        'vid' : str,
                        'manufacturing_test_data': str,
                    }                     
                }
            }
        }
    }

# ==========================
# Parser for:
#  * 'show idprom all'
# ==========================
class ShowIdprom(ShowIdpromSchema):
    '''
    Parser for 
        show idprom all
    '''

    cli_command = ['show idprom all']

    def cli(self, output = None):
        # checking for output, else generating one
        if not output: 
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # output dictionary initialised
        result_dict = {}

        # possible regex patterns below:

        # Switch Number: 1 
        pSwitch = re.compile(r'^Switch +Number: +(?P<switch>\S[\S ]*)$')

        # Module 1 Idprom:
        pModule = re.compile(r'^Module +(?P<number>\S[\S ]*) +Idprom:$')

        # Power Supply 0 Idprom:
        pPowerSupply = re.compile(r'^Power +Supply +(?P<number>\S[\S ]*) +Idprom:$')

        # Fantray 0 Idprom:
        pFantray = re.compile(r'^Fantray +(?P<number>\S[\S ]*) +Idprom:$')

        # Controller Type          : 4371
        pControllerType = re.compile(r'^Controller +Type *: +(?P<controller_type>\S[\S ]*)$')

        # Hardware Revision        : 0.2
        pHardwareRevision = re.compile(r'^Hardware +Revision *: +(?P<hardware_revision>\S[\S ]*)$')

        # Top Assy. Part Number    : 68-103001-01
        pTopAssyPartNumber = re.compile(r'^Top +Assy\. +Part +Number *: +(?P<top_assy_part_number>\S[\S ]*)$')

        # Top Assy. Revision       : 10  
        pTopAssyRevision = re.compile(r'^Top +Assy\. +Revision *: +(?P<top_assy_revision>\S[\S ]*)$')

        # PCB Part Number          : 73-19902-02
        pPcbPartNumber = re.compile(r'^PCB +Part +Number *: +(?P<pcb_part_number>\S[\S ]*)$')

        # Board Revision           : 14   
        pBoardRevision = re.compile(r'^Board +Revision *: +(?P<board_revision>\S[\S ]*)$')

        # Deviation Number         : 0
        pDeviationNumber = re.compile(r'^Deviation +Number *: +(?P<deviation_number>\S[\S ]*)$')

        # PCB Serial Number        : FDO25130VES
        pPcbSerialNumber = re.compile(r'^PCB +Serial +Number *: +(?P<pcb_serial_number>\S[\S ]*)$')

        # RMA Test History         : 00
        pRmaTestHistory = re.compile(r'^RMA +Test +History *: +(?P<rma_test_history>\S[\S ]*)$')

        # RMA Number               : 0-0-0-0
        pRmaNumber = re.compile(r'^RMA +Number *: +(?P<rma_number>\S[\S ]*)$')

        # RMA History              : 00
        pRmaHistory = re.compile(r'^RMA +History *: +(?P<rma_history>\S[\S ]*)$')

        # CLEI Code                : TBD 
        pCleiCode = re.compile(r'^CLEI +Code *: +(?P<clei_code>\S[\S ]*)$')

        # Product Identifier (PID) : C9500X-28C8D
        pPid = re.compile(r'^Product +Identifier +\(PID\) *: +(?P<pid>\S[\S ]*)$')

        # Version Identifier (VID) : V00
        pVid = re.compile(r'^Version +Identifier +\(VID\) *: +(?P<vid>\S[\S ]*)$')

        # Manufacturing Test Data  : 00 00 00 00 00 00 00 00 
        pManufacturingTestData = re.compile(r'^Manufacturing +Test +Data *: +(?P<manufacturing_test_data>\S[\S ]*)$')

        # Base MAC Address         : 28 AF FD BE 94 00  
        pBaseMacAddress = re.compile(r'^Base +MAC +Address *: +(?P<base_mac_address>\S[\S ]*)$')

        # Environment Monitor Data : 06 00 00 00 0C 30 C3 00  
        pEnvironmentMonitorData = re.compile(r'^Environment +Monitor +Data *: +(?P<environment_monitor_data>\S[\S ]*)$')

        # Max Power Requirement    : 195 Watts
        pMaxPowerRequirementWatts = re.compile(r'^Max +Power +Requirement *: +(?P<max_power_requirement_watts>\d+) +Watts$')

        # Typical Power Requirement: 195 Watt
        pTypicalPowerRequirementWatts = re.compile(r'^Typical +Power +Requirement *: +(?P<typical_power_requirement_watts>\d+) +Watts$')

        # Field Diagnostics Data   : 00 00 00 00 00 00 00 00 
        pFieldDiagnosticsData = re.compile(r'^Field +Diagnostics +Data +: +(?P<field_diagnostics_data>\S[\S ]*)$')

        # Max Power Output         : 1500 Watts
        pMaxPowerOutputWatts = re.compile(r'^Max +Power +Output *: +(?P<max_power_output_watts>\d*) +Watts$')

        # Output parsing starts now:

        for line in out.splitlines():
            line = line.strip()

            m = pSwitch.match(line)

            if m: 
                group = m.groupdict()
                switch = group['switch']
                switch_dict = result_dict.setdefault('switch', {})
                switch_id_dict = switch_dict.setdefault(switch, {})
                continue

            m = pModule.match(line)

            if m:
                group = m.groupdict()
                number = group['number']
                idprom_type_dict = switch_id_dict.setdefault('module_idprom', {})
                idprom_type_id_dict = idprom_type_dict.setdefault(number, {})
                continue

            m = pPowerSupply.match(line)

            if m:
                group = m.groupdict()
                number = group['number']
                idprom_type_dict = switch_id_dict.setdefault('power_supply_idprom', {})
                idprom_type_id_dict = idprom_type_dict.setdefault(number, {})
                continue

            m = pFantray.match(line)

            if m:
                group = m.groupdict()
                number = group['number']
                idprom_type_dict = switch_id_dict.setdefault('fantray_idprom', {})
                idprom_type_id_dict = idprom_type_dict.setdefault(number, {})
                continue

            m = pControllerType.match(line)

            if m:
                group = m.groupdict()
                controller_type = group['controller_type']
                idprom_type_id_dict.update({'controller_type' : controller_type})
                continue

            m = pHardwareRevision.match(line)

            if m:
                group = m.groupdict()
                hardware_revision = group['hardware_revision']
                idprom_type_id_dict.update({'hardware_revision' : hardware_revision})
                continue

            m = pTopAssyPartNumber.match(line)

            if m:
                group = m.groupdict()
                top_assy_part_number = group['top_assy_part_number']
                idprom_type_id_dict.update({'top_assy_part_number' : top_assy_part_number})
                continue

            m = pTopAssyRevision.match(line)

            if m:
                group = m.groupdict()
                top_assy_revision = group['top_assy_revision']
                idprom_type_id_dict.update({'top_assy_revision' : top_assy_revision})
                continue

            m = pPcbPartNumber.match(line)

            if m:
                group = m.groupdict()
                pcb_part_number = group['pcb_part_number']
                idprom_type_id_dict.update({'pcb_part_number' : pcb_part_number})
                continue

            m = pBoardRevision.match(line)

            if m:
                group = m.groupdict()
                board_revision = group['board_revision']
                idprom_type_id_dict.update({'board_revision' : board_revision})
                continue

            m = pDeviationNumber.match(line)

            if m:
                group = m.groupdict()
                deviation_number = group['deviation_number']
                idprom_type_id_dict.update({'deviation_number' : int(deviation_number)})
                continue    

            m = pPcbSerialNumber.match(line)

            if m:
                group = m.groupdict()
                pcb_serial_number = group['pcb_serial_number']
                idprom_type_id_dict.update({'pcb_serial_number' : pcb_serial_number})
                continue

            m = pRmaTestHistory.match(line)

            if m:
                group = m.groupdict()
                rma_test_history = group['rma_test_history']
                idprom_type_id_dict.update({'rma_test_history' : rma_test_history})
                continue

            m = pRmaNumber.match(line)

            if m:
                group = m.groupdict()
                rma_number = group['rma_number']
                idprom_type_id_dict.update({'rma_number' : rma_number})
                continue

            m = pRmaHistory.match(line)

            if m:
                group = m.groupdict()
                rma_history = group['rma_history']
                idprom_type_id_dict.update({'rma_history' : rma_history})
                continue

            m = pCleiCode.match(line)

            if m:
                group = m.groupdict()
                clei_code = group['clei_code']
                idprom_type_id_dict.update({'clei_code' : clei_code})
                continue

            m = pPid.match(line)

            if m:
                group = m.groupdict()
                pid = group['pid']
                idprom_type_id_dict.update({'pid' : pid})
                continue

            m = pVid.match(line)

            if m:
                group = m.groupdict()
                vid = group['vid']
                idprom_type_id_dict.update({'vid' : vid})
                continue

            m = pManufacturingTestData.match(line)

            if m:
                group = m.groupdict()
                manufacturing_test_data = group['manufacturing_test_data']
                idprom_type_id_dict.update({'manufacturing_test_data' : manufacturing_test_data})
                continue

            m = pBaseMacAddress.match(line)
    
            if m:
                group = m.groupdict()
                base_mac_address = group['base_mac_address']
                idprom_type_id_dict.update({'base_mac_address' : base_mac_address})
                continue

            m = pEnvironmentMonitorData.match(line)
            
            if m:
                group = m.groupdict()
                environment_monitor_data = group['environment_monitor_data']
                if 'environment_monitor_data' in idprom_type_id_dict.keys():
                    if len(idprom_type_id_dict['environment_monitor_data']) > len (environment_monitor_data):
                        pass
                    else:
                        idprom_type_id_dict.update({'environment_monitor_data' : environment_monitor_data})

                else:
                    idprom_type_id_dict.update({'environment_monitor_data' : environment_monitor_data})
                continue    

            m = pMaxPowerRequirementWatts.match(line)

            if m:
                group = m.groupdict()
                max_power_requirement_watts = group['max_power_requirement_watts']
                idprom_type_id_dict.update({'max_power_requirement_watts' : int(max_power_requirement_watts)})
                continue
            
            m = pTypicalPowerRequirementWatts.match(line)

            if m:
                group = m.groupdict()
                typical_power_requirement_watts = group['typical_power_requirement_watts']
                idprom_type_id_dict.update({'typical_power_requirement_watts' : int(typical_power_requirement_watts)})
                continue

            m = pFieldDiagnosticsData.match(line)

            if m:
                group = m.groupdict()
                field_diagnostics_data = group['field_diagnostics_data']
                idprom_type_id_dict.update({'field_diagnostics_data' : field_diagnostics_data})
                continue

            m = pMaxPowerOutputWatts.match(line)

            if m:
                group = m.groupdict()
                max_power_output_watts = group['max_power_output_watts']
                idprom_type_id_dict.update({'max_power_output_watts' : int(max_power_output_watts)})
                continue

        return result_dict
        
class ShowIdpromInterfaceSchema(MetaParser):
    """
    Schema for show idprom interface {interface}
    """
    schema = {
        'idprom_for_transceiver': {
            'description': str, 
            'transceiver_type': str, 
            'product_identifier': str, 
            'vendor_revision': str, 
            'serial_number': str, 
            'vendor_name': str,
            'vendor_oui': str,
            'clei_code': str,
            'cisco_part_number': str,
            'device_state': str, 
            'date_code': str,
            'connector_type': str, 
            'encoding': str,
            Optional('nominal_bitrate_per_channel'): str,
        },
    }
              
class ShowIdpromInterface(ShowIdpromInterfaceSchema):
    """ Parser for show idprom interface {interface}"""

    cli_command = 'show idprom interface {interface}'
    
    def cli(self, interface, output=None): 
        if output is None:
           # excute command to get output
           output = self.device.execute(self.cli_command.format(interface=interface))
            
        # initial variables
        ret_dict = {}
        
        # IDPROM for transceiver
        p1 = re.compile('^(?P<idprom_for_transceiver>IDPROM for transceiver)')
        
        # Description         = QSFP28 optics (type 134)
        p2 = re.compile('^Description\s+=\s+(?P<description>.*)$')

        # Transceiver Ty     = QSFP 100GE CU1M (464)
        p3 = re.compile('^Transceiver Type:\s+=\s+(?P<transceiver_type>.*)$')

        # Product Identifier (PID)   = QSFP-100G-CU1M
        p4 = re.compile('^Product Identifier\s+\(PID\)\s+=\s+(?P<product_identifier>.*)$')
 
        # Vendor Revision            = A
        # Vendor Revision            = 1.0
        p5 = re.compile('^Vendor Revision\s+=\s+(?P<vendor_revision>[\w.]+)$')

        # Serial Number (SN)         = APF22340870-A
        p6 = re.compile('^Serial Number\s+\(SN\)\s+=\s+(?P<serial_number>[\w\S]+)$')
        
        # Vendor Name                = CISCO-AMPHENOL
        p7 = re.compile('^Vendor Name\s+=\s+(?P<vendor_name>[\w\S]+)$')

        # Vendor OUI (IEEE company ID)     = 78.A7.14 (7907092)
        p8 = re.compile('^Vendor OUI\s+\(IEEE company ID\)\s+=\s+(?P<vendor_oui>.*)$')
        
        # CLEI code      = CMPQACECAA
        p9 = re.compile('^CLEI code\s+=\s+(?P<clei_code>[\w]+)$')
    
        # Cisco part number      = 37-1666-01
        p10 = re.compile('^Cisco part number\s+=\s+(?P<cisco_part_number>[\d\S]+)$')

        # Device State      = Enabled.
        p11 = re.compile('^Device State\s+=\s+(?P<device_state>[\w\S]+)$')
        
        # Date code (yy/mm/dd)    = 18/08/25
        p12 = re.compile('^Date code\s+\S+\s+=\s+(?P<date_code>[\d\S]+)$')

        # Connector type      = No separable connector
        # Connector type      = LC.
        p13 = re.compile('^Connector type\s+=\s+(?P<connector_type>[\w\s.]+)$')

        # Encoding           = 64B66B
        # Encoding           = 8B10B (1)
        p14= re.compile('^Encoding\s+=\s+(?P<encoding>.*)$')
        
        # Nominal bitrate per channel    = 25GE (25500 Mbits/s)
        p15 = re.compile('^Nominal bitrate per channel\s+=\s+(?P<nominal_bitrate_per_channel>.*)$')

        for line in output.splitlines():
            line=line.strip()
            
            # IDPROM for transceiver
            m=p1.match(line)
            if m:
                group=m.groupdict()
                root_dict = ret_dict.setdefault('idprom_for_transceiver',{})
                
            # Description        = QSFP28 optics (type 134)
            m=p2.match(line)
            if m:
                group=m.groupdict()
                root_dict['description'] = group['description']
                continue
                
            # Transceiver Ty     = QSFP 100GE CU1M (464)                
            m=p3.match(line)
            if m:
                group=m.groupdict()
                root_dict['transceiver_type'] = group['transceiver_type']
                continue

            # Product Identifier (PID)   = QSFP-100G-CU1M
            m=p4.match(line)
            if m:
                group=m.groupdict()
                root_dict['product_identifier'] = group['product_identifier']
                continue

            # Vendor Revision            = A
            m=p5.match(line)
            if m:
                group=m.groupdict()
                root_dict['vendor_revision'] = group['vendor_revision']
                continue
                
            # Serial Number (SN)         = APF22340870-A
            m=p6.match(line)
            if m:
                group=m.groupdict()
                root_dict['serial_number'] = group['serial_number']
                continue

            # Vendor Name                = CISCO-AMPHENOL
            m=p7.match(line)
            if m:
                group=m.groupdict()
                root_dict['vendor_name'] = group['vendor_name']
                continue
                
            # Vendor OUI (IEEE company ID)     = 78.A7.14 (7907092)
            m=p8.match(line)
            if m:
                group=m.groupdict()
                root_dict['vendor_oui'] = group['vendor_oui']
                continue

            # CLEI code        = CMPQACECAA
            m=p9.match(line)
            if m:
                group=m.groupdict()
                root_dict['clei_code'] = group['clei_code']
                continue
                
            # Cisco part number      = 37-1666-01
            m=p10.match(line)
            if m:
                group=m.groupdict()
                root_dict['cisco_part_number'] = group['cisco_part_number']
                continue  
                
            # Device State      = Enabled.
            m=p11.match(line)
            if m:
                group=m.groupdict()
                root_dict['device_state'] = group['device_state']
                continue 

            # Date code (yy/mm/dd)    = 18/08/25
            m=p12.match(line)
            if m:
                group=m.groupdict()
                root_dict['date_code'] = group['date_code']
                continue                
            
            # Connector type      = No separable connector
            m=p13.match(line)
            if m:
                group=m.groupdict()
                root_dict['connector_type'] = group['connector_type']
                continue    

            # Encoding           = 64B66B
            m=p14.match(line)
            if m:
                group=m.groupdict()
                root_dict['encoding'] = group['encoding']
                continue

            # Nominal bitrate per channel    = 25GE (25500 Mbits/s)
            m=p15.match(line)
            if m:
                group=m.groupdict()
                root_dict['nominal_bitrate_per_channel'] = group['nominal_bitrate_per_channel']
                continue				
                
        return ret_dict     


# ==========================
# Schema for:
#  * 'show idprom tan switch {number}'
#  * 'show idprom tan switch all'
# ==========================
class ShowIdpromTanSchema(MetaParser):
    """Schema for:
        show idprom tan switch {switch_num}
        show idprom tan switch all"""

    schema = {
        'switch': {
            Any(): {
                'switch_num': int,
                'part_num': str,
                'revision_num': int,
            },
        }
    }
class ShowIdpromTan(ShowIdpromTanSchema):
    """Parser for:
        show idprom tan switch {switch_num}
        show idprom tan switch all
         """

    cli_command = ['show idprom tan switch {switch_num}',
                    'show idprom tan switch all']

    def cli(self, switch_num=None, output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[0].format(switch_num=switch_num)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        # Switch 01 ---------
        p1 = re.compile(r"^Switch\s+(?P<switch_num>\d+)$")
        # Top Assy. Part Number           : 68-101195-01
        p2 = re.compile(r"^Top\s+Assy.\s+Part\s+Number\s+:\s+(?P<part_num>\d+-\d+-\d+)$")
        # Top Assy. Revision Number       : 31
        p3 = re.compile(r"^Top\s+Assy.\s+Revision\s+Number\s+:\s+(?P<revision_num>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #Switch 01 ---------
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                switch_var = dict_val['switch_num']
                switch_group = ret_dict.setdefault('switch', {})
                sw_dict = ret_dict['switch'].setdefault(switch_var, {})
                sw_dict['switch_num'] = int(switch_var)
                continue

            # Top Assy. Part Number           : 68-101195-01
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                part_num_var = dict_val['part_num']
                sw_dict['part_num'] = part_num_var
                continue

            # Top Assy. Revision Number       : 31
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                revision_part_num = dict_val['revision_num']
                sw_dict['revision_num'] = int(revision_part_num)
                continue


        return ret_dict 