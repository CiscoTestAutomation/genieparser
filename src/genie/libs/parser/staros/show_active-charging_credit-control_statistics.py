'''starOS implementation of show active-charging credit-control statistics.py

'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema, Optional

class CreditControlSchema(MetaParser):
    '''Schema for show active-charging credit-control statistics'''

    schema = {
        'cca_info': {
            Any():{
            'Assume Possitive':str,
            'Total Sessions':str,
            Optional('Result Codes'):{
                Optional('2001'):str,
                Optional('2002'):str,
                Optional('2xxx'):str,
                Optional('4001'):str,
                Optional('4002'):str,
                Optional('4010'):str,
                Optional('4011'):str,
                Optional('4012'):str,
                Optional('5001'):str,
                Optional('5002'):str,
                Optional('5003'):str,
                Optional('5004'):str,
                Optional('5005'):str,
                Optional('5006'):str,
                Optional('5031'):str
                }
            }
        }
    }


class ShowCreditControl(CreditControlSchema):
    '''Parser for show active-charging credit-control statistics'''

    cli_command = 'show active-charging credit-control statistics'

    '''         
  Credit Control Group  : Nil - (Uncorrelated)

    CC Session Stats:
      Total Current Sessions:  0             
      Total ECS Adds:          0             Total CC Starts:         0             
      Total Session Updates:   0             Total Terminated:        214358034     
      Session Switchovers:     0             

    CC Message Stats:
      Total Messages Received: 0             Total Messages Sent:     2068          
      Total CC Requests:       0             Total CC Answers:        0             
      CCR-Initial:             0             CCA-Initial:             0             
      CCA-Initial Accept:      0             CCA-Initial Reject:      0             
      CCA-Initial Timeouts:    0             
      CCR-Update:              0             CCA-Update:              0             
      CCA-Update Timeouts:     0             
      CCR-Final:               0             CCA-Final:               0             
      CCA-Final Timeouts:      0             
      CCR-Event:               0             CCA-Event:               0             
      CCA-Event Timeouts:      0             CCR-Event Retry:         0             
      ASR:                     0             ASA:                     0             
      RAR:                     2068          RAA:                     2068          
      CCA Dropped:             0             

    CC Message Error Stats:
      Diameter Protocol Errs:  0             Transient Failures:      0             
      Permanent Failures:      0             Bad Answers:             0             
      Unknown Session Reqs:    0             Unknown Command Code:    0             
      Request Timeouts:        0             Parse Errors:            0             
      Unknown Rating Group:    0             Unknown Rulebase:        0             
      Unk Failure Handling:    0             

    Backpressure Stats:
      CCR-I Messages :         0             CCR-U Messages :         0             
      CCR-T Messages :         0             CCR-E Messages :         0             

    CC Update Reporting Reason Stats:
      Threshold:               0             QHT:                     0             
      Final:                   0             Quota Exhausted:         0             
      Validity Time:           0             Other Quota:             0             
      Rating Condition Change: 0             Forced Reauthorization:  0             

    CC Termination Cause Stats:
      Diameter Logout:         0             Service Not Provided:    0             
      Bad Answer:              0             Administrative:          0             
      Link Broken:             0             Auth Expired:            0             
      User Moved:              0             Session Timeout:         0             

    CC Bad Answer Stats:
      Auth-Application-Id:     0             Session-Id:              0             
      CC-Request-Number:       0             CC-Request-Type:         0             
      Origin-Host:             0             Origin-Realm:            0             
      Parse-Message-Errors:    0             Parse-Mscc-Errors:       0             
      Misc:                    0             

    CC Traffic Category Stats:
      Category Creates:        0             Category Deletes:        0             
      Category Lookups:        0             
      Hits:                    0             Misses:                  0             
      Trigger Events:          0             Final Unit Consumed:     0             
      MSCC GSU Null Grant:     0             MSCC FUI Redirect:       0             
      Category Success:        0             Rating Failed:           0             
      Service Denied:          0             Limit Reached:           0             
      Auth Rejected:           0             Other Errors:            0             

    CCA Initial Message Stats:
      Result Code 2001:        0             Result Code 5003:        0             
      Result Code 4010:        0             Result Code 4011:        0             
      Result Code 4012:        0             Result Code 5031:        0             

    CCA Update Message Stats:
      Result Code 2001:        0             Result Code 5003:        0             
      Result Code 4010:        0             Result Code 4011:        0             
      Result Code 4012:        0             Result Code 5031:        0             

    CCA Event Message Stats:
      Result Code 2001:        0             Other Result Codes:      0             

    Failure Handling Stats:
      Action-Terminated:       0             Action-Continue:         0             
      Offline Active Sessions: 0             Action-Discard:          0             

    CCA Result Code 2xxx Stats:
      Result Code 2xxx:        0             Result Code 2001:        0             
      Result Code 2002:        0             

    CCA Result Code 4xxx Stats:
      Result Code 4001:        0             Result Code 4002:        0             
      Result Code 4010:        0             Result Code 4011:        0             
      Result Code 4012:        0             

    CCA Result Code 5xxx Stats:
      Result Code 5001:        0             Result Code 5002:        0             
      Result Code 5003:        0             Result Code 5004:        0             
      Result Code 5005:        0             Result Code 5006:        0             
      Result Code 5031:        0             
      All Other Result Codes:  0             

    CCA Initial Experimental Result Code Stats:
      Exp Result Code 5199:    0             

    OCS Unreachable Stats:
      Tx-Expiry:               0             Response-TimeOut:        0             
      Connection-Failure:      0             Action-Continue:         0             
      Action-Terminated:       0             Server Retries:          0             

    Assumed-Positive Sessions:
      Current:                 0             Cumulative:              0      
    '''

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        cca_dict = {}
        result_dict = {}
        # initial regexp pattern
        p0 = re.compile(r'^Credit\sControl\sGroup\s+.\s+(?P<ccgroup>.*$)')
        p1 = re.compile(r'Total\sCurrent\sSessions.\s*(?P<sessions>\d+)')
        p2 = re.compile(r'Result\sCode\s(?P<C2>2...):\s+(?P<C2xxx>\d+)')
        p2_2 = re.compile(r'.*?  Result Code (?P<C2_2>2...).*?(?P<C2xxx_2>\d+)')
        p3 = re.compile(r'Result\sCode\s(?P<C4>4...):\s+(?P<C4xxx>\d+)')
        p3_2 = re.compile(r'.*?  Result Code (?P<C4_2>4...).*?(?P<C4xxx_2>\d+)')
        p4 = re.compile(r'Result\sCode\s(?P<C5>5...):\s+(?P<C5xxx>\d+)')
        p4_2 = re.compile(r'.*?  Result Code (?P<C5_2>5...).*?(?P<C5xxx_2>\d+)')
        p5 = re.compile(r'^Current:\s+(?P<assume>\d+)')

        for line in out.splitlines():
            line = line.strip()
            m = p0.match(line)
            if m:
                if 'cca_info' not in cca_dict:
                    result_dict = cca_dict.setdefault('cca_info', {})
                ccgroup = m.groupdict()['ccgroup']
                result_dict[ccgroup] = {}
                continue
            m = p1.match(line)
            if m:
                if 'cca_info' not in cca_dict:
                    result_dict = cca_dict.setdefault('cca_info', {})
                sessions = m.groupdict()['sessions']
                result_dict[ccgroup]["Total Sessions"] = sessions
                continue
            m = p2.match(line)
            if m:
                if 'cca_info' not in cca_dict:
                    result_dict = cca_dict.setdefault('cca_info', {})
                c2xxx = m.groupdict()['C2xxx']
                C2 = m.groupdict()['C2']
                C2_list =["2xxx","2001","2002"]
                if "Result Codes" not in result_dict[ccgroup]:
                    result_dict[ccgroup]["Result Codes"]={}
                for code in C2_list:
                    if code in C2 and int(c2xxx)>1:
                        result_dict[ccgroup]["Result Codes"][code] = c2xxx
                n = p2_2.match(line)
                if n:
                    C2_2 = n.groupdict()['C2_2']
                    c2xxx_2 = n.groupdict()['C2xxx_2']
                    for code in C2_list:
                        if code in C2_2 and int(c2xxx_2)>1:
                            result_dict[ccgroup]["Result Codes"][code] = c2xxx_2
                continue

            m = p3.match(line)
            if m:
                if 'cca_info' not in cca_dict:
                    result_dict = cca_dict.setdefault('cca_info', {})
                c4xxx = m.groupdict()['C4xxx']
                C4 = m.groupdict()['C4']
                C4_list = ["4001","4002","4010","4011","4012"]
                if "Result Codes" not in result_dict[ccgroup]:
                    result_dict[ccgroup]["Result Codes"]={}
                for code in C4_list:
                    if code in C4 and int(c4xxx)>1:
                        result_dict[ccgroup]["Result Codes"][code] = c4xxx
                n = p3_2.match(line)
                if n:
                    C4_2 = n.groupdict()['C4_2']
                    c4xxx_2 = n.groupdict()['C4xxx_2']
                    for code in C4_list:
                        if code in C4_2 and int(c4xxx_2)>1:
                            result_dict[ccgroup]["Result Codes"][code] = c4xxx_2
                continue

            m = p4.match(line)
            if m:
                if 'cca_info' not in cca_dict:
                    result_dict = cca_dict.setdefault('cca_info', {})
                c5xxx = m.groupdict()['C5xxx']
                C5 = m.groupdict()['C5']
                C5_list = ["5001", "5002", "5003", "5004", "5005", "5006", "5031"]
                if "Result Codes" not in result_dict[ccgroup]:
                    result_dict[ccgroup]["Result Codes"]={}
                for code in C5_list:
                    if code in C5 and int(c5xxx)>1:
                        result_dict[ccgroup]["Result Codes"][code] = c5xxx
                n = p4_2.match(line)
                if n:
                    C5_2 = n.groupdict()['C5_2']
                    c5xxx_2 = n.groupdict()['C5xxx_2']
                    for code in C5_list:
                        if code in C5_2 and int(c5xxx_2)>1:
                            result_dict[ccgroup]["Result Codes"][code] = c5xxx_2
                continue
            
            m = p5.match(line)
            if m:
                if 'cca_info' not in cca_dict:
                    result_dict = cca_dict.setdefault('cca_info', {})
                assume = m.groupdict()['assume']
                result_dict[ccgroup]["Assume Possitive"] = assume
                continue

        return cca_dict