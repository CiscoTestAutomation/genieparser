''' show_traffic.py

Parser for the following show commands:
    * show traffic
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =============================================
# Schema for 'show traffic'
# =============================================
class ShowTrafficSchema(MetaParser):
    """Schema for
        * show traffic
    """
    schema = {
        Any(): {
            'received': {
                'duration': int,
                'packets': int,
                'bytes': int,
                'bytes_sec': int,
                'packets_sec': int
            },
            'transmitted': {
                'duration': int,
                'packets': int,
                'bytes': int,
                'bytes_sec': int,
                'packets_sec': int                
            },
            'packets_input_1_minute': int,
            'bytes_input_1_minute': int,
            'packets_output_1_minute': int,
            'bytes_output_1_minute': int,
            'packets_drop_rate_1_minute': int,
            'packets_input_5_minute': int,
            'bytes_input_5_minute': int,
            'packets_output_5_minute': int,
            'bytes_output_5_minute': int,
            'packets_drop_rate_5_minute': int
        },
    }

# =============================================
# Parser for 'show traffic'
# =============================================
class ShowTraffic(ShowTrafficSchema):
    """Parser for
        * show traffic
    """

    cli_command = 'show traffic'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # GigabitEthernet0/0:
        p1 = re.compile(r'^(?P<name>\S+):$')

        # received (in 1618693.940 secs):
        # transmitted (in 1618693.940 secs):
        p2 = re.compile(r'^(?P<queue>\S+).+?(?P<duration>\d+\.\d+)\s+\S+')

        # 415466249 packets       29074806307 bytes
        p3 = re.compile(r'(?P<packets>\d+)\s+packets\s+(?P<bytes>\d+)\s+\S*')

        # 1 pkts/sec      17001 bytes/sec
        p4 = re.compile(r'(?P<packets_sec>\d+)\s+pkts\/sec\s+(?P<bytes_sec>\d+)\s+bytes\/sec$')

        # 1 minute input rate 9452 pkts/sec,  661142 bytes/sec
        p5 = re.compile(r'^1 minute input rate\s+(?P<packets_input_1_minute>\d+)\s+pkts\/sec,\s+'
            '(?P<bytes_input_1_minute>\d+)\s+bytes\/sec$')

        # 1 minute output rate 206 pkts/sec,  41887 bytes/sec    
        p6 = re.compile(r'^1 minute output rate\s+(?P<packets_output_1_minute>\d+)\s+pkts\/sec,\s+'
            '(?P<bytes_output_1_minute>\d+)\s+bytes\/sec$')

        # 1 minute drop rate, 0 pkts/sec    
        p7 = re.compile(r'^1 minute drop rate,\s+(?P<packets_drop_rate_1_minute>\d+)\s+pkts\/sec$')
        
        # 5 minute input rate 11309 pkts/sec,  790978 bytes/sec
        p8 = re.compile(r'^5 minute input rate\s+(?P<packets_input_5_minute>\d+)\s+pkts\/sec,\s+'
            '(?P<bytes_input_5_minute>\d+)\s+bytes\/sec$')
        
        # 5 minute output rate 0 pkts/sec,  0 bytes/sec
        p9 = re.compile(r'^5 minute output rate\s+(?P<packets_output_5_minute>\d+)\s+pkts\/sec,\s+'
            '(?P<bytes_output_5_minute>\d+)\s+bytes\/sec$')
        
        # 5 minute drop rate, 0 pkts/sec
        p10 = re.compile(r'^5 minute drop rate,\s+(?P<packets_drop_rate_5_minute>\d+)\s+pkts\/sec$')



        for line in out.splitlines():
            line=line.strip()
            
            # GigabitEthernet0/0:
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                instance_dict = ret_dict.setdefault(groups['name'], {})
                continue           
            
            # received (in 1618693.940 secs):
            # transmitted (in 1618693.940 secs):
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                if groups['duration']:
                    duration = int(groups['duration'].split('.')[0])
                    groups['duration'] = duration
                    instance_dict.update({groups['queue'] : {'duration' : groups['duration']}})
                    #Each iteration that will change to be the value that lives in queue. Reusable variable
                    queue = groups['queue']            
                    continue
            
            # 415466249 packets       29074806307 bytes
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                instance_dict[queue].update({'packets' : int(groups['packets']), 'bytes' : int(groups['bytes'])})
                continue
            
            # 1 pkts/sec      17001 bytes/sec
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                instance_dict[queue].update(
                    {'packets_sec' : int(groups['packets_sec']), 'bytes_sec' : int(groups['bytes_sec'])}
                )
                continue
            
            # 1 minute input rate 9452 pkts/sec,  661142 bytes/sec
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update(
                    {'packets_input_1_minute' : int(groups['packets_input_1_minute']), 'bytes_input_1_minute' : int(groups['bytes_input_1_minute'])}
                )
                continue
            
            # 1 minute output rate 206 pkts/sec,  41887 bytes/sec 
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update(
                    {'packets_output_1_minute' : int(groups['packets_output_1_minute']), 'bytes_output_1_minute' : int(groups['bytes_output_1_minute'])}
                )
                continue
            
            # 1 minute drop rate, 0 pkts/sec 
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'packets_drop_rate_1_minute' : int(groups['packets_drop_rate_1_minute'])})
                continue
            
            # 5 minute input rate 11309 pkts/sec,  790978 bytes/sec
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update(
                    {'packets_input_5_minute' : int(groups['packets_input_5_minute']), 'bytes_input_5_minute' : int(groups['bytes_input_5_minute'])}
                )
                continue
            
            # 5 minute output rate 0 pkts/sec,  0 bytes/sec
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update(
                    {'packets_output_5_minute' : int(groups['packets_output_5_minute']), 'bytes_output_5_minute' : int(groups['bytes_output_5_minute'])}
                )
                continue
            
            # 5 minute drop rate, 0 pkts/sec
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'packets_drop_rate_5_minute' : int(groups['packets_drop_rate_5_minute'])})
                continue 
            
        return ret_dict