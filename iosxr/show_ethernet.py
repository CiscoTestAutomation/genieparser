import re

from metaparser import MetaParser
from metaparser.util.schemaengine import Any

from xbu_shared.parser.base import *

class ShowEthernetCfmMeps(MetaParser):

    # TODO schema

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def cli(self):

        cmd = 'show ethernet cfm peer meps'

        out = self.device.execute(cmd)

        result = {
            'entries' : []
        }

        # Sample Output

        # Flags:
        # > - Ok                          I - Wrong interval
        # R - Remote Defect received      V - Wrong level
        # L - Loop (our MAC received)     T - Timed out
        # C - Config (our ID received)    M - Missing (cross-check)
        # X - Cross-connect (wrong MAID)  U - Unexpected (cross-check)
        # * - Multiple errors received    S - Standby
        # 
        # Domain domain7_1 (level 7), Service service7_1
        # Down MEP on GigabitEthernet0/0/1/0.1 MEP-ID 10
        # ================================================================================
        # St    ID MAC Address    Port    Up/Downtime   CcmRcvd SeqErr   RDI Error
        # -- ----- -------------- ------- ----------- --------- ------ ----- -----
        #  >    40 a80c.0d4f.18d2 Up      13:20:10        48010      0     0     0
        # 
        # Domain domain7_2 (level 7), Service service7_2
        # Down MEP on GigabitEthernet0/0/1/0.2 MEP-ID 10
        # ================================================================================
        # St    ID MAC Address    Port    Up/Downtime   CcmRcvd SeqErr   RDI Error
        # -- ----- -------------- ------- ----------- --------- ------ ----- -----
        #  >    40 a80c.0d4f.18d2 Up      13:20:10        48010      0     0     0

        title_found = False
        header_processed = False
        field_indice = []

        def _retrieve_fields(line,field_indice):
            res = []
            for idx,(start,end) in enumerate(field_indice):
                if idx == len(field_indice) - 1:
                    res.append(line[start:].strip())
                else:
                    res.append(line[start:end].strip())
            return res

        lines = out.splitlines()
        for idx,line in enumerate(lines):

            m = re.match(r'Domain (\w+).+level (\w+).+Service (\w+)',line)
            if m:
                domain = m.group(1)
                level = m.group(2)
                service = m.group(3)

            m = re.match(r'.+ on (\S+) MEP-ID (\w+)',line)
            if m:
                interface = m.group(1)
                local_id = m.group(2)
                
            if idx == len(lines) - 1:
                break

            line = line.rstrip()
            if not header_processed:
                # 1. check proper title header exist
                if re.match(r"^St\s+ID\s+MAC Address\s+Port\s+Up/Downtime\s+CcmRcvd\s+SeqErr\s+RDI\s+Error",line):
                    title_found = True
                    continue
                # 2. get dash header line
                if title_found and re.match(r"^(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)",line):
                    match = re.match(r"^(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)",line)
                    start = 0
                    for field in match.groups():
                        if '-' in field:
                            end = start + len(field)
                            field_indice.append((start,end))
                            start = end
                        else:
                            start += len(field)
                            end += len(field)
                    header_processed = True
                    continue

            elif re.match('^\s*$',line):
                title_found = False
                header_processed = False
                field_indice = []

            else:
                status,remote_id,mac,port,time,ccm_rcvd,seq_error,rdi,error = _retrieve_fields(line,field_indice)
                result['entries'].append({
                    'domain' : domain,
                    'level' : level,
                    'service' : service,
                    'status' : status,
                    'remote_id' : remote_id,
                    'local_id' : local_id,
                    'interface' : interface,
                    'mac_address' : mac,
                    'time' : time,
                    'ccm_rcvd' : ccm_rcvd,
                    'seq_error' : seq_error,
                    'rdi' : rdi,
                    'error' : error,
                })

        return result

# vim: ft=python ts=8 sw=4 et
