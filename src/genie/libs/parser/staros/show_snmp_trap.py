"""starOS implementation of show snmp trap.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowSNMPSchema(MetaParser):
    """Schema for show port table"""

    schema = {
        'snmp_info': {
            Any(): {
                'Date': str,
                'Time': str,
                'Trap': str
            },
        }    
    }


class ShowSNMP(ShowSNMPSchema):
    """Parser for show snmp trap history"""

    cli_command = 'show snmp trap history'

    """
Wed Aug 10 09:45:04 2022 Internal trap notification 53 (CLISessionEnd) user CERT_digidata_ASR privilege level Security Administrator ttyname /dev/pts/5
Wed Aug 10 09:45:32 2022 Internal trap notification 1215 (CPUWarn) facility cli instance 5008255 card 5 cpu 0 allocated 600 used 546
Wed Aug 10 09:46:42 2022 Internal trap notification 1220 (CPUOverClear) facility vpnctrl instance 0 card 5 cpu 0 allocated 150 used 58
Wed Aug 10 09:46:42 2022 Internal trap notification 1216 (CPUWarnClear) facility vpnctrl instance 0 card 5 cpu 0 allocated 150 used 58
Wed Aug 10 09:47:12 2022 Internal trap notification 52 (CLISessionStart) user ag796c privilege level Security Administrator ttyname /dev/pts/5
Wed Aug 10 09:49:20 2022 Internal trap notification 53 (CLISessionEnd) user m47902 privilege level Security Administrator ttyname 
Wed Aug 10 09:52:02 2022 Internal trap notification 52 (CLISessionStart) user CERT_PRIME privilege level Security Administrator ttyname /dev/pts/2
Wed Aug 10 09:52:21 2022 Internal trap notification 53 (CLISessionEnd) user CERT_PRIME privilege level Security Administrator ttyname /dev/pts/2
Wed Aug 10 09:54:02 2022 Internal trap notification 52 (CLISessionStart) user CERT_PRIME privilege level Security Administrator ttyname /dev/pts/2
Wed Aug 10 09:54:22 2022 Internal trap notification 53 (CLISessionEnd) user CERT_PRIME privilege level Security Administrator ttyname /dev/pts/2
Wed Aug 10 09:54:41 2022 Internal trap notification 1113 (EGTPCPathFailClear) context SAEGW, service SGW-S5, interface type sgw-egress, self address 201.175.153.170,  peer address 217.168.3.33, peer restart counter 2,   peer session count  3, clear reason echo-req
Wed Aug 10 09:54:52 2022 Internal trap notification 1112 (EGTPCPathFail) context SAEGW, service SGW-S5, interface type sgw-egress, self address 201.175.153.170,  peer address 186.37.245.1, peer old restart counter 5,  peer new restart counter 5,  peer session count  4, failure reason no-response-from-peer,  path failure detection Enabled
Wed Aug 10 09:54:54 2022 Internal trap notification 1112 (EGTPCPathFail) context SAEGW, service SGW-S5, interface type sgw-egress, self address 201.175.153.170,  peer address 190.91.232.132, peer old restart counter 6,  peer new restart counter 6,  peer session count  5, failure reason no-response-from-peer,  path failure detection Enabled
Wed Aug 10 09:55:09 2022 Internal trap notification 1112 (EGTPCPathFail) context SAEGW, service SGW-S5, interface type sgw-egress, self address 201.175.153.170,  peer address 186.37.245.35, peer old restart counter 16,  peer new restart counter 16,  peer session count  1, failure reason no-response-from-peer,  path failure detection Enabled
Wed Aug 10 09:56:05 2022 Internal trap notification 1113 (EGTPCPathFailClear) context SAEGW, service SGW-S5, interface type sgw-egress, self address 201.175.153.170,  peer address 186.37.245.1, peer restart counter 5,   peer session count  2, clear reason echo-req
Wed Aug 10 09:56:06 2022 Internal trap notification 1184 (TestModeEntered) context local user dv503s ttyname /dev/pts/4 address type IPV4 remote ip address 10.32.1.144
Wed Aug 10 09:57:21 2022 Internal trap notification 53 (CLISessionEnd) user dv503s privilege level Security Administrator ttyname /dev/pts/4
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        trap_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'\w+\s(?P<date>\w+\s\d+)\s(?P<time>\d+:\d+:\d+)\s\d+\s\w+\s\w+\s\w+\s\d+\s.(?P<trap>\w*)')
        trap_number =1
        for line in out.splitlines():
            line = line.strip()
            m = p0.match(line)
            if m:
                if 'snmp_info' not in trap_dict:
                    result_dict = trap_dict.setdefault('snmp_info',{})
                trap_secuence = "trap_"+str(trap_number)
                date = m.groupdict()['date']
                time = m.groupdict()['time']
                trap = m.groupdict()['trap']
                trap_number+=1
                result_dict[trap_secuence] = {}
                result_dict[trap_secuence]["Date"]=date
                result_dict[trap_secuence]["Time"]=time
                result_dict[trap_secuence]["Trap"]=trap

        return trap_dict