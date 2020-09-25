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
                        'IN Packet Count': int,
                        'OUT Packet Count': int,
                        'IN Byte Count': int,
                        'OUT Byte Count': int,
                        'IN 5min Bit Rate (bps)': int,
                        'OUT 5min Bit Rate (bps)': int,
                        'IN 5min Max Bit Rate (bps)': int,
                        'OUT 5min Max Bit Rate (bps)': int,
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
            #import pdb; pdb.set_trace()
            if line:
                line = line.strip()
                # print(line)
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface=group['interface']
                result_dict[interface]={}
                result_dict[interface]['protocol']={}
                continue
                
            
            m = p2.match(line)
            
            if m:
                group = m.groupdict()
                protocol=group['protocol']
                result_dict[interface]['protocol'][protocol]={}
                result_dict[interface]['protocol'][protocol].update({'IN Packet Count': int(group['In_Packet_Count'])})
                result_dict[interface]['protocol'][protocol].update({'OUT Packet Count': int(group['Out_Packet_Count'])})
                continue
            
            m = p3.match(line)
            
            if m:
                group = m.groupdict()
                result_dict[interface]['protocol'][protocol].update({'IN Byte Count': int(group['In_Byte_Count'])})
                result_dict[interface]['protocol'][protocol].update({'OUT Byte Count': int(group['Out_Byte_Count'])})
                
    
                   
            m = p4.match(line)
            
            if m:
                
                group = m.groupdict()
                result_dict[interface]['protocol'][protocol].update({'IN 5min Bit Rate (bps)': int(group['In_Bitrate'])})
                result_dict[interface]['protocol'][protocol].update({'OUT 5min Bit Rate (bps)': int(group['Out_Bitrate'])})
                
                
            
            m = p5.match(line)
            
            if m:
                group = m.groupdict()
                result_dict[interface]['protocol'][protocol].update({'IN 5min Max Bit Rate (bps)': int(group['In_Bitrate_Max'])})
                result_dict[interface]['protocol'][protocol].update({'OUT 5min Max Bit Rate (bps)': int(group['Out_Bitrate_Max'])})
                

        

        result_dict = {'interface': result_dict}  
        return result_dict