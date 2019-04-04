''' traceroute.py

IOSXE parsers for the following show commands:

    * traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# =====================================================================================================
# Schema for:
#   * 'traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}'
# =====================================================================================================
class TracerouteSchema(MetaParser):

    ''' Schema for:
        * 'traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}'
    '''

    schema = {
        'traceroute': 
            {Any(): 
                {'hops': 
                    {Any(): 
                        {'address': str,
                        Optional('probe_msec'): list,
                        Optional('vrf_in_name'): str,
                        Optional('vrf_out_name'): str,
                        Optional('vrf_in_id'): str,
                        Optional('vrf_out_id'): str,
                        Optional('label_name'): 
                            {Any(): 
                                {'label': int,
                                'exp': int,
                                },
                            },
                        },
                    },
                },
            },
        }


# =====================================================================================================
# Schema for:
#   * 'traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}'
# =====================================================================================================
class Traceroute(TracerouteSchema):

    ''' Parser for:
        * 'traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}'
    '''

    cli_command = 'traceroute {address} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}'

    def cli(self, address='', timeout=None, probe=None, min=None, max=None, source=None, output=None):

        # Init vars
        ret_dict = {}

        if output is None:
            return ret_dict
        else:
            out = output

        # Type escape sequence to abort.

        # Tracing the route to 172.16.166.253
        p1 = re.compile(r'^Tracing +the +route +to +(?P<traceroute>(\S+))$')

        # VRF info: (vrf in name/id, vrf out name/id)

        # 1 10.1.1.2 (red/1001, red/1001)
        # 2 10.2.1.2 (red/1001, red/1001)
        p2 = re.compile(r'^(?P<hop>(\d+)) +(?P<address>([a-zA-Z0-9\.\:]+))'
                         ' +\((?P<vrf_in_name>(\S+))\/(?P<vrf_in_id>(\d+)),'
                         ' +(?P<vrf_out_name>(\S+))\/(?P<vrf_out_id>(\d+))\)$')

        # 1 172.31.255.125 [MPLS: Label 624 Exp 0] 70 msec 200 msec 19 msec
        # 2 10.0.9.1 [MPLS: Label 300678 Exp 0] 177 msec 150 msec 9 msec
        # 3 192.168.14.61 [MPLS: Label 302537 Exp 0] 134 msec 1 msec 55 msec
        # 4 192.168.15.1 [MPLS: Label 24133 Exp 0] 6 msec 7 msec 64 msec
        # 5 10.80.241.86 [MPLS: Label 24147 Exp 0] 69 msec 65 msec 111 msec 
        # 6 10.90.135.110 [MPLS: Label 24140 Exp 0] 21 msec 4 msec 104 msec
        # 7 172.31.166.10 92 msec 51 msec 148 msec
        p3 = re.compile(r'^(?P<hop>(\d+)) +(?P<address>([a-zA-Z0-9\.\:]+))'
                         '(?: +\((?P<in_name>(\S+))\/(?P<in_id>(\d+)),'
                         ' +(?P<out_name>(\S+))\/(?P<out_id>(\d+))\))?'
                         '(?: +\[(?P<label_name>(MPLS)): +Label (?P<label>(\d+))'
                         ' +Exp +(?P<exp>(\d+))\])? +(?P<probe_msec>(.*))$')

        for line in out.splitlines():

            line = line.strip()

            # Tracing the route to 172.16.166.253
            m = p1.match(line)
            if m:
                traceroute = m.groupdict()['traceroute']
                tr_dict = ret_dict.setdefault('traceroute', {}).\
                                   setdefault(traceroute, {})
                continue

            # 1 10.1.1.2 (red/1001, red/1001)
            # 2 10.2.1.2 (red/1001, red/1001)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                hops_dict = tr_dict.setdefault('hops', {}).\
                                    setdefault(group['hop'], {})
                hops_dict['address'] = group['address']
                hops_dict['vrf_in_name'] = group['vrf_in_name']
                hops_dict['vrf_in_id'] = group['vrf_in_id']
                hops_dict['vrf_out_name'] = group['vrf_out_name']
                hops_dict['vrf_out_id'] = group['vrf_out_id']
                continue

            # 1 172.31.255.125 [MPLS: Label 624 Exp 0] 70 msec 200 msec 19 msec
            # 2 10.0.9.1 [MPLS: Label 300678 Exp 0] 177 msec 150 msec 9 msec
            # 3 192.168.14.61 [MPLS: Label 302537 Exp 0] 134 msec 1 msec 55 msec
            # 4 192.168.15.1 [MPLS: Label 24133 Exp 0] 6 msec 7 msec 64 msec
            # 5 10.80.241.86 [MPLS: Label 24147 Exp 0] 69 msec 65 msec 111 msec 
            # 6 10.90.135.110 [MPLS: Label 24140 Exp 0] 21 msec 4 msec 104 msec
            # 7 172.31.166.10 92 msec 51 msec 148 msec
            m = p3.match(line)
            if m:
                group = m.groupdict()
                hops_dict = tr_dict.setdefault('hops', {}).\
                                    setdefault(group['hop'], {})
                hops_dict['address'] = group['address']
                hops_dict['probe_msec'] = group['probe_msec'].\
                                            strip().replace(" msec", "").split()
                if group['label_name']:
                    label_dict = hops_dict.setdefault('label_name', {}).\
                                           setdefault(group['label_name'], {})
                    label_dict['label'] = int(group['label'])
                    label_dict['exp'] = int(group['exp'])
                continue

        return ret_dict
