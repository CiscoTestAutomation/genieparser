import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===============================
# Schema for:
#  * 'show ap dot11 5ghz channel'
# ===============================
class ShowApDot115GhzChannelSchema(MetaParser):
    """Schema for show ap dot11 5ghz channel."""

    schema = {
        "channel_assignment": {
            "chan_assn_mode": str,
            "chan_upd_int": int,
            "anchor_time_hour": int,
            "channel_noise": "Enable",
            "channel_interference": str,
            "channel_load": str,
            "device_aware": str,
            "clean_air": str,
            "wlc_leader_name": str,
            "wlc_leader_ip": str,
            "last_run_seconds": int,
            "dca_level": str,
            "dca_db": int,
            "chan_width": str,
            "max_chan_width": int,
            "dca_min_energy_dbm": float,
            "chan_energy_min_dbm": float,
            "chan_energy_average_dbm": float,
            "chan_energy_max_dbm": float,
            "chan_dwell_minimum": str,
            "chan_dwell_average": str,
            "chan_dwell_max": str,
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
        chan_assn_mode_capture = re.compile(r"^\s+Channel\s+Assignment\s+Mode\s+:\s+(?P<chan_assn_mode>\S+)")
        #   Channel Update Interval                    : 12 Hours
        chan_update_int_capture = re.compile(r"^\s+Channel\s+Update\s+Interval\s+:\s+(?P<chan_upd_int>\d+)\s+Hours$")
        #   Anchor time (Hour of the day)              : 7
        anchor_time_capture = re.compile(
            r"^\s+Anchor\s+time\s+\(Hour\s+of\s+the\s+day\)\s+:\s+(?P<anchor_time_hour>\d+)$")
        #   Channel Update Contribution
        chan_upd_cont_capture = re.compile(r"^\s+Channel\s+Update\s+Contribution$")
        #     Noise                                    : Enable
        channel_noise_capture = re.compile(r"^\s+Noise\s+:\s+(?P<channel_noise>(Enable|Disable))$")
        #     Interference                             : Enable
        channel_interference_capture = re.compile(r"^\s+Interference\s+:\s+(?P<channel_interference>(Enable|Disable))$")
        #     Load                                     : Disable
        channel_load_capture = re.compile(r"^\s+Load\s+:\s+(?P<channel_load>(Enable|Disable))$")
        #     Device Aware                             : Disable
        device_aware_capture = re.compile(r"^\s+Device\s+Aware\s+:\s+(?P<device_aware>(Enable|Disable))$")
        #   CleanAir Event-driven RRM option           : Disabled
        clean_air_capture = re.compile(
            r"^\s+CleanAir\s+Event-driven\s+RRM\s+option\s+:\s+(?P<clean_air>(Enabled|Disabled))$")
        #   Channel Assignment Leader                  : sj-00a-ewlc1 (10.7.5.133)
        chan_assn_leader_capture = re.compile(
            r"^\s+Channel\s+Assignment\s+Leader\s+:\s+(?P<wlc_leader_name>\S+)\s+(?P<wlc_leader_ip>\(\d+\.\d+\.\d+\.\d+\))$")
        #   Last Run                                   : 15995 seconds ago
        last_run_capture = re.compile(r"^\s+Last\s+Run\s+:\s+(?P<last_run_seconds>\d+)\s+seconds\s+ago$")
        #   DCA Sensitivity Level                      : MEDIUM : 15 dB
        dca_sensitivity_capture = re.compile(
            r"^\s+DCA\s+Sensitivity\s+Level\s+:\s+(?P<dca_level>\S+)\s+:\s+(?P<dca_db>\d+)\s+dB$")
        #   DCA 802.11n/ac Channel Width               : 80 MHz
        dca_chan_width_capture = re.compile(r"^\s+DCA\s+802.11n/ac\s+Channel\s+Width\s+:\s+(?P<chan_width>.*)$")
        #   DBS Max Channel Width                      : 80 MHz
        dbs_max_chan_width_capture = re.compile(
            r"^\s+DBS\s+Max\s+Channel\s+Width\s+:\s+(?P<max_chan_width>\d+)\s+MHz$")
        #   DCA Minimum Energy Limit                   : -95 dBm
        dca_min_energy_capture = re.compile(
            r"^\s+DCA\s+Minimum\s+Energy\s+Limit\s+:\s+(?P<dca_min_energy_dbm>\S+)\s+dBm$")
        #   Channel Energy Levels
        chan_energy_levels_capture = re.compile(r"^\s+Channel\s+Energy\s+Levels$")
        #     Minimum                                  : -94 dBm
        chan_energy_min_capture = re.compile(r"^\s+Minimum\s+:\s+(?P<chan_energy_min_dbm>\S+)\s+dBm")
        #     Average                                  : -82 dBm
        chan_energy_average_capture = re.compile(r"^\s+Average\s+:\s+(?P<chan_energy_average_dbm>\S+)\s+dBm")
        #     Maximum                                  : -81 dBm
        chan_energy_max_capture = re.compile(r"^\s+Maximum\s+:\s+(?P<chan_energy_max_dbm>\S+)\s+dBm")
        #   Channel Dwell Times
        chan_dwell_times_capture = re.compile(r"^\s+Channel\s+Dwell\s+Times$")
        #     Minimum                                  : 4 hours 9 minutes 54 seconds
        chan_dwell_minimum_capture = re.compile(
            r"^\s+Minimum\s+:\s+(?P<chan_dwell_min_hours>\d+)\s+hours\s+(?P<chan_dwell_min_minutes>\d+)\s+minutes\s+(?P<chan_dwell_min_seconds>\d+)\s+seconds$")
        #     Average                                  : 4 hours 24 minutes 54 seconds
        chan_dwell_average_capture = re.compile(
            r"^\s+Average\s+:\s+(?P<chan_dwell_average_hours>\d+)\s+hours\s+(?P<chan_dwell_average_minutes>\d+)\s+minutes\s+(?P<chan_dwell_average_second>\d+)\s+seconds$")
        #     Maximum                                  : 4 hours 26 minutes 35 seconds
        chan_dwell_max_capture = re.compile(
            r"^\s+Maximum\s+:\s+(?P<chan_dwell_max_hours>\d+)\s+hours\s+(?P<chan_dwell_max_minutes>\d+)\s+minutes\s+(?P<chan_dwell_max_seconds>\d+)\s+seconds$")
        #   802.11a 5 GHz Auto-RF Channel List
        channel_list_capture = re.compile(r"^\s+802.11a\s+5\s+GHz\s+Auto-RF\s+Channel\s+List$")
        #     Allowed Channel List                     : 36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161
        allowed_channel_list_capture = re.compile(r"^\s+Allowed\s+Channel\s+List\s+:\s+(?P<allowed_channel_list>\S+)$")
        #     Unused Channel List                      : 165
        unused_channel_list_capture = re.compile(r"^\s+Unused\s+Channel\s+List\s+:\s+(?P<unused_channel_list>\d+)$")

        remove_lines = ()

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                # clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                clean_line = clean_line.rstrip()
                if not clean_line.startswith(remove_lines):
                    rendered_lines.append(clean_line)
            return rendered_lines

        def match_regex(line, regex_patterns):
            groups = {}
            for capture, pattern in regex_patterns.items():
                if pattern.match(line):
                    match = pattern.match(line)
                    groups = match.groupdict()
            return groups

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

        out = filter_lines(raw_output=out, remove_lines=remove_lines)

        for line in out:
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
                continue
            #     Noise                                    : Enable
            elif channel_noise_capture.match(line):
                channel_noise_capture_match = channel_noise_capture.match(line)
                groups = channel_noise_capture_match.groupdict()
                channel_noise = groups['channel_noise']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'channel_noise': channel_noise})
                continue
            #     Interference                             : Enable
            elif channel_interference_capture.match(line):
                channel_interference_capture_match = channel_interference_capture.match(line)
                groups = channel_interference_capture_match.groupdict()
                channel_interference = groups['channel_interference']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update(
                    {'channel_interference': channel_interference})
                continue
                #     Load                                     : Disable
            elif channel_load_capture.match(line):
                channel_load_capture_match = channel_load_capture.match(line)
                groups = channel_load_capture_match.groupdict()
                channel_load = groups['channel_load']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'channel_load': channel_load})
                continue
            #     Device Aware                             : Disable
            elif device_aware_capture.match(line):
                device_aware_capture_match = device_aware_capture.match(line)
                groups = device_aware_capture_match.groupdict()
                device_aware = groups['device_aware']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'device_aware': device_aware})
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
                chan_width = groups['chan_width']
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'chan_width': chan_width})
                continue
            #   DBS Max Channel Width                      : 80 MHz
            elif dbs_max_chan_width_capture.match(line):
                dbs_max_chan_width_capture_match = dbs_max_chan_width_capture.match(line)
                groups = dbs_max_chan_width_capture_match.groupdict()
                max_chan_width = change_data_type(groups['max_chan_width'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'max_chan_width': max_chan_width})
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
                continue
            #     Minimum                                  : -94 dBm
            elif chan_energy_min_capture.match(line):
                chan_energy_min_capture_match = chan_energy_min_capture.match(line)
                groups = chan_energy_min_capture_match.groupdict()
                chan_energy_min_dbm = change_data_type(groups['chan_energy_min_dbm'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update(
                    {'chan_energy_min_dbm': chan_energy_min_dbm})
                continue
            #     Average                                  : -82 dBm
            elif chan_energy_average_capture.match(line):
                chan_energy_average_capture_match = chan_energy_average_capture.match(line)
                groups = chan_energy_average_capture_match.groupdict()
                chan_energy_average_dbm = change_data_type(groups['chan_energy_average_dbm'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update(
                    {'chan_energy_average_dbm': chan_energy_average_dbm})
                continue
            #     Maximum                                  : -81 dBm
            elif chan_energy_max_capture.match(line):
                chan_energy_max_capture_match = chan_energy_max_capture.match(line)
                groups = chan_energy_max_capture_match.groupdict()
                chan_energy_max_dbm = change_data_type(groups['chan_energy_max_dbm'])
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update(
                    {'chan_energy_max_dbm': chan_energy_max_dbm})
                continue
            #   Channel Dwell Times
            elif chan_dwell_times_capture.match(line):
                chan_dwell_times_capture_match = chan_dwell_times_capture.match(line)
                groups = chan_dwell_times_capture_match.groupdict()
                continue
            #     Minimum                                  : 4 hours 9 minutes 54 seconds
            elif chan_dwell_minimum_capture.match(line):
                chan_dwell_minimum_capture_match = chan_dwell_minimum_capture.match(line)
                groups = chan_dwell_minimum_capture_match.groupdict()
                chan_dwell_min_hours = groups['chan_dwell_min_hours']
                chan_dwell_min_minutes = groups['chan_dwell_min_minutes']
                chan_dwell_min_seconds = groups['chan_dwell_min_seconds']
                chan_dwell_minimum = chan_dwell_min_hours + ' hours ' + chan_dwell_min_minutes + ' minutes ' + chan_dwell_min_seconds + ' seconds'
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'chan_dwell_minimum': chan_dwell_minimum})
                continue
            #     Average                                  : 4 hours 24 minutes 54 seconds
            elif chan_dwell_average_capture.match(line):
                chan_dwell_average_capture_match = chan_dwell_average_capture.match(line)
                groups = chan_dwell_average_capture_match.groupdict()
                chan_dwell_average_hours = groups['chan_dwell_average_hours']
                chan_dwell_average_minutes = groups['chan_dwell_average_minutes']
                chan_dwell_average_seconds = groups['chan_dwell_average_second']
                chan_dwell_average = chan_dwell_average_hours + ' hours ' + chan_dwell_average_minutes + ' minutes ' + chan_dwell_average_seconds + ' seconds'
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'chan_dwell_average': chan_dwell_average})
                continue
            #     Maximum                                  : 4 hours 26 minutes 35 seconds
            elif chan_dwell_max_capture.match(line):
                chan_dwell_max_capture_match = chan_dwell_max_capture.match(line)
                groups = chan_dwell_max_capture_match.groupdict()
                chan_dwell_max_hours = groups['chan_dwell_max_hours']
                chan_dwell_max_minutes = groups['chan_dwell_max_minutes']
                chan_dwell_max_seconds = groups['chan_dwell_max_seconds']
                chan_dwell_max = chan_dwell_max_hours + ' hours ' + chan_dwell_max_minutes + ' minutes ' + chan_dwell_max_seconds + ' seconds'
                show_ap_dot11_5ghz_channel_dict['channel_assignment'].update({'chan_dwell_max': chan_dwell_max})
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
