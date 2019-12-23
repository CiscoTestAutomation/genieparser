'''
show_traffic_collector.py

Parser for the following show commands:

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
            'external_interfaces':{
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

                interface_dict = ret_dict.setdefault('external_interfaces',{}).setdefault(group['interface'],{})
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
            'prefix': str,
            'label': int,
            'state': str,
            'counters_type':{
                Any():{
                    Any():{
                        'packet':int,
                        'packet_rate': str,
                        'byte':int,
                        'byte_rate': str
                    },
                    'history_of_counters':{
                        'time_slot':{
                            Any():{
                                'packets': int,
                                'bytes': int,
                            },
                        },
                    },
                },
            },
        },
    }

class ShowTrafficCollecterIpv4CountersPrefixDetail(ShowTrafficCollecterIpv4CountersPrefixDetailSchema):

    ''' Parser for show traffic-collector ipv4 counters prefix <prefix> detail '''

    cli_command = ['Parser for show traffic-collector ipv4 counters prefix {prefix} detail']

    def cli(self, prefix, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(prefix=prefix))
        else:
            out = output

        #Init vars
        ret_dict = {}

        # Prefix: 1.1.1.10/32  Label: 16010 State: Active
        p1 = re.compile(r'Prefix: +(?P<prefix>[\d\.\/]+) +Label: +(?P<label>\d+) +State: (?P<state>\S+)')

        #Base:
        p2 = re.compile(r'(?P<counters_type>(Base|TM Counters)):')

        # Average over the last 5 collection intervals:
        p3 = re.compile(r'Average +over +the +last +(?P<interval>\d+) +collection +intervals:')
            
        # Packet rate: 9496937 pps, Byte rate: 9363979882 Bps
        p4 = re.compile (r'Packet +rate: +(?P<packet>\d+) +(?P<packet_rate>\w+)+, Byte +rate: +(?P<byte>\d+) +(?P<byte_rate>\w+)')
        
        # History of counters:
        #     23:01 - 23:02: Packets 9379529, Bytes: 9248215594 
        #     23:00 - 23:01: Packets 9687124, Bytes: 9551504264 
        #     22:59 - 23:00: Packets 9539200, Bytes: 9405651200 
        #     22:58 - 22:59: Packets 9845278, Bytes: 9707444108 
        #     22:57 - 22:58: Packets 9033554, Bytes: 8907084244   
        p5 = re.compile(r'(?P<time_slot>[\d\:\-\s]+): +Packets +(?P<packets>\d+), +Bytes: +(?P<bytes>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # Prefix: 1.1.1.10/32  Label: 16010 State: Active
            m = p1.match(line)
            if m:
                label_list = ['prefix', 'label', 'state']
                group = m.groupdict()
                counters_dict = ret_dict.setdefault('ipv4_counters', {})
                for key in label_list:
                    
                    value = int (group[key]) if key is 'label'else group[key]
                    counters_dict.update({key: value})

                continue

            #Base:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                type_dict = counters_dict.setdefault('counters_type', {}).setdefault(group['counters_type'].strip().lower().replace(' ','_'), {})
                continue
            
            # Average over the last 5 collection intervals:
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interval_dict = type_dict.setdefault('average_of_last_{}_collection_intervals'.format(group['interval']), {})
                continue
            
            
            # Packet rate: 9496937 pps, Byte rate: 9363979882 Bps
            m = p4.match(line)
            if m:
                label_list = ['packet', 'packet_rate', 'byte', 'byte_rate']
                group = m.groupdict()
                for key in label_list:
                    value = int (group[key]) if key is 'packet' or key is 'byte' else group[key]
                    interval_dict.update({key: value})
                continue

            # History of counters:
            #     23:01 - 23:02: Packets 9379529, Bytes: 9248215594 
            #     23:00 - 23:01: Packets 9687124, Bytes: 9551504264 
            #     22:59 - 23:00: Packets 9539200, Bytes: 9405651200 
            #     22:58 - 22:59: Packets 9845278, Bytes: 9707444108 
            #     22:57 - 22:58: Packets 9033554, Bytes: 8907084244   
            m = p5.match(line)
            if m:
                label_list = ['packets', 'bytes']
                group = m.groupdict()
                history_dict = type_dict.setdefault('history_of_counters', {})
                time_dict = history_dict.setdefault('time_slot', {}).setdefault(group['time_slot'], {})
                for key in label_list:
                    value = int(group[key])
                    time_dict.update({key: value})
                continue

        return ret_dict

