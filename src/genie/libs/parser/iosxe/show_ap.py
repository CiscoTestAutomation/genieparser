import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


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
        # a121-cap22                       2      9130AXI   a4b2.32ff.2db9  2c57.41ff.b979  Fab A  UK          10.6.33.106                               Registered
        ap_neighbor_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<slots_count>\d+)\s+(?P<ap_model>\S+)\s+(?P<ethernet_mac>\S+)\s+(?P<radio_mac>\S+)(?P<location>.*)\s+(?P<ap_ip_address>\d+\.\d+\.\d+\.\d+)\s+(?P<state>(Registered))")

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
            "wlc_leader_name": str,
            "wlc_leader_ip": str,
            "last_run_seconds": int,
            "dca_level": str,
            "dca_db": int,
            "chan_width_mhz": int,
            "max_chan_width_mhz": int,
            "dca_min_energy_dbm": float,
            "channel_energy_levels" : {
                "min_dbm": float,
                "average_dbm": float,
                "max_dbm": float,               
            },
            "channel_dwell_times": {
                "minimum": str,
                "average": str,
                "max": str,
            },
            "allowed_channel_list": str,
            "unused_channel_list": str
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
        #   Channel Assignment Leader                  : sj-00a-ewlc1 (10.7.5.133)
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
        #     Minimum                                  : 4 hours 9 minutes 54 seconds
        #     Average                                  : 4 hours 24 minutes 54 seconds
        #     Maximum                                  : 4 hours 26 minutes 35 seconds
        #   802.11a 5 GHz Auto-RF Channel List
        #     Allowed Channel List                     : 36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161
        #     Unused Channel List                      : 165

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
        chan_assn_leader_capture = re.compile(
            r"^Channel\s+Assignment\s+Leader\s+:\s+(?P<wlc_leader_name>\S+)\s+(?P<wlc_leader_ip>\(\d+\.\d+\.\d+\.\d+\))$")
        #   Last Run                                   : 15995 seconds ago
        last_run_capture = re.compile(r"^Last\s+Run\s+:\s+(?P<last_run_seconds>\d+)\s+seconds\s+ago$")
        #   DCA Sensitivity Level                      : MEDIUM : 15 dB
        dca_sensitivity_capture = re.compile(
            r"^DCA\s+Sensitivity\s+Level\s+:\s+(?P<dca_level>\S+)\s+:\s+(?P<dca_db>\d+)\s+dB$")
        #   DCA 802.11n/ac Channel Width               : 80 MHz
        dca_chan_width_capture = re.compile(r"^DCA\s+802\.11n\/ac\s+Channel\s+Width\s+:\s+(?P<chan_width>\d+)\s+MHz$")
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
        chan_dwell_minimum_capture = re.compile(
            r"^Minimum\s+:\s+(?P<chan_dwell_min_hours>\d+)\s+hours\s+(?P<chan_dwell_min_minutes>\d+)\s+minutes\s+(?P<chan_dwell_min_seconds>\d+)\s+seconds$")
        #     Average                                  : 4 hours 24 minutes 54 seconds
        chan_dwell_average_capture = re.compile(
            r"^Average\s+:\s+(?P<chan_dwell_average_hours>\d+)\s+hours\s+(?P<chan_dwell_average_minutes>\d+)\s+minutes\s+(?P<chan_dwell_average_second>\d+)\s+seconds$")
        #     Maximum                                  : 4 hours 26 minutes 35 seconds
        chan_dwell_max_capture = re.compile(
            r"^Maximum\s+:\s+(?P<chan_dwell_max_hours>\d+)\s+hours\s+(?P<chan_dwell_max_minutes>\d+)\s+minutes\s+(?P<chan_dwell_max_seconds>\d+)\s+seconds$")
        #   802.11a 5 GHz Auto-RF Channel List
        channel_list_capture = re.compile(r"^802.11a\s+5\s+GHz\s+Auto-RF\s+Channel\s+List$")
        #     Allowed Channel List                     : 36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161
        allowed_channel_list_capture = re.compile(r"^Allowed\s+Channel\s+List\s+:\s+(?P<allowed_channel_list>\S+)$")
        #     Unused Channel List                      : 165
        unused_channel_list_capture = re.compile(r"^Unused\s+Channel\s+List\s+:\s+(?P<unused_channel_list>\d+)$")


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
            #   Channel Assignment Leader                  : sj-00a-ewlc1 (10.7.5.133)
            elif chan_assn_leader_capture.match(line):
                chan_assn_leader_capture_match = chan_assn_leader_capture.match(line)
                groups = chan_assn_leader_capture_match.groupdict()
                wlc_leader_name = groups['wlc_leader_name']
                wlc_leader_ip = groups['wlc_leader_ip']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'wlc_leader_name': wlc_leader_name})
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
            #   DCA 802.11n/ac Channel Width               : 80 MHz
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
            elif chan_dwell_minimum_capture.match(line):
                print(line)
                chan_dwell_minimum_capture_match = chan_dwell_minimum_capture.match(line)
                groups = chan_dwell_minimum_capture_match.groupdict()
                chan_dwell_min_hours = groups['chan_dwell_min_hours']
                chan_dwell_min_minutes = groups['chan_dwell_min_minutes']
                chan_dwell_min_seconds = groups['chan_dwell_min_seconds']
                chan_dwell_minimum = chan_dwell_min_hours + ' hours ' + chan_dwell_min_minutes + ' minutes ' + chan_dwell_min_seconds + ' seconds'
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_dwell_times"].update({'minimum': chan_dwell_minimum})
                continue
            #     Average                                  : 4 hours 24 minutes 54 seconds
            elif chan_dwell_average_capture.match(line):
                chan_dwell_average_capture_match = chan_dwell_average_capture.match(line)
                groups = chan_dwell_average_capture_match.groupdict()
                chan_dwell_average_hours = groups['chan_dwell_average_hours']
                chan_dwell_average_minutes = groups['chan_dwell_average_minutes']
                chan_dwell_average_seconds = groups['chan_dwell_average_second']
                chan_dwell_average = chan_dwell_average_hours + ' hours ' + chan_dwell_average_minutes + ' minutes ' + chan_dwell_average_seconds + ' seconds'
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_dwell_times"].update({'average': chan_dwell_average})
                continue
            #     Maximum                                  : 4 hours 26 minutes 35 seconds
            elif chan_dwell_max_capture.match(line):
                chan_dwell_max_capture_match = chan_dwell_max_capture.match(line)
                groups = chan_dwell_max_capture_match.groupdict()
                chan_dwell_max_hours = groups['chan_dwell_max_hours']
                chan_dwell_max_minutes = groups['chan_dwell_max_minutes']
                chan_dwell_max_seconds = groups['chan_dwell_max_seconds']
                chan_dwell_max = chan_dwell_max_hours + ' hours ' + chan_dwell_max_minutes + ' minutes ' + chan_dwell_max_seconds + ' seconds'
                show_ap_dot11_5ghz_channel_dict['channel_assignment']["channel_dwell_times"].update({'max': chan_dwell_max})
                continue
            #   802.11a 5 GHz Auto-RF Channel List
            elif channel_list_capture.match(line):
                channel_list_capture_match = channel_list_capture.match(line)
                groups = channel_list_capture_match.groupdict()
                continue
            #     Allowed Channel List                     : 36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161
            elif allowed_channel_list_capture.match(line):
                allowed_channel_list_capture_match = allowed_channel_list_capture.match(line)
                groups = allowed_channel_list_capture_match.groupdict()
                allowed_channel_list = groups['allowed_channel_list']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update(
                    {'allowed_channel_list': allowed_channel_list})
                continue
            #     Unused Channel List                      : 165
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
                "channel": str
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
        # AP Name                           Mac Address     Slot    Admin State    Oper State    Width  Txpwr           Channel
        # ---------------------------------------------------------------------------------------------------------------------------------
        # ab-1-test-4800                 5c50.1501.40e0  1       Enabled        Down          20     *1/8 (23 dBm)   (36)*
        # ab21-cap40                    5c50.15f5.e5c0  1       Enabled        Up            20     *7/8 (6 dBm)    (100)*
        # ab12-cap2                     5c50.1504.7b20  1       Enabled        Up            20     *7/8 (6 dBm)    (116)*
        # ab21-cap36                    5c50.1504.87e0  1       Enabled        Up            20     *7/8 (6 dBm)    (100)*
        # ab21-cap28                    5c50.1504.8920  1       Enabled        Up            20     *7/8 (6 dBm)    (120)*
        # ab31-cap26                    5c50.1504.8940  1       Enabled        Up            20     *6/8 (9 dBm)    (128)*
        # ab22-cap16                    5c50.1504.89a0  1       Enabled        Up            20     *7/8 (8 dBm)    (48)*
        # ab22-cap24                    5c50.1504.89e0  1       Enabled        Up            20     *7/8 (8 dBm)    (36)*
        # ab22-cap18                    5c50.1504.8ac0  1       Enabled        Up            20     *7/8 (6 dBm)    (124)*
        # ab32-cap13                    5c50.1504.8bc0  1       Enabled        Up            20     *6/8 (9 dBm)    (124)*
        #
        # AP Name                           Mac Address     Slot    Admin State    Oper State    Width  Txpwr           Channel
        # ---------------------------------------------------------------------------------------------------------------------------------
        # ab22-cap10                    5c50.1504.8be0  1       Enabled        Up            20     *6/8 (9 dBm)    (132)*
        # ab11-cap18                    5c50.1504.8c20  1       Enabled        Up            20     *7/8 (8 dBm)    (48)*
        # ab22-cap8                     5c50.1504.8c40  1       Enabled        Up            20     *7/8 (8 dBm)    (149)*
        # ab22-cap22                    5c50.1504.8ce0  1       Enabled        Up            20     *8/8 (5 dBm)    (40)*
        # ab22-cap6                     5c50.1504.8d80  1       Enabled        Up            20     *7/8 (6 dBm)    (100)*
        # ab31-cap29                    5c50.1504.8dc0  1       Enabled        Up            20     *5/8 (12 dBm)   (52)*
        # ab21-cap33                    5c50.1504.8de0  1       Enabled        Up            20     *7/8 (8 dBm)    (36)*
        # ab31-cap21                    5c50.1504.8f20  1       Enabled        Up            20     *7/8 (6 dBm)    (116)*
        # ab21-cap27                    5c50.1504.8f60  1       Enabled        Up            20     *7/8 (6 dBm)    (132)*
        # ab21-cap35                    5c50.1504.aca0  1       Enabled        Up            20     *7/8 (6 dBm)    (140)*

        # AP Name                           Mac Address     Slot    Admin State    Oper State    Width  Txpwr           Channel
        ap_header_capture = re.compile(
            r"^AP\s+Name\s+Mac\s+Address\s+Slot\s+Admin\s+State\s+Oper\s+State\s+Width\s+Txpwr\s+Channel$")
        # ---------------------------------------------------------------------------------------------------------------------------------
        delimiter_capture = re.compile(
            r"^---------------------------------------------------------------------------------------------------------------------------------$")
        # ab22-cap10                    5c50.1504.8be0  1       Enabled        Up            20     *6/8 (9 dBm)    (132)*
        ap_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<mac_address>\S+)\s+(?P<slot>\d+)\s+(?P<admin_state>(Enabled|Disabled))"
                        r"\s+(?P<oper_state>\S+)\s+(?P<width>\d+)\s+(?P<tx_pwr>\*.*dBm\))\s+(?P<channel>\S+)$")

        for line in out.splitlines():
            line = line.strip()
            # AP Name                           Mac Address     Slot    Admin State    Oper State    Width  Txpwr           Channel
            if ap_header_capture.match(line):
                continue
            # ---------------------------------------------------------------------------------------------------------------------------------
            elif delimiter_capture.match(line):
                continue
            # ab22-cap10                    5c50.1504.8be0  1       Enabled        Up            20     *6/8 (9 dBm)    (132)*
            elif ap_info_capture.match(line):
                if not ap_dot11_5ghz_summ.get('ap_name'):
                    ap_dot11_5ghz_summ['ap_name'] = {}
                ap_info_capture_match = ap_info_capture.match(line)
                groups = ap_info_capture_match.groupdict()
                print(groups)
                ap_name = groups['ap_name']
                mac_address = groups['mac_address']
                slot = int(groups['slot'])
                admin_state = groups['admin_state']
                oper_state = groups['oper_state']
                width = int(groups['width'])
                tx_pwr = groups['tx_pwr']
                channel = groups['channel']
                ap_dot11_5ghz_summ['ap_name'].update({ap_name: {}})
                ap_dot11_5ghz_summ['ap_name'][ap_name]['mac_address'] = mac_address
                ap_dot11_5ghz_summ['ap_name'][ap_name]['slot'] = slot
                ap_dot11_5ghz_summ['ap_name'][ap_name]['admin_state'] = admin_state
                ap_dot11_5ghz_summ['ap_name'][ap_name]['oper_state'] = oper_state
                ap_dot11_5ghz_summ['ap_name'][ap_name]['width'] = width
                ap_dot11_5ghz_summ['ap_name'][ap_name]['tx_pwr'] = tx_pwr
                ap_dot11_5ghz_summ['ap_name'][ap_name]['channel'] = channel
                continue
            # print(ap_dot11_5ghz_summ)

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
