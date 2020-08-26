import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_ap import ShowApDot115GhzChannel


# ==========================================
# Unit test for 'show ap dot11 5ghz channel'
# ==========================================
class TestShowApDot115GhzChannel(unittest.TestCase):
    """Unit test for 'show ap dot11 5ghz channel'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
    "channel_assignment": {
        "chan_assn_mode": "AUTO",
        "chan_upd_int": 12,
        "anchor_time_hour": 7,
        "channel_noise": "Enable",
        "channel_interference": "Enable",
        "channel_load": "Disable",
        "device_aware": "Disable",
        "clean_air": "Disabled",
        "wlc_leader_name": "sj-00a-ewlc1",
        "wlc_leader_ip": "10.7.5.133",
        "last_run_seconds": 15995,
        "dca_level": "MEDIUM",
        "dca_db": 15,
        "chan_width": "80 MHz",
        "max_chan_width": 80,
        "dca_min_energy_dbm": -95.0,
        "chan_energy_min_dbm": -94.0,
        "chan_energy_average_dbm": -82.0,
        "chan_energy_max_dbm": -81.0,
        "chan_dwell_minimum": "4 hours 9 minutes 54 seconds",
        "chan_dwell_average": "4 hours 24 minutes 54 seconds",
        "chan_dwell_max": "4 hours 26 minutes 35 seconds",
        "allowed_channel_list": "36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161",
        "unused_channel_list": "165"
    }
}

    golden_output1 = {'execute.return_value': '''
Leader Automatic Channel Assignment
  Channel Assignment Mode                    : AUTO
  Channel Update Interval                    : 12 Hours
  Anchor time (Hour of the day)              : 7
  Channel Update Contribution
    Noise                                    : Enable
    Interference                             : Enable
    Load                                     : Disable
    Device Aware                             : Disable
  CleanAir Event-driven RRM option           : Disabled
  Channel Assignment Leader                  : sj-00a-ewlc1 (10.7.5.133)
  Last Run                                   : 15995 seconds ago

  DCA Sensitivity Level                      : MEDIUM : 15 dB
  DCA 802.11n/ac Channel Width               : 80 MHz
  DBS Max Channel Width                      : 80 MHz
  DCA Minimum Energy Limit                   : -95 dBm
  Channel Energy Levels
    Minimum                                  : -94 dBm
    Average                                  : -82 dBm
    Maximum                                  : -81 dBm
  Channel Dwell Times
    Minimum                                  : 4 hours 9 minutes 54 seconds 
    Average                                  : 4 hours 24 minutes 54 seconds 
    Maximum                                  : 4 hours 26 minutes 35 seconds 
  802.11a 5 GHz Auto-RF Channel List
    Allowed Channel List                     : 36,40,44,48,52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,149,153,157,161
    Unused Channel List                      : 165        
    '''}

    def test_show_ap_dot11_5ghz_channel_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowApDot115GhzChannel(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ap_dot11_5ghz_channel_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowApDot115GhzChannel(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
