import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxe.show_tcpproxy import (
    ShowTcpproxyStatus,
    ShowTcpProxyStatistics)


# ============================================
# unittest for 'show tcpproxy status'
# ============================================
class TestShowTcpproxyStatus(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        ==========================================================
                    TCP Proxy Status
        ==========================================================

        Configuration
        -------------
        VPG Name            : VirtualPortGroup2
        VPG IP Addr         : 192.168.2.1
        VPG IP Mask         : 255.255.255.0
        SNG Name            : SNG-APPQOE
        SNG IP Addr         : 192.168.2.2

        Status
        ------
        Operational State   : RUNNING
        '''
        }

    golden_parsed_output = {
        'configuration': {
            'vpg_name': 'VirtualPortGroup2',
            'vpg_ip_addr': '192.168.2.1',
            'vpg_ip_mask': '255.255.255.0',
            'sng_name': 'SNG-APPQOE',
            'sng_ip_addr': '192.168.2.2'
            },
        'status': {
            'operational_state': 'RUNNING'
            }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowTcpproxyStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowTcpproxyStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

# ============================================
# unittest for 'show tcpproxy statistics'
# ============================================
class TestShowTcpProxyStatistics(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        ==========================================================
                    TCP Proxy Statistics
        ==========================================================
        Total Connections                   : 32420
        Max Concurrent Connections          : 1466
        Flow Entries Created                : 32432
        Flow Entries Deleted                : 32432
        Current Flow Entries                : 0
        Current Connections                 : 0
        Connections In Progress             : 0
        Failed Connections                  : 12
	    Invalid Flow Entries : 0
        SYNCACHE Added                      : 32432
        SYNCACHE Not Added:NAT entry null   : 0
        SYNCACHE Not Added:Mrkd for Cleanup : 0
        SYN purge enqueued                  : 0
        SYN purge enqueue failed            : 0
        Other cleanup enqueued              : 0
        Other cleanup enqueue failed        : 0
        Stack Cleanup enqueued              : 11787
        Stack Cleanup enqueue failed        : 0
        Timer Expire Cleanup enqueued       : 0
        Timer Expire Cleanup enqueue failed : 0
        Proxy Cleanup enqueued              : 20645
        Proxy Cleanup enqueue failed        : 0
        Cleanup Req watcher called          : 118623
        Pre-tcp-flow-list enq failed        : 0
        Pre-tcp-flow-list deq failed(timer) : 0
        Pre-tcp-flow-list deq failed(accept): 0
        Pre-tcp-flow-list enq Success       : 32432
        Pre-tcp-flow-list deq (cleanup)     : 0
        Pre-tcp-flow-list deq (accept)      : 32432
        Pre-tcp cleanup timeout update count: 0
        Total Flow Entries pending cleanup  : 0
        Total Cleanup done                  : 32432
        Num stack cb with null ctx          : 0
        Vpath Cleanup from nmrx-thread      : 0
        Vpath Cleanup from ev-thread        : 32432
        Failed Conn already accepted conn   : 0
        SSL Init Failure                    : 0

        Max Queue Length Work               : 27
        Current Queue Length Work           : 0
        Max Queue Length ISM                : 0
        Current Queue Length ISM            : 0
        Max Queue Length SC                 : 0
        Current Queue Length SC             : 0
        Total Tx Enq Ign due to Conn Close  : 15
        Current Rx epoll                    : 0
        Current Tx epoll                    : 0

        Paused by TCP Tx Full               : 0
        Resumed by TCP Tx below threshold   : 0
        Paused by TCP Buffer Consumed       : 0
        Resumed by TCP Buffer Released      : 0
        SSL Pause Done                      : 0
        SSL Resume Done                     : 0
        SNORT Pause Done                    : 0
        SNORT Resume Done                   : 0
        EV SSL Pause Process                : 0
        EV SNORT Pause Process              : 0
        EV SSL/SNORT Resume Process         : 4728
        Socket Pause Done                   : 0
        Socket Resume Done                  : 4728
        SSL Pause Called                    : 0
        SSL Resume Called                   : 0
        Async Events Sent                   : 31822
        Async Events Processed              : 31822
        Tx Async Events Sent                : 416778
        Tx Async Events Recvd               : 416777
        Tx Async Events Processed           : 416777
        Failed Send                         : 0

        TCP SSL Reset Initiated             : 0
        TCP SNORT Reset Initiated           : 0
        TCP FIN Received from clnt/svr      : 44168
        TCP Reset Received from clnt/svr    : 24995
        SSL FIN Received -> SC              : 0
        SSL Reset Received -> SC            : 0
        SC FIN Received -> SSL              : 0
        SC Reset Received -> SSL            : 0
        SSL FIN Received -> TCP             : 0
        SSL Reset Received -> TCP           : 0
        TCP FIN Processed                   : 44168
        TCP FIN Ignored FD Already Closed   : 0
        TCP Reset Processed                 : 20672
        SVC Reset Processed                 : 0

        Flow Cleaned with Client Data       : 0
        Flow Cleaned with Server Data       : 0
        Buffers dropped in Tx socket close  : 1
        TCP 4k Allocated Buffers            : 416778
        TCP 16k Allocated Buffers           : 0
        TCP 32k Allocated Buffers           : 0
        TCP 128k Allocated Buffers          : 0
        TCP Freed Buffers                   : 449210
        SSL Allocated Buffers               : 0
        SSL Freed Buffers                   : 0
        TCP Received Buffers                : 351938
        TCP to SSL Enqueued Buffers         : 0
        SSL to SVC Enqueued Buffers         : 0
        SVC to SSL Enqueued Buffers         : 0
        SSL to TCP Enqueued Buffers         : 0
        TCP Buffers Sent                    : 351933

        TCP Failed Buffers Allocations      : 0
        TCP Failed 16k Buffers Allocations  : 0
        TCP Failed 32k Buffers Allocations  : 0
        TCP Failed 128k Buffers Allocations : 0
        SSL Failed Buffers Allocations      : 0
        Rx Sock Bytes Read < 512            : 49486
        Rx Sock Bytes Read < 1024           : 3207
        Rx Sock Bytes Read < 2048           : 18568
        Rx Sock Bytes Read < 4096           : 280677
        SSL Server Init                     : 0
        Flows Dropped-Snort Gbl Health Yellow        : 0
        Flows Dropped-Snort Inst Health Yellow       : 0
        Flows Dropped-WCAPI Channel Health Yellow    : 0
        Total WCAPI snd flow create svc chain failed : 0
        Total WCAPI send data svc chain failed       : 0
        Total WCAPI send close svc chain failed      : 0
        Total Tx Enqueue Failed                      : 0
        Total Cleanup Flow Msg Add to wk_q Failed    : 0
        Total Cleanup Flow Msg Added to wk_q         : 0
        Total Cleanup Flow Msg Rcvd in wk_q          : 0
        Total Cleanup Flow Ignored, Already Done     : 0
        Total Cleanup SSL Msg Add to wk_q Failed     : 0
        Total UHI mmap                               : 7793
        Total UHI munmap                             : 0
	    Total UHI Page Alloc : 0
	    Total UHI Page Alloc Retry : 0
	    Total UHI Page Alloc Failed : 0
	    Total UHI Page Alloc Failed Invalid Size : 0
	    Total UHI Page Free : 0

        Total Enable Rx Enqueued                     : 0
        Total Enable Rx Called                       : 0
        Total Enable Rx Process Done                 : 0
        Total Enable Rx Enqueue Failed               : 0
        Total Enable Rx Process Failed               : 0
        Total Enable Rx socket on Client Stack Close : 11228
        Total Enable Rx socket on Server Stack Close : 20594
	    Unified Logging Msg Received : 0
	    Unified Logging Drop (Data Too Long) : 0
	    Unified Logging Enqueue Success : 0
	    Unified Logging Dequeue Success : 0
	    Unified Logging Deq Fail(not enough space) : 0
        Flow Stats Add Failure count                 : 0
        Flow Stats Delete Failure count              : 0
	    AOIM Sync Started : 0
	    AOIM Sync Completed : 0
	    AOIM Sync Errored : 0
        '''
        }

    golden_parsed_output = {
        'tcpproxy_statistics': {
            'total_connections': 32420,
            'max_concurrent_connections': 1466,
            'flow_entries_created': 32432,
            'flow_entries_deleted': 32432,
            'current_flow_entries': 0,
            'current_connections': 0,
            'connections_in_progress': 0,
            'failed_connections': 12,
            'invalid_flow_entries': 0,
            'syncache_added': 32432,
            'syncache_not_added_nat_entry_null': 0,
            'syncache_not_added_mrkd_for_cleanup': 0,
            'syn_purge_enqueued': 0,
            'syn_purge_enqueue_failed': 0,
            'other_cleanup_enqueued': 0,
            'other_cleanup_enqueue_failed': 0,
            'stack_cleanup_enqueued': 11787,
            'stack_cleanup_enqueue_failed': 0,
            'timer_expire_cleanup_enqueued': 0,
            'timer_expire_cleanup_enqueue_failed': 0,
            'proxy_cleanup_enqueued': 20645,
            'proxy_cleanup_enqueue_failed': 0,
            'cleanup_req_watcher_called': 118623,
            'pre_tcp_flow_list_enq_failed': 0,
            'pre_tcp_flow_list_deq_failed_timer': 0,
            'pre_tcp_flow_list_deq_failed_accept': 0,
            'pre_tcp_flow_list_enq_success': 32432,
            'pre_tcp_flow_list_deq_cleanup': 0,
            'pre_tcp_flow_list_deq_accept': 32432,
            'pre_tcp_cleanup_timeout_update_count': 0,
            'total_flow_entries_pending_cleanup': 0,
            'total_cleanup_done': 32432,
            'num_stack_cb_with_null_ctx': 0,
            'vpath_cleanup_from_nmrx_thread': 0,
            'vpath_cleanup_from_ev_thread': 32432,
            'failed_conn_already_accepted_conn': 0,
            'ssl_init_failure': 0,
            'max_queue_length_work': 27,
            'current_queue_length_work': 0,
            'max_queue_length_ism': 0,
            'current_queue_length_ism': 0,
            'max_queue_length_sc': 0,
            'current_queue_length_sc': 0,
            'total_tx_enq_ign_due_to_conn_close': 15,
            'current_rx_epoll': 0,
            'current_tx_epoll': 0,
            'paused_by_tcp_tx_full': 0,
            'resumed_by_tcp_tx_below_threshold': 0,
            'paused_by_tcp_buffer_consumed': 0,
            'resumed_by_tcp_buffer_released': 0,
            'ssl_pause_done': 0,
            'ssl_resume_done': 0,
            'snort_pause_done': 0,
            'snort_resume_done': 0,
            'ev_ssl_pause_process': 0,
            'ev_snort_pause_process': 0,
            'ev_ssl_snort_resume_process': 4728,
            'socket_pause_done': 0,
            'socket_resume_done': 4728,
            'ssl_pause_called': 0,
            'ssl_resume_called': 0,
            'async_events_sent': 31822,
            'async_events_processed': 31822,
            'tx_async_events_sent': 416778,
            'tx_async_events_recvd': 416777,
            'tx_async_events_processed': 416777,
            'failed_send': 0,
            'tcp_ssl_reset_initiated': 0,
            'tcp_snort_reset_initiated': 0,
            'tcp_fin_received_from_clnt_svr': 44168,
            'tcp_reset_received_from_clnt_svr': 24995,
            'ssl_fin_received_sc': 0,
            'ssl_reset_received_sc': 0,
            'sc_fin_received_ssl': 0,
            'sc_reset_received_ssl': 0,
            'ssl_fin_received_tcp': 0,
            'ssl_reset_received_tcp': 0,
            'tcp_fin_processed': 44168,
            'tcp_fin_ignored_fd_already_closed': 0,
            'tcp_reset_processed': 20672,
            'svc_reset_processed': 0,
            'flow_cleaned_with_client_data': 0,
            'flow_cleaned_with_server_data': 0,
            'buffers_dropped_in_tx_socket_close': 1,
            'tcp_4k_allocated_buffers': 416778,
            'tcp_16k_allocated_buffers': 0,
            'tcp_32k_allocated_buffers': 0,
            'tcp_128k_allocated_buffers': 0,
            'tcp_freed_buffers': 449210,
            'ssl_allocated_buffers': 0,
            'ssl_freed_buffers': 0,
            'tcp_received_buffers': 351938,
            'tcp_to_ssl_enqueued_buffers': 0,
            'ssl_to_svc_enqueued_buffers': 0,
            'svc_to_ssl_enqueued_buffers': 0,
            'ssl_to_tcp_enqueued_buffers': 0,
            'tcp_buffers_sent': 351933,
            'tcp_failed_buffers_allocations': 0,
            'tcp_failed_16k_buffers_allocations': 0,
            'tcp_failed_32k_buffers_allocations': 0,
            'tcp_failed_128k_buffers_allocations': 0,
            'ssl_failed_buffers_allocations': 0,
            'rx_sock_bytes_read_512': 49486,
            'rx_sock_bytes_read_1024': 3207,
            'rx_sock_bytes_read_2048': 18568,
            'rx_sock_bytes_read_4096': 280677,
            'ssl_server_init': 0,
            'flows_dropped_snort_gbl_health_yellow': 0,
            'flows_dropped_snort_inst_health_yellow': 0,
            'flows_dropped_wcapi_channel_health_yellow': 0,
            'total_wcapi_snd_flow_create_svc_chain_failed': 0,
            'total_wcapi_send_data_svc_chain_failed': 0,
            'total_wcapi_send_close_svc_chain_failed': 0,
            'total_tx_enqueue_failed': 0,
            'total_cleanup_flow_msg_add_to_wk_q_failed': 0,
            'total_cleanup_flow_msg_added_to_wk_q': 0,
            'total_cleanup_flow_msg_rcvd_in_wk_q': 0,
            'total_cleanup_flow_ignored_already_done': 0,
            'total_cleanup_ssl_msg_add_to_wk_q_failed': 0,
            'total_uhi_mmap': 7793,
            'total_uhi_munmap': 0,
            'total_uhi_page_alloc': 0,
            'total_uhi_page_alloc_retry': 0,
            'total_uhi_page_alloc_failed': 0,
            'total_uhi_page_alloc_failed_invalid_size': 0,
            'total_uhi_page_free': 0,
            'total_enable_rx_enqueued': 0,
            'total_enable_rx_called': 0,
            'total_enable_rx_process_done': 0,
            'total_enable_rx_enqueue_failed': 0,
            'total_enable_rx_process_failed': 0,
            'total_enable_rx_socket_on_client_stack_close': 11228,
            'total_enable_rx_socket_on_server_stack_close': 20594,
            'unified_logging_msg_received': 0,
            'unified_logging_drop_data_too_long': 0,
            'unified_logging_enqueue_success': 0,
            'unified_logging_dequeue_success': 0,
            'unified_logging_deq_fail_not_enough_space': 0,
            'flow_stats_add_failure_count': 0,
            'flow_stats_delete_failure_count': 0,
            'aoim_sync_started': 0,
            'aoim_sync_completed': 0,
            'aoim_sync_errored': 0
            }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowTcpProxyStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowTcpProxyStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
		unittest.main()