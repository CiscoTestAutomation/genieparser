"""starOS implementation of show_service_all.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowServiceSchema(MetaParser):
    """Schema for show service all"""

    schema = {
        'service_all': {
            Any(): {
                'CONTEXTID': str,
                'SERVICEID': str,
                'CONTEXTNAME': str,
                'STATE': str,
                'SESSIONS': str,
                'TYPES': str
            },
        }    
    }


class ShowService(ShowServiceSchema):
    """Parser for show service all"""

    cli_command = 'show service all'

    """
ContextID   ServiceID   ContextName   ServiceName   State         Sessions   Type
---------   ---------   -----------   -----------   ----------    -----------   ----
2           1           SAEGW         GTPU_ePDG     Started       0             gtpu
2           2           SAEGW         PGW-S5        Started       0             gtpu
2           3           SAEGW         SGW-S1u       Started       0             gtpu
2           4           SAEGW         SGW-S5        Started       0             gtpu
2           5           SAEGW         GGSN          Started       12000000      ggsn
2           6           SAEGW         EGTP_ePDG     Started       0             egtp
2           7           SAEGW         PGW-S5        Started       0             egtp
2           8           SAEGW         SGW-S11       Started       0             egtp
2           9           SAEGW         SGW-S5        Started       0             egtp
2           10          SAEGW         PGW-SVC       Started       10000000      pgw
2           11          SAEGW         SGW-SVC       Started       10000000      sgw
2           12          SAEGW         SAEGW         Started       10000000      saegw
7           1           Gx            Gxd-IUSA      Started       0             imsa
7           2           Gx            Gxd-Nextel    Started       0             imsa
7           3           Gx            IMS-IPv6      Started       0             imsa
7           4           Gx            IMS_SOS       Started       0             imsa
7           5           Gx            IMS_VOLTE_ORACLE Started       0             imsa
10          13          ePDG          ePDG          Initialized   0             epdg             
    
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
        p0 = re.compile(r'(?P<contextid>^\d+)\s+(?P<serviceid>\d+)\s+(?P<contextname>\w+)\s+(?P<servicename>.*?)\s+(?P<state>\w+)\s+(?P<sessions>\d+)\s+(?P<types>\w+)')
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'service_all' not in recovery_dict:
                    result_dict = recovery_dict.setdefault('service_all',{})
                contextid = m.groupdict()['contextid']
                serviceid = m.groupdict()['serviceid']
                contextname = m.groupdict()['contextname']
                servicename = m.groupdict()['servicename']
                state = m.groupdict()['state']
                sessions = m.groupdict()['sessions']
                types = m.groupdict()['types']
                result_dict[servicename] = {}
                result_dict[servicename]['CONTEXTID'] = contextid
                result_dict[servicename]['SERVICEID'] = serviceid
                result_dict[servicename]['CONTEXTNAME'] = contextname
                result_dict[servicename]['STATE'] = state
                result_dict[servicename]['SESSIONS'] = sessions
                result_dict[servicename]['TYPES'] = types          
                continue

        return recovery_dict