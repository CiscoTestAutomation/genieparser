import logging
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
import re


class DisplayConfigDhcpSchema(MetaParser):
    schema = {
        Any(): {
            Optional("domain"): str,
            Optional("gateway"): str,
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

class DisplayConfigDhcp(DisplayConfigDhcpSchema):
    # note below command does not exist.
    # there is no command that filters all dhcp info (unless regex on cli)
    # but that is not a good option. better to leverage python for that
    # the real command we will run is display current-configuration.
    cli_command = "display dhcp configuration"

    def cli(self, output=None):
        real_cmd = "display current-configuration"
        out = self.device.execute(real_cmd) if output is None else output

        # below regex extracts blocks op dhcp pools until the ! char:
        # !
        # ip pool dhcppool-vlan10
        #  network 10.23.25.0 mask 255.255.255.0
        # #
        p_get_dhcp_pool_blocks = re.compile(
            r'(?P<dhcp_pool_block>ip pool[\s\S]*?(?=\n.*?\#))')

        # ex:  domain-name Wijnen.local
        p_block_domain = re.compile(r"^domain-name (?P<domain_name>.*$)")

        # ex: ip pool dhcppool-vlan10
        p_block_pool_name = re.compile(r"^ip pool (?P<pool_name>.*)$")

        # ex:  gateway-list 10.23.25.254
        # something huawei config appends an extra whitespace at the end!
        p_block_gateway = re.compile(
            r"^gateway-list\s+(?P<gateway>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w.*)$")

        # ex:  network 10.0.10.160 255.255.255.240
        p_block_network = re.compile(
            r"^network\s(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+mask\s+(?P<subnet_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

        # note: there are a lot of options. for parsing we do not opinionate
        # we also dont do matching in the option data.
        # because it can contain almost everything
        p_block_options = re.compile(
            r"^option\s(?P<option>\d+)\s+ip-address\s+(?P<data>.*)")

        # ex:  nbns-list 1.1.1.3
        p_block_netbios_servers = re.compile(
            r"^nbns-list\s(?P<netbios_servers>.*)$")

        # ex:  dns-list 10.23.4.1 10.23.4.13
        p_block_dns_servers = re.compile(r"^dns-list\s(?P<dns_servers>.*)$")

        # lease can be in format: lease day 12 hour 0 minute 0
        # if not found in config the default hvrp is 1 day but hidden. so : lease day 1 hour 0 minute 0
        # we get the whole part after lease. no further usecases for further processing atm
        p_block_lease_time = re.compile(r"^lease\s+(?P<lease_options>.*)$")


        # lets get all blocks in the config
        get_dhcp_pool_blocks = p_get_dhcp_pool_blocks.findall(out)

        # note: can be multiples of below in a configuration
        # ex:  excluded-ip-address 10.23.25.1 10.23.25.100
        # ex:  excluded-ip-address 10.23.25.240 10.23.25.253
        p_get_dhcp_excluded = re.compile(
            r"^excluded-ip-address\s+(?P<exclude_range_start>[^ ]*)\s+(?P<exclude_range_end>[^ ]*)")

        dhcp_pools = {}
        for block in get_dhcp_pool_blocks:
            # set the indexes for nested dicts to 1 with every new block to parse
            index_networks = 1
            index_options = 1
            index_excluded = 1
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
                    gateway = gateway.strip()
                    dhcp_pools[pool_name]['gateway'] = gateway

                m = p_block_network.match(line)
                if m:
                    ip = m.groupdict()['ip']
                    subnet = m.groupdict()['subnet_mask']
                    network = {
                        "ip": ip,
                        "subnet_mask": subnet,
                    }
                    dhcp_pools[pool_name]['networks'][index_networks] = network

                m = p_block_options.match(line)
                if m:
                    option = m.groupdict()['option']
                    data = m.groupdict()['data']
                    option = {
                        "option": option,
                        # "type": "ip",
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

                m = p_get_dhcp_excluded.match(line)
                if m:
                    excluded_range_start = m.groupdict()['exclude_range_start']
                    exclude_range_end = m.groupdict()['exclude_range_end']
                    dhcp_pools[pool_name]['dhcp_excludes'][index_excluded] = {
                        "end": exclude_range_end,
                        "start": excluded_range_start
                    }
                    index_excluded += 1

        return dhcp_pools
