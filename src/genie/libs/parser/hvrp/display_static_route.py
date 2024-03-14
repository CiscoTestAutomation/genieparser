from genie.metaparser import MetaParser, Any
import re
import logging


class DisplayStaticrouteSchema(MetaParser):
    schema = {
        "ip_routes": {
            Any(): {
                "ip_version": str,
                'subnet': str,
                'subnet_mask': str,
                'subnet_prefix': str,
                'next_hop': str,
                'preference': str,
                'route_name': str,
            }
        }
    }


class DisplayStaticRoute(DisplayStaticrouteSchema):
    cli_command = "display current-configuration | include ^ip route-static"

    """
ip route-static 0.0.0.0 0.0.0.0 192.168.12.42 preference 1
ip route-static 0.0.0.0 0.0.0.0 1.1.1.2 track bfd-session aa
ip route-static 145.7.64.247 255.255.255.255 NULL0 preference 250
ip route-static 145.13.71.128 255.255.255.128 192.168.12.42 preference 1
ip route-static 145.13.71.128 255.255.255.128 NULL0 preference 250
ip route-static 145.13.76.0 255.255.255.0 192.168.12.42 preference 1
ip route-static 145.13.76.0 255.255.255.0 NULL0 preference 250
ip route-static 192.168.28.0 255.255.255.0 192.168.12.42 preference 1
ip route-static 192.168.28.0 255.255.255.0 NULL0 preference 250 description testroute
ipv6 route-static :: 0 2001:67C:2504:F009::15A preference 1 description testroute-2
ipv6 route-static 2A07:3500:1BC0:: 49 2A07:3500:1BC0::F001:1002 description testroute-3
    """

    @staticmethod
    def convert_netmask_to_cidr(netmask):
        return sum(bin(int(x)).count('1') for x in netmask.split('.'))

    def cli(self, output=None):
        out = self.device.execute(
            self.cli_command) if output is None else output

        ip_routes_dict = {}

        result_dict = {}

        # matches
        # ip route-static 192.168.28.0 255.255.255.0 192.168.12.42 preference 1
        # ip route-static 192.168.28.0 255.255.255.0 NULL0 preference 250 description testroute
        p_ip_route_with_next_hop = re.compile(r'^(ipv6|ip)\sroute-static\s+(?P<subnet>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[:A-Z0-9]{0,39})\s+(?P<subnet_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[:A-Z0-9]{0,39})\s+(?P<next_hop>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[A-Za-z0-9-_:\.\/]*)')
        p_ip_version = re.compile(r"^(?P<ip_version>ipv6|ip)")
        p_preference = re.compile(r"(.*)preference\s+(?P<preference>\w+)")
        p_route_name = re.compile(r"(.*)description\s+(?P<route_name>([A-Za-z0-9-_@\"\`\&\,\+\=\/\'\.\(\)\[\]]*))")

        logging.debug(out)
        for line in out.splitlines():
            line = line.strip()

            match_route_with_next_hop = p_ip_route_with_next_hop.match(line)
            if match_route_with_next_hop:
                subnet = match_route_with_next_hop.groupdict()['subnet']
                subnet_mask = match_route_with_next_hop.groupdict()[
                    'subnet_mask']
                subnet_prefix = str(self.convert_netmask_to_cidr(subnet_mask))
                next_hop = match_route_with_next_hop.groupdict()['next_hop']

                match_ip_version = p_ip_version.match(line)
                ip_version = "4"
                if match_ip_version:
                    if "v6" in match_ip_version.groupdict()['ip_version']:
                        ip_version = "6"

                preference = ''
                match_preference = p_preference.match(line)
                if match_preference:
                    preference = match_preference.groupdict()['preference']


                route_name = ''
                match_route_name = p_route_name.match(line)
                if match_route_name:
                    route_name = match_route_name.groupdict()['route_name']

                if 'ip_routes' not in ip_routes_dict:
                    result_dict = ip_routes_dict.setdefault('ip_routes', {})

                identifier = f"{subnet}/{subnet_prefix}/{next_hop}"
                result_dict[identifier] = {
                    'ip_version': ip_version,
                    'subnet': subnet,
                    'subnet_mask': subnet_mask,
                    'subnet_prefix': subnet_prefix,
                    'next_hop': next_hop,
                    'route_name': route_name,
                    'preference': preference,
                }
                continue
        return ip_routes_dict