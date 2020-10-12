""" show_dampening.py
    supports commands:
        * show im dampening
        * show im dampening {interface}
"""

# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =============================================
# Parser for 'show im dampening'
# =============================================

class ShowImDampeningSchema(MetaParser):
    schema = {
                'interface': {
                    Any(): {
                    'protocol': {
                        Any(): {
                        'capsulation': str,
                        'penalty': int,
                        'suppressed': str,
                        }
                    }
                }
            }
        }
                    
class ShowImDampening(ShowImDampeningSchema):
    """ Parser for show im dampening"""
    
    cli_command = 'show im dampening'

    def cli(self,output=None):
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
        result_dict.setdefault('interface', {})
        
        # GigabitEthernet0/0/0/1                                               2389 YES
        # POS0/2/0/0                  <base>             ppp                      0 NO 
        p1 = re.compile(r'^(?P<interface>.{1,26}) +(?P<prot>.{1,20}) +(?P<cap>.{1,10}) +(?P<pen>\d+) +(?P<sup>YES|NO)')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue
            
            m = p1.match(line)
            
            if m:
                group = m.groupdict()
                interface=group['interface'].rstrip()
                
                # set "not_present" on any empty fields
                for empty in group.keys():
                    if group.get(empty).startswith(' '):
                        group[empty]="not_present"
                protocol=group['prot'].rstrip()
                
                if result_dict['interface'].get(interface)==None:
                    result_dict['interface'][interface]={}
                    result_dict['interface'][interface]['protocol']={}
                result_dict['interface'][interface]['protocol'][protocol]={}
                result_dict['interface'][interface]['protocol'][protocol].update({'capsulation': group['cap']})  
                result_dict['interface'][interface]['protocol'][protocol].update({'penalty': int(group['pen'])})
                result_dict['interface'][interface]['protocol'][protocol].update({'suppressed': group['sup'].lower()})                                     
                continue
        return result_dict

class ShowImDampeningIntfSchema(MetaParser):
    schema = {
        'interface': {
            Any(): {
            'dampening_status': str,    
            Optional('currently_suppressed'): str,
            Optional('half_life'): int,
            Optional('max_supress_time'): int,
            Optional('penalty'): int,
            Optional('reuse'): int,
            Optional('suppress'): int,
            Optional('suppressed_secs_remaining'): int,
            Optional('underlying_state'): str,
            Optional('protocol'): 
                     {Any():
                        {Optional('protocol_capsulation'): str, 
                        Optional('protocol_penalty'): int,
                        Optional('protocol_suppression'): str,
                        Optional('protocol_suppression_timer'): int,
                        Optional('protocol_underlying_state'): str,
                      },
                   },
                }
        }
    }
    
class ShowImDampeningIntf(ShowImDampeningIntfSchema):
    """ Parser for show im dampening interface {interface} """
    
    cli_command = ['show im dampening interface {interface}']
    
    def cli(self, interface=None, output=None):
        """parsing mechanism: cli
        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[1].format(
                                          interface=interface))
        else:
            out = output
        
        result_dict = {}
        result_dict.setdefault('interface', {})
        
        # TenGigE 0/1/0/0 (0x01180020)
        # GigabitEthernet0/2/0/0 (0x080002c0)
        p1 = re.compile(r'^(?P<interface>[a-zA-Z].+[\/\d]+) \(')
        
        # Dampening enabled: Penalty 1625, SUPPRESSED (42 secs remaining)
        p2 = re.compile(r'Dampening\s(?P<stat>\w+): +Penalty\s(?P<pen>\d+), +SUPPRESSED\s\((?P<sup>\d+)')
        
        # Dampening enabled: Penalty 0, not suppressed
        p3 = re.compile(r'Dampening\s(?P<stat_ns>\w+): +Penalty\s(?P<pen_ns>\d+), +not\ssupp.+')
        
        # underlying-state:  Up
        # Underlying state: Down
        p4 = re.compile(r'^[a-z-A-Z\s]+state:\s+(?P<und_stat>\S+)')
        
        #  half-life: 1        reuse:             1000 
        p5 = re.compile(r'half-life:\s+(?P<half_life>\d+) +reuse:\s+(?P<reuse>\d+)')
        
        # suppress:  1500     max-suppress-time: 4 
        p6 = re.compile(r'suppress:\s+(?P<suppress>\d+) +max-suppress-time:\s(?P<max_suppress>\d+)')
        
        # ipv6           ipv6               1625  YES    42s  remaining        Down
        p7 = re.compile(r'^(?P<prot>[a-z\d<>].{1,12}) +(?P<prot_cap>[a-z\d<>].{1,12}) +(?P<prot_pen>\d+) +(?P<prot_sup>YES|NO) +(?P<prot_sup_time>\d+). +remaining\s+(?P<prot_state>\S+)')
        
        p8 = re.compile(r'^(?P<stat>Dampening not enabled)')
        
        for line in out.splitlines():
    
            if line:
                line = line.strip()

            else:
                continue

            m = p1.match(line)
            
            if m:
                group = m.groupdict()
                interface=group['interface']
                if result_dict['interface'].get(interface)==None:
                    result_dict['interface'][interface]={}
                    
                    
            m = p2.match(line)
            
            if m:
                group = m.groupdict()
                result_dict['interface'][interface].update({'dampening_status': group['stat'].lower()})
                result_dict['interface'][interface].update({'penalty': int(group['pen'])})
                result_dict['interface'][interface].update({'suppressed_secs_remaining': int(group['sup'])})
                result_dict['interface'][interface].update({'currently_suppressed': 'yes'})
                
            m = p3.match(line)
            
            if m:
                group = m.groupdict()
                result_dict['interface'][interface].update({'dampening_status': group['stat_ns'].lower()})
                result_dict['interface'][interface].update({'penalty': int(group['pen_ns'])})
                result_dict['interface'][interface].update({'currently_suppressed': 'no'})
            
            m = p4.match(line)

            if m:
                group = m.groupdict()
                result_dict['interface'][interface].update({'underlying_state': group['und_stat'].lower()})

            m = p5.match(line)

            if m:
                group = m.groupdict()
                result_dict['interface'][interface].update({'half_life': int(group['half_life'])})
                result_dict['interface'][interface].update({'reuse': int(group['reuse'])})

            m = p6.match(line)

            if m:
                group = m.groupdict()
                result_dict['interface'][interface].update({'suppress': int(group['suppress'])})
                result_dict['interface'][interface].update({'max_supress_time': int(group['max_suppress'])})
                     
            m = p7.match(line)
            
            if m:
                group = m.groupdict()
                if result_dict['interface'][interface].get('protocol')==None:
                    result_dict['interface'][interface]['protocol']={}
                protocol=group['prot'].rstrip()
                if result_dict['interface'][interface]['protocol'].get(protocol)==None:
                    result_dict['interface'][interface]['protocol'][protocol]={}
                result_dict['interface'][interface]['protocol'][protocol].update({'protocol_capsulation': group['prot_cap'].rstrip()})
                result_dict['interface'][interface]['protocol'][protocol].update({'protocol_penalty': int(group['prot_pen'])})
                result_dict['interface'][interface]['protocol'][protocol].update({'protocol_suppression': group['prot_sup'].lower()})
                result_dict['interface'][interface]['protocol'][protocol].update({'protocol_suppression_timer': int(group['prot_sup_time'])})                       
                result_dict['interface'][interface]['protocol'][protocol].update({'protocol_underlying_state': group['prot_state'].lower()})
            
            m = p8.match(line)
            
            if m:
                group = m.groupdict()
                result_dict['interface'][interface]={}
                result_dict['interface'][interface].update({'dampening_status': 'dampening_not_enabled'})
                result_dict['interface'][interface].update({})
 
                
            
        return result_dict    
                  