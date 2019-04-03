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
class TracerouteNumericTimeoutProbeTTLSourceSchema(MetaParser):

    ''' Schema for:
        * 'traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}'
    '''

    schema = {
        'traceroute': 
            {Any(): 
                {'vrf_in': str,
                'vrf_out': str,
                'hops': 
                    {Any(): 
                        {'address': str,
                        Optional('label_name'): 
                            {Any(): 
                                {'label': int,
                                'exp': int,
                                },
                            },
                        'first': int,
                        'second': int,
                        'third': int,
                        },
                    },
                },
            },
        }


# =====================================================================================================
# Schema for:
#   * 'traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}'
# =====================================================================================================
class TracerouteNumericTimeoutProbeTTLSource(TracerouteNumericTimeoutProbeTTLSourceSchema):

    ''' Parser for:
        * 'traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}'
    '''

    cli_command = 'traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}'

    def cli(self, traceroute='', timeout='', probe='', min='', max='', source='', output=None):

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
        p2 = re.compile(r'^VRF +info: +\(vrf +in +(?P<vrf_in>(\S+)), +vrf +out'
                         ' +(?P<vrf_out>(\S+))\)$')

        # 1 172.31.255.125 [MPLS: Label 624 Exp 0] 70 msec 200 msec 19 msec
        # 2 10.0.9.1 [MPLS: Label 300678 Exp 0] 177 msec 150 msec 9 msec
        # 3 192.168.14.61 [MPLS: Label 302537 Exp 0] 134 msec 1 msec 55 msec
        # 4 192.168.15.1 [MPLS: Label 24133 Exp 0] 6 msec 7 msec 64 msec
        # 5 10.80.241.86 [MPLS: Label 24147 Exp 0] 69 msec 65 msec 111 msec 
        # 6 10.90.135.110 [MPLS: Label 24140 Exp 0] 21 msec 4 msec 104 msec
        # 7 172.31.166.10 92 msec 51 msec 148 msec
        p3 = re.compile(r'^(?P<hop>(\d+)) +(?P<address>([a-zA-Z0-9\.\:]+))'
                         '(?: +\[(?P<label_name>(MPLS)): +Label (?P<label>(\d+))'
                         ' +Exp +(?P<exp>(\d+))\])? +(?P<first>(\d+)) +msec'
                         ' +(?P<second>(\d+)) +msec +(?P<third>(\d+)) +msec$')

        for line in out.splitlines():

            line = line.strip()

            # Tracing the route to 172.16.166.253
            m = p1.match(line)
            if m:
                traceroute = m.groupdict()['traceroute']
                tr_dict = ret_dict.setdefault('traceroute', {}).\
                                   setdefault(traceroute, {})
                continue

            # VRF info: (vrf in name/id, vrf out name/id)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                tr_dict['vrf_in'] = group['vrf_in']
                tr_dict['vrf_out'] = group['vrf_out']
                continue

            # 1 172.31.255.125 [MPLS: Label 624 Exp 0] 70 msec 200 msec 19 msec
            # 7 172.31.166.10 92 msec 51 msec 148 msec
            m = p3.match(line)
            if m:
                group = m.groupdict()
                hops_dict = tr_dict.setdefault('hops', {}).\
                                    setdefault(group['hop'], {})
                hops_dict['address'] = group['address']
                hops_dict['first'] = int(group['first'])
                hops_dict['second'] = int(group['second'])
                hops_dict['third'] = int(group['third'])
                if group['label_name']:
                    label_dict = hops_dict.setdefault('label_name', {}).\
                                           setdefault(group['label_name'], {})
                    label_dict['label'] = int(group['label'])
                    label_dict['exp'] = int(group['exp'])
                continue

        return ret_dict
