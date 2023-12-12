''' test_vdsl_option.py

IOSXE parsers for the following test commands:

    * 'test vdsl option {option1} {option2}'
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use
# import parser utils
from genie.libs.parser.utils.common import Common

# ==================================================================
# Parser Schema for 'test vdsl option {option1} {option2}'
# ==================================================================


class TestVdslOptionSchema(MetaParser):
    """Schema for test vdsl option {option1} {option2}' """

    schema = {
        "debug_flags": str,
        "Seq_0": str,
        "name": str,
        "metanoiaPort": str,
        "sfp_type": str,
        "metanoiaPort_state": str,
        "metanoiaPort_cnt": str,
        "mac": str,
        "choice": str,
        "hw_interface": Or(str,int),
        "sw_interface": Or(str,int),
        "firmware_file": str,
        "upgrade_file": str,
        "Upgrade_file_info": str,
        "sfp_version": str,
        "notification_seq": str,
        "vdsl_state": str,
        "ebm_tx": str,
        "ebm_rx": str,
        "ebm_wait_timeout": str,
        "ebm_rx_loss": str,
        "vid_co": str,
        "vid_cpe": str,
        Optional("serial_no_co"): str,
        "serial_no_cpe": str,
        Optional("version_co"): str,
        "version_co_cpe": str,
        Optional("capability_co"): str,
        "capability_co_cpe": str,
        "line_attn_up": str,
        "line_attn_down": str,              
    }

# ===========================================================
# Parser for 'test vdsl option {option1} {option2}'
# ===========================================================

class TestVdslOption(TestVdslOptionSchema):
    """ parser for test vdsl option {option1} {option2} """

    cli_command = 'test vdsl option {option1} {option2}'
            
    def cli(self, option1=6, option2=0x0, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(option1=option1,option2=option2))
        else:
            out = output
          
        ctrl_dict = {}

        #Debug flags: 0x8000
        p1 = re.compile(r'^(Debug\s+flags):\s+(?P<v1>\w+)$')
        
        #Seq 0: slot=0 slot_port=0 bay=0 port=0 Name:MetaMgr0_0_0
        p2 = re.compile(r'^(Seq\s+\d+):\s+(?P<v1>.+)\s+Name:(?P<v2>\w+)')

        #MetanoiaPort=0 SFP type: 1 State: 2 cnt=290
        p3 = re.compile(r'^(MetanoiaPort)=(?P<v1>\d+)\s+(SFP\s+type):\s+(?P<v2>\d+)\s+(State):\s+(?P<v3>\d+)\s+(cnt)=(?P<v4>\d+)')
        
        #MAC:00:00:00:00:00:00 Choice:0
        p4 = re.compile(r'^(MAC):(?P<v1>([0-9a-fA-F].?){12})\s+(Choice):(?P<v2>\d+)')
        
        #hw interface:GigabitEthernet0/0/0 sw interface:GigabitEthernet0/0/0
        p5 = re.compile(r'^(hw\s+interface):(?P<v1>.+)\s+sw\s+(interface):(?P<v2>.+)')
        
        #Firmware file: /etc/SFP_V5311-T-R_CSP.b, size=491520, version=1_62_8463
        p6 = re.compile(r'^(Firmware\s+file):\s+(?P<v1>.*)$')
        
        #Upgrade file: [], size=0, version= offset=0x0
        p7 = re.compile(r'^(Upgrade\s+file):\s+(?P<v1>.*)$')
        
        #Upgrade file info: 
        p8 = re.compile(r'^(Upgrade\s+file info):(?P<v1>.*)$')
        
        #SFP version: 1_62_8463
        p9 = re.compile(r'^(SFP\s+version):\s+(?P<v1>.+)$')
        
        #Notification Seq: 0x3 cnt: 0x23 Stat Cycle:255 
        p10 = re.compile(r'^(Notification\s+Seq):\s+(?P<v1>.+)$')     

        #VDSL State: 5
        p11 = re.compile(r'^(VDSL\s+State):\s+(?P<v1>\d+)$') 
        
        #EBM Tx: 709799 Rx: 709799
        p12 = re.compile(r'^(EBM\s+Tx):\s+(?P<v1>\d+)\s+Rx:\s+(?P<v2>\d+)')
        
        #EBM Wait Timeout: 0 Rx Loss: 0
        p13 = re.compile(r'^(EBM\s+Wait\s+Timeout):\s+(?P<v1>\d+)\s+Rx\s+Loss:\s+(?P<v2>\d+)')
        
        #G994 vid CO: BDCM CPE: META
        p14 = re.compile(r'^(.*\s+vid\s+CO):\s+(?P<v1>\w+)\s+CPE:\s+(?P<v2>\w+)')
        
        #Serial No CO: eq_nr multiline_cpe software_rev CPE: MET211611AC V5311TR 1_62_8463
        p15 = re.compile(r'^(Serial\s+No\s+CO):(?P<v1>.+)\s+CPE:\s+(?P<v2>.+)')
        
        #Version CO: v11.02.31       CPE: 1_62_8463 MT5311
        p16 = re.compile(r'^(Version\s+CO):(?P<v1>.+)\s+CPE:\s+(?P<v2>.+)')
        
        #Capability CO: 000000000000000200 CPE: 040004000C01000300
        p17 = re.compile(r'^(Capability\s+CO):(?P<v1>.+)\s+CPE:\s+(?P<v2>.+)')
        
        #Line Attn: UP: 65535 DOWN: 22 
        p18 = re.compile(r'^(Line\s+Attn:\s+UP):\s+(?P<v1>\d+)\s+DOWN:\s+(?P<v2>\d+)')  
        
        for line in out.splitlines():
            line = line.strip()

            #Debug flags: 0x8000
            m = p1.match(line)
            if m:
                group = m.groupdict()
                param = 'debug_flags'
                ctrl_dict[param] = group['v1']
                continue
            
            #Seq 0: slot=0 slot_port=0 bay=0 port=0 Name:MetaMgr0_0_0        
            m = p2.match(line)
            if m:
                group = m.groupdict()
                param = 'Seq_0'
                ctrl_dict[param] = group['v1']                
                param2 = 'name'
                ctrl_dict[param2] = group['v2']
                continue

            #MetanoiaPort=0 SFP type: 1 State: 2 cnt=290
            m = p3.match(line)
            if m:      
                group = m.groupdict()
                param = 'metanoiaPort'
                ctrl_dict[param] = group['v1']
                param2 = 'sfp_type'
                ctrl_dict[param2] = group['v2']
                param3 = 'metanoiaPort_state'
                ctrl_dict[param3] = group['v3']
                param4 = 'metanoiaPort_cnt'
                ctrl_dict[param4] = group['v4']
                continue
            
            #MAC:00:00:00:00:00:00 Choice:0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                param = 'mac'
                ctrl_dict[param] = group['v1']
                param2 = 'choice'
                ctrl_dict[param2] = group['v2']
                continue
            
            #hw interface:GigabitEthernet0/0/0 sw interface:GigabitEthernet0/0/0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                param = 'hw_interface'
                ctrl_dict[param] = group['v1']
                param2 = 'sw_interface'
                ctrl_dict[param2] = group['v2']
                continue
                
            #Firmware file: /etc/SFP_V5311-T-R_CSP.b, size=491520, version=1_62_8463
            m = p6.match(line)
            if m:
                group = m.groupdict()
                param = 'firmware_file'
                ctrl_dict[param] = group['v1']
                continue                

            #Upgrade file: [], size=0, version= offset=0x0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                param = 'upgrade_file'
                ctrl_dict[param] = group['v1']

            #Upgrade file info: 
            m = p8.match(line)
            if m:
                group = m.groupdict()
                param = 'Upgrade_file_info'
                ctrl_dict[param] = group['v1']
                continue                

            #SFP version: 1_62_8463
            m = p9.match(line)
            if m:
                group = m.groupdict()
                param = 'sfp_version'
                ctrl_dict[param] = group['v1']
                continue

            #Notification Seq: 0x3 cnt: 0x23 Stat Cycle:255
            m = p10.match(line)
            if m:
                group = m.groupdict()
                param = 'notification_seq'
                ctrl_dict[param] = group['v1']
                continue                

            #VDSL State: 5
            m = p11.match(line)
            if m:
                group = m.groupdict()
                param = 'vdsl_state'
                ctrl_dict[param] = group['v1']
                continue

            #EBM Tx: 709799 Rx: 709799
            m = p12.match(line)
            if m:
                group = m.groupdict()
                param = 'ebm_tx'
                ctrl_dict[param] = group['v1']
                param2 = 'ebm_rx'
                ctrl_dict[param2] = group['v2']
                continue  

            #EBM Wait Timeout: 0 Rx Loss: 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                param = 'ebm_wait_timeout'
                ctrl_dict[param] = group['v1']
                param2 = 'ebm_rx_loss'
                ctrl_dict[param2] = group['v2']
                continue  
            
            #G994 vid CO: BDCM CPE: META           
            m = p14.match(line)
            if m:
                group = m.groupdict()
                param = 'vid_co'
                ctrl_dict[param] = group['v1']
                param2 = 'vid_cpe'
                ctrl_dict[param2] = group['v2']
                continue
            
            #Serial No CO: eq_nr multiline_cpe software_rev CPE: MET211611AC V5311TR 1_62_8463
            m = p15.match(line)
            if m:
                group = m.groupdict()
                param = 'serial_no_co'
                ctrl_dict[param] = group['v1']
                param2 = 'serial_no_cpe'
                ctrl_dict[param2] = group['v2']
                continue

            #Version CO: v11.02.31 CPE: 1_62_8463 MT5311
            m = p16.match(line)
            if m:
                group = m.groupdict()
                param = 'version_co'
                ctrl_dict[param] = group['v1']
                param2 = 'version_co_cpe'
                ctrl_dict[param2] = group['v2']
                continue

            #Capability CO: 000000000000000200 CPE: 040004000C01000300 
            m = p17.match(line)
            if m:
                group = m.groupdict()
                param = 'capability_co'
                ctrl_dict[param] = group['v1']
                param2 = 'capability_co_cpe'
                ctrl_dict[param2] = group['v2']
                continue            
            
            #Line Attn: UP: 65535 DOWN: 22
            m = p18.match(line)
            if m:
                group = m.groupdict()
                param = 'line_attn_up'
                ctrl_dict[param] = group['v1']
                param2 = 'line_attn_down'
                ctrl_dict[param2] = group['v2']
                continue

        return ctrl_dict                
                  

                
                
                 
         	                      
