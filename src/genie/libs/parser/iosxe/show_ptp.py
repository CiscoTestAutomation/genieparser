"""
    show_ptp.py
    IOSXE parsers for the following show commands:
    
    * show ptp brief
    * show ptp brief | exclude FAULTY
    * show ptp clock
    * show ptp parent
    * show ptp port {interface}
    
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =====================================
#  Schema for 
#  * 'show ptp brief'  
#  * 'show ptp brief | exclude FAULTY'
# ======================================
class ShowPtpBriefSchema(MetaParser):
    """Schema for 'show ptp brief'
    """
    schema = {
        'interface': {
            Any(): {
                'domain': int,
                'state': str,
            }
        }
    }
    
# ===================================
#  Parser for 
#  * 'show ptp brief'
#  * 'show ptp brief | exclude FAULTY'
# =====================================
class ShowPtpBrief(ShowPtpBriefSchema):
    """
    Parser for :
        * show ptp brief
        * show ptp brief | exclude {ptp_state}
    """

    cli_command = ['show ptp brief', 'show ptp brief | exclude {ptp_state}']
    
    def cli(self, ptp_state = "", output=None):
        if output is None:
            if ptp_state:
                cmd = self.cli_command[1].format(ptp_state=ptp_state)    
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)    

        #TenGigabitEthernet1/0/6    0    MASTER
        p = re.compile(r'^(?P<interface>[a-zA-Z\d\/\.]+)\s+(?P<domain>\d+)\s+(?P<state>\w+)$')
        
        # initial return dictionary
        ret_dict ={}
        
        for line in output.splitlines():
            line = line.strip()
            
            #TenGigabitEthernet1/0/6    0  MASTER
            m = p.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                sub_dict = ret_dict.setdefault('interface', {}).setdefault(interface, {})
                
                domain = group['domain']
                sub_dict['domain'] = int(domain)
                
                state = group['state']
                sub_dict['state'] = state
                
                continue
        return ret_dict    

# ==============================
#  Schema for 'show ptp clock'
# ==============================
class ShowPtpClockSchema(MetaParser):
    """Schema for 'show ptp clock'
    """
    schema = {
        'ptp_clock_info': {
            'device_type': str,
            'device_profile': str,
            'clock_identity': str,
            'clock_domain': int,
            'network_transport_protocol': str,
            'message_general_ip_dscp': int,
            'message_event_ip_dscp': int,
            'number_of_ptp_ports': int,
            Optional('priority1'): int,
            Optional('priority2'): int,
            Optional('clock_quality'): {
                Optional('class'): int,
                Optional('accuracy'): str,
                Optional('offset'): int
            },
            Optional('offset_from_master'): int,
            Optional('mean_path_delay_ns'): int,
            Optional('steps_removed'): int

        },
    }

# =============================
#  Parser for 'show ptp clock'
# =============================
class ShowPtpClock(ShowPtpClockSchema):
    """
    Parser for :
        * show ptp clock
    """

    cli_command = 'show ptp clock'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        #PTP Device Type: Boundary clock
        p1 = re.compile(r'^PTP\sDevice\sType\:\s(?P<device_type>.*)$')

        #PTP Device Profile: Default Profile
        p2 = re.compile(r'^PTP\sDevice\sProfile\:\s(?P<device_profile>.*)$')

        #Clock Identity: 0x34:ED:1B:FF:FE:7D:F2:80
        p3 = re.compile(r'^Clock\sIdentity\:\s(?P<clock_identity>(0x(?:[\da-fA-F]:?).*))$')

        #Clock Domain: 0
        p4 = re.compile(r'^Clock\sDomain\:\s(?P<clock_domain>\d+)$')

        #Network Transport Protocol: 802.3
        p5 = re.compile(r'^Network\sTransport\sProtocol\:\s(?P<network_transport_protocol>\S+)$')

        #Message general ip dscp  : 47
        p6 = re.compile(r'^Message\sgeneral\sip\sdscp\s+\:\s(?P<message_general_ip_dscp>\d+)$')

        #Message event  ip dscp   : 59
        p7 = re.compile(r'^Message\sevent\s+ip\sdscp\s+\:\s(?P<message_event_ip_dscp>\d+)$')

        #Number of PTP ports: 75
        p8 = re.compile(r'^Number\sof\sPTP\sports\:\s(?P<number_of_ptp_ports>\d+)$')

        #Priority1: 128
        p9 = re.compile(r'^Priority1\:\s(?P<priority1>\d+)$')

        #Priority2: 128
        p10 = re.compile(r'^Priority2\:\s(?P<priority2>\d+)$')

        #Class: 248
        p11 = re.compile(r'^Class\:\s(?P<class>\d+)$')

        #Accuracy: Unknown
        p12 = re.compile(r'^Accuracy\:\s(?P<accuracy>\S+)$')

        #Offset (log variance): 17258
        p13 = re.compile(r'^Offset\s\(log\svariance\)\:\s(?P<offset>\d+)$')

        #Offset From Master(ns): -19
        p14 = re.compile(r'^Offset\sFrom\sMaster\(ns\)\:\s(?P<offset_from_master>\S+)$')

        #Mean Path Delay(ns): 83
        p15 = re.compile(r'^Mean\sPath\sDelay\(ns\)\:\s(?P<mean_path_delay_ns>\d+)$')

        #Steps Removed: 2
        p16 = re.compile(r'^Steps\sRemoved\:\s(?P<steps_removed>\d+)$')

        # initial return dictionary
        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()

            #PTP Device Type: Boundary clock
            m = p1.match(line)
            if m:
                ptp_clock_info = ret_dict.setdefault('ptp_clock_info',{})
                ptp_clock_info['device_type'] = m.groupdict()['device_type']
                continue

            #PTP Device Profile: Default Profile
            m = p2.match(line)
            if m:
                ptp_clock_info['device_profile'] = m.groupdict()['device_profile']
                continue
            
            #Clock Identity: 0x34:ED:1B:FF:FE:7D:F2:80
            m = p3.match(line)
            if m:
                clock_identity = m.groupdict()['clock_identity']
                ptp_clock_info['clock_identity'] = clock_identity
                continue
            
            #Clock Domain: 0
            m = p4.match(line)
            if m:
                clock_domain = m.groupdict()['clock_domain']
                ptp_clock_info['clock_domain'] = int(clock_domain)
                continue

            #Network Transport Protocol: 802.3
            m = p5.match(line)
            if m:
                network_transport_protocol = m.groupdict()['network_transport_protocol']
                ptp_clock_info['network_transport_protocol'] = network_transport_protocol
                continue

            #Message general ip dscp  : 47
            m = p6.match(line)
            if m:
                message_general_ip_dscp = m.groupdict()['message_general_ip_dscp']
                ptp_clock_info['message_general_ip_dscp'] = int(message_general_ip_dscp)
                continue

            #Message event  ip dscp   : 59
            m = p7.match(line)
            if m:
                message_event_ip_dscp = m.groupdict()['message_event_ip_dscp']
                ptp_clock_info['message_event_ip_dscp'] = int(message_event_ip_dscp)
                continue

            #Number of PTP ports: 75
            m = p8.match(line)
            if m:
                number_of_ptp_ports = m.groupdict()['number_of_ptp_ports']
                ptp_clock_info['number_of_ptp_ports'] = int(number_of_ptp_ports)
                continue

            #Priority1: 128
            m = p9.match(line)
            if m:
                priority1 = m.groupdict()['priority1']
                ptp_clock_info['priority1'] = int(priority1)
                continue

            #Priority2: 128
            m = p10.match(line)
            if m:
                priority2 = m.groupdict()['priority2']
                ptp_clock_info['priority2'] = int(priority2)
                continue

            #Class: 248
            m = p11.match(line)
            if m:
                clock_quality = ptp_clock_info.setdefault('clock_quality', {})
                clock_quality['class'] = int(m.groupdict()['class'])
                continue

            #Accuracy: Unknown
            m = p12.match(line)
            if m:
                accuracy = m.groupdict()['accuracy']
                clock_quality['accuracy'] = accuracy
                continue

            #Offset (log variance): 17258
            m = p13.match(line)
            if m:
                offset = m.groupdict()['offset']
                clock_quality['offset'] = int(offset)
                continue

            #Offset From Master(ns): 0
            m = p14.match(line)
            if m:
                offset_from_master = m.groupdict()['offset_from_master']
                ptp_clock_info['offset_from_master'] = int(offset_from_master)
                continue

            #Mean Path Delay(ns): 52
            m = p15.match(line)
            if m:
                mean_path_delay_ns = m.groupdict()['mean_path_delay_ns']
                ptp_clock_info['mean_path_delay_ns'] = int(mean_path_delay_ns)
                continue

            #Steps Removed: 0
            m = p16.match(line)
            if m:
                steps_removed = m.groupdict()['steps_removed']
                ptp_clock_info['steps_removed'] = int(steps_removed)
                continue
        return ret_dict

# =============================
#  Schema for 'show ptp parent'
# =============================
class ShowPtpParentSchema(MetaParser):
    """Schema for 'show ptp parent'
    """
    schema = {
        'ptp_parent_property': {
            'parent_clock': {
                'identity': str,
                'port_number': int,
                'observed_parent_offset': int,
                'phase_change_rate': str,
            },
            'grandmaster_clock': {
                'identity': str,
                'gd_class': int,
                'accuracy': str,
                'offset': str,
                'priority1': int,
                'priority2': int
            }
        },            
    }        


# ==============================
#  Parser for 'show ptp parent'
# ==============================
class ShowPtpParent(ShowPtpParentSchema):
    """
    Parser for :
        * show ptp parent
    """

    cli_command = 'show ptp parent'

    def cli(self, output=None):
    	
        if output is None:
            output = self.device.execute(self.cli_command)
        	
        #Parent Clock Identity: 0xE4:1F:7B:FF:FE:52:5D:0
        p1 = re.compile(r'^Parent\sClock\sIdentity\:\s(?P<identity>(0x(?:[\da-fA-F]:?).*))$')
        
        #Parent Port Number: 9
        p2 = re.compile(r'^Parent\sPort\sNumber\:\s(?P<port_number>\d+)$')
        
        #Observed Parent Offset (log variance): 17258
        p3 = re.compile(r'^Observed\sParent\sOffset\s\(log\svariance\)\:\s(?P<observed_parent_offset>\d+)$')
        
        #Observed Parent Clock Phase Change Rate: N/A
        p4 = re.compile(r'^Observed\sParent\sClock\sPhase\sChange\sRate\:\s(?P<phase_change_rate>\S+)$')
        
        #Grandmaster Clock Identity: 0x0:1:2:FF:FE:2:AA:BB
        p5 = re.compile(r'^Grandmaster\sClock\sIdentity\:\s(?P<identity>(0x(?:[\da-fA-F]:?).*))$')
        
        #Class: 248
        p6 = re.compile(r'^Class\:\s(?P<gd_class>\d+)$')
        
        #Accuracy: Unknown
        p7 = re.compile(r'^Accuracy\:\s(?P<accuracy>\S+)$')
        
        #Offset (log variance): N/A
        p8 = re.compile(r'^Offset\s\(log\svariance\)\:\s(?P<offset>\S+)$')
        
        #Priority1: 128
        p9 = re.compile(r'^Priority1\:\s(?P<priority1>\d+)$')
        
        #Priority2: 128
        p10 = re.compile(r'^Priority2\:\s(?P<priority2>\d+)$')
        
        # initial return dictionary
        ret_dict ={}
        
        for line in output.splitlines():
            line = line.strip()
            
            #Parent Clock Identity: 0xE4:1F:7B:FF:FE:52:5D:0
            m = p1.match(line)
            if m:
                ptp_parent_property = ret_dict.setdefault('ptp_parent_property',{})
                parent_clock = ptp_parent_property.setdefault('parent_clock',{})
                identity = m.groupdict()['identity']
                parent_clock['identity'] = identity
                continue
            
            #Parent Port Number: 9
            m = p2.match(line)
            if m:
                port_number = m.groupdict()['port_number']
                parent_clock['port_number'] = int(port_number)
                continue
            
            #Observed Parent Offset (log variance): 17258
            m = p3.match(line)
            if m:
                observed_parent_offset = m.groupdict()['observed_parent_offset']
                parent_clock['observed_parent_offset'] = int(observed_parent_offset)
                continue
            
            #Observed Parent Clock Phase Change Rate: N/A
            m = p4.match(line)
            if m:
                phase_change_rate =  m.groupdict()['phase_change_rate']
                parent_clock['phase_change_rate'] = phase_change_rate
                continue
            
            #Grandmaster Clock Identity: 0x0:11:1:FF:FE:0:0:1
            m = p5.match(line)
            if m:
                grandmaster_clock = ptp_parent_property.setdefault('grandmaster_clock', {})
                identity = m.groupdict()['identity']
                grandmaster_clock['identity'] = identity
                continue
            
            #Class: 6
            m = p6.match(line)
            if m:
                gd_class = m.groupdict()['gd_class']
                grandmaster_clock['gd_class'] = int(gd_class)
                continue
            
            #Accuracy: Unknown
            m = p7.match(line)
            if m:
                accuracy = m.groupdict()['accuracy']
                grandmaster_clock['accuracy'] = accuracy
                continue
            
            #Offset (log variance): N/A
            m = p8.match(line)
            if m:
                offset = m.groupdict()['offset']
                grandmaster_clock['offset'] = offset
                continue
            
            #Priority1: 128
            m = p9.match(line)
            if m:
                priority1 = m.groupdict()['priority1']
                grandmaster_clock['priority1'] = int(priority1)
                continue
                
            #Priority2: 128
            m = p10.match(line)
            if m:
                priority2 = m.groupdict()['priority2']
                grandmaster_clock['priority2'] = int(priority2)
                continue
        return ret_dict    


# =======================================
#  Schema for 'show ptp port {interface}'
# =======================================
class ShowPtpPortInterfaceSchema(MetaParser):
    """Schema for 'show ptp port {interface}'
    """
    schema = {                                                                  
        'ptp_port_dataset': {                                                   
            'ptp_info': {                                                       
                'interface': str,                                               
                'version': int,                                                 
                'slot_number': int,                                             
            },                                                                  
            'port_info': {                                                      
                'identity': str,                                                
                'number': int,                                                  
                Optional('state'): str,                                         
            },                                                                  
            Optional('delay_request_interval'): int,                            
            Optional('announce_receipt_time_out'): int,                         
            Optional('announce_interval'): int,                                 
            Optional('sync_interval'): int,                                     
            Optional('delay_mechanism'): str,                                   
            Optional('peer_delay_request_interval'): int,                       
            Optional('sync_fault_limit'): int,                                  
        },
        Optional('ptp_role_primary'): str		
    }

# =======================================
#  Parser for 'show ptp port {interface}'
# =======================================
class ShowPtpPortInterface(ShowPtpPortInterfaceSchema):
    """
    Parser for :
        * show ptp port {interface}
    """
    cli_command = 'show ptp port {interface}'
    def cli(self, interface, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))
 	    
        #PTP PORT DATASET: TenGigabitEthernet1/0/33
        p1 = re.compile(r'^PTP\sPORT\sDATASET\:\s(?P<interface>\S+)$')  
        
        #Port identity: clock identity: 0x34:ED:1B:FF:FE:7D:F2:80
        p2 = re.compile(r'^Port\sidentity\:\sclock\sidentity:\s(?P<identity>(0x(?:[\da-fA-F]:?).*))$')
        
        #Port identity: port number: 33
        p3 = re.compile(r'^Port\sidentity\:\sport\snumber:\s(?P<number>\d+)$')
        
        #PTP version: 2
        p4 = re.compile(r'^PTP\sversion\:\s(?P<version>\d+)$')
        
        #PTP port number: 33
        p5 = re.compile(r'^PTP\sport\snumber\:\s(?P<number>\d+)$')
        
        #PTP slot number: 1
        p6 = re.compile(r'^PTP\sslot\snumber\:\s(?P<slot_number>\d+)$')
        
        #Port state: SLAVE
        p7 = re.compile(r'^Port\sstate\:\s(?P<state>\S+)$')
        
        #Delay request interval(log mean): 0
        p8 = re.compile(r'^Delay\srequest\sinterval\(log\smean\)\:\s(?P<delay_request_interval>\d+)$')
        
        #Announce receipt time out: 3
        p9 = re.compile(r'^Announce\sreceipt\stime\sout\:\s(?P<announce_receipt_time_out>\d+)$')
        
        #Announce interval(log mean): 0
        p10 = re.compile(r'^Announce\sinterval\(log\smean\)\:\s(?P<announce_interval>\d+)$')
        
        #Sync interval(log mean): 0
        p11 = re.compile(r'^Sync\sinterval\(log\smean\)\:\s(?P<sync_interval>\d+)$')
        
        #Delay Mechanism: End to End
        p12 = re.compile(r'^Delay\sMechanism\:\s(?P<delay_mechanism>.*)$')
        
        #Peer delay request interval(log mean): 0
        p13 = re.compile(r'^Peer\sdelay\srequest\sinterval\(log\smean\)\:\s(?P<peer_delay_request_interval>\d+)$')
        
        #Sync fault limit: 500000000
        p14 = re.compile(r'^Sync\sfault\slimit\:\s(?P<sync_fault_limit>\d+)$')
        
        #ptp role primary : Disabled
        p15 = re.compile(r'^ptp\srole\sprimary\s\:\s(?P<ptp_role_primary>\S+)$')
        
        # initial return dictionary
        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()
            
            # PTP PORT DATASET: TenGigabitEthernet1/0/1
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                ptp_port_dataset = ret_dict.setdefault('ptp_port_dataset',{})
                ptp_info = ptp_port_dataset.setdefault('ptp_info',{})
                ptp_info['interface'] = interface
                port_info = ptp_port_dataset.setdefault('port_info',{})
                continue
            
            #Port identity: clock identity: 0x34:ED:1B:FF:FE:7D:F2:80
            m = p2.match(line)
            if m:
                identity = m.groupdict()['identity']
                port_info['identity'] = identity
                continue
            
            #Port identity: port number: 1
            m = p3.match(line)
            if m:
                number = m.groupdict()['number']
                port_info['number'] = int(number)
                continue
            
            #PTP version: 2
            m = p4.match(line)
            if m:
                version = m.groupdict()['version']
                ptp_info['version'] = int(version)
                continue
            
            #PTP port number: 1
            m = p5.match(line)
            if m:
                number = m.groupdict()['number']
                port_info['number'] = int(number)
                continue
            
            #PTP slot number: 1
            m = p6.match(line)
            if m:
                slot_number = m.groupdict()['slot_number']
                ptp_info['slot_number'] = int(slot_number)
                continue
            
            #Port state: FAULTY
            m = p7.match(line)
            if m:
                state = m.groupdict()['state']
                port_info['state'] = state 
                continue
            
            #Delay request interval(log mean): 0
            m = p8.match(line)
            if m:
                delay_request_interval = m.groupdict()['delay_request_interval']
                ptp_port_dataset['delay_request_interval'] = int(delay_request_interval)
                continue
            
            #Announce receipt time out: 3
            m = p9.match(line)
            if m:
                announce_receipt_time_out = m.groupdict()['announce_receipt_time_out']
                ptp_port_dataset['announce_receipt_time_out'] = int(announce_receipt_time_out)
                continue
            
            #Announce interval(log mean): 0
            m = p10.match(line)
            if m:
                announce_interval = m.groupdict()['announce_interval']
                ptp_port_dataset['announce_interval'] = int(announce_interval)
                continue
            
            #Sync interval(log mean): 0
            m = p11.match(line)
            if m:
                sync_interval = m.groupdict()['sync_interval']
                ptp_port_dataset['sync_interval'] = int(sync_interval)
                continue
            
            #Delay Mechanism: Peer to Peer
            m = p12.match(line)
            if m:
                delay_mechanism = m.groupdict()['delay_mechanism']
                ptp_port_dataset['delay_mechanism'] = delay_mechanism
                continue
            
            #Peer delay request interval(log mean): 0
            m = p13.match(line)
            if m:
                peer_delay_request_interval = m.groupdict()['peer_delay_request_interval']
                ptp_port_dataset['peer_delay_request_interval'] = int(peer_delay_request_interval)
                continue
            
            #Sync fault limit: 500000000
            m = p14.match(line)
            if m:
                sync_fault_limit = m.groupdict()['sync_fault_limit']
                ptp_port_dataset['sync_fault_limit'] = int(sync_fault_limit)
                continue
            
            #ptp role primary : Disabled
            m = p15.match(line)
            if m:
                ptp_role_primary = m.groupdict()['ptp_role_primary']
                ret_dict['ptp_role_primary'] = ptp_role_primary
                continue
        return ret_dict
