"""  show_mfib.py
   supported commands:
        *  show ip mfib vrf <vrf> summary
        *  show ip mfib vrf <vrf> active | c HW Rate
        *  show ip mfib vrf <vrf> active
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowIpMfibVrfSummarySchema(MetaParser):
    """Schema for:
        show ip mfib vrf {vrf} summary
    """
    schema = {
        'vrf': {
            Any():{
                'prefixes':{
                    'total':int,
                    'fwd':int,
                    'non_fwd':int,
                    'deleted':int
                },
                'ioitems':{
                    'total':int,
                    'fwd':int,
                    'non_fwd':int,
                    'deleted':int
                },
                'forwarding_prefixes':{
                    's_g':int,
                    'g':int,
                    'g_m':int
                },
                'table_id':str,
                'instance':str,
                'database':str
            },
        }
    }
    
class ShowIpMfibVrfSummary(ShowIpMfibVrfSummarySchema):
    """Parser for show ip mfib vrf {vrf} summary parameters"""

    cli_command = 'show ip mfib vrf {vrf} summary'

    def cli(self, vrf, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            out = output

        # initial return dictionary
        result_dict = {}
    
        ##VRF vrf3001
        p1=re.compile(r"^VRF (\S+)$")
        
        ##49 prefixes (49/0/0 fwd/non-fwd/deleted)
        ##98 ioitems (98/0/0 fwd/non-fwd/deleted)
        p2=re.compile(r"^(?P<total>\d+)\s+(?P<field>\S+) \((?P<fwd>\d+)\/(?P<non_fwd>\d+)\/(?P<deleted>\d+).*$")
        
        ##Forwarding prefixes: [20 (S,G), 27 (*,G), 2 (*,G/m)]
        p3=re.compile(r"^Forwarding prefixes:\s+\[(?P<s_g>\d+)[ \(A-z\,\)]+\,\s+(?P<g>\d+)[ \(\*\,A-Z\)]+\,\s+(?P<g_m>\d+).*$")
        
        ##Table id 0xB, instance 0x7FC5BE77F480
        p4=re.compile(r"^Table id (?P<table_id>\S+)\,\s+instance\s+(?P<instance>\S+)$")
        
        ##Database: epoch 0
        p5=re.compile(r"Database: ([a-z0-9 ]+)")
        
        for line in out.splitlines():
            line=line.strip()
            
            ##VRF vrf3001
            m=p1.match(line)
            if m:
               prefix_dict=result_dict.setdefault('vrf',{}).setdefault(m.groups()[0],{}) 
               continue
               
            ##49 prefixes (49/0/0 fwd/non-fwd/deleted)
            ##98 ioitems (98/0/0 fwd/non-fwd/deleted)
            m=p2.match(line)
            if m:
                r=m.groupdict()
                dict2=prefix_dict.setdefault(r['field'],{})
                r.pop('field')
                for key,value in r.items():
                    dict2.update({key:int(value)})
                continue
                
            ##Forwarding prefixes: [20 (S,G), 27 (*,G), 2 (*,G/m)]
            m=p3.match(line)
            if m:
                r=m.groupdict()
                dict3=prefix_dict.setdefault('forwarding_prefixes',{})
                for key,value in r.items():
                    dict3.update({key:int(value)})
                continue
                
            ##Table id 0xB, instance 0x7FC5BE77F480
            m=p4.match(line)
            if m:
                r=m.groupdict()
                for key,value in r.items():
                    prefix_dict.update({key:value})    
                continue
                
            ##Database: epoch 0
            m=p5.match(line)
            if m:
                prefix_dict.update({'database':m.groups()[0]}) 
                continue
        return result_dict
        
class ShowIpMfibVrfActiveHwRateSchema(MetaParser):
    """Schema for:
        show ip mfib vrf <vrf> active | c HW Rate
    """
    schema = {
        'mfib_group_count': {
            'matched_line':int
        }
    }
    
class ShowIpMfibVrfActiveHwRate(ShowIpMfibVrfActiveHwRateSchema):
    """Parser for show ip mfib vrf <vrf> active | c HW Rate"""

    cli_command = 'show ip mfib vrf {vrf} active | c HW Rate'

    def cli(self, vrf, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            out = output

        ret_dict={}

        # initial return dictionary        
        if not out.strip():
            return ret_dict
            
        out=out.strip()
        if out:
            ret_dict['mfib_group_count']={}
            ret_dict['mfib_group_count']['matched_line']=int(out.split("=")[1])
                
        return ret_dict
        
class ShowIpMfibVrfActiveSchema(MetaParser):
    """Schema for:
        show ip mfib vrf <vrf> active
    """
    schema = {
        'vrf': {
            Any():{
                'groups':{
                    Any():{
                        'source':str,
                        'sw_rate_details':{
                            'sw_rate_utilized':int,
                            'utilised_speed_type':str,
                            'max_sw_rate':int,
                            'max_sw_speed_type':str,
                            'duration':str,
                        },
                        'hw_rate_details':{
                            'hw_rate_utilized':int,
                            'utilised_speed_type':str,
                            'max_hw_rate':int,
                            'max_hw_speed_type':str,
                        },
                    },
                },
            },
        }
    }
    
class ShowIpMfibVrfActive(ShowIpMfibVrfActiveSchema):
    """Parser for show ip mfib vrf <vrf> active"""

    cli_command = 'show ip mfib vrf {vrf} active'

    def cli(self, vrf, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        
        if not out.strip():
            return result_dict
    
        ##VRF vrf3001
        p1=re.compile(r"^VRF (\S+)$")
        
        ##Group: 228.1.1.1
        p2=re.compile(r"^Group:\s+(\S+)$")
        
        ##Source: 161.1.1.2,
        ##RP-tree,
        p3=re.compile(r"(?:Source: +)?(\S+)\,$")
        
        ##SW Rate: 100 pps/0 kbps(1sec), 0 kbps(last 210 sec)
        p4=re.compile(r"^SW Rate: +(?P<sw_rate_utilized>\d+) +(?P<utilised_speed_type>\S+)\/"
                      r"(?P<max_sw_rate>\d+) +(?P<max_sw_speed_type>\S+)\(.*\(last +(?P<duration>.*)\)$")
                      
        ##HW Rate: 2000 pps/7750 kbps(1sec)
        p5=re.compile(r"^HW Rate: +(?P<hw_rate_utilized>\d+) +(?P<utilised_speed_type>\S+)\/"
                    r"(?P<max_hw_rate>\d+) +(?P<max_hw_speed_type>\S+)\(.*$")

        for line in out.splitlines():
            line = line.strip()
            
            ##VRF vrf3001
            m=p1.match(line)
            if m:
                main_dict=result_dict.setdefault("vrf",{}).setdefault(m.groups()[0],{})
                continue
                
            ##Group: 228.1.1.1
            m=p2.match(line)
            if m:
                group_dict=main_dict.setdefault('groups',{}).setdefault(m.groups()[0],{})
                continue
                
            ##Source: 161.1.1.2,
            m=p3.match(line)
            if m:
                group_dict['source']=m.groups()[0]
                continue
                
            ##SW Rate: 100 pps/0 kbps(1sec), 0 kbps(last 210 sec)
            m=p4.match(line)
            if m:
                r=m.groupdict()
                sw_details=group_dict.setdefault("sw_rate_details",{})
                for key,value in r.items():
                    sw_details[key]=int(value) if value.isdigit() else value.strip()
                continue
                
            ##HW Rate: 2000 pps/7750 kbps(1sec)
            m=p5.match(line)
            if m:
                r=m.groupdict()
                hw_details=group_dict.setdefault("hw_rate_details",{})
                for key,value in r.items():
                    hw_details[key]=int(value) if value.isdigit() else value.strip()
                continue
                
        return result_dict

        
