""" show_snmpv3user.py

AireOS parser for the following command:
    * 'show snmpv3user'

"""

from queue import PriorityQueue
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ======================
# Schema for:
#  * 'show snmpv3user'
# ======================

class ShowSnmpv3UserSchema(MetaParser):
    """Schema for show snmpv3user"""

    schema = {
        "snmp_username": {
            str: {
                "access_mode": str,
                "authentication": str,
                "encryption": str,
            }
        }
    }
# ======================
# Parser for:
#  * 'show snmpv3user'
# ======================
class ShowSnmpv3UserSchema(ShowSnmpv3UserSchema):
    """Parser for show snmpv3user"""

    cli_command = 'show snmpv3user'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        snmpv3user_dict = {}   

        #SNMP v3 User Name    AccessMode  Authentication Encryption   
        #-------------------- ----------- -------------- ----------   
        #zabbix                Read/Write  HMAC-SHA       CFB-AES     
        #zenoss                Read/Write  HMAC-SHA       CFB-AES     
        #piadmin               Read/Write  HMAC-SHA       CFB-AES     
        #snmp_dnac             Read Only   HMAC-SHA       CFB-AES     
        #snmp_dnas             Read/Write  HMAC-SHA       CFB-AES     
        #sciencelogic          Read/Write  HMAC-SHA       CFB-AES 
        #zabbix                Read/Write  HMAC-SHA       CFB-AES 

        snmp_user_info_capture = re.compile(r"^(?P<snmp_user>\S+)\s+(?P<access_mode>\S+)\s+(?P<authentication>\S+)\s+(?P<encryption>\S+)$")

        for line in out.splitlines():
            line = line.strip()
            #SNMP v3 User Name    AccessMode  Authentication Encryption 
            if line.startswith('SNMP'):
                continue
            elif line.startswith('-----'):
                continue
            elif snmp_user_info_capture.match(line):
                snmp_user_info_capture_match = snmp_user_info_capture.match(line)
                groups = snmp_user_info_capture_match.groupdict()
                snmp_user = groups['snmp_user']
                access_mode = groups['access_mode']
                authentication = groups['authentication']
                encryption = groups['encryption']
                if not snmpv3user_dict.get('snmp_username', {}):
                    snmpv3user_dict['snmp_username'] = {}
                snmpv3user_dict['snmp_username'][snmp_user] = {}
                snmpv3user_dict['snmp_username'][snmp_user].update({'access_mode':  access_mode})
                snmpv3user_dict['snmp_username'][snmp_user].update({'authentication':  authentication})
                snmpv3user_dict['snmp_username'][snmp_user].update({'encryption':  encryption})
                continue

        return snmpv3user_dict



            

