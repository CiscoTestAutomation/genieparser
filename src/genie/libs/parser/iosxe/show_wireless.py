import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ========================================
# Schema for:
#  * 'show wireless fabric client summary'
# ========================================
class ShowWirelessFabricClientSummarySchema(MetaParser):
    """Schema for show wireless fabric client summary."""

    schema = {
        "number_of_fabric_clients" : int,
        Optional("clients") : {
            Optional(int) : {
                Optional("mac_address") : str,
                Optional("ap_name") : str,
                Optional("wlan") : str,
                Optional("state") : str,
                Optional("protocol") : str,
                Optional("method") : str,
            }
        }
    }


# ========================================
# Parser for:
#  * 'show wireless fabric client summary'
# ========================================
class ShowWirelessFabricClientSummary(ShowWirelessFabricClientSummarySchema):
    """Parser for show wireless fabric client summary"""

    cli_command = 'show wireless fabric client summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output=output

        show_wireless_fabric_client_summary_dict = {}

        # Number of Fabric Clients : 8

        # MAC Address    AP Name                          WLAN State              Protocol Method     
        # --------------------------------------------------------------------------------------------
        # 58bf.ea72.1730 a2-11-cap43                   17   Run                11ac     Dot1x     
        # 58bf.ea73.39b4 a2-11-cap50                   19   IP Learn           11n(2.4) MAB       
        # 58bf.ea47.1c4c a2-11-cap52                   19   Webauth Pending    11n(2.4) MAB       
        # --------------------------------------------------------------------------------------------
        # 58bf.ea47.1c59 a2-11-cap46                   17   Run                11ac     Dot1x     
        # 58bf.ea41.eac4 a2-12-cap15                   19   Webauth Pending    11n(2.4) MAB       
        # 58bf.eaef.9769 a2-11-cap44                   19   Webauth Pending    11n(2.4) MAB       
        # --------------------------------------------------------------------------------------------
        # 58bf.ea02.5c2a a2-12-cap17                   19   Webauth Pending    11ac     MAB       
        # 58bf.ea09.f357 a2-12-cap17                   19   Webauth Pending    11ac     MAB   

        # Number of Fabric Clients : 8
        clients_capture = r"(?P<clients>\S+)"
        p_clients = re.compile(r"Number\s+of\s+Fabric\s+Clients\s+:\s+{clients_capture}".format(clients_capture=clients_capture))

        # MAC Address    AP Name                          WLAN State              Protocol Method
        p_header = re.compile(r"MAC\s+Address\s+AP\s+Name\s+WLAN\s+State\s+Protocol\s+Method")

        # -------------------------------------------------------------------------------------------------------------------------
        p_delimiter = re.compile(
            r"^-------------------------------------------------------------------------------------------------------------------------$")

        # 58bf.ea72.1730 a2-11-cap43                   17   Run                11ac     Dot1x
        mac_capture = r"(?P<mac>\S{4}\.\S{4}\.\S{4})"
        name_capture = r"(?P<name>\S+)"
        wlan_capture = r"(?P<wlan>\S+)"
        state_capture = r"(?P<state>.*)"
        protocol_capture = r"(?P<protocol>\S+)"
        method_capture = r"(?P<method>(Dot1x|MAB))"
        p_client_info = re.compile(r"{mac_capture}\s+{name_capture}\s+{wlan_capture}\s+{state_capture}\s+{protocol_capture}\s+{method_capture}".format(mac_capture=mac_capture, name_capture=name_capture, 
                                                                                                                                                        wlan_capture=wlan_capture, state_capture=state_capture,
                                                                                                                                                        protocol_capture=protocol_capture, method_capture=method_capture))


        show_wireless_fabric_client_summary_dict = {}
        client_index = 0

        for line in output.splitlines():
            line = line.strip()
            # Number of Fabric Clients : 8
            if p_clients.match(line):
                match = p_clients.match(line)
                client_count = int(match.group('clients'))
                if not show_wireless_fabric_client_summary_dict.get('number_of_fabric_clients'):
                    show_wireless_fabric_client_summary_dict.update({'number_of_fabric_clients' : client_count})
                continue
            # MAC Address    AP Name                          WLAN State              Protocol Method
            elif p_header.match(line):
                match = p_header.match(line)
                continue
            # -------------------------------------------------------------------------------------------------------------------------
            elif p_delimiter.match(line):
                match = p_delimiter.match(line)
                continue
            # 58bf.ea72.1730 a2-11-cap43                   17   Run                11ac     Dot1x
            elif p_client_info.match(line):
                match = p_client_info.match(line)
                groups = match.groupdict()
                mac_address = groups['mac']
                ap_name = groups['name']
                wlan = groups['wlan']
                state = groups['state'].strip()
                protocol = groups['protocol']
                method = groups['method']
                if not show_wireless_fabric_client_summary_dict.get('clients'):
                    show_wireless_fabric_client_summary_dict['clients'] = {}
                client_index += 1
                show_wireless_fabric_client_summary_dict['clients'].update({client_index : {}})
                show_wireless_fabric_client_summary_dict['clients'][client_index].update({'mac_address' : mac_address})
                show_wireless_fabric_client_summary_dict['clients'][client_index].update({'ap_name' : ap_name})
                show_wireless_fabric_client_summary_dict['clients'][client_index].update({'wlan' : wlan})
                show_wireless_fabric_client_summary_dict['clients'][client_index].update({'state' : state})
                show_wireless_fabric_client_summary_dict['clients'][client_index].update({'protocol' : protocol})
                show_wireless_fabric_client_summary_dict['clients'][client_index].update({'method' : method})

        return show_wireless_fabric_client_summary_dict