from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
import re


# =====================================
# Schema for 'show ip routes'
# =====================================
class ShowIpRoutesSchema(MetaParser):

    """
    Schema for
        * show ip routes
        * show ip routes <prefix>
        * show ip routes vpn <vpn>
        * show ip routes vpn <vpn> <prefix>
    """

    schema = {
        'vrf': {
            Any(): {
                'prefixes': {
                    Any(): {
                        'prefix': str,
                         'protocol': str,
                         'protocol_sub_type': str,
                         'next_hop_list': {
                            Any(): {  # index
                                'index': int,
                                'nh_if_name': str,
                                'nh_vpn': str,
                                'nh_addr': str,
                                'tloc_ip': str,
                                'color': str,
                                'encap': str,
                                'status': list
                            }
                        }
                    }
                }
            }
        }
    }


# =====================================
# Parser for 'show ip routes'
# =====================================
class ShowIpRoutes(ShowIpRoutesSchema):
    """
    parser for
        show ip routes
        show ip routes <prefix>
        show ip routes vpn <vpn>
        show ip routes vpn <vpn> <prefix>
    """

    cli_command = ['show ip routes',
                   'show ip routes {prefix}',
                   'show ip routes vpn {vpn}',
                   'show ip routes vpn {vpn} {prefix}'
                   ]

    def cli(self, prefix=None, vpn=None, output=None):

        if output is None:
            if prefix and vpn:
                cmd = self.cli_command[3].format(prefix=prefix, vpn=vpn)
            elif prefix:
                cmd = self.cli_command[1].format(prefix=prefix)
            elif vpn:
                cmd = self.cli_command[2].format(vpn=vpn)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        #                                             PATH                      ATTRIBUTE
        #                                             PROTOCOL  NEXTHOP     NEXTHOP          NEXTHOP
        # VPN    PREFIX              PROTOCOL         SUB TYPE  IF NAME     ADDR             VPN      TLOC IP          COLOR            ENCAP  STATUS
        # ---------------------------------------------------------------------------------------------------------------------------------------------
        # 0      0.0.0.0/0           static           -         ge2/3       19.75.2.192      -        -                -                -      F,S
        p1 = re.compile(r'(?P<vrf>\d+)\s+(?P<prefix>[\d\.\/]+)\s+(?P<protocol>\S+)\s+(?P<protocol_sub_type>\S+)\s+(?P<nh_if_name>\S+)\s+(?P<nh_addr>[\d\.\/]+|-)\s+(?P<nh_vpn>\S+)\s+(?P<tloc_ip>[\d\.\/]+|-)\s+(?P<color>\S+)\s+(?P<encap>\S+)\s+(?P<status>\S+)')

        index = 1

        for line in out.splitlines():
            line = line.strip()

            # 0      0.0.0.0/0           static           -         ge2/3       19.75.2.192      -        -                -                -      F,S
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['vrf']:
                    vrf = group['vrf']
                if prefix != group['prefix']:
                    prefix = group['prefix']
                    index = 1

                route_info = parsed_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('prefixes', {}).setdefault(prefix, {})
                route_info['prefix'] = prefix
                route_info['protocol'] = group['protocol']
                route_info['protocol_sub_type'] = group['protocol_sub_type']

                nh_list_dict = route_info.setdefault('next_hop_list', {})
                idx_dict = nh_list_dict.setdefault(index, {})
                idx_dict['index'] = index
                idx_dict['nh_addr'] = group['nh_addr']
                idx_dict['nh_if_name'] = group['nh_if_name']
                idx_dict['nh_vpn'] = group['nh_vpn']
                idx_dict['status'] = group['status'].split(",")
                idx_dict['tloc_ip'] = group['tloc_ip']
                idx_dict['color'] = group['color']
                idx_dict['encap'] = group['encap']
                index += 1

        return parsed_dict
