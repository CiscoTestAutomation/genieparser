"""show_rpf.py

IOSXE parsers for the following show commands:

    * show ip rpf <mroute address>
    * show ip rpf vrf <WORD> <mroute address>
    * show ipv6 rpf <mroute address>
    * show ipv6 rpf vrf <WORD> <mroute address>
"""

# import iosxe parser
from genie.libs.parser.iosxe.show_rpf import ShowIpRpf as ShowIpRpf_iosxe, \
                                             ShowIpv6Rpf as ShowIpv6Rpf_iosxe

# ==============================================
# Parser for 'show ip rpf <mroute address>'
# Parser for 'show ip rpf vrf <WORD> <mroute address>'
# ==============================================
class ShowIpRpf(ShowIpRpf_iosxe):
    """Parser for:
        show ip rpf <mroute address>
        show ip rpf vrf <vrf> <mroute address>"""
    pass


# ===========================================
# Parser for 'show ipv6 rpf <mroute address>'
# Parser for 'show ipv6 rpf vrf <vrf> <mroute address>'
# ===========================================
class ShowIpv6Rpf(ShowIpv6Rpf_iosxe):
    """Parser for:
        show ipv6 rpf <mroute address>
        show ipv6 rpf vrf <vrf> <mroute address>"""
    pass

