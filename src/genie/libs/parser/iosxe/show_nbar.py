# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# ======================================================
# Schema for 'show ip nbar protocol-discovery protocol'
# ======================================================

class ShowIpNbarDiscoverySchema(MetaParser):
    schema = {
        'interface': {
            Any(): {
                'protocol': {
                    Any(): {
                        'in_packet_count': int,
                        'out_packet_count': int,
                        'in_byte_count': int,
                        'out_byte_count': int,
                        'in_5min_bit_rate_bps': int,
                        'out_5min_bit_rate_bps': int,
                        'in_5min_max_bit_rate_bps': int,
                        'out_5min_max_bit_rate_bps': int,
                    }
                }
            }
        }
    }

class ShowIpNbarDiscovery(ShowIpNbarDiscoverySchema):
    """Parser for show ip nbar protocol-discovery protocol on IOS-XE
    parser class - implements detail parsing mechanisms for cli output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = 'show ip nbar protocol-discovery protocol'

    
    def cli(self, output=None):
        """parsing mechanism: cli
        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
            
        result_dict = {}
        p1 = re.compile(r'^(?P<interface>Gig.+|Ten.+|Fast.+ |Port.+)')
        p2 = re.compile(r'^(?P<protocol>[\w\-]+) +(?P<In_Packet_Count>[\d]+) +(?P<Out_Packet_Count>[\d]+)')
        p3 = re.compile(r'^(?P<In_Byte_Count>[\d]+) +(?P<Out_Byte_Count>[\d]+)')
        p4 = re.compile(r'^(?P<In_Bitrate>[\d]+) +(?P<Out_Bitrate>[\d]+)')
        p5 = re.compile(r'^(?P<In_Bitrate_Max>[\d]+) +(?P<Out_Bitrate_Max>[\d]+)')

        

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interfaces = result_dict.setdefault('interface', {})
                interface = interfaces.setdefault(group['interface'], {})
                interface['protocol']={}
                continue
                
            
            m = p2.match(line)
            
            if m:
                group = m.groupdict()
                protocol=group['protocol']
                interface['protocol'][protocol]={}
                interface['protocol'][protocol].update({'in_packet_count': int(group['In_Packet_Count'])})
                interface['protocol'][protocol].update({'out_packet_count': int(group['Out_Packet_Count'])})
                continue
            
            m = p3.match(line)
            
            if m:
                group = m.groupdict()
                interface['protocol'][protocol].update({'in_byte_count': int(group['In_Byte_Count'])})
                interface['protocol'][protocol].update({'out_byte_count': int(group['Out_Byte_Count'])})
                
    
                   
            m = p4.match(line)
            
            if m:
                
                group = m.groupdict()
                interface['protocol'][protocol].update({'in_5min_bit_rate_bps': int(group['In_Bitrate'])})
                interface['protocol'][protocol].update({'out_5min_bit_rate_bps': int(group['Out_Bitrate'])})
                
                
            
            m = p5.match(line)
            
            if m:
                group = m.groupdict()
                interface['protocol'][protocol].update({'in_5min_max_bit_rate_bps': int(group['In_Bitrate_Max'])})
                interface['protocol'][protocol].update({'out_5min_max_bit_rate_bps': int(group['Out_Bitrate_Max'])})
                

        

        return result_dict
