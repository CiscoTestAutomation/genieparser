# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ldp import (
    ShowLDPSession, ShowLDPOverview)

# =================================
# Unit test for 'show ldp session'
# =================================


class TestShowLDPSession(unittest.TestCase):
    '''unit test for "show ldp session'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'ldp-session-information': {
            'ldp-session': [{
                'ldp-neighbor-address': '59.128.2.250',
                'ldp-session-state': 'Operational',
                'ldp-connection-state': 'Open',
                'ldp-remaining-time': '26',
                'ldp-session-adv-mode': 'DU'
            }]
        }
    }

    golden_output = {
        'execute.return_value':
        '''
          Address                           State       Connection  Hold time  Adv. Mode
        59.128.2.250                        Operational Open          26         DU
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

# =================================
# Unit test for 'show ldp overview'
# =================================


class TestShowLDPOverview(unittest.TestCase):
    '''unit test for "show ldp overview'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ldp overview
        Instance: master
        Reference count: 2
        Router ID: 106.187.14.240
        LDP inet: enabled
        Transport preference: IPv4
        Message id: 4
        Configuration sequence: 1
        Deaggregate: disabled
        Explicit null: disabled
        IPv6 tunneling: disabled
        Strict targeted hellos: disabled
        Loopback if added: no
        Route preference: 9
        Unicast transit LSP chaining: disabled
        P2MP transit LSP chaining: disabled
        Transit LSP statistics based on route statistics: disabled
        LDP route acknowledgement: enabled
        BGP export: enabled
        LDP mtu discovery: disabled
        LDP SR Mapping Client: disabled
        Capabilities enabled: none
        Egress FEC capabilities enabled: entropy-label-capability
        Downstream unsolicited Sessions:
            Operational: 1
            Retention: liberal
            Control: ordered
        Auto targeted sessions:
            Auto targeted: disabled
            Dynamic tunnel session count: 0
        P2MP:
            Recursive route: disabled
            No rsvp tunneling: disabled
        Timers:
            Keepalive interval: 10, Keepalive timeout: 30
            Link hello interval: 5, Link hello hold time: 15
            Targeted hello interval: 15, Targeted hello hold time: 45
            Label withdraw delay: 60, Make before break timeout: 30
            Make before break switchover delay: 3
            Link protection timeout: 120
        Graceful restart:
            Restart: disabled, Helper: enabled, Restart in process: false
            Reconnect time: 60000, Max neighbor reconnect time: 120000
            Recovery time: 160000, Max neighbor recovery time: 240000
        Traffic Engineering:
            Bgp igp: disabled
            Both ribs: disabled
            Mpls forwarding: disabled
        IGP:
            Tracking igp metric: disabled
            Sync session up delay: 10
        Session protection:
            Session protection: disabled
            Session protection timeout: 0
        Interface addresses advertising:
            106.187.14.157
        LDP Job:
            Read job time quantum: 1000, Write job time quantum: 1000
            Read job loop quantum: 100, Write job loop quantum: 100
            Backup inbound read job time quantum: 1000, Backup outbound read job time quantum: 1000
            Backup inbound read job loop quantum: 100, Backup outbound read job loop quantum: 100
        Label allocation:
            Current number of LDP labels allocated: 1
            Total number of LDP labels allocated: 1
            Total number of LDP labels freed: 0
            Total number of LDP label allocation failure: 0
            Current number of labels allocated by all protocols: 0
    '''}

    golden_parsed_output = {
        'ldp_overview_information': {
            'ldp_overview': {
                'ldp_auto_targeted_session': {
                    'ldp_auto_targeted_dyn_tun_ses_count': 0,
                    'ldp_auto_targeted_session_enabled': 'disabled'
                },
                'ldp_bgp_export': 'enabled',
                'ldp_configuration_sequence': 1,
                'ldp_deaggregate': 'disabled',
                'ldp_explicit_null': 'disabled',
                'ldp_gr_overview': {
                    'ldp_gr_helper': 'enabled',
                    'ldp_gr_max_neighbor_reconnect_time': 120000,
                    'ldp_gr_max_neighbor_recovery_time': 240000,
                    'ldp_gr_reconnect_time': 60000,
                    'ldp_gr_recovery_time': 160000,
                    'ldp_gr_restart': 'disabled',
                    'ldp_gr_restarting': 'false'
                },
                'ldp_igp_overview': {
                    'ldp_igp_sync_session_up_delay': 10,
                    'ldp_tracking_igp_metric': 'disabled'
                },
                'ldp_inet': 'enabled',
                'ldp_instance_capability': {
                    'ldp_capability': 'none'
                },
                'ldp_instance_egress_fec_capability': {
                    'ldp_egress_fec_capability': 'entropy-label-capability'
                },
                'ldp_instance_name': 'master',
                'ldp_interface_address': {
                    'interface_address': '106.187.14.157'
                },
                'ldp_ipv6_tunneling': 'disabled',
                'ldp_job_overview': {
                    'ldp_inbound_read_job_loop_quantum': 100,
                    'ldp_inbound_read_job_time_quantum': 1000,
                    'ldp_outbound_read_job_loop_quantum': 100,
                    'ldp_outbound_read_job_time_quantum': 1000,
                    'ldp_read_job_loop_quantum': 100,
                    'ldp_read_job_time_quantum': 1000,
                    'ldp_write_job_loop_quantum': 100,
                    'ldp_write_job_time_quantum': 1000
                },
                'ldp_label_allocation': {
                    'ldp_global_label_current_allocs': 0,
                    'ldp_label_alloc_failure': 0,
                    'ldp_label_current_allocs': 1,
                    'ldp_label_total_allocs': 1,
                    'ldp_label_total_frees': 0
                },
                'ldp_loopback_if_added': 'no',
                'ldp_message_id': 4,
                'ldp_mtu_discovery': 'disabled',
                'ldp_p2mp': {
                    'ldp_p2mp_no_rsvp_tunneling_enabled': 'disabled',
                    'ldp_p2mp_recursive_route_enabled': 'disabled'
                },
                'ldp_p2mp_transit_lsp_chaining': 'disabled',
                'ldp_reference_count': 2,
                'ldp_route_acknowledgement': 'enabled',
                'ldp_route_preference': 9,
                'ldp_router_id': '106.187.14.240',
                'ldp_session_count': {
                    'ldp_control_mode': 'ordered',
                    'ldp_retention_mode': 'liberal',
                    'ldp_session_operational': 1
                },
                'ldp_session_protect_overview': {
                    'ldp_session_protect': 'disabled',
                    'ldp_session_protect_timeout': 0
                },
                'ldp_sr_mapping_client': 'disabled',
                'ldp_strict_targeted_hellos': 'disabled',
                'ldp_te_overview': {
                    'ldp_te_bgp_igp': 'disabled',
                    'ldp_te_both_ribs': 'disabled',
                    'ldp_te_mpls_forwarding': 'disabled'
                },
                'ldp_timer_overview': {
                    'ldp_instance_keepalive_interval': 10,
                    'ldp_instance_keepalive_timeout': 30,
                    'ldp_instance_label_withdraw_delay': 60,
                    'ldp_instance_link_hello_hold_time': 15,
                    'ldp_instance_link_hello_interval': 5,
                    'ldp_instance_link_protection_timeout': 120,
                    'ldp_instance_make_before_break_switchover_delay': 3,
                    'ldp_instance_make_before_break_timeout': 30,
                    'ldp_instance_targeted_hello_hold_time': 45,
                    'ldp_instance_targeted_hello_interval': 15
                },
                'ldp_transit_lsp_route_stats': 'disabled',
                'ldp_transport_preference': 'IPv4',
                'ldp_unicast_transit_lsp_chaining': 'disabled'
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPOverview(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPOverview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
