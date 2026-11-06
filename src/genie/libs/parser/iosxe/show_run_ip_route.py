import logging

from genie.metaparser import MetaParser, Any
import re


logger = logging.getLogger(__name__)


class ShowRunIpRouteSchema(MetaParser):
    schema = {
        "ip_routes": {
            Any(): {
                'vrf': str,
                'vrf_global': str,
                'subnet': str,
                'subnet_mask': str,
                'cidr': int,
                'next_hop': str,
                'forward_address': str,
                'route_name': str,
                'metric': str,
                'track_object': str,
                'permanent': str,
                'tag': str,
            }
        }
    }


class ShowRunIpRoute(ShowRunIpRouteSchema):
    cli_command = "show running-config | i ^ip route"

    # SEVERAL DIFFERENT REAL WORLD EXAMPLES
    """
    ip route vrf 3rdParty 139.156.202.96 255.255.255.240 10.194.48.110
    ip route vrf 3rdParty 139.156.202.96 255.255.255.240 10.194.48.110 name Management
    ip route 139.156.202.96 255.255.255.240 10.194.48.110
    ip route 139.156.202.96 255.255.255.251 Vlan100
    ip route 139.156.202.96 255.255.255.240 Vlan100 10.194.48.110
    ip route 139.156.202.96 255.255.255.240 GigabitEthernet0/1/1
    ip route 139.156.202.96 255.255.255.240 GigabitEthernet0/1/1 240
    ip route 139.156.202.96 255.255.255.240 GigabitEthernet0/1/1 10.194.48.110
    ip route 192.168.1.0 255.255.255.0 GigabitEthernet0/0/0 213.162.171.193 name Management track 100
    ip route 139.156.202.96 255.255.255.240 10.194.48.110 name Management
    ip route 139.156.202.96 255.255.255.240 10.194.48.110 255
    ip route 139.156.202.96 255.255.255.240 Vlan100 255
    ip route 139.156.202.96 255.255.255.240 Vlan100 10.194.48.110 255
    ip route 139.156.202.96 255.255.255.240 10.194.48.110 track 100
    ip route 139.156.202.96 255.255.255.240 Vlan100 track 100
    ip route 139.156.202.96 255.255.255.240 Vlan100 10.194.48.110 track 100
    ip route 139.156.202.96 255.255.255.240 GigabitEthernet0/1/1 10.194.48.110 track 100
    ip route 139.156.202.96 255.255.255.240 10.194.48.110 255 track 100
    ip route 139.156.202.96 255.255.255.240 Vlan100 255 track 100
    ip route 139.156.202.96 255.255.255.240 Vlan100 10.194.48.110 255 track 100
    ip route 139.156.202.96 255.255.255.240 GigabitEthernet0/1/1 10.194.48.110 255 track 100
    ip route 10.73.238.0 255.255.254.0 10.73.224.1 name Dat"a`
    ip route 60.250.233.50 255.255.255.255 GigabitEthernet0/0 115.186.231.1 name Taiwan=Ware&house-TWTL-EP.10.1.1.1
    ip route vrf wlvbnavpn-11495 10.122.230.176 255.255.255.255 Cellular0/2/0 10 permanent name Loopback0_WBLM1151
    ip route 139.156.202.96 255.255.255.240 Serial0/0/0:0.110 10.194.48.110 255 track 100
    ip route vrf infinity01 10.100.0.0 255.255.0.0 FastEthernet4 222.229.224.185 global name Lala3-VPN-Inifnity-ED
    """


    @staticmethod
    def netmask_to_cidr(netmask):
        '''
        # code to convert netmask ip to cidr number
        :param netmask: netmask ip addr (eg: 255.255.255.0)
        :return: equivalent cidr number to given netmask ip (eg: 24)
        '''
        return sum([bin(int(x)).count('1') for x in netmask.split('.')])

    def cli(self, output=None):
        out = self.device.execute(
            self.cli_command) if output is None else output

        ip_routes_dict = {}

        result_dict = {}

        # MANDATORY EXAMPLE STATEMENT: ip route 139.156.202.96 255.255.255.240 OR ip route 139.156.202.96 255.255.255.240 GigabitEthernet0/1/1 WHERE VRF IS AN OPTIONAL
        p_ip_route_with_next_hop = re.compile(r'((^ip\sroute|^ip\sroute\svrf\s(?P<vrf>([A-Za-z0-9-_]*))))\s+(?P<subnet>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<subnet_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<next_hop>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[A-Za-z0-9-_:\.\/]*)')
        # FINDS OPTIONAL track tracking_object: ex track 100
        p_track_with_track_object = re.compile(r'(.*)track\s+(?P<tracking_object>\d+)')
        # FINDS OPTIONAL name iamastaticroute: ex name Management
        # 1/28/2022 commented below because found a route with "TE ST" in it bleggh
        # p_route_name = re.compile(r'(.*)name\s+(?P<route_name>([A-Za-z0-9-_@\"\`\&\,\+\=\/\'\.\(\)\[\]]*))')
        p_route_name = re.compile(r'(.*)name\s+(?P<route_name>(\".*\")|([A-Za-z0-9-_@\"\`\&\,\+\=\/\'\.\(\)\[\]]*))')
        p_forward_address = re.compile(r'(?P<forward_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        p_metric = re.compile(r'(?P<metric>\d+)')
        p_permanent = re.compile(r'(?P<permanent>permanent)')
        p_vrf_global = re.compile(r'(?P<vrf_global>global)')
        p_tag = re.compile(r'tag (?P<tag>\d+)')

        for line in out.splitlines():
            try:
                line = line.strip()
                temp_string = line

                match_route_with_next_hop = p_ip_route_with_next_hop.match(line)
                if match_route_with_next_hop:
                    vrf = match_route_with_next_hop.groupdict()['vrf'] or ''
                    subnet = match_route_with_next_hop.groupdict()['subnet']
                    subnet_mask = match_route_with_next_hop.groupdict()['subnet_mask']
                    cidr = self.netmask_to_cidr(subnet_mask)
                    next_hop = match_route_with_next_hop.groupdict()['next_hop']

                    # we remove the default statements from the result to parse the chaos after it.
                    temp_string = temp_string.replace(match_route_with_next_hop.group(), '').strip()

                    route_name = ''
                    match_naming_statements = p_route_name.match(temp_string)
                    if match_naming_statements:
                        route_name = match_naming_statements.groupdict()['route_name']
                        # we remove name statements from the line
                        temp_string = temp_string.replace(f'name {route_name}', '').strip()

                    track_object = ''
                    match_tracking_statements = p_track_with_track_object.match(temp_string)
                    if match_tracking_statements:
                        track_object = match_tracking_statements.groupdict()['tracking_object']
                        # we remove track statements from the line
                        temp_string = temp_string.replace(f'track {track_object}', '').strip()

                    # FORWARD ADRESS IS NOT PROPERLY MARKED BY CISCO. NO PREPEND INLINE
                    forward_address = ''
                    match_forward_address = p_forward_address.match(temp_string)
                    if match_forward_address:
                        forward_address = match_forward_address.groupdict()['forward_address']
                        # we remove forward_address statements from the line
                        temp_string = temp_string.replace(f'{forward_address}', '').strip()

                    # METRIC IS NOT PROPERLY MARKED BY CISCO. NO PREPEND INLINE
                    metric = ''
                    match_metric = p_metric.match(temp_string)
                    if match_metric:
                        metric = match_metric.groupdict()['metric']
                        # we remove metric statements from the line
                        temp_string = temp_string.replace(f'{metric}', '').strip()

                    permanent = ''
                    match_permanent = p_permanent.match(temp_string)
                    if match_permanent:
                        permanent = match_permanent.groupdict()['permanent']
                        # we remove permanent statements from the line
                        temp_string = temp_string.replace(f'{permanent}', '').strip()

                    vrf_global = ''
                    match_permanent = p_vrf_global.match(temp_string)
                    if match_permanent:
                        vrf_global = match_permanent.groupdict()['vrf_global']
                        # we remove vrf_global statements from the line
                        temp_string = temp_string.replace(f'{vrf_global}', '').strip()

                    tag = ''
                    match_tag = p_tag.match(temp_string)
                    if match_tag:
                        tag = match_tag.groupdict()['tag']
                        # we remove tag statements from the line
                        temp_string = temp_string.replace(f'tag {tag}', '').strip()

                    if 'ip_routes' not in ip_routes_dict:
                        result_dict = ip_routes_dict.setdefault('ip_routes', {})

                    identifier = f"{subnet}/{cidr}/{next_hop}"

                    result_dict[identifier] = {
                        'vrf': vrf,
                        'vrf_global': vrf_global,
                        'subnet': subnet,
                        'subnet_mask': subnet_mask,
                        'cidr': cidr,
                        'next_hop': next_hop,
                        'forward_address': forward_address,
                        'route_name': route_name,
                        'metric': metric,
                        'track_object': track_object,
                        'permanent': permanent,
                        'tag': tag,
                    }
                    continue

            except UnboundLocalError as e:
                logger.info(f"{e} on static route: {line}")
                continue
        return ip_routes_dict