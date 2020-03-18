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
                                1: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'ip-options _default_ip_options_map',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                2: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'netbios',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                3: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'rtsp',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'tcp_proxy': {
                                        'bytes_dropped': 0,
                                        'bytes_in_buffer': 0,
                                    },
                                    'v6_fail_close': 0,
                                },
                                4: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'sunrpc',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'tcp_proxy': {
                                        'bytes_dropped': 0,
                                        'bytes_in_buffer': 0,
                                    },
                                    'v6_fail_close': 0,
                                },
                                5: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'tftp',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                6: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'xdmcp',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                7: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'dns preset_dns_map',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                8: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'ftp',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                9: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'h323 h225 _default_h323_map',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'tcp_proxy': {
                                        'bytes_dropped': 0,
                                        'bytes_in_buffer': 0,
                                    },
                                    'v6_fail_close': 0,
                                },
                                10: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'h323 ras _default_h323_map',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                11: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'rsh',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                12: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'esmtp _default_esmtp_map',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                13: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'sqlnet',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'v6_fail_close': 0,
                                },
                                14: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'sip ',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'tcp_proxy': {
                                        'bytes_dropped': 0,
                                        'bytes_in_buffer': 0,
                                    },
                                    'v6_fail_close': 0,
                                },
                                15: {
                                    'drop': 0,
                                    'five_minute_pkt_rate': 0,
                                    'lock_fail': 0,
                                    'name': 'skinny ',
                                    'packet': 0,
                                    'reset_drop': 0,
                                    'sctp_drop_override': 0,
                                    'tcp_proxy': {
                                        'bytes_dropped': 0,
                                        'bytes_in_buffer': 0,
                                    },
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