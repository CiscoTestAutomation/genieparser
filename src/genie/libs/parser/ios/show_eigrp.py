""" show_eigrp.py
IOS parsers for the following commands

    * 'show ip eigrp neighbors'
    * 'show ip eigrp vrf {vrf} neighbors'
    * 'show ipv6 eigrp neighbors'
    * 'show ipv6 eigrp vrf {vrf} neighbors'
    * 'show ip eigrp neighbors detail'
    * 'show ip eigrp vrf {vrf} neighbors detail'
    * 'show ipv6 eigrp neighbors detail'
"""

# iosxe show ip eigrp
from genie.libs.parser.iosxe.show_eigrp import (
    ShowIpEigrpNeighbors as ShowIpEigrpNeighbors_iosxe,
    ShowIpv6EigrpNeighbors as ShowIpv6EigrpNeighbors_iosxe,
    ShowIpEigrpNeighborsDetail as ShowIpEigrpNeighborsDetail_iosxe,
    ShowIpv6EigrpNeighborsDetail as ShowIpv6EigrpNeighborsDetail_iosxe,
)


class ShowIpEigrpNeighbors(ShowIpEigrpNeighbors_iosxe):
    # Parser for:
    #   * 'show ip eigrp vrf {vrf} neighbors'
    #   * 'show ip eigrp neighbors'

    def cli(self, vrf="", output=None):
        return super().cli(vrf=vrf, output=output)


class ShowIpv6EigrpNeighbors(ShowIpv6EigrpNeighbors_iosxe):
    # Parser for:
    #   * 'show ipv6 eigrp vrf {vrf} neighbors'
    #   * 'show ipv6 eigrp neighbors'

    def cli(self, vrf="", output=None):
        return super().cli(vrf=vrf, output=output)


class ShowIpEigrpNeighborsDetail(ShowIpEigrpNeighborsDetail_iosxe):
    # Parser for:
    #   'show ip eigrp neighbors detail'
    #   'show ip eigrp vrf {vrf} neighbors detail'

    def cli(self, vrf="", output=None):
        return super().cli(vrf=vrf, output=output)


class ShowIpv6EigrpNeighborsDetail(ShowIpv6EigrpNeighborsDetail_iosxe):
    # Parser for:
    #   'show ipv6 eigrp neighbors detail'

    def cli(self, output=None):
        return super().cli(output=output)
