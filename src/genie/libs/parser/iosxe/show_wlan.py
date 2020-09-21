import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ==============================
# Schema for:
#  * 'show wlan id client stats'
# ==============================
class ShowWlanIdClientStatsSchema(MetaParser):
    """Schema for show wlan id client stats."""

    schema = {}


# ==============================
# Parser for:
#  * 'show wlan id client stats'
# ==============================
class ShowWlanIdClientStats(ShowWlanIdClientStatsSchema):
    """Parser for show wlan id client stats"""

    cli_command = ["show wlan id client stats"]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        else:
            output = output

        wlan_capture = (
            # Wlan Profile Name: lizzard_Global, Wlan Id: 17
            r"^Wlan Profile Name:\s+(?P<profile_name>\S+), Wlan Id: (?P<id>\d+)$"
        )

        # Current client state statistics:
        client_stats_capture = (
            r"^"
            #   Authenticating         : 7
            r"\s+Authenticating\s+:\s+(?P<auth>\d+)\n+"
            #   Mobility               : 0
            r"\s+Mobility\s+:\s+(?P<mobility>\d+)\n+"
            #   IP Learn               : 0
            r"\s+IP Learn\s+:\s+(?P<ip_learn>\d+)\n+"
            #   Webauth Pending        : 0
            r"\s+Webauth Pending\s+:\s+(?P<webauth>\d+)\n+"
            #   Run                    : 2
            r"\s+Run\s+:\s+(?P<run>\d+)\n+"
        )

        # Total client delete reasons
        client_delete_capture = (
            r"^"
            # No Operation                                                    : 0
            r"\s+No Operation\s+:\s+(?P<no_operation>\d+)\n+"
            # Internal error                                                  : 0
            r"\s+Internal error\s+:\s+(?P<internal_error>\d+)\n+"
            # Deauthentication or disassociation request                      : 0
            r"\s+Deauthentication or disassociation request\s+:\s+(?P<deauth_request>\d+)\n+"
            # Session Manager                                                 : 0
            r"\s+Session Manager\s+:\s+(?P<session_manager>\d+)\n+"
            # L3 authentication failure                                       : 0
            r"\s+L3 authentication failure\s+:\s+(?P<l3_auth_fail>\d+)\n+"
            # Delete received from AP                                         : 0
            r"\s+Delete received from AP\s+:\s+(?P<ap_delete>\d+)\n+"
            # BSSID down                                                      : 1
            r"\s+BSSID down\s+:\s+(?P<bssid_down>\d+)\n+"
            # AP down/disjoin                                                 : 2
            r"\s+AP down/disjoin\s+:\s+(?P<ap_down>\d+)\n+"
            # Connection timeout                                              : 0
            r"\s+Connection timeout\s+:\s+(?P<connection_timeout>\d+)\n+"
            # MAC authentication failure                                      : 0
            r"\s+MAC authentication failure\s+:\s+(?P<mac_auth_fail>\d+)\n+"
            # Datapath plumb                                                  : 0
            r"\s+Datapath plumb\s+:\s+(?P<datapath_plumb>\d+)\n+"
            # Due to SSID change                                              : 163
            r"\s+Due to SSID change\s+:\s+(?P<ssid_change>\d+)\n+"
            # Due to VLAN change                                              : 0
            r"\s+Due to VLAN change\s+:\s+(?P<vlan_change>\d+)\n+"
            # Due to IP Zone change                                              : 0
            r"\s+Due to IP Zone change\s+:\s+(?P<ip_zone_change>\d+)\n+"
            # Admin deauthentication                                          : 0
            r"\s+Admin deauthentication\s+:\s+(?P<admin_deauth>\d+)\n+"
            # QoS failure                                                     : 0
            r"\s+QoS failure\s+:\s+(?P<qos_fail>\d+)\n+"
            # WPA key exchange timeout                                        : 13
            r"\s+WPA key exchange timeout\s+:\s+(?P<wpa_key_timeout>\d+)\n+"
            # WPA group key update timeout                                    : 101
            r"\s+WPA group key update timeout\s+:\s+(?P<wpa_groupkey_timeout>\d+)\n+"
            # 802.11w MAX SA queries reached                                  : 0
            r"\s+802.11w MAX SA queries reached\s+:\s+(?P<sa_queries_reached>\d+)\n+"
            # Client deleted during HA recovery                               : 0
            r"\s+Client deleted during HA recovery\s+:\s+(?P<ha_recovery>\d+)\n+"
            # Client blacklist                                                : 0
            r"\s+Client blacklist\s+:\s+(?P<blacklist>\d+)\n+"
        )
