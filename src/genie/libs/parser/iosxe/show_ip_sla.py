"""
    show_ip_sla.py
    IOSXE parsers for the following show commands:

    * show ip sla summary
"""



from genie import parsergen
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
from genie.metaparser.util.schemaengine import Schema

# ==============================
# Schema for 'show ip sla summary'
# ==============================

class ShowIpSlaSummarySchema(MetaParser):
    ''' Schema for "show ip sla summary" '''
    schema ={'probes':
    {Any(): 
    {
        Optional('id'): str,
        Optional('type'): str,
        Optional('destination'): str,
        Optional('rtt_stats'): str,
        Optional('return_code'): str,
        Optional('last_run'): str
    },
    },
    }


class ShowIpSlaSummary(ShowIpSlaSummarySchema):
    """Parser for:
    show ip sla summary
    parser class implements detail parsing mechanisms for cli.
    """

    # schema - class variable
    #
    # Purpose is to make sure the parser always return the ouput 
    # (nested dict) that has the same data structure across all supported parsing mechanisms

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def cli(self):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which consists of the 3 steps:
        execution, transforming, returning
        """

        parsed_dict = {}
        cmd = 'show ip sla summary'
        
        out = self.device.execute(cmd)

        #ID           Type        Destination       Stats       Return      Last
        #                                                       Code        Run 
        #-----------------------------------------------------------------------
        #*1           tcp-connect 123.23.213.32     RTT=44      OK          21 seconds ag
        #                                                                   o            
        #                                                                                
        #                                                                                
        #                                                                                
        #*2           dns         11.121.2.123      -           Timeout     7 seconds ago

        if out:
            headers = [['ID','Type','Destination','Stats','Return','Last'],['','','','','Code','Run']]
            result = parsergen.oper_fill_tabular(device_output = out, header_fields=headers, label_fields = ['id','type','destination','rtt_stats','return_code','last_run'])
            struct_output = result.entries
            if struct_output:
                for id, id_dict in struct_output.items():
                    if id:
                        probe_id = id.split('*')[1]
                        del id_dict['id']
                        rtt = id_dict['rtt_stats']
                        if 'ago' not in id_dict['last_run']:
                            id_dict['last_run'] = id_dict['last_run'] + 'o'
                        if 'RTT=' in rtt:
                            rtt_updated = rtt.split('RTT=')[1]
                            id_dict['rtt_stats'] = rtt_updated
                        else:
                            pass
                        parsed_dict.setdefault('probes',{}).update({probe_id: id_dict})
                    else:
                        # This else clause is added to mitigate the limitation that sometimes the cli output line for this command
                        # may include just the letter 'o' as it would be cut from the Last Run column due to width limitation.
                        pass

        return parsed_dict

