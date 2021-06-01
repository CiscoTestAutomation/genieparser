# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional

class ShowSslproxyStatusSchema(MetaParser):
    ''' Schema for show sslproxy status'''
    schema = {
        'configuration': {
            Optional('ca_cert_bundle'): str,
            'ca_tp_label': str,
            'cert_lifetime': int,
            'ec_key_type': str,
            'rsa_key_modulus': int,
            'cert_revocation': str,
            'expired_cert': str,
            'untrusted_cert': str,
            'unknown_status': str,
            'unsupported_protocol_ver': str,
            'unsupported_cipher_suites': str,
            'failure_mode_action': str,
            'min_tls_ver': str,
        },
        'status': {
            Optional('ssl_proxy_operational_state'): str,
            Optional('tcp_proxy_operational_state'): str,
            'clear_mode': str,
        }
    }


class ShowSslproxyStatus(ShowSslproxyStatusSchema):

    """ Parser for "show sslproxy status" """

    cli_command = "show sslproxy status"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # Configuration
        p1 = re.compile(r'^Configuration$')

        # Status
        p2 = re.compile(r'^Status$')

        # CA Cert Bundle                 : /bootflash/vmanage-admin/sslProxyDefaultCAbundle.pem
        # CA TP Label                    : PROXY-SIGNING-CA
        # Cert Lifetime                  : 730
        # EC Key type                    : P256
        # RSA Key Modulus                : 2048
        # Cert Revocation                : NONE
        # Expired Cert                   : drop
        # Untrusted Cert                 : drop
        # Unknown Status                 : drop
        # Unsupported Protocol Ver       : drop
        # Unsupported Cipher Suites      : drop
        # Failure Mode Action            : close
        # Min TLS Ver                    : TLS Version 1.1
        # SSL Proxy Operational State    : RUNNING
        # TCP Proxy Operational State    : RUNNING
        # Clear Mode                     : FALSE
        p3 = re.compile(r'^(?P<key>[\s\S]+\w) +: +(?P<value>[\s\S]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Configuration
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                configuration_dict = parsed_dict.setdefault('configuration', {})
                last_dict_ptr = configuration_dict
                continue

            # Status
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                status_dict = parsed_dict.setdefault('status', {})
                last_dict_ptr = status_dict
                continue

            # CA Cert Bundle                 : /bootflash/vmanage-admin/sslProxyDefaultCAbundle.pem
            # CA TP Label                    : PROXY-SIGNING-CA
            # Cert Lifetime                  : 730
            # EC Key type                    : P256
            # RSA Key Modulus                : 2048
            # Cert Revocation                : NONE
            # Expired Cert                   : drop
            # Untrusted Cert                 : drop
            # Unknown Status                 : drop
            # Unsupported Protocol Ver       : drop
            # Unsupported Cipher Suites      : drop
            # Failure Mode Action            : close
            # Min TLS Ver                    : TLS Version 1.1
            # SSL Proxy Operational State    : RUNNING
            # TCP Proxy Operational State    : RUNNING
            # Clear Mode                     : FALSE
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                last_dict_ptr.update({key: value})

        return parsed_dict


class ShowSslProxyStatisticsSchema(MetaParser):
    ''' Schema for show sslproxy statistics'''
    schema = {
        "sslproxy_statistics":{
            "connection_statistics":{
                "total_connections": int,
                "proxied_connections": int,
                "non_proxied_connections": int,
                "clear_connections": int,
                "active_proxied_connections": int,
                "active_non_proxied_connections": int,
                "active_clear_connections": int,
                "max_conc_proxied_connections": int,
                "max_conc_non_proxied_connections": int,
                "max_conc_clear_connections": int,
                "total_closed_connections": int
            },
            "non_proxied_connection_reasons":{
                Optional("unsupported_cipher"): int,
                Optional("unsupported_ssl_version"): int,
                Optional("non_ssl_traffic"): int,
                Optional("memory_allocation_failure"): int,
                Optional("memory_access_failure"): int,
                Optional("handshake_unsupported"): int,
                Optional("ssl_parse_failure"): int,
                Optional("ssl_error"): int,
                Optional("unexpected_packet"): int,
                Optional("ism_state_error"): int,
                Optional("exception"): int,
                Optional("endpoint_alert"): int,
                Optional("fin_rst_received_during_handshake"): int,
                Optional("pushdown_by_sc"): int,
                Optional("ism_flow_create_failure"): int,
                Optional("pushdown_default"): int
            },
            "dropped_connection_reasons":{
                Optional("unsupported_ssl_version"): int,
                Optional("unsupported_cipher"): int,
                Optional("untrusted_certificate"): int,
                Optional("unable_to_get_proxy_certificate"): int,
                Optional("expired_certificate"): int,
                Optional("ocsp_cert_verification_failure"): int,
                Optional("handshake_unsupported"): int,
                Optional("endpoint_alert"): int,
                Optional("fin_rst_received_during_handshake"): int,
                Optional("read_in_invalid_state"): int,
                Optional("invalid_fsm_event_received"): int,
                Optional("invalid_msg_type_rcvd_from_ism_de"): int,
                Optional("event_received_in_wrong_state"): int,
                Optional("ism_key_packet_send_fail"): int,
                Optional("ism_flow_create_failure"): int,
                Optional("failed_to_load_key_in_de"): int,
                Optional("invalid_peer_segment"): int,
                Optional("fail_to_get_orig_ch_during_pushdown"): int,
                Optional("decrypt_encrypt_failure"): int,
                Optional("rst_rcvd_during_ps_pc_key_pending"): int,
                Optional("no_ssl_record_in_flow_segment"): int,
                Optional("memory_allocation_failure"): int,
                Optional("memory_access_failure"): int,
                Optional("abort_on_ssl_parse_failure"): int,
                Optional("failed_to_save_orig_client_hello"):int,
                Optional("invalid_ssl_record_header"): int,
                Optional("unable_to_send_hs_message_to_ism"): int,
                Optional("fail_to_get_memory_from_pool_in_ism"): int
            },
            "alert_generated":{
                "c2s": int,
                "s2c": int
            },
            "alert_received":{
                "c2s": int,
                "s2c": int
            },
            "connection_closure_statistics":{
                "c2s":{
                    "fin_received_at_ps": int,
                    "fin_rec_after_ssl_handshake_at_ps": int,
                    "fin_rec_during_ssl_handshake_at_ps": int,
                    "fin_rec_for_non_ssl_conn_at_ps": int,
                    "fin_sent_to_sc_from_ps": int,
                    "fin_received_at_pc_from_sc": int,
                    "fin_sent_to_server": int,
                    "rst_generated_by_ps": int,
                    "rst_received_at_ps": int,
                    "rst_sent_to_sc_from_ps": int,
                    "rst_received_at_pc_from_sc": int,
                    "rst_sent_to_server": int,
                    "close_notify_received_at_ps": int,
                    "close_notify_fin_sent_to_sc_from_ps": int,
                    "close_notify_fin_rec_at_pc_from_sc": int,
                    "close_notify_sent_to_server": int
                },
                "s2c":{
                    "fin_received_at_pc": int,
                    "fin_rec_after_ssl_handshake_at_pc": int,
                    "fin_rec_during_ssl_handshake_at_pc": int,
                    "fin_rec_for_non_ssl_conn_at_pc": int,
                    "fin_sent_to_sc_from_pc": int,
                    "fin_received_at_ps_from_sc": int,
                    "fin_sent_to_client": int,
                    "rst_generated_by_pc": int,
                    "rst_received_at_pc": int,
                    "rst_sent_to_sc_from_pc": int,
                    "rst_received_at_ps_from_sc": int,
                    "rst_sent_to_client": int,
                    "close_notify_received_at_pc": int,
                    "close_notify_fin_sent_to_sc_from_pc": int,
                    "close_notify_fin_rec_at_ps_from_sc": int,
                    "close_notify_sent_to_client": int
                }
            },
            "proxy_server":{
                "lwssl_flow_create": int,
                "lwssl_flow_delete": int,
                Optional("lfs_mem_alloc_failure"): int,
                "fin_generated_by_sc": int,
                "rst_generated_by_sc": int,
                "close_notify_sent": int
            },
            "proxy_client":{
                "lwssl_flow_create": int,
                "lwssl_flow_delete": int,
                Optional("lfs_mem_alloc_failure"): int,
                "fin_generated_by_sc": int,
                "rst_generated_by_sc": int,
                "close_notify_sent": int
            },
            "ism":{
                "ism_flow_create": int,
                "ism_flow_delete": int,
                "ism_fifo_enqueue_failed": int,
                "ism_sem_post_failed": int,
                "lwssl_failed_to_send_msg": int,
                "lwssl_mem_alloc_failed_for_ism_msg": int
            },
            "resource_manager":{
                "session_alloc_success": int,
                "session_alloc_failures": int,
                "session_free_success": int,
                "session_free_failures": int
            },
            "oscp_statistics":{
                "app_statistics":{
                    "ocsp_requests": int,
                    "ocsp_responses": int,
                    "ocsp_timeouts": int,
                    "ocsp_failures": int,
                    "ocsp_good_responses": int,
                    "ocsp_revoked_responses": int,
                    "ocsp_unknown_responses": int,
                    "ocsp_internal_errors": int
                },
                "client_statistics":{
                    "ocsp_requests": int,
                    "ocsp_responses": int,
                    "ocsp_timeouts": int,
                    "ocsp_failures": int,
                    "ocsp_good_responses": int,
                    "ocsp_revoked_responses": int,
                    "ocsp_unknown_responses": int,
                    "ocsp_internal_errors": int
                }
            },
            Optional("oscp_stapling"):{
                "ocsp_stapling_requests": int,
                "ocsp_stapling_responses": int,
                "ocsp_stapling_valid_responses": int,
                "ocsp_stapling_revoked_responses": int,
                "ocsp_stapling_unknown_responses": int,
                "ocsp_response_validation_failure": int
            },
            "ssl_statistics":{
                "flow_requested_ssl_tls_version":{
                    Optional("ssl_v2_flows"): int,
                    Optional("ssl_v3_flows"): int,
                    Optional("tls_1.0_flows"): int,
                    Optional("tls_1.1_flows"): int,
                    Optional("tls_1.2_flows"): int,
                    Optional("tls_1.3_flows"): int
                },
                "flow_selected_ssl_tls_version":{
                    Optional("tls_1.0_flows"): int,
                    Optional("tls_1.1_flows"): int,
                    Optional("tls_1.2_flows"): int
                },
                "client_hello_extensions":{
                    Optional("pushdown"): int,
                    Optional("bypass"): int,
                    Optional("strip"): int,
                    Optional("process"): int
                },
                "ssl_handshake_statistics":{
                    Optional("ssl_handshakes_started"): int,
                    Optional("ssl_handshakes_completed"): int,
                    Optional("full_ssl_handshakes"): int,
                    Optional("ssl_renegotiation"): int,
                    Optional("ssl_resumption"): int,
                    Optional("ssl_resumption_session_id"): int,
                    Optional("ssl_resumption_session_tkt"): int,
                    Optional("ssl_fallback_to_full_hs"): int,
                    Optional("ssl_failed_renego"): int,
                    Optional("ssl_cert_validation_success"):int,
                    Optional("ssl_cert_validation_reqs"):int,
                    Optional("cert_validation_failures"):int,
                    Optional("ssl_server_cert_validation_reqs"): int,
                    Optional("ssl_server_cert_validation_success"): int,
                    Optional("server_cert_verify_failed_expired"): int,
                    Optional("server_cert_verify_failed_untrusted"): int,
                    Optional("ssl_client_cert_validation_reqs"): int,
                    Optional("ssl_client_cert_validation_success"): int,
                    Optional("client_cert_verify_failed_expired"): int,
                    Optional("client_cert_verify_failed_untrusted"): int,
                    Optional("revocation_check_requests"): int,
                    Optional("revocation_check_good_response"): int
                },
                "policy_statistics":{
                    "drop":{
                        "expired_certificate": int,
                        "failure_mode": int,
                        "unknown_status": int,
                        "unsupported_cipher_suites": int,
                        "unsupported_protocol_versions": int,
                        "untrusted_certificate": int
                    },
                    "decrypt":{
                        "expired_certificate": int,
                        "failure_mode": int,
                        "unknown_status": int,
                        "untrusted_certificate": int
                    },
                    "no_decrypt":{
                        "unsupported_cipher_suites": int,
                        "unsupported_protocol_versions": int
                    }
                }
            },
            "packet_counters":{
                "proxy_server":{
                    "from_client": int,
                    "to_sc": int,
                    "from_sc": int,
                    "to_client": int
                },
                "proxy_client":{
                    "from_server": int,
                    "to_sc": int,
                    "from_sc": int,
                    "to_server": int
                },
                "clear_packets":{
                    "proxy_server":{
                        "from_client": int,
                        "to_sc": int,
                        "from_sc": int,
                        "to_client": int
                    },
                    "proxy_client":{
                        "from_server": int,
                        "to_sc": int,
                        "from_sc": int,
                        "to_server": int
                    }
                },
                "dropped_packets":{
                    "c2s_wcapi_deny_packet": int,
                    "s2c_wcapi_deny_packet": int
                }
            }
        }
    }


class ShowSslProxyStatistics(ShowSslProxyStatisticsSchema):

    """ Parser for show sslproxy statistics"""

    cli_command = "show sslproxy statistics"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)

        # SSL Proxy Statistics
        p1 = re.compile(r'^SSL +Proxy +Statistics$')

        # Connection Statistics:
        p2 = re.compile(r'^Connection +Statistics:$')

        # Non-proxied Connection Reasons:
        p3 = re.compile(r'^Non-proxied +Connection +Reasons:$')

        # Dropped Connection Reasons:
        p4 = re.compile(r'^Dropped +Connection +Reasons:$')

        # Alert Generated:
        p5 = re.compile(r'^Alert +Generated:$')

        # Alert Received:
        p6 = re.compile(r'^Alert +Received:$')

        # Connection Closure Statistics:
        p7 = re.compile(r'^Connection +Closure +Statistics:$')

        # C2S
        # S2C
        p8 = re.compile(r'^(?P<c2s_s2c_stats>[C2S|S2C]+)$')

        # Proxy Server:
        p9 = re.compile(r'^Proxy +Server:$')

        # Proxy Client:
        p10 = re.compile(r'^Proxy +Client:$')

        # ISM:
        p11 = re.compile(r'^ISM:$')

        # Resource Manager:
        p12 = re.compile(r'^Resource +Manager:$')

        # OCSP Statistics:
        p13 = re.compile(r'^OCSP +Statistics:$')

        # APP Statistics
        # Client Statistics
        p14 = re.compile(r'^(?P<oscp_stats>[APP Statistics|Client Statistics]+)$')

        # SSL Statistics:
        p15 = re.compile(r'^SSL +Statistics:$')

        # Flow Requested SSL/TLS version:
        p16 = re.compile(r'^Flow +Requested +SSL/TLS +version:$')

        # Flow Selected SSL/TLS version:
        p17 = re.compile(r'^Flow +Selected +SSL/TLS +version:$')

        # Client Hello Extensions:
        p18 = re.compile(r'^Client +Hello +Extensions:$')

        # SSL Handshake Statistics:
        p19 = re.compile(r'^SSL +Handshake +Statistics:$')

        # Policy Statistics:
        p20 = re.compile(r'^Policy +Statistics:$')

        # Packet Counters:
        p21 = re.compile(r'^Packet +Counters:$')

        # Clear Packets:
        p22 = re.compile(r'^Clear +Packets:$')

        # Dropped Packets:
        p23 = re.compile(r'^Dropped +Packets:$')

        # Drop
        # Decrypt
        # No Decrypt
        p24 = re.compile(r'^(?P<policy_stats>[Drop|Decrypt|No Decrypt]+)$')

        # Proxy Server
        # Proxy Client
        p25 = re.compile(r'^(?P<proxy_type>Proxy +(Server|Client))$')

        # OCSP Stapling:
        p26 = re.compile(r'^OCSP +Stapling:$')

        # Note - Due to large output limited the sample match string comments
        # Total Connections                  : 0
        # Proxied Connections                : 0
        # Non-proxied Connections            : 0
        # Clear Connections                  : 0
        # Active Proxied Connections         : 0
        # Active Non-proxied Connections     : 0
        # Active Clear Connections           : 0
        # Max Conc Proxied Connections       : 0
        # Max Conc Non-proxied Connections   : 0
        # Max Conc Clear Connections         : 0
        # Total Closed Connections           : 0
        p27 = re.compile(r'^(?P<key>[\s\S]+\S)(\s+:|:) +(?P<value>[\d]+)$')

        parsed_dict = {}
        last_dict_ptr = {}

        for line in output.splitlines():
            line = line.strip()

            # SSL Proxy Statistics
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                sslproxy_statistics_dict = parsed_dict.setdefault('sslproxy_statistics', {})
                last_dict_ptr = sslproxy_statistics_dict
                continue

            # Connection Statistics:
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                connection_statistics_dict = sslproxy_statistics_dict.setdefault('connection_statistics', {})
                last_dict_ptr = connection_statistics_dict
                continue

            # Non-proxied Connection Reasons:
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                non_proxied_connection_reasons_dict = sslproxy_statistics_dict.setdefault('non_proxied_connection_reasons', {})
                last_dict_ptr = non_proxied_connection_reasons_dict
                continue

            # Dropped Connection Reasons:
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                dropped_connection_reasons_dict = sslproxy_statistics_dict.setdefault('dropped_connection_reasons', {})
                last_dict_ptr = dropped_connection_reasons_dict
                continue

            # Alert Generated:
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                alert_generated_dict = sslproxy_statistics_dict.setdefault('alert_generated', {})
                last_dict_ptr = alert_generated_dict
                continue

            # Alert Received:
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                alert_received_dict = sslproxy_statistics_dict.setdefault('alert_received', {})
                last_dict_ptr = alert_received_dict
                continue

            # Connection Closure Statistics:
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                connection_closure_statistics_dict = sslproxy_statistics_dict.setdefault('connection_closure_statistics', {})
                last_dict_ptr = connection_closure_statistics_dict
                continue

            # C2S
            # S2C
            m8 = p8.match(line)
            if m8:
                groups = m8.groupdict()
                if 'C2S' in groups['c2s_s2c_stats']:
                    c2s_stats_dict = connection_closure_statistics_dict.setdefault('c2s', {})
                    last_dict_ptr = c2s_stats_dict
                    continue
                if 'S2C' in groups['c2s_s2c_stats']:
                    s2c_stats_dict = connection_closure_statistics_dict.setdefault('s2c', {})
                    last_dict_ptr = s2c_stats_dict
                    continue

            # Proxy Server:
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                proxy_server_dict = sslproxy_statistics_dict.setdefault('proxy_server', {})
                last_dict_ptr = proxy_server_dict
                continue


            # Proxy Client:
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                proxy_client_dict = sslproxy_statistics_dict.setdefault('proxy_client', {})
                last_dict_ptr = proxy_client_dict
                continue

            # ISM:
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                ism_dict = sslproxy_statistics_dict.setdefault('ism', {})
                last_dict_ptr = ism_dict
                continue

            # Resource Manager:
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                resource_manager_dict = sslproxy_statistics_dict.setdefault('resource_manager', {})
                last_dict_ptr = resource_manager_dict
                continue

            # OCSP Statistics:
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                oscp_statistics_dict = sslproxy_statistics_dict.setdefault('oscp_statistics', {})
                last_dict_ptr = oscp_statistics_dict
                continue

            # APP Statistics
            # Client Statistics
            m14 = p14.match(line)
            if m14:
                groups = m14.groupdict()
                if 'APP Statistics' in groups['oscp_stats']:
                    app_statistics_dict = oscp_statistics_dict.setdefault('app_statistics', {})
                    last_dict_ptr = app_statistics_dict
                    continue
                if 'Client Statistics' in groups['oscp_stats']:
                    client_statistics_dict = oscp_statistics_dict.setdefault('client_statistics', {})
                    last_dict_ptr = client_statistics_dict
                    continue

            # SSL Statistics:
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                ssl_statistics_dict = sslproxy_statistics_dict.setdefault('ssl_statistics', {})
                last_dict_ptr = ssl_statistics_dict
                continue

            # Flow Requested SSL/TLS version:
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                flow_requested_ssl_tls_version_dict = ssl_statistics_dict.setdefault('flow_requested_ssl_tls_version', {})
                last_dict_ptr = flow_requested_ssl_tls_version_dict
                continue

            # Flow Selected SSL/TLS version:
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                flow_selected_ssl_tls_version_dict = ssl_statistics_dict.setdefault('flow_selected_ssl_tls_version', {})
                last_dict_ptr = flow_selected_ssl_tls_version_dict
                continue

            # Client Hello Extensions:
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                client_hello_extensions_dict = ssl_statistics_dict.setdefault('client_hello_extensions', {})
                last_dict_ptr = client_hello_extensions_dict
                continue

            # SSL Handshake Statistics:
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                ssl_handshake_statistics_dict = ssl_statistics_dict.setdefault('ssl_handshake_statistics', {})
                last_dict_ptr = ssl_handshake_statistics_dict
                continue

            # Policy Statistics:
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                policy_statistics_dict = ssl_statistics_dict.setdefault('policy_statistics', {})
                last_dict_ptr = policy_statistics_dict
                continue

            # Packet Counters:
            m21 = p21.match(line)
            if m21:
                group = m21.groupdict()
                packet_counters_dict = sslproxy_statistics_dict.setdefault('packet_counters', {})
                last_dict_ptr = packet_counters_dict
                continue

            # Clear Packets:
            m22 = p22.match(line)
            if m22:
                group = m22.groupdict()
                clear_packets_dict = packet_counters_dict.setdefault('clear_packets', {})
                last_dict_ptr = clear_packets_dict
                continue

            # Dropped Packets:
            m23 = p23.match(line)
            if m23:
                group = m23.groupdict()
                dropped_packets_dict = packet_counters_dict.setdefault('dropped_packets', {})
                last_dict_ptr = dropped_packets_dict
                continue

            # Drop
            # Decrypt
            # No Decrypt
            m24 = p24.match(line)
            if m24:
                groups = m24.groupdict()
                if 'Drop' in groups['policy_stats']:
                    drop_dict = policy_statistics_dict.setdefault('drop', {})
                    last_dict_ptr = drop_dict
                    continue
                if 'No Decrypt' in groups['policy_stats']:
                    no_decrypt_dict = policy_statistics_dict.setdefault('no_decrypt', {})
                    last_dict_ptr = no_decrypt_dict
                    continue
                if 'Decrypt' in groups['policy_stats']:
                    decrypt_dict = policy_statistics_dict.setdefault('decrypt', {})
                    last_dict_ptr = decrypt_dict
                    continue

            # Proxy Client
            # Proxy Server
            m25 = p25.match(line)
            if m25:
                group = m25.groupdict()
                proxy_type = group['proxy_type'].replace(' ', '_').lower()
                if 	proxy_type not in packet_counters_dict:
                    packet_counters_proxy_dict = packet_counters_dict.setdefault(proxy_type, {})
                    last_dict_ptr = packet_counters_proxy_dict
                    continue
                if 	proxy_type not in clear_packets_dict:
                    clear_packets_proxy_dict = clear_packets_dict.setdefault(proxy_type, {})
                    last_dict_ptr = clear_packets_proxy_dict
                    continue

            # OCSP Stapling:
            m26 = p26.match(line)
            if m26:
                group = m26.groupdict()
                oscp_stapling_dict = sslproxy_statistics_dict.setdefault('oscp_stapling', {})
                last_dict_ptr = oscp_stapling_dict
                continue

            # Total Connections                  : 0
            # Proxied Connections                : 0
            # Non-proxied Connections            : 0
            # Clear Connections                  : 0
            # Active Proxied Connections         : 0
            # Active Non-proxied Connections     : 0
            # Active Clear Connections           : 0
            # Max Conc Proxied Connections       : 0
            # Max Conc Non-proxied Connections   : 0
            # Max Conc Clear Connections         : 0
            # Total Closed Connections           : 0
            m27 = p27.match(line)
            if m27:
                groups = m27.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                key = re.sub(r'[^a-zA-Z0-9 \n\.]', '_', key)
                last_dict_ptr.update({key: int(groups['value'])})

        return parsed_dict
