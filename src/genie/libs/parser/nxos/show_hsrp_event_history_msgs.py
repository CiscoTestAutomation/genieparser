from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

# ====================================================
# Schema for 'show hsrp internal event-history msgs'
# ====================================================
class ShowHsrpEventHistoryMsgsSchema(MetaParser):
    
    ''' Schema for "show hsrp internal event-history msgs" '''

    schema = {  
        "msgs":{
            Any():{
                 'date' : str,
                 'time' : str,
                 'proc_name' : str,
                 'msg_type' : str,
                 Optional('debug_msg'): str,
                 Optional('opcode'): str,
                 Optional('opcode_id'): str,
                 Optional('ret_val'): str,
                 Optional('src_sap'): str,
                 Optional('dst_sap'): str,
                 Optional('flags'): str,
                 Optional('ha_seqno'): str,
                 Optional('rr_token'): str,
                 Optional('sync'): str

            } 
        }       
    }

import re

# ====================================================
# Parser for 'show hsrp internal event-history msgs'
# ====================================================
class ShowHsrpEventHistoryMsgs(ShowHsrpEventHistoryMsgsSchema):

    ''' Parser for "show hsrp internal event-history msgs"'''

    cli_command = 'show hsrp internal event-history msgs'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        event_history_msgs_dict={}
        result_dict={}

        p1_1 = re.compile(r'^\[(?P<log_num>\d+)\]\s+(?P<date>\d{4} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-9]{1,2}) (?P<time>[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{6}) \[(?P<proc_name>[^\]]+)\] (?P<msg_type>E_DEBUG_DSF)\s+(?P<debug_msg>.+)$')
        p1_2 = re.compile(r'^\[(?P<log_num>\d+)\]\s+(?P<date>\d{4} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-9]{1,2}) (?P<time>[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{6}) \[(?P<proc_name>[^\]]+)\] (?P<msg_type>E_MTS_RX|E_MTS_TX)\s+\[(REQ|NOT)\] Opc:(?P<opcode>[^,]+), Id:(?P<opcode_id>[^,]+), Ret:(?P<ret_val>.+)$')
        p2 = re.compile(r'^\s*Src:[^\/]+\/(?P<src_sap>\d+), Dst:[^\/]+\/(?P<dst_sap>\d+), Flags:(?P<flags>.+)$')
        p3 = re.compile(r'^\s*HA_SEQNO:(?P<ha_seqno>[^,]+), RRtoken:(?P<rr_token>[^,]+), Sync:(?P<sync>[^,]+), Payloadsize:(\d+)$')
        #p4 = re.compile(r'^\s*Payload:\s*$')
        #p5 = re.compile(r'^\s*.*$')

        for line in out.splitlines():
            line = line.strip()

            m = p1_1.match(line)
            if m:
                if 'msgs' not in event_history_msgs_dict:
                    result_dict = event_history_msgs_dict.setdefault('msgs',{})
                log_num = m.groupdict()['log_num']
                date = m.groupdict()['date']
                time = m.groupdict()['time']
                proc_name = m.groupdict()['proc_name']
                msg_type = m.groupdict()['msg_type']
                debug_msg = m.groupdict()['debug_msg']

                result_dict[log_num] = {}
                result_dict[log_num]['date'] = date
                result_dict[log_num]['time'] = time
                result_dict[log_num]['proc_name'] = proc_name
                result_dict[log_num]['msg_type'] = msg_type
                result_dict[log_num]['debug_msg'] = debug_msg
                continue

            m = p1_2.match(line)
            if m:
                if 'msgs' not in event_history_msgs_dict:
                    result_dict = event_history_msgs_dict.setdefault('msgs',{})
                log_num = m.groupdict()['log_num']
                date = m.groupdict()['date']
                time = m.groupdict()['time']
                proc_name = m.groupdict()['proc_name']
                msg_type = m.groupdict()['msg_type']
                opcode = m.groupdict()['opcode']
                opcode_id = m.groupdict()['opcode_id']
                ret_val = m.groupdict()['ret_val']
                
                result_dict[log_num] = {}
                result_dict[log_num]['date'] = date
                result_dict[log_num]['time'] = time
                result_dict[log_num]['proc_name'] = proc_name
                result_dict[log_num]['msg_type'] = msg_type
                result_dict[log_num]['opcode'] = opcode
                result_dict[log_num]['opcode_id'] = opcode_id
                result_dict[log_num]['ret_val'] = ret_val
                continue
            
            m = p2.match(line)
            if m:
                src_sap = m.groupdict()['src_sap']
                dst_sap = m.groupdict()['dst_sap']
                flags = m.groupdict()['flags']

                result_dict[log_num]['src_sap'] = src_sap
                result_dict[log_num]['dst_sap'] = dst_sap
                result_dict[log_num]['flags'] = flags
                continue
            
            m = p3.match(line)
            if m:
                ha_seqno = m.groupdict()['ha_seqno']
                rr_token = m.groupdict()['rr_token']
                sync = m.groupdict()['sync']

                result_dict[log_num]['ha_seqno'] = ha_seqno
                result_dict[log_num]['rr_token'] = rr_token
                result_dict[log_num]['sync'] = sync
                continue
            

        return event_history_msgs_dict



        
    
