import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or

# ====================
# Schema for:
#  * 'show ap summary'
# ====================
class ShowApSummarySchema(MetaParser):
    """Schema for show ap summary."""

    schema = {
        "ap_neighbor_count": int,
        "ap_name": {
            str: {
                "slots_count": int,
                "ap_model": str,
                "ethernet_mac": str,
                "radio_mac": str,
                "location": str,
                "country": str,
                "ap_ip_address": str,
                "state": str
            }
        }
    }

# ====================
# Parser for:
#  * 'show ap summary'
# ====================
class ShowApSummary(ShowApSummarySchema):
    """Parser for show ap summary"""

    cli_command = 'show ap summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ap_summary_dict = {}
        # Number of APs: 149
        #
        # AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # a121-cap22                       2      9130AXI   a4b2.32ff.2db9  2c57.41ff.b979  Fab A  UK          10.6.33.106                               Registered
        # a132-cap15                       2      9130AXI   a4b2.32ff.b3d5  2c57.41ff.f2c0  Fab A  UK          10.6.32.146                               Registered
        # a111-cap27                       2      9130AXI   a4b2.32ff.b3ed  2c57.41ff.f380  Fab A  UK          10.6.32.118.                              Registered
        # a112-cap11                       2      9130AXI   a4b2.32ff.b362  2c57.41ff.f720  Fab A  UK          10.6.33.160                               Registered
        # a112-cap10                       2      9130AXI   a4b2.32ff.b5b1  2c57.41ff.d1a0  Fab A  UK          10.6.33.102                               Registered
        # a112-cap17                       2      9130AXI   a4b2.32ff.b5c5  2c57.41ff.d240  Fab A  UK          10.6.32.203                               Registered
        # a112-cap14                       2      9130AXI   a4b2.32ff.b5c9  2c57.41ff.d260  Fab A  UK          10.6.32.202                               Registered
        # a122-cap09                       2      9130AXI   a4b2.32ff.b5e1  2c57.41ff.d320  Fab A  UK          10.6.33.133                               Registered
        # a131-cap43                       2      9130AXI   a4b2.32ff.b5e5  2c57.41ff.d340  Fab A  UK          10.6.33.93                                Registered
        # a122-cap08                       2      9130AXI   a4b2.32ff.b5e9  2c57.41ff.d360  Fab A  UK          10.6.32.166                               Registered

        # Number of APs: 149
        ap_neighbor_count_capture = re.compile(r"^Number\s+of\s+APs:\s+(?P<ap_neighbor_count>\d+)")

        # AP002C.C862.E708  2      AIR-AP1815I-A-K9      002c.c862.e708  002c.c88a.fd20  default location    US    9.4.57.241    Registered
        ap_neighbor_info_capture = re.compile(
               r"^(?P<ap_name>\S+)\s+(?P<slots_count>\d+)\s+(?P<ap_model>\S+)\s+" 
               "(?P<ethernet_mac>\S+)\s+(?P<radio_mac>\S+)\s+(?P<location>.*)\s+" 
               "(?P<country>\S+)\s+(?P<ap_ip_address>\d+\.\d+\.\d+\.\d+)\s+" 
               "(?P<state>(Registered))")

        remove_lines = ('AP Name', '----')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out_filter = filter_lines(raw_output=out, remove_lines=remove_lines)

        ap_summary_data = {}

        for line in out_filter:
            # Number of APs: 149
            if ap_neighbor_count_capture.match(line):
                ap_neighbor_count_match = ap_neighbor_count_capture.match(line)
                groups = ap_neighbor_count_match.groupdict()
                ap_neighbor_count = int(groups['ap_neighbor_count'])
                ap_summary_dict['ap_neighbor_count'] = ap_neighbor_count
            # a121-cap22                       2      9130AXI   a4b2.32ff.2db9  2c57.41ff.b979  Fab A  UK          10.6.33.106                               Registered
            elif ap_neighbor_info_capture.match(line):
                ap_neighbor_info_match = ap_neighbor_info_capture.match(line)
                groups = ap_neighbor_info_match.groupdict()
                # ap name is the key to place all the ap neighbor info
                ap_name = ''
                # Loop over all regex matches found
                for k, v in groups.items():
                    # If the key value is ap_name, update the outer ap_name variable with the ap_name regex match
                    if k == 'ap_name':
                        ap_name = v
                    else:
                        # ap_model can sometimes be a digit e.g., '4800'. This needs to be a string.
                        if k != 'ap_model' and v.isdigit():
                            v = int(v)
                        elif str(v):
                            # The location value can be any value as a string but need to strip the whitespace
                            v = v.strip()
                        if not ap_summary_dict.get("ap_name", {}):
                            ap_summary_dict["ap_name"] = {}
                        ap_summary_dict['ap_name'][ap_name] = {}
                        ap_summary_data.update({k: v})
                ap_summary_dict['ap_name'][ap_name].update(ap_summary_data)
                ap_summary_data = {}
                continue

        return ap_summary_dict


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


# ====================================
# Schema for:
#  * 'show ap dot11 dual-band summary'
# ====================================
class ShowApDot11DualBandSummarySchema(MetaParser):
    """Schema for show ap dot11 dual-band summary."""

    schema = {
        "ap_dot11_dual-band_summary": {
            "index": {
                int: {
                    "ap_name": str,
                    "ap_mac_address": str,
                    "slot_id": int,
                    "admin_state": str,
                    "oper_state": str,
                    "width": int,
                    "tx_pwr": str,
                    "mode": str,
                    "subband": str,
                    "channel": str
                }
            }
        }
    }


# ====================================
# Parser for:
#  * 'show ap dot11 dual-band summary'
# ====================================
class ShowApDot11DualBandSummary(ShowApDot11DualBandSummarySchema):
    """Parser for show ap dot11 dual-band summary"""

    cli_command = 'show ap dot11 dual-band summary'

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # aa-test-4800                 64d8.14ff.fd0d  0     Enabled       Down           20     *1/8 (23 dBm)   Local   All        (6)*
        ap_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<ap_mac_address>\S+)\s+(?P<slot_id>\d+)\s+(?P<admin_state>(Enabled|Disabled))\s+(?P<oper_state>\S+)\s+(?P<width>\d+)\s+(?P<tx_pwr>(N\/A|\*.*m\)))\s+(?P<mode>\S+)\s+(?P<subband>\S+)\s+(?P<channel>\S+)$")

        ap_index = 0

        for line in output.splitlines():
            line = line.strip()

            # aa-test-4800                 64d8.14ff.fd0d  0     Enabled       Down           20     *1/8 (23 dBm)   Local   All        (6)*
            m = ap_info_capture.match(line)
            if m:
                groups = m.groupdict()
                ap_index += 1

                if not ret_dict.get('ap_dot11_dual-band_summary'):
                    ret_dict['ap_dot11_dual-band_summary'] = {"index": {}}
                ret_dict['ap_dot11_dual-band_summary']["index"][ap_index]  = {
                    'ap_name': groups['ap_name'],
                    'ap_mac_address': groups['ap_mac_address'],
                    'slot_id': int(groups['slot_id']),
                    'admin_state': groups['admin_state'],
                    'oper_state': groups['oper_state'],
                    'width': int(groups['width']),
                    'tx_pwr': groups['tx_pwr'],
                    'mode': groups['mode'],
                    'subband': groups['subband'],
                    'channel': groups['channel']
                }

        return ret_dict


# ===============================
# Schema for:
#  * 'show ap dot11 5ghz channel'
# ===============================
class ShowApDot115GhzChannelSchema(MetaParser):
    """Schema for show ap dot11 5ghz channel."""

    schema = {
        "channel_assignment": {
            "chan_assn_mode": str,
            "chan_upd_int": str,
            "anchor_time_hour": int,
            "channel_update_contribution": {
                "channel_noise": "Enable",
                "channel_interference": str,
                "channel_load": str,
                "device_aware": str,
            },
            "clean_air": str,
            Optional("zero_wait"): str,
            "wlc_leader_name": str,
            Optional("wlc_leader_ip"): str,
            Optional("wlc_leader_ipv4"): str,
            Optional("wlc_leader_ipv6"): str,
            "last_run_seconds": int,
            "dca_level": str,
            Optional("dca_aggressive"): str,
            "dca_db": int,
            "chan_width_mhz": Or(int, str),
            "max_chan_width_mhz": Or(int, float),
            "dca_min_energy_dbm": Or(float, int),
            "channel_energy_levels" : {
                "min_dbm": Or(float, int),
                "average_dbm": Or(float, int),
                "max_dbm": Or(float, int),
            },
            "channel_dwell_times": {
                "minimum": str,
                "average": str,
                "max": str,
            },
            "allowed_channel_list": str,
            "unused_channel_list": str,
        }
    }

# ===============================
# Parser for:
#  * 'show ap dot11 5ghz channel'
# ===============================
class ShowApDot115GhzChannel(ShowApDot115GhzChannelSchema):
    """Parser for show ap dot11 5ghz channel"""

    cli_command = 'show ap dot11 5ghz channel'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        show_ap_dot11_5ghz_channel_dict = {}

        # Leader Automatic Channel Assignment
        #   Channel Assignment Mode                    : AUTO
        #   Channel Update Interval                    : 12 Hours
        #   Anchor time (Hour of the day)              : 7
        #   Channel Update Contribution
        #     Noise                                    : Enable
        #     Interference                             : Enable
        #     Load                                     : Disable
        #     Device Aware                             : Disable
        #   CleanAir Event-driven RRM option           : Disabled
        #   Channel Assignment Leader                  : sj-00a-ewlc (9.4.62.51) (2001:9:4:62::51)
        #   Last Run                                   : 15995 seconds ago
        #
        #   DCA Sensitivity Level                      : MEDIUM : 15 dB
        #   DCA 802.11n/ac Channel Width               : 80 MHz
        #   DBS Max Channel Width                      : 80 MHz
        #   DCA Minimum Energy Limit                   : -95 dBm
        #   Channel Energy Levels
        #     Minimum                                  : -94 dBm
        #     Average                                  : -82 dBm
        #     Maximum                                  : -81 dBm
        #   Channel Dwell Times
        #     Minimum                                  : 2 days 21 hours 20 minutes 14 seconds 
        #     Average                                  : 4 days 6 hours 26 minutes 41 seconds 
        #     Maximum                                  : 4 days 17 hours 41 minutes 1 second  
        #   802.11a 5 GHz Auto-RF Channel List
        #     Allowed Channel List                     : 36,40,44,48,149,153,157,161 
        #     Unused Channel List                      : 52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,165,169,173 

        lead_auto_chan_assn_capture = re.compile(r"^Leader\s+Automatic\s+Channel\s+Assignment$")
        #   Channel Assignment Mode                    : AUTO
        chan_assn_mode_capture = re.compile(r"^Channel\s+Assignment\s+Mode\s+:\s+(?P<chan_assn_mode>\S+)")
        #   Channel Update Interval                    : 12 Hours
        chan_update_int_capture = re.compile(r"^Channel\s+Update\s+Interval\s+:\s+(?P<chan_upd_int>.*)$")
        #   Anchor time (Hour of the day)              : 7
        anchor_time_capture = re.compile(
            r"^Anchor\s+time\s+\(Hour\s+of\s+the\s+day\)\s+:\s+(?P<anchor_time_hour>\d+)$")
        #   Channel Update Contribution
        chan_upd_cont_capture = re.compile(r"^Channel\s+Update\s+Contribution$")
        #     Noise                                    : Enable
        channel_noise_capture = re.compile(r"^Noise\s+:\s+(?P<channel_noise>(Enable|Disable))$")
        #     Interference                             : Enable
        channel_interference_capture = re.compile(r"^Interference\s+:\s+(?P<channel_interference>(Enable|Disable))$")
        #     Load                                     : Disable
        channel_load_capture = re.compile(r"^Load\s+:\s+(?P<channel_load>(Enable|Disable))$")
        #     Device Aware                             : Disable
        device_aware_capture = re.compile(r"^Device\s+Aware\s+:\s+(?P<device_aware>(Enable|Disable))$")
        #   CleanAir Event-driven RRM option           : Disabled
        clean_air_capture = re.compile(
            r"^CleanAir\s+Event-driven\s+RRM\s+option\s+:\s+(?P<clean_air>(Enabled|Disabled))$")
        #   Channel Assignment Leader                  : sj-00a-ewlc1 (10.7.5.133)
        #   Channel Assignment Leader                  : vidya-ewlc-5 (9.4.62.51) (2001:9:4:62::51) 
        chan_assn_leader_capture = re.compile('^Channel\s+Assignment\s+Leader\s+:\s+(?P<wlc_leader_name>\S+)\s+((?P<wlc_leader_ip>\(\d+\.\d+\.\d+\.\d+\))|(?P<wlc_leader_ipv4>\(\d+\.\d+\.\d+\.\d+\))\s+(?P<wlc_leader_ipv6>\(\d+\:\d+\:\d+\:\d+\::\d+\)))$')
        #   Last Run                                   : 15995 seconds ago
        last_run_capture = re.compile(r"^Last\s+Run\s+:\s+(?P<last_run_seconds>\d+)\s+seconds\s+ago$")
        #   DCA Sensitivity Level                      : MEDIUM : 15 dB
        dca_sensitivity_capture = re.compile(
            r"^DCA\s+Sensitivity\s+Level\s+:\s+(?P<dca_level>\S+)\s+:\s+(?P<dca_db>\d+)\s+dB$")
        #   DCA 802.11n/ac Channel Width               : 80 MHz
        #   DCA 802.11n/ac Channel Width               : best 
        dca_chan_width_capture = re.compile(r"^DCA\s+802\.11n\/ac\s+Channel\s+Width\s+:\s+((?P<chan_width>(\d+\S+|\S+)))")
        #   DBS Max Channel Width                      : 80 MHz
        dbs_max_chan_width_capture = re.compile(
            r"^DBS\s+Max\s+Channel\s+Width\s+:\s+(?P<max_chan_width>\d+)\s+MHz$")
        #   DCA Minimum Energy Limit                   : -95 dBm
        dca_min_energy_capture = re.compile(
            r"^DCA\s+Minimum\s+Energy\s+Limit\s+:\s+(?P<dca_min_energy_dbm>\S+)\s+dBm$")
        #   Channel Energy Levels
        chan_energy_levels_capture = re.compile(r"^Channel\s+Energy\s+Levels$")
        #     Minimum                                  : -94 dBm
        chan_energy_min_capture = re.compile(r"^Minimum\s+:\s+(?P<chan_energy_min_dbm>\S+)\s+dBm")
        #     Average                                  : -82 dBm
        chan_energy_average_capture = re.compile(r"^Average\s+:\s+(?P<chan_energy_average_dbm>\S+)\s+dBm")
        #     Maximum                                  : -81 dBm
        chan_energy_max_capture = re.compile(r"^Maximum\s+:\s+(?P<chan_energy_max_dbm>\S+)\s+dBm")
        #   Channel Dwell Times
        chan_dwell_times_capture = re.compile(r"^Channel\s+Dwell\s+Times$")
        #     Minimum                                  : 4 hours 9 minutes 54 seconds
        #     Minimum                                  : 2 days 2 hours 52 minutes 25 seconds 
        chan_dwell_minimum_capture = re.compile(r"^Minimum\s+:\s+((?P<chan_dwell_min_days>\d+)\s+(day|days)\s+)?((?P<chan_dwell_min_hours>\d+)\s+(hour|hours)\s+)?((?P<chan_dwell_min_minutes>\d+)\s+(minute|minutes)\s+)?(?P<chan_dwell_min_seconds>\d+)\s+(second|seconds)$")
        #     Average                                  : 4 hours 24 minutes 54 seconds
        #     Average                                  : 3 days 11 hours 58 minutes 52 seconds 
        chan_dwell_average_capture = re.compile(  r"^Average\s+:\s+((?P<chan_dwell_average_days>\d+)\s+(day|days)\s+)?((?P<chan_dwell_average_hours>\d+)\s+(hour|hours)\s+)?((?P<chan_dwell_average_minutes>\d+)\s+(minute|minutes)\s+)?(?P<chan_dwell_average_second>\d+)\s+(second|seconds)$")
        #     Maximum                                  : 4 hours 26 minutes 35 seconds
        #     Maximum                                  : 3 days 23 hours 13 minutes 12 seconds 
        chan_dwell_max_capture = re.compile(r"^Maximum\s+:\s+((?P<chan_dwell_max_days>\d+)\s+(day|days)\s+)?((?P<chan_dwell_max_hours>\d+)\s+(hour|hours)\s+)?((?P<chan_dwell_max_minutes>\d+)\s+(minute|minutes)\s+)?(?P<chan_dwell_max_seconds>\d+)\s+(second|seconds)$")

        # 802.11a 5 GHz Auto-RF Channel List
        channel_list_capture = re.compile(r"^802.11a\s+5\s+GHz\s+Auto-RF\s+Channel\s+List$")
        # Allowed Channel List             : 36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161
        allowed_channel_list_capture = re.compile(r"^Allowed\s+Channel\s+List\s+:\s+(?P<allowed_channel_list>\S+)$")
        # Unused Channel List              : 52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,165,169,173 
        unused_channel_list_capture = re.compile(r"^Unused\s+Channel\s+List\s+:\s+(?P<unused_channel_list>\S+)$") 
        # Zero Wait DFS                    : Disabled 
        zero_wait_capture = re.compile(r"^Zero\s+Wait\s+DFS\s+:\s+(?P<zero_wait>(Enabled|Disabled))$") 
        # DCA Aggressive Remaining Cycle   : 6(60 minutes)
        dca_aggressive_capture = re.compile(r"^DCA\s+Aggressive\s+Remaining\s+Cycle\s+:\s+(?P<dca_aggressive>\S+\s+\w+\S)") 


        def change_data_type(value):
            if value.isdigit():
                value = value.strip()
                value = int(value)
            else:
                try:
                    # Change strings to float if possible
                    value = float(value)
                except ValueError:
                    # if the value is not an int or float, leave it as a string.
                    pass
            return value

        for line in out.splitlines():
            line = line.strip()
            # Leader Automatic Channel Assignment
            if lead_auto_chan_assn_capture.match(line):
                lead_auto_chan_assn_capture_match = lead_auto_chan_assn_capture.match(line)
                groups = lead_auto_chan_assn_capture_match.groupdict()
                if not show_ap_dot11_5ghz_channel_dict.get('channel_assignment', {}):
                    show_ap_dot11_5ghz_channel_dict['channel_assignment'] = {}
                continue
            #   Channel Assignment Mode                    : AUTO
            elif chan_assn_mode_capture.match(line):
                chan_assn_mode_capture_match = chan_assn_mode_capture.match(line)
                groups = chan_assn_mode_capture_match.groupdict()
                chan_assn_mode = groups['chan_assn_mode']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'chan_assn_mode': chan_assn_mode})
                continue
            #   Channel Update Interval                    : 12 Hours
            elif chan_update_int_capture.match(line):
                chan_update_int_capture_match = chan_update_int_capture.match(line)
                groups = chan_update_int_capture_match.groupdict()
                chan_upd_int = change_data_type(groups['chan_upd_int'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'chan_upd_int': chan_upd_int})
                continue
            #   Anchor time (Hour of the day)              : 7
            elif anchor_time_capture.match(line):
                anchor_time_capture_match = anchor_time_capture.match(line)
                groups = anchor_time_capture_match.groupdict()
                anchor_time_hour = change_data_type(groups['anchor_time_hour'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'anchor_time_hour': anchor_time_hour})
                continue
            #   Channel Update Contribution
            elif chan_upd_cont_capture.match(line):
                chan_upd_cont_capture_match = chan_upd_cont_capture.match(line)
                groups = chan_upd_cont_capture_match.groupdict()
                if not show_ap_dot11_5ghz_channel_dict["channel_assignment"].get("channel_update_contribution", {}):
                    show_ap_dot11_5ghz_channel_dict["channel_assignment"].update({"channel_update_contribution" : {} })
                continue
            #     Noise                                    : Enable
            elif channel_noise_capture.match(line):
                channel_noise_capture_match = channel_noise_capture.match(line)
                groups = channel_noise_capture_match.groupdict()
                channel_noise = groups['channel_noise']
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_update_contribution"].update({'channel_noise': channel_noise})
                continue
            #     Interference                             : Enable
            elif channel_interference_capture.match(line):
                channel_interference_capture_match = channel_interference_capture.match(line)
                groups = channel_interference_capture_match.groupdict()
                channel_interference = groups['channel_interference']
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_update_contribution"].update(
                    {'channel_interference': channel_interference})
                continue
                #     Load                                     : Disable
            elif channel_load_capture.match(line):
                channel_load_capture_match = channel_load_capture.match(line)
                groups = channel_load_capture_match.groupdict()
                channel_load = groups['channel_load']
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_update_contribution"].update({'channel_load': channel_load})
                continue
            #     Device Aware                             : Disable
            elif device_aware_capture.match(line):
                device_aware_capture_match = device_aware_capture.match(line)
                groups = device_aware_capture_match.groupdict()
                device_aware = groups['device_aware']
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_update_contribution"].update({'device_aware': device_aware})
                continue
            #   CleanAir Event-driven RRM option           : Disabled
            elif clean_air_capture.match(line):
                clean_air_capture_match = clean_air_capture.match(line)
                groups = clean_air_capture_match.groupdict()
                clean_air = groups['clean_air']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'clean_air': clean_air})
                continue
            #  Zero Wait DFS                              : Disabled 
            elif zero_wait_capture.match(line):
                zero_wait_capture_match = zero_wait_capture.match(line)
                groups = zero_wait_capture_match.groupdict()
                zero_wait = groups['zero_wait']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'zero_wait': zero_wait})
                continue
            #   Channel Assignment Leader                  : sj-00a-ewlc1 (10.7.5.133)
            #   Channel Assignment Leader                  : vidya-ewlc-5 (9.4.62.51) (2001:9:4:62::51) 
            elif chan_assn_leader_capture.match(line):
                chan_assn_leader_capture_match = chan_assn_leader_capture.match(line)
                groups = chan_assn_leader_capture_match.groupdict()
                wlc_leader_name = groups['wlc_leader_name']
                wlc_leader_ip = groups['wlc_leader_ip']
                wlc_leader_ipv4 = groups['wlc_leader_ipv4']
                wlc_leader_ipv6 = groups['wlc_leader_ipv6']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'wlc_leader_name': wlc_leader_name})
                if wlc_leader_ipv6:
                    show_ap_dot11_5ghz_channel_dict['channel_assignment'].update(
                        {'wlc_leader_ipv4': wlc_leader_ipv4.replace('(', '').replace(')', '')})
                    show_ap_dot11_5ghz_channel_dict['channel_assignment'].update(
                        {'wlc_leader_ipv6': wlc_leader_ipv6.replace('(', '').replace(')', '')})
                else:
                    show_ap_dot11_5ghz_channel_dict['channel_assignment'].update(
                        {'wlc_leader_ip': wlc_leader_ip.replace('(', '').replace(')', '')})
                continue
            #   Last Run                                   : 15995 seconds ago
            elif last_run_capture.match(line):
                last_run_capture_match = last_run_capture.match(line)
                groups = last_run_capture_match.groupdict()
                last_run_seconds = change_data_type(groups['last_run_seconds'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'last_run_seconds': last_run_seconds})
                continue
            #   DCA Sensitivity Level                      : MEDIUM : 15 dB
            elif dca_sensitivity_capture.match(line):
                dca_sensitivity_capture_match = dca_sensitivity_capture.match(line)
                groups = dca_sensitivity_capture_match.groupdict()
                dca_level = groups['dca_level']
                dca_db = change_data_type(groups['dca_db'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'dca_level': dca_level})
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'dca_db': dca_db})
                continue
            #  DCA Aggressive Remaining Cycle             : 6(60 minutes)
            elif dca_aggressive_capture.match(line):
                dca_aggressive_capture_match = dca_aggressive_capture.match(line)
                groups = dca_aggressive_capture_match.groupdict()
                dca_aggressive = groups['dca_aggressive']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'dca_aggressive': dca_aggressive})
                continue
            #   DCA 802.11n/ac Channel Width               : 80 MHz
            #   DCA 802.11n/ac Channel Width               : best 
            elif dca_chan_width_capture.match(line):
                dca_chan_width_capture_match = dca_chan_width_capture.match(line)
                groups = dca_chan_width_capture_match.groupdict()
                chan_width = change_data_type(groups['chan_width'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'chan_width_mhz': chan_width})
                continue
            #   DBS Max Channel Width                      : 80 MHz
            elif dbs_max_chan_width_capture.match(line):
                dbs_max_chan_width_capture_match = dbs_max_chan_width_capture.match(line)
                groups = dbs_max_chan_width_capture_match.groupdict()
                max_chan_width = change_data_type(groups['max_chan_width'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'max_chan_width_mhz': max_chan_width})
                continue
            #   DCA Minimum Energy Limit                   : -95 dBm
            elif dca_min_energy_capture.match(line):
                dca_min_energy_capture_match = dca_min_energy_capture.match(line)
                groups = dca_min_energy_capture_match.groupdict()
                dca_min_energy_dbm = change_data_type(groups['dca_min_energy_dbm'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'dca_min_energy_dbm': dca_min_energy_dbm})
                continue
            #   Channel Energy Levels
            elif chan_energy_levels_capture.match(line):
                chan_energy_levels_capture_match = chan_energy_levels_capture.match(line)
                groups = chan_energy_levels_capture_match.groupdict()
                if not show_ap_dot11_5ghz_channel_dict["channel_assignment"].get("channel_energy_levels", {}):
                    show_ap_dot11_5ghz_channel_dict["channel_assignment"].update({"channel_energy_levels" : {}})
                continue
            #     Minimum                                  : -94 dBm
            elif chan_energy_min_capture.match(line):
                chan_energy_min_capture_match = chan_energy_min_capture.match(line)
                groups = chan_energy_min_capture_match.groupdict()
                chan_energy_min_dbm = change_data_type(groups['chan_energy_min_dbm'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_energy_levels"].update(
                    {'min_dbm': chan_energy_min_dbm})
                continue
            #     Average                                  : -82 dBm
            elif chan_energy_average_capture.match(line):
                chan_energy_average_capture_match = chan_energy_average_capture.match(line)
                groups = chan_energy_average_capture_match.groupdict()
                chan_energy_average_dbm = change_data_type(groups['chan_energy_average_dbm'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_energy_levels"].update(
                    {'average_dbm': chan_energy_average_dbm})
                continue
            #     Maximum                                  : -81 dBm
            elif chan_energy_max_capture.match(line):
                chan_energy_max_capture_match = chan_energy_max_capture.match(line)
                groups = chan_energy_max_capture_match.groupdict()
                chan_energy_max_dbm = change_data_type(groups['chan_energy_max_dbm'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_energy_levels"].update(
                    {'max_dbm': chan_energy_max_dbm})
                continue
            #   Channel Dwell Times
            elif chan_dwell_times_capture.match(line):
                chan_dwell_times_capture_match = chan_dwell_times_capture.match(line)
                groups = chan_dwell_times_capture_match.groupdict()
                if not show_ap_dot11_5ghz_channel_dict["channel_assignment"].get("channel_dwell_times", {}):
                    show_ap_dot11_5ghz_channel_dict["channel_assignment"].update({ "channel_dwell_times" : {} })
                continue
            #     Minimum                                  : 4 hours 9 minutes 54 seconds
            #     Minimum                                  : 2 days 21 hours 20 minutes 14 seconds  
            elif chan_dwell_minimum_capture.match(line):
                chan_dwell_minimum_capture_match = chan_dwell_minimum_capture.match(line)
                groups = chan_dwell_minimum_capture_match.groupdict()
                chan_dwell_min_days = groups['chan_dwell_min_days']
                chan_dwell_min_hours = groups['chan_dwell_min_hours']
                chan_dwell_min_minutes = groups['chan_dwell_min_minutes']
                chan_dwell_min_seconds = groups['chan_dwell_min_seconds']
                if chan_dwell_min_days:
                    chan_dwell_minimum = chan_dwell_min_days + ' days ' + chan_dwell_min_hours + ' hours ' + chan_dwell_min_minutes + ' minutes ' + chan_dwell_min_seconds + ' seconds'

                elif chan_dwell_min_hours:
                    chan_dwell_minimum = chan_dwell_min_hours + ' hours ' + chan_dwell_min_minutes + ' minutes ' + chan_dwell_min_seconds + ' seconds'
                elif chan_dwell_min_minutes:
                    chan_dwell_minimum = chan_dwell_min_minutes + ' minutes ' + chan_dwell_min_seconds + ' seconds'
                else:
                    chan_dwell_minimum = chan_dwell_min_seconds + ' seconds'
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_dwell_times"].update({'minimum': chan_dwell_minimum})
                continue
            #     Average                                  : 4 hours 24 minutes 54 seconds
            #     Average                                  : 4 days 6 hours 26 minutes 41 seconds 
            elif chan_dwell_average_capture.match(line):
                chan_dwell_average_capture_match = chan_dwell_average_capture.match(line)
                groups = chan_dwell_average_capture_match.groupdict()
                chan_dwell_average_days = groups['chan_dwell_average_days']
                chan_dwell_average_hours = groups['chan_dwell_average_hours']
                chan_dwell_average_minutes = groups['chan_dwell_average_minutes']
                chan_dwell_average_seconds = groups['chan_dwell_average_second']
                if chan_dwell_average_days:
                    chan_dwell_average = chan_dwell_average_days + ' days ' + chan_dwell_average_hours + ' hours ' + chan_dwell_average_minutes + ' minutes ' + chan_dwell_average_seconds + ' seconds'
                elif chan_dwell_average_hours:
                    chan_dwell_average = chan_dwell_average_hours + ' hours ' + chan_dwell_average_minutes + ' minutes ' + chan_dwell_average_seconds + ' seconds'
                elif chan_dwell_average_minutes:
                    chan_dwell_average = chan_dwell_average_minutes + ' minutes ' + chan_dwell_average_seconds + ' seconds'
                else:
                    chan_dwell_average = chan_dwell_average_seconds + ' seconds'
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_dwell_times"].update({'average': chan_dwell_average})
                continue
            #     Maximum                                  : 4 hours 26 minutes 35 seconds
            #     Maximum                                  : 4 days 17 hours 41 minutes 1 second  
            elif chan_dwell_max_capture.match(line):
                chan_dwell_max_capture_match = chan_dwell_max_capture.match(line)
                groups = chan_dwell_max_capture_match.groupdict()
                chan_dwell_max_days = groups['chan_dwell_max_days']
                chan_dwell_max_hours = groups['chan_dwell_max_hours']
                chan_dwell_max_minutes = groups['chan_dwell_max_minutes']
                chan_dwell_max_seconds = groups['chan_dwell_max_seconds']
                if chan_dwell_max_days:
                    chan_dwell_max = chan_dwell_max_days + ' days ' + chan_dwell_max_hours + ' hours ' + chan_dwell_max_minutes + ' minutes ' + chan_dwell_max_seconds + ' seconds'
                elif chan_dwell_max_hours:
                    chan_dwell_max = chan_dwell_max_hours + ' hours ' + chan_dwell_max_minutes + ' minutes ' + chan_dwell_max_seconds + ' seconds'
                elif chan_dwell_max_minutes:
                    chan_dwell_max = chan_dwell_max_minutes + ' minutes ' + chan_dwell_max_seconds + ' seconds'
                else:
                    chan_dwell_max = chan_dwell_max_seconds + ' seconds'
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_dwell_times"].update({'max': chan_dwell_max})
                continue
            #   802.11a 5 GHz Auto-RF Channel List
            elif channel_list_capture.match(line):
                channel_list_capture_match = channel_list_capture.match(line)
                groups = channel_list_capture_match.groupdict()
                continue
            # Allowed Channel List             : 36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161
            elif allowed_channel_list_capture.match(line):
                allowed_channel_list_capture_match = allowed_channel_list_capture.match(line)
                groups = allowed_channel_list_capture_match.groupdict()
                allowed_channel_list = groups['allowed_channel_list']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update(
                    {'allowed_channel_list': allowed_channel_list})
                continue
            #     Unused Channel List                      : 52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,165,169,173 
            elif unused_channel_list_capture.match(line):
                unused_channel_list_capture_match = unused_channel_list_capture.match(line)
                groups = unused_channel_list_capture_match.groupdict()
                unused_channel_list = groups['unused_channel_list']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update(
                    {'unused_channel_list': unused_channel_list})
                continue

        return show_ap_dot11_5ghz_channel_dict
        

# ===============================
# Schema for:
#  * 'show ap dot11 5ghz summary'
# ===============================
class ShowApDot115GhzSummarySchema(MetaParser):
    """Schema for show ap dot11 5ghz summary."""

    schema = {
        "ap_name": {
            str: {
                "mac_address": str,
                "slot": int,
                "admin_state": str,
                "oper_state": str,
                "width": int,
                "tx_pwr": str,
                "channel": str,
                Optional("mode"): str      
            }
        } 
    }     


# ===============================
# Parser for:
#  * 'show ap dot11 5ghz summary'
# ===============================
class ShowApDot115GhzSummary(ShowApDot115GhzSummarySchema):
    """Parser for show ap dot11 5ghz summary"""

    cli_command = 'show ap dot11 5ghz summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ap_dot11_5ghz_summ = {}
        # AP Name                       Mac Address     Slot    Admin State    Oper State    Width  Txpwr           Channel   Mode
        # ---------------------------------------------------------------------------------------------------------------------------------
        # ab-1-test-4800                 5c50.15ff.41e1  1       Enabled        Down          20     *1/8 (23 dBm)   (36)*
        # ab21-cap40                    5c50.15ff.dbb6  1       Enabled        Up            20     *7/8 (6 dBm)    (100)*
        # ab12-cap2                     5c50.15ff.7f24  1       Enabled        Up            20     *7/8 (6 dBm)    (116)*
        # ab21-cap36                    5c50.15ff.8be4  1       Enabled        Up            20     *7/8 (6 dBm)    (100)*
        # ab21-cap28                    5c50.15ff.8d24  1       Enabled        Up            20     *7/8 (6 dBm)    (120)*
        # ab31-cap26                    5c50.15ff.8d44  1       Enabled        Up            20     *6/8 (9 dBm)    (128)*
        # ab22-cap16                    5c50.15ff.8da4  1       Enabled        Up            20     *7/8 (8 dBm)    (48)*
        # ab22-cap24                    5c50.15ff.8de4  1       Enabled        Up            20     *7/8 (8 dBm)    (36)*
        # ab22-cap18                    5c50.15ff.8ec4  1       Enabled        Up            20     *7/8 (6 dBm)    (124)*
        # ab32-cap13                    5c50.15ff.8fc4  1       Enabled        Up            20     *6/8 (9 dBm)    (124)*
        #
        # AP Name                       Mac Address     Slot    Admin State    Oper State    Width  Txpwr           Channel     Mode
        # ---------------------------------------------------------------------------------------------------------------------------------
        # ab22-cap10                    5c50.15ff.8fe4  1       Enabled        Up            20     *6/8 (9 dBm)    (132)*
        # BHS-A-204 				    00a7.42ff.d4d0  1 	    Enabled 	   Up 			 20 	 3/7 (12 dBm)   (124)       Local
        # ab11-cap18                    5c50.15ff.9024  1       Enabled        Up            20     *7/8 (8 dBm)    (48)*
        # ab22-cap8                     5c50.15ff.9044  1       Enabled        Up            20     *7/8 (8 dBm)    (149)*
        # ab22-cap22                    5c50.15ff.90e4  1       Enabled        Up            20     *8/8 (5 dBm)    (40)*
        # ab22-cap6                     5c50.15ff.9184  1       Enabled        Up            20     *7/8 (6 dBm)    (100)*
        # ab31-cap29                    5c50.15ff.91c4  1       Enabled        Up            20     *5/8 (12 dBm)   (52)*
        # ab21-cap33                    5c50.15ff.91e4  1       Enabled        Up            20     *7/8 (8 dBm)    (36)*
        # ab31-cap21                    5c50.15ff.9324  1       Enabled        Up            20     *7/8 (6 dBm)    (116)*
        # ab21-cap27                    5c50.15ff.9364  1       Enabled        Up            20     *7/8 (6 dBm)    (132)*
        # ab21-cap35                    5c50.15ff.b0a4  1       Enabled        Up            20     *7/8 (6 dBm)    (140)*

        # AP Name                       Mac Address     Slot    Admin State    Oper State    Width  Txpwr           Channel
        # AP Name                       Mac Address     Slot    Admin State    Oper State    Width  Txpwr           Channel     Mode
        ap_header_capture = re.compile(
            r"^AP\s+Name\s+Mac\s+Address\s+Slot\s+Admin\s+State\s+Oper\s+State\s+Width\s+Txpwr\s+Channel$")
        # ---------------------------------------------------------------------------------------------------------------------------------
        delimiter_capture = re.compile(
            r"^---------------------------------------------------------------------------------------------------------------------------------$")


        # ab22-cap10                   5c50.15ff.8fe4 1       Enabled        Up            20     *6/8 (9 dBm)    (132)*
        # BHS-A-204 				   00a7.42ff.d4d0 1 	  Enabled 		 Up 		   20 	   3/7 (12 dBm)   (124)   Local
        p1 = re.compile(r"^(?P<ap_name>\S+)\s+(?P<mac_address>\S+)\s+"
                                       "(?P<slot>\d+)\s+(?P<admin_state>(Enabled|Disabled))\s+(?P<oper_state>\S+)\s+"
                                       "(?P<width>\d+)\s+(?P<tx_pwr>(\*\d\/\d.*dBm\))|(\d\/\d.*dBm\)))\s+"
                                       "(?P<channel>\S+)\s*(?P<mode>\S+|^.{0}$)?$")

        for line in out.splitlines():
            line = line.strip()

            # ab22-cap10                   5c50.15ff.8fe4 1       Enabled        Up            20     *6/8 (9 dBm)    (132)*
            # BHS-A-204 				   00a7.42ff.d4d0 1 	  Enabled 		 Up 		   20 	   3/7 (12 dBm)   (124)   Local
            if ap_header_capture.match(line):
                continue
            # ---------------------------------------------------------------------------------------------------------------------------------
            elif delimiter_capture.match(line):
                continue

            # ab22-cap10                   5c50.15ff.8fe4 1       Enabled        Up            20     *6/8 (9 dBm)    (132)*
            # BHS-A-204 				   00a7.42ff.d4d0 1 	  Enabled 		 Up 		   20 	   3/7 (12 dBm)   (124)   Local
            elif p1.match(line):
                if not ap_dot11_5ghz_summ.get('ap_name'):
                    ap_dot11_5ghz_summ['ap_name'] = {}
                ap_info_capture_match = p1.match(line)
                groups = ap_info_capture_match.groupdict()
                ap_name = groups['ap_name']
                mac_address = groups['mac_address']
                slot = int(groups['slot'])
                admin_state = groups['admin_state']
                oper_state = groups['oper_state']
                width = int(groups['width'])
                tx_pwr = groups['tx_pwr']
                channel = groups['channel']

                # define ap_name_dict and set ap_name
                ap_name_dict = ap_dot11_5ghz_summ['ap_name'].setdefault(ap_name, {})

                # update ap_name_dict
                ap_name_dict['mac_address'] = mac_address
                ap_name_dict['slot'] = slot
                ap_name_dict['admin_state'] = admin_state
                ap_name_dict['oper_state'] = oper_state
                ap_name_dict['width'] = width
                ap_name_dict['tx_pwr'] = tx_pwr
                ap_name_dict['channel'] = channel

                # assign mode if it is captured in groups otherwise remove it from groups deictionary and set mode to None
                if groups['mode']:
                    mode = groups['mode']
                    ap_name_dict['mode'] = mode
                else:
                    try:
                        del groups['mode']
                        mode = None
                    except: KeyError
                continue

        return ap_dot11_5ghz_summ


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


# =========================================
# Schema for:
#  * 'show ap led-brightness-level summary'
# =========================================
class ShowApLedBrightnessLevelSummarySchema(MetaParser):
    """Schema for show ap led-brightness-level summary."""

    schema = {
        "ap_name": {
            str: {
                "led_brightness_level": int
            }
        }
    }


# =========================================
# Parser for:
#  * 'show ap led-brightness-level summary'
# =========================================
class ShowApLedBrightnessLevelSummary(ShowApLedBrightnessLevelSummarySchema):
    """Parser for show ap led-brightness-level summary"""

    cli_command = 'show ap led-brightness-level summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ap_led_brightness_level_summary_dict = {}

        # AP Name                           LED Brightness level
        # --------------------------------------------------------
        # b881-cap4                     8
        # b852-cap6                     8
        # b861-cap14                    8
        # b822-cap10                    8
        # b871-cap1                     8
        # b861-cap7                     8
        # b852-cap18                    8
        # b871-cap3                     8
        # b862-cap2                     8
        # b801-cap16                    8
        #
        # AP Name                           LED Brightness level
        # --------------------------------------------------------
        # b832-cap3                     8
        # b802-cap4                     8
        # b862-cap5                     8
        # b851-cap9                     8
        # b802-cap8                     8
        # b822-cap14                    8
        # b872-cap8                     8
        # b872-cap6                     8
        # b862-cap18                    8
        # b822-cap16                    8

        # AP Name                           LED Brightness level
        ap_header_capture = re.compile(r"^AP\s+Name\s+LED\s+Brightness\s+level$")
        # --------------------------------------------------------
        delimiter_capture = re.compile(r"^--------------------------------------------------------$")
        # jain-farallon                  8
        ap_info_capture = re.compile(r"^(?P<ap_name>\S+)\s+(?P<led_brightness_level>\d+)$")

        for line in out.splitlines():
            line = line.strip()
            # AP Name                           LED Brightness level
            if ap_header_capture.match(line):
                continue
            # --------------------------------------------------------
            elif delimiter_capture.match(line):
                continue
            # jain-farallon                  8
            elif ap_info_capture.match(line):
                ap_info_capture_match = ap_info_capture.match(line)
                groups = ap_info_capture_match.groupdict()
                ap_name = groups['ap_name']
                led_brightness_level = int(groups['led_brightness_level'])
                if not ap_led_brightness_level_summary_dict.get('ap_name', {}):
                    ap_led_brightness_level_summary_dict['ap_name'] = {}
                ap_led_brightness_level_summary_dict['ap_name'][ap_name] = {
                    'led_brightness_level': led_brightness_level}
                continue

        return ap_led_brightness_level_summary_dict



# =========================================
# Schema for:
#  * 'show ap cdp neighbor'
# =========================================
class ShowApCdpNeighborSchema(MetaParser):
    """Schema for show ap cdp neighbor."""

    schema = {
        "ap_cdp_neighbor_count": int,
        "ap_name": {
            Optional(str): {
                Optional("ap_ip"): str,
                Optional("neighbor_name"): str,
                Optional("neighbor_port"): str,
                Optional("neighbor_ip_count"): int,
                Optional("neighbor_ip_addresses"): list
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
                neighbor_ip_match = neighbor_ip_capture.match(line)
                groups = neighbor_ip_match.groupdict()
                neighbor_ip = groups['neighbor_ip']
                if not ap_cdp_neighbor_dict['ap_name'][ap_name].get('neighbor_ip_addresses', {}):
                    ap_cdp_neighbor_dict['ap_name'][ap_name]['neighbor_ip_addresses'] = []
                ap_cdp_neighbor_dict['ap_name'][ap_name]['neighbor_ip_addresses'].append(neighbor_ip)
                continue

        return ap_cdp_neighbor_dict

# =============================
# Schema for:
#  * 'show ap config general'
# =============================
class ShowApConfigGeneralSchema(MetaParser):
    """Schema for show ap config general."""

    schema = {
        "ap_name": {
            str: {
                Optional("cisco_ap_identifier"): str,
                Optional("country_code"): str,
                Optional("regulatory_domain_allowed_by_country"): str,
                Optional("ap_country_code"): str,
                Optional("ap_regulatory_domain"): {
                    Optional("slot_0"): str,
                    Optional("slot_1"): str,
                },
                Optional("mac_address"): str,
                Optional("ip_address_configuration"): str,
                Optional("ip_address"): str,
                Optional("ip_netmask"): str,
                Optional("gateway_ip_address"): str,
                Optional("fallback_ip_address_being_used"): str,
                Optional("domain"): str,
                Optional("name_server"): str,
                Optional("capwap_path_mtu"): int,
                Optional("capwap_active_window_size"): int,
                Optional("telnet_state"): str,
                Optional("cpu_type"): str,
                Optional("memory_type"): str,
                Optional("memory_size_kb"): int,
                Optional("ssh_state"): str,
                Optional("cisco_ap_location"): str,
                Optional("site_tag_name"): str,
                Optional("rf_tag_name"): str,
                Optional("policy_tag_name"): str,
                Optional("ap_join_profile"): str,
                Optional("flex_profile"): str,
                Optional("ap_filter_name"): str,
                Optional("primary_cisco_controller_name"): str,
                Optional("primary_cisco_controller_ip_address"): str,
                Optional("secondary_cisco_controller_name"): str,
                Optional("secondary_cisco_controller_ip_address"): str,
                Optional("tertiary_cisco_controller_name"): str,
                Optional("tertiary_cisco_controller_ip_address"): str,
                Optional("administrative_state"): str,
                Optional("operation_state"): str,
                Optional("nat_external_ip_address"): str,
                Optional("ap_certificate_type"): str,
                Optional("ap_mode"): str,
                Optional("ap_vlan_tagging_state"): str,
                Optional("ap_vlan_tag"): int,
                Optional("capwap_preferred_mode"): str,
                Optional("capwap_udp_lite"): str,
                Optional("ap_submode"): str,
                Optional("office_extend_mode"): str,
                Optional("dhcp_server"): str,
                Optional("remote_ap_debug"): str,
                Optional("logging_trap_severity_level"): str,
                Optional("logging_syslog_facility"): str,
                Optional("software_version"): str,
                Optional("boot_version"): str,
                Optional("mini_ios_version"): str,
                Optional("stats_reporting_period"): int,
                Optional("led_state"): str,
                Optional("led_flash_state"): str,
                Optional("led_flash_timer"): int,
                Optional("mdns_group_id"): int,
                Optional("mdns_rule_name"): str,
                Optional("poe_pre_standard_switch"): str,
                Optional("poe_power_injector_mac_address"): str,
                Optional("power_type_mode"): str,
                Optional("number_of_slots"): int,
                Optional("ap_model"): str,
                Optional("ios_version"): str,
                Optional("reset_button"): str,
                Optional("ap_serial_number"): str,
                Optional("management_frame_validation"): str,
                Optional("management_frame_protection"): str,
                Optional("ap_user_name"): str,
                Optional("ap_802_1x_user_mode"): str,
                Optional("ap_802_1x_user_name"): str,
                Optional("cisco_ap_system_logging_host"): str,
                Optional("cisco_ap_secured_logging_tls_mode"): str,
                Optional("ap_up_time"): str,
                Optional("ap_capwap_up_time"): str,
                Optional("join_date_and_time"): str,
                Optional("join_taken_time"): str,
                Optional("join_priority"): int,
                Optional("ap_link_latency"): str,
                Optional("ap_lag_configuration_status"): str,
                Optional("lag_support_for_ap"): str,
                Optional("rogue_detection"): str,
                Optional("rogue_containment_auto_rate"): str,
                Optional("rogue_containment_of_standalone_flexconnect_aps"): str,
                Optional("rogue_detection_report_interval"): int,
                Optional("rogue_ap_minimum_rssi"): float,
                Optional("rogue_ap_minimum_transient_time"): int,
                Optional("ap_tcp_mss_adjust"): str,
                Optional("ap_tcp_mss_size"): int,
                Optional("ap_ipv6_tcp_mss_adjust"): str,
                Optional("ap_ipv6_tcp_mss_size"): int,
                Optional("hyperlocation_admin_status"): str,
                Optional("retransmit_count"): int,
                Optional("retransmit_interval"): int,
                Optional("fabric_status"): str,
                Optional("fips_status"): str,
                Optional("wlancc_status"): str,
                Optional("usb_module_type"): str,
                Optional("usb_module_state"): str,
                Optional("usb_operational_state"): str,
                Optional("usb_override"): str,
                Optional("gas_rate_limit_admin_status"): str,
                Optional("wpa3_capability"): str,
                Optional("ewc_ap_capability"): str,
                Optional("awips_capability"): str,
                Optional("proxy_hostname"): str,
                Optional("proxy_port"): str,
                Optional("proxy_no_proxy_list"): str,
                Optional("grpc_server_status"): str,
                Optional("unencrypted_data_keep_alive"): str,
                Optional("local_dhcp_server"): str,
                Optional("traffic_distribution_statistics_capability"): str,
                Optional("dual_dfs_statistics"): str
            }
        }
    }


# ===========================
# Parser for:
#  * 'show ap config general'
# ===========================
class ShowApConfigGeneral(ShowApConfigGeneralSchema):
    """Parser for show ap config general"""

    cli_command = ['show ap name {ap_name} config general','show ap config general']

    def cli(self, ap_name='', output=None):
        if output is None:
            if ap_name:
                cmd = self.cli_command[0].format(ap_name=ap_name)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)	
        else:
            out = output
            
        ap_config_general_dict = {}

        #         Cisco AP Name   : bg-1-cap1
        # =================================================
        #
        # Cisco AP Identifier                             : 70b3.d2ff.59b6
        # Country Code                                    : IN
        # Regulatory Domain Allowed by Country            : 802.11bg:-A   802.11a:-DN
        # AP Country Code                                 : IN  - India
        # AP Regulatory Domain
        #   Slot 0                                        : -A
        #   Slot 1                                        : -D
        # MAC Address                                     : 70b3.17ff.bdcc
        # IP Address Configuration                        : DHCP
        # IP Address                                      : 10.10.5.14
        # IP Netmask                                      : 255.255.254.0
        # Gateway IP Address                              : 10.10.5.1
        # Fallback IP Address Being Used                  :
        # Domain                                          :
        # Name Server                                     :
        # CAPWAP Path MTU                                 : 1485
        # Capwap Active Window Size                       : 1
        # Telnet State                                    : Disabled
        # CPU Type                                        :  ARMv7 Processor rev 1 (v7l)
        # Memory Type                                     : DDR3
        # Memory Size                                     : 1028096 KB
        # SSH State                                       : Enabled
        # Cisco AP Location                               : default location
        # Site Tag Name                                   : b8
        # RF Tag Name                                     : Custom-RF
        # Policy Tag Name                                 : b1_policy_tag
        # AP join Profile                                 : APG_b18
        # Flex Profile                                    : default-flex-profile
        # AP Filter name                                  : b8
        # Primary Cisco Controller Name                   : b7-wl-ewlc1
        # Primary Cisco Controller IP Address             : 10.6.4.17
        # Secondary Cisco Controller Name                 : b8-wl-wlc3
        # Secondary Cisco Controller IP Address           : 10.6.7.16
        # Tertiary Cisco Controller Name                  : b3-wl-wlc3
        # Tertiary Cisco Controller IP Address            : 10.6.4.17
        # Administrative State                            : Enabled
        # Operation State                                 : Registered
        # NAT External IP Address                         : 10.10.5.12
        # AP Certificate type                             : Manufacturer Installed Certificate
        # AP Mode                                         : Local
        # AP VLAN tagging state                           : Disabled
        # AP VLAN tag                                     : 0
        # CAPWAP Preferred mode                           : IPv4
        # CAPWAP UDP-Lite                                 : Not Configured
        # AP Submode                                      : Not Configured
        # Office Extend Mode                              : Disabled
        # Dhcp Server                                     : Disabled
        # Remote AP Debug                                 : Disabled
        # Logging Trap Severity Level                     : information
        # Logging Syslog facility                         : kern
        # Software Version                                : 10.145.1.9
        # Boot Version                                    : 10.4.2.4
        # Mini IOS Version                                : 0.0.0.0
        # Stats Reporting Period                          : 0
        # LED State                                       : Enabled
        # LED Flash State                                 : Enabled
        # LED Flash Timer                                 : 0
        # MDNS Group Id                                   : 0
        # MDNS Rule Name                                  :
        # PoE Pre-Standard Switch                         : Disabled
        # PoE Power Injector MAC Address                  : Disabled
        # Power Type/Mode                                 : PoE/Full Power
        # Number of Slots                                 : 3
        # AP Model                                        : AIR-AP4800-D-K9
        # IOS Version                                     : 10.145.1.9
        # Reset Button                                    : Disabled
        # AP Serial Number                                : FGL2102AZZZ
        # Management Frame Validation                     : Capable
        # Management Frame Protection                     : Capable
        # AP User Name                                    : admin
        # AP 802.1X User Mode                             : Global
        # AP 802.1X User Name                             : Not Configured
        # Cisco AP System Logging Host                    : 10.16.19.6
        # Cisco AP Secured Logging TLS mode               : Disabled
        # AP Up Time                                      : 3 days 9 hours 44 minutes 18 seconds
        # AP CAPWAP Up Time                               : 3 days 9 hours 37 minutes 20 seconds
        # Join Date and Time                              : 08/14/2020 19:48:09
        # Join Taken Time                                 : 6 minutes 57 seconds
        # Join Priority                                   : 1
        # AP Link Latency                                 : Disable
        # AP Lag Configuration Status                     : Disabled
        # Lag Support for AP                              : Yes
        # Rogue Detection                                 : Enabled
        # Rogue Containment auto-rate                     : Disabled
        # Rogue Containment of standalone flexconnect APs : Disabled
        # Rogue Detection Report Interval                 : 10
        # Rogue AP minimum RSSI                           : -70
        # Rogue AP minimum transient time                 : 0
        # AP TCP MSS Adjust                               : Enabled
        # AP TCP MSS Size                                 : 1250
        # AP IPv6 TCP MSS Adjust                          : Enabled
        # AP IPv6 TCP MSS Size                            : 1250
        # Hyperlocation Admin Status                      : Disabled
        # Retransmit count                                : 5
        # Retransmit interval                             : 3
        # Fabric status                                   : Disabled
        # FIPS status                                     : Disabled
        # WLANCC status                                   : Disabled
        # USB Module Type                                 : USB Module
        # USB Module State                                : Enabled
        # USB Operational State                           : Disabled
        # USB Override                                    : Disabled
        # GAS rate limit Admin status                     : Disabled
        # WPA3 Capability                                 : Enabled
        # EWC-AP Capability                               : Disabled
        # AWIPS Capability                                : Enabled
        # Proxy Hostname                                  : Not Configured
        # Proxy Port                                      : Not Configured
        # Proxy NO_PROXY list                             : Not Configured
        # GRPC server status                              : Disabled
        # Unencrypted Data Keep Alive                     : Enabled
        # Local DHCP Server                               : Disabled
        # Traffic Distribution Statistics Capability      : Enabled
        # Dual DFS Statistics                             : Disabled

     

        # Cisco AP Name   : bg-1-cap1
        cisco_ap_name_capture = re.compile(r"^Cisco\s+AP\s+Name\s+:\s+(?P<cisco_ap_name>.*)$")
        
        # Cisco AP Identifier                             : 70b3.d2ff.59b6
        cisco_ap_identifier_capture = re.compile(r"^Cisco\s+AP\s+Identifier\s+:\s+(?P<cisco_ap_identifier>.*)$")
        
        # Country Code                                    : IN
        country_code_capture = re.compile(r"^Country\s+Code\s+:\s+(?P<country_code>.*)$")
        
        # Regulatory Domain Allowed by Country            : 802.11bg:-A   802.11a:-DN
        regulatory_domain_allowed_by_country_capture = re.compile(
            r"^Regulatory\s+Domain\s+Allowed\s+by\s+Country\s+:\s+(?P<regulatory_domain_allowed_by_country>.*)$")
        
        # AP Country Code                                 : IN  - India
        ap_country_code_capture = re.compile(r"^AP\s+Country\s+Code\s+:\s+(?P<ap_country_code>.*)$")
        
        # Slot 0                                        : -A
        slot_0_capture = re.compile(r"^Slot\s+0\s+:\s+(?P<slot_0>.*)$")
        
        # Slot 1                                        : -D
        slot_1_capture = re.compile(r"^Slot\s+1\s+:\s+(?P<slot_1>.*)$")
        
        # MAC Address                                     : 70b3.17ff.bdcc
        mac_address_capture = re.compile(r"^MAC\s+Address\s+:\s+(?P<mac_address>.*)$")
        
        # IP Address Configuration                        : DHCP
        ip_address_configuration_capture = re.compile(
            r"^IP\s+Address\s+Configuration\s+:\s+(?P<ip_address_configuration>.*)$")
        
        # IP Address                                      : 10.10.5.14
        ip_address_capture = re.compile(r"^IP\s+Address\s+:\s+(?P<ip_address>.*)$")
        
        # IP Netmask                                      : 255.255.254.0
        ip_netmask_capture = re.compile(r"^IP\s+Netmask\s+:\s+(?P<ip_netmask>.*)$")
        
        # Gateway IP Address                              : 10.10.5.1
        gateway_ip_address_capture = re.compile(r"^Gateway\s+IP\s+Address\s+:\s+(?P<gateway_ip_address>.*)$")
        
        # Fallback IP Address Being Used                  :
        fallback_ip_address_being_used_capture = re.compile(
            r"^Fallback\s+IP\s+Address\s+Being\s+Used\s+:\s+(?P<fallback_ip_address_being_used>.*)$")
        
        # Domain                                          :
        domain_capture = re.compile(r"^Domain\s+:\s+(?P<domain>.*)$")
        
        # Name Server                                     :
        name_server_capture = re.compile(r"^Name\s+Server\s+:\s+(?P<name_server>.*)$")
        
        # CAPWAP Path MTU                                 : 1485
        capwap_path_mtu_capture = re.compile(r"^CAPWAP\s+Path\s+MTU\s+:\s+(?P<capwap_path_mtu>.*)$")
        
        # Capwap Active Window Size                       : 1
        capwap_active_window_size_capture = re.compile(
            r"^Capwap\s+Active\s+Window\s+Size\s+:\s+(?P<capwap_active_window_size>.*)$")
        
        # Telnet State                                    : Disabled
        telnet_state_capture = re.compile(r"^Telnet\s+State\s+:\s+(?P<telnet_state>.*)$")
        
        # CPU Type                                        :  ARMv7 Processor rev 1 (v7l)
        cpu_type_capture = re.compile(r"^CPU\s+Type\s+:\s+(?P<cpu_type>.*)$")
        
        # Memory Type                                     : DDR3
        memory_type_capture = re.compile(r"^Memory\s+Type\s+:\s+(?P<memory_type>.*)$")
        
        # Memory Size                                     : 1028096 KB
        memory_size_capture = re.compile(r"^Memory\s+Size\s+:\s+(?P<memory_size>\d+)\s+KB$")
        
        # SSH State                                       : Enabled
        ssh_state_capture = re.compile(r"^SSH\s+State\s+:\s+(?P<ssh_state>.*)$")
        
        # Cisco AP Location                               : default location
        cisco_ap_location_capture = re.compile(r"^Cisco\s+AP\s+Location\s+:\s+(?P<cisco_ap_location>.*)$")
        
        # Site Tag Name                                   : b8
        site_tag_name_capture = re.compile(r"^Site\s+Tag\s+Name\s+:\s+(?P<site_tag_name>.*)$")
        
        # RF Tag Name                                     : Custom-RF
        rf_tag_name_capture = re.compile(r"^RF\s+Tag\s+Name\s+:\s+(?P<rf_tag_name>.*)$")
        
        # Policy Tag Name                                 : b1_policy_tag
        policy_tag_name_capture = re.compile(r"^Policy\s+Tag\s+Name\s+:\s+(?P<policy_tag_name>.*)$")
        
        # AP join Profile                                 : APG_b18
        ap_join_profile_capture = re.compile(r"^AP\s+join\s+Profile\s+:\s+(?P<ap_join_profile>.*)$")
        
        # Flex Profile                                    : default-flex-profile
        flex_profile_capture = re.compile(r"^Flex\s+Profile\s+:\s+(?P<flex_profile>.*)$")
        
        # AP Filter name                                  : b8
        ap_filter_name_capture = re.compile(r"^AP\s+Filter\s+name\s+:\s+(?P<ap_filter_name>.*)$")
        
        # Primary Cisco Controller Name                   : b7-wl-ewlc1
        primary_cisco_controller_name_capture = re.compile(
            r"^Primary\s+Cisco\s+Controller\s+Name\s+:\s+(?P<primary_cisco_controller_name>.*)$")
        
        # Primary Cisco Controller IP Address             : 10.6.4.17
        primary_cisco_controller_ip_address_capture = re.compile(
            r"^Primary\s+Cisco\s+Controller\s+IP\s+Address\s+:\s+(?P<primary_cisco_controller_ip_address>.*)$")
        
        # Secondary Cisco Controller Name                 : b8-wl-wlc3
        secondary_cisco_controller_name_capture = re.compile(
            r"^Secondary\s+Cisco\s+Controller\s+Name\s+:\s+(?P<secondary_cisco_controller_name>.*)$")
        
        # Secondary Cisco Controller IP Address           : 10.6.7.16
        secondary_cisco_controller_ip_address_capture = re.compile(
            r"^Secondary\s+Cisco\s+Controller\s+IP\s+Address\s+:\s+(?P<secondary_cisco_controller_ip_address>.*)$")
        
        # Tertiary Cisco Controller Name                  : b3-wl-wlc3
        tertiary_cisco_controller_name_capture = re.compile(
            r"^Tertiary\s+Cisco\s+Controller\s+Name\s+:\s+(?P<tertiary_cisco_controller_name>.*)$")
        
        # Tertiary Cisco Controller IP Address            : 10.6.4.17
        tertiary_cisco_controller_ip_address_capture = re.compile(
            r"^Tertiary\s+Cisco\s+Controller\s+IP\s+Address\s+:\s+(?P<tertiary_cisco_controller_ip_address>.*)$")
        
        # Administrative State                            : Enabled
        administrative_state_capture = re.compile(r"^Administrative\s+State\s+:\s+(?P<administrative_state>.*)$")
        
        # Operation State                                 : Registered
        operation_state_capture = re.compile(r"^Operation\s+State\s+:\s+(?P<operation_state>.*)$")
        
        # NAT External IP Address                         : 10.10.5.12
        nat_external_ip_address_capture = re.compile(
            r"^NAT\s+External\s+IP\s+Address\s+:\s+(?P<nat_external_ip_address>.*)$")
        
        # AP Certificate type                             : Manufacturer Installed Certificate
        ap_certificate_type_capture = re.compile(r"^AP\s+Certificate\s+type\s+:\s+(?P<ap_certificate_type>.*)$")
        
        # AP Mode                                         : Local
        ap_mode_capture = re.compile(r"^AP\s+Mode\s+:\s+(?P<ap_mode>.*)$")
        
        # AP VLAN tagging state                           : Disabled
        ap_vlan_tagging_state_capture = re.compile(r"^AP\s+VLAN\s+tagging\s+state\s+:\s+(?P<ap_vlan_tagging_state>.*)$")
        
        # AP VLAN tag                                     : 0
        ap_vlan_tag_capture = re.compile(r"^AP\s+VLAN\s+tag\s+:\s+(?P<ap_vlan_tag>.*)$")
        
        # CAPWAP Preferred mode                           : IPv4
        capwap_preferred_mode_capture = re.compile(r"^CAPWAP\s+Preferred\s+mode\s+:\s+(?P<capwap_preferred_mode>.*)$")
        
        # CAPWAP UDP-Lite                                 : Not Configured
        capwap_udp_lite_capture = re.compile(r"^CAPWAP\s+UDP-Lite\s+:\s+(?P<capwap_udp_lite>.*)$")
        
        # AP Submode                                      : Not Configured
        ap_submode_capture = re.compile(r"^AP\s+Submode\s+:\s+(?P<ap_submode>.*)$")
        
        # Office Extend Mode                              : Disabled
        office_extend_mode_capture = re.compile(r"^Office\s+Extend\s+Mode\s+:\s+(?P<office_extend_mode>.*)$")
        
        # Dhcp Server                                     : Disabled
        dhcp_server_capture = re.compile(r"^Dhcp\s+Server\s+:\s+(?P<dhcp_server>.*)$")
        
        # Remote AP Debug                                 : Disabled
        remote_ap_debug_capture = re.compile(r"^Remote\s+AP\s+Debug\s+:\s+(?P<remote_ap_debug>.*)$")
        
        # Logging Trap Severity Level                     : information
        logging_trap_severity_level_capture = re.compile(
            r"^Logging\s+Trap\s+Severity\s+Level\s+:\s+(?P<logging_trap_severity_level>.*)$")
        
        # Logging Syslog facility                         : kern
        logging_syslog_facility_capture = re.compile(
            r"^Logging\s+Syslog\s+facility\s+:\s+(?P<logging_syslog_facility>.*)$")
        
        # Software Version                                : 10.145.1.9
        software_version_capture = re.compile(r"^Software\s+Version\s+:\s+(?P<software_version>.*)$")
        
        # Boot Version                                    : 10.4.2.4
        boot_version_capture = re.compile(r"^Boot\s+Version\s+:\s+(?P<boot_version>.*)$")
        
        # Mini IOS Version                                : 0.0.0.0
        mini_ios_version_capture = re.compile(r"^Mini\s+IOS\s+Version\s+:\s+(?P<mini_ios_version>.*)$")
        
        # Stats Reporting Period                          : 0
        stats_reporting_period_capture = re.compile(
            r"^Stats\s+Reporting\s+Period\s+:\s+(?P<stats_reporting_period>.*)$")
        
        # LED State                                       : Enabled
        led_state_capture = re.compile(r"^LED\s+State\s+:\s+(?P<led_state>.*)$")
        
        # LED Flash State                                 : Enabled
        led_flash_state_capture = re.compile(r"^LED\s+Flash\s+State\s+:\s+(?P<led_flash_state>.*)$")
        
        # LED Flash Timer                                 : 0
        led_flash_timer_capture = re.compile(r"^LED\s+Flash\s+Timer\s+:\s+(?P<led_flash_timer>.*)$")
        
        # MDNS Group Id                                   : 0
        mdns_group_id_capture = re.compile(r"^MDNS\s+Group\s+Id\s+:\s+(?P<mdns_group_id>.*)$")
        
        # MDNS Rule Name                                  :
        mdns_rule_name_capture = re.compile(r"^MDNS\s+Rule\s+Name\s+:\s+(?P<mdns_rule_name>.*)$")
        
        # PoE Pre-Standard Switch                         : Disabled
        poe_pre_standard_switch_capture = re.compile(
            r"^PoE\s+Pre-Standard\s+Switch\s+:\s+(?P<poe_pre_standard_switch>.*)$")
        
        # PoE Power Injector MAC Address                  : Disabled
        poe_power_injector_mac_address_capture = re.compile(
            r"^PoE\s+Power\s+Injector\s+MAC\s+Address\s+:\s+(?P<poe_power_injector_mac_address>.*)$")
        
        # Power Type/Mode                                 : PoE/Full Power
        power_type_mode_capture = re.compile(r"^Power\s+Type/Mode\s+:\s+(?P<power_type_mode>.*)$")
        
        # Number of Slots                                 : 3
        number_of_slots_capture = re.compile(r"^Number\s+of\s+Slots\s+:\s+(?P<number_of_slots>.*)$")
        
        # AP Model                                        : AIR-AP4800-D-K9
        ap_model_capture = re.compile(r"^AP\s+Model\s+:\s+(?P<ap_model>.*)$")
        
        # IOS Version                                     : 10.145.1.9
        ios_version_capture = re.compile(r"^IOS\s+Version\s+:\s+(?P<ios_version>.*)$")
        
        # Reset Button                                    : Disabled
        reset_button_capture = re.compile(r"^Reset\s+Button\s+:\s+(?P<reset_button>.*)$")
        
        # AP Serial Number                                : FGL2102AZZZ
        ap_serial_number_capture = re.compile(r"^AP\s+Serial\s+Number\s+:\s+(?P<ap_serial_number>.*)$")
        
        # Management Frame Validation                     : Capable
        management_frame_validation_capture = re.compile(
            r"^Management\s+Frame\s+Validation\s+:\s+(?P<management_frame_validation>.*)$")
        
        # Management Frame Protection                     : Capable
        management_frame_protection_capture = re.compile(
            r"^Management\s+Frame\s+Protection\s+:\s+(?P<management_frame_protection>.*)$")
        
        # AP User Name                                    : admin
        ap_user_name_capture = re.compile(r"^AP\s+User\s+Name\s+:\s+(?P<ap_user_name>.*)$")
        
        # AP 802.1X User Mode                             : Global
        ap_802_1x_user_mode_capture = re.compile(r"^AP\s+802.1X\s+User\s+Mode\s+:\s+(?P<ap_802_1x_user_mode>.*)$")
        
        # AP 802.1X User Name                             : Not Configured
        ap_802_1x_user_name_capture = re.compile(r"^AP\s+802.1X\s+User\s+Name\s+:\s+(?P<ap_802_1x_user_name>.*)$")
        
        # Cisco AP System Logging Host                    : 10.16.19.6
        cisco_ap_system_logging_host_capture = re.compile(
            r"^Cisco\s+AP\s+System\s+Logging\s+Host\s+:\s+(?P<cisco_ap_system_logging_host>.*)$")
        
        # Cisco AP Secured Logging TLS mode               : Disabled
        cisco_ap_secured_logging_tls_mode_capture = re.compile(
            r"^Cisco\s+AP\s+Secured\s+Logging\s+TLS\s+mode\s+:\s+(?P<cisco_ap_secured_logging_tls_mode>.*)$")
        
        # AP Up Time                                      : 3 days 9 hours 44 minutes 18 seconds
        ap_up_time_capture = re.compile(r"^AP\s+Up\s+Time\s+:\s+(?P<ap_up_time>.*)$")
        
        # AP CAPWAP Up Time                               : 3 days 9 hours 37 minutes 20 seconds
        ap_capwap_up_time_capture = re.compile(r"^AP\s+CAPWAP\s+Up\s+Time\s+:\s+(?P<ap_capwap_up_time>.*)$")
        
        # Join Date and Time                              : 08/14/2020 19:48:09
        join_date_and_time_capture = re.compile(r"^Join\s+Date\s+and\s+Time\s+:\s+(?P<join_date_and_time>.*)$")
        
        # Join Taken Time                                 : 6 minutes 57 seconds
        join_taken_time_capture = re.compile(r"^Join\s+Taken\s+Time\s+:\s+(?P<join_taken_time>.*)$")
        
        # Join Priority                                   : 1
        join_priority_capture = re.compile(r"^Join\s+Priority\s+:\s+(?P<join_priority>.*)$")
        
        # AP Link Latency                                 : Disable
        ap_link_latency_capture = re.compile(r"^AP\s+Link\s+Latency\s+:\s+(?P<ap_link_latency>.*)$")
        
        # AP Lag Configuration Status                     : Disabled
        ap_lag_configuration_status_capture = re.compile(
            r"^AP\s+Lag\s+Configuration\s+Status\s+:\s+(?P<ap_lag_configuration_status>.*)$")
        
        # Lag Support for AP                              : Yes
        lag_support_for_ap_capture = re.compile(r"^Lag\s+Support\s+for\s+AP\s+:\s+(?P<lag_support_for_ap>.*)$")
        
        # Rogue Detection                                 : Enabled
        rogue_detection_capture = re.compile(r"^Rogue\s+Detection\s+:\s+(?P<rogue_detection>.*)$")
        
        # Rogue Containment auto-rate                     : Disabled
        rogue_containment_auto_rate_capture = re.compile(
            r"^Rogue\s+Containment\s+auto-rate\s+:\s+(?P<rogue_containment_auto_rate>.*)$")
        
        # Rogue Containment of standalone flexconnect APs : Disabled
        rogue_containment_of_standalone_flexconnect_aps_capture = re.compile(
            r"^Rogue\s+Containment\s+of\s+standalone\s+flexconnect\s+APs\s+:\s+(?P<rogue_containment_of_standalone_flexconnect_aps>.*)$")
        
        # Rogue Detection Report Interval                 : 10
        rogue_detection_report_interval_capture = re.compile(
            r"^Rogue\s+Detection\s+Report\s+Interval\s+:\s+(?P<rogue_detection_report_interval>.*)$")
        
        # Rogue AP minimum RSSI                           : -70
        rogue_ap_minimum_rssi_capture = re.compile(r"^Rogue\s+AP\s+minimum\s+RSSI\s+:\s+(?P<rogue_ap_minimum_rssi>.*)$")
        
        # Rogue AP minimum transient time                 : 0
        rogue_ap_minimum_transient_time_capture = re.compile(
            r"^Rogue\s+AP\s+minimum\s+transient\s+time\s+:\s+(?P<rogue_ap_minimum_transient_time>.*)$")
        
        # AP TCP MSS Adjust                               : Enabled
        ap_tcp_mss_adjust_capture = re.compile(r"^AP\s+TCP\s+MSS\s+Adjust\s+:\s+(?P<ap_tcp_mss_adjust>.*)$")
        
        # AP TCP MSS Size                                 : 1250
        ap_tcp_mss_size_capture = re.compile(r"^AP\s+TCP\s+MSS\s+Size\s+:\s+(?P<ap_tcp_mss_size>.*)$")
        
        # AP IPv6 TCP MSS Adjust                          : Enabled
        ap_ipv6_tcp_mss_adjust_capture = re.compile(
            r"^AP\s+IPv6\s+TCP\s+MSS\s+Adjust\s+:\s+(?P<ap_ipv6_tcp_mss_adjust>.*)$")
        
        # AP IPv6 TCP MSS Size                            : 1250
        ap_ipv6_tcp_mss_size_capture = re.compile(r"^AP\s+IPv6\s+TCP\s+MSS\s+Size\s+:\s+(?P<ap_ipv6_tcp_mss_size>.*)$")
        
        # Hyperlocation Admin Status                      : Disabled
        hyperlocation_admin_status_capture = re.compile(
            r"^Hyperlocation\s+Admin\s+Status\s+:\s+(?P<hyperlocation_admin_status>.*)$")
        
        # Retransmit count                                : 5
        retransmit_count_capture = re.compile(r"^Retransmit\s+count\s+:\s+(?P<retransmit_count>.*)$")
        
        # Retransmit interval                             : 3
        retransmit_interval_capture = re.compile(r"^Retransmit\s+interval\s+:\s+(?P<retransmit_interval>.*)$")
        
        # Fabric status                                   : Disabled
        fabric_status_capture = re.compile(r"^Fabric\s+status\s+:\s+(?P<fabric_status>.*)$")
        
        # FIPS status                                     : Disabled
        fips_status_capture = re.compile(r"^FIPS\s+status\s+:\s+(?P<fips_status>.*)$")
        
        # WLANCC status                                   : Disabled
        wlancc_status_capture = re.compile(r"^WLANCC\s+status\s+:\s+(?P<wlancc_status>.*)$")
        
        # USB Module Type                                 : USB Module
        usb_module_type_capture = re.compile(r"^USB\s+Module\s+Type\s+:\s+(?P<usb_module_type>.*)$")
        
        # USB Module State                                : Enabled
        usb_module_state_capture = re.compile(r"^USB\s+Module\s+State\s+:\s+(?P<usb_module_state>.*)$")
        
        # USB Operational State                           : Disabled
        usb_operational_state_capture = re.compile(r"^USB\s+Operational\s+State\s+:\s+(?P<usb_operational_state>.*)$")
        
        # USB Override                                    : Disabled
        usb_override_capture = re.compile(r"^USB\s+Override\s+:\s+(?P<usb_override>.*)$")
        
        # GAS rate limit Admin status                     : Disabled
        gas_rate_limit_admin_status_capture = re.compile(
            r"^GAS\s+rate\s+limit\s+Admin\s+status\s+:\s+(?P<gas_rate_limit_admin_status>.*)$")
        
        # WPA3 Capability                                 : Enabled
        wpa3_capability_capture = re.compile(r"^WPA3\s+Capability\s+:\s+(?P<wpa3_capability>.*)$")
        
        # EWC-AP Capability                               : Disabled
        ewc_ap_capability_capture = re.compile(r"^EWC-AP\s+Capability\s+:\s+(?P<ewc_ap_capability>.*)$")
        
        # AWIPS Capability                                : Enabled
        awips_capability_capture = re.compile(r"^AWIPS\s+Capability\s+:\s+(?P<awips_capability>.*)$")
        
        # Proxy Hostname                                  : Not Configured
        proxy_hostname_capture = re.compile(r"^Proxy\s+Hostname\s+:\s+(?P<proxy_hostname>.*)$")
        
        # Proxy Port                                      : Not Configured
        proxy_port_capture = re.compile(r"^Proxy\s+Port\s+:\s+(?P<proxy_port>.*)$")
        
        # Proxy NO_PROXY list                             : Not Configured
        proxy_no_proxy_list_capture = re.compile(r"^Proxy\s+NO_PROXY\s+list\s+:\s+(?P<proxy_no_proxy_list>.*)$")
        
        # GRPC server status                              : Disabled
        grpc_server_status_capture = re.compile(r"^GRPC\s+server\s+status\s+:\s+(?P<grpc_server_status>.*)$")
        
        # Unencrypted Data Keep Alive                     : Enabled
        unencrypted_data_keep_alive_capture = re.compile(
            r"^Unencrypted\s+Data\s+Keep\s+Alive\s+:\s+(?P<unencrypted_data_keep_alive>.*)$")
        
        # Local DHCP Server                               : Disabled
        local_dhcp_server_capture = re.compile(r"^Local\s+DHCP\s+Server\s+:\s+(?P<local_dhcp_server>.*)$")
        
        # Traffic Distribution Statistics Capability      : Enabled
        traffic_distribution_statistics_capability_capture = re.compile(
            r"^Traffic\s+Distribution\s+Statistics\s+Capability\s+:\s+(?P<traffic_distribution_statistics_capability>.*)$")
        
        # Dual DFS Statistics                             : Disabled
        dual_dfs_statistics_capture = re.compile(r"^Dual\s+DFS\s+Statistics\s+:\s+(?P<dual_dfs_statistics>.*)$")

        remove_lines = ('====', 'AP Regulatory')

        def change_data_type(value):
            if value.isdigit():
                value = value.strip()
                value = int(value)
            else:
                try:
                    # Change strings to float if possible
                    value = float(value)
                except ValueError:
                    # if the value is not an int or float, leave it as a string.
                    pass
            return value

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines


        out_filter = filter_lines(raw_output=out, remove_lines=remove_lines)
        ap_name_key = ''

        for line in out_filter:
            # Cisco AP Name   : bg-1-cap1
            if cisco_ap_name_capture.match(line):
                cisco_ap_name_match = cisco_ap_name_capture.match(line)
                groups = cisco_ap_name_match.groupdict()
                cisco_ap_name = groups['cisco_ap_name']
                ap_name_key = cisco_ap_name
                if not ap_config_general_dict.get('ap_name', {}):
                    ap_config_general_dict['ap_name'] = {}
                ap_config_general_dict['ap_name'].update({ap_name_key: {}})
            # Cisco AP Identifier                             : 70b3.d2ff.59b6
            elif cisco_ap_identifier_capture.match(line):
                cisco_ap_identifier_match = cisco_ap_identifier_capture.match(line)
                groups = cisco_ap_identifier_match.groupdict()
                cisco_ap_identifier = groups['cisco_ap_identifier']
                cisco_ap_identifier = change_data_type(value=cisco_ap_identifier)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'cisco_ap_identifier': cisco_ap_identifier})
            # Country Code                                    : IN
            elif country_code_capture.match(line):
                country_code_match = country_code_capture.match(line)
                groups = country_code_match.groupdict()
                country_code = groups['country_code']
                country_code = change_data_type(value=country_code)
                ap_config_general_dict['ap_name'][ap_name_key].update({'country_code': country_code})
            # Regulatory Domain Allowed by Country            : 802.11bg:-A   802.11a:-DN
            elif regulatory_domain_allowed_by_country_capture.match(line):
                regulatory_domain_allowed_by_country_match = regulatory_domain_allowed_by_country_capture.match(line)
                groups = regulatory_domain_allowed_by_country_match.groupdict()
                regulatory_domain_allowed_by_country = groups['regulatory_domain_allowed_by_country']
                regulatory_domain_allowed_by_country = change_data_type(value=regulatory_domain_allowed_by_country)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'regulatory_domain_allowed_by_country': regulatory_domain_allowed_by_country})
            # AP Country Code                                 : IN  - India
            elif ap_country_code_capture.match(line):
                ap_country_code_match = ap_country_code_capture.match(line)
                groups = ap_country_code_match.groupdict()
                ap_country_code = groups['ap_country_code']
                ap_country_code = change_data_type(value=ap_country_code)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_country_code': ap_country_code})
            # Slot 0                                        : -A
            elif slot_0_capture.match(line):
                if not ap_config_general_dict["ap_name"][ap_name_key].get("ap_regulatory_domain"):
                    ap_config_general_dict["ap_name"][ap_name_key].update({ "ap_regulatory_domain": {} })
                slot_0_match = slot_0_capture.match(line)
                groups = slot_0_match.groupdict()
                slot_0 = groups['slot_0']
                slot_0 = change_data_type(value=slot_0)
                ap_config_general_dict['ap_name'][ap_name_key]["ap_regulatory_domain"].update({'slot_0': slot_0})
            # Slot 1                                        : -D
            elif slot_1_capture.match(line):
                if not ap_config_general_dict["ap_name"][ap_name_key].get("ap_regulatory_domain"):
                    ap_config_general_dict["ap_name"][ap_name_key].update({ "ap_regulatory_domain": {} })
                slot_1_match = slot_1_capture.match(line)
                groups = slot_1_match.groupdict()
                slot_1 = groups['slot_1']
                slot_1 = change_data_type(value=slot_1)
                ap_config_general_dict['ap_name'][ap_name_key]["ap_regulatory_domain"].update({'slot_1': slot_1})
            # MAC Address                                     : 70b3.17ff.bdcc
            elif mac_address_capture.match(line):
                mac_address_match = mac_address_capture.match(line)
                groups = mac_address_match.groupdict()
                mac_address = groups['mac_address']
                mac_address = change_data_type(value=mac_address)
                ap_config_general_dict['ap_name'][ap_name_key].update({'mac_address': mac_address})
            # IP Address Configuration                        : DHCP
            elif ip_address_configuration_capture.match(line):
                ip_address_configuration_match = ip_address_configuration_capture.match(line)
                groups = ip_address_configuration_match.groupdict()
                ip_address_configuration = groups['ip_address_configuration']
                ip_address_configuration = change_data_type(value=ip_address_configuration)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ip_address_configuration': ip_address_configuration})
            # IP Address                                      : 10.10.5.14
            elif ip_address_capture.match(line):
                ip_address_match = ip_address_capture.match(line)
                groups = ip_address_match.groupdict()
                ip_address = groups['ip_address']
                ip_address = change_data_type(value=ip_address)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ip_address': ip_address})
            # IP Netmask                                      : 255.255.254.0
            elif ip_netmask_capture.match(line):
                ip_netmask_match = ip_netmask_capture.match(line)
                groups = ip_netmask_match.groupdict()
                ip_netmask = groups['ip_netmask']
                ip_netmask = change_data_type(value=ip_netmask)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ip_netmask': ip_netmask})
            # Gateway IP Address                              : 10.10.5.1
            elif gateway_ip_address_capture.match(line):
                gateway_ip_address_match = gateway_ip_address_capture.match(line)
                groups = gateway_ip_address_match.groupdict()
                gateway_ip_address = groups['gateway_ip_address']
                gateway_ip_address = change_data_type(value=gateway_ip_address)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'gateway_ip_address': gateway_ip_address})
            # Fallback IP Address Being Used                  :
            elif fallback_ip_address_being_used_capture.match(line):
                fallback_ip_address_being_used_match = fallback_ip_address_being_used_capture.match(line)
                groups = fallback_ip_address_being_used_match.groupdict()
                fallback_ip_address_being_used = groups['fallback_ip_address_being_used']
                fallback_ip_address_being_used = change_data_type(value=fallback_ip_address_being_used)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'fallback_ip_address_being_used': fallback_ip_address_being_used})
            # Domain                                          :
            elif domain_capture.match(line):
                domain_match = domain_capture.match(line)
                groups = domain_match.groupdict()
                domain = groups['domain']
                domain = change_data_type(value=domain)
                ap_config_general_dict['ap_name'][ap_name_key].update({'domain': domain})
            # Name Server                                     :
            elif name_server_capture.match(line):
                name_server_match = name_server_capture.match(line)
                groups = name_server_match.groupdict()
                name_server = groups['name_server']
                name_server = change_data_type(value=name_server)
                ap_config_general_dict['ap_name'][ap_name_key].update({'name_server': name_server})
            # CAPWAP Path MTU                                 : 1485
            elif capwap_path_mtu_capture.match(line):
                capwap_path_mtu_match = capwap_path_mtu_capture.match(line)
                groups = capwap_path_mtu_match.groupdict()
                capwap_path_mtu = groups['capwap_path_mtu']
                capwap_path_mtu = change_data_type(value=capwap_path_mtu)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'capwap_path_mtu': capwap_path_mtu})
            # Capwap Active Window Size                       : 1
            elif capwap_active_window_size_capture.match(line):
                capwap_active_window_size_match = capwap_active_window_size_capture.match(line)
                groups = capwap_active_window_size_match.groupdict()
                capwap_active_window_size = groups['capwap_active_window_size']
                capwap_active_window_size = change_data_type(value=capwap_active_window_size)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'capwap_active_window_size': capwap_active_window_size})
            # Telnet State                                    : Disabled
            elif telnet_state_capture.match(line):
                telnet_state_match = telnet_state_capture.match(line)
                groups = telnet_state_match.groupdict()
                telnet_state = groups['telnet_state']
                telnet_state = change_data_type(value=telnet_state)
                ap_config_general_dict['ap_name'][ap_name_key].update({'telnet_state': telnet_state})
            # CPU Type                                        :  ARMv7 Processor rev 1 (v7l)
            elif cpu_type_capture.match(line):
                cpu_type_match = cpu_type_capture.match(line)
                groups = cpu_type_match.groupdict()
                cpu_type = groups['cpu_type']
                cpu_type = change_data_type(value=cpu_type)
                ap_config_general_dict['ap_name'][ap_name_key].update({'cpu_type': cpu_type})
            # Memory Type                                     : DDR3
            elif memory_type_capture.match(line):
                memory_type_match = memory_type_capture.match(line)
                groups = memory_type_match.groupdict()
                memory_type = groups['memory_type']
                memory_type = change_data_type(value=memory_type)
                ap_config_general_dict['ap_name'][ap_name_key].update({'memory_type': memory_type})
            # Memory Size                                     : 1028096 KB
            elif memory_size_capture.match(line):
                memory_size_match = memory_size_capture.match(line)
                groups = memory_size_match.groupdict()
                memory_size = groups['memory_size']
                memory_size = change_data_type(value=memory_size)
                ap_config_general_dict['ap_name'][ap_name_key].update({'memory_size_kb': memory_size})
            # SSH State                                       : Enabled
            elif ssh_state_capture.match(line):
                ssh_state_match = ssh_state_capture.match(line)
                groups = ssh_state_match.groupdict()
                ssh_state = groups['ssh_state']
                ssh_state = change_data_type(value=ssh_state)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ssh_state': ssh_state})
            # Cisco AP Location                               : default location
            elif cisco_ap_location_capture.match(line):
                cisco_ap_location_match = cisco_ap_location_capture.match(line)
                groups = cisco_ap_location_match.groupdict()
                cisco_ap_location = groups['cisco_ap_location']
                cisco_ap_location = change_data_type(value=cisco_ap_location)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'cisco_ap_location': cisco_ap_location})
            # Site Tag Name                                   : b8
            elif site_tag_name_capture.match(line):
                site_tag_name_match = site_tag_name_capture.match(line)
                groups = site_tag_name_match.groupdict()
                site_tag_name = groups['site_tag_name']
                site_tag_name = change_data_type(value=site_tag_name)
                ap_config_general_dict['ap_name'][ap_name_key].update({'site_tag_name': site_tag_name})
            # RF Tag Name                                     : Custom-RF
            elif rf_tag_name_capture.match(line):
                rf_tag_name_match = rf_tag_name_capture.match(line)
                groups = rf_tag_name_match.groupdict()
                rf_tag_name = groups['rf_tag_name']
                rf_tag_name = change_data_type(value=rf_tag_name)
                ap_config_general_dict['ap_name'][ap_name_key].update({'rf_tag_name': rf_tag_name})
            # Policy Tag Name                                 : b1_policy_tag
            elif policy_tag_name_capture.match(line):
                policy_tag_name_match = policy_tag_name_capture.match(line)
                groups = policy_tag_name_match.groupdict()
                policy_tag_name = groups['policy_tag_name']
                policy_tag_name = change_data_type(value=policy_tag_name)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'policy_tag_name': policy_tag_name})
            # AP join Profile                                 : APG_b18
            elif ap_join_profile_capture.match(line):
                ap_join_profile_match = ap_join_profile_capture.match(line)
                groups = ap_join_profile_match.groupdict()
                ap_join_profile = groups['ap_join_profile']
                ap_join_profile = change_data_type(value=ap_join_profile)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_join_profile': ap_join_profile})
            # Flex Profile                                    : default-flex-profile
            elif flex_profile_capture.match(line):
                flex_profile_match = flex_profile_capture.match(line)
                groups = flex_profile_match.groupdict()
                flex_profile = groups['flex_profile']
                flex_profile = change_data_type(value=flex_profile)
                ap_config_general_dict['ap_name'][ap_name_key].update({'flex_profile': flex_profile})
            # AP Filter name                                  : b8
            elif ap_filter_name_capture.match(line):
                ap_filter_name_match = ap_filter_name_capture.match(line)
                groups = ap_filter_name_match.groupdict()
                ap_filter_name = groups['ap_filter_name']
                ap_filter_name = change_data_type(value=ap_filter_name)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ap_filter_name': ap_filter_name})
            # Primary Cisco Controller Name                   : b7-wl-ewlc1
            elif primary_cisco_controller_name_capture.match(line):
                primary_cisco_controller_name_match = primary_cisco_controller_name_capture.match(line)
                groups = primary_cisco_controller_name_match.groupdict()
                primary_cisco_controller_name = groups['primary_cisco_controller_name']
                primary_cisco_controller_name = change_data_type(value=primary_cisco_controller_name)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'primary_cisco_controller_name': primary_cisco_controller_name})
            # Primary Cisco Controller IP Address             : 10.6.4.17
            elif primary_cisco_controller_ip_address_capture.match(line):
                primary_cisco_controller_ip_address_match = primary_cisco_controller_ip_address_capture.match(line)
                groups = primary_cisco_controller_ip_address_match.groupdict()
                primary_cisco_controller_ip_address = groups['primary_cisco_controller_ip_address']
                primary_cisco_controller_ip_address = change_data_type(value=primary_cisco_controller_ip_address)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'primary_cisco_controller_ip_address': primary_cisco_controller_ip_address})
            # Secondary Cisco Controller Name                 : b8-wl-wlc3
            elif secondary_cisco_controller_name_capture.match(line):
                secondary_cisco_controller_name_match = secondary_cisco_controller_name_capture.match(line)
                groups = secondary_cisco_controller_name_match.groupdict()
                secondary_cisco_controller_name = groups['secondary_cisco_controller_name']
                secondary_cisco_controller_name = change_data_type(value=secondary_cisco_controller_name)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'secondary_cisco_controller_name': secondary_cisco_controller_name})
            # Secondary Cisco Controller IP Address           : 10.6.7.16
            elif secondary_cisco_controller_ip_address_capture.match(line):
                secondary_cisco_controller_ip_address_match = secondary_cisco_controller_ip_address_capture.match(line)
                groups = secondary_cisco_controller_ip_address_match.groupdict()
                secondary_cisco_controller_ip_address = groups['secondary_cisco_controller_ip_address']
                secondary_cisco_controller_ip_address = change_data_type(value=secondary_cisco_controller_ip_address)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'secondary_cisco_controller_ip_address': secondary_cisco_controller_ip_address})
            # Tertiary Cisco Controller Name                  : b3-wl-wlc3
            elif tertiary_cisco_controller_name_capture.match(line):
                tertiary_cisco_controller_name_match = tertiary_cisco_controller_name_capture.match(line)
                groups = tertiary_cisco_controller_name_match.groupdict()
                tertiary_cisco_controller_name = groups['tertiary_cisco_controller_name']
                tertiary_cisco_controller_name = change_data_type(value=tertiary_cisco_controller_name)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'tertiary_cisco_controller_name': tertiary_cisco_controller_name})
            # Tertiary Cisco Controller IP Address            : 10.6.4.17
            elif tertiary_cisco_controller_ip_address_capture.match(line):
                tertiary_cisco_controller_ip_address_match = tertiary_cisco_controller_ip_address_capture.match(line)
                groups = tertiary_cisco_controller_ip_address_match.groupdict()
                tertiary_cisco_controller_ip_address = groups['tertiary_cisco_controller_ip_address']
                tertiary_cisco_controller_ip_address = change_data_type(value=tertiary_cisco_controller_ip_address)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'tertiary_cisco_controller_ip_address': tertiary_cisco_controller_ip_address})
            # Administrative State                            : Enabled
            elif administrative_state_capture.match(line):
                administrative_state_match = administrative_state_capture.match(line)
                groups = administrative_state_match.groupdict()
                administrative_state = groups['administrative_state']
                administrative_state = change_data_type(value=administrative_state)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'administrative_state': administrative_state})
            # Operation State                                 : Registered
            elif operation_state_capture.match(line):
                operation_state_match = operation_state_capture.match(line)
                groups = operation_state_match.groupdict()
                operation_state = groups['operation_state']
                operation_state = change_data_type(value=operation_state)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'operation_state': operation_state})
            # NAT External IP Address                         : 10.10.5.12
            elif nat_external_ip_address_capture.match(line):
                nat_external_ip_address_match = nat_external_ip_address_capture.match(line)
                groups = nat_external_ip_address_match.groupdict()
                nat_external_ip_address = groups['nat_external_ip_address']
                nat_external_ip_address = change_data_type(value=nat_external_ip_address)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'nat_external_ip_address': nat_external_ip_address})
            # AP Certificate type                             : Manufacturer Installed Certificate
            elif ap_certificate_type_capture.match(line):
                ap_certificate_type_match = ap_certificate_type_capture.match(line)
                groups = ap_certificate_type_match.groupdict()
                ap_certificate_type = groups['ap_certificate_type']
                ap_certificate_type = change_data_type(value=ap_certificate_type)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_certificate_type': ap_certificate_type})
            # AP Mode                                         : Local
            elif ap_mode_capture.match(line):
                ap_mode_match = ap_mode_capture.match(line)
                groups = ap_mode_match.groupdict()
                ap_mode = groups['ap_mode']
                ap_mode = change_data_type(value=ap_mode)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ap_mode': ap_mode})
            # AP VLAN tagging state                           : Disabled
            elif ap_vlan_tagging_state_capture.match(line):
                ap_vlan_tagging_state_match = ap_vlan_tagging_state_capture.match(line)
                groups = ap_vlan_tagging_state_match.groupdict()
                ap_vlan_tagging_state = groups['ap_vlan_tagging_state']
                ap_vlan_tagging_state = change_data_type(value=ap_vlan_tagging_state)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_vlan_tagging_state': ap_vlan_tagging_state})
            # AP VLAN tag                                     : 0
            elif ap_vlan_tag_capture.match(line):
                ap_vlan_tag_match = ap_vlan_tag_capture.match(line)
                groups = ap_vlan_tag_match.groupdict()
                ap_vlan_tag = groups['ap_vlan_tag']
                ap_vlan_tag = change_data_type(value=ap_vlan_tag)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ap_vlan_tag': ap_vlan_tag})
            # CAPWAP Preferred mode                           : IPv4
            elif capwap_preferred_mode_capture.match(line):
                capwap_preferred_mode_match = capwap_preferred_mode_capture.match(line)
                groups = capwap_preferred_mode_match.groupdict()
                capwap_preferred_mode = groups['capwap_preferred_mode']
                capwap_preferred_mode = change_data_type(value=capwap_preferred_mode)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'capwap_preferred_mode': capwap_preferred_mode})
            # CAPWAP UDP-Lite                                 : Not Configured
            elif capwap_udp_lite_capture.match(line):
                capwap_udp_lite_match = capwap_udp_lite_capture.match(line)
                groups = capwap_udp_lite_match.groupdict()
                capwap_udp_lite = groups['capwap_udp_lite']
                capwap_udp_lite = change_data_type(value=capwap_udp_lite)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'capwap_udp_lite': capwap_udp_lite})
            # AP Submode                                      : Not Configured
            elif ap_submode_capture.match(line):
                ap_submode_match = ap_submode_capture.match(line)
                groups = ap_submode_match.groupdict()
                ap_submode = groups['ap_submode']
                ap_submode = change_data_type(value=ap_submode)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ap_submode': ap_submode})
            # Office Extend Mode                              : Disabled
            elif office_extend_mode_capture.match(line):
                office_extend_mode_match = office_extend_mode_capture.match(line)
                groups = office_extend_mode_match.groupdict()
                office_extend_mode = groups['office_extend_mode']
                office_extend_mode = change_data_type(value=office_extend_mode)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'office_extend_mode': office_extend_mode})
            # Dhcp Server                                     : Disabled
            elif dhcp_server_capture.match(line):
                dhcp_server_match = dhcp_server_capture.match(line)
                groups = dhcp_server_match.groupdict()
                dhcp_server = groups['dhcp_server']
                dhcp_server = change_data_type(value=dhcp_server)
                ap_config_general_dict['ap_name'][ap_name_key].update({'dhcp_server': dhcp_server})
            # Remote AP Debug                                 : Disabled
            elif remote_ap_debug_capture.match(line):
                remote_ap_debug_match = remote_ap_debug_capture.match(line)
                groups = remote_ap_debug_match.groupdict()
                remote_ap_debug = groups['remote_ap_debug']
                remote_ap_debug = change_data_type(value=remote_ap_debug)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'remote_ap_debug': remote_ap_debug})
            # Logging Trap Severity Level                     : information
            elif logging_trap_severity_level_capture.match(line):
                logging_trap_severity_level_match = logging_trap_severity_level_capture.match(line)
                groups = logging_trap_severity_level_match.groupdict()
                logging_trap_severity_level = groups['logging_trap_severity_level']
                logging_trap_severity_level = change_data_type(value=logging_trap_severity_level)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'logging_trap_severity_level': logging_trap_severity_level})
            # Logging Syslog facility                         : kern
            elif logging_syslog_facility_capture.match(line):
                logging_syslog_facility_match = logging_syslog_facility_capture.match(line)
                groups = logging_syslog_facility_match.groupdict()
                logging_syslog_facility = groups['logging_syslog_facility']
                logging_syslog_facility = change_data_type(value=logging_syslog_facility)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'logging_syslog_facility': logging_syslog_facility})
            # Software Version                                : 10.145.1.9
            elif software_version_capture.match(line):
                software_version_match = software_version_capture.match(line)
                groups = software_version_match.groupdict()
                software_version = groups['software_version']
                software_version = change_data_type(value=software_version)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'software_version': software_version})
            # Boot Version                                    : 10.4.2.4
            elif boot_version_capture.match(line):
                boot_version_match = boot_version_capture.match(line)
                groups = boot_version_match.groupdict()
                boot_version = groups['boot_version']
                boot_version = change_data_type(value=boot_version)
                ap_config_general_dict['ap_name'][ap_name_key].update({'boot_version': boot_version})
            # Mini IOS Version                                : 0.0.0.0
            elif mini_ios_version_capture.match(line):
                mini_ios_version_match = mini_ios_version_capture.match(line)
                groups = mini_ios_version_match.groupdict()
                mini_ios_version = groups['mini_ios_version']
                mini_ios_version = change_data_type(value=mini_ios_version)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'mini_ios_version': mini_ios_version})
            # Stats Reporting Period                          : 0
            elif stats_reporting_period_capture.match(line):
                stats_reporting_period_match = stats_reporting_period_capture.match(line)
                groups = stats_reporting_period_match.groupdict()
                stats_reporting_period = groups['stats_reporting_period']
                stats_reporting_period = change_data_type(value=stats_reporting_period)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'stats_reporting_period': stats_reporting_period})
            # LED State                                       : Enabled
            elif led_state_capture.match(line):
                led_state_match = led_state_capture.match(line)
                groups = led_state_match.groupdict()
                led_state = groups['led_state']
                led_state = change_data_type(value=led_state)
                ap_config_general_dict['ap_name'][ap_name_key].update({'led_state': led_state})
            # LED Flash State                                 : Enabled
            elif led_flash_state_capture.match(line):
                led_flash_state_match = led_flash_state_capture.match(line)
                groups = led_flash_state_match.groupdict()
                led_flash_state = groups['led_flash_state']
                led_flash_state = change_data_type(value=led_flash_state)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'led_flash_state': led_flash_state})
            # LED Flash Timer                                 : 0
            elif led_flash_timer_capture.match(line):
                led_flash_timer_match = led_flash_timer_capture.match(line)
                groups = led_flash_timer_match.groupdict()
                led_flash_timer = groups['led_flash_timer']
                led_flash_timer = change_data_type(value=led_flash_timer)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'led_flash_timer': led_flash_timer})
            # MDNS Group Id                                   : 0
            elif mdns_group_id_capture.match(line):
                mdns_group_id_match = mdns_group_id_capture.match(line)
                groups = mdns_group_id_match.groupdict()
                mdns_group_id = groups['mdns_group_id']
                mdns_group_id = change_data_type(value=mdns_group_id)
                ap_config_general_dict['ap_name'][ap_name_key].update({'mdns_group_id': mdns_group_id})
            # MDNS Rule Name                                  :
            elif mdns_rule_name_capture.match(line):
                mdns_rule_name_match = mdns_rule_name_capture.match(line)
                groups = mdns_rule_name_match.groupdict()
                mdns_rule_name = groups['mdns_rule_name']
                mdns_rule_name = change_data_type(value=mdns_rule_name)
                ap_config_general_dict['ap_name'][ap_name_key].update({'mdns_rule_name': mdns_rule_name})
            # PoE Pre-Standard Switch                         : Disabled
            elif poe_pre_standard_switch_capture.match(line):
                poe_pre_standard_switch_match = poe_pre_standard_switch_capture.match(line)
                groups = poe_pre_standard_switch_match.groupdict()
                poe_pre_standard_switch = groups['poe_pre_standard_switch']
                poe_pre_standard_switch = change_data_type(value=poe_pre_standard_switch)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'poe_pre_standard_switch': poe_pre_standard_switch})
            # PoE Power Injector MAC Address                  : Disabled
            elif poe_power_injector_mac_address_capture.match(line):
                poe_power_injector_mac_address_match = poe_power_injector_mac_address_capture.match(line)
                groups = poe_power_injector_mac_address_match.groupdict()
                poe_power_injector_mac_address = groups['poe_power_injector_mac_address']
                poe_power_injector_mac_address = change_data_type(value=poe_power_injector_mac_address)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'poe_power_injector_mac_address': poe_power_injector_mac_address})
            # Power Type/Mode                                 : PoE/Full Power
            elif power_type_mode_capture.match(line):
                power_type_mode_match = power_type_mode_capture.match(line)
                groups = power_type_mode_match.groupdict()
                power_type_mode = groups['power_type_mode']
                power_type_mode = change_data_type(value=power_type_mode)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'power_type_mode': power_type_mode})
            # Number of Slots                                 : 3
            elif number_of_slots_capture.match(line):
                number_of_slots_match = number_of_slots_capture.match(line)
                groups = number_of_slots_match.groupdict()
                number_of_slots = groups['number_of_slots']
                number_of_slots = change_data_type(value=number_of_slots)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'number_of_slots': number_of_slots})
            # AP Model                                        : AIR-AP4800-D-K9
            elif ap_model_capture.match(line):
                ap_model_match = ap_model_capture.match(line)
                groups = ap_model_match.groupdict()
                ap_model = groups['ap_model']
                ap_model = change_data_type(value=ap_model)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ap_model': ap_model})
            # IOS Version                                     : 10.145.1.9
            elif ios_version_capture.match(line):
                ios_version_match = ios_version_capture.match(line)
                groups = ios_version_match.groupdict()
                ios_version = groups['ios_version']
                ios_version = change_data_type(value=ios_version)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ios_version': ios_version})
            # Reset Button                                    : Disabled
            elif reset_button_capture.match(line):
                reset_button_match = reset_button_capture.match(line)
                groups = reset_button_match.groupdict()
                reset_button = groups['reset_button']
                reset_button = change_data_type(value=reset_button)
                ap_config_general_dict['ap_name'][ap_name_key].update({'reset_button': reset_button})
            # AP Serial Number                                : FGL2102AZZZ
            elif ap_serial_number_capture.match(line):
                ap_serial_number_match = ap_serial_number_capture.match(line)
                groups = ap_serial_number_match.groupdict()
                ap_serial_number = groups['ap_serial_number']
                ap_serial_number = change_data_type(value=ap_serial_number)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_serial_number': ap_serial_number})
            # Management Frame Validation                     : Capable
            elif management_frame_validation_capture.match(line):
                management_frame_validation_match = management_frame_validation_capture.match(line)
                groups = management_frame_validation_match.groupdict()
                management_frame_validation = groups['management_frame_validation']
                management_frame_validation = change_data_type(value=management_frame_validation)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'management_frame_validation': management_frame_validation})
            # Management Frame Protection                     : Capable
            elif management_frame_protection_capture.match(line):
                management_frame_protection_match = management_frame_protection_capture.match(line)
                groups = management_frame_protection_match.groupdict()
                management_frame_protection = groups['management_frame_protection']
                management_frame_protection = change_data_type(value=management_frame_protection)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'management_frame_protection': management_frame_protection})
            # AP User Name                                    : admin
            elif ap_user_name_capture.match(line):
                ap_user_name_match = ap_user_name_capture.match(line)
                groups = ap_user_name_match.groupdict()
                ap_user_name = groups['ap_user_name']
                ap_user_name = change_data_type(value=ap_user_name)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ap_user_name': ap_user_name})
            # AP 802.1X User Mode                             : Global
            elif ap_802_1x_user_mode_capture.match(line):
                ap_802_1x_user_mode_match = ap_802_1x_user_mode_capture.match(line)
                groups = ap_802_1x_user_mode_match.groupdict()
                ap_802_1x_user_mode = groups['ap_802_1x_user_mode']
                ap_802_1x_user_mode = change_data_type(value=ap_802_1x_user_mode)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_802_1x_user_mode': ap_802_1x_user_mode})
            # AP 802.1X User Name                             : Not Configured
            elif ap_802_1x_user_name_capture.match(line):
                ap_802_1x_user_name_match = ap_802_1x_user_name_capture.match(line)
                groups = ap_802_1x_user_name_match.groupdict()
                ap_802_1x_user_name = groups['ap_802_1x_user_name']
                ap_802_1x_user_name = change_data_type(value=ap_802_1x_user_name)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_802_1x_user_name': ap_802_1x_user_name})
            # Cisco AP System Logging Host                    : 10.16.19.6
            elif cisco_ap_system_logging_host_capture.match(line):
                cisco_ap_system_logging_host_match = cisco_ap_system_logging_host_capture.match(line)
                groups = cisco_ap_system_logging_host_match.groupdict()
                cisco_ap_system_logging_host = groups['cisco_ap_system_logging_host']
                cisco_ap_system_logging_host = change_data_type(value=cisco_ap_system_logging_host)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'cisco_ap_system_logging_host': cisco_ap_system_logging_host})
            # Cisco AP Secured Logging TLS mode               : Disabled
            elif cisco_ap_secured_logging_tls_mode_capture.match(line):
                cisco_ap_secured_logging_tls_mode_match = cisco_ap_secured_logging_tls_mode_capture.match(line)
                groups = cisco_ap_secured_logging_tls_mode_match.groupdict()
                cisco_ap_secured_logging_tls_mode = groups['cisco_ap_secured_logging_tls_mode']
                cisco_ap_secured_logging_tls_mode = change_data_type(value=cisco_ap_secured_logging_tls_mode)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'cisco_ap_secured_logging_tls_mode': cisco_ap_secured_logging_tls_mode})
            # AP Up Time                                      : 3 days 9 hours 44 minutes 18 seconds
            elif ap_up_time_capture.match(line):
                ap_up_time_match = ap_up_time_capture.match(line)
                groups = ap_up_time_match.groupdict()
                ap_up_time = groups['ap_up_time']
                ap_up_time = change_data_type(value=ap_up_time)
                ap_config_general_dict['ap_name'][ap_name_key].update({'ap_up_time': ap_up_time})
            # AP CAPWAP Up Time                               : 3 days 9 hours 37 minutes 20 seconds
            elif ap_capwap_up_time_capture.match(line):
                ap_capwap_up_time_match = ap_capwap_up_time_capture.match(line)
                groups = ap_capwap_up_time_match.groupdict()
                ap_capwap_up_time = groups['ap_capwap_up_time']
                ap_capwap_up_time = change_data_type(value=ap_capwap_up_time)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_capwap_up_time': ap_capwap_up_time})
            # Join Date and Time                              : 08/14/2020 19:48:09
            elif join_date_and_time_capture.match(line):
                join_date_and_time_match = join_date_and_time_capture.match(line)
                groups = join_date_and_time_match.groupdict()
                join_date_and_time = groups['join_date_and_time']
                join_date_and_time = change_data_type(value=join_date_and_time)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'join_date_and_time': join_date_and_time})
            # Join Taken Time                                 : 6 minutes 57 seconds
            elif join_taken_time_capture.match(line):
                join_taken_time_match = join_taken_time_capture.match(line)
                groups = join_taken_time_match.groupdict()
                join_taken_time = groups['join_taken_time']
                join_taken_time = change_data_type(value=join_taken_time)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'join_taken_time': join_taken_time})
            # Join Priority                                   : 1
            elif join_priority_capture.match(line):
                join_priority_match = join_priority_capture.match(line)
                groups = join_priority_match.groupdict()
                join_priority = groups['join_priority']
                join_priority = change_data_type(value=join_priority)
                ap_config_general_dict['ap_name'][ap_name_key].update({'join_priority': join_priority})
            # AP Link Latency                                 : Disable
            elif ap_link_latency_capture.match(line):
                ap_link_latency_match = ap_link_latency_capture.match(line)
                groups = ap_link_latency_match.groupdict()
                ap_link_latency = groups['ap_link_latency']
                ap_link_latency = change_data_type(value=ap_link_latency)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_link_latency': ap_link_latency})
            # AP Lag Configuration Status                     : Disabled
            elif ap_lag_configuration_status_capture.match(line):
                ap_lag_configuration_status_match = ap_lag_configuration_status_capture.match(line)
                groups = ap_lag_configuration_status_match.groupdict()
                ap_lag_configuration_status = groups['ap_lag_configuration_status']
                ap_lag_configuration_status = change_data_type(value=ap_lag_configuration_status)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_lag_configuration_status': ap_lag_configuration_status})
            # Lag Support for AP                              : Yes
            elif lag_support_for_ap_capture.match(line):
                lag_support_for_ap_match = lag_support_for_ap_capture.match(line)
                groups = lag_support_for_ap_match.groupdict()
                lag_support_for_ap = groups['lag_support_for_ap']
                lag_support_for_ap = change_data_type(value=lag_support_for_ap)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'lag_support_for_ap': lag_support_for_ap})
            # Rogue Detection                                 : Enabled
            elif rogue_detection_capture.match(line):
                rogue_detection_match = rogue_detection_capture.match(line)
                groups = rogue_detection_match.groupdict()
                rogue_detection = groups['rogue_detection']
                rogue_detection = change_data_type(value=rogue_detection)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'rogue_detection': rogue_detection})
            # Rogue Containment auto-rate                     : Disabled
            elif rogue_containment_auto_rate_capture.match(line):
                rogue_containment_auto_rate_match = rogue_containment_auto_rate_capture.match(line)
                groups = rogue_containment_auto_rate_match.groupdict()
                rogue_containment_auto_rate = groups['rogue_containment_auto_rate']
                rogue_containment_auto_rate = change_data_type(value=rogue_containment_auto_rate)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'rogue_containment_auto_rate': rogue_containment_auto_rate})
            # Rogue Containment of standalone flexconnect APs : Disabled
            elif rogue_containment_of_standalone_flexconnect_aps_capture.match(line):
                rogue_containment_of_standalone_flexconnect_aps_match = rogue_containment_of_standalone_flexconnect_aps_capture.match(
                    line)
                groups = rogue_containment_of_standalone_flexconnect_aps_match.groupdict()
                rogue_containment_of_standalone_flexconnect_aps = groups[
                    'rogue_containment_of_standalone_flexconnect_aps']
                rogue_containment_of_standalone_flexconnect_aps = change_data_type(
                    value=rogue_containment_of_standalone_flexconnect_aps)
                ap_config_general_dict['ap_name'][ap_name_key].update({
                    'rogue_containment_of_standalone_flexconnect_aps': rogue_containment_of_standalone_flexconnect_aps})
            # Rogue Detection Report Interval                 : 10
            elif rogue_detection_report_interval_capture.match(line):
                rogue_detection_report_interval_match = rogue_detection_report_interval_capture.match(line)
                groups = rogue_detection_report_interval_match.groupdict()
                rogue_detection_report_interval = groups['rogue_detection_report_interval']
                rogue_detection_report_interval = change_data_type(value=rogue_detection_report_interval)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'rogue_detection_report_interval': rogue_detection_report_interval})
            # Rogue AP minimum RSSI                           : -70
            elif rogue_ap_minimum_rssi_capture.match(line):
                rogue_ap_minimum_rssi_match = rogue_ap_minimum_rssi_capture.match(line)
                groups = rogue_ap_minimum_rssi_match.groupdict()
                rogue_ap_minimum_rssi = groups['rogue_ap_minimum_rssi']
                rogue_ap_minimum_rssi = change_data_type(value=rogue_ap_minimum_rssi)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'rogue_ap_minimum_rssi': rogue_ap_minimum_rssi})
            # Rogue AP minimum transient time                 : 0
            elif rogue_ap_minimum_transient_time_capture.match(line):
                rogue_ap_minimum_transient_time_match = rogue_ap_minimum_transient_time_capture.match(line)
                groups = rogue_ap_minimum_transient_time_match.groupdict()
                rogue_ap_minimum_transient_time = groups['rogue_ap_minimum_transient_time']
                rogue_ap_minimum_transient_time = change_data_type(value=rogue_ap_minimum_transient_time)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'rogue_ap_minimum_transient_time': rogue_ap_minimum_transient_time})
            # AP TCP MSS Adjust                               : Enabled
            elif ap_tcp_mss_adjust_capture.match(line):
                ap_tcp_mss_adjust_match = ap_tcp_mss_adjust_capture.match(line)
                groups = ap_tcp_mss_adjust_match.groupdict()
                ap_tcp_mss_adjust = groups['ap_tcp_mss_adjust']
                ap_tcp_mss_adjust = change_data_type(value=ap_tcp_mss_adjust)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_tcp_mss_adjust': ap_tcp_mss_adjust})
            # AP TCP MSS Size                                 : 1250
            elif ap_tcp_mss_size_capture.match(line):
                ap_tcp_mss_size_match = ap_tcp_mss_size_capture.match(line)
                groups = ap_tcp_mss_size_match.groupdict()
                ap_tcp_mss_size = groups['ap_tcp_mss_size']
                ap_tcp_mss_size = change_data_type(value=ap_tcp_mss_size)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_tcp_mss_size': ap_tcp_mss_size})
            # AP IPv6 TCP MSS Adjust                          : Enabled
            elif ap_ipv6_tcp_mss_adjust_capture.match(line):
                ap_ipv6_tcp_mss_adjust_match = ap_ipv6_tcp_mss_adjust_capture.match(line)
                groups = ap_ipv6_tcp_mss_adjust_match.groupdict()
                ap_ipv6_tcp_mss_adjust = groups['ap_ipv6_tcp_mss_adjust']
                ap_ipv6_tcp_mss_adjust = change_data_type(value=ap_ipv6_tcp_mss_adjust)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_ipv6_tcp_mss_adjust': ap_ipv6_tcp_mss_adjust})
            # AP IPv6 TCP MSS Size                            : 1250
            elif ap_ipv6_tcp_mss_size_capture.match(line):
                ap_ipv6_tcp_mss_size_match = ap_ipv6_tcp_mss_size_capture.match(line)
                groups = ap_ipv6_tcp_mss_size_match.groupdict()
                ap_ipv6_tcp_mss_size = groups['ap_ipv6_tcp_mss_size']
                ap_ipv6_tcp_mss_size = change_data_type(value=ap_ipv6_tcp_mss_size)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ap_ipv6_tcp_mss_size': ap_ipv6_tcp_mss_size})
            # Hyperlocation Admin Status                      : Disabled
            elif hyperlocation_admin_status_capture.match(line):
                hyperlocation_admin_status_match = hyperlocation_admin_status_capture.match(line)
                groups = hyperlocation_admin_status_match.groupdict()
                hyperlocation_admin_status = groups['hyperlocation_admin_status']
                hyperlocation_admin_status = change_data_type(value=hyperlocation_admin_status)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'hyperlocation_admin_status': hyperlocation_admin_status})
            # Retransmit count                                : 5
            elif retransmit_count_capture.match(line):
                retransmit_count_match = retransmit_count_capture.match(line)
                groups = retransmit_count_match.groupdict()
                retransmit_count = groups['retransmit_count']
                retransmit_count = change_data_type(value=retransmit_count)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'retransmit_count': retransmit_count})
            # Retransmit interval                             : 3
            elif retransmit_interval_capture.match(line):
                retransmit_interval_match = retransmit_interval_capture.match(line)
                groups = retransmit_interval_match.groupdict()
                retransmit_interval = groups['retransmit_interval']
                retransmit_interval = change_data_type(value=retransmit_interval)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'retransmit_interval': retransmit_interval})
            # Fabric status                                   : Disabled
            elif fabric_status_capture.match(line):
                fabric_status_match = fabric_status_capture.match(line)
                groups = fabric_status_match.groupdict()
                fabric_status = groups['fabric_status']
                fabric_status = change_data_type(value=fabric_status)
                ap_config_general_dict['ap_name'][ap_name_key].update({'fabric_status': fabric_status})
            # FIPS status                                     : Disabled
            elif fips_status_capture.match(line):
                fips_status_match = fips_status_capture.match(line)
                groups = fips_status_match.groupdict()
                fips_status = groups['fips_status']
                fips_status = change_data_type(value=fips_status)
                ap_config_general_dict['ap_name'][ap_name_key].update({'fips_status': fips_status})
            # WLANCC status                                   : Disabled
            elif wlancc_status_capture.match(line):
                wlancc_status_match = wlancc_status_capture.match(line)
                groups = wlancc_status_match.groupdict()
                wlancc_status = groups['wlancc_status']
                wlancc_status = change_data_type(value=wlancc_status)
                ap_config_general_dict['ap_name'][ap_name_key].update({'wlancc_status': wlancc_status})
            # USB Module Type                                 : USB Module
            elif usb_module_type_capture.match(line):
                usb_module_type_match = usb_module_type_capture.match(line)
                groups = usb_module_type_match.groupdict()
                usb_module_type = groups['usb_module_type']
                usb_module_type = change_data_type(value=usb_module_type)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'usb_module_type': usb_module_type})
            # USB Module State                                : Enabled
            elif usb_module_state_capture.match(line):
                usb_module_state_match = usb_module_state_capture.match(line)
                groups = usb_module_state_match.groupdict()
                usb_module_state = groups['usb_module_state']
                usb_module_state = change_data_type(value=usb_module_state)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'usb_module_state': usb_module_state})
            # USB Operational State                           : Disabled
            elif usb_operational_state_capture.match(line):
                usb_operational_state_match = usb_operational_state_capture.match(line)
                groups = usb_operational_state_match.groupdict()
                usb_operational_state = groups['usb_operational_state']
                usb_operational_state = change_data_type(value=usb_operational_state)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'usb_operational_state': usb_operational_state})
            # USB Override                                    : Disabled
            elif usb_override_capture.match(line):
                usb_override_match = usb_override_capture.match(line)
                groups = usb_override_match.groupdict()
                usb_override = groups['usb_override']
                usb_override = change_data_type(value=usb_override)
                ap_config_general_dict['ap_name'][ap_name_key].update({'usb_override': usb_override})
            # GAS rate limit Admin status                     : Disabled
            elif gas_rate_limit_admin_status_capture.match(line):
                gas_rate_limit_admin_status_match = gas_rate_limit_admin_status_capture.match(line)
                groups = gas_rate_limit_admin_status_match.groupdict()
                gas_rate_limit_admin_status = groups['gas_rate_limit_admin_status']
                gas_rate_limit_admin_status = change_data_type(value=gas_rate_limit_admin_status)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'gas_rate_limit_admin_status': gas_rate_limit_admin_status})
            # WPA3 Capability                                 : Enabled
            elif wpa3_capability_capture.match(line):
                wpa3_capability_match = wpa3_capability_capture.match(line)
                groups = wpa3_capability_match.groupdict()
                wpa3_capability = groups['wpa3_capability']
                wpa3_capability = change_data_type(value=wpa3_capability)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'wpa3_capability': wpa3_capability})
            # EWC-AP Capability                               : Disabled
            elif ewc_ap_capability_capture.match(line):
                ewc_ap_capability_match = ewc_ap_capability_capture.match(line)
                groups = ewc_ap_capability_match.groupdict()
                ewc_ap_capability = groups['ewc_ap_capability']
                ewc_ap_capability = change_data_type(value=ewc_ap_capability)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'ewc_ap_capability': ewc_ap_capability})
            # AWIPS Capability                                : Enabled
            elif awips_capability_capture.match(line):
                awips_capability_match = awips_capability_capture.match(line)
                groups = awips_capability_match.groupdict()
                awips_capability = groups['awips_capability']
                awips_capability = change_data_type(value=awips_capability)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'awips_capability': awips_capability})
            # Proxy Hostname                                  : Not Configured
            elif proxy_hostname_capture.match(line):
                proxy_hostname_match = proxy_hostname_capture.match(line)
                groups = proxy_hostname_match.groupdict()
                proxy_hostname = groups['proxy_hostname']
                proxy_hostname = change_data_type(value=proxy_hostname)
                ap_config_general_dict['ap_name'][ap_name_key].update({'proxy_hostname': proxy_hostname})
            # Proxy Port                                      : Not Configured
            elif proxy_port_capture.match(line):
                proxy_port_match = proxy_port_capture.match(line)
                groups = proxy_port_match.groupdict()
                proxy_port = groups['proxy_port']
                proxy_port = change_data_type(value=proxy_port)
                ap_config_general_dict['ap_name'][ap_name_key].update({'proxy_port': proxy_port})
            # Proxy NO_PROXY list                             : Not Configured
            elif proxy_no_proxy_list_capture.match(line):
                proxy_no_proxy_list_match = proxy_no_proxy_list_capture.match(line)
                groups = proxy_no_proxy_list_match.groupdict()
                proxy_no_proxy_list = groups['proxy_no_proxy_list']
                proxy_no_proxy_list = change_data_type(value=proxy_no_proxy_list)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'proxy_no_proxy_list': proxy_no_proxy_list})
            # GRPC server status                              : Disabled
            elif grpc_server_status_capture.match(line):
                grpc_server_status_match = grpc_server_status_capture.match(line)
                groups = grpc_server_status_match.groupdict()
                grpc_server_status = groups['grpc_server_status']
                grpc_server_status = change_data_type(value=grpc_server_status)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'grpc_server_status': grpc_server_status})
            # Unencrypted Data Keep Alive                     : Enabled
            elif unencrypted_data_keep_alive_capture.match(line):
                unencrypted_data_keep_alive_match = unencrypted_data_keep_alive_capture.match(line)
                groups = unencrypted_data_keep_alive_match.groupdict()
                unencrypted_data_keep_alive = groups['unencrypted_data_keep_alive']
                unencrypted_data_keep_alive = change_data_type(value=unencrypted_data_keep_alive)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'unencrypted_data_keep_alive': unencrypted_data_keep_alive})
            # Local DHCP Server                               : Disabled
            elif local_dhcp_server_capture.match(line):
                local_dhcp_server_match = local_dhcp_server_capture.match(line)
                groups = local_dhcp_server_match.groupdict()
                local_dhcp_server = groups['local_dhcp_server']
                local_dhcp_server = change_data_type(value=local_dhcp_server)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'local_dhcp_server': local_dhcp_server})
            # Traffic Distribution Statistics Capability      : Enabled
            elif traffic_distribution_statistics_capability_capture.match(line):
                traffic_distribution_statistics_capability_match = traffic_distribution_statistics_capability_capture.match(
                    line)
                groups = traffic_distribution_statistics_capability_match.groupdict()
                traffic_distribution_statistics_capability = groups['traffic_distribution_statistics_capability']
                traffic_distribution_statistics_capability = change_data_type(
                    value=traffic_distribution_statistics_capability)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'traffic_distribution_statistics_capability': traffic_distribution_statistics_capability})
            # Dual DFS Statistics                             : Disabled
            elif dual_dfs_statistics_capture.match(line):
                dual_dfs_statistics_match = dual_dfs_statistics_capture.match(line)
                groups = dual_dfs_statistics_match.groupdict()
                dual_dfs_statistics = groups['dual_dfs_statistics']
                dual_dfs_statistics = change_data_type(value=dual_dfs_statistics)
                ap_config_general_dict['ap_name'][ap_name_key].update(
                    {'dual_dfs_statistics': dual_dfs_statistics})
        return ap_config_general_dict


# ========================
# Schema for:
#  * 'show ap tag summary'
# ========================
class ShowApTagSummarySchema(MetaParser):
    """Schema for show ap tag summary."""

    schema = {
        "ap_name": {
            Any(): {
                "ap_mac": str,
                "site_tag_name": str,
                "policy_tag_name": str,
                "rf_tag_name": str,
                "misconfigured": str,
                "tag_source": str,
            },
        },
        "number_of_aps": int,
    }


# ========================
# Parser for:
#  * 'show ap tag summary'
# ========================
class ShowApTagSummary(ShowApTagSummarySchema):
    """Parser for show ap tag summary"""

    cli_command = 'show ap tag summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)

        else:
            out = output

        # Number of APs: 20

        # AP Name                 AP Mac           Site Tag Name                     Policy Tag Name                   RF Tag Name                       Misconfigured    Tag Source
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # b25a-13-cap10         3c41.0fff.3f83   default-site-tag-fabric           PT_Fabri_B25_B25-1_fe778      Standard                          No               Static
        # b25b-12-cap01         3c41.0fff.4773   default-site-tag-fabric           PT_Fabri_B25_B25-1_fe778      Standard                          No               Static
        # b25b-11-cap01         3c41.0fff.4c7f   default-site-tag-fabric           PT_Fabri_B25_B25-1_fe778      Standard                          No               Static
        # b25a-12-cap07         3c41.0fff.4cd7   default-site-tag-fabric           PT_Fabri_B25_B25-1_fe778      Standard                          No               Static
        # b25a-11-cap05         3c41.0fff.4cdf   default-site-tag-fabric           PT_Fabri_B25_B25-1_fe778      Standard                          No               Static
        # b25a-11-cap04         3c41.0fff.4d4b   default-site-tag-fabric           PT_Fabri_B25_B25-1_fe778      Standard                          No               Static
        # b25a-12-cap08         3c41.0fff.4d63   default-site-tag-fabric           PT_Fabri_B25_B25-1_fe778      Standard                          No               Static
        # ...OUTPUT OMITTED..

        # Number of APs: 20
        ap_number_capture = re.compile(r"^Number of APs: (?P<number_of_aps>\d+)$")

        # b25a-13-cap10         3c41.0fff.3f83   default-site-tag-fabric           PT_Fabri_B25_B25-1_fe778      Standard                          No               Static
        ap_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<ap_mac>\S{4}\.\S{4}\.\S{4})\s+(?P<site_tag_name>\S+)\s+(?P<policy_tag_name>\S+)\s+(?P<rf_tag_name>\S+)\s+(?P<misconfigured>\S+)\s+(?P<tag_source>\S+)$"
        )

        ap_info_obj = {}

        for line in out.splitlines():
            line = line.strip()

            match = ap_number_capture.match(line)
            if match:
                group = match.groupdict()

                # format str to int
                group["number_of_aps"] = int(group["number_of_aps"])

                ap_info_obj.update(group)

                continue

            match = ap_info_capture.match(line)
            if match:
                group = match.groupdict()

                # pull a key from group to use as new_key
                new_key = "ap_name"
                new_group = {group[new_key]: {}}

                # update and pop new_key
                new_group[group[new_key]].update(group)
                new_group[group[new_key]].pop(new_key)

                ap_info_obj.setdefault(new_key, {})

                ap_info_obj[new_key].update(new_group)

                continue

        return ap_info_obj    
        

class ShowApStatusSchema(MetaParser):
    """Schema for show ap status."""

    schema = {
        "ap_name": {
            str: {
                "status": str,
                "mode": str,
                "country": str
            }
        }
    }

class ShowApStatus(ShowApStatusSchema):
    """Parser for show ap status"""

    cli_command = 'show ap status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # AP002C.C862.E708                    Enabled    Local             US
        p1 = re.compile(r"^(?P<ap_name>\S+)\s+(?P<status>\S+)\s+(?P<mode>\S+)\s+(?P<country>\S+)$")

        ap_dict = {}
        ret_dict = {}

        for line in output.splitlines():
            line = line.rstrip()
            # AP002C.C862.E708                    Enabled    Local             US
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ap_dict = ret_dict.setdefault('ap_name', {}).\
                    setdefault(groups['ap_name'], {})
                ap_dict.update({
                    'status': groups['status'],
                    'mode': groups['mode'],
                    'country': groups['country']
                })
        return ret_dict

