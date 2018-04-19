"""show_mcast.py

IOSXE parsers for the following show commands:

    * show ip rpf <mroute address>
    * show ip rpf vrf <WORD> <mroute address>
    * show ipv6 rpf <mroute address>
    * show ipv6 rpf vrf <WORD> <mroute address>
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ==============================================
# Parser for 'show ip rpf <mroute address>'
# Parser for 'show ip rpf vrf <WORD> <mroute address>'
# ==============================================

class ShowIpRpfSchema(MetaParser):
    """Schema for:
        show ip rpf <mroute address>
        show ip rpf vrf <vrf> <mroute address>
        show ipv6 rpf <mroute address>
        show ipv6 rpf vrf <vrf> <mroute address>"""

    schema = {'vrf':         
                {Any(): {
                    'source_address': str,
                    Optional('source_host'): str,
                    'path':
                        {Any():
                            {'neighbor_address': str,
                             'interface_name': str,
                             'table_type': str,
                             Optional('neighbor_host'): str,
                             Optional('admin_distance'): str,
                             Optional('route_mask'): str,
                             Optional('table_feature'): str,
                             Optional('table_feature_instance'): str,
                             Optional('recursion_count'): int,
                             Optional('metric'): int,
                             Optional('distance_preferred_lookup'): bool,
                             Optional('lookup_vrf'): str,
                             Optional('lookup_topology'): str,
                             Optional('originated_topology'): str
                            }
                        },
                    },
                },
            }

class ShowIpRpf(ShowIpRpfSchema):
    """Parser for:
        show ip rpf <mroute address>
        show ip rpf vrf <vrf> <mroute address>"""

    def cli(self, mroute, af='ip', vrf=''):

        # set vrf infomation
        if vrf:
            cmd = 'show {af} rpf vrf {vrf} {mroute}'\
                  .format(af=af, vrf=vrf, mroute=mroute)
        else:
            cmd = 'show {af} rpf {mroute}'\
                  .format(af=af, mroute=mroute)
            vrf = 'default'

        # excute command to get output
        out = self.device.execute(cmd)

        # initial variables
        ret_dict = {}
        intf = ''
        rpf_nbr = ''
        distance = ''

        for line in out.splitlines():
            line = line.strip()

            # RPF information for 2001:99:99::99
            p1 = re.compile(r'^RPF +information +for +(?P<mroute>[\w\:\.]+)$')
            m = p1.match(line)
            if m:
                mroute = m.groupdict()['mroute']

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                ret_dict['vrf'][vrf]['source_address'] = mroute
                continue

            # RPF information for host1 (172.16.10.13)
            # RPF information for ? (10.1.1.100)
            p1_1 = re.compile(r'^RPF +information +for +(?P<host>[\w\?]+) +'
                               '\((?P<mroute>[\w\:\.]+)\)$')
            m = p1_1.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                host = m.groupdict()['host']
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                ret_dict['vrf'][vrf]['source_address'] = mroute
                ret_dict['vrf'][vrf]['source_host'] = host
                continue

            # RPF interface: BRI0
            p2 = re.compile(r'^RPF +interface: +(?P<intf>[\w\/\.\-]+)$')
            m = p2.match(line)
            if m:
                intf = m.groupdict()['intf']
                continue

            # RPF neighbor: 2001:99:99::99
            p3 = re.compile(r'^RPF +neighbor: +(?P<neighbor>[\w\.\:]+)$')
            m = p3.match(line)
            if m:
                rpf_nbr = m.groupdict()['neighbor']

                path = (rpf_nbr + ' ' + intf).strip()
                if 'path' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['path'] = {}
                if path and path not in ret_dict['vrf'][vrf]['path']:
                    ret_dict['vrf'][vrf]['path'][path] = {}
                # interface_name
                if intf:
                    ret_dict['vrf'][vrf]['path'][path]['interface_name'] = intf
                ret_dict['vrf'][vrf]['path'][path]['neighbor_address'] = rpf_nbr
                continue

            # RPF neighbor: sj1.cisco.com (172.16.121.10)
            p3_1 = re.compile(r'^RPF +neighbor: +(?P<host>[\w\.\?]+) +'
                               '\((?P<neighbor>[\w\.\:]+)\)$')
            m = p3_1.match(line)
            if m:
                nei_host = m.groupdict()['host']
                rpf_nbr = m.groupdict()['neighbor']

                path = (rpf_nbr + ' ' + intf).strip()
                if 'path' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['path'] = {}
                if path and path not in ret_dict['vrf'][vrf]['path']:
                    ret_dict['vrf'][vrf]['path'][path] = {}

                # interface_name
                if intf:
                    ret_dict['vrf'][vrf]['path'][path]['interface_name'] = intf
                # neighbor_host
                ret_dict['vrf'][vrf]['path'][path]['neighbor_host'] = nei_host
                # rpf_nbr
                ret_dict['vrf'][vrf]['path'][path]['neighbor_address'] = rpf_nbr

                continue

            # RPF route/mask: 10.1.1.0/24
            # RPF route/mask: 172.16.0.0/255.255.0.0
            p4 = re.compile(r'^RPF +route\/mask:'
                             ' +(?P<route>[\w\/\:\.]+)\/(?P<mask>[\d\:\.]+)$')
            m = p4.match(line)
            if m:
                route = m.groupdict()['route']
                mask = m.groupdict()['mask']

                # convert 255.255.0.0 to 16
                if '.' in mask:
                    mask = sum([bin(int(x)).count("1") for x in mask.split(".")])

                ret_dict['vrf'][vrf]['path'][path]['route_mask'] = '{r}/{m}'.format(r=route, m=mask)
                continue

            # RPF type: Mroute
            # RPF type: unicast (rip)
            # RPF type: unicast (ospf 2)
            p5 = re.compile(r'^RPF +type: +(?P<type>\w+)'
                             '( *\((?P<table_feature>\w+)( *(?P<inst>\d+))?\))?$')
            m = p5.match(line)
            if m:
                table_feature = m.groupdict()['table_feature']
                table_type = m.groupdict()['type'].lower()
                table_feature_instance = m.groupdict()['inst']

                ret_dict['vrf'][vrf]['path'][path]['table_type'] = table_type
                if table_feature:
                    ret_dict['vrf'][vrf]['path'][path]['table_feature'] = table_feature
                if table_feature_instance:
                    ret_dict['vrf'][vrf]['path'][path]\
                        ['table_feature_instance'] = table_feature_instance
                continue

            # RPF recursion count: 0
            p6 =  re.compile(r'^RPF +recursion +count:'
                              ' +(?P<count>\d+)$')
            m = p6.match(line)
            if m:
                count = int(m.groupdict()['count'])
                ret_dict['vrf'][vrf]['path'][path]['recursion_count'] = count
                continue

            # Metric preference: 128
            p7 = re.compile(r'^Metric +preference: +(?P<preference>\d+)$')
            m = p7.match(line)
            if m:
                distance = m.groupdict()['preference']

                path = (rpf_nbr + ' ' + intf + ' ' + distance).strip()
                if 'path' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['path'] = {}
                else:
                    for exsited_path in ret_dict['vrf'][vrf]['path']:
                        if exsited_path in path:
                            ret_dict['vrf'][vrf]['path'][path] = \
                                ret_dict['vrf'][vrf]['path'][exsited_path]
                            del(ret_dict['vrf'][vrf]['path'][exsited_path])
                            break
                if path and path not in ret_dict['vrf'][vrf]['path']:
                    ret_dict['vrf'][vrf]['path'][path] = {}

                ret_dict['vrf'][vrf]['path'][path]['admin_distance'] = distance
                continue

            # Metric: 0
            p8 = re.compile(r'^Metric: +(?P<metric>\d+)$')
            m = p8.match(line)
            if m:
                metric = int(m.groupdict()['metric'])
                ret_dict['vrf'][vrf]['path'][path]['metric'] = metric
                continue

            # Doing distance-preferred lookups across tables
            p9 = re.compile(r'^Doing +distance\-preferred +lookups +across +tables$')
            m = p9.match(line)
            if m:
                ret_dict['vrf'][vrf]['path'][path]['distance_preferred_lookup'] = True
                continue

            # Using Group Based VRF Select, RPF VRF: blue
            p10 = re.compile(r'^Using +Group +Based +VRF +Select, +RPF +VRF: +(?P<vrf>\S+)$')
            m = p10.match(line)
            if m:
                lookup_vrf = m.groupdict()['vrf']
                ret_dict['vrf'][vrf]['path'][path]['lookup_vrf'] = lookup_vrf
                continue

            # RPF topology: ipv4 multicast base, originated from ipv4 unicast base
            p10 = re.compile(r'^RPF +topology: +(?P<lookup_topology>[\w\s]+)'
                              '(, +originated +from +(?P<originated_topology>[\w\s]+))?$')
            m = p10.match(line)
            if m:
                lookup_topology = m.groupdict()['lookup_topology']
                originated_topology = m.groupdict()['originated_topology']
                ret_dict['vrf'][vrf]['path'][path]['lookup_topology'] = lookup_topology
                if originated_topology:
                    ret_dict['vrf'][vrf]['path'][path]['originated_topology'] = originated_topology
                continue
        return ret_dict


# ===========================================
# Parser for 'show ipv6 rpf <mroute address>'
# Parser for 'show ipv6 rpf vrf <vrf> <mroute address>'
# ===========================================
class ShowIpv6Rpf(ShowIpRpf):
    """Parser for:
        show ipv6 rpf <mroute address>
        show ipv6 rpf vrf <vrf> <mroute address>"""

    def cli(self, mroute, vrf=''):
        return super().cli(mroute=mroute, af='ipv6', vrf=vrf)

