'''
Author: Knox Hutchinson
Contact: https://dataknox.dev
https://twitter.com/data_knox
https://youtube.com/c/dataknox
'''
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# ======================================================
# Schema for 'show ip route'
# ======================================================

class ShowIPRouteSchema(MetaParser):
    schema = {
        'routes': {
            Any(): {
                'source_proto': str,
                'is_preferred': bool,
                'prefix': str,
                'subnet': str,
                'mask': str,
                'admin_dist': int,
                'metric': int,
                'next_hop': str,
                'vlan': str
            }
        }
    }

class ShowIPRoute(ShowIPRouteSchema):
    """Parser for show ip route on Dell PowerSwitch OS6 devices
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = 'show ip route'
    
    """
    S      *0.0.0.0/0 [254/1] via 10.10.21.1,   02d:06h:00m,  Vl20
    C      *10.10.21.0/24 [0/0] directly connected,   Vl20
    """
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        rt_dict = {}

        result_dict = {}

        p0 = re.compile(r'^(?P<source>\w)\s+(?P<preferred>[*]?)(?P<subnet>[\d.]+)\/(?P<mask>\d+)\s\[(?P<admin_dist>\d+)\/(?P<metric>\d+)\]\s(via |directly )(?P<next_hop>([\d.]+|connected)),\s+[^V]+Vl(?P<vlan>\d+)')

        for line in out.splitlines():
            line = line.strip()
            m = p0.match(line)
            if m:
                if 'routes' not in rt_dict:
                    result_dict = rt_dict.setdefault('routes',{})
                source_proto = m.groupdict()['source']
                is_preferred_star = m.groupdict()['preferred']
                if is_preferred_star:
                    is_preferred = True
                else:
                    is_preferred = False
                subnet = m.groupdict()['subnet']
                subnet_key = f"route-{subnet.replace('.','_')}"
                mask = m.groupdict()['mask']
                ad = m.groupdict()['admin_dist']
                metric = m.groupdict()['metric']
                next_hop = m.groupdict()['next_hop']
                vlan = m.groupdict()['vlan']
                if subnet_key not in result_dict:
                    result_dict[subnet_key] = {}
                    result_dict[subnet_key]['source_proto'] = source_proto
                    result_dict[subnet_key]['is_preferred'] = is_preferred
                    result_dict[subnet_key]['prefix'] = f"{subnet}/{mask}"
                    result_dict[subnet_key]['subnet'] = subnet
                    result_dict[subnet_key]['mask'] = mask
                    result_dict[subnet_key]['admin_dist'] = int(ad)
                    result_dict[subnet_key]['metric'] = int(metric)
                    result_dict[subnet_key]['next_hop'] = next_hop
                    result_dict[subnet_key]['vlan'] = vlan
        return rt_dict