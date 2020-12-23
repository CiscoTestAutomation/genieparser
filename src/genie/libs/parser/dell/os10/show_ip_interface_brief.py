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
# Schema for 'show ip interface'
# ======================================================


class ShowIPInterfaceBriefSchema(MetaParser):
    schema = {
        'ints': {
            Any(): {
                'ip_address': str,
                'ok': bool,
                'method': str,                
                'status': str,
                'protocol': str
            }
        }
    }


class ShowIPInterfaceBrief(ShowIPInterfaceBriefSchema):
    """Parser for show ip interface brief on Dell PowerSwitch OS10 devices
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = 'show ip interface brief'

    """
    Interface Name            IP-Address          OK       Method       Status     Protocol 
    =========================================================================================
    Ethernet 1/1/1            unassigned          YES      unset        up          up       
    Ethernet 1/1/2            unassigned          YES      unset        up          up       
    Ethernet 1/1/3            unassigned          YES      unset        up          up       
    Ethernet 1/1/4            unassigned          YES      unset        up          up       
    Ethernet 1/1/5            unassigned          NO       unset        up          down     
    Ethernet 1/1/6            unassigned          NO       unset        up          down     
    Ethernet 1/1/7            unassigned          NO       unset        up          down     
    Ethernet 1/1/8            unassigned          NO       unset        up          down     
    Ethernet 1/1/9            unassigned          NO       unset        up          down     
    Ethernet 1/1/10           unassigned          NO       unset        up          down     
    Ethernet 1/1/11           unassigned          NO       unset        up          down     
    Ethernet 1/1/12           unassigned          NO       unset        up          down     
    Ethernet 1/1/13           unassigned          NO       unset        up          down     
    Ethernet 1/1/14           unassigned          NO       unset        up          down     
    Ethernet 1/1/15           unassigned          NO       unset        up          down     
    Ethernet 1/1/16           unassigned          NO       unset        up          down     
    Ethernet 1/1/17           unassigned          NO       unset        up          down     
    Ethernet 1/1/18           unassigned          NO       unset        up          down     
    Ethernet 1/1/19           unassigned          NO       unset        up          down     
    Ethernet 1/1/20           unassigned          NO       unset        up          down     
    Ethernet 1/1/21           unassigned          NO       unset        up          down     
    Ethernet 1/1/22           unassigned          NO       unset        up          down     
    Ethernet 1/1/23           unassigned          NO       unset        up          down     
    Ethernet 1/1/24           unassigned          NO       unset        up          down     
    Ethernet 1/1/25           unassigned          NO       unset        up          down     
    Ethernet 1/1/26           unassigned          NO       unset        up          down     
    Ethernet 1/1/27           unassigned          NO       unset        up          down     
    Ethernet 1/1/28           unassigned          NO       unset        up          down     
    Ethernet 1/1/29           unassigned          NO       unset        up          down     
    Ethernet 1/1/30           unassigned          NO       unset        up          down     
    Ethernet 1/1/31           unassigned          NO       unset        up          down     
    Ethernet 1/1/32           unassigned          NO       unset        up          down     
    Management 1/1/1          10.10.21.16/24      YES      manual       up          up       
    Vlan 1                    unassigned          YES      unset        up          up
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        int_dict = {}

        result_dict = {}

        p0 = re.compile(
            r'^(?P<int_name>\w+\s(\d+\/\d+\/\d+|\d+))\s+(?P<ip_add>(unassigned|\d+\.\d+\.\d+\.\d+\/\d+))\s+(?P<ok>(YES|NO))\s+(?P<method>(unset|manual|DHCP))\s+(?P<status>(up|down))\s+(?P<protocol>(up|down))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:            
                int_name = m.groupdict()['int_name']    
                ip_add = m.groupdict()['ip_add']
                ok = m.groupdict()['ok']
                if ok == 'YES':
                    ok = True
                else:
                    ok = False
                method = m.groupdict()['method']
                status = m.groupdict()['status']
                protocol = m.groupdict()['protocol']
                if 'ints' not in int_dict:
                    result_dict = int_dict.setdefault('ints', {})
                result_dict[int_name] = {}
                result_dict[int_name]['ip_address'] = ip_add
                result_dict[int_name]['ok'] = ok
                result_dict[int_name]['method'] = method
                result_dict[int_name]['status'] = status
                result_dict[int_name]['protocol'] = protocol
                continue
        return int_dict
