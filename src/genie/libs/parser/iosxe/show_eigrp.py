''' show_ip_eirgp.py
IOSXE parsers for the following commands

    * 'show ip eigrp neighbors'
    * 'show ip eigrp neighbors detail'
'''

#Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# Libs
from genie.libs.parser.utils.common import Common

class ShowEigrpNeighborsSchema(MetaParser):
    ''' Schema for:
        * 'show ip eigrp neighbors'
    '''

    schema = { 
        'eigrp': {
            Optional('index'):
                {Any():
                    {'peer_handle': int,
                     'nbr_address': str,
                     'interface': str,
                     'hold_time': int,
                     'uptime': str,
                     'q_cnt': int,
                     'last_seq_number': int,
                     'srtt': int,
                     'rto': float, },
            },
        },
    }

# ====================================
# Parser for 'show ip eigrp neighbors'
# ====================================
class ShowEigrpNeighbors(ShowEigrpNeighborsSchema):

    cli_command = 'show ip eigrp neighbors'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {'eirgp': {}}

        # H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
        #                             (sec)           (ms)          Cnt Num
        # 0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
        # 2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5
        # 1   10.1.2.3     Gi0/1      11    00:20:39  2202   5000   0   5
        r1 = re.compile(r'^(?P<peer_handle>\d+) +'
                         '(?P<nbr_address>\S+) +'
                         '(?P<interface>[A-Za-z]+\s*[\d\/]+) +'
                         '(?P<hold_time>\d+) +(?P<uptime>\S+) +'
                         '(?P<srtt>\d+) +'
                         '(?P<rto>\d+) +'
                         '(?P<q_cnt>\d+) +'
                         '(?P<last_seq_num>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            result = r1.match()

            if result:
                group = result.groupdict()

                device_dict = devices_dict_info.setdelfault(device_id_index, {})

                device_dict['peer_handle'] = group['peer_handle']
                device_dict['nbr_address'] = group['nbr_address']
                device_dict['interface'] = group['interface']
                device_dict['hold_time'] = group['hold_time']
                device_dict['uptime'] = group['uptime']
                device_dict['srtt'] = group['srtt']
                device_dict['rto'] = group['rto']
                device_dict['q_cnt'] = group['q_cnt']
                device_dict['last_seq_num'] = group['last_seq_num']

        if device_id_index:
             parsed_dict.setdefault('cdp', {}).\
                setdefault('index', devices_dict_info)

        return parsed_dict