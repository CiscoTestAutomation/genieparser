''' show_snmp.py

IOSXE parsers for the following show commands:
    * show snmp mib
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ==========================
# Schema for 'show snmp mib'
# ==========================
class ShowSnmpMibSchema(MetaParser):

    ''' Schema for "show snmp mib" '''

    schema = {
        Any(): 
            {Optional(Any()): 
                {Optional(Any()): str,
                },
            },
        }


# ==========================
# Parser for 'show snmp mib'
# ==========================
class ShowSnmpMib(ShowSnmpMibSchema):

    ''' Parser for "show snmp mib" '''

    cli_command = 'show snmp mib'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # lldpLocalSystemData.1
        # dot3adAggPortDebugPartnerSyncTransitionCount
        p1 = re.compile(r'^(?P<snmp>([a-zA-Z0-9]+))(?:\.(?P<num>(\d+)))?$')

        # optIfObjects.1.1.1
        # mib-10.49.1.3.1.1.9
        # rmon.10.76.1.1
        # rmon.19.1
        p2 = re.compile(r'^(?P<snmp>([a-zA-Z0-9\-\.]+))$')

        for line in out.splitlines():
            line = line.strip()

            # lldpLocalSystemData.1
            # dot3adAggPortDebugPartnerSyncTransitionCount
            m = p1.match(line)
            if m:
                group = m.groupdict()
                item_dict = ret_dict.setdefault(group['snmp'], {})
                if group['num']:
                    num_dict = item_dict.setdefault(group['num'], {})
                continue

            # rmon.19.1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                item_dict = ret_dict.setdefault(group['snmp'], {})
                continue

        return ret_dict

