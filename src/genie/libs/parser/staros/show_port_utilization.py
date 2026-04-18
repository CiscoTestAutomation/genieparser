"""starOS implementation of show_port_utilization.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowPortUtilizationSchema(MetaParser):
    """Schema for show port utilization table"""

    schema = {
        'port_table': {
            Any(): {
                'current_rx': str,
                'current_tx': str,
                '5min_rx': str,
                '5min_tx': str,
                '15min_rx': str,
                '15min_tx': str
            },
        }    
    }


class ShowPortUtilization(ShowPortUtilizationSchema):
    """Parser for show port utilization table"""

    cli_command = 'show port utilization table'

    """
                                ------ Average Port Utilization (in mbps) ------
Port   Type                       Current           5min             15min    
                                 Rx      Tx      Rx       Tx       Rx     Tx
----- ------------------------  ------- -------  ------- -------  ------- -------
 1/1  Virtual Ethernet          0       0        0       0        0       0      
 1/10 Virtual Ethernet          0       0        0       0        0       0      
 1/11 Virtual Ethernet          0       0        0       0        0       0      
 1/12 Virtual Ethernet          0       0        0       0        0       0      
 1/13 Virtual Ethernet          0       0        0       0        0       0      
 1/14 Virtual Ethernet          0       0        0       0        0       0      
 1/15 Virtual Ethernet          0       0        0       0        0       0      
 1/16 Virtual Ethernet          0       0        0       0        0       0      
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        port_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'((?P<port_id>\d+.\d+)\s+(10G|Virtual)\sEthernet\s+(?P<rx_cur>\d+)\s+(?P<tx_cur>\d+)\s+(?P<rx_5min>\d+)\s+(?P<tx_5min>\d+)\s+(?P<rx_15min>\d+)\s+(?P<tx_15min>\d+))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'port_table' not in port_dict:
                    result_dict = port_dict.setdefault('port_table',{})
                port = m.groupdict()['port_id']
                rx_cur = m.groupdict()['rx_cur']
                tx_cur = m.groupdict()['tx_cur']
                rx_5min = m.groupdict()['rx_5min']
                tx_5min = m.groupdict()['tx_5min']
                rx_15min = m.groupdict()['rx_15min']
                tx_15min = m.groupdict()['tx_15min']
                result_dict[port] = {}
                result_dict[port]['current_rx'] = rx_cur
                result_dict[port]['current_tx'] = tx_cur
                result_dict[port]['5min_rx'] = rx_5min
                result_dict[port]['5min_tx'] = tx_5min
                result_dict[port]['15min_rx'] = rx_15min
                result_dict[port]['15min_tx'] = tx_15min                
                continue

        return port_dict