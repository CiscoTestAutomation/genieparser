import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===============================
# Schema for:
#  * 'show ap rf-profile summary'
# ===============================
class ShowApRfProfileSummarySchema(MetaParser):
    """Schema for show ap rf-profile summary."""

    schema = {
        "rf_profile_summary": {
            "rf_profile_count": int,
            "rf_profiles": {
                str: {
                    "rf_profile_name": str,
                    "band": str,
                    "description": str,
                    "state": str
                }
            }
        }
    }



# ===============================
# Parser for:
#  * 'show ap rf-profile summary'
# ===============================
class ShowApRfProfileSummary(ShowApRfProfileSummarySchema):
    """Parser for show ap rf-profile summary"""

    cli_command = 'show ap rf-profile summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        rf_profile_summary_dict = {}

        # Number of RF-profiles: 14
        #
        # RF Profile Name                  Band     Description                          State
        # ------------------------------------------------------------------------------------
        # Custom-RF_a                      5 GHz    Custom-RF_a_Desc                     Up
        # Custom-RF_b                      2.4 GHz  Custom-RF_b_Desc                     Up
        # Low_Client_Density_rf_5gh        5 GHz    pre configured Low Client Density rf Up
        # High_Client_Density_rf_5gh       5 GHz    pre configured High Client Density r Up
        # Low-Client-Density-802.11a       5 GHz                                         Up
        # Low_Client_Density_rf_24gh       2.4 GHz  pre configured Low Client Density rf Up
        # High-Client-Density-802.11a      5 GHz                                         Up
        # High_Client_Density_rf_24gh      2.4 GHz  pre configured High Client Density r Up
        # Low-Client-Density-802.11bg      2.4 GHz                                       Up
        # High-Client-Density-802.11bg     2.4 GHz                                       Up
        # Typical_Client_Density_rf_5gh    5 GHz    pre configured Typical Density rfpro Up
        # Typical-Client-Density-802.11a   5 GHz                                         Up
        # Typical_Client_Density_rf_24gh   2.4 GHz  pre configured Typical Client Densit Up
        # Typical-Client-Density-802.11bg  2.4 GHz                                       Up
        #


        # Number of RF-profiles: 14
        rf_profile_count_capture = re.compile(r"^Number\s+of\s+RF-profiles:\s+(?P<rf_profile_count>\d+)")
        # Custom-RF_a                      5 GHz    Custom-RF_a_Desc                     Up
        rf_profile_info_capture = re.compile(
            r"^(?P<rf_profile_name>\S+)\s+(?P<band>\S+\s+\S+)\s+(?P<description>.*)(?P<state>(Up|Down))")
        # RF Profile Name                  Band     Description                          State
        # ------------------------------------------------------------------------------------


        rf_profile_data = {}

        for line in out.splitlines():
            line = line.strip()
            # Number of RF-profiles: 14
            if rf_profile_count_capture.match(line):
                rf_profile_count_match = rf_profile_count_capture.match(line)
                groups = rf_profile_count_match.groupdict()
                rf_profile_count = int(groups['rf_profile_count'])
                if not rf_profile_summary_dict.get('rf_profile_summary', {}):
                    rf_profile_summary_dict['rf_profile_summary'] = {}
                rf_profile_summary_dict['rf_profile_summary']['rf_profile_count'] = rf_profile_count
                continue
            elif line.startswith('RF Profile Name'):
                continue
            elif line.startswith('-----'):
                continue
            # Custom-RF_a                      5 GHz    Custom-RF_a_Desc                     Up
            elif rf_profile_info_capture.match(line):
                rf_profile_info_match = rf_profile_info_capture.match(line)
                groups = rf_profile_info_match.groupdict()
                rf_profile_name = ''
                for k, v in groups.items():
                    if k == 'rf_profile_name':
                        rf_profile_name = v
                    v = v.strip()
                    if not rf_profile_summary_dict['rf_profile_summary'].get('rf_profiles', {}):
                        rf_profile_summary_dict['rf_profile_summary']['rf_profiles'] = {}
                    rf_profile_summary_dict['rf_profile_summary']['rf_profiles'][rf_profile_name] = {}
                    rf_profile_data.update({k: v})
                rf_profile_summary_dict['rf_profile_summary']['rf_profiles'][rf_profile_name].update(rf_profile_data)
                rf_profile_data = {}
                continue

        return rf_profile_summary_dict


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
