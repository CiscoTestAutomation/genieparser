import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ====================
# Schema for:
#  * 'show access-tunnel summary'
# ====================
class ShowAccessTunnelSummarySchema(MetaParser):
    """Schema for show access-tunnel summary."""

    schema = {
        "data_tunnels_count": int,
        "name": {
            str: {
                "rloc_ip": str,
                "ap_ip": str,
                "vrf_id": str,
                "src_port": str,
                "dst_port": str,
                "ifid": str,
                "up_time": str,
            }
        }
    }


# ====================
# Parser for:
#  * 'show access-tunnel summary'
# ====================
class ShowAccessTunnelSummary(ShowAccessTunnelSummarySchema):
    """Parser for show access-tunnel summary"""

    # Access Tunnels General Statistics:
    #  Number of AccessTunnel Data Tunnels       = 2  

    # Name    RLOC IP(Source)  AP IP(Destination)  VRF ID  Source Port  Destination Port
    # ------  ---------------  ------------------  ------  -----------  ----------------
    # Ac0     112.1.1.1        112.201.2.152       0       N/A          4788
    # Ac1     112.1.1.2        112.201.2.153       1       N/A          4789

    # Name   IfId            Uptime
    # ------ ---------- --------------------
    # Ac0    0x00000069 0 days, 02:55:04
    # Ac1    0x0000006A 0 days, 02:53:45

    cli_command = 'show access-tunnel summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Number of AccessTunnel Data Tunnels       = 2
        p1 = re.compile(r"^\s+Number\s+of\s+AccessTunnel\s+Data\s+Tunnels\s+=\s+(?P<data_tunnels_count>\d+)")

        # Ac0     112.1.1.1        112.201.2.152       0       N/A          4789
        p2 = re.compile(
            r"^(?P<name>\S+)\s+(?P<rloc_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<ap_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<vrf_id>\S+)\s+(?P<src_port>\S+)\s+(?P<dst_port>\S+)")

        # Ac0    0x00000069 0 days, 02:55:04
        p3 = re.compile(r"^(?P<name>\S+)\s+(?P<ifid>\S+)\s+(?P<up_time>.*\d+\:\d+\:\d+)")

        access_tunnel_dict = {}
        access_tunnel_ret_dict = {}
        i = 0
        for line in output.splitlines():
            line = line.rstrip()
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                data_tunnels_count = int(groups['data_tunnels_count'])
                access_tunnel_ret_dict['data_tunnels_count'] = data_tunnels_count
            m2 = p2.match(line)
            if m2:
                groups = m2.groupdict()
                access_tunnel_dict = access_tunnel_ret_dict.setdefault('name', {}).setdefault(groups['name'], {})
                access_tunnel_dict.update({
                    'rloc_ip': groups['rloc_ip'],
                    'ap_ip': groups['ap_ip'],
                    'vrf_id': groups['vrf_id'],
                    'src_port': groups['src_port'],
                    'dst_port': groups['dst_port']
                })

            m3 = p3.match(line)
            if m3:
                groups = m3.groupdict()

                access_tunnel_dict.update({
                    'ifid': groups['ifid'],
                    'up_time': groups['up_time']

                })
                i = i + 1
                if groups["name"] == list(access_tunnel_ret_dict["name"].keys())[i - 1]:
                    access_tunnel_ret_dict["name"][groups["name"]]["ifid"] = groups['ifid']
                    access_tunnel_ret_dict["name"][groups["name"]]["up_time"] = groups['up_time']
        return access_tunnel_ret_dict
