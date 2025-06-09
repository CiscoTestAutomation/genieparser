'''   show_prp_channel_detail.py

IOSXE parsers for the following show commands:

    * 'show prp channel detail'

'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowPrpChannelDetailsSchema(MetaParser):
    """ Schema for show prp channel detail """
    schema = {
        'prp_channel': {
            Any(): {
                'layer_type': str,
                'ports': str,
                'maxports': str,
                'port_state': str,
                'protocol': str,
                Any(): {
                    Optional('slot_port'): str,
                    Optional('port_state'): str,
                    Optional('protocol'): str,
                }
            }
        }
    }

class ShowPrpChannelDetails(ShowPrpChannelDetailsSchema):
    
    """ Parser for show prp channel detail
    """
    cli_command = ['show prp channel detail']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        parsed_dict = {}
        port_dict = {}
    
        # PRP-channel: PR1
        p1 = re.compile(r'PRP-channel:\s(?P<prp_channel_id>PR\d+)')

        # Layer type = L2 
        p2 = re.compile(r'Layer\s*type\s*=\s*(?P<prp_layer_type>\w+)')

        # Ports: 2	Maxports = 2
        p3 = re.compile(r'Ports:\s*(?P<prp_ports>\d+)\s*Maxports = (?P<prp_max_ports>\d+)')

        # Port state = prp-channel is Inuse
        p4 = re.compile(r'Port\s*state\s*=\s*prp-channel\s*is\s*(?P<prp_port_state>\w+)')

        # Logical slot/port = 1/1	Port state = Inuse 
        p5 = re.compile(r'Logical\s*[a-zA-z\/]+\s*=\s*(?P<prp_slot_port>[\d\/]+)*\s*Port\s*state\s*=\s*(?P<prp_port_state>\S+)')

        # Protocol = Enabled 
        p6 = re.compile(r'\s*Protocol\s*=\s*(?P<prp_protocol>\w+)')

        for line in out.splitlines():
            line = line.strip()
            
            # PRP-channel: PR1
            m = p1.match(line)

            if m:
                prpchannel_id = m.group('prp_channel_id')
                devices_dict = parsed_dict.setdefault('prp_channel', {}).setdefault(prpchannel_id, {})
                continue
            
            # Layer type = L2 
            m = p2.match(line)
            if m:
                devices_dict['layer_type'] = m.group('prp_layer_type')
                continue
            
            # Ports: 2	Maxports = 2
            m = p3.match(line)
            if m:
                devices_dict['ports'] = m.group('prp_ports')
                devices_dict['maxports'] = m.group('prp_max_ports')
                continue
            
            # Port state = prp-channel is Inuse
            m = p4.match(line)
            if m:
                devices_dict['port_state'] = m.group('prp_port_state')
                continue
            
            # Port:
            if 'Port:' in line:
                port = line.split(':')[-1].strip()
                port_dict = devices_dict.setdefault(port, {})
                continue
        
            # Logical slot/port = 1/1	Port state = Inuse 
            m = p5.match(line)
            if m:
                slot_port_state_dict = m.groupdict()
                if slot_port_state_dict:
                    port_dict['slot_port'] = slot_port_state_dict['prp_slot_port']
                    port_dict['port_state'] = slot_port_state_dict['prp_port_state']
                continue
            
            # Protocol = Enabled 
            m = p6.match(line)
            if m:
                if 'protocol' not in devices_dict.keys():
                    devices_dict['protocol'] = m.group('prp_protocol')
                else:
                    port_dict['protocol'] = m.group('prp_protocol')
                continue
            
        return parsed_dict