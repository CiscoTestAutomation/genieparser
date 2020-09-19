import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================================
# Schema for:
#  * 'show wireless client summary'
# =================================
class ShowWirelessClientSummarySchema(MetaParser):
    """Schema for show wireless client summary."""

    schema = {
        "wireless_client_summary": {
            "wireless_client_count": int,
            Optional("included_clients"): {
                Optional(int): {
                    Optional("id"): int,
                    Optional("mac_address"): str,
                    Optional("ap_name"): str,
                    Optional("type"): str,
                    Optional("state"): str,
                    Optional("protocol"): str,
                    Optional("method"): str,
                    Optional("role"): str
                }
            },
            "wireless_excluded_client_count": int,
            Optional("excluded_clients"): {
                Optional(int): {
                    Optional("id"): int,
                    Optional("mac_address"): str,
                    Optional("ap_name"): str,
                    Optional("type"): str,
                    Optional("state"): str,
                    Optional("protocol"): str,
                    Optional("method"): str,
                    Optional("role"): str
                }
            }
        }
    }


# =================================
# Parser for:
#  * 'show wireless client summary'
# =================================
class ShowWirelessClientSummary(ShowWirelessClientSummarySchema):
    """Parser for show wireless client summary"""

    cli_command = 'show wireless client summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        show_wireless_client_summary_dict = {}

        # Number of Clients: 13
        #
        # MAC Address    AP Name                                        Type ID   State             Protocol Method     Role
        # -------------------------------------------------------------------------------------------------------------------------
        # 58bf.ea58.b399 b80-72-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.ea58.b463 b80-82-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.ea58.b4ae b80-12-cap17                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.ea58.b4b1 b80-32-cap13                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.ea58.b4b6 b80-42-cap13                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.ea30.90cc b80-22-cap14                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eaa4.c601 b80-32-cap4                                  WLAN 19   IP Learn          11n(2.4) MAB        Local
        # 58bf.eae8.9e46 b80-51-cap7                                  WLAN 17   Authenticating    11ac     Dot1x      Unknown
        # 58bf.ea28.dbba b80-61-cap4                                  WLAN 17   Authenticating    11ac     Dot1x      Unknown
        # 58bf.ea32.c516 b80-62-cap1                                  WLAN 19   IP Learn          11n(5)   MAB        Local
        # 58bf.eaf0.3746 b80-12-cap14                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eab2.9354 b80-51-cap6                                  WLAN 17   Run               11n(5)   Dot1x      Local
        # 58bf.ea15.f311 b80-61-cap4                                  WLAN 19   Webauth Pending   11n(2.4) MAB        Local
        #
        # Number of Excluded Clients: 2
        #
        # MAC Address    AP Name                          Type ID   State              Protocol Method
        # ------------------------------------------------------------------------------------------------
        # 58bf.ea8a.20e6 b80-61-cap20                   WLAN 17   Excluded           11ac     Dot1x
        # 58bf.ea37.4442 b80-62-cap14                   WLAN 17   Excluded           11ac     Dot1x

        # Number of Clients: 13
        wireless_client_count_capture = re.compile(r"^Number\s+of\s+Clients:\s+(?P<wireless_client_count>\d+)$")
        # MAC Address    AP Name                                        Type ID   State             Protocol Method     Role
        wireless_client_info_header_capture = re.compile(
            r"^MAC\s+Address\s+AP\s+Name\s+Type\s+ID\s+State\s+Protocol\s+Method\s+Role$")
        # -------------------------------------------------------------------------------------------------------------------------
        delimiter_capture = re.compile(
            r"^-------------------------------------------------------------------------------------------------------------------------$")
        # 58bf.ea58.b399 b80-72-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
        wireless_client_info_capture = re.compile(
            r"^(?P<mac_address>\S+)\s+(?P<ap_name>\S+)\s+(?P<type>\S+)\s+(?P<id>\d+)\s+(?P<state>.*)\s+(?P<protocol>\S+)\s+(?P<method>(Dot1x|MAB))\s+(?P<role>\S+)$")
        # Number of Excluded Clients: 2
        wireless_excluded_client_count_capture = re.compile(
            r"^Number\s+of\s+Excluded\s+Clients:\s+(?P<wireless_excluded_client_count>\d+)$")
        # MAC Address    AP Name                          Type ID   State              Protocol Method
        exclude_client_header_capture = re.compile(
            r"^MAC\s+Address\s+AP\s+Name\s+Type\s+ID\s+State\s+Protocol\s+Method$")
        # ------------------------------------------------------------------------------------------------
        delimiter_2_capture = re.compile(
            r"^------------------------------------------------------------------------------------------------$")
        # 58bf.ea8a.20e6 b80-61-cap20                   WLAN 17   Excluded           11ac     Dot1x
        wireless_excluded_clients_info_capture = re.compile(
            r"^(?P<mac_address>\S+)\s+(?P<ap_name>\S+)\s+(?P<type>\S+)\s+(?P<id>\d+)\s+(?P<state>\S+)\s+(?P<protocol>\S+)\s+(?P<method>\S+)$")

        include_index = 0
        exclude_index = 0

        for line in out.splitlines():
            line = line.strip()
            # Number of Clients: 13
            if wireless_client_count_capture.match(line):
                wireless_client_count_capture_match = wireless_client_count_capture.match(line)
                groups = wireless_client_count_capture_match.groupdict()
                if not show_wireless_client_summary_dict.get('wireless_client_summary', {}):
                    show_wireless_client_summary_dict['wireless_client_summary'] = {}
                wireless_client_count = int(groups['wireless_client_count'])
                show_wireless_client_summary_dict['wireless_client_summary'][
                    'wireless_client_count'] = wireless_client_count
                continue
            # MAC Address    AP Name                                        Type ID   State             Protocol Method     Role
            elif wireless_client_info_header_capture.match(line):
                wireless_client_info_header_capture_match = wireless_client_info_header_capture.match(line)
                groups = wireless_client_info_header_capture_match.groupdict()
                continue
            # -------------------------------------------------------------------------------------------------------------------------
            elif delimiter_capture.match(line):
                delimiter_capture_match = delimiter_capture.match(line)
                groups = delimiter_capture_match.groupdict()
                continue
            # 58bf.ea58.b399 b80-72-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
            elif wireless_client_info_capture.match(line):
                wireless_client_info_capture_match = wireless_client_info_capture.match(line)
                groups = wireless_client_info_capture_match.groupdict()
                mac_address = groups['mac_address']
                ap_name = groups['ap_name']
                type = groups['type']
                id = int(groups['id'])
                state = groups['state'].strip()
                print(state)
                protocol = groups['protocol']
                method = groups['method']
                role = groups['role']
                if not show_wireless_client_summary_dict['wireless_client_summary'].get('included_clients'):
                    show_wireless_client_summary_dict['wireless_client_summary']['included_clients'] = {}
                include_index = include_index + 1
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'].update(
                    {include_index: {}})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'id': id})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'mac_address': mac_address})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'ap_name': ap_name})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'type': type})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'id': id})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'state': state})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'protocol': protocol})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'method': method})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'role': role})
                continue
            # Number of Excluded Clients: 2
            elif wireless_excluded_client_count_capture.match(line):
                wireless_excluded_client_count_capture_match = wireless_excluded_client_count_capture.match(line)
                groups = wireless_excluded_client_count_capture_match.groupdict()
                wireless_excluded_client_count = int(groups['wireless_excluded_client_count'])
                show_wireless_client_summary_dict['wireless_client_summary'][
                    'wireless_excluded_client_count'] = wireless_excluded_client_count
                continue
            # MAC Address    AP Name                          Type ID   State              Protocol Method
            elif exclude_client_header_capture.match(line):
                exclude_client_header_capture_match = exclude_client_header_capture.match(line)
                groups = exclude_client_header_capture_match.groupdict()
                continue
            # ------------------------------------------------------------------------------------------------
            elif delimiter_2_capture.match(line):
                delimiter_2_capture_match = delimiter_2_capture.match(line)
                groups = delimiter_2_capture_match.groupdict()
                continue
            # 58bf.ea8a.20e6 b80-61-cap20                   WLAN 17   Excluded           11ac     Dot1x
            elif wireless_excluded_clients_info_capture.match(line):
                wireless_excluded_clients_info_capture_match = wireless_excluded_clients_info_capture.match(line)
                groups = wireless_excluded_clients_info_capture_match.groupdict()
                mac_address = groups['mac_address']
                ap_name = groups['ap_name']
                type = groups['type']
                id = int(groups['id'])
                state = groups['state'].strip()
                protocol = groups['protocol']
                method = groups['method']
                if not show_wireless_client_summary_dict['wireless_client_summary'].get('excluded_clients'):
                    show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'] = {}
                exclude_index = exclude_index + 1
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'].update(
                    {exclude_index: {}})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'id': id})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'mac_address': mac_address})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'ap_name': ap_name})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'type': type})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'id': id})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'state': state})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'protocol': protocol})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'method': method})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'role': role})
                continue

        return show_wireless_client_summary_dict

