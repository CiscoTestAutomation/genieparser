"""
    show_ipv6.py
    NXOS parsers for the following show commands:

    * show ipv6 neighbor detail vrf all
    * show ipv6 nd interface vrf all
    * show ipv6 icmp neighbor detail vrf all
    * show ipv6 routers vrf all


"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

# ======================================================
# Parser for 'show ipv6 neighbor detail vrf all'
# ======================================================

class ShowIpv6NeighborsDetailVrfAllSchema(MetaParser):
    """
       Schema for "show ipv6 neighbor detail vrf all"
    """

    schema = {}

class ShowIpv6NeighborsDetailVrfAll(ShowIpv6NeighborsDetailVrfAllSchema):
    """
       Parser for "show ipv6 neighbor detail vrf all"
    """

    cli_command = 'show ipv6 neighbor detail vrf all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # regex

        for line in out.splitlines():
            line = line.strip()



        return ret_dict

# ======================================================
# Parser for 'show ipv6 nd interface vrf all'
# ======================================================

class ShowIpv6NdInterfaceVrfAllSchema(MetaParser):
    """
       Schema for "show ipv6 nd interface vrf all"
    """

    schema = {}

class ShowIpv6NdInterfaceVrfAll(ShowIpv6NdInterfaceVrfAllSchema):
    """
       Parser for "show ipv6 nd interface vrf all"
    """

    cli_command = 'show ipv6 nd interface vrf all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # regex

        for line in out.splitlines():
            line = line.strip()



        return ret_dict


# ======================================================
# Parser for 'show ipv6 icmp neighbor detail vrf all'
# ======================================================

# ======================================================
# Parser for 'show ipv6 routers vrf all'
# ======================================================

class ShowIpv6RoutersVrfAllSchema(MetaParser):
    """
       Schema for "show ipv6 routers vrf all"
    """

    schema = {
        'interfaces': {
            Any(): {
                'interface': str,  # Conf/Ops Str
                'router_advertisement': {
                    'router': str,
                    'last_update_time_min': int,
                    'current_hop_limit': int,
                    'lifetime': int,
                    'addrFlag': int,
                    'other_flag': int,
                    'mtu': int,
                    'home_agent_flag': int,
                    'preference': str,
                    'reachable_time_msec': int,
                    'retransmission_time': int,
                    'prefix': str,
                    'onlink_flag' : int,
                    'autonomous_flag': int,
                    'valid_lifetime': int,
                    'preferred_lifetime': int
                },
            }
        }
    }

class ShowIpv6RoutersVrfAll(ShowIpv6RoutersVrfAllSchema):
    """
       Parser for "show ipv6 routers vrf all"
    """

    cli_command = 'show ipv6 routers vrf all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Router fe80::f816:3eff:fe82:6320 on Ethernet1/1 , last update time 3.2 min
        p1 = re.compile(r'^Router +(?P<router>\S+) +on +(?P<interface>\S+) , +last +update +time +(?P<last_update_time_min>\S+) min$')

        # Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
        p2 = re.compile(r'^Current_hop_limit +(?P<current_hop_limit>(\d+)), +Lifetime +(?P<lifetime>(\d+)), +AddrFlag +'
                         '(?P<addrFlag>(\d+)), +OtherFlag +(?P<other_flag>(\d+)), +MTU +(?P<mtu>(\d+))$')

        # HomeAgentFlag 0, Preference Medium
        p3 = re.compile(r'^HomeAgentFlag +(?P<home_agent_flag>(\d+)), +Preference +(?P<preference>(\w+))$')

        # Reachable time 0 msec, Retransmission time 0 msec
        p4 = re.compile(r'')

        #   Prefix 2010:2:3::/64  onlink_flag 1 autonomous_flag 1
        p5 = re.compile(r'')

        #   valid lifetime 2592000, preferred lifetime 604800
        p6 = re.compile(r'')


        for line in out.splitlines():
            line = line.strip()
        return ret_dict

