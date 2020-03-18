''' show_ip.py

Parser for the following show commands:
    * show ip local pool {pool}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema, 
                                                Any,
                                                Optional)

# =============================================
# Schema for 'show ip local pool {pool}'
# =============================================
class ShowIpLocalPoolSchema(MetaParser):
    """Schema for
        * show ip local pool {pool}
    """

    schema = {
        'pool': {
            str: {
                'available_addresses': list,
                'in_use_addresses': list,
                'begin': str,
                'end': str,
                'free': int,
                'held': int,
                'in_use': int,
                'mask': str,
            }
        }
    }

# =============================================
# Parser for 'show ip local pool {pool}'
# =============================================
class ShowIpLocalPool(ShowIpLocalPoolSchema):
    """Parser for
        * show ip local pool {pool}
    """

    cli_command = 'show ip local pool {pool}'

    def cli(self, pool, output=None):
        if output is None:
            # execute command to get output
            cmd = self.cli_command.format(pool=pool)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        address_type = None

        # 192.168.1.144   192.168.1.147   255.255.255.252     2        0        2
        p1 = re.compile(r'^(?P<begin>\S+) +(?P<end>\S+) +'
                        r'(?P<mask>\S+) +(?P<free>\d+) +'
                        r'(?P<held>\d+) +(?P<in_use>\d+)$')

        # Available Addresses:
        p2 = re.compile(r'^Available +Addresses:$')

        # In Use Addresses:
        p3 = re.compile(r'^In +Use +Addresses:$')

        # 192.168.1.145
        p4 = re.compile(r'^(?P<ip_address>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # 192.168.1.144   192.168.1.147   255.255.255.252     2        0        2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                pool_dict = ret_dict.setdefault('pool', {}). \
                    setdefault(pool, {})
                pool_dict.update({'begin': group['mask']})
                pool_dict.update({'end': group['mask']})
                pool_dict.update({'mask': group['mask']})
                pool_dict.update({'free': int(group['free'])})
                pool_dict.update({'held': int(group['held'])})
                pool_dict.update({'in_use': int(group['in_use'])})
                continue
            
            # Available Addresses:
            m = p2.match(line)
            if m:
                group = m.groupdict
                address_type = 'available_addresses'
                continue
            
            # In Use Addresses:
            m = p3.match(line)
            if m:
                group = m.groupdict
                address_type = 'in_use_addresses'
                continue

            # 192.168.1.145
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if address_type:
                    address_type_list = pool_dict.get(address_type, [])
                    address_type_list.append(group['ip_address'])
                    pool_dict.update({address_type: address_type_list})
                continue

        return ret_dict