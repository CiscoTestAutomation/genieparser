from genie.metaparser import MetaParser, Any
import re
import logging


class DisplayStaticrouteSchema(MetaParser):
    schema = {
        "ip_routes": {
            Any(): {
                'subnet': str,
                'subnet_mask': str,
                'next_hop': str,
                'preference': str,
                'route_name': str,
                'vpn_instance': str,
                'bfd_session_name': str
            }
        }
    }


class DisplayStaticroute(DisplayStaticrouteSchema):
    cli_command = "display current-configuration | include ^ip route-static"

    """
    ip route-static 0.0.0.0 0.0.0.0 213.162.171.193 preference 1
    ip route-static 0.0.0.0 0.0.0.0 Tunnel0/0/10 preference 5
    ip route-static 10.127.249.45 255.255.255.255 Cellular0/0/0 preference 10
    ip route-static 145.7.64.247 255.255.255.255 NULL0 preference 250
    ip route-static 145.13.71.128 255.255.255.128 213.162.171.193 preference 1
    ip route-static 145.13.71.128 255.255.255.128 NULL0 preference 250
    ip route-static 145.13.71.128 255.255.255.128 Tunnel0/0/10 preference 5
    ip route-static 145.13.71.128 255.255.255.128 Cellular0/0/0 preference 10
    ip route-static 145.13.76.0 255.255.255.0 213.162.171.193 preference 1
    ip route-static 145.13.76.0 255.255.255.0 NULL0 preference 250
    ip route-static 145.13.76.0 255.255.255.0 Tunnel0/0/10 preference 5
    ip route-static 145.13.76.0 255.255.255.0 Cellular0/0/0 preference 10
    ip route-static 192.168.28.0 255.255.255.0 213.162.171.193 preference 1
    ip route-static 192.168.28.0 255.255.255.0 NULL0 preference 250
    ip route-static 192.168.28.0 255.255.255.0 Tunnel0/0/10 preference 5
    ip route-static 192.168.28.0 255.255.255.0 Cellular0/0/0 preference 10
    """

    def cli(self, output=None):
        out = self.device.execute(
            self.cli_command) if output is None else output

        ip_routes_dict = {}

        result_dict = {}

        p_ip_route_with_next_hop = re.compile(r'^ip\sroute-static\s+(?P<subnet>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<subnet_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<next_hop>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[A-Za-z0-9-_:\.\/]*)')
        p_metric = re.compile(r"(.*)preference\s+(?P<metric>\w+)")
        p_route_name = re.compile(r"(.*)description\s+(?P<route_name>([A-Za-z0-9-_@\"\`\&\,\+\=\/\'\.\(\)\[\]]*))")
        p_vpn_instance = re.compile(r"((.*)vpn-instance\s+(?P<vrf>([A-Za-z0-9-_@\"\`\&\,\+\=\/\'\.\(\)\[\]]*)))")
        p_bfd_session_name = re.compile(r"(.*)bfd-session\s+session-name\s+(?P<bfd_session_name>([A-Za-z0-9-_@\"\`\&\,\+\=\/\'\.\(\)\[\]]*))")

        logging.debug(out)
        for count, line in enumerate(out.splitlines()):
            line = line.strip()

            match_route_with_next_hop = p_ip_route_with_next_hop.match(line)
            if match_route_with_next_hop:
                subnet = match_route_with_next_hop.groupdict()['subnet']
                subnet_mask = match_route_with_next_hop.groupdict()[
                    'subnet_mask']
                next_hop = match_route_with_next_hop.groupdict()['next_hop']

            match_metric = p_metric.match(line)
            if match_metric:
                metric = match_metric.groupdict()['metric']


            route_name = ''
            match_route_name = p_route_name.match(line)
            if match_route_name:
                route_name = match_route_name.groupdict()['route_name']

            vpn_instance = ''
            match_vpn_instance = p_vpn_instance.match(line)
            if match_vpn_instance:
                vpn_instance = match_route_name.groupdict()['vpn_instance']

            bfd_session_name = ''
            match_bfd_session_name = p_bfd_session_name.match(line)
            if match_bfd_session_name:
                bfd_session_name = match_bfd_session_name.groupdict()['bfd_session_name']

            if 'ip_routes' not in ip_routes_dict:
                result_dict = ip_routes_dict.setdefault('ip_routes', {})
            result_dict[count] = {
                'subnet': subnet,
                'subnet_mask': subnet_mask,
                'next_hop': next_hop,
                'route_name': route_name,
                'preference': metric,
                'vpn_instance': vpn_instance,
                'bfd_session_name': bfd_session_name
            }
            continue
        return ip_routes_dict