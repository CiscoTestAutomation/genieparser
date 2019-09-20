"""show_ip_nat.py
    supported commands:
        * show ip nat translations
        * show ip nat translations verbose
        * show ip nat statistics
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowIpNatTranslationsSchema(MetaParser):
    """ Schema for the commands:
            * show ip nat translations
            * show ip nat translations verbose
    """

    schema = {
        'nat_translations': {
            'index': {
                Any(): {  # 1, 2 ,3, ...
                    'protocol': str,
                    Optional('inside_global'): str,
                    Optional('inside_local'): str,
                    Optional('outside_local'): str,
                    Optional('outside_global'): str,
                    Optional('details'): {
                        'create': str,
                        'use': str,
                        'timeout': str,
                        'map_id_in': int,
                        'mac_address': str,
                        'input_idb': str,
                        'entry_id': str,
                        'use_count': int
                    }
                }
            },
            Optional('number_of_translations'): int
        }
    }

class ShowIpNatTranslations(ShowIpNatTranslationsSchema):
    """
        * show ip nat translations
        * show ip nat translations verbose
    """

    cli_command = ['show ip nat translation', 'show ip nat translations verbose']

    def cli(self, option=None, output=None):
        
        if option:
            cmd = self.cli_command[1].format(option="verbose")
        
        if not option:
            cmd = self.cli_command[0]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # udp  10.5.5.1:1025          192.0.2.1:4000 --- ---
        # udp  10.5.5.1:1024          192.0.2.3:4000 --- ---
        # udp  10.5.5.1:1026          192.0.2.2:4000 --- ---
        # --- 171.69.233.209     192.168.1.95 --- ---
        # --- 171.69.233.210     192.168.1.89 --- ---
        # udp 171.69.233.209:1220  192.168.1.95:1220  171.69.2.132:53    171.69.2.132:53
        # tcp 171.69.233.209:11012 192.168.1.89:11012 171.69.1.220:23    171.69.1.220:23
        # tcp 171.69.233.209:1067  192.168.1.95:1067  171.69.1.161:23    171.69.1.161:23
        p1 = re.compile(r'^(?P<protocol>-+|udp|tcp) +(?P<inside_global>\S+) '
                         '+(?P<inside_local>\S+) +(?P<outside_local>\S+) +(?P<outside_global>\S+)$')

        # initialize variables
        ret_dict = {}
        index = 1

        for line in out.splitlines():
            line = line.strip()

            # udp  10.5.5.1:1025          192.0.2.1:4000 --- ---
            # udp  10.5.5.1:1024          192.0.2.3:4000 --- ---
            # udp  10.5.5.1:1026          192.0.2.2:4000 --- ---
            # --- 171.69.233.209     192.168.1.95 --- ---
            # --- 171.69.233.210     192.168.1.89 --- ---
            # udp 171.69.233.209:1220  192.168.1.95:1220  171.69.2.132:53    171.69.2.132:53
            # tcp 171.69.233.209:11012 192.168.1.89:11012 171.69.1.220:23    171.69.1.220:23
            # tcp 171.69.233.209:1067  192.168.1.95:1067  171.69.1.161:23    171.69.1.161:23
            m = p1.match(line)
            if m:
                group = m.groupdict()
                #import pdb;pdb.set_trace()
                protocol_dict = ret_dict.setdefault('nat_translations', {}).setdefault('index', {}).setdefault(index, {})
                protocol_dict.update({'protocol': group['protocol']})
                protocol_dict.update({'inside_global': group['inside_global']})
                protocol_dict.update({'inside_local': group['inside_local']})
                protocol_dict.update({'outside_global': group['outside_global']})
                protocol_dict.update({'outside_local': group['outside_local']})

                index += 1

                continue
            
        return ret_dict





