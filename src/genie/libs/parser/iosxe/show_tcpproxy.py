# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional

class ShowTcpproxyStatusSchema(MetaParser):
    ''' Schema for show tcpproxy status'''
    schema = {
        'configuration': {
            'vpg_name': str,
            'vpg_ip_addr': str,
            'vpg_ip_mask': str,
            'sng_name': str,
            'sng_ip_addr': str,
        },
        'status': {
            'operational_state': str,
        }
    }


class ShowTcpproxyStatus(ShowTcpproxyStatusSchema):

    """ Parser for "show tcpproxy status" """

    cli_command = "show tcpproxy status"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        last_dict_ptr = {}

        # Configuration
        p1 = re.compile(r'^Configuration$')

        # Status
        p2 = re.compile(r'^Status$')

        # VPG Name            : VirtualPortGroup2
        # VPG IP Addr         : 192.168.2.1
        # VPG IP Mask         : 255.255.255.0
        # SNG Name            : SNG-APPQOE
        # SNG IP Addr         : 192.168.2.2
        # Operational State   : RUNNING
        p3 = re.compile(r'^(?P<key>[\s\S]+\w) +: +(?P<value>[\s\S]+)$')

        for line in output.splitlines():
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

            # VPG Name            : VirtualPortGroup2
            # VPG IP Addr         : 192.168.2.1
            # VPG IP Mask         : 255.255.255.0
            # SNG Name            : SNG-APPQOE
            # SNG IP Addr         : 192.168.2.2
            # Operational State   : RUNNING
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                value = groups['value']
                last_dict_ptr.update({key: value})

        return parsed_dict

class ShowTcpProxyStatisticsSchema(MetaParser):
    ''' Schema for show tcpproxy statistics'''
    schema = {
        'tcpproxy_statistics':{
            'total_connections': int,
            'max_concurrent_connections': int,
            'flow_entries_created': int,
            'flow_entries_deleted': int,
            'current_flow_entries': int,
            Optional('current_valid_flow_entries'): int,
            'current_connections': int,
            'connections_in_progress': int,
            'failed_connections': int,
            Optional('invalid_flow_entries'): int,
            'syncache_added': int,
            Optional('syncache_not_added_nat_entry_null'): int,
            Optional('syncache_not_added_mrkd_for_cleanup'): int,
            Optional('syncache_not_added_flow_entry_null'): int,
            Optional('syncache_not_added_flow_invalid'): int,
            Optional('syncache_not_added_flow_is_in_use'): int,
            'syn_purge_enqueued': int,
            'syn_purge_enqueue_failed': int,
            'other_cleanup_enqueued': int,
            'other_cleanup_enqueue_failed': int,
            'stack_cleanup_enqueued': int,
            'stack_cleanup_enqueue_failed': int,
            'timer_expire_cleanup_enqueued': int,
            'timer_expire_cleanup_enqueue_failed': int,
            'proxy_cleanup_enqueued': int,
            'proxy_cleanup_enqueue_failed': int,
            Optional('proxy_cleanup_sent_to_ev_flow_q'): int,
            Optional('proxy_cleanup_enq_done_by_ev_flow_q'): int,
            'cleanup_req_watcher_called': int,
            'pre_tcp_flow_list_enq_failed': int,
            'pre_tcp_flow_list_deq_failed_timer': int,
            'pre_tcp_flow_list_deq_failed_accept': int,
            'pre_tcp_flow_list_enq_success': int,
            'pre_tcp_flow_list_deq_cleanup': int,
            'pre_tcp_flow_list_deq_accept': int,
            'pre_tcp_cleanup_timeout_update_count': int,
            Optional('total_flow_entries_pending_cleanup_0'): int,
            Optional('total_flow_entries_pending_cleanup'):int,
            'total_cleanup_done': int,
            'num_stack_cb_with_null_ctx': int,
            'vpath_cleanup_from_nmrx_thread': int,
            'vpath_cleanup_from_ev_thread': int,
            Optional('syncache_flow_mismatch'): int,
            Optional('failed_conn_already_accepted_conn'): int,
            'ssl_init_failure': int,
            Optional('max_queue_length_work'): int,
            Optional('current_queue_length_work'): int,
            Optional('max_queue_length_ism'): int,
            Optional('current_queue_length_ism'): int,
            Optional('current_queue_length_work'): int,
            Optional('max_queue_length_sc'): int,
            Optional('current_queue_length_sc'): int,
            'total_tx_enq_ign_due_to_conn_close': int,
            'current_rx_epoll': int,
            'current_tx_epoll': int,
            'paused_by_tcp_tx_full': int,
            'resumed_by_tcp_tx_below_threshold': int,
            'paused_by_tcp_buffer_consumed': int,
            'resumed_by_tcp_buffer_released': int,
            'ssl_pause_done': int,
            'ssl_resume_done': int,
            'snort_pause_done': int,
            'snort_resume_done': int,
            Optional('dre_pause_done'): int,
            Optional('dre_resume_done'): int,
            Optional('dre_resume_msg_to_be_sent'): int,
            Optional('dre_resume_msg_sent'): int,
            'ev_ssl_pause_process': int,
            'ev_snort_pause_process': int,
            Optional('ev_dre_pause_process'): int,
            'ev_ssl_snort_resume_process': int,
            'socket_pause_done': int,
            'socket_resume_done': int,
            'ssl_pause_called': int,
            'ssl_resume_called': int,
            'async_events_sent': int,
            'async_events_processed': int,
            'tx_async_events_sent': int,
            'tx_async_events_recvd': int,
            'tx_async_events_processed': int,
            'failed_send': int,
            'tcp_ssl_reset_initiated': int,
            'tcp_snort_reset_initiated': int,
            Optional('tcp_dre_close_initiated'): int,
            'tcp_fin_received_from_clnt_svr': int,
            'tcp_reset_received_from_clnt_svr': int,
            'ssl_fin_received_sc': int,
            'ssl_reset_received_sc': int,
            'sc_fin_received_ssl': int,
            'sc_reset_received_ssl': int,
            'ssl_fin_received_tcp': int,
            'ssl_reset_received_tcp': int,
            'tcp_fin_processed': int,
            'tcp_fin_ignored_fd_already_closed': int,
            'tcp_reset_processed': int,
            'svc_reset_processed': int,
            'flow_cleaned_with_client_data': int,
            'flow_cleaned_with_server_data': int,
            Optional('buffers_dropped_in_tx_sock_closed'): int,
            Optional('buffers_dropped_in_tx_not_writable'): int,
            Optional('buffers_dropped_in_tx_socket_close'): int,
            Optional('buffers_dropped_in_tx_socket_closed'): int,
            'tcp_4k_allocated_buffers': int,
            'tcp_16k_allocated_buffers': int,
            'tcp_32k_allocated_buffers': int,
            'tcp_128k_allocated_buffers': int,
            'tcp_freed_buffers': int,
            'ssl_allocated_buffers': int,
            'ssl_freed_buffers': int,
            'tcp_received_buffers': int,
            'tcp_to_ssl_enqueued_buffers': int,
            'ssl_to_svc_enqueued_buffers': int,
            'svc_to_ssl_enqueued_buffers': int,
            'ssl_to_tcp_enqueued_buffers': int,
            'tcp_buffers_sent': int,
            'tcp_failed_buffers_allocations': int,
            'tcp_failed_16k_buffers_allocations': int,
            'tcp_failed_32k_buffers_allocations': int,
            'tcp_failed_128k_buffers_allocations': int,
            'ssl_failed_buffers_allocations': int,
            'rx_sock_bytes_read_512': int,
            'rx_sock_bytes_read_1024': int,
            'rx_sock_bytes_read_2048': int,
            'rx_sock_bytes_read_4096': int,
            'ssl_server_init': int,
            'flows_dropped_snort_gbl_health_yellow': int,
            'flows_dropped_snort_inst_health_yellow': int,
            'flows_dropped_wcapi_channel_health_yellow': int,
            'total_wcapi_snd_flow_create_svc_chain_failed': int,
            Optional('total_wcapi_snd_flow_delete_svc_chain_failed'): int,
            'total_wcapi_send_data_svc_chain_failed': int,
            'total_wcapi_send_close_svc_chain_failed': int,
            'total_tx_enqueue_failed': int,
            'total_cleanup_flow_msg_add_to_wk_q_failed': int,
            'total_cleanup_flow_msg_added_to_wk_q': int,
            'total_cleanup_flow_msg_rcvd_in_wk_q': int,
            'total_cleanup_flow_ignored_already_done': int,
            'total_cleanup_ssl_msg_add_to_wk_q_failed': int,
            Optional('total_ssl_trigger_reset_msg_to_wk_q_failed'): int,
            'total_uhi_mmap': int,
            'total_uhi_munmap': int,
            Optional('total_uhi_page_alloc'): int,
            Optional('total_uhi_page_alloc_retry'): int,
            Optional('total_uhi_page_alloc_failed'): int,
            Optional('total_uhi_page_alloc_failed_invalid_size'): int,
            Optional('total_uhi_page_free'): int,
            'total_enable_rx_enqueued': int,
            'total_enable_rx_called': int,
            'total_enable_rx_process_done': int,
            'total_enable_rx_enqueue_failed': int,
            'total_enable_rx_process_failed': int,
            'total_enable_rx_socket_on_client_stack_close': int,
            'total_enable_rx_socket_on_server_stack_close': int,
            Optional('unified_logging_msg_received'): int,
            Optional('unified_logging_drop_data_too_long'): int,
            Optional('unified_logging_enqueue_success'): int,
            Optional('unified_logging_dequeue_success'): int,
            Optional('unified_logging_deq_fail_not_enough_space'): int,
            'flow_stats_add_failure_count': int,
            'flow_stats_delete_failure_count': int,
            Optional('aoim_sync_started'): int,
            Optional('aoim_sync_completed'): int,
            Optional('aoim_sync_errored'): int,
            Optional('current_queue_length_sc_0'): int,
            Optional('current_queue_length_ism_0'): int,
            Optional('max_queue_length_work_0'): int,
            Optional('max_queue_length_sc_0'): int,
            Optional('max_queue_length_ism_0'): int,
            Optional('current_queue_length_work_0'): int
            }
        }

class ShowTcpProxyStatistics(ShowTcpProxyStatisticsSchema):

    """ Parser for "show tcpproxy statistics" """

    cli_command = "show tcpproxy statistics"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)

        # TCP Proxy Statistics
        p1 = re.compile(r'^TCP +Proxy +Statistics$')

        # Total Connections                   : 32420
        # Max Concurrent Connections          : 1466
        # Flow Entries Created                : 32432
        # Flow Entries Deleted                : 32432
        # Current Flow Entries                : 0
        # Current Connections                 : 0
        # Connections In Progress             : 0
        # Failed Connections                  : 12
        # Invalid Flow Entries : 0
        # SYNCACHE Added                      : 32432
        # SYNCACHE Not Added:NAT entry null   : 0
        # SYNCACHE Not Added:Mrkd for Cleanup : 0
        # SYN purge enqueued                  : 0
        # SYN purge enqueue failed            : 0
        # Other cleanup enqueued              : 0
        # Other cleanup enqueue failed        : 0
        # Stack Cleanup enqueued              : 11787
        # Stack Cleanup enqueue failed        : 0
        # Timer Expire Cleanup enqueued       : 0
        # Timer Expire Cleanup enqueue failed : 0
        # Proxy Cleanup enqueued              : 20645
        # Proxy Cleanup enqueue failed        : 0
        # Cleanup Req watcher called          : 118623
        # Pre-tcp-flow-list enq failed        : 0
        # Pre-tcp-flow-list deq failed(timer) : 0
        # Pre-tcp-flow-list enq Success       : 32432
        # Pre-tcp-flow-list deq (cleanup)     : 0
        # Pre-tcp-flow-list deq (accept)      : 32432

        # Total Flow Entries pending cleanup  : 0
        # Total Cleanup done                  : 32432
        # Num stack cb with null ctx          : 0
        # Vpath Cleanup from nmrx-thread      : 0
        # Vpath Cleanup from ev-thread        : 32432
        # Failed Conn already accepted conn   : 0
        # SSL Init Failure                    : 0

        # Max Queue Length Work               : 27
        # Current Queue Length Work           : 0
        # Max Queue Length ISM                : 0
        # Current Queue Length ISM            : 0
        # Max Queue Length SC                 : 0
        # Current Queue Length SC             : 0
        # Total Tx Enq Ign due to Conn Close  : 15
        # Current Rx epoll                    : 0
        # Current Tx epoll                    : 0

        # Paused by TCP Tx Full               : 0
        # Resumed by TCP Tx below threshold   : 0
        # Paused by TCP Buffer Consumed       : 0
        # Resumed by TCP Buffer Released      : 0
        # SSL Pause Done                      : 0
        # SSL Resume Done                     : 0
        # SNORT Pause Done                    : 0
        # SNORT Resume Done                   : 0
        # EV SSL Pause Process                : 0
        # EV SNORT Pause Process              : 0
        # EV SSL/SNORT Resume Process         : 4728
        # Socket Pause Done                   : 0
        # Socket Resume Done                  : 4728
        # SSL Pause Called                    : 0
        # SSL Resume Called                   : 0
        # Async Events Sent                   : 31822
        # Async Events Processed              : 31822
        # Tx Async Events Sent                : 416778
        # Tx Async Events Recvd               : 416777
        # Tx Async Events Processed           : 416777
        # Failed Send                         : 0

        # TCP SSL Reset Initiated             : 0
        # TCP SNORT Reset Initiated           : 0
        # TCP FIN Received from clnt/svr      : 44168
        # TCP Reset Received from clnt/svr    : 24995
        # SSL FIN Received -> SC              : 0
        # SSL Reset Received -> SC            : 0
        # SC FIN Received -> SSL              : 0
        # SC Reset Received -> SSL            : 0
        # SSL FIN Received -> TCP             : 0
        # SSL Reset Received -> TCP           : 0
        # TCP FIN Processed                   : 44168
        # TCP FIN Ignored FD Already Closed   : 0
        # TCP Reset Processed                 : 20672
        # SVC Reset Processed                 : 0

        # Flow Cleaned with Client Data       : 0
        # Flow Cleaned with Server Data       : 0
        # Buffers dropped in Tx socket close  : 1
        # TCP 4k Allocated Buffers            : 416778
        # TCP 16k Allocated Buffers           : 0
        # TCP 32k Allocated Buffers           : 0
        # TCP 128k Allocated Buffers          : 0
        # TCP Freed Buffers                   : 449210
        # SSL Allocated Buffers               : 0
        # SSL Freed Buffers                   : 0
        # TCP Received Buffers                : 351938
        # TCP to SSL Enqueued Buffers         : 0
        # SSL to SVC Enqueued Buffers         : 0
        # SVC to SSL Enqueued Buffers         : 0
        # SSL to TCP Enqueued Buffers         : 0
        # TCP Buffers Sent                    : 351933

        # TCP Failed Buffers Allocations      : 0
        # TCP Failed 16k Buffers Allocations  : 0
        # TCP Failed 32k Buffers Allocations  : 0
        # TCP Failed 128k Buffers Allocations : 0
        # SSL Failed Buffers Allocations      : 0
        # Rx Sock Bytes Read < 512            : 49486
        # Rx Sock Bytes Read < 1024           : 3207
        # Rx Sock Bytes Read < 2048           : 18568
        # Rx Sock Bytes Read < 4096           : 280677
        # SSL Server Init                     : 0
        # Flows Dropped-Snort Gbl Health Yellow        : 0
        # Flows Dropped-Snort Inst Health Yellow       : 0
        # Flows Dropped-WCAPI Channel Health Yellow    : 0
        # Total WCAPI snd flow create svc chain failed : 0
        # Total WCAPI send data svc chain failed       : 0
        # Total WCAPI send close svc chain failed      : 0
        # Total Tx Enqueue Failed                      : 0
        # Total Cleanup Flow Msg Add to wk_q Failed    : 0
        # Total Cleanup Flow Msg Added to wk_q         : 0
        # Total Cleanup Flow Msg Rcvd in wk_q          : 0
        # Total Cleanup Flow Ignored, Already Done     : 0
        # Total Cleanup SSL Msg Add to wk_q Failed     : 0
        # Total UHI mmap                               : 7793
        # Total UHI munmap                             : 0
        # Total UHI Page Alloc : 0
        # Total UHI Page Alloc Retry : 0
        # Total UHI Page Alloc Failed : 0
        # Total UHI Page Alloc Failed Invalid Size : 0
        # Total UHI Page Free : 0
        # Total Enable Rx Enqueued                     : 0
        # Total Enable Rx Called                       : 0
        # Total Enable Rx Process Done                 : 0
        # Total Enable Rx Enqueue Failed               : 0
        # Total Enable Rx Process Failed               : 0
        # Total Enable Rx socket on Client Stack Close : 11228
        # Total Enable Rx socket on Server Stack Close : 20594
        # Unified Logging Msg Received : 0
        # Unified Logging Drop (Data Too Long) : 0
        # Unified Logging Enqueue Success : 0
        # Unified Logging Dequeue Success : 0
        # Unified Logging Deq Fail(not enough space) : 0
        # Flow Stats Add Failure count                 : 0
        # Flow Stats Delete Failure count              : 0
        # AOIM Sync Started : 0
        # AOIM Sync Completed : 0
        # AOIM Sync Errored : 0
        p2 = re.compile(r'^(?P<key>[\s\S]+\S)(\s+:|:) +(?P<value>[\d]+)$')

        parsed_dict = {}
        last_dict_ptr = {}

        for line in output.splitlines():
            line = line.strip()

            # TCP Proxy Statistics
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                tcpproxy_statistics_dict = parsed_dict.setdefault('tcpproxy_statistics', {})
                last_dict_ptr = tcpproxy_statistics_dict
                continue

            # Total Connections                   : 32420
            # Max Concurrent Connections          : 1466
            # Flow Entries Created                : 32432
            # Flow Entries Deleted                : 32432
            # Current Flow Entries                : 0
            # Current Connections                 : 0
            # Connections In Progress             : 0
            # Failed Connections                  : 12
            # SYNCACHE Added                      : 32432
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                key = re.sub(r'[^a-zA-Z0-9 \n\.]', '_', key)
                key = key.strip('_').replace('____', '_').replace('___', '_').replace('__', '_')
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                last_dict_ptr.update({key: value})

        return parsed_dict
