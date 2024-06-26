# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, ListOf


# ==================================================
# Schema for 'show pool {address_family} name {pool_name}'
# ==================================================
class ShowPoolAddressFamilyPoolSchema(MetaParser):
    """Schema for show pool {address_family} name {pool_name}"""

    schema = {
        'pool_name' : {
            Any() : {
                'vrf' : {
                    Any() : {
                        'pool_id' : int,
                        'pool_scope' : str,
                        'prefix_length': str,
                        'utilization': {
                            Optional('used'): int,
                            Optional('excl'): int,
                            Optional('free'): int,
                            Optional('total'): int,
                            'utilization': str,
                        },
                        'range_list': {
                            'range_start': str,
                            'range_end': str,
                            Optional('default_router'): str,
                            Optional('used_address'): str,
                            Optional('excluded_address'): str,
                            Optional('free_address'): str,
                        }
                    }
                }
            }
        }
    }

# ========================================================
# Parser for 'show pool {address_family} name {pool_name}'
# ========================================================
class ShowPoolAddressFamilyPool(ShowPoolAddressFamilyPoolSchema):
    """Parser for show pool {address_family} name {pool_name}"""
    
    cli_command = 'show pool {address_family} name {pool_name}'
    def cli(self, address_family='', pool_name='', output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(address_family=address_family,pool_name=pool_name))

        ret_dict = {} 
        
        #  Pool CATL_POOL Allocations
        p1 = re.compile(r'^(Pool\s+(?P<pool_name>\S+)\s+Allocations)$')
        
        # VRF: default
        p2 = re.compile(r'^VRF:\s+(?P<vrf_name>\w+)$')
        
        # Pool Id: 0
        p3 = re.compile(r'^Pool\s+Id:\s+(?P<pool_id>\d+)$')
        
        # Pool Scope: VRF Specific Pool
        p4 = re.compile(r'^Pool\s+Scope:\s+(?P<pool_scope>\w+\s+\w+\s+\w+)$')
        
        # Prefix Length: 32
        p5 = re.compile(r'^Prefix\s+Length:\s+(?P<prefix_length>\d+)$')
        
        # Used:             0
        p6 = re.compile(r'^Used:\s+(?P<used>\d+)$')
        
        # Excl:             0
        p7 = re.compile(r'^Excl:\s+(?P<excl>\d+)$')
        
        # Free:           253
        p8 = re.compile(r'^Free:\s+(?P<free>\d+)$')
        
        # Total:          253
        p9 = re.compile(r'^Total:\s+(?P<total>\d+)$')
        
        # Utilization:    0%
        p10 = re.compile(r'^Utilization:\s+(?P<utilization>\S+)$')
        
        # Range Start        :  192.168.1.2
        p11 = re.compile(r'^Range\s+Start\s+:\s+(?P<range_start>\S+)$')
        
        # Range End          :  192.168.1.254 
        p12 = re.compile(r'^Range\s+End\s+:\s+(?P<range_end>\S+)$')
        
        # Default Router     :  0.0.0.0 
        p13 = re.compile(r'^Default\s+Router\s+:\s+(?P<default_router>\S+)$')
        
        # Used Addresses     :  0
        p14 = re.compile(r'^Used\s+Addresses\s+:\s+(?P<used_address>\S+)$')
        
        # Excluded Addresses :  0 
        p15 = re.compile(r'^Excluded\s+Addresses\s+:\s+(?P<excluded_address>\S+)$')
        
        # Free Addresses     :  253
        p16 = re.compile(r'^Free\s+Addresses\s+:\s+(?P<free_address>\S+)$')
        
        for line in output.splitlines():
            line = line.strip()
            
            #  Pool CATL_POOL Allocations
            m = p1.match(line)
            if m:
                group = m.groupdict()
                pool_name = group['pool_name']
                pool_dict = ret_dict.setdefault('pool_name', {}).setdefault(pool_name, {})
                continue
            
            # VRF: default    
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf_name']
                vrf_dict = pool_dict.setdefault('vrf', {}).setdefault(vrf, {})
                continue
            
            # Pool Id: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['pool_id'] = int(group['pool_id'])
                continue
            
            # Pool Scope: VRF Specific Pool
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['pool_scope'] = group['pool_scope']
                continue
            
            # Prefix Length: 32
            m = p5.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['prefix_length'] = group['prefix_length']
                continue
            
            # Used:             0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                #utilization = group['utilization']
                ut_dict = vrf_dict.setdefault('utilization', {})
                ut_dict ['used'] = int(group['used'])
                continue
            
            # Excl:             0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ut_dict ['excl'] = int(group['excl'])
                continue
            
            # Free:           253
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ut_dict ['free'] = int(group['free'])
                continue
            
            # Total:          253
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ut_dict ['total'] = int(group['total'])
                continue
            
            # Utilization:    0%
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ut_dict ['utilization'] = group['utilization']
                continue
            
            # Range Start        :  192.168.1.2
            m = p11.match(line)
            if m:
                group = m.groupdict()
                range_dict = vrf_dict.setdefault('range_list', {})
                range_dict ['range_start'] = group['range_start']
                continue
            
            # Range End          :  192.168.1.254 
            m = p12.match(line)
            if m:
                group = m.groupdict()
                range_dict ['range_end'] = group['range_end']
                continue
            
            # Default Router     :  0.0.0.0 
            m = p13.match(line)
            if m:
                group = m.groupdict()
                range_dict ['default_router'] = group['default_router']
                continue
            
            # Used Addresses     :  0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                range_dict ['used_address'] = group['used_address']
                continue
            
            # Excluded Addresses :  0 
            m = p15.match(line)
            if m:
                group = m.groupdict()
                range_dict ['excluded_address'] = group['excluded_address']
                continue
            
            # Free Addresses     :  253
            m = p16.match(line)
            if m:
                group = m.groupdict()
                range_dict ['free_address'] = group['free_address']
                continue
            
        return ret_dict
                
