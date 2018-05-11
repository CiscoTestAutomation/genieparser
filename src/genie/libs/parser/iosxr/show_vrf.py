""" show_vrf.py

IOSXR parsers for the following show commands:
    * 'show vrf detail'
"""

# Python
import re
import xmltodict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


class ShowVrfAllDetailSchema(MetaParser):
    """Schema for show vrf all detail"""

    schema = {Any():
                {
                 Optional('route_distinguisher'): str,
                 Optional('vpn_id'): str,
                 Optional('interfaces'):  list,
                 Optional('vrf_mode'):  str,
                 Optional('description'):  str,
                 'address_family': {
                    Any(): {
                        Optional('route_target'): {
                            Any(): {
                                'route_target': str,
                                'rt_type': str,
                            },
                        },
                        Optional('route_policy'): {
                            'import': str,
                            'export': str
                        },
                    },
                }
            },
        }

class ShowVrfAllDetail(ShowVrfAllDetailSchema):
    """Parser for show vrf all detail"""

    def cli(self):
        cmd = 'show vrf all detail'
        out = self.device.execute(cmd)
        
        # Init vars
        vrf_dict = {}
        af_dict = {}
        intf_conf = False
        rt_type = None

        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            # VRF VRF1; RD 200:1; VPN ID not set
            p1 = re.compile(r'^VRF +(?P<vrf>[\w\-]+); +'
                             'RD +(?P<rd>[\w\s\:\<\>]+); +'
                             'VPN +ID +(?P<vpn_id>[\w\s\:]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']

                if vrf not in vrf_dict:
                    vrf_dict[vrf] = {}

                if 'not' not in m.groupdict()['rd']:
                    vrf_dict[vrf]['route_distinguisher'] = m.groupdict()['rd']

                if 'not' not in m.groupdict()['vpn_id']:
                    vrf_dict[vrf]['vpn_id'] = m.groupdict()['vpn_id']

                continue

            # VRF mode: Regular
            p2 = re.compile(r'^VRF +mode: +(?P<mode>[\w\-]+)$')
            m = p2.match(line)
            if m:
                vrf_dict[vrf]['vrf_mode'] = m.groupdict()['mode'].lower()
                continue

            # Description not set
            p3 = re.compile(r'^Description *(?P<desc>[\w\:\s\-]+)$')
            m = p3.match(line)
            if m:
                vrf_dict[vrf]['description'] = m.groupdict()['desc']
                continue

            # Interfaces:
            #     GigabitEthernet0/0/0/1
            p4 = re.compile(r'^Interfaces:$')
            m = p4.match(line)
            if m:
                intf_conf = True
                vrf_dict[vrf]['interfaces'] = []
                continue

            p4_1 = re.compile(r'^(?P<intf>[\w\s\/\.\-]+)$')
            m = p4_1.match(line)
            if m and intf_conf:
                intfs = m.groupdict()['intf'].split()
                vrf_dict[vrf]['interfaces'].extend(intfs)
                intf_conf = False
                continue

            # Address family IPV4 Unicast
            p5 = re.compile(r'^Address +family +(?P<af>[\w\s]+)$')
            m = p5.match(line)
            if m:
                af = m.groupdict()['af'].lower()
                if 'address_family' not in vrf_dict[vrf]:
                    vrf_dict[vrf]['address_family'] = {}
                if af not in vrf_dict[vrf]['address_family']:
                    vrf_dict[vrf]['address_family'][af] = {}

                af_dict = vrf_dict[vrf]['address_family'][af]
                continue

            # No Export VPN route-target communities
            # Export VPN route-target communities:
            p6 = re.compile(r'^Export +VPN +route\-target communities:$')
            m = p6.match(line)
            if m:
                rt_type = 'export'
                if 'route_target' not in af_dict:
                    af_dict['route_target'] = {}
                continue

            # No import VPN route-target communities
            # Import VPN route-target communities:
            p6_1 = re.compile(r'^Import +VPN +route\-target +communities:$')
            m = p6_1.match(line)
            if m:
                rt_type = 'import'
                if 'route_target' not in af_dict:
                    af_dict['route_target'] = {}
                continue

            #     RT:100:1
            p6_1 = re.compile(r'RT: *(?P<rt>[\w\:\.]+)$')
            m = p6_1.match(line)
            if m and rt_type:
                rt = m.groupdict()['rt']
                if rt not in af_dict['route_target']:
                    af_dict['route_target'][rt] = {}
                af_dict['route_target'][rt]['route_target'] = rt
                if 'rt_type' in af_dict['route_target'][rt]:
                    af_dict['route_target'][rt]['rt_type'] = 'both'
                else:
                    af_dict['route_target'][rt]['rt_type'] = rt_type.strip()
                continue

            # No import route policy
            p7 = re.compile(r'^No +import +route +policy$')
            m = p7.match(line)
            if m:
                rt_type = None
                continue

            # Import route policy: all-pass
            p7_1 = re.compile(r'^Import +route +policy: +(?P<route_map>[\w\-]+)$')
            m = p7_1.match(line)
            if m:
                rt_type = None
                if 'route_policy' not in af_dict:
                    af_dict['route_policy'] = {}
                af_dict['route_policy']['import'] = m.groupdict()['route_map']
                continue


            # No export route policy
            p8 = re.compile(r'^No +export +route +policy$')
            m = p8.match(line)
            if m:
                rt_type = None
                continue

            # Export route policy: allpass
            p8_1 = re.compile(r'^Export +route +policy: +(?P<route_map>[\w\-]+)$')
            m = p8_1.match(line)
            if m:
                rt_type = None
                if 'route_policy' not in af_dict:
                    af_dict['route_policy'] = {}
                af_dict['route_policy']['export'] = m.groupdict()['route_map']
                continue        

        return vrf_dict

# vim: ft=python et sw=4
