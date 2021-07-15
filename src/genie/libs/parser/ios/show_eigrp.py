""" show_eigrp.py
IOS parsers for the following commands

    * 'show ip eigrp neighbors'
    * 'show ip eigrp vrf {vrf} neighbors'
    * 'show ipv6 eigrp neighbors'
    * 'show ip eigrp neighbors detail'
    * 'show ip eigrp vrf {vrf} neighbors detail'
    * 'show ipv6 eigrp neighbors detail'
    * 'show ip eigrp interfaces'
    * 'show ipv6 eigrp interfaces'
"""

# iosxe show ip eigrp
from genie.libs.parser.iosxe.show_eigrp import (
    ShowIpEigrpNeighbors as ShowIpEigrpNeighbors_iosxe,
    ShowIpv6EigrpNeighbors as ShowIpv6EigrpNeighbors_iosxe,
    ShowIpEigrpNeighborsDetail as ShowIpEigrpNeighborsDetail_iosxe,
    ShowIpv6EigrpNeighborsDetail as ShowIpv6EigrpNeighborsDetail_iosxe,
    ShowIpEigrpInterfaces as ShowIpEigrpInterfaces_iosxe,
    ShowIpv6EigrpInterfaces as ShowIpv6EigrpInterfaces_iosxe,
    ShowIpEigrpInterfacesDetail as ShowIpEigrpInterfacesDetail_iosxe,
    ShowIpv6EigrpInterfacesDetail as ShowIpv6EigrpInterfacesDetail_iosxe,
)


class ShowIpEigrpNeighbors(ShowIpEigrpNeighbors_iosxe):
    # Parser for:
    #   * 'show ip eigrp vrf {vrf} neighbors'
    #   * 'show ip eigrp neighbors'
    pass


class ShowIpv6EigrpNeighbors(ShowIpv6EigrpNeighbors_iosxe):
    # Parser for:
    #   * 'show ipv6 eigrp neighbors'

    cli_command = 'show ipv6 eigrp neighbors'

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)


class ShowIpEigrpNeighborsDetail(ShowIpEigrpNeighborsDetail_iosxe):
    # Parser for:
    #   'show ip eigrp neighbors detail'
    #   'show ip eigrp vrf {vrf} neighbors detail'
    pass


class ShowIpv6EigrpNeighborsDetail(ShowIpv6EigrpNeighborsDetail_iosxe):
    # Parser for:
    #   'show ipv6 eigrp neighbors detail'
    pass


class ShowIpEigrpInterfaces(ShowIpEigrpInterfaces_iosxe):
    # Parser for:
    #   'show ip eigrp interfaces'
    pass


class ShowIpv6EigrpInterfaces(ShowIpv6EigrpInterfaces_iosxe):
    # Parser for:
    #   'show ipv6 eigrp interfaces'
    pass


class ShowIpEigrpInterfacesDetail(ShowIpEigrpInterfacesDetail_iosxe):
    # Parser for:
    #   'show ip eigrp interfaces detail'
    pass


class ShowIpv6EigrpInterfacesDetail(ShowIpv6EigrpInterfacesDetail_iosxe):
    # Parser for:
    #   'show ipv6 eigrp interfaces detail'
    pass
