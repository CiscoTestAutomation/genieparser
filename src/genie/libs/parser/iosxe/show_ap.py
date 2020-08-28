import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =========================
# Schema for:
#  * 'show ap cdp neighbor'
# =========================
class ShowApCdpNeighborSchema(MetaParser):
    """Schema for show ap cdp neighbor."""

    schema = {
        "ap_cdp_neighbor_count": int,
        "ap_name": {
            str: {
                "ap_ip": str,
                "neighbor_name": str,
                "neighbor_port": str,
                "neighbor_ip_count": int,
                "neighbor_ip_addresses": {
                  int: str
                }
            }
        }
    }


# =========================
# Parser for:
#  * 'show ap cdp neighbor'
# =========================
class ShowApCdpNeighbor(ShowApCdpNeighborSchema):
    """Parser for show ap cdp neighbor"""

    cli_command = 'show ap cdp neighbor'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ap_cdp_neighbor_dict = {}
        # Number of neighbors: 149
        #
        # AP Name                          AP IP                                     Neighbor Name      Neighbor Port
        # -------------------------------------------------------------------------------------------------------------
        # 0221-cap22                   10.8.33.106                              a02-21-sd-sw1.cisco.com TenGigabitEthernet3/0/47
        #
        # Neighbor IP Count: 1
        # 10.8.32.1
        # 0232-cap15                   10.8.32.46                              a02-32-sd-sw1.cisco.com TenGigabitEthernet9/0/47
        #
        # Neighbor IP Count: 1
        # 10.8.32.1
        #
        # 0211-cap27                   10.8.32.188                              a02-11-sd-sw1.cisco.com TenGigabitEthernet4/0/46
        #
        # Neighbor IP Count: 1
        # 10.8.32.1
        #
        # 0212-cap11                   10.8.33.160                              a02-12-sd-sw2.cisco.com TenGigabitEthernet1/0/40
        #
        # Neighbor IP Count: 1
        # 10.8.32.1
        #
        # 0212-cap10                   10.8.33.102                              a02-12-sd-sw1.cisco.com TenGigabitEthernet1/0/43
        #
        # Neighbor IP Count: 1
        # 10.8.32.1
        #
        # 0212-cap17                   10.8.32.203                              a02-12-sd-sw2.cisco.com TenGigabitEthernet1/0/47
        #
        # Neighbor IP Count: 1
        # 10.8.32.1
        #
        # 0212-ca.4                   10.8.32.202                              a02-12-sd-sw1.cisco.com TenGigabitEthernet1/0/48
        #
        # Neighbor IP Count: 1
        # 10.8.32.1
        #
        # 0222-cap09                   10.8.33.33                              a02-22-sd-sw2.cisco.com TenGigabitEthernet8/0/48
        #
        # Neighbor IP Count: 1
        # 10.8.32.1
        #
        # 0231-cap43                   10.8.33.93                               a02-31-sd-sw1.cisco.com TenGigabitEthernet4/0/47
        #
        # Neighbor IP Count: 1
        # 10.8.32.1
        #
        # 0222-cap08                   10.8.32.166                              a02-22-sd-sw2.cisco.com TenGigabitEthernet4/0/47
        #
        # Neighbor IP Count: 1
        # 10.8.32.1

        neighbor_count_capture = re.compile(r"^Number\s+of\s+neighbors:\s+(?P<neighbor_count>\d+)$")
        # 0221-cap22                   10.8.33.106                              a02-21-sd-sw1.cisco.com TenGigabitEthernet3/0/47
        neighbor_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<ap_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<neighbor_name>\S+)\s+(?P<neighbor_port>\S+)$")
        # Neighbor IP Count: 1
        neighbor_ip_count_capture = re.compile(r"^Neighbor\s+IP\s+Count:\s+(?P<neighbor_ip_count>\d+)$")
        # 10.8.32.1
        neighbor_ip_capture = re.compile(r"^(?P<neighbor_ip>\d+\.\d+\.\d+\.\d+)$")

        for line in out.splitlines():
            line = line.strip()
            # Number of neighbors: 149
            if neighbor_count_capture.match(line):
                neighbor_count_capture_match = neighbor_count_capture.match(line)
                groups = neighbor_count_capture_match.groupdict()
                neighbor_count = int(groups['neighbor_count'])
                ap_cdp_neighbor_dict['ap_cdp_neighbor_count'] = neighbor_count
                continue
            # AP Name                          AP IP                                     Neighbor Name      Neighbor Port
            elif line.startswith('AP Name'):
                continue
            #   -------------------------------------------------------------------------------------------------------------
            elif line.startswith('-----'):
                continue
            # 0221-cap22                   10.8.33.106                              a02-21-sd-sw1.cisco.com TenGigabitEthernet3/0/47
            elif neighbor_info_capture.match(line):
                neighbor_ip_index = 0
                neighbor_info_capture_match = neighbor_info_capture.match(line)
                groups = neighbor_info_capture_match.groupdict()
                ap_name = groups['ap_name']
                ap_ip = groups['ap_ip']
                neighbor_name = groups['neighbor_name']
                neighbor_port = groups['neighbor_port']
                if not ap_cdp_neighbor_dict.get('ap_name', {}):
                    ap_cdp_neighbor_dict['ap_name'] = {}
                ap_cdp_neighbor_dict['ap_name'][ap_name] = {}
                ap_cdp_neighbor_dict['ap_name'][ap_name]['ap_ip'] = ap_ip
                ap_cdp_neighbor_dict['ap_name'][ap_name]['neighbor_name'] = neighbor_name
                ap_cdp_neighbor_dict['ap_name'][ap_name]['neighbor_port'] = neighbor_port
            # Neighbor IP Count: 1
            elif neighbor_ip_count_capture.match(line):
                neighbor_ip_count_match = neighbor_ip_count_capture.match(line)
                groups = neighbor_ip_count_match.groupdict()
                neighbor_ip_count = int(groups['neighbor_ip_count'])
                ap_cdp_neighbor_dict['ap_name'][ap_name]['neighbor_ip_count'] = neighbor_ip_count
            # 10.8.32.1
            elif neighbor_ip_capture.match(line):
                neighbor_ip_index = neighbor_ip_index + 1
                neighbor_ip_match = neighbor_ip_capture.match(line)
                groups = neighbor_ip_match.groupdict()
                neighbor_ip = groups['neighbor_ip']
                if not ap_cdp_neighbor_dict['ap_name'][ap_name].get('neighbor_ip_addresses', {}):
                    ap_cdp_neighbor_dict['ap_name'][ap_name]['neighbor_ip_addresses'] = {}
                ap_cdp_neighbor_dict['ap_name'][ap_name]['neighbor_ip_addresses'][neighbor_ip_index] = neighbor_ip
                continue

        return ap_cdp_neighbor_dict