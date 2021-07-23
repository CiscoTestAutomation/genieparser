"""show_tcp.py

IOSXR parser for the following show command:
    * 'show tcp detail pcb all '
"""
import re
import genie.parsergen as pg

# import parser utils
from genie.libs.parser.utils.common import Common

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any


# =======================================
# Schema for 'show tcp detail pcb all'
# =======================================
class ShowTcpDetailPcbAllSchema(MetaParser):
    """Schema for show tcp detail pcb all

    """

    schema = {
        Any(): {
            'connection_state': str,
            'io_state': str,
            'socket_state': int,
            'established_datetime': str,
            'tcp_connection_data': {
                'PCB': str,
                'SO': str,
                'TCPCB': str,
                'VRFID': str,
                'pak_prio': str,
                'TOS': int,
                'TTL': int,
                'Hash_index': int,
                'local_host': str,
                'local_port': int,
                'local_app_pid': int,
                'foreign_host': str,
                'foreign_port': int,
                'local_api': {
                    'PID': int,
                    'Instance': int,
                    'SPL_ID': int,
                }
            },
            'current_queue': {
                'send': {
                    'send_size_bytes': int,
                    'max_send_size_bytes': int
                },
                'receive': {
                    'receive_size_bytes': int,
                    'max_receive_size_bytes': int,
                    'mis_ordered_bytes': int,
                    'receive_size_packages': int,
                },
                'event_timers': {
                    'retrans': {
                        'starts': int,
                        'wakeups': int,
                        'next_msec': int
                    },
                    'sendWnd': {
                        'starts': int,
                        'wakeups': int,
                        'next_msec': int
                    },
                    'timewait': {
                        'starts': int,
                        'wakeups': int,
                        'next_msec': int
                    },
                    'ackhold': {
                        'starts': int,
                        'wakeups': int,
                        'next_msec': int
                    },
                    'keepalive': {
                        'starts': int,
                        'wakeups': int,
                        'next_msec': int
                    },
                    'pmtuager': {
                        'starts': int,
                        'wakeups': int,
                        'next_msec': int
                    },
                    'giveup': {
                        'starts': int,
                        'wakeups': int,
                        'next_msec': int
                    },
                    'throttle': {
                        'starts': int,
                        'wakeups': int,
                        'next_msec': int
                    }
                },
                'sequence_numbers': {
                    'iss': int,
                    'snduna': int,
                    'sndnxt': int,
                    'sndmax': int,
                    'sndwnd': int,
                    'sndcwnd': int,
                    'irs': int,
                    'rcvnxt': int,
                    'rcvwnd': int,
                    'rcvadv': int,
                },
                'round_trip_delay': {
                    'SRTT_ms': int,
                    'RTTO_ms': int,
                    'RTV_ms': int,
                    'KRTT_ms': int,
                    'minRTT_ms': int,
                    'maxRTT_ms': int
                },
                'times': {
                    'ACK_hold_ms': int,
                    'Keepalive_sec': int,
                    'SYN_waittime_sec': int,
                    'Giveup_ms': int,
                    'Retransmission_retries': int,
                    'Retransmit_forever': bool,
                    'Connect_retries_remaining': int,
                    'connect_retry_interval_sec': int
                },
                'flags': {
                    'State': str,
                    'Feature': str,
                    'Request': str,
                },
                'Datagrams': {
                    'MSS_bytes': int,
                    'peer_MSS_bytes': int,
                    'min_MSS_bytes': int,
                    'max_MSS_bytes': int
                },
                'Window_Scales': {
                    'RCV': int,
                    'SND': int,
                    'Request_RCV': int,
                    'Request_SND': int
                },
                'Timestamp_option': {
                    'recent': int,
                    'recent_age': int,
                    'last_ACK_sent': int
                },
                'Sack_Blocks': {
                    'start': int,
                    'end': int
                },
                'Sack_Holes': {
                    'start': int,
                    'end': int,
                    'dups': int,
                    'rxmit': int,
                },
                'Socket_options': {
                    'SO_ACCEPTCONN': bool,
                    'SO_REUSEADDR': bool,
                    'SO_REUSEPORT': bool,
                    'SO_NBIO': bool
                },
                'Socket_States': {
                    'SS_NOFDREF': bool,
                    'SS_ISCONNECTED': bool,
                    'SS_ISDISCONNECTING': bool,
                    'SS_CANTSENDMORE': bool,
                    'SS_CANTRCVMORE': bool,
                    'SS_PRIV': bool
                },
                'Socket_Receive-Buffer_States': {
                    'SB_SEL': bool,
                    'SB_DEL_WAKEUP': bool,
                    'SB_CWAKEUP': bool
                },
                'Socket_Send_Buffer_States': {
                    'SB_DEL_WAKEUP': bool,
                    'SB_WAKEUP': bool
                },
                'Socket_Receive_Buffer': {
                    'watermarks': {
                        'low': int,
                        'high': int
                    },
                    'notify_threshold': int
                },
                'Socket_Misc_Info': {
                    'RCV_data_size': int,
                    'SO_QLen': int,
                    'SO_Q0Len': int,
                    'SO_QLimit': int,
                    'SO_Error': int,
                    'SO_Auto_Rearm': int
                },
                'PDU_Information': {
                    'PDU_Buffer': int,
                    'FIB_Lookup_Cache': {
                        'IFH': str,
                        'PD_CTX': {
                            'Size': int,
                            'Data': str
                        },
                        'Num_Labels': int,
                        'Label_Stack': {
                            'Num_Peers_With_Authentication': int
                        }

                    }
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

        # ==============================================================
        p0 = re.compile(r'^=+')

        # Connection state is ESTAB, I/O status: 0, socket status: 0
        p1 = re.compile(r'^Connection state is (?P<connection_state>\S+),'
                       r' ?(I\/O status: (?P<io_status>\d+))?,'
                       r' ?(socket status: ?(?P<socket_status>\d+))?$')

        # Established at Mon Jul 12 09:44:25 2021
        p2 = re.compile(r'^Established at (?P<established_datetime>.+)$')

        # PCB 0x00007f553800d8f8, SO 0x7f5538008698, TCPCB 0x7f5538008b58, vrfid 0x60000000,
        p3 = re.compile(r'^(PCB (?P<pcb>\w+)?,)? ?'
                        r'((SO (?P<so>\w+))?,)? ?'
                        r'((TCPCB (?P<tcpcb>\w+))?,)? ?'
                        r'((vrfid (?P<vrfid>\w+))?,)?$')

        # Pak Prio: Medium, TOS: 192, TTL: 1, Hash index: 26
        p4 = re.compile(r'^(Pak Prio: (?P<pak_prio>\w+),)? '
                        r'(TOS: (?P<tos>\d+),)? '
                        r'(TTL: (?P<ttl>\d+),)? '
                        r'(Hash index: (?P<hash_index>\d+))?$')

        # Local host: 2000:108:10::1, Local port: 179 (Local App PID: 11298)
        p5 = re.compile(r'^(Local host: (?P<local_host>\S+),)? '
                        r'(Local port: (?P<local_port>\d+))? '
                        r'(\(Local App PID: (?P<local_app_pid>\d+)\))?$')

        # Foreign host: 2000:108:10::2, Foreign port: 56357
        p6 = re.compile(r'^(Foreign host: (?P<foreign_host>\S+),)? '
                        r'(Foreign port: (?P<foreign_port>\d+))?$')

        # (Local App PID/instance/SPL_APP_ID: 11298/1/0)
        p7 = re.compile(r'^(\(Local App PID\/instance\/SPL_APP_ID: (?P<local_instance_spl>\S+)\))?$')

        # Current send queue size in bytes: 0 (max 24576)
        p8 = re.compile(r'^Current send queue size in bytes: (?P<send_queue_size_bytes>\d+)'
                        r' ?(\(max (?P<send_max_bytes>\d+)\))?$')

        # Current receive queue size in bytes: 0 (max 32768)  mis-ordered: 0 bytes
        p9 = re.compile(r'^Current receive queue size in bytes: (?P<receive_queue_size_bytes>\d+) ?'
                        r'(\(max (?P<receive_max_bytes>\d+)\))?( +)?'
                        r'(mis-ordered: ?(?P<receive_mis_ordered_bytes>\d+) ? bytes)?$')

        # Current receive queue size in packets: 0 (max 0)
        p10 = re.compile(r'^Current receive queue size in packets: (?P<receive_queue_packages>\d+) ?'
                        r'(\(max (?P<receive_max_packages>\d+)\))?$')

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
        p20 = re.compile(r'^( +)?(iss: (?P<iss_sequence>\d+))?( +)?'
                        r'(snduna: (?P<snduna_sequence>\d+))?( +)?'
                        r'(sndnxt: (?P<sndnxt_sequence>\d+))?$')

        #    sndmax: 1042166346  sndwnd: 32739       sndcwnd: 2880
        p21 = re.compile(r'^( +)?(sndmax: (?P<sndmax_sequence>\d+))?( +)?'
                        r'(sndwnd: (?P<sndwnd_sequence>\d+))?( +)?'
                        r'(sndcwnd: (?P<sndcwnd_sequence>\d+))?$')

        #    irs: 309426134   rcvnxt: 309426287   rcvwnd: 32701   rcvadv: 309458988
        p22 = re.compile(r'^( +)?(irs: (?P<irs_sequence>\d+))?( +)?'
                        r'(rcvnxt: (?P<rcvnxt_sequence>\d+))?( +)?'
                        r'(rcvwnd: (?P<rcvwnd_sequence>\d+))?( +)?'
                        r'(rcvadv: (?P<rcvadv_sequence>\d+))?$')

        # SRTT: 28 ms,  RTTO: 300 ms,  RTV: 214 ms,  KRTT: 0 ms
        p23 = re.compile(r'^(SRTT: (?P<srtt_round_trips>\d+) ms)?,( +)?'
                        r'(RTTO: (?P<rtto_round_trips>\d+) ms)?,( +)?'
                        r'(RTV: (?P<rtv_round_trips>\d+) ms)?,( +)?'
                        r'(KRTT: (?P<krtt_round_trips>\d+) ms)?$')

        # minRTT: 2 ms,  maxRTT: 213 ms
        p24 = re.compile(r'^(minRTT: (?P<minrtt_round_trips>\d+) ms)?,?( +)?'
                        r'(maxRTT: (?P<maxrtt_round_trips>\d+) ms)?$')

        # ACK hold time: 200 ms, Keepalive time: 0 sec, SYN waittime: 30 sec
        p25 = re.compile(r'^(ACK hold time: (?P<ack_holdtime_ms>\d+) ms)?,?( +)?'
                        r'(Keepalive time: (?P<keepalive_time_sec>\d+) sec)?,?( +)?'
                        r'(SYN waittime: (?P<syn_waittime_sec>\d+) sec)?$')

        # Giveup time: 0 ms, Retransmission retries: 0, Retransmit forever: FALSE
        p26 = re.compile(r'^(Giveup time: (?P<giveup_time_ms>\d+) ms)?,?( +)?'
                        r'(Retransmission retries: (?P<retransmission_retries>\d+))?,?( +)?'
                        r'(Retransmit forever: (?P<retransmit_forever>\S+))?$')

        # Connect retries remaining: 0, connect retry interval: 0 secs
        p27 = re.compile(r'^(Connect retries remaining: (?P<connect_retries_remaining>\d+))?'
                        r',?( +)?(connect retry interval: (?P<connect_retry_interval>\d+) secs)?$')

        # State flags: none
        p28 = re.compile(r'^State flags: (?P<states_flags>.+)$')

        # Feature flags: Win Scale, Nagle
        p29 = re.compile(r'^Feature flags: (?P<feature_flags>.+)$')

        # Request flags: Win Scale
        p30 = re.compile(r'^Request flags: (?P<request_flags>.+)$')

        # Datagrams (in bytes): MSS 1440, peer MSS 1440, min MSS 1440, max MSS 1440
        p31 = re.compile(r'^Datagrams (\(in bytes\))?: (MSS (?P<mss>\d+))?,? ?'
                        r'(peer MSS (?P<peer_mss>\d+))?,? ?'
                        r'(min MSS (?P<min_mss>\d+))?,? ?'
                        r'(max MSS (?P<max_mss>\d+))?$')

        # Window scales: rcv 0, snd 0, request rcv 0, request snd 0
        p32 = re.compile(r'^Window scales: (rcv (?P<rcv>\d+))?,? ?'
                        r'(snd (?P<snd>\d+))?,? ?'
                        r'(request rcv (?P<request_rcv>\d+))?,? ?'
                        r'(request snd (?P<request_snd>\d+))?$')

        # Timestamp option: recent 0, recent age 0, last ACK sent 0
        p33 = re.compile(r'^Timestamp option: (recent (?P<recent>\d+))?,? ?'
                        r'(recent age (?P<recent_age>\d+))?,? ?'
                        r'(last ACK sent (?P<last_ACK_sent>\d+))?$')

        # Sack blocks {start, end}: none
        # Sack blocks {start, end}: 100/200
        p34 = re.compile(r'^Sack blocks {start, end}: (?P<blocks_start_end>(\d+\/\d+|\.+))$')

        # Sack holes {start, end, dups, rxmit}: none
        p35 = re.compile(r'^Sack holes {start, end, dups, rxmit}: (?P<holes_start_end>\.+)$')

        # Socket options: SO_REUSEADDR, SO_REUSEPORT, SO_NBIO
        p36 = re.compile(r'^Socket options: ((?P<so_reuseaddr>\w+))?,? ?'
                        r'((?P<so_reuseport>\w+))?,? ?'
                        r'(?P<so_nbio>\w+),? ?')

        # Socket states: SS_ISCONNECTED, SS_PRIV
        p37 = re.compile(r'^Socket states: ((?P<ss_isconnected>\w+))?,? ?'
                        r'((?P<ss_priv>\w+))?$')

        # Socket receive buffer states: SB_DEL_WAKEUP
        p38 = re.compile(r'^Socket receive buffer states: ((?P<receive_buffer_states>\w+))?$')

        # Socket send buffer states: SB_DEL_WAKEUP
        p39 = re.compile(r'^Socket send buffer states: ((?P<send_buffer_states>\w+))?$')

        # Socket receive buffer: Low/High watermark 1/32768
        p40 = re.compile(r'^Socket receive buffer: (Low\/High watermark (?P<receive_buffer>\S+))?$')

        # Socket send buffer   : Low/High watermark 2048/24576, Notify threshold 0
        p41 = re.compile(r'^Socket send buffer +: '
                        r'(Low\/High watermark (?P<send_low_high_watermark>\S+))?,? ?'
                        r'(Notify threshold (?P<send_notify_threshold>\d+))?$')

        # Socket misc info     : Rcv data size (sb_cc) 0, so_qlen 0,
        p42 = re.compile(r'^Socket misc info +: (Rcv data size \(sb_cc\) '
                        r'(?P<rcv_data_size>\d+))?,? ?'
                        r'(so_qlen (?P<misc_so_qlen>\d+))?$')

        #           so_q0len 0, so_qlimit 0, so_error 0
        p43 = re.compile(r'^ +(so_q0len (?P<so_q0len>\d+))?,? ?'
                        r'(so_qlimit (?P<so_qlimit>\d+))?,? ?'
                        r'(so_error (?P<so_error>\d+))?$')

        #            so_auto_rearm 1
        p44 = re.compile(r'^ +(so_auto_rearm (?P<so_auto_rearm>\d+))$')

        # PDU information:
        p45 = re.compile(r'^PDU information:$')

        #  #PDU's in buffer: 0
        p46 = re.compile(r'^ +#?PDU\'s in buffer: (?P<pdu_in_buffer>\d+)$')

        # FIB Lookup Cache:  IFH: 0x1000058  PD ctx: size: 8  data: 0x0 0xa6fe66ce
        p47 = re.compile(r'^FIB Lookup Cache:( +)?'
                        r'(IFH: (?P<fib_ifh>\S+))?( +)?'
                        r'(PD ctx: size: (?P<pd_ctx_size>\d+))?( +)?'
                        r'(data: (?P<pd_ctx_data>.+))?$')

        # Num Labels: 0  Label Stack: 0
        p48 = re.compile(r'^( +)?(Num Labels: (?P<num_label>\d+))?( +)?(Label Stack: (?P<lable_stack>\d+))?$')

        # Num of peers with authentication info: 0
        p49 = re.compile(r'^( +)?(Num of peers with authentication info: (?P<num_peer_with_auth>\d+))?')

        for cur_line in out.splitlines():
            cur_line = cur_line.strip()

            # * con0/RP0/CPU0   admin   hardware     0  00:00:00
            m = p.match(cur_line)


            if m:
                if 'line' not in ret_dict:
                    user_dict = ret_dict.setdefault('line', {})
                active = m.groupdict()['active']
                line = m.groupdict()['line']
                user = m.groupdict()['user']
                service = m.groupdict()['service']
                conns = m.groupdict()['conns']
                idle = m.groupdict()['idle']
                location = m.groupdict()['location']

                # declare line dictionary inside root dictionary
                user_dict[line] = {}

                # check if line is active and set boolean feild
                user_dict[line]['active'] = True if active == '*' else False
                user_dict[line]['user'] = user
                user_dict[line]['service'] = service
                user_dict[line]['conns'] = conns
                user_dict[line]['idle'] = idle

                # check if location is not empty and set
                if location:
                    user_dict[line]['location'] = location.strip()
                continue
        return ret_dict
