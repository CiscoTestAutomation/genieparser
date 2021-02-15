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
            All(){
                'id': str,
                'probe_status': str, #Codes: * active, ^ inactive, ~ pending
                'type': str,
                'destination': str,
                'rtt_stats': str,
                'return_code': str,
                'last_run_seconds_ago': int,
            },
        },
    }


class ShowIpSlaSummary(ShowIpSlaSummarySchema):
    """Parser for:
    show ip sla summary
    """

    def cli(self):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which consists of the 3 steps:
        execution, transforming, returning
        """

        parsed_dict = {}
        cli_command = 'show ip sla summary'
        
        out = self.device.execute(cmd)

        #ID           Type        Destination       Stats       ReturnCOde     LastRun
        #-----------------------------------------------------------------------------
        #*1           tcp-connect 123.23.213.32     RTT=44      OK             21 seconds ago                                                                              
        #*2           dns         11.121.2.123      -           Timeout        7 seconds ago

        if out:
            headers = [['ID','Type','Destination','Stats','Return','Last'],['','','','','Code','Run']]
            result = parsergen.oper_fill_tabular(device_output = out, header_fields=headers, label_fields = ['id','type','destination','rtt_stats_mseconds','return_code','last_run_seconds_ago'])
            struct_output = result.entries
            if struct_output:
                for id, id_dict in struct_output.items():
                    if id:
                        # Defining patterns to be matched for different columns
                        # The patterns for the state of the ip sla probe defined by the Codes: * active, ^ inactive, ~ pending
                        active_pattern = re.compile(r'\*(\S+)')
                        inactive_pattern = re.compile(r'\^(\S+)')
                        pending_pattern = re.compile(r'\~(\S+)')
                        
                        # The pattern for the last_run_seconds_ago collumn
                        last_run_pattern = re.compile(r'(\S+) sec\S+')

                        # The pattern for the rtt_stats_mseconds (for milliseconds) 
                        # The first pattern is for normal RTT denoted in milliseconds and therefore would not require any further processing
                        # The second pattern is for RTT denoted in microseconds and for standardisation purposes will be converted to milliseconds 
                        rtt_pattern_milliseconds = re.compile(r'RTT=(\d{1,4})')
                        rtt_pattern_microseconds = re.compile(r'RTT=(\d{1,4})u')

                        # Setting the probe_id and the codes values
                        if active_pattern.match(id):
                            probe_id = active_pattern.match(id).group(1)
                            id_dict['probe_status'] = 'active'
                        elif inactive_pattern.match(id):
                            probe_id = inactive_pattern.match(id).group(1)
                            id_dict['probe_status'] = 'inactive'
                        elif pending_pattern.match(id):
                            probe_id = pending_pattern.match(id).group(1)
                            id_dict['probe_status'] = 'pending'
                        del id_dict['id']

                        # Setting the rtt_stats_mseconds column value
                        # If the value is in milliseconds
                        if rtt_pattern_milliseconds.match(id_dict['rtt_stats_mseconds']):
                            id_dict['rtt_stats_mseconds'] = rtt_pattern_milliseconds.match(id_dict['rtt_stats_mseconds']).group(1)
                        # If the value is in microseconds
                        elif rtt_pattern_microseconds.match(id_dict['rtt_stats_mseconds']):
                            id_dict['rtt_stats_mseconds'] = int(rtt_pattern_microseconds.match(id_dict['rtt_stats_mseconds']).group(1))/1000
                        # If the value is a dash, no further processing is needed
                        else:
                            pass

                        # Setting the value for the last_run_seconds_ago collumn
                        if last_run_pattern.match(id_dict['last_run_seconds_ago']):
                            id_dict['last_run_seconds_ago'] = last_run_pattern.match(id_dict['last_run_seconds_ago']).group(1)
                        
                        
                        parsed_dict.setdefault('id',{}).update({probe_id: id_dict})
                    else:
                        # This else clause is added to mitigate the limitation that sometimes the cli output line for this command
                        # may include just the letter 'o' as it would be cut from the Last Run column due to width limitation.
                        pass

        return parsed_dict

