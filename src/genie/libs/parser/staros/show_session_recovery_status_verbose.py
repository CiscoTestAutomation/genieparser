"""starOS implementation of show_session_recovery_status_verbose.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowVerboseSchema(MetaParser):
    """Schema for show session recovery status verbose"""

    schema = {
        'session_recovery_table': {
            Any(): {
                'STATE': str,
                'SESSMGR ACTIVE': str,
                'SESSMGR STANDBY': str,
                'AAAMGR ACTIVE': str,
                'AAAMGR STANDBY': str,
                'DEMUX ACTIVE': str,
                'STATUS': str
            },
        }    
    }


class ShowRecovery(ShowVerboseSchema):
    """Parser for show session recovery status verbose"""

    cli_command = 'show session recovery status verbose'

    """
 cpu state    active standby  active standby  active  status
---- -------  ------ -------  ------ -------  ------  -------------------------
 1/0 Active   48     1        48     1        0       Good                     
 1/1 Active   48     1        47     1        0       Good                     
 1/2 Active   48     1        49     1        0       Good                     
 2/0 Active   48     1        48     1        0       Good                     
 2/1 Active   48     1        48     1        0       Good                     
 2/2 Active   48     1        48     1        0       Good                     
 3/0 Active   48     1        48     1        0       Good                     
 3/1 Active   48     1        48     1        0       Good                     
 3/2 Active   48     1        48     1        0       Good                     
 4/0 Standby  0      48       0      49       0       Good                     
 4/1 Standby  0      48       0      48       0       Good                     
 4/2 Standby  0      48       0      49       0       Good                     
 5/0 Active   0      0        0      0        14      Good (Demux)             
    
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        recovery_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'(?P<cpu>\d.\d)\s+(?P<state>\w+)\s+(?P<s_active>\d+)\s+(?P<s_standby>\d+)\s+(?P<a_active>\d+)\s+(?P<a_standby>\d+)\s+(?P<demux>\d+)\s+(?P<status>\w+)')
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'session_recovery_table' not in recovery_dict:
                    result_dict = recovery_dict.setdefault('session_recovery_table',{})
                cpu = m.groupdict()['cpu']
                state = m.groupdict()['state']
                s_active = m.groupdict()['s_active']
                s_standby = m.groupdict()['s_standby']
                a_active = m.groupdict()['a_active']
                a_standby = m.groupdict()['a_standby']
                demux = m.groupdict()['demux']
                status = m.groupdict()['status']
                result_dict[cpu] = {}
                result_dict[cpu]['STATE'] = state
                result_dict[cpu]['SESSMGR ACTIVE'] = s_active
                result_dict[cpu]['SESSMGR STANDBY'] = s_standby
                result_dict[cpu]['AAAMGR ACTIVE'] = a_active
                result_dict[cpu]['AAAMGR STANDBY'] = a_standby
                result_dict[cpu]['DEMUX ACTIVE'] = demux
                result_dict[cpu]['STATUS'] = status          
                continue

        return recovery_dict