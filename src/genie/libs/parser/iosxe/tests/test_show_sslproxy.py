import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxe.show_sslproxy import (ShowSslproxyStatus,
                                                   ShowSslProxyStatistics)


# ============================================
# unittest for 'show sslproxy status'
# ============================================
class TestShowSslproxyStatus(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        Configuration
        -------------
        CA Cert Bundle                 : /bootflash/vmanage-admin/sslProxyDefaultCAbundle.pem
        CA TP Label                    : PROXY-SIGNING-CA
        Cert Lifetime                  : 730
        EC Key type                    : P256
        RSA Key Modulus                : 2048
        Cert Revocation                : NONE
        Expired Cert                   : drop
        Untrusted Cert                 : drop
        Unknown Status                 : drop
        Unsupported Protocol Ver       : drop
        Unsupported Cipher Suites      : drop
        Failure Mode Action            : close
        Min TLS Ver                    : TLS Version 1.1

        Status
        ------
        SSL Proxy Operational State    : RUNNING
        TCP Proxy Operational State    : RUNNING
        Clear Mode                     : FALSE
        '''
        }

    golden_parsed_output = {
        'configuration': {
            'ca_cert_bundle': '/bootflash/vmanage-admin/sslProxyDefaultCAbundle.pem',
            'ca_tp_label': 'PROXY-SIGNING-CA',
            'cert_lifetime': 730,
            'ec_key_type': 'P256',
            'rsa_key_modulus': 2048,
            'cert_revocation': 'NONE',
            'expired_cert': 'drop',
            'untrusted_cert': 'drop',
            'unknown_status': 'drop',
            'unsupported_protocol_ver': 'drop',
            'unsupported_cipher_suites': 'drop',
            'failure_mode_action': 'close',
            'min_tls_ver': 'TLS Version 1.1'
            },
        'status': {
            'ssl_proxy_operational_state': 'RUNNING',
            'tcp_proxy_operational_state': 'RUNNING',
            'clear_mode': 'FALSE'
            }
        }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSslproxyStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSslproxyStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ============================================
# unittest for 'show sslproxy statistics'
# ============================================
class TestShowSslProxyStatistics(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        C8kv_SN1#show sslproxy statistics
        ==========================================================
        SSL Proxy Statistics
        ==========================================================
        Connection Statistics:
            Total Connections : 0
            Proxied Connections : 0
            Non-proxied Connections : 0
            Clear Connections : 0
            Active Proxied Connections : 0
            Active Non-proxied Connections : 0
            Active Clear Connections : 0
            Max Conc Proxied Connections : 0
            Max Conc Non-proxied Connections : 0
            Max Conc Clear Connections : 0
            Total Closed Connections : 0

        Non-proxied Connection Reasons:
            Unsupported Cipher : 0
            Unsupported SSL Version : 0
            Non SSL Traffic : 0
            Memory Allocation Failure : 0
            Memory Access Failure : 0
            Handshake Unsupported : 0
            SSL Parse Failure : 0
            SSL Error : 0
            Unexpected Packet : 0
            ISM State Error : 0
            Exception : 0
            Endpoint Alert : 0
            FIN/RST Received during handshake : 0
            Pushdown by SC : 0
            Pushdown Default : 0

        Dropped Connection Reasons:
            Unsupported SSL Version : 0
            Unsupported Cipher : 0
            Untrusted Certificate : 0
            Unable to get Proxy certificate : 0
            Expired Certificate : 0
            OCSP Cert Verification Failure : 0
            Handshake Unsupported : 0
            Endpoint Alert : 0
            FIN/RST Received during handshake : 0
            Read in Invalid State : 0
            Invalid FSM Event Received : 0
            Invalid Msg Type Rcvd from ISM/DE : 0
            Event Received in Wrong State : 0
            ISM Key Packet Send Fail : 0
            ISM Flow Create Failure : 0
            Failed to Load Key in DE : 0
            Invalid Peer Segment : 0
            Fail to get Orig CH during Pushdown: 0
            Decrypt/Encrypt Failure : 0
            RST Rcvd during PS/PC key pending : 0
            No SSL Record in Flow Segment : 0
            Memory Allocation Failure : 0
            Memory Access Failure : 0
            Abort on SSL Parse Failure : 0
            Invalid SSL Record Header : 0
            Unable to send HS message to ISM : 0
            Fail to get Memory from Pool in ISM: 0

        Alert Generated:
            C2S : 0
            S2C : 0

        Alert Received:
            C2S : 0
            S2C : 0

        Connection Closure Statistics:
        C2S
            FIN Received at PS : 0
            FIN Rec after SSL Handshake at PS : 0
            FIN Rec during SSL Handshake at PS : 0
            FIN Rec for Non-SSL Conn at PS : 0
            FIN Sent to SC from PS : 0
            FIN Received at PC from SC : 0
            FIN Sent to Server : 0
            RST Generated by PS : 0
            RST Received at PS : 0
            RST Sent to SC from PS : 0
            RST Received at PC from SC : 0
            RST Sent to Server : 0
            Close Notify Received at PS : 0
            Close Notify FIN Sent to SC from PS: 0
            Close Notify FIN Rec at PC from SC : 0
            Close Notify Sent to Server : 0
        S2C
            FIN Received at PC : 0
            FIN Rec after SSL Handshake at PC : 0
            FIN Rec during SSL Handshake at PC : 0
            FIN Rec for Non-SSL Conn at PC : 0
            FIN Sent to SC from PC : 0
            FIN Received at PS from SC : 0
            FIN Sent to Client : 0
            RST Generated by PC : 0
            RST Received at PC : 0
            RST Sent to SC from PC : 0
            RST Received at PS from SC : 0
            RST Sent to Client : 0
            Close Notify Received at PC : 0
            Close Notify FIN Sent to SC from PC: 0
            Close Notify FIN Rec at PS from SC : 0
            Close Notify Sent to Client : 0

        Proxy Server:
            LWSSL Flow Create : 0
            LWSSL Flow Delete : 0
            FIN Generated by SC : 0
            RST Generated by SC : 0
            Close Notify Sent : 0

        Proxy Client:
            LWSSL Flow Create : 0
            LWSSL Flow Delete : 0
            FIN Generated by SC : 0
            RST Generated by SC : 0
            Close Notify Sent : 0

        ISM:
            ISM Flow Create : 0
            ISM Flow Delete : 0
            ISM FIFO Enqueue Failed : 0
            ISM Sem Post Failed : 0
            LWSSL Failed to Send Msg : 0
            LWSSL Mem alloc failed for ISM Msg : 0

        Resource Manager:
            Session Alloc Success : 0
            Session Alloc Failures : 0
            Session Free Success : 0
            Session Free Failures : 0

        OCSP Statistics:
        APP Statistics
            OCSP Requests : 0
            OCSP Responses : 0
            OCSP Timeouts : 0
            OCSP Failures : 0
            OCSP Good responses : 0
            OCSP Revoked responses : 0
            OCSP Unknown responses : 0
            OCSP Internal Errors : 0
        Client Statistics
            OCSP Requests : 0
            OCSP Responses : 0
            OCSP Timeouts : 0
            OCSP Failures : 0
            OCSP Good responses : 0
            OCSP Revoked responses : 0
            OCSP Unknown responses : 0
            OCSP Internal Errors : 0

        OCSP Stapling:
            OCSP Stapling Requests : 0
            OCSP Stapling Responses : 0
            OCSP Stapling Valid Responses : 0
            OCSP Stapling Revoked Responses : 0
            OCSP Stapling Unknown Responses : 0
            OCSP Response Validation Failure : 0

        SSL Statistics:
        Flow Requested SSL/TLS version:
            SSL V2 Flows : 0
            SSL V3 Flows : 0
            TLS 1.0 Flows : 0
            TLS 1.1 Flows : 0
            TLS 1.2 Flows : 0
            TLS 1.3 Flows : 0
        Flow Selected SSL/TLS version:
            TLS 1.0 Flows : 0
            TLS 1.1 Flows : 0
            TLS 1.2 Flows : 0
        Client Hello Extensions:
            Pushdown : 0
            Bypass : 0
            Strip : 0
            Process : 0
        SSL Handshake Statistics:
            SSL Handshakes Started : 0
            SSL Handshakes Completed : 0
            Full SSL Handshakes : 0
            SSL Renegotiation : 0
            SSL Resumption : 0
            SSL Resumption session ID : 0
            SSL Resumption session tkt : 0
            SSL fallback to full hs : 0
            SSL failed renego : 0
            SSL server cert validation reqs : 0
            SSL server cert validation success : 0
            Server cert verify failed expired : 0
            Server cert verify failed untrusted: 0
            SSL client cert validation reqs : 0
            SSL client cert validation success : 0
            Client cert verify failed expired : 0
            Client cert verify failed untrusted: 0
            Revocation Check Requests : 0
            Revocation Check Good Response : 0 
        Policy Statistics:
        Drop
            expired-certificate : 0
            failure-mode : 0
            unknown-status : 0
            unsupported-cipher-suites : 0
            unsupported-protocol-versions : 0
            untrusted-certificate : 0
        Decrypt
            expired-certificate : 0
            failure-mode : 0
            unknown-status : 0
            untrusted-certificate : 0
        No Decrypt
            unsupported-cipher-suites : 0
            unsupported-protocol-versions : 0

        Packet Counters:
            Proxy Server
            From Client : 0
            To SC : 0
            From SC : 0
            To Client : 0
            Proxy Client
            From Server : 0
            To SC : 0
            From SC : 0
            To Server : 0
        Clear Packets:
            Proxy Server
            From Client : 0
            To SC : 0
            From SC : 0
            To Client : 0
            Proxy Client
            From Server : 0
            To SC : 0
            From SC : 0
            To Server : 0
        Dropped Packets:
            C2S WCAPI DENY packet : 0
            S2C WCAPI DENY packet : 0
        '''
        }

    golden_parsed_output = {
        'sslproxy_statistics': {
            'connection_statistics': {
                'total_connections': 0,
                'proxied_connections': 0,
                'non_proxied_connections': 0,
                'clear_connections': 0,
                'active_proxied_connections': 0,
                'active_non_proxied_connections': 0,
                'active_clear_connections': 0,
                'max_conc_proxied_connections': 0,
                'max_conc_non_proxied_connections': 0,
                'max_conc_clear_connections': 0,
                'total_closed_connections': 0
            },
            'non_proxied_connection_reasons': {
                'unsupported_cipher': 0,
                'unsupported_ssl_version': 0,
                'non_ssl_traffic': 0,
                'memory_allocation_failure': 0,
                'memory_access_failure': 0,
                'handshake_unsupported': 0,
                'ssl_parse_failure': 0,
                'ssl_error': 0,
                'unexpected_packet': 0,
                'ism_state_error': 0,
                'exception': 0,
                'endpoint_alert': 0,
                'fin_rst_received_during_handshake': 0,
                'pushdown_by_sc': 0,
                'pushdown_default': 0
            },
            'dropped_connection_reasons': {
                'unsupported_ssl_version': 0,
                'unsupported_cipher': 0,
                'untrusted_certificate': 0,
                'unable_to_get_proxy_certificate': 0,
                'expired_certificate': 0,
                'ocsp_cert_verification_failure': 0,
                'handshake_unsupported': 0,
                'endpoint_alert': 0,
                'fin_rst_received_during_handshake': 0,
                'read_in_invalid_state': 0,
                'invalid_fsm_event_received': 0,
                'invalid_msg_type_rcvd_from_ism_de': 0,
                'event_received_in_wrong_state': 0,
                'ism_key_packet_send_fail': 0,
                'ism_flow_create_failure': 0,
                'failed_to_load_key_in_de': 0,
                'invalid_peer_segment': 0,
                'fail_to_get_orig_ch_during_pushdown': 0,
                'decrypt_encrypt_failure': 0,
                'rst_rcvd_during_ps_pc_key_pending': 0,
                'no_ssl_record_in_flow_segment': 0,
                'memory_allocation_failure': 0,
                'memory_access_failure': 0,
                'abort_on_ssl_parse_failure': 0,
                'invalid_ssl_record_header': 0,
                'unable_to_send_hs_message_to_ism': 0,
                'fail_to_get_memory_from_pool_in_ism': 0
            },
            'alert_generated': {
                'c2s': 0,
                's2c': 0
            },
            'alert_received': {
                'c2s': 0,
                's2c': 0
            },
            'connection_closure_statistics': {
                'c2s': {
                    'fin_received_at_ps': 0,
                    'fin_rec_after_ssl_handshake_at_ps': 0,
                    'fin_rec_during_ssl_handshake_at_ps': 0,
                    'fin_rec_for_non_ssl_conn_at_ps': 0,
                    'fin_sent_to_sc_from_ps': 0,
                    'fin_received_at_pc_from_sc': 0,
                    'fin_sent_to_server': 0,
                    'rst_generated_by_ps': 0,
                    'rst_received_at_ps': 0,
                    'rst_sent_to_sc_from_ps': 0,
                    'rst_received_at_pc_from_sc': 0,
                    'rst_sent_to_server': 0,
                    'close_notify_received_at_ps': 0,
                    'close_notify_fin_sent_to_sc_from_ps': 0,
                    'close_notify_fin_rec_at_pc_from_sc': 0,
                    'close_notify_sent_to_server': 0
                },
                's2c': {
                    'fin_received_at_pc': 0,
                    'fin_rec_after_ssl_handshake_at_pc': 0,
                    'fin_rec_during_ssl_handshake_at_pc': 0,
                    'fin_rec_for_non_ssl_conn_at_pc': 0,
                    'fin_sent_to_sc_from_pc': 0,
                    'fin_received_at_ps_from_sc': 0,
                    'fin_sent_to_client': 0,
                    'rst_generated_by_pc': 0,
                    'rst_received_at_pc': 0,
                    'rst_sent_to_sc_from_pc': 0,
                    'rst_received_at_ps_from_sc': 0,
                    'rst_sent_to_client': 0,
                    'close_notify_received_at_pc': 0,
                    'close_notify_fin_sent_to_sc_from_pc': 0,
                    'close_notify_fin_rec_at_ps_from_sc': 0,
                    'close_notify_sent_to_client': 0
                }
            },
            'proxy_server': {
                'lwssl_flow_create': 0,
                'lwssl_flow_delete': 0,
                'fin_generated_by_sc': 0,
                'rst_generated_by_sc': 0,
                'close_notify_sent': 0
            },
            'proxy_client': {
                'lwssl_flow_create': 0,
                'lwssl_flow_delete': 0,
                'fin_generated_by_sc': 0,
                'rst_generated_by_sc': 0,
                'close_notify_sent': 0
            },
            'ism': {
                'ism_flow_create': 0,
                'ism_flow_delete': 0,
                'ism_fifo_enqueue_failed': 0,
                'ism_sem_post_failed': 0,
                'lwssl_failed_to_send_msg': 0,
                'lwssl_mem_alloc_failed_for_ism_msg': 0
            },
            'resource_manager': {
                'session_alloc_success': 0,
                'session_alloc_failures': 0,
                'session_free_success': 0,
                'session_free_failures': 0
            },
            'oscp_statistics': {
                'app_statistics': {
                    'ocsp_requests': 0,
                    'ocsp_responses': 0,
                    'ocsp_timeouts': 0,
                    'ocsp_failures': 0,
                    'ocsp_good_responses': 0,
                    'ocsp_revoked_responses': 0,
                    'ocsp_unknown_responses': 0,
                    'ocsp_internal_errors': 0
                },
                'client_statistics': {
                    'ocsp_requests': 0,
                    'ocsp_responses': 0,
                    'ocsp_timeouts': 0,
                    'ocsp_failures': 0,
                    'ocsp_good_responses': 0,
                    'ocsp_revoked_responses': 0,
                    'ocsp_unknown_responses': 0,
                    'ocsp_internal_errors': 0
                }
            },
            'oscp_stapling': {
                'ocsp_stapling_requests': 0,
                'ocsp_stapling_responses': 0,
                'ocsp_stapling_valid_responses': 0,
                'ocsp_stapling_revoked_responses': 0,
                'ocsp_stapling_unknown_responses': 0,
                'ocsp_response_validation_failure': 0
            },
            'ssl_statistics': {
                'flow_requested_ssl_tls_version': {
                    'ssl_v2_flows': 0,
                    'ssl_v3_flows': 0,
                    'tls_1.0_flows': 0,
                    'tls_1.1_flows': 0,
                    'tls_1.2_flows': 0,
                    'tls_1.3_flows': 0
                },
                'flow_selected_ssl_tls_version': {
                    'tls_1.0_flows': 0,
                    'tls_1.1_flows': 0,
                    'tls_1.2_flows': 0
                },
                'client_hello_extensions': {
                    'pushdown': 0,
                    'bypass': 0,
                    'strip': 0,
                    'process': 0
                },
                'ssl_handshake_statistics': {
                    'ssl_handshakes_started': 0,
                    'ssl_handshakes_completed': 0,
                    'full_ssl_handshakes': 0,
                    'ssl_renegotiation': 0,
                    'ssl_resumption': 0,
                    'ssl_resumption_session_id': 0,
                    'ssl_resumption_session_tkt': 0,
                    'ssl_fallback_to_full_hs': 0,
                    'ssl_failed_renego': 0,
                    'ssl_server_cert_validation_reqs': 0,
                    'ssl_server_cert_validation_success': 0,
                    'server_cert_verify_failed_expired': 0,
                    'server_cert_verify_failed_untrusted': 0,
                    'ssl_client_cert_validation_reqs': 0,
                    'ssl_client_cert_validation_success': 0,
                    'client_cert_verify_failed_expired': 0,
                    'client_cert_verify_failed_untrusted': 0,
                    'revocation_check_requests': 0,
                    'revocation_check_good_response': 0
                },
                'policy_statistics': {
                    'drop': {
                        'expired_certificate': 0,
                        'failure_mode': 0,
                        'unknown_status': 0,
                        'unsupported_cipher_suites': 0,
                        'unsupported_protocol_versions': 0,
                        'untrusted_certificate': 0
                    },
                    'decrypt': {
                        'expired_certificate': 0,
                        'failure_mode': 0,
                        'unknown_status': 0,
                        'untrusted_certificate': 0
                    },
                    'no_decrypt': {
                        'unsupported_cipher_suites': 0,
                        'unsupported_protocol_versions': 0
                    }
                }
            },
            'packet_counters': {
                'proxy_server': {
                    'from_client': 0,
                    'to_sc': 0,
                    'from_sc': 0,
                    'to_client': 0
                },
                'proxy_client': {
                    'from_server': 0,
                    'to_sc': 0,
                    'from_sc': 0,
                    'to_server': 0
                },
                'clear_packets': {
                    'proxy_server': {
                        'from_client': 0,
                        'to_sc': 0,
                        'from_sc': 0,
                        'to_client': 0
                    },
                    'proxy_client': {
                        'from_server': 0,
                        'to_sc': 0,
                        'from_sc': 0,
                        'to_server': 0
                    }
                },
                'dropped_packets': {
                    'c2s_wcapi_deny_packet': 0,
                    's2c_wcapi_deny_packet': 0
                }
            }
        }
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSslProxyStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSslProxyStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
		unittest.main()
