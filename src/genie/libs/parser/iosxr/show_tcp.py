"""show_tcp.py

IOSXR parser for the following show command:
    * 'show tcp detail pcb all '
"""
import re
from typing import Dict, Any

import genie.parsergen as pg

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

import logging

log = logging.getLogger(__name__)


# =======================================
# Schema for 'show tcp detail pcb all'
# =======================================
class ShowTcpDetailPcbAllSchema(MetaParser):
    """Schema for show tcp detail pcb all

    """
    schema = {
        'pcb_address': {
            Any(): {
                'connection_state': str,
                'io_status': int,
                'socket_status': int,
                'established_datetime': str,
                'tcp_connection_data': {
                    'pcb': str,
                    'so': str,
                    'tcpcb': str,
                    'vrfid': str,
                    'pak_prio': str,
                    'tos': int,
                    'ttl': int,
                    'hash_index': int,
                    'local_host': str,
                    'local_port': int,
                    'local_app_pid': int,
                    'foreign_host': str,
                    'foreign_port': int,
                    'local_app': {
                        'pid': int,
                        'instance': int,
                        'spl_id': int
                    }
                },
                'current_queue': {
                    'send': {
                        'send_size_bytes': int,
                        'max_send_size_bytes': int
                    },
                    'receive': {
                        Optional('receive_size_bytes'): int,
                        Optional('max_receive_size_bytes'): int,
                        Optional('mis_ordered_bytes'): int,
                        Optional('receive_size_packages'): int,
                        Optional('max_receive_size_packages'): int
                    }
                },
                'event_timers': {
                    Any(): {
                        'starts': int,
                        'wakeups': int,
                        'next_msec': int
                    }
                },
                'sequences': {
                    'iss': int,
                    'snduna': int,
                    'sndnxt': int,
                    'sndmax': int,
                    'sndwnd': int,
                    'sndcwnd': int,
                    'irs': int,
                    'rcvnxt': int,
                    'rcvwnd': int,
                    'rcvadv': int
                },
                'round_trip_delay': {
                    'srtt_ms': int,
                    'rtto_ms': int,
                    'rtv_ms': int,
                    'krtt_ms': int,
                    'min_rtt_ms': int,
                    'max_rtt_ms': int
                },
                'times': {
                    'ack_hold_ms': int,
                    'keepalive_sec': int,
                    'syn_waittime_sec': int,
                    'giveup_ms': int,
                    'retransmission_retries': int,
                    'retransmit_forever': str,
                    'connect_retries_remaining': int,
                    'connect_retry_interval_sec': int
                },
                'flags': {
                    'state': str,
                    'feature': str,
                    'request': str
                },
                'datagrams': {
                    'mss_bytes': int,
                    'peer_mss_bytes': int,
                    'min_mss_bytes': int,
                    'max_mss_bytes': int
                },
                'window_scales': {
                    'rcv': int,
                    'snd': int,
                    'request_rcv': int,
                    'request_snd': int
                },
                'timestamp_option': {
                    'recent': int,
                    'recent_age': int,
                    'last_ack_sent': int
                },
                'sack_blocks': {
                    'start': str,
                    'end': str
                },
                'sack_holes': {
                    'start': str,
                    'end': str,
                    'dups': str,
                    'rxmit': str
                },
                'socket_options': str,
                'socket_states': str,
                'socket_receive_buffer_states': str,
                'socket_send_buffer_states': str,
                'socket_receive_buffer': {
                    'watermarks': {
                        'low': int,
                        'high': int
                    }
                },
                'socket_send_buffer': {
                    'watermarks': {
                        'low': int,
                        'high': int
                    },
                    Optional('notify_threshold'): int
                },
                'socket_misc_info': {
                    'rcv_data_size': int,
                    'so_qlen': int,
                    'so_q0len': int,
                    'so_qlimit': int,
                    'so_error': int,
                    'so_auto_rearm': int
                },
                'pdu_information': {
                    'pdu_buffer': int,
                    'fib_lookup_cache': {
                        'ifh': str,
                        'pd_ctx': {
                            'size': int,
                            'data': str
                        }
                    },
                    Optional('num_label'): int,
                    Optional('label_stack'): int,
                    Optional('num_peers_with_authentication'): int
                }
            }

        }
    }


# =======================================
# Parser for 'show tcp detail pcb all'
# =======================================

class ShowTcpDetailPcbAll(ShowTcpDetailPcbAllSchema):
    """Parser for show users on iosxr"""

    cli_command = 'show tcp detail pcb all'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial root return dictionary
        ret_dict = {}
        temp_data = {}

        # Connection state is ESTAB, I/O status: 0, socket status: 0
        p1 = re.compile(r'^Connection +state +is *(?P<connection_state>\S+)'
                        r'(, *(I\/O +status: *(?P<io_status>\d+))?)?'
                        r'(, *(socket +status: *(?P<socket_status>\d+))?)?$')

        # Established at Mon Jul 12 09:44:25 2021
        p2 = re.compile(r'^Established +at +(?P<established_datetime>.+)$')

        # PCB 0x00007f553800d8f8, SO 0x7f5538008698, TCPCB 0x7f5538008b58, vrfid 0x60000000,
        p3 = re.compile(r'^PCB *(?P<pcb>\w+),? *'
                        r'((SO *(?P<so>\w+))?)?,? *'
                        r'((TCPCB *(?P<tcpcb>\w+))?)?,? *'
                        r'((vrfid *(?P<vrfid>\w+))?)?,?$')

        # Pak Prio: Medium, TOS: 192, TTL: 1, Hash index: 26
        p4 = re.compile(r'^Pak Prio: *(?P<pak_prio>\w+),?'
                        r' *(TOS: *(?P<tos>\d+))?,?'
                        r' *(TTL: *(?P<ttl>\d+))?,?'
                        r' *(Hash index: *(?P<hash_index>\d+))?$')

        # Local host: 2000:108:10::1, Local port: 179 (Local App PID: 11298)
        p5 = re.compile(r'^Local host: *(?P<local_host>((\d{1,5}:)+:\d+))'
                        r'(,? *(Local port: *(?P<local_port>\d+))?,? *)?'
                        r'(\(Local App PID: *(?P<local_app_pid>\d+)\))?$')

        # Foreign host: 2000:108:10::2, Foreign port: 56357
        p6 = re.compile(r'^Foreign host: *(?P<foreign_host>\S+), '
                        r'(Foreign port: *(?P<foreign_port>\d+))?$')

        # (Local App PID/instance/SPL_APP_ID: 11298/1/0)
        p7 = re.compile(r'^\(Local App PID\/instance\/SPL_APP_ID: *(?P<local_instance_spl>\S+)\)$')

        # Current send queue size in bytes: 0 (max 24576)
        p8 = re.compile(r'^Current send queue size in bytes: *(?P<send_queue_size_bytes>\d+)'
                        r' *(\(max *(?P<send_max_bytes>\d+)\))?$')

        # Current receive queue size in bytes: 0 (max 32768)  mis-ordered: 0 bytes
        p9 = re.compile(r'^Current receive queue size in bytes: *(?P<receive_queue_size_bytes>\d+) *'
                        r'(\(max *(?P<receive_max_bytes>\d+)\))? *'
                        r'(mis-ordered: *(?P<receive_mis_ordered_bytes>\d+) * bytes)?$')

        # Current receive queue size in packets: 0 (max 0)
        p10 = re.compile(r'^Current receive queue size in packets: *(?P<receive_queue_packages>\d+) *'
                         r'(\(max *(?P<receive_max_packages>\d+)\))?$')

        # Timer          Starts    Wakeups         Next(msec)
        p11 = re.compile(r'^Timer +Starts +Wakeups +Next\(msec\)$')

        # Retrans             3          0                0
        p12 = re.compile(r'^Retrans +(?P<retrans_starts>\d+) +'
                         r'(?P<retrans_wakeups>\d+) +'
                         r'(?P<retrans_next_msec>\d+)$')

        # SendWnd             0          0                0
        p13 = re.compile(r'^SendWnd +(?P<sendwnd_starts>\d+) +'
                         r'(?P<sendwnd_wakeups>\d+) +'
                         r'(?P<sendwnd_next_msec>\d+)$')

        # TimeWait            0          0                0
        p14 = re.compile(r'^TimeWait +(?P<timewait_starts>\d+) +'
                         r'(?P<timewait_wakeups>\d+) +'
                         r'(?P<timewait_next_msec>\d+)$')

        # AckHold             4          3                0
        p15 = re.compile(r'^AckHold +(?P<ackhold_starts>\d+) +'
                         r'(?P<ackhold_wakeups>\d+) +'
                         r'(?P<ackhold_next_msec>\d+)$')

        # KeepAlive           1          0                0
        p16 = re.compile(r'^KeepAlive +(?P<keepalive_starts>\d+) +'
                         r'(?P<keepalive_wakeups>\d+) +'
                         r'(?P<keepalive_next_msec>\d+)$')

        # PmtuAger            0          0                0
        p17 = re.compile(r'^PmtuAger +(?P<pmtuager_starts>\d+) +'
                         r'(?P<pmtuager_wakeups>\d+) +'
                         r'(?P<pmtuager_next_msec>\d+)$')

        # GiveUp              0          0                0
        p18 = re.compile(r'^GiveUp +(?P<giveup_starts>\d+) +'
                         r'(?P<giveup_wakeups>\d+) +'
                         r'(?P<giveup_next_msec>\d+)$')

        # Throttle            0          0                0
        p19 = re.compile(r'^Throttle +(?P<throttle_starts>\d+) +'
                         r'(?P<throttle_wakeups>\d+) +'
                         r'(?P<throttle_next_msec>\d+)$')

        #    iss: 1042166212  snduna: 1042166346  sndnxt: 1042166346
        p20 = re.compile(r'^(iss: *(?P<iss_sequence>\d+))? *'
                         r'(snduna: *(?P<snduna_sequence>\d+))? *'
                         r'(sndnxt: *(?P<sndnxt_sequence>\d+))?$')

        #    sndmax: 1042166346  sndwnd: 32739       sndcwnd: 2880
        p21 = re.compile(r'(sndmax: *(?P<sndmax_sequence>\d+) *)?'
                         r'(sndwnd: *(?P<sndwnd_sequence>\d+))? *'
                         r'(sndcwnd: *(?P<sndcwnd_sequence>\d+))?$')

        #    irs: 309426134   rcvnxt: 309426287   rcvwnd: 32701   rcvadv: 309458988
        p22 = re.compile(r'(irs: *(?P<irs_sequence>\d+) *)?'
                         r'(rcvnxt: *(?P<rcvnxt_sequence>\d+))? *'
                         r'(rcvwnd: *(?P<rcvwnd_sequence>\d+))? *'
                         r'(rcvadv: *(?P<rcvadv_sequence>\d+))?$')

        # SRTT: 28 ms,  RTTO: 300 ms,  RTV: 214 ms,  KRTT: 0 ms
        p23 = re.compile(r'^SRTT: *(?P<srtt_round_trips>\d+) ms, *'
                         r'(RTTO: *(?P<rtto_round_trips>\d+) ms)?, *'
                         r'(RTV: *(?P<rtv_round_trips>\d+) ms)?, *'
                         r'(KRTT: *(?P<krtt_round_trips>\d+) ms)?$')

        # minRTT: 2 ms,  maxRTT: 213 ms
        p24 = re.compile(r'^minRTT: *(?P<minrtt_round_trips>\d+) ms,? *'
                         r'(maxRTT: *(?P<maxrtt_round_trips>\d+) ms)?$')

        # ACK hold time: 200 ms, Keepalive time: 0 sec, SYN waittime: 30 sec
        p25 = re.compile(r'^ACK hold time: *(?P<ack_holdtime_ms>\d+) ms,? *'
                         r'(Keepalive time: *(?P<keepalive_time_sec>\d+) sec)?,? *'
                         r'(SYN waittime: *(?P<syn_waittime_sec>\d+) sec)?$')

        # Giveup time: 0 ms, Retransmission retries: 0, Retransmit forever: FALSE
        p26 = re.compile(r'^Giveup time: *(?P<giveup_time_ms>\d+) ms,? *'
                         r'(Retransmission retries: *(?P<retransmission_retries>\d+))?,? *'
                         r'(Retransmit forever: *(?P<retransmit_forever>\S+))?$')

        # Connect retries remaining: 0, connect retry interval: 0 secs
        p27 = re.compile(r'^Connect retries remaining: *(?P<connect_retries_remaining>\d+)'
                         r',? *(connect retry interval: *(?P<connect_retry_interval>\d+) secs)?$')

        # State flags: none
        p28 = re.compile(r'^State flags: *(?P<states_flags>.+)$')

        # Feature flags: Win Scale, Nagle
        p29 = re.compile(r'^Feature flags: *(?P<feature_flags>.+)$')

        # Request flags: Win Scale
        p30 = re.compile(r'^Request flags: *(?P<request_flags>.+)$')

        # Datagrams (in bytes): MSS 1440, peer MSS 1440, min MSS 1440, max MSS 1440
        p31 = re.compile(r'^Datagrams *(\(in bytes\))?: *(MSS *(?P<mss>\d+))?,? *'
                         r'(peer MSS *(?P<peer_mss>\d+))?,? *'
                         r'(min MSS *(?P<min_mss>\d+))?,? *'
                         r'(max MSS *(?P<max_mss>\d+))?$')

        # Window scales: rcv 0, snd 0, request rcv 0, request snd 0
        p32 = re.compile(r'^Window scales: *(rcv *(?P<rcv>\d+))?,? *'
                         r'(snd *(?P<snd>\d+))?,? *'
                         r'(request rcv *(?P<request_rcv>\d+))?,? *'
                         r'(request snd *(?P<request_snd>\d+))?$')

        # Timestamp option: recent 0, recent age 0, last ACK sent 0
        p33 = re.compile(r'^Timestamp option: *(recent *(?P<recent>\d+))?,? *'
                         r'(recent age *(?P<recent_age>\d+))?,? *'
                         r'(last ACK sent *(?P<last_ACK_sent>\d+))?$')

        # Sack blocks {start, end}: none
        # Sack blocks {start, end}: 100/200
        p34 = re.compile(r'^Sack blocks {start, end}: *(?P<blocks_start_end>(\d+\/\d+|\w+))$')

        # Sack holes {start, end, dups, rxmit}: none
        p35 = re.compile(r'^Sack holes {start, end, dups, rxmit}: *(?P<holes_start_end>.+)$')

        # Socket options: SO_REUSEADDR, SO_REUSEPORT, SO_NBIO
        p36 = re.compile(r'^Socket options: *(?P<socket_options>.+)$')

        # Socket states: SS_ISCONNECTED, SS_PRIV
        p37 = re.compile(r'^Socket states: *(?P<socket_states>.+)$')

        # Socket receive buffer states: SB_DEL_WAKEUP
        p38 = re.compile(r'^Socket receive buffer states: *(?P<receive_buffer_states>.+)$')

        # Socket send buffer states: SB_DEL_WAKEUP
        p39 = re.compile(r'^Socket send buffer states: *(?P<send_buffer_states>.+)$')

        # Socket receive buffer: Low/High watermark 1/32768
        p40 = re.compile(r'^Socket receive buffer: *(Low\/High watermark *(?P<receive_buffer>\S+))?$')

        # Socket send buffer   : Low/High watermark 2048/24576, Notify threshold 0
        p41 = re.compile(r'^Socket send buffer +: '
                         r'(Low\/High watermark *(?P<send_low_high_watermark>\d+\/\d+))?,? *'
                         r'(Notify threshold *(?P<send_notify_threshold>\d+))?$')

        # Socket misc info     : Rcv data size (sb_cc) 0, so_qlen 0,
        p42 = re.compile(r'^Socket misc info +: *(Rcv data size \(sb_cc\) *'
                         r'(?P<rcv_data_size>\d+))?(,? *'
                         r'(so_qlen *(?P<misc_so_qlen>\d+))?)?,?$')

        #           so_q0len 0, so_qlimit 0, so_error 0
        p43 = re.compile(r'so_q0len *(?P<so_q0len>\d+),? *'
                         r'(so_qlimit *(?P<so_qlimit>\d+))?,? *'
                         r'(so_error *(?P<so_error>\d+))?$')

        #            so_auto_rearm 1
        p44 = re.compile(r'so_auto_rearm *(?P<so_auto_rearm>\d+)$')

        # PDU information:
        p45 = re.compile(r'^PDU information:$')

        #  #PDU's in buffer: 0
        p46 = re.compile(r'#?PDU\'s in buffer: *(?P<pdu_in_buffer>\d+)$')

        # FIB Lookup Cache:  IFH: 0x1000058  PD ctx: size: 8  data: 0x0 0xa6fe66ce
        p47 = re.compile(r'^FIB Lookup Cache: *'
                         r'(IFH: *(?P<fib_ifh>\S+))? *'
                         r'(PD ctx: size: *(?P<pd_ctx_size>\d+))? *'
                         r'(data: *(?P<pd_ctx_data>.+))?$')

        # Num Labels: 0  Label Stack: 0
        p48 = re.compile(r'^Num Labels: *(?P<num_label>\d+) *(Label Stack:)?$')

        # Num of peers with authentication info: 0
        p49 = re.compile(r'^Num of peers with authentication info: *(?P<num_peer_with_auth>\d+)$')

        pcb_key = None
        current_queue = None
        current_queue_receive = None
        event_timer = None
        sequences = None
        times = None
        flags = None
        pud_info = None
        tcp_conn_data = None
        socket_misc_info = None

        for line in out.splitlines():
            line = line.strip()

            if not line:
                continue

            # Connection state is ESTAB, I/O status: 0, socket status: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['connection_state']:
                    temp_data.setdefault('connection_state', group['connection_state'])

                if group['io_status']:
                    temp_data.setdefault('io_status', int(group['io_status']))

                if group['socket_status']:
                    temp_data.setdefault('socket_status', int(group['socket_status']))

                continue

            # Established at Mon Jul 12 09:44:25 2021
            m = p2.match(line)
            if m:
                group = m.groupdict()
                temp_data.setdefault('established_datetime', group['established_datetime'])

                continue

            # PCB 0x00007f553800d8f8, SO 0x7f5538008698, TCPCB 0x7f5538008b58, vrfid 0x60000000,
            m = p3.match(line)
            if m:
                group = m.groupdict()
                top_key = ret_dict.setdefault('pcb_address', {})
                pcb_key = top_key.setdefault(group['pcb'], {})
                pcb_key.setdefault('connection_state', temp_data['connection_state'])
                pcb_key.setdefault('io_status', temp_data['io_status'])
                pcb_key.setdefault('socket_status', temp_data['socket_status'])
                pcb_key.setdefault('established_datetime', temp_data['established_datetime'])

                tcp_conn_data = pcb_key.setdefault('tcp_connection_data', {})
                tcp_conn_data['pcb'] = group['pcb']

                if group['so']:
                    tcp_conn_data.setdefault('so', group['so'])

                if group['tcpcb']:
                    tcp_conn_data.setdefault('tcpcb', group['tcpcb'])

                if group['vrfid']:
                    tcp_conn_data.setdefault('vrfid', group['vrfid'])

                temp_data.clear()

                continue

            # Pak Prio: Medium, TOS: 192, TTL: 1, Hash index: 26
            m = p4.match(line)
            if m:
                group = m.groupdict()
                tcp_conn_data = pcb_key.setdefault('tcp_connection_data', {})

                if group['pak_prio']:
                    tcp_conn_data.setdefault('pak_prio', group['pak_prio'])

                if group['tos']:
                    tcp_conn_data.setdefault('tos', int(group['tos']))

                if group['ttl']:
                    tcp_conn_data.setdefault('ttl', int(group['ttl']))

                if group['hash_index']:
                    tcp_conn_data.setdefault('hash_index', int(group['hash_index']))

                continue

            # Local host: 2000:108:10::1, Local port: 179 (Local App PID: 11298)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                tcp_conn_data = pcb_key.setdefault('tcp_connection_data', {})

                if group['local_host']:
                    tcp_conn_data['local_host'] = group['local_host']

                if group['local_port']:
                    tcp_conn_data['local_port'] = int(group['local_port'])

                if group['local_app_pid']:
                    tcp_conn_data['local_app_pid'] = int(group['local_app_pid'])

                continue

            # Foreign host: 2000:108:10::2, Foreign port: 56357
            m = p6.match(line)
            if m:
                group = m.groupdict()
                tcp_conn_data = pcb_key.setdefault('tcp_connection_data', {})

                if group['foreign_host']:
                    tcp_conn_data['foreign_host'] = group['foreign_host']

                if group['foreign_port']:
                    tcp_conn_data['foreign_port'] = int(group['foreign_port'])

                continue

            # (Local App PID/instance/SPL_APP_ID: 11298/1/0)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                local_app = tcp_conn_data.setdefault('local_app', {})
                if '/' in group['local_instance_spl']:
                    lis_data = group['local_instance_spl'].split('/')

                    local_app.setdefault('pid', int(lis_data[0]))

                    if lis_data[1]:
                        local_app.setdefault('instance', int(lis_data[1]))

                    if lis_data[2]:
                        local_app.setdefault('spl_id', int(lis_data[2]))

                continue

            # Current send queue size in bytes: 0 (max 24576)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                current_queue = pcb_key.setdefault('current_queue', {})
                current_queue_send = current_queue.setdefault('send', {})

                current_queue_send.setdefault('send_size_bytes', int(group['send_queue_size_bytes']))

                if group['send_max_bytes']:
                    current_queue_send.setdefault('max_send_size_bytes', int(group['send_max_bytes']))

                continue

            # Current receive queue size in bytes: 0 (max 32768)  mis-ordered: 0 bytes
            m = p9.match(line)
            if m:
                group = m.groupdict()
                current_queue_receive = current_queue.setdefault('receive', {})

                current_queue_receive.setdefault('receive_size_bytes', int(group['receive_queue_size_bytes']))

                if group['receive_max_bytes']:
                    current_queue_receive.setdefault('max_receive_size_bytes', int(group['receive_max_bytes']))

                if group['receive_mis_ordered_bytes']:
                    current_queue_receive.setdefault('mis_ordered_bytes', int(group['receive_mis_ordered_bytes']))

                continue

            # Current receive queue size in packets: 0 (max 0)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                current_queue_receive.setdefault('receive_size_packages', int(group['receive_queue_packages']))

                if group['receive_max_packages']:
                    current_queue_receive.setdefault('max_receive_size_packages', int(group['receive_max_packages']))

                continue

            # Timer          Starts    Wakeups         Next(msec)
            m = p11.match(line)
            if m:
                event_timer = pcb_key.setdefault('event_timers', {})

                continue

            # Retrans             3          0                0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                retruns = event_timer.setdefault('retrans', {})

                if group['retrans_starts']:
                    retruns['starts'] = int(group['retrans_starts'])

                if group['retrans_wakeups']:
                    retruns['wakeups'] = int(group['retrans_wakeups'])

                if group['retrans_next_msec']:
                    retruns['next_msec'] = int(group['retrans_next_msec'])

                continue

            # SendWnd             0          0                0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                sendwnd = event_timer.setdefault('sendWnd', {})

                if group['sendwnd_starts']:
                    sendwnd['starts'] = int(group['sendwnd_starts'])

                if group['sendwnd_wakeups']:
                    sendwnd['wakeups'] = int(group['sendwnd_wakeups'])

                if group['sendwnd_next_msec']:
                    sendwnd['next_msec'] = int(group['sendwnd_next_msec'])

                continue

            # timewait             0          0                0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                timewait = event_timer.setdefault('timewait', {})

                if group['timewait_starts']:
                    timewait['starts'] = int(group['timewait_starts'])

                if group['timewait_wakeups']:
                    timewait['wakeups'] = int(group['timewait_wakeups'])

                if group['timewait_next_msec']:
                    timewait['next_msec'] = int(group['timewait_next_msec'])

                continue

            # AckHold             4          3                0
            m = p15.match(line)
            if m:

                group = m.groupdict()
                ackhold = event_timer.setdefault('ackhold', {})

                if group['ackhold_starts']:
                    ackhold['starts'] = int(group['ackhold_starts'])

                if group['ackhold_wakeups']:
                    ackhold['wakeups'] = int(group['ackhold_wakeups'])

                if group['ackhold_next_msec']:
                    ackhold['next_msec'] = int(group['ackhold_next_msec'])

                continue

            # keepalive             1          0                0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                keepalive = event_timer.setdefault('keepalive', {})

                if group['keepalive_starts']:
                    keepalive['starts'] = int(group['keepalive_starts'])

                if group['keepalive_wakeups']:
                    keepalive['wakeups'] = int(group['keepalive_wakeups'])

                if group['keepalive_next_msec']:
                    keepalive['next_msec'] = int(group['keepalive_next_msec'])

                continue

            # pmtuager             0          0                0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                pmtuager = event_timer.setdefault('pmtuager', {})

                if group['pmtuager_starts']:
                    pmtuager['starts'] = int(group['pmtuager_starts'])

                if group['pmtuager_wakeups']:
                    pmtuager['wakeups'] = int(group['pmtuager_wakeups'])

                if group['pmtuager_next_msec']:
                    pmtuager['next_msec'] = int(group['pmtuager_next_msec'])

                continue

            # giveup             1          0                0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                giveup = event_timer.setdefault('giveup', {})

                if group['giveup_starts']:
                    giveup['starts'] = int(group['giveup_starts'])

                if group['giveup_wakeups']:
                    giveup['wakeups'] = int(group['giveup_wakeups'])

                if group['giveup_next_msec']:
                    giveup['next_msec'] = int(group['giveup_next_msec'])

                continue

            # throttle             1          0                0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                giveup = event_timer.setdefault('throttle', {})

                if group['throttle_starts']:
                    giveup['starts'] = int(group['throttle_starts'])

                if group['throttle_wakeups']:
                    giveup['wakeups'] = int(group['throttle_wakeups'])

                if group['throttle_next_msec']:
                    giveup['next_msec'] = int(group['throttle_next_msec'])

                continue

            # iss: 1042166212  snduna: 1042166346  sndnxt: 1042166346
            m = p20.match(line)
            if m:
                sequences = pcb_key.setdefault('sequences', {})
                group = m.groupdict()

                if group['iss_sequence']:
                    sequences['iss'] = int(group['iss_sequence'])

                if group['snduna_sequence']:
                    sequences['snduna'] = int(group['snduna_sequence'])

                if group['sndnxt_sequence']:
                    sequences['sndnxt'] = int(group['sndnxt_sequence'])

                continue

            # sndmax: 1042166346  sndwnd: 32739       sndcwnd: 2880
            m = p21.match(line)
            if m:
                group = m.groupdict()

                if group['sndmax_sequence']:
                    sequences['sndmax'] = int(group['sndmax_sequence'])

                if group['sndwnd_sequence']:
                    sequences['sndwnd'] = int(group['sndwnd_sequence'])

                if group['sndcwnd_sequence']:
                    sequences['sndcwnd'] = int(group['sndcwnd_sequence'])

                continue

            # irs: 309426134   rcvnxt: 309426287   rcvwnd: 32701   rcvadv: 309458988
            m = p22.match(line)
            if m:
                group = m.groupdict()

                if group['irs_sequence']:
                    sequences['irs'] = int(group['irs_sequence'])

                if group['rcvnxt_sequence']:
                    sequences['rcvnxt'] = int(group['rcvnxt_sequence'])

                if group['rcvwnd_sequence']:
                    sequences['rcvwnd'] = int(group['rcvwnd_sequence'])

                if group['rcvadv_sequence']:
                    sequences['rcvadv'] = int(group['rcvadv_sequence'])

                continue

            # SRTT: 28 ms,  RTTO: 300 ms,  RTV: 214 ms,  KRTT: 0 ms
            m = p23.match(line)
            if m:
                group = m.groupdict()
                round_trip_delay = pcb_key.setdefault('round_trip_delay', {})

                if group['srtt_round_trips']:
                    round_trip_delay['srtt_ms'] = int(group['srtt_round_trips'])

                if group['rtto_round_trips']:
                    round_trip_delay['rtto_ms'] = int(group['rtto_round_trips'])

                if group['rtv_round_trips']:
                    round_trip_delay['rtv_ms'] = int(group['rtv_round_trips'])

                if group['krtt_round_trips']:
                    round_trip_delay['krtt_ms'] = int(group['krtt_round_trips'])

                continue

            # minRTT: 2 ms,  maxRTT: 213 ms
            m = p24.match(line)
            if m:
                group = m.groupdict()
                round_trip_delay = pcb_key.setdefault('round_trip_delay', {})

                if group['minrtt_round_trips']:
                    round_trip_delay['min_rtt_ms'] = int(group['minrtt_round_trips'])

                if group['maxrtt_round_trips']:
                    round_trip_delay['max_rtt_ms'] = int(group['maxrtt_round_trips'])

                continue

            # ACK hold time: 200 ms, Keepalive time: 0 sec, SYN waittime: 30 sec
            m = p25.match(line)
            if m:
                group = m.groupdict()
                times = pcb_key.setdefault('times', {})

                if group['ack_holdtime_ms']:
                    times['ack_hold_ms'] = int(group['ack_holdtime_ms'])

                if group['keepalive_time_sec']:
                    times['keepalive_sec'] = int(group['keepalive_time_sec'])

                if group['syn_waittime_sec']:
                    times['syn_waittime_sec'] = int(group['syn_waittime_sec'])

                continue

            # Giveup time: 0 ms, Retransmission retries: 0, Retransmit forever: FALSE
            m = p26.match(line)
            if m:

                group = m.groupdict()
                times = pcb_key.setdefault('times', {})

                if group['giveup_time_ms']:
                    times['giveup_ms'] = int(group['giveup_time_ms'])

                if group['retransmission_retries']:
                    times['retransmission_retries'] = int(group['retransmission_retries'])

                if group['retransmit_forever']:
                    times['retransmit_forever'] = group['retransmit_forever']

                continue

            # Connect retries remaining: 0, connect retry interval: 0 secs
            m = p27.match(line)
            if m:
                group = m.groupdict()

                if group['connect_retries_remaining']:
                    times['connect_retries_remaining'] = int(group['connect_retries_remaining'])

                if group['connect_retry_interval']:
                    times['connect_retry_interval_sec'] = int(group['connect_retry_interval'])

                continue

            # State flags: none
            m = p28.match(line)
            if m:
                group = m.groupdict()
                flags = pcb_key.setdefault('flags', {})

                flags['state'] = group['states_flags']

                continue

            # Feature flags: Win Scale, Nagle
            m = p29.match(line)
            if m:
                group = m.groupdict()

                flags['feature'] = group['feature_flags']

                continue

            # Request flags: Win Scale
            m = p30.match(line)
            if m:
                group = m.groupdict()
                flags['request'] = group['request_flags']

                continue

            # Datagrams (in bytes): MSS 1440, peer MSS 1440, min MSS 1440, max MSS 1440
            m = p31.match(line)
            if m:
                group = m.groupdict()
                datagrams = pcb_key.setdefault('datagrams', {})

                if group['mss']:
                    datagrams['mss_bytes'] = int(group['mss'])

                if group['peer_mss']:
                    datagrams['peer_mss_bytes'] = int(group['peer_mss'])

                if group['min_mss']:
                    datagrams['min_mss_bytes'] = int(group['min_mss'])

                if group['max_mss']:
                    datagrams['max_mss_bytes'] = int(group['max_mss'])

                continue

            # Window scales: rcv 0, snd 0, request rcv 0, request snd 0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                window_scales = pcb_key.setdefault('window_scales', {})

                if group['rcv']:
                    window_scales['rcv'] = int(group['rcv'])

                if group['snd']:
                    window_scales['snd'] = int(group['snd'])

                if group['request_rcv']:
                    window_scales['request_rcv'] = int(group['request_rcv'])

                if group['request_snd']:
                    window_scales['request_snd'] = int(group['request_snd'])

                continue

            # Timestamp option: recent 0, recent age 0, last ACK sent 0
            m = p33.match(line)
            if m:
                group = m.groupdict()
                timestamp_option = pcb_key.setdefault('timestamp_option', {})

                if group['recent']:
                    timestamp_option['recent'] = int(group['recent'])

                if group['recent_age']:
                    timestamp_option['recent_age'] = int(group['recent_age'])

                if group['last_ACK_sent']:
                    timestamp_option['last_ack_sent'] = int(group['last_ACK_sent'])

                continue

            # Sack blocks {start, end}: none
            # Sack blocks {start, end}: 100/200
            m = p34.match(line)
            if m:
                group = m.groupdict()
                sack_blocks = pcb_key.setdefault('sack_blocks', {})

                if '/' not in group['blocks_start_end']:
                    sack_blocks['start'] = group['blocks_start_end']
                    sack_blocks['end'] = group['blocks_start_end']
                else:
                    star_end = group['blocks_start_end'].split('/', 1)
                    sack_blocks['start'] = star_end[0]
                    sack_blocks['end'] = star_end[1]

                continue

            # Sack holes {start, end, dups, rxmit}: none
            # Sack holes {start, end}: 100/200/300/400
            m = p35.match(line)
            if m:
                group = m.groupdict()
                sack_holes = pcb_key.setdefault('sack_holes', {})

                if '/' not in group['holes_start_end']:
                    sack_holes['start'] = group['holes_start_end']
                    sack_holes['end'] = group['holes_start_end']
                    sack_holes['dups'] = group['holes_start_end']
                    sack_holes['rxmit'] = group['holes_start_end']
                else:
                    sack_holes_data = group['holes_start_end'].split('/')
                    sack_holes['start'] = sack_holes_data[0]
                    sack_holes.setdefault('end', sack_holes_data[1])
                    sack_holes.setdefault('dups', sack_holes_data[2])
                    sack_holes.setdefault('rxmit', sack_holes_data[4])

                continue

            # Socket options: SO_REUSEADDR, SO_REUSEPORT, SO_NBIO
            m = p36.match(line)
            if m:
                group = m.groupdict()
                pcb_key.setdefault('socket_options', group['socket_options'])

                continue

            # Socket states: SS_ISCONNECTED, SS_PRIV
            m = p37.match(line)
            if m:
                group = m.groupdict()
                pcb_key.setdefault('socket_states', group['socket_states'])

                continue

            # Socket receive buffer states: SB_DEL_WAKEUP
            m = p38.match(line)
            if m:
                group = m.groupdict()
                pcb_key.setdefault('socket_receive_buffer_states', group['receive_buffer_states'])

                continue

            # Socket send buffer states: SB_DEL_WAKEUP
            m = p39.match(line)
            if m:
                group = m.groupdict()
                pcb_key.setdefault('socket_send_buffer_states', group['send_buffer_states'])

                continue

            # Socket receive buffer: Low/High watermark 1/32768
            m = p40.match(line)
            if m:
                group = m.groupdict()
                socket_receive_buffer = pcb_key.setdefault('socket_receive_buffer', {})
                receive_watermark = socket_receive_buffer.setdefault('watermarks', {})

                receive_watermark_data = group['receive_buffer'].split('/')
                receive_watermark['low'] = int(receive_watermark_data[0])
                receive_watermark['high'] = int(receive_watermark_data[1])

                continue

            # Socket send buffer   : Low/High watermark 2048/24576, Notify threshold 0
            m = p41.match(line)
            if m:
                group = m.groupdict()
                socket_send_buffer = pcb_key.setdefault('socket_send_buffer', {})
                send_watermark = socket_send_buffer.setdefault('watermarks', {})

                send_watermark_data = group['send_low_high_watermark'].split('/')
                send_watermark['low'] = int(send_watermark_data[0])
                send_watermark['high'] = int(send_watermark_data[1])

                if group['send_notify_threshold']:
                    socket_send_buffer['notify_threshold'] = int(group['send_notify_threshold'])

                continue

            # Socket misc info     : Rcv data size (sb_cc) 0, so_qlen 0,
            m = p42.match(line)
            if m:
                group = m.groupdict()
                socket_misc_info = pcb_key.setdefault('socket_misc_info', {})

                if group['rcv_data_size']:
                    socket_misc_info['rcv_data_size'] = int(group['rcv_data_size'])

                if group['misc_so_qlen']:
                    socket_misc_info['so_qlen'] = int(group['misc_so_qlen'])

                continue

            #          so_q0len 0, so_qlimit 0, so_error 0
            m = p43.match(line)
            if m:
                group = m.groupdict()

                if group['so_q0len']:
                    socket_misc_info['so_q0len'] = int(group['so_q0len'])

                if group['so_qlimit']:
                    socket_misc_info['so_qlimit'] = int(group['so_qlimit'])

                if group['so_error']:
                    socket_misc_info['so_error'] = int(group['so_error'])

                continue

            #               so_auto_rearm 1
            m = p44.match(line)
            if m:
                group = m.groupdict()

                if group['so_auto_rearm']:
                    socket_misc_info['so_auto_rearm'] = int(group['so_auto_rearm'])

                continue

            # PDU information:
            m = p45.match(line)
            if m:
                pud_info = pcb_key.setdefault('pdu_information', {})

                continue

            #     #PDU's in buffer: 0
            m = p46.match(line)
            if m:
                group = m.groupdict()
                pud_info.setdefault('pdu_buffer', int(group['pdu_in_buffer']))

                continue

            # FIB Lookup Cache:  IFH: 0x1000058  PD ctx: size: 8  data: 0x0 0xa6fe66ce
            m = p47.match(line)
            if m:
                group = m.groupdict()
                fib_cache = pud_info.setdefault('fib_lookup_cache', {})

                if group['fib_ifh']:
                    fib_cache['ifh'] = group['fib_ifh']

                if group['pd_ctx_size'] or group['pd_ctx_data']:
                    pd_ctx = fib_cache.setdefault('pd_ctx', {})
                    pd_ctx['size'] = int(group['pd_ctx_size'])
                    pd_ctx['data'] = group['pd_ctx_data']

                continue

            #   Num Labels: 0  Label Stack: 0
            m = p48.match(line)
            if m:
                group = m.groupdict()
                pud_info['num_label'] = int(group['num_label'])

                continue

            #   Num of peers with authentication info: 0
            m = p49.match(line)
            if m:
                group = m.groupdict()
                pud_info['num_peers_with_authentication'] = int(group['num_peer_with_auth'])

                continue

        return ret_dict
