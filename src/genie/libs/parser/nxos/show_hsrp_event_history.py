''' show_hsrp_event_history.py

NXOS parsers for the following show commands:
    * show hsrp internal event-history errors
    * show hsrp internal event-history debugs
    * show hsrp internal event-history msgs

'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

# ====================================================
# Schema for 'show hsrp internal event-history errors'
# ====================================================
class ShowHsrpEventHistoryErrorsSchema(MetaParser):
    
    ''' Schema for "show hsrp internal event-history errors" '''
   
    schema = {  
        'event_type':{
            'error':{
                int : {
                    'date' : str,
                    'time' : str,
                    'proc_name' : str,
                    'pid' : int, 
                    'msg' : str
                }            
            }
        }      
    }


# ====================================================
# Parser for 'show hsrp internal event-history errors'
# ====================================================
class ShowHsrpEventHistoryErrors(ShowHsrpEventHistoryErrorsSchema):

    ''' Parser for "show hsrp internal event-history errors"'''

    cli_command = 'show hsrp internal event-history errors'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        event_history_errors_dict={}
        #[2] 2021 Apr 21 12:28:21.913775 [hsrp_engine] E_DEBUG    [24399]:(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv4, VLAN=1001
        p1 = re.compile(r'^\[(?P<log_num>\d+)\]\s+(?P<date>\d{4} [a-zA-Z]+ [0-9]{1,2}) (?P<time>[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{6}) \[(?P<proc_name>.+)\] E_DEBUG\s+\[(?P<pid>\d+)\]:(?P<msg>.+)$')

        for line in output.splitlines():
            line = line.strip()
            #[2] 2021 Apr 21 12:28:21.913775 [hsrp_engine] E_DEBUG    [24399]:(Acast) Get Bundle For IOD Failed: Reason='No bundle found for VLAN', AddrType=IPv4, VLAN=1001  
            m = p1.match(line)
            if m:
                result_dict = event_history_errors_dict.setdefault('event_type',{})
                result_dict['error'] = event_history_errors_dict['event_type'].setdefault('error',{})
                
                groups = m.groupdict()

                log_dict = result_dict['error'].setdefault(int(groups['log_num']), {})
                log_dict.update({'date': groups['date']})
                log_dict.update({'time': groups['time']})
                log_dict.update({'proc_name': groups['proc_name']})
                log_dict.update({'pid': int(groups['pid'])})
                log_dict.update({'msg': groups['msg']})
                continue

        return event_history_errors_dict

# ====================================================
# Schema for 'show hsrp internal event-history debugs'
# ====================================================
class ShowHsrpEventHistoryDebugsSchema(MetaParser):
    
    ''' Schema for "show hsrp internal event-history debugs" '''
   
    schema = {  
        'event_type':{
            'debug':{
                int : {
                    'date' : str,
                    'time' : str,
                    'proc_name' : str,
                    'pid' : int, 
                    'msg' : str
                } 
            }       
        }
    }


# ====================================================
# Parser for 'show hsrp internal event-history debugs'
# ====================================================
class ShowHsrpEventHistoryDebugs(ShowHsrpEventHistoryDebugsSchema):

    ''' Parser for "show hsrp internal event-history debugs"'''

    cli_command = 'show hsrp internal event-history debugs'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        event_history_debugs_dict={}

        #[1] 2021 Apr 30 05:43:16.822827 [hsrp_engine] E_DEBUG    [24399]:[0]:  Time Taken For Show Run: Time=0.015553
        p1 = re.compile(r'^\[(?P<log_num>\d+)\]\s+(?P<date>\d{4} [a-zA-Z]+ [0-9]{1,2}) (?P<time>[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{6}) \[(?P<proc_name>.+)\] E_DEBUG\s+\[(?P<pid>\d+)\]:\[\d+\]:\s*(?P<msg>.+)$')

        for line in output.splitlines():
            line = line.strip()
            #[1] 2021 Apr 30 05:43:16.822827 [hsrp_engine] E_DEBUG    [24399]:[0]:  Time Taken For Show Run: Time=0.015553
            m = p1.match(line)
            if m:
                result_dict = event_history_debugs_dict.setdefault('event_type',{})
                result_dict['debug'] = event_history_debugs_dict['event_type'].setdefault('debug',{})

                groups = m.groupdict()

                log_dict = result_dict['debug'].setdefault(int(groups['log_num']), {})
                log_dict.update({'date': groups['date']})
                log_dict.update({'time': groups['time']})
                log_dict.update({'proc_name': groups['proc_name']})
                log_dict.update({'pid': int(groups['pid'])})
                log_dict.update({'msg': groups['msg']})
                continue

        return event_history_debugs_dict

# ====================================================
# Schema for 'show hsrp internal event-history msgs'
# ====================================================
class ShowHsrpEventHistoryMsgsSchema(MetaParser):
    
    ''' Schema for "show hsrp internal event-history msgs" '''

    schema = {
        'event_type': {
            'message': {
                int : {
                    'date' : str,
                    'time' : str,
                    'proc_name' : str,
                    'msg_type' : str,
                    Optional('msg') : str,
                    Optional('opcode') : str,
                    Optional('opcode_id') : str,
                    Optional('ret_val') : str,
                    Optional('src_sap') : int,
                    Optional('dst_sap') : int,
                    Optional('flags') : str,
                    Optional('ha_seqno') : str,
                    Optional('rr_token') : str,
                    Optional('sync') : str
                } 
            }       
        }  
    }

# ====================================================
# Parser for 'show hsrp internal event-history msgs'
# ====================================================
class ShowHsrpEventHistoryMsgs(ShowHsrpEventHistoryMsgsSchema):

    ''' Parser for "show hsrp internal event-history msgs"'''

    cli_command = 'show hsrp internal event-history msgs'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        event_history_msgs_dict={}

        #[37] 2021 Aug 13 13:26:35.415873 [hsrp_engine] E_DEBUG_DSF    [/Class.cc:331]initRnPrefixTable
        p1_1 = re.compile(r'^\[(?P<log_num>\d+)\]\s+(?P<date>\d{4} [a-zA-Z]+ [0-9]{1,2}) (?P<time>[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{6}) \[(?P<proc_name>[^\]]+)\] (?P<msg_type>E_DEBUG_DSF)\s+(?P<msg>.+)$')

        #[1] 2021 May 10 12:08:54.364555 [hsrp_engine] E_MTS_RX    [REQ] Opc:MTS_OPC_SDWRAP_DEBUG_DUMP(1530), Id:0X0A8359C5, Ret:SUCCESS
        p1_2 = re.compile(r'^\[(?P<log_num>\d+)\]\s+(?P<date>\d{4} [a-zA-Z]+ [0-9]{1,2}) (?P<time>[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{6}) \[(?P<proc_name>[^\]]+)\] (?P<msg_type>E_MTS_RX|E_MTS_TX)\s+\[(REQ|NOT)\] Opc:(?P<opcode>[^,]+), Id:(?P<opcode_id>[^,]+), Ret:(?P<ret_val>.+)$')
        
        #Src:0x00000101/46265, Dst:0x00000101/340, Flags:None
        p2 = re.compile(r'^\s*Src:[^\/]+\/(?P<src_sap>\d+), Dst:[^\/]+\/(?P<dst_sap>\d+), Flags:(?P<flags>.+)$')

        #HA_SEQNO:0X00000000, RRtoken:0x0A8359C5, Sync:UNKNOWN, Payloadsize:308
        p3 = re.compile(r'^\s*HA_SEQNO:(?P<ha_seqno>[^,]+), RRtoken:(?P<rr_token>[^,]+), Sync:(?P<sync>[^,]+), Payloadsize:(\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #[37] 2021 Aug 13 13:26:35.415873 [hsrp_engine] E_DEBUG_DSF    [/Class.cc:331]initRnPrefixTable
            m = p1_1.match(line)
            if m:
                result_dict = event_history_msgs_dict.setdefault('event_type',{})
                result_dict['message'] = event_history_msgs_dict['event_type'].setdefault('message',{})

                groups = m.groupdict()
                log_num = groups['log_num']

                log_dict = result_dict['message'].setdefault(int(log_num), {})
                log_dict.update({'date': groups['date']})
                log_dict.update({'time': groups['time']})
                log_dict.update({'proc_name': groups['proc_name']})
                log_dict.update({'msg_type': groups['msg_type']})
                log_dict.update({'msg': groups['msg']})
                continue

            #[1] 2021 May 10 12:08:54.364555 [hsrp_engine] E_MTS_RX    [REQ] Opc:MTS_OPC_SDWRAP_DEBUG_DUMP(1530), Id:0X0A8359C5, Ret:SUCCESS
            m = p1_2.match(line)
            if m:
                result_dict = event_history_msgs_dict.setdefault('event_type',{})
                result_dict['message'] = event_history_msgs_dict['event_type'].setdefault('message',{})
                
                groups = m.groupdict()
                log_num = groups['log_num']

                log_dict = result_dict['message'].setdefault(int(log_num), {})
                log_dict.update({'date': groups['date']})
                log_dict.update({'time': groups['time']})
                log_dict.update({'proc_name': groups['proc_name']})
                log_dict.update({'msg_type': groups['msg_type']})
                log_dict.update({'opcode': groups['opcode']})
                log_dict.update({'opcode_id': groups['opcode_id']})
                log_dict.update({'ret_val': groups['ret_val']})
                continue
            
            #Src:0x00000101/46265, Dst:0x00000101/340, Flags:None
            m = p2.match(line)
            if m:
                groups = m.groupdict()

                log_dict = result_dict['message'].setdefault(int(log_num), {})
                log_dict.update({'src_sap': int(groups['src_sap'])})
                log_dict.update({'dst_sap': int(groups['dst_sap'])})
                log_dict.update({'flags': groups['flags']})
                continue
            
            #HA_SEQNO:0X00000000, RRtoken:0x0A8359C5, Sync:UNKNOWN, Payloadsize:308
            m = p3.match(line)
            if m:
                groups = m.groupdict()

                log_dict = result_dict['message'].setdefault(int(log_num), {})
                log_dict.update({'ha_seqno': groups['ha_seqno']})
                log_dict.update({'rr_token': groups['rr_token']})
                log_dict.update({'sync': groups['sync']})
                continue
            
        return event_history_msgs_dict
