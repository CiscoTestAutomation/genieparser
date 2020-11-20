"""show_ddos.py

JUNOS parsers for the following commands:
    * show ddos-protection statistics

"""

import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema

class ShowDdosProtectionStatisticsSchema(MetaParser):
    """
    Schema for:
        * show ddos-protection statistics
    """
    
    schema = {
            "ddos-statistics-information": {
                "aggr-level-control-mode": str,
                "aggr-level-detection-mode": str,
                "ddos-flow-detection-enabled": str,
                "ddos-logging-enabled": str,
                "ddos-policing-fpc-enabled": str,
                "ddos-policing-re-enabled": str,
                "detection-mode": str,
                "flow-report-rate": str,
                "flows-cumulative": str,
                "flows-current": str,
                "packet-types-in-violation": str,
                "packet-types-seen-violation": str,
                "total-violations": str,
                "violation-report-rate": str
            }
        }

class ShowDdosProtectionStatistics(ShowDdosProtectionStatisticsSchema):
    """ Parser for:
        * show ddos-protection statistics
    """

    cli_command = 'show ddos-protection statistics'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        res = {}        

        # DDOS protection global statistics:
        p1 = re.compile(r'^DDOS protection global statistics:$')

        # Policing on routing engine:         Yes
        # Policing on FPC:                    Yes
        # Flow detection:                     No
        # Logging:                            Yes
        # Policer violation report rate:      100
        # Flow report rate:                   100
        # Default flow detection mode         Automatic
        # Default flow level detection mode   Automatic
        # Default flow level control mode     Drop
        # Currently violated packet types:    0
        # Packet types have seen violations:  0
        # Total violation counts:             0
        # Currently tracked flows:            0
        # Total detected flows:               0
        p2 = re.compile(r'(?P<key>[\s\S]+)(:|mode) +(?P<value>[\w\d]+)')

        keys_dict = {
            'Policing on routing engine': 'ddos-policing-re-enabled',
            'Policing on FPC': 'ddos-policing-fpc-enabled',               
            'Flow detection': 'ddos-flow-detection-enabled',
            'Logging': 'ddos-logging-enabled',                          
            'Policer violation report rate': 'violation-report-rate',  
            'Flow report rate':'flow-report-rate',
            'Default flow detection ': 'detection-mode',      
            'Default flow level detection ': 'aggr-level-detection-mode',
            'Default flow level control ': 'aggr-level-control-mode',
            'Currently violated packet types': 'packet-types-in-violation',
            'Packet types have seen violations': 'packet-types-seen-violation',
            'Total violation counts': 'total-violations',      
            'Currently tracked flows': 'flows-current',        
            'Total detected flows': 'flows-cumulative'                  
        }

        for line in out.splitlines():
            line = line.strip()            

            m = p1.match(line)
            if m:
                res = {'ddos-statistics-information':{}}
                continue
            
            m = p2.match(line)
            if m:
                group = m.groupdict()
                key = group['key']
                value = group['value']

                res['ddos-statistics-information'][keys_dict[key]] = value 
                continue

        return res