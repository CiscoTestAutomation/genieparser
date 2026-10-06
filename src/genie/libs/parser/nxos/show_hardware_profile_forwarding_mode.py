import re

from genie.metaparser import MetaParser


class ShowHardwareProfileForwardingModeSchema(MetaParser):
    """Schema for show hardware profile forwarding-mode"""

    schema = {
        'forwarding_mode': str,
        'unicast_ipv4_size': int,
        'unicast_ipv4_rpf_size': int,
        'unicast_ipv6_size': int,
        'multicast_size': int,
    }


class ShowHardwareProfileForwardingMode(ShowHardwareProfileForwardingModeSchema):
    """Parser for show hardware profile forwarding-mode"""

    cli_command = 'show hardware profile forwarding-mode'

    def cli(self, command, output=None, **kwargs):
        if output is None:
            output = self.device.execute(command)

        ret_dict = {}

        # ===========================
        p1 = re.compile(r'^=+$')

        # forwarding-mode : normal
        p2 = re.compile(r'^forwarding-mode +: +(?P<forwarding_mode>\S+)$')

        # unicast IPv4 size     = 24576
        # unicast IPv4 rpf size = 0
        # unicast IPv6 size     = 0
        # multicast size        = 8192
        p3 = re.compile(r'^(?P<name>unicast +IPv4 +rpf +size|unicast +IPv4 +size|unicast +IPv6 +size|multicast +size) += +(?P<size>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # ===========================
            m = p1.match(line)
            if m:
                continue

            # forwarding-mode : normal
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['forwarding_mode'] = groups['forwarding_mode']
                continue

            # unicast IPv4 size     = 24576
            # unicast IPv4 rpf size = 0
            # unicast IPv6 size     = 0
            # multicast size        = 8192
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                key = '_'.join(groups['name'].lower().split())
                ret_dict[key] = int(groups['size'])
                continue

        return ret_dict
