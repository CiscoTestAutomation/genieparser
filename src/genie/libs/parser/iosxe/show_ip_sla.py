'''show_ip_sla.py
IOSXE parsers for the following show commands:
    * show ip sla summary
'''

# Python
import re
import xmltodict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ===============================
# Schema for 'show ip sla summary'
# ===============================
class ShowIpSlaSummarySchema(MetaParser):
    ''' Schema for "show ip sla summary" '''
    schema = {
        'id': {
            Any(): {
                'state': str,
                'type': str,
                'destination': str,
                'rtt_in_milliseconds': float,
                'return_code': str,
                'last_run': str,
            },
        },
    }

# TODO remember to divide bt 1000 if rtt is in microseconds (u)

# ===============================
# Parser for 'show ip sla summary'
# ===============================
class ShowIpSlaSummary(ShowIpSlaSummarySchema):
    """Parser for:
    show ip sla summary
    """

    def cli(self, output=''):

        cli_command = 'show ip sla summary'
        
        parsed_dict = {}

        if output is None:
            out = self.device.execute(cli_command)
        else:
            out = output

        # ID           Type        Destination       Stats       ReturnCode  LastRun
        # -----------------------------------------------------------------------
        # *1           tcp-connect 123.23.213.32     RTT=44      OK          21 seconds ago                                                                                
        # *2           dns         11.121.2.123      -           Timeout     7 seconds ago                                                                              
        # *3           udp-jitter  121.32.11.1       RTT=1       OK          54 seconds ago                                                                             
        # *4           udp-jitter  12.223.33.3       RTT=1       OK          15 seconds ago                                                                                                                                                   
        # *5           udp-jitter  13.132.32.2       RTT=1       OK          8 seconds ago                                                                                
        # *6           udp-jitter  11.311.31.2       RTT=1       OK          40 seconds ago                                                                              
        # *7           icmp-echo   131.31.11.1       RTT=1       OK          2 seconds ago
        
        # ID       Type      Destination  State   Stats(ms)  ReturnCode  LastRun
        # ---      ----      -----------  -----   -------  ----------  -------
        # 100   icmp-jitter   192.0.2.2    Active   100      OK       22:49:53 PST Tue May 3 2011
        # 101   udp-jitter    192.0.2.2    Active   100      OK       22:49:53 PST Tue May 3 2011
        # 102   tcp-connect   192.0.2.2    Active    -      NoConnection  22:49:53 PST Tue May 3 2011
        # 103   video         1232:232  		 Active   100      OK       22:49:53 PST Tue May 3 2011  
        #                       ::222                                                                  
        # 104   video         1232:232  		 Active   100      OK       22:49:53 PST Tue May 3 2011 
        #                       ::222  
        
        p1 = re.compile(r'^(?P<state_symbol>\*|\^|\~)*(?P<id>[\d]+) +'
            '(?P<type>[\w-]+) +(?P<destination>[\d.]+) +(?P<state_word>[\w]+)*'
            ' +(RTT=)*(?P<rtt_in_milliseconds>[\d]+)(?P<is_microseconds>u)* +'
            '(?P<return_code>[\w]+) +(?P<last_run>[\w\: ]+)')

        p2 = re.compile(r'(?P<extended_ip_address>[\d\:\.]+)')
        
        for line in out.splitlines():

            m = p1.match(line)
            if m:
                group = m.groupdict()
                id = group['id']
                id_dict = parsed_dict.setdefault(id, {})
                id_dict['type'] = group['type']
                id_dict['destination'] = group['destination']
                id_dict['rtt_in_milliseconds'] = group['rtt_in_milliseconds']
                id_dict['return_code'] = group['return_code']
                id_dict['last_run'] = group['last_run']

                # State can be a *, ^, or ~ at front of line, or can be a word
                if group['state_symbol'] == '*':
                    id_dict['state'] = 'active' 
                elif group['state_symbol'] == '^':
                    id_dict['state'] = 'inactive'
                elif group['state_symbol'] == '~':
                    id_dict['state'] = 'pending'
                else:
                    id_dict['state'] = group['state_word'].lower()

                # RTT is in microseconds if followed by a "u"
                if group['is_microseconds']:
                    id_dict['rtt_in_milliseconds'] /= 1000

                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict['destination'].join(group['extended_ip_address'])


        # if out:
        #     headers = [['ID','Type','Destination','Stats','Return','Last'],['','','','','Code','Run']]
        #     result = parsergen.oper_fill_tabular(device_output = out, header_fields=headers, label_fields = ['id','type','destination','rtt_stats_mseconds','return_code','last_run_seconds_ago'])
        #     struct_output = result.entries
        #     if struct_output:
        #         for id, id_dict in struct_output.items():
        #             if id:
        #                 # Defining patterns to be matched for different columns
        #                 # The patterns for the state of the ip sla probe defined by the Codes: * active, ^ inactive, ~ pending
        #                 active_pattern = re.compile(r'\*(\S+)')
        #                 inactive_pattern = re.compile(r'\^(\S+)')
        #                 pending_pattern = re.compile(r'\~(\S+)')
                        
        #                 # The pattern for the last_run_seconds_ago collumn
        #                 last_run_pattern = re.compile(r'(\S+) sec\S+')

        #                 # The pattern for the rtt_stats_mseconds (for milliseconds) 
        #                 # The first pattern is for normal RTT denoted in milliseconds and therefore would not require any further processing
        #                 # The second pattern is for RTT denoted in microseconds and for standardisation purposes will be converted to milliseconds 
        #                 rtt_pattern_milliseconds = re.compile(r'RTT=(\d{1,4})')
        #                 rtt_pattern_microseconds = re.compile(r'RTT=(\d{1,4})u')

        #                 # Setting the probe_id and the codes values
        #                 if active_pattern.match(id):
        #                     probe_id = active_pattern.match(id).group(1)
        #                     id_dict['probe_status'] = 'active'
        #                 elif inactive_pattern.match(id):
        #                     probe_id = inactive_pattern.match(id).group(1)
        #                     id_dict['probe_status'] = 'inactive'
        #                 elif pending_pattern.match(id):
        #                     probe_id = pending_pattern.match(id).group(1)
        #                     id_dict['probe_status'] = 'pending'
        #                 del id_dict['id']

        #                 # Setting the rtt_stats_mseconds column value
        #                 # If the value is in milliseconds
        #                 if rtt_pattern_milliseconds.match(id_dict['rtt_stats_mseconds']):
        #                     id_dict['rtt_stats_mseconds'] = rtt_pattern_milliseconds.match(id_dict['rtt_stats_mseconds']).group(1)
        #                 # If the value is in microseconds
        #                 elif rtt_pattern_microseconds.match(id_dict['rtt_stats_mseconds']):
        #                     id_dict['rtt_stats_mseconds'] = int(rtt_pattern_microseconds.match(id_dict['rtt_stats_mseconds']).group(1))/1000
        #                 # If the value is a dash, no further processing is needed
        #                 else:
        #                     pass

        #                 # Setting the value for the last_run_seconds_ago collumn
        #                 if last_run_pattern.match(id_dict['last_run_seconds_ago']):
        #                     id_dict['last_run_seconds_ago'] = last_run_pattern.match(id_dict['last_run_seconds_ago']).group(1)
                        
                        
        #                 parsed_dict.setdefault('id',{}).update({probe_id: id_dict})
        #             else:
        #                 # This else clause is added to mitigate the limitation that sometimes the cli output line for this command
        #                 # may include just the letter 'o' as it would be cut from the Last Run column due to width limitation.
        #                 pass

        return parsed_dict

