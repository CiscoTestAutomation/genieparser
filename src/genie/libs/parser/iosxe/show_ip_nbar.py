"""show_ip_nbar.py
    supported commands:
        * show ip nbar classification socket-cache <number_of_sockets>
        
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema,
                                                Any,
                                                Optional,
                                                Or,
                                                And,
                                                Default,
                                                Use)

# import parser utils
from genie.libs.parser.utils.common import Common



class ShowIpNbarClassificationSocketSchema(MetaParser):
    """ Schema for the commands:
            * show ip nbar classification socket-cache <number_of_sockets>
    """

    schema = {
        'flow_cache': {
            Any():{
                'server_ip': str,
                'vrf': int,
                'port': int,
                'proto': str,
                'app_name': str,
                'is_valid': str,
                'is_black_list': str,
                'is_learn_ph': str,
                'expiry_time': int,
                'entry_type': str,
                'hit_count': int
            }
        }
    }


class ShowIpNbarClassificationSocket(ShowIpNbarClassificationSocketSchema):
    """
        * show ip nbar classification socket-cache <number_of_sockets>
    """

    cli_command = ['show ip nbar classification socket-cache {number_of_sockets}']
                  
    def cli(self, number_of_sockets=None, output=None):
        if output is None:
            cmd = self.cli_command[0].format(number_of_sockets=number_of_sockets)
            out = self.device.execute(cmd)
        else:
            out = output
        
        # |10.169.188.209                          |    2|  443|TCP  |ssl                    |No   |No   |Yes  |633      |Infra|1      |
        p1 = re.compile(r'^\|(?P<server_ip>\S+)[\s|]+(?P<vrf>\d+)[\s|]+(?P<port>\d+)\|(?P<proto>\S+)[\s|]+(?P<app_name>\S+)[\s|]+(?P<is_valid>\w+)[\s|]+(?P<is_black_list>\w+)[\s|]+(?P<is_learn_ph>\w+)[\s|]+(?P<expiry_time>\d+)[\s|]+(?P<entry_type>\w+)\|(?P<hit_count>\d+)[\s|]+$')
       
        ret_dict = {}
        first_line = 1
        sess_num = 1 
        for line in out.splitlines():
            line = line.strip()
            
            #zbfw zonepair-statistics ZP_lanZone_lanZone_Is_-902685811
            m = p1.match(line)      
            if m:
                groups = m.groupdict()
                if(first_line == 1):
                    first_line = first_line + 1
                    sess_dict = ret_dict.setdefault('flow_cache',{})
                
                feature_dict = sess_dict.setdefault(sess_num, {})
                feature_dict.update({'server_ip': groups['server_ip']})
                feature_dict.update({'vrf': int(groups['vrf'])})
                feature_dict.update({'port': int(groups['port'])})
                feature_dict.update({'proto': groups['proto']})
                feature_dict.update({'app_name': groups['app_name']})
                feature_dict.update({'is_valid': groups['is_valid']})
                feature_dict.update({'is_black_list': groups['is_black_list']})
                feature_dict.update({'is_learn_ph': groups['is_learn_ph']})
                feature_dict.update({'expiry_time': int(groups['expiry_time'])})
                feature_dict.update({'entry_type': groups['entry_type']})
                feature_dict.update({'hit_count': int(groups['hit_count'])})
                sess_num = sess_num + 1

        
        return(ret_dict)


