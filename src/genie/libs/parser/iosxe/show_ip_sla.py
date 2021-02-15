'''show_ip_sla.py
IOSXE parsers for the following show commands:
    * show ip sla summary
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ===============================
# Schema for 'show ip sla summary'
# ===============================
class ShowIpSlaSummarySchema(MetaParser):
    ''' Schema for "show ip sla summary" '''
    schema = {
        'ids': {
            Any(): {
                'state': str,
                'type': str,
                'destination': str,
                'rtt_stats': str,
                'return_code': str,
                'last_run': str,
            },
        }
    }


# ===============================
# Parser for 'show ip sla summary'
# ===============================
class ShowIpSlaSummary(ShowIpSlaSummarySchema):
    """Parser for:
    show ip sla summary
    """

    cli_command = 'show ip sla summary'

    def cli(self, output=None):
        
        parsed_dict = {}

        if output is None:
            out = self.device.execute(self.cli_command)
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
        
        p1 = re.compile(r'(?P<state_symbol>\*|\^|\~)*(?P<id>[\d]+) +'
        '(?P<type>[\w-]+) +(?P<destination>[\d.\:]+)\s*(?P<state_word>[\w]+)*'
        ' +(RTT=)*((?P<rtt_milliseconds>[\d]+)|(?P<rtt_na>-))'
        '(?P<is_microseconds>u)* +(?P<return_code>[\w]+) +'
        '(?P<last_run>[\w\: ]+)')

        p2 = re.compile(r'^ *(?P<extended_ip_address>[\d\:\.]+)')
        
        for line in out.splitlines():
            line = line.strip()

            #*1           tcp-connect 123.23.213.32     RTT=44      OK          21 seconds ago
            # 100   icmp-jitter   192.0.2.2    Active   100      OK       22:49:53 PST Tue May 3 2011
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id = group['id']
                id_dict = parsed_dict.setdefault('ids', {}).setdefault(id, {})
                
                # State can be a *, ^, or ~ at front of line, or can be a word
                if group['state_symbol'] == '*':
                    id_dict['state'] = 'active' 
                elif group['state_symbol'] == '^':
                    id_dict['state'] = 'inactive'
                elif group['state_symbol'] == '~':
                    id_dict['state'] = 'pending'
                else:
                    id_dict['state'] = group['state_word'].lower()
                
                id_dict['type'] = group['type']
                id_dict['destination'] = group['destination']

                # RTT Stats can be milliseconds, microseconds, or - (n/a)
                if group['rtt_na']:
                    id_dict['rtt_stats'] = '-'
                elif group['is_microseconds']:
                    rtt_in_microseconds = float(group['rtt_milliseconds'])\
                         / 1000
                    id_dict['rtt_stats'] = "{} microsecond(s)"\
                        .format(rtt_in_microseconds) 
                else:
                    rtt_in_milliseconds = group['rtt_milliseconds']
                    id_dict['rtt_stats'] = "{} millisecond(s)"\
                        .format(rtt_in_milliseconds)


                id_dict['return_code'] = group['return_code']
                id_dict['last_run'] = group['last_run']

                continue


            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict['destination'] += group['extended_ip_address']
                continue


        return parsed_dict
