''' traceroute.py

IOSXR parsers for the following show commands:

    * traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ================
# Schema for:
#   * 'traceroute'
# ================
class TracerouteSchema(MetaParser):

    ''' Schema for:
        * 'traceroute'
    '''

    schema = {
        'traceroute':
            {Any():
                 {'hops':
                      {Any():
                           {'paths':
                                {Any():
                                     {'address': str,
                                      Optional('name'): str,
                                      Optional('probe_msec'): list,
                                      Optional('vrf_in_name'): str,
                                      Optional('vrf_out_name'): str,
                                      Optional('vrf_in_id'): str,
                                      Optional('vrf_out_id'): str,
                                      Optional('label_info'):
                                          {Optional('label_name'): str,
                                           Optional('exp'): int,
                                           Optional('MPLS'):
                                               {'label': str,
                                                'exp': int,
                                                },
                                           },
                                      Optional('mru'): int,
                                      },
                                 },
                            Optional('code'): str,
                            }
                       },
                  Optional('timeout_seconds'): int,
                  Optional('name_of_address'): str,
                  'address': str,
                  Optional('vrf'): str,
                  Optional('mask'): str,
                  },
             },
    }


# ================
# Schema for:
#   * 'traceroute'
# ================
class Traceroute(TracerouteSchema):

    ''' Parser for:
        * 'traceroute'
    '''

    def cli(self, output):

        # Init vars
        ret_dict = {}
        vrf, tr_dict = None, None
        # Set output
        out = output
        # init index for paths
        index = 1
        # Type escape sequence to abort.
        # traceroute 10.151.22.22
        # traceroute vrf MG501 192.168.1.1 numeric 
        p1 = re.compile(r'^traceroute( +vrf +(?P<vrf>\S+))? +[\S ]+$')

        # Tracing the route to 172.16.166.253
        p1_1 = re.compile(r'^Tracing +the +route +to +(?P<traceroute>(\S+))$')

        # Tracing MPLS Label Switched Path to 172.31.165.220/32, timeout is 2 seconds
        p1_2 = re.compile(r'^Tracing +MPLS +Label +Switched +Path +to'
                           ' +(?P<traceroute>\S+), +timeout +is'
                           ' +(?P<timeout>(\d+)) +seconds$')

        # Tracing the route to www.cisco.com (10.36.3.3)
        p1_3 = re.compile(r'^Tracing +the +route +to +(?P<name_of_address>\S+)'
                           ' \(+(?P<traceroute>\S+)\)$')

        # VRF info: (vrf in name/id, vrf out name/id)

        # 1 10.1.1.2 (red/1001, red/1001)
        # 2 10.2.1.2 (red/1001, red/1001)
        p2 = re.compile(r'^((?P<hop>(\d+)) +)?(?P<address>([a-zA-Z0-9\.\:]+))'
                         ' +\((?P<vrf_in_name>(\S+))\/(?P<vrf_in_id>(\d+)),'
                         ' +(?P<vrf_out_name>(\S+))\/(?P<vrf_out_id>(\d+))\)$')

        # L 1 10.169.197.93 MRU 1552 [Labels: implicit-null Exp: 0] 1 ms
        # ! 2 10.169.197.102 1 ms
        p3_1 = re.compile(r'^(?P<code>(!|Q|.|L|D|M|P|R|I|X)) +(?P<hop>(\d+))'
                           ' +(?P<address>([a-zA-Z0-9\.\:]+))'
                           '(?: +MRU +(?P<mru>(\d+)))?'
                           '(?: +\[Labels: +(?P<label_name>(\S+)) +Exp: +(?P<exp>(\d+))\])?'
                           ' +(?P<probe_msec>(.*))$')

        # 0 192.168.197.94 MRU 1552 [Labels: 1015 Exp: 0]
        p3_2 = re.compile(r'^((?P<hop>(\d+)) +)?(?P<address>([a-zA-Z0-9\.\:]+))'
                           ' +MRU +(?P<mru>(\d+)) +\[Labels: +(?P<label_name>(\S+))'
                           ' +Exp: +(?P<exp>(\d+))\]$')

        # 1 172.31.255.125 [MPLS: Label 624 Exp 0] 70 msec 200 msec 19 msec
        # 2 10.0.9.1 [MPLS: Label 300678 Exp 0] 177 msec 150 msec 9 msec
        # 3 192.168.14.61 [MPLS: Label 302537 Exp 0] 134 msec 1 msec 55 msec
        # 4 192.168.15.1 [MPLS: Label 24133 Exp 0] 6 msec 7 msec 64 msec
        # 5 10.80.241.86 [MPLS: Label 24147 Exp 0] 69 msec 65 msec 111 msec
        # 6 10.90.135.110 [MPLS: Label 24140 Exp 0] 21 msec 4 msec 104 msec
        # 7 172.31.166.10 92 msec 51 msec 148 msec
        # 8 10.169.197.101 1 msec 1 msec *
        # 1 10.19.198.29 [MPLS: Labels 16052/16062/16063/39 Exp 0] 2 msec 2 msec 2 msec
        p4 = re.compile(r'^((?P<hop>(\d+)) +)?(?P<address>([a-zA-Z0-9\.\:]+))(?: +\[(?P<label_name>(MPLS))'
                ': +Labels? (?P<label>(\S+)) +Exp +(?P<exp>(\d+))\])? +(?P<probe_msec>(\d+.*))$')
        # 1 p5DC5A26A.dip0.t-ipconnect.de (10.169.197.93) 0 msec *  1 msec *  0 msec
        p5 = re.compile(r'^((?P<hop>(\d+)) +)?(?P<name>[\S]+)'
                         ' +\(+(?P<address>([\d\.]+))\) +(?P<probe_msec>(.*))$')
        # 1  *
        p6 = re.compile(r'^((?P<hop>(\d+)) +)?(?P<address>\*)$')

        for line in out.splitlines():
            line = line.strip()
            
            # traceroute 10.151.22.22
            # traceroute vrf MG501 192.168.1.1 numeric
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if 'vrf' in group:
                    vrf = group['vrf']
                continue

            # Tracing the route to 172.16.166.253
            m = p1_1.match(line)
            if m:
                traceroute = m.groupdict()['traceroute']
                tr_dict = ret_dict.setdefault('traceroute', {}).\
                                   setdefault(traceroute, {})
                tr_dict['address'] = traceroute
                continue

            # Tracing MPLS Label Switched Path to 172.31.165.220/32, timeout is 2 seconds
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                traceroute = group['traceroute']
                tr_dict = ret_dict.setdefault('traceroute', {}).\
                                   setdefault(traceroute, {})
                tr_dict['timeout_seconds'] = int(group['timeout'])
                if '/' in traceroute:
                    new_out = re.search('(?P<ip>[\d\.]+)\/+(?P<mask>\d+)', traceroute)
                    address = new_out.groupdict()['ip']
                    mask = new_out.groupdict()['mask']
                    tr_dict['address'] = address
                    tr_dict['mask'] = mask
                else:
                    tr_dict['address'] = traceroute

                continue

            # Tracing the route to www.cisco.com (10.36.3.3)
            m = p1_3.match(line)
            if m:
                group = m.groupdict()
                traceroute = group['traceroute']
                name_of_address = group['name_of_address']
                tr_dict = ret_dict.setdefault('traceroute', {}).\
                                   setdefault(traceroute, {})
                tr_dict['name_of_address'] = name_of_address
                tr_dict['address'] = traceroute
                continue

            # 1 10.1.1.2 (red/1001, red/1001)
            # 2 10.2.1.2 (red/1001, red/1001)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group.get('hop'):
                    index = 1
                    path_dict = tr_dict.setdefault('hops', {}).\
                                        setdefault(group['hop'], {}).setdefault('paths',{})
                index_dict = path_dict.setdefault(index, {})
                index_dict['address'] = group['address']
                index_dict['vrf_in_name'] = group['vrf_in_name']
                index_dict['vrf_in_id'] = group['vrf_in_id']
                index_dict['vrf_out_name'] = group['vrf_out_name']
                index_dict['vrf_out_id'] = group['vrf_out_id']
                index += 1
                continue

            # L 1 10.169.197.93 MRU 1552 [Labels: implicit-null Exp: 0] 1 ms
            # ! 2 10.169.197.102 1 ms
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                hops_dict = tr_dict.setdefault('hops', {}). \
                    setdefault(group['hop'], {})
                if group.get('hop'):
                    index = 1
                    path_dict = hops_dict.setdefault('paths',{})
                index_dict = path_dict.setdefault(index, {})
                index_dict['address'] = group['address']
                if group['code']:
                    hops_dict['code'] = group['code']
                if group['mru']:
                    index_dict['mru'] = int(group['mru'])
                if group['label_name']:
                    label_dict = index_dict.setdefault('label_info', {})
                    label_dict['label_name'] = group['label_name']
                    label_dict['exp'] = int(group['exp'])
                if group['probe_msec']:
                    index_dict['probe_msec'] = group['probe_msec'].strip().\
                                                replace(" msec", "").\
                                                replace(" ms", "").\
                                                split()
                index += 1
                continue

            #   0 192.168.197.94 MRU 1552 [Labels: 1015 Exp: 0]
            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                if group.get('hop'):
                    index = 1
                    path_dict = tr_dict.setdefault('hops', {}).\
                                        setdefault(group['hop'], {}).setdefault('paths',{})
                index_dict = path_dict.setdefault(index, {})
                index_dict['address'] = group['address']
                if group['mru']:
                    index_dict['mru'] = int(group['mru'])
                if group['label_name']:
                    label_dict = index_dict.setdefault('label_info', {})
                    label_dict['label_name'] = group['label_name']
                    label_dict['exp'] = int(group['exp'])
                index += 1
                continue

            # 1 172.31.255.125 [MPLS: Label 624 Exp 0] 70 msec 200 msec 19 msec
            # 2 10.0.9.1 [MPLS: Label 300678 Exp 0] 177 msec 150 msec 9 msec
            # 3 192.168.14.61 [MPLS: Label 302537 Exp 0] 134 msec 1 msec 55 msec
            # 4 192.168.15.1 [MPLS: Label 24133 Exp 0] 6 msec 7 msec 64 msec
            # 5 10.80.241.86 [MPLS: Label 24147 Exp 0] 69 msec 65 msec 111 msec 
            # 6 10.90.135.110 [MPLS: Label 24140 Exp 0] 21 msec 4 msec 104 msec
            # 7 172.31.166.10 92 msec 51 msec 148 msec
            # 8 10.169.197.101 1 msec 1 msec *
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if group.get('hop'):
                    index = 1
                    path_dict = tr_dict.setdefault('hops', {}).\
                                        setdefault(group['hop'], {}).setdefault('paths',{})
                index_dict = path_dict.setdefault(index, {})
                index_dict['address'] = group['address']
                index_dict['probe_msec'] = group['probe_msec'].strip().\
                                            replace(" msec", "").\
                                            replace(" ms", "").\
                                            split()
                if group['label_name']:
                    label_dict = index_dict.setdefault('label_info', {}).\
                                        setdefault(group['label_name'], {})
                    label_dict['label'] = group['label']
                    label_dict['exp'] = int(group['exp'])
                index += 1
                continue

            # 1 p5DC5A26A.dip0.t-ipconnect.de (10.169.197.93) 0 msec *  1 msec *  0 msec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if group.get('hop'):
                    index = 1
                    path_dict = tr_dict.setdefault('hops', {}).\
                        setdefault(group['hop'], {}).\
                        setdefault('paths',{})
                index_dict = path_dict.setdefault(index, {})
                index_dict['address'] = group['address']
                index_dict['name'] = group['name']
                index_dict['probe_msec'] = group['probe_msec'].strip().\
                                            replace(" msec", "").\
                                            replace(" ms", "").\
                                            split()
                index += 1
                continue
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if group.get('hop'):
                    index = 1
                    path_dict = tr_dict.setdefault('hops', {}).\
                        setdefault(group['hop'], {}).\
                        setdefault('paths',{})
                index_dict = path_dict.setdefault(index, {})
                index_dict['address'] = group['address']
                index += 1
                continue
        
        # Update vrf if found from the command
        if tr_dict and vrf:
            tr_dict.update({'vrf': vrf})
        
        return ret_dict
