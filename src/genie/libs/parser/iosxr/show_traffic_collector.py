'''
show_traffic_collector.py

Parser for the following show commands:

* 'show traffic-collector external-interface'
* 'show traffic-collector ipv4 counters prefix <prefix> detail'

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use
# import parser utils
from genie.libs.parser.utils.common import Common


# ======================================================
# Parser for 'show traffic-collector external-interface'
# ======================================================

class ShowTrafficCollecterExternalInterfaceSchema(MetaParser):

        """Schema for show traffic-collector external-interface"""

        schema = {
            'interface':{
                Any():{
                    'status': str
                },
            },
        }

class ShowTrafficCollecterExternalInterface(ShowTrafficCollecterExternalInterfaceSchema):

    ''' Parser for show traffic-collector external-interface '''

    cli_command = ['show traffic-collector external-interface']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        #Init vars
        ret_dict = {}

        # Interface             Status          
        # --------------------  ----------------
        # Te0/1/0/3             Enabled 
        # Te0/1/0/4             Enabled

        p1 = re.compile(r'(?P<interface>^\w+[\.\/\d]+) +(?P<status>\S+)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                interface_dict = ret_dict.setdefault('interface',{}).\
                    setdefault(interface,{})
                interface_dict.update({'status': group['status']})
                continue
        
        return ret_dict

# ========================================================================
# Parser for 'show traffic-collector ipv4 counters prefix <prefix> detail'
# ========================================================================

class ShowTrafficCollecterIpv4CountersPrefixDetailSchema(MetaParser):

    '''Schema show traffic-controller ipv4 counters prefix <prefix> detail '''

    schema = {
        'ipv4_counters':{
            'prefix': {
                Any():{
                    'label': int,
                    'state': str,
                    'counters':{
                        Any():{
                            'average':{
                                'last_collection_intervals': int,
                                'packet_rate':int,
                                'byte_rate':int,
                                },
                            'history_of_counters':{
                                Any():{
                                    'packets': int,
                                    'bytes': int,
                                },
                            },
                        },
                    },
                },
            },
        },
    }

class ShowTrafficCollecterIpv4CountersPrefixDetail(ShowTrafficCollecterIpv4CountersPrefixDetailSchema):

    ''' Parser for 
    show traffic-collector ipv4 counters prefix <prefix> detail
     '''

    cli_command = ['show traffic-collector ipv4 counters prefix {prefix} detail']

    def cli(self, prefix, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(prefix=prefix))
        else:
            out = output

        #Init vars
        ret_dict = {}

        # Prefix: 10.4.1.10/32  Label: 16010 State: Active
        p1 = re.compile(r'Prefix: +(?P<prefix>[\d\.\/]+) +'
        'Label: +(?P<label>\d+) +State: (?P<state>\S+)')

        #Base:
        #TM Counters:
        p2 = re.compile(r'(?P<counters>(Base|TM Counters)):')

        # Average over the last 5 collection intervals:
        p3 = re.compile(r'Average +over +the +last +(?P<interval>\d+) +collection '
        '+intervals:')
            
        # Packet rate: 9496937 pps, Byte rate: 9363979882 Bps
        p4 = re.compile (r'Packet +rate: +(?P<packet_rate>\d+) +pps, Byte '
        '+rate: +(?P<byte_rate>\d+) +Bps')
        
        # History of counters:
        #     23:01 - 23:02: Packets 9379529, Bytes: 9248215594 
        p5 = re.compile(r'(?P<time_slot>[\d\:\-\s]+): +Packets +(?P<packets>\d+), '
        '+Bytes: +(?P<bytes>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # Prefix: 10.4.1.10/32  Label: 16010 State: Active
            m = p1.match(line)
            if m:
                label_list = ['label', 'state']
                group = m.groupdict()
                counters_dict = ret_dict.setdefault('ipv4_counters', {}).\
                    setdefault('prefix', {}).setdefault(group['prefix'], {})
                for key in label_list:
                    value = int (group[key]) if key == 'label'else group[key]
                    counters_dict.update({key: value})
                continue

            #Base:
            #TM Counters:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                type_dict = counters_dict.setdefault('counters', {}).\
                    setdefault(group['counters'].strip().lower().\
                        replace(' ','_'), {})
                continue
            
            # Average over the last 5 collection intervals:
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interval_dict = type_dict.setdefault('average', {})
                interval_dict.update({'last_collection_intervals': int(group['interval'])})
                continue
            
            
            # Packet rate: 9496937 pps, Byte rate: 9363979882 Bps
            m = p4.match(line)
            if m:
                label_list = ['packet_rate', 'byte_rate']
                group = m.groupdict()
                for key in label_list: 
                    interval_dict.update({key: int (group[key])})
                continue

            # History of counters:
            #     23:01 - 23:02: Packets 9379529, Bytes: 9248215594 
            m = p5.match(line)
            if m:
                label_list = ['packets', 'bytes']
                group = m.groupdict()
                time_dict = type_dict.setdefault('history_of_counters', {}).\
                    setdefault(group['time_slot'], {})
                for key in label_list:
                    value = int(group[key])
                    time_dict.update({key: value})
                continue
            
        return ret_dict

