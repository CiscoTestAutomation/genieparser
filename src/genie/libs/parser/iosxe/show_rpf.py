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
                    Optional('mofrr'): str,
                    'path':
                        {Any():
                            {'neighbor_address': str,
                             'interface_name': str,
                             'table_type': str,
                             Optional('neighbor_host'): str,
                             Optional('directly_connected'): bool,
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

    cli_command = ['show {af} rpf vrf {vrf} {mroute}', 'show {af} rpf {mroute}']

    def cli(self, mroute, af='ip', vrf='',output=None):
        if output is None:
            # set vrf infomation
            if vrf:
                cmd = self.cli_command[0].format(af=af, vrf=vrf, mroute=mroute)
            else:
                cmd = self.cli_command[1].format(af=af, mroute=mroute)
                vrf = 'default'
            # excute command to get output
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        ret_dict = {}
        intf = ''
        rpf_nbr = ''
        distance = ''

        # RPF information for 2001:99:99::99
        # RPF information for sj-eng-mbone.cisco.com
        p1 = re.compile(r'^RPF +information +for +(?P<mroute>[\S]+)$')

        # RPF information for host1 (172.16.10.13)
        # RPF information for ? (10.1.1.100)
        # RPF information for sj-eng-mbone.cisco.com (172.16.25.13)
        # RPF information for ? (192.168.16.226) MoFRR Enabled
        p1_1 = re.compile(r'^RPF +information +for +(?P<host>[\S]+) +'
                           '\((?P<mroute>[\w\:\.]+)\)( +MoFRR +(?P<mofrr>[\w]+))?$')

        # RPF interface: BRI0
        # RPF interface:GigabitEthernet3/2/0
        p2 = re.compile(r'^RPF +interface: *(?P<intf>[\S]+)$')

        # RPF neighbor: 2001:99:99::99
        # RPF neighbor: eng-isdn-pri3.cisco.com
        # RPF neighbor:FE80::40:1:3
        p3 = re.compile(r'^RPF +neighbor: *(?P<neighbor>[\S]+)$')

        # RPF neighbor: sj1.cisco.com (172.16.121.10)
        # RPF neighbor: eng-isdn-pri3.cisco.com (172.16.16.10)
        # RPF neighbor: ? (10.1.101.4) - directly connected
        p3_1 = re.compile(r'^RPF +neighbor: +(?P<host>[\S]+) +'
                            '\((?P<neighbor>[\w\.\:]+)\)( - (?P<directly_connected>directly connected))?$')

        # RPF route/mask: 10.1.1.0/24
        # RPF route/mask: 172.16.0.0/255.255.0.0
        # RPF route/mask:2001:db8:400::/64
        p4 = re.compile(r'^RPF +route\/mask:'
                         ' *(?P<route>[\w\/\:\.]+)\/(?P<mask>[\d\:\.]+)$')

        # RPF type: Mroute
        # RPF type: unicast (rip)
        # RPF type: unicast (ospf 2)
        # RPF type:Unicast
        p5 = re.compile(r'^RPF +type: *(?P<type>\w+)'
                         '( *\((?P<table_feature>\w+)( *(?P<inst>\d+))?\))?$')

        # RPF recursion count: 0
        # RPF recursion count:0
        p6 =  re.compile(r'^RPF +recursion +count:'
                          ' *(?P<count>\d+)$')

        # Metric preference: 128
        # Metric preference:110
        p7 = re.compile(r'^Metric +preference: *(?P<preference>\d+)$')

        # Metric: 0
        # Metric:30
        p8 = re.compile(r'^Metric: *(?P<metric>\d+)$')

        # Doing distance-preferred lookups across tables
        p9 = re.compile(r'^Doing +distance\-preferred +lookups +across +tables$')

        # Using Group Based VRF Select, RPF VRF: blue
        p10 = re.compile(r'^Using +Group +Based +VRF +Select, +RPF +VRF: +(?P<vrf>\S+)$')

        # RPF topology: ipv4 multicast base, originated from ipv4 unicast base
        p11 = re.compile(r'^RPF +topology: +(?P<lookup_topology>[\w\s]+)'
                          '(, +originated +from +(?P<originated_topology>[\w\s]+))?$')

        for line in out.splitlines():
            line = line.strip()

            # RPF information for 2001:99:99::99
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
            # RPF information for ? (192.168.16.226) MoFRR Enabled
            m = p1_1.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                host = m.groupdict()['host']
                mofrr = m.groupdict()['mofrr']
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                ret_dict['vrf'][vrf]['source_address'] = mroute
                ret_dict['vrf'][vrf]['source_host'] = host
                if mofrr:
                    ret_dict['vrf'][vrf]['mofrr'] = mofrr
                continue
           
            # RPF interface: BRI0
            m = p2.match(line)
            if m:
                intf = m.groupdict()['intf']
                continue
            
            # RPF neighbor: 2001:99:99::99
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
            # RPF neighbor: ? (10.1.101.4) - directly connected
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

                if m.groupdict()['directly_connected']:
                    ret_dict['vrf'][vrf]['path'][path]['directly_connected'] = True
                continue
            
            # RPF route/mask: 10.1.1.0/24
            # RPF route/mask: 172.16.0.0/255.255.0.0
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
            m = p6.match(line)
            if m:
                count = int(m.groupdict()['count'])
                ret_dict['vrf'][vrf]['path'][path]['recursion_count'] = count
                continue
        
            # Metric preference: 128
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
            m = p8.match(line)
            if m:
                metric = int(m.groupdict()['metric'])
                ret_dict['vrf'][vrf]['path'][path]['metric'] = metric
                continue
            
            # Doing distance-preferred lookups across tables
            m = p9.match(line)
            if m:
                ret_dict['vrf'][vrf]['path'][path]['distance_preferred_lookup'] = True
                continue
            
            # Using Group Based VRF Select, RPF VRF: blue
            m = p10.match(line)
            if m:
                lookup_vrf = m.groupdict()['vrf']
                ret_dict['vrf'][vrf]['path'][path]['lookup_vrf'] = lookup_vrf
                continue
            
            # RPF topology: ipv4 multicast base, originated from ipv4 unicast base
            m = p11.match(line)
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

    def cli(self, mroute, af='ipv6', vrf='',output=None):
        return super().cli(mroute=mroute, af=af, vrf=vrf,output=output)

