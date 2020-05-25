import unittest
from unittest.mock import Mock

# PyATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.asa.show_service_policy import (ShowServicePolicy)

# ============================================
# unit test for 'show service policy'
# =============================================
class TestShowServicePolicy(unittest.TestCase):
    '''
       unit test for show service policy
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None
    golden_parsed_output = {
        'global_policy': {
            'service_policy': {
                'global_policy': {
                    'class_map': {
                        'inspection_default': {
                            'inspect': {
                                'dns': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'inspect_map': 'preset_dns_map',
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                'esmtp': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'inspect_map': '_default_esmtp_map',
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                'ftp': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                'h323 h225': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'inspect_map': '_default_h323_map',
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'tcp_proxy': {
                                        'bytes_dropped': 0,
                                        'bytes_in_buffer': 0,
                                    },
                                    'v6_fail_close': 0,
                                },
                                'h323 ras': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'inspect_map': '_default_h323_map',
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                'ip-options': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'inspect_map': '_default_ip_options_map',
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                'netbios': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                'rsh': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                'rtsp': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'tcp_proxy': {
                                        'bytes_dropped': 0,
                                        'bytes_in_buffer': 0,
                                    },
                                    'v6_fail_close': 0,
                                },
                                'sip': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'tcp_proxy': {
                                        'bytes_dropped': 0,
                                        'bytes_in_buffer': 0,
                                    },
                                    'v6_fail_close': 0,
                                },
                                'skinny': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'tcp_proxy': {
                                        'bytes_dropped': 0,
                                        'bytes_in_buffer': 0,
                                    },
                                    'v6_fail_close': 0,
                                },
                                'sqlnet': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                'sunrpc': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'tcp_proxy': {
                                        'bytes_dropped': 0,
                                        'bytes_in_buffer': 0,
                                    },
                                    'v6_fail_close': 0,
                                },
                                'tftp': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                'xdmcp': {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
        show service-policy 

        Global policy: 
        Service-policy: global_policy
            Class-map: inspection_default
            Inspect: ip-options _default_ip_options_map, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            Inspect: netbios, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            Inspect: rtsp, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
                    tcp-proxy: bytes in buffer 0, bytes dropped 0
            Inspect: sunrpc, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
                    tcp-proxy: bytes in buffer 0, bytes dropped 0
            Inspect: tftp, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            Inspect: xdmcp, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            Inspect: dns preset_dns_map, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            Inspect: ftp, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            Inspect: h323 h225 _default_h323_map, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
                    tcp-proxy: bytes in buffer 0, bytes dropped 0
            Inspect: h323 ras _default_h323_map, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            Inspect: rsh, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            Inspect: esmtp _default_esmtp_map, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            Inspect: sqlnet, packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            Inspect: sip , packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
                    tcp-proxy: bytes in buffer 0, bytes dropped 0
            Inspect: skinny , packet 0, lock fail 0, drop 0, reset-drop 0, 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
                    tcp-proxy: bytes in buffer 0, bytes dropped 0
          '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowServicePolicy(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        route_obj = ShowServicePolicy(device=self.device)
        parsed_output = route_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()