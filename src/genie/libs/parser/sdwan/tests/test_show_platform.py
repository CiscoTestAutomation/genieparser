# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.sdwan.show_platform import ShowPlatformHardwareQfpActiveFeatureAppqoe


class TestShowPlatformHardwareQfpActiveFeatureAppqoe(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': """
        show platform hardware qfp active feature appqoe stats all
        APPQOE Feature Statistics:
        Global:
               ip-non-tcp-pkts: 0
               not-enabled: 0
               cft_handle_pkt: 0
               sdvt_divert_req_fail: 0
               syn_policer_rate: 800
           SDVT Global stats:
             AppNAV registration: 1
             within SDVT syn policer limit: 266004
        SN Index [0 (Green)]
           SDVT Count stats:
             decaps: 679143
             encaps: 743013
             packets unmarked in ingress: 502868
             Expired Connections: 64609
             Idle timed-out persistent Connections: 50409
             decaps: Processed control messages from SN: 14200
             decaps: delete requests received total: 14200
               decaps: delete - protocol decision: 14200
           SDVT Packet stats:
             Divert packets/bytes: 743013/43313261
             Reinject packets/bytes: 679010/503129551
           SDVT Drop Cause stats:
           SDVT Errors stats:
        SN Index [Default]
           SDVT Count stats:
           SDVT Packet stats:
           SDVT Drop Cause stats:
           SDVT Errors stats:
        """
    }

    golden_parsed_output = {
        'feature': {
            'appqoe': {
                'global': {
                    'cft_handle_pkt': 0,
                    'ip_non_tcp_pkts': 0,
                    'not_enabled': 0,
                    'sdvt_divert_req_fail': 0,
                    'sdvt_global_stats': {
                        'appnav_registration': 1,
                        'within_sdvt_syn_policer_limit': 266004
                    },
                    'syn_policer_rate': 800
                },
                'sn_index': {
                    '0 (Green)': {
                        'sdvt_count_stats': {
                            'decap_messages': {
                                'delete_requests_recieved': 14200,
                                'deleted_protocol_decision': 14200,
                                'processed_control_messages': 14200
                            },
                            'decaps': 679143,
                            'encaps': 743013,
                            'expired_connections': 64609,
                            'idle_timed_out_persistent_connections': 50409,
                            'packets_unmarked_in_ingress': 502868
                        },
                        'sdvt_drop_cause_stats': {},
                        'sdvt_errors_stats': {},
                        'sdvt_packet_stats': {
                            'divert': {
                                'bytes': 43313261,
                                'packets': 743013
                            },
                            'reinject': {
                                'bytes': 503129551,
                                'packets': 679010
                            }
                        }
                    },
                    'Default': {
                        'sdvt_count_stats': {},
                        'sdvt_drop_cause_stats': {},
                        'sdvt_errors_stats': {},
                        'sdvt_packet_stats': {}
                    }
                }
            }
        }
    }


    def test_show_platform_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowPlatformHardwareQfpActiveFeatureAppqoe(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_platform_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowPlatformHardwareQfpActiveFeatureAppqoe(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()


if __name__ == '__main__':
    unittest.main()
