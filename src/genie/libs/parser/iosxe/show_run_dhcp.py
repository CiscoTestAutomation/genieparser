import logging
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
import re
from netaddr import AddrFormatError, IPAddress, IPNetwork

logger = logging.getLogger(__name__)


def create_cidr_notation(subnet, mask):
    try:
        cidr = IPNetwork(f"{subnet}/{mask}").prefixlen
        # ex:  10.0.0.0/24
        return f"{subnet}/{cidr}"
    except AddrFormatError:
        return "0.0.0.0"


def check_if_ip_in_network(ipaddress, network, subnet_mask):
    cidr = create_cidr_notation(network, subnet_mask)
    return IPAddress(ipaddress) in IPNetwork(cidr)


def extract_excluded_ip_address(exclude_addresses, subnet, subnet_mask, block_vrf=None):
    """
    Used in: DHCP Pools
    Example: ip dhcp excluded-address x.x.x.x x.x.x.x
    two conditions:
    exclude host:
        check if ip is in range --> add in exclude address as start and end
    exclude range
        check if first is in range --> exit when not
        if in range check, second --> if ok than add both to exclude address
        as start and end address
    If none matches return empty string
    :param settings:
    :return:
    """
    excluded_ip_addresses = {}

    for exclude_address in exclude_addresses['data']:
        exclude_vrf = exclude_addresses.get('vrf', None)

        # needs refactor.
        # 2 cases:
        #  - a pool with vrf statement should only match exclude statements with vrf
        #  - a pool without vrf statement should only match exclude statements without vrf
        if (block_vrf is not None and exclude_vrf is not None and exclude_vrf in block_vrf) or (block_vrf is None and exclude_vrf is None):
            in_network = check_if_ip_in_network(
                exclude_address,
                subnet,
                subnet_mask)
            if not in_network:
                break

            if len(exclude_addresses['data']) > 1:
                excluded_ip_addresses = {'start': exclude_addresses['data'][0],
                                         'end': exclude_addresses['data'][1]}
            else:
                excluded_ip_addresses = {'start': exclude_addresses['data'][0],
                                         'end': exclude_addresses['data'][0]}

    return excluded_ip_addresses


class ShowRunDhcpSchema(MetaParser):
    schema = {
        Any(): {
            Optional("domain"): str,
            Optional("gateway"): str,
            Optional("vrf"): str,
            Optional("boot_file"): str,
            Optional("netbios_servers"): list,
            Optional("dns_servers"): list,
            Optional("dhcp_excludes"): {
                Any(): {
                    Optional('end'): str,
                    Optional('start'): str,
                }
            },
            Optional("networks"): {
                Any(): {
                    Optional('ip'): str,
                    Optional('subnet_mask'): str,
                    Optional('secondary'): bool,
                }
            },
            Optional("dhcp_options"): {
                Any(): {
                    Optional("option"): str,
                    Optional("type"): str,
                    Optional("data"): str,
                }
            },
            Optional("lease_time"): str,
        },
    }


class ShowRunDhcp(ShowRunDhcpSchema):
    # note below command does not exist.
    # there is no command that filters all dhcp info (unless regex on cli)
    # but that is not a good option. better to leverage python for that
    # the real command we will run is show running-config.
    cli_command = "show running-config dhcp"

    def cli(self, output=None):
        real_cmd = "show running-config"
        out = self.device.execute(real_cmd) if output is None else output

        # below regex extracts blocks op dhcp pools until the ! char:
        # !
        # ip dhcp pool hatseflats-2
        #  network 172.16.3.0 255.255.255.0
        # !
        p_get_dhcp_pool_blocks = re.compile(
            r'(?P<dhcp_pool_block>ip dhcp pool[\s\S]*?(?=\n.*?\!))')

        # note: can be multiples of below in a configuration
        # ex: ip dhcp excluded-address 10.0.11.0 10.0.11.2
        # ex: ip dhcp excluded-address vrf lala 10.0.11.0 10.0.11.2
        p_get_dhcp_excluded = re.compile(
            r"^ip dhcp excluded-address (.*?)(?P<excludes>[0-9]+.*)$")

        p_get_dhcp_excluded_vrf = re.compile(
            r"^ip dhcp excluded-address vrf (?P<vrf>.*?)(?=\s)(.*?)(?P<excludes>[0-9]+.*)$")

        # regex extraction patterns for inside a block
        # note that we stripped the ident space of it
        #
        # ex:  domain-name Wijnen.local
        p_block_pool_name = re.compile(r"^ip dhcp pool (?P<pool_name>.*)$")
        p_block_domain = re.compile(r"^domain-name (?P<domain_name>.*$)")

        # ex:  default-router 10.24.125.254
        # ex:  default-router hostname.com
        p_block_gateway = re.compile(
            r"^default-router (?P<gateway>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w.*)$")

        # ex:  network 10.0.10.160 255.255.255.240
        p_block_network = re.compile(
            r"^network\s(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<subnet_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$")
        # ex:  network 10.0.10.160 255.255.255.240 secondary
        p_block_network_secondary = re.compile(
            r"^network\s(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<subnet_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<secondary>secondary)$")

        # note: there are a lot of options. for parsing we do not opinionate
        # we also dont do matching in the option data.
        # because it can contain almost everything
        p_block_options = re.compile(
            r"^option\s(?P<option>\d+)\s(?P<type>\w+)\s(?P<data>.*)$")

        # we capture everything after the keyword and split it later.
        # ex:  netbios-name-server 172.16.1.21 domain2.com
        # ex:  netbios-name-server domain1.com domain2.com
        # ex:  netbios-name-server 172.16.1.21 172.14.9.2
        p_block_netbios_servers = re.compile(
            r"^netbios-name-server\s(?P<netbios_servers>.*)$")

        p_block_dns_servers = re.compile(r"^dns-server\s(?P<dns_servers>.*)$")

        # lease can be in format: lease 0, lease 0 0, lease 0 0 0
        # where the zero can be a number. in format hour minute second
        # or with the word infinite.
        p_block_lease_time = re.compile(
            r"^lease\s+(?P<lease_options>infinite|.*)$")

        # needed to match the excluded range to vrf
        p_global_block_vrf = re.compile(r"vrf\s+(?P<vrf>.*?(?=\s))")

        # ex:  vrf my_first_vrf
        p_block_vrf = re.compile(r"^vrf\s+(?P<vrf>.*)$")

        # ex:  bootfile testfile
        p_boot_file = re.compile(r"^bootfile\s+(?P<boot_file>.*)$")

        # try except for routers without pools
        get_dhcp_pool_blocks = p_get_dhcp_pool_blocks.findall(out)


        dhcp_pools = {}
        excludes_list = []
        for line in out.splitlines():
            line = line.strip()

            m = p_get_dhcp_excluded.match(line)
            if m:
                excludes = m.groupdict()["excludes"]
                excludes_list.append({
                    "data": excludes.split(" ")
                })

            m = p_get_dhcp_excluded_vrf.match(line)
            if m:
                excludes = m.groupdict()["excludes"]
                vrf = m.groupdict()['vrf']
                excludes_list.append({
                    "vrf": vrf,
                    "data": excludes.split(" ")
                })

        for block in get_dhcp_pool_blocks:
            # set the indexes for nested dicts to 1 with every new block to parse
            index_networks = 1
            index_excluded = 1
            index_options = 1
            global_block_vrf = p_global_block_vrf.findall(block) or None
            for line in block.splitlines():
                line = line.strip()

                m = p_block_pool_name.match(line)
                if m:
                    pool_name = m.groupdict()['pool_name']
                    # setup nested items
                    dhcp_pools[pool_name] = {
                        'networks': {},
                        'dhcp_options': {},
                        'dhcp_excludes': {}
                    }

                m = p_block_domain.match(line)
                if m:
                    domain_name = m.groupdict()['domain_name']
                    dhcp_pools[pool_name]['domain'] = domain_name

                m = p_block_gateway.match(line)
                if m:
                    gateway = m.groupdict()['gateway']
                    dhcp_pools[pool_name]['gateway'] = gateway

                # reset m cause below ones look in global statements
                m = None
                m_network = p_block_network.match(line)
                if m_network:
                    m = m_network
                m_secondary = p_block_network_secondary.match(line)
                if m_secondary:
                    m = m_secondary
                if m:
                    ip = m.groupdict()['ip']
                    subnet = m.groupdict()['subnet_mask']
                    secondary = bool(m.groupdict().get("secondary"))
                    network = {
                        "ip": ip,
                        "subnet_mask": subnet,
                        "secondary": secondary,
                    }
                    dhcp_pools[pool_name]['networks'][index_networks] = network
                    index_networks += 1
                    # make sure there are excludes otherwise useless
                    if excludes_list:
                        for excluded in excludes_list:
                            matched = extract_excluded_ip_address(
                                excluded,
                                network['ip'],
                                network['subnet_mask'],
                                global_block_vrf
                            )
                            if matched:
                                dhcp_pools[pool_name]['dhcp_excludes'][
                                    index_excluded] = matched
                                index_excluded += 1

                m = p_block_options.match(line)
                if m:
                    option = m.groupdict()['option']
                    type = m.groupdict()['type']
                    data = m.groupdict()['data']
                    option = {
                        "option": option,
                        "type": type,
                        "data": data,
                    }
                    dhcp_pools[pool_name]['dhcp_options'][index_options] = option
                    index_options += 1

                m = p_block_netbios_servers.match(line)
                if m:
                    # perhaps we dont need to split.
                    # but then its a not a nice list
                    _ = m.groupdict()['netbios_servers']
                    netbios_servers = _.split(" ")
                    dhcp_pools[pool_name]['netbios_servers'] = netbios_servers

                m = p_block_dns_servers.match(line)
                if m:
                    # perhaps we dont need to split.
                    # but then its a not a nice list
                    _ = m.groupdict()['dns_servers']
                    dns_servers = _.split(" ")
                    dhcp_pools[pool_name]['dns_servers'] = dns_servers

                m = p_block_lease_time.match(line)
                if m:
                    lease_time = m.groupdict()['lease_options']
                    dhcp_pools[pool_name]['lease_time'] = lease_time

                m = p_block_vrf.match(line)
                if m:
                    vrf = m.groupdict()['vrf']
                    dhcp_pools[pool_name]['vrf'] = vrf

                m = p_boot_file.match(line)
                if m:
                    boot_file = m.groupdict()['boot_file']
                    dhcp_pools[pool_name]['boot_file'] = boot_file

        logging.debug(dhcp_pools)
        return dhcp_pools