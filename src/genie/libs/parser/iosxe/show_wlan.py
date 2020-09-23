import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ======================
# Schema for:
#  * 'show wlan summary'
# ======================
class ShowWlanSummarySchema(MetaParser):
    """Schema for show wlan summary."""

    schema = {
        "wlan_summary": {
            "wlan_count": int,
            "wlan_id": {
                int: {
                    "profile_name": str,
                    "ssid": str,
                    "status": str,
                    "security": str
                }
            }
        }
    }


# ======================
# Parser for:
#  * 'show wlan summary'
# ======================
class ShowWlanSummary(ShowWlanSummarySchema):
    """Parser for show wlan summary"""

    cli_command = 'show ap cdp neighbor'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        wlan_summary_dict = {}

        # Number of WLANs: 4
        #
        # ID   Profile Name                     SSID                             Status Security
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 17   lizzard_Global                  lizzard                         UP     [WPA2][802.1x][FT + 802.1x][AES],[FT Enabled]
        # 18   wip_Global                      wip                             UP     [WPA2][802.1x + CCKM][AES]
        # 19   internet_Global                  internet                         UP     [open],MAC Filtering
        # 20   lizzard-l_Global                lizzard-legacy                  UP     [WPA2][802.1x][AES]

        # Number of WLANs: 4
        wlan_count_capture = re.compile(r"^Number\s+of\s+WLANs:\s+(?P<wlan_count>\d+)$")
        # ID   Profile Name                     SSID                             Status Security
        wlan_info_header_capture = re.compile(r"^ID\s+Profile\s+Name\s+SSID\s+Status\s+Security$")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        delimiter_capture = re.compile(
            r"^----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------$")
        # 17   lizzard_Global                  lizzard                         UP     [WPA2][802.1x][FT + 802.1x][AES],[FT Enabled]
        wlan_info_capture = re.compile(
            r"^(?P<wlan_id>\d+)\s+(?P<profile_name>\S+)\s+(?P<ssid>\S+)\s+(?P<wlan_status>\S+)\s+(?P<status_security>.*$)")

        for line in out.splitlines():
            line = line.strip()
            # Number of WLANs: 4
            if wlan_count_capture.match(line):
                wlan_count_capture_match = wlan_count_capture.match(line)
                groups = wlan_count_capture_match.groupdict()
                if not wlan_summary_dict.get('wlan_summary', {}):
                    wlan_summary_dict['wlan_summary'] = {}
                wlan_count = int(groups['wlan_count'])
                wlan_summary_dict['wlan_summary']['wlan_count'] = wlan_count
                continue
            # ID   Profile Name                     SSID                             Status Security
            elif wlan_info_header_capture.match(line):
                wlan_info_header_capture_match = wlan_info_header_capture.match(line)
                groups = wlan_info_header_capture_match.groupdict()
                continue
            # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            elif delimiter_capture.match(line):
                delimiter_capture_match = delimiter_capture.match(line)
                groups = delimiter_capture_match.groupdict()
                continue
            # 17   lizzard_Global                  lizzard                         UP     [WPA2][802.1x][FT + 802.1x][AES],[FT Enabled]
            elif wlan_info_capture.match(line):
                wlan_info_capture_match = wlan_info_capture.match(line)
                groups = wlan_info_capture_match.groupdict()
                wlan_id = int(groups['wlan_id'])
                profile_name = groups['profile_name']
                ssid = groups['ssid']
                wlan_status = groups['wlan_status']
                status_security = groups['status_security']
                if not wlan_summary_dict['wlan_summary'].get('wlan_id', {}):
                    wlan_summary_dict['wlan_summary']['wlan_id'] = {}
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id] = {}
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'profile_name': profile_name})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'ssid': ssid})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'status': wlan_status})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'security': status_security})
                continue

        return wlan_summary_dict

