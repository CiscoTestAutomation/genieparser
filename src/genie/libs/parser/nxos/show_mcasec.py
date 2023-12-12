'''show_macsec.py

NXOS parsers for the following show commands:
    * show macsec mka summary
    * show macsec mka session
    * show macsec mka session interface {interface} details
    * show macsec mka session interface {interface} 
    * show macsec mka session details    
    * show macsec mka statistics
'''

# python
import re
# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common

# =========================================
# Schema for 'show macsec mka summary'
# =========================================

class ShowMacSecMkaSummarySchema(MetaParser):
    """Schema for
        * show macsec mka summary
    """

    schema = {
        Any(): {
            Optional("status"): str,
            Optional("cipher_suite"): str,
            Optional("key_server"): str,
            Optional("macsec_policy"): str,
            Optional("keychain"): str,
            Optional("fallback_keychain"): str,
        },
        Optional("macsec_shutdown"): bool,
    }

# =====================================
# Parser for 'show macsec mka summary'
# ======================================

class ShowMacSecMkaSummary(ShowMacSecMkaSummarySchema):
    """Parser for 
        show macsec mka summary
    """

    cli_command = ['show macsec mka summary']

    def cli(self,output=None):
        if output is None:
           cmd = self.cli_command[0]
           output = self.device.execute(cmd)

        p0 = re.compile(r'Macsec is shutdown')
        
        #Interface          Status   Cipher (Operational)   Key-Server   MACSEC-policy                    Keychain                         Fallback-keychain
        #Ethernet1/1        Secured  GCM-AES-XPN-256        Yes          mp1                              kc1                              no keychain
        #Ethernet1/9/1      Init      No Cipher             Yes         Test-MP1                          Test-KC1                         no keychain

        p1 = re.compile(r'(?P<interface>[E|e]thernet[0-9/]+)\s+'
            r'(?P<status>[Secured|Init|Pending|down]+)\s+'
            r'(?P<cipher_suite>GCM-AES-128|GCM-AES-256|CM-AES-XPN-128|GCM-AES-XPN-256|No Cipher|-)\s+'
            r'(?P<key_server>Yes|No|-)\s+(?P<macsec_policy>\S+)\s+'
            r'(?P<keychain>\S+)\s+(?P<fallback_keychain>([\S\s]*))$')
        macSecMkaSummaryDict = {}
        
        for line in output.splitlines():
            line = line.strip()

            m0 = p0.match(line)
            if m0:
                #in case of macsec feature shutdown, no other details exist in cli output
                # return dict with 'macsec_shutdown set to True
                macSecMkaSummaryDict['macsec_shutdown'] = True 
                return macSecMkaSummaryDict
                
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                mka_summary_dict = macSecMkaSummaryDict.setdefault(interface, {})

                mka_summary_dict['status']=group['status']
                mka_summary_dict['cipher_suite']=group['cipher_suite']
                mka_summary_dict['key_server']=group['key_server']
                mka_summary_dict['macsec_policy']=group['macsec_policy']
                mka_summary_dict['keychain']=group['keychain']
                mka_summary_dict['fallback_keychain']=group['fallback_keychain']
        return macSecMkaSummaryDict

# =========================================
# Schema for 'show macsec mka session'
# =========================================
class ShowMacSecMkaSessionSchema(MetaParser):
    """Schema for 
    * show macsec mka session
    * show macsec mka session interface {interface} 
    """

    schema = {
        Any(): {
            Optional("local_txSci"): str,
            Optional("peers"): str,
            Optional("status"): str,
            Optional("key_server"): str,
            Optional("auth_mode"): str,
        },
        Optional("macsec_shutdown"): bool,
        Optional("total_sessions"): int, 
        Optional("secured_sessions"): int,
        Optional("pending_sessions"): int,
    }

# =====================================
# Parser for 'show macsec mka session'
# ======================================


class ShowMacSecMkaSession(ShowMacSecMkaSessionSchema):
    """Parser for 
       
        * show macsec mka session
        * show macsec mka session interface {interface} 
    
    """
    cli_command = ['show macsec mka session', 'show macsec mka session interface {interface}']

    def cli(self,interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        p0 = re.compile(r'Macsec is shutdown')
        #Ethernet1/1        6026.aa7e.0302/0001              1                  Secured            Yes                PRIMARY-PSK
        p1 = re.compile(r'(?P<interface>\S+)\s+'
            r'(?P<local_txSci>\S+)\s+'
            r'(?P<peers>([\d]+))\s+'
            r'(?P<status>([a-zA-Z]+))\s+'
            r'(?P<key_server>([a-zA-Z]+))\s+'
            r'(?P<auth_mode>\S+)$')

        # Total Number of Sessions : 28
        # Secured Sessions : 21
        # Pending Sessions : 7
        p2 = re.compile(r'Total Number of Sessions\s+:\s+(?P<total_sessions>\d+)')
        p3 = re.compile(r'Secured Sessions\s+:\s+(?P<secured_sessions>\d+)')
        p4 = re.compile(r'Pending Sessions\s+:\s+(?P<pending_sessions>\d+)')

        macSecMkaSessionDict={}
        for line in output.splitlines():
            line = line.strip()
            
            m0 = p0.match(line) 
            if m0:
                #in case of macsec feature shutdown, no other details exist in cli output
                # return dict with 'macsec_shutdown set to True
                macSecMkaSessionDict['macsec_shutdown'] = True 
                return macSecMkaSessionDict
        
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                interface = group['interface']
                if interface not in macSecMkaSessionDict:
                    mka_session_dict = macSecMkaSessionDict.setdefault(interface, {})
                
                if group['local_txSci']:
                    mka_session_dict['local_txSci']=group['local_txSci']

                if group['peers']:
                    mka_session_dict['peers']=group['peers']

                if group['status']:
                    mka_session_dict['status']=group['status']

                if group['key_server']:
                    mka_session_dict['key_server']=group['key_server']

                if group['auth_mode']:
                    mka_session_dict['auth_mode']=group['auth_mode']

                continue 
            
            m2  = p2.match(line) 
            if m2:
                group = m2.groupdict()
                macSecMkaSessionDict.update({'total_sessions' : int(group['total_sessions'])})
                continue
            
            m3  = p3.match(line) 
            if m3:
                group = m3.groupdict()
                macSecMkaSessionDict.update({'secured_sessions' : int(group['secured_sessions'])})
                continue
            
            m4  = p4.match(line) 
            if m4:
                group = m4.groupdict()
                macSecMkaSessionDict.update({'pending_sessions' : int(group['pending_sessions'])})
            
        return macSecMkaSessionDict


# =========================================
# Schema for 'show macsec mka session details'
# =========================================


class ShowMacSecMkaSessionSchemaDetails(MetaParser):
    """Schema for 
        * show macsec mka session interface {interface} details
        * show macsec mka session details    
    """

    schema = {
        Any(): {
            Any(): {
                Optional("status"): str,
                Optional("local_txSci"): str,
                Optional("local_txSsci"): str,
                Optional("mka_port_identifier"): str,
                Optional("cak_name"): str,
                Optional("ca_auth_mode"): str,
                Optional("member_intentifier"): str,
                Optional("message_num"): str,
                Optional("mka_policy_name"): str,
                Optional("key_server_prio"): str,
                Optional("key_server"): str,
                Optional("include_icv"): str,
                Optional("sak_cipher_suite"): str,
                Optional("sak_cipher_suite_oper"): str,
                Optional("replay_window_size"): str,
                Optional("conf_offset"): str,
                Optional("conf_offset_oper"): str,
                Optional("latest_sak_status"): str,
                Optional("latest_sak_an"): str,
                Optional("latest_sak_ki"): str,
                Optional("latest_sak_kn"): str,
                Optional("last_sak_key_time"): str,
                Optional("ca_peer_cnt"): str,
                Optional("eapol_dst_mac"): str,
                Optional("ether_type"): str,
                Optional("peer_status"): {
                    Optional("peer_mi"): str,
                    Optional("rx_sci"): str,
                    Optional("peer_cak"): str,
                    Optional("latest_rx_mkpdu"): str,
                },
            },
        },
        Optional('macsec_shutdown'): bool
    }

# =====================================
# Parser for 'show macsec mka session'
# ======================================

class ShowMacSecMkaSessionDetails(ShowMacSecMkaSessionSchemaDetails):
    """Parser for    
        * show macsec mka session interface {interface} details
        * show macsec mka session details    
    
    """
    cli_command = ['show macsec mka session details', 'show macsec mka session interface {interface} details']

    def cli(self,interface="", output=None):

        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
                output = self.device.execute(cmd)
            else:
                cmd = self.cli_command[0]
                output = self.device.execute(cmd)

        # -----------------------------------
        # Macsec is shutdown
        # -----------------------------------
        p0 = re.compile(r'Macsec is shutdown')
        
        #Interface Name          : Ethernet1/1
        p1 =  re.compile(r'^Interface +Name\s+\:\s+(?P<interface>\S+)')

        #Session Status                      : SECURED - Secured MKA Session with MACsec
        p2 =  re.compile(r'^Session +Status\s+\:\s+(?P<status>(.*))')

        #Local Tx-SCI                        : 6026.aa7e.0302/0001
        p3 =  re.compile(r'^Local +Tx-SCI\s+\:\s+(?P<local_txSci>\S+)')

        #Local Tx-SSCI                       : 1
        p4 =  re.compile(r'^Local +Tx-SSCI\s+\:\s+(?P<local_txSsci>\S+)')

        #MKA Port Identifier                 : 1
        p5 =  re.compile(r'^MKA +Port +Identifier\s+\:\s+(?P<mka_port_identi>\S+)')

        #CAK Name (CKN)                      : 12
        p6 =  re.compile(r'^CAK +Name +\(CKN\)\s+\:\s+(?P<cak_name>\S+)')

        #CA Authentication Mode              : PRIMARY-PSK
        p7 =  re.compile(r'^CA +Authentication +Mode\s+\:\s+(?P<ca_auth_mode>\S+)')

        #Member Identifier (MI)              : 48456637DBF545CA72654999
        p8 =  re.compile(r'^Member +Identifier +\(MI\)\s+\:\s+(?P<member_intenti>\S+)')

        #Message Number (MN)                 : 171474
        p9 =  re.compile(r'^Message +Number +\(MN\)\s+\:\s+(?P<message_num>\S+)')

        #MKA Policy Name                     : mp1
        p10 =  re.compile(r'^MKA +Policy +Name\s+\:\s+(?P<mka_policy_name>\S+)')

        #Key Server Priority                 : 0
        p11 =  re.compile(r'^Key +Server +Priority\s+\:\s+(?P<key_server_prio>\S+)')

        #Key Server                          : Yes
        p12 =  re.compile(r'^Key +Server\s+\:\s+(?P<key_server>\S+)')

        #Include ICV                         : Yes
        p13 =  re.compile(r'^Include +ICV\s+\:\s+(?P<include_icv>\S+)')

        #SAK Cipher Suite                    : GCM-AES-XPN-256
        p14 =  re.compile(r'^SAK +Cipher +Suite\s+\:\s+(?P<sak_cipher_suite_cfg>\S+)')

        #SAK Cipher Suite (Operational)      : GCM-AES-XPN-256
        p15 =  re.compile(r'^SAK +Cipher +Suite +\(Operational\)\s+\:\s+(?P<sak_cipher_suite_oper>\S+)')

        #Replay Window Size                  : 15000
        p16 =  re.compile(r'^Replay +Window +Size\s+\:\s+(?P<replay_window_size>\S+)')

        #Confidentiality Offset              : CONF-OFFSET-50
        p17 =  re.compile(r'^Confidentiality +Offset +\s+\:\s+(?P<conf_offset_cfg>\S+)')

        #Confidentiality Offset (Operational): CONF-OFFSET-50
        p18 =  re.compile(r'^Confidentiality +Offset +\(Operational\)\s+\:\s+(?P<conf_offset_oper>\S+)')

        #Latest SAK Status                   : Rx & TX
        p19 =  re.compile(r'^Latest +SAK +Status\s+\:\s+(?P<latest_sak_status>\S+\s+\S+\s+\S+)')

        #Latest SAK AN                       : 0
        p20 =  re.compile(r'^Latest +SAK +AN\s+\:\s+(?P<latest_sak_an>\S+)')

        #Latest SAK KI                       : 48456637DBF545CA7265499900000001
        p21 =  re.compile(r'^Latest +SAK +KI\s+\:\s+(?P<latest_sak_ki>\S+)')

        #Latest SAK KN                       : 1
        p22 =  re.compile(r'^Latest +SAK +KN\s+\:\s+(?P<latest_sak_kn>\S+)')

        #Last SAK key time                   : 13:45:55 PDT Thu Oct 13 2022
        p23 =  re.compile(r'^Last SAK key time\s+\:\s+(?P<last_sak_key_time>([0-9\:]+\s+[A-Z]+\s+[A-Za-z]+\s+[A-Za-z]+\s+\d+\s\d+))')

        #CA Peer Count                       : 1
        p24 =  re.compile(r'^CA +Peer +Count\s+\:\s+(?P<ca_peer_cnt>\S+)')

        #Eapol dest mac                      : 0180.c200.0003
        p25 =  re.compile(r'^Eapol +dest +mac\s+\:\s+(?P<eapol_dst_mac>\S+)')

        #Ether-type                          : 0x888e
        p26 =  re.compile(r'^Ether-type\s+\:\s+(?P<ether_type>\S+)')

        #Peer Status:
        p27 =  re.compile(r'^Peer +\Status:')

        #Peer MI                             : 3007D03EFE2933B1EAD94639
        p28 =  re.compile(r'^Peer +MI\s+\:\s+(?P<peer_mi>\S+)')

        #RxSCI                               : 3c13.cc55.e506/0001
        p29 =  re.compile(r'^RxSCI\s+\:\s+(?P<rx_sci>\S+)')

        #Peer CAK                            : Match
        p30 =  re.compile(r'^Peer +CAK\s+\:\s+(?P<peer_cak>\S+)')

        #Latest Rx MKPDU                     : 13:06:06 PDT Mon Oct 17 2022
        p31 =  re.compile(r'^Latest +Rx +MKPDU\s+\:\s+(?P<latest_rx_mkpdu>([0-9\:]+\s+[A-Z]+\s+[A-Za-z]+\s+[A-Za-z]+\s+\d+\s\d+))')

        macSecMkaSessionDict={}
        count = 0
        for line in output.splitlines():
            line = line.strip()
            
            m0 = p0.match(line)
            if m0:
                #in case of macsec feature shutdown, no other details exist in cli output
                # return dict with 'macsec_shutdown set to True
                macSecMkaSessionDict['macsec_shutdown'] = True 
                return macSecMkaSessionDict
                
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                interface = group['interface']
                count += 1
                mka_session_detail = macSecMkaSessionDict.setdefault(count, {})
                mka_session_detail_dict = mka_session_detail.setdefault(interface, {})
                
                continue
            
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                mka_session_detail_dict['status']=group['status']
                continue

            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                mka_session_detail_dict['local_txSci']=group['local_txSci']
                continue

            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                mka_session_detail_dict['local_txSsci']=group['local_txSsci']
                continue

            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                mka_session_detail_dict['mka_port_identifier']=group['mka_port_identi']
                continue

            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                mka_session_detail_dict['cak_name']=group['cak_name']
                continue

            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                mka_session_detail_dict['ca_auth_mode']=group['ca_auth_mode']
                continue

            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                mka_session_detail_dict['member_intentifier']=group['member_intenti']
                continue

            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                mka_session_detail_dict['message_num']=group['message_num']
                continue

            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                mka_session_detail_dict['mka_policy_name']=group['mka_policy_name']
                continue

            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                mka_session_detail_dict['key_server_prio']=group['key_server_prio']
                continue

            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                mka_session_detail_dict['key_server']=group['key_server']
                continue

            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                mka_session_detail_dict['include_icv']=group['include_icv']
                continue

            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                mka_session_detail_dict['sak_cipher_suite']=group['sak_cipher_suite_cfg']
                continue

            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                mka_session_detail_dict['sak_cipher_suite_oper']=group['sak_cipher_suite_oper']
                continue

            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                mka_session_detail_dict['replay_window_size']=group['replay_window_size']
                continue

            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                mka_session_detail_dict['conf_offset']=group['conf_offset_cfg']
                continue

            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                mka_session_detail_dict['conf_offset_oper']=group['conf_offset_oper']
                continue

            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                mka_session_detail_dict['latest_sak_status']=group['latest_sak_status']
                continue

            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                mka_session_detail_dict['latest_sak_an']=group['latest_sak_an']
                continue

            m21 = p21.match(line)
            if m21:
                group = m21.groupdict()
                mka_session_detail_dict['latest_sak_ki']=group['latest_sak_ki']
                continue

            m22 = p22.match(line)
            if m22:
                group = m22.groupdict()
                mka_session_detail_dict['latest_sak_kn']=group['latest_sak_kn']
                continue

            m23 = p23.match(line)
            if m23:
                group = m23.groupdict()
                mka_session_detail_dict['last_sak_key_time']=group['last_sak_key_time']
                continue

            m24 = p24.match(line)
            if m24:
                group = m24.groupdict()
                mka_session_detail_dict['ca_peer_cnt']=group['ca_peer_cnt']
                continue

            m25 = p25.match(line)
            if m25:
                group = m25.groupdict()
                mka_session_detail_dict['eapol_dst_mac']=group['eapol_dst_mac']
                continue

            m26 = p26.match(line)
            if m26:
                group = m26.groupdict()
                mka_session_detail_dict['ether_type']=group['ether_type']
                continue

            m27 = p27.match(line)
            if m27:
                mka_session_detail_dict['peer_status']={}
                continue

            m28 = p28.match(line)
            if m28:
                group = m28.groupdict()
                mka_session_detail_dict['peer_status']['peer_mi']=group['peer_mi']
                continue

            m29 = p29.match(line)
            if m29:
                group = m29.groupdict()
                mka_session_detail_dict['peer_status']['rx_sci']=group['rx_sci']
                continue

            m30 = p30.match(line)
            if m30:
                group = m30.groupdict()
                mka_session_detail_dict['peer_status']['peer_cak']=group['peer_cak']
                continue

            m31 = p31.match(line)
            if m31:
                group = m31.groupdict()
                mka_session_detail_dict['peer_status']['latest_rx_mkpdu']=group['latest_rx_mkpdu']
                continue
        
        return macSecMkaSessionDict


# =========================================
# Schema for 'show macsec mka statistics'
# =========================================

class ShowMacSecMkaStatsSchema(MetaParser):
    """Schema for 
        show macsec mka statistics 
    
    """

    schema = {
        Optional("mka_global_stats"): {
            Optional("mka_session_events"): {
                 Optional("secured_events"): int,
                 Optional("del_secured_events"): int,
                 Optional("keepalive_timeout_events"): int,
            },
            Optional("ca_statistics"): {
                 Optional("pairwise_cak_rekeys"): int,
            },
            Optional("sa_statistics"): {
                 Optional("saks_generated"): int,
                 Optional("saks_rekeyed"): int,
                 Optional("saks_recieved"): int,
                 Optional("sak_response_recieved"): int,
            },
            Optional("mkpdu_statistics"): {
                 Optional("mkpdu_valid_rx"): int,
                 Optional("mkpdu_rx_distributed_sak"): int,
                 Optional("mkpdus_tx"): int,
                 Optional("mkpdu_tx_distributed_sak"): int,
            },
        },
        Optional("mka_error_cnt_total"): {
            Optional("session_failures"): {
                Optional("bringup_failures"): int,
            },
            Optional("sak_failures"): {
                Optional("sak_gen"): int,
                Optional("hash_key_gen"): int,
                Optional("sack_ecrypt_wrap"): int,
                Optional("sack_decrypt_unwrap"): int,
                Optional("sack_cipher_mismatch"): int,
            },
            Optional("ca_failures"): {
                Optional("ick_derivation"): int,
                Optional("kek_derivation"):  int,
                Optional("invalid_peer_macsec_capab"): int,
            },
            Optional("macsec_failures"): {
                Optional("rx_sa_install"): int,
                Optional("tx_sa_install"): int,
            },
            Optional("mkpdu_failures"): {
                Optional("mkpdu_tx"): int,
                Optional("mkpdu_rx_bad_peer_mn"): int,
                Optional("mkpdu_rx_no_recent_peerlist_mn"): int,
                Optional("mkpdu_rxdrop_sakuse_kn_mismatch"): int,
                Optional("mkpdu_rxdrop_sakuse_rx_notset"): int,
                Optional("mkpdu_rxdrop_sakuse_key_mi_mismatch"): int,
                Optional("mkpdu_rxdrop_sakuse_an_not_inuse"): int,
                Optional("mkpdu_rxdrop_sakuse_ks_rxtx_notset"): int,
            },
            Optional("global_stats"): {
                Optional("mkpdu_rx_invalid_ckn"): int,
                Optional("mkpdu_tx_pkt_build_fail"): int,
            },
        },
        Optional('macsec_shutdown'): bool
    }

# =============================================
# Parser for 'show macsec mka statistics'
# ==============================================

class ShowMacSecMkaStats(ShowMacSecMkaStatsSchema):
    """Parser for 
        show  macsec mka statistics
    """
    cli_command = ['show macsec mka statistics']

    def cli(self,output=None):
        if output is None:
            cmd = self.cli_command
            output = self.device.execute(cmd)
        

        # -----------------------------------
        # Macsec is shutdown
        # -----------------------------------
        p0 = re.compile(r'Macsec is shutdown')
        
        #MKA Global Statistics
        p1 = re.compile(r'^MKA +Global +Statistics')

        #MKA Session Events:
        p2 =  re.compile(r'^MKA +Session +Events\:')

        #Secured Events............. 51
        p3 =  re.compile(r'^Secured +Events\S+\s+(?P<secured_events>\S+)')

        #Deleted (Secured) Events... 0
        p4 =  re.compile(r'^Deleted +\(Secured\) +Events\S+\s+(?P<del_secured_events>\S+)')

        #Keepalive Timeout Events... 8748926
        p5 = re.compile(r'^Keepalive +Timeout +Events\S+\s+(?P<keepalive_timeout_events>\S+)')

        #CA Statistics
        p6 = re.compile(r'^CA +Statistics')

        #Pairwise CAK Rekeys........ 0
        p7 = re.compile(r'^Pairwise +CAK +Rekeys\S+\s+(?P<pairwise_cak_rekeys>\S+)')

        #SA Statistics
        p8 = re.compile(r'^SA +Statistics')

        #   SAKs Generated............. 85
        p9 = re.compile(r'^SAKs +Generated\S+\s+(?P<saks_generated>\S+)')

        #   SAKs Rekeyed............... 0
        p10 = re.compile(r'^SAKs +Rekeyed\S+\s+(?P<saks_rekeyed>\S+)')

        #   SAKs Received.............. 0
        p11 = re.compile(r'^SAKs +Received\S+\s+(?P<saks_recieved>\S+)')

        #  SAK Responses Received..... 51
        p12 = re.compile(r'^SAK +Responses +Received\S+\s+(?P<sak_response_recieved>\S+)')

        #MKPDU Statistics
        p13 = re.compile(r'^MKPDU +Statistics')

        #   MKPDUs Validated & Rx...... 8748688
        p14 = re.compile(r'^MKPDUs +Validated +& +Rx\S+\s+(?P<mkpdu_valid_rx>\S+)')

        #      "Distributed SAK"..... 0
        p15 = re.compile(r'^\"Distributed +SAK\"\S+\s+(?P<mkpdu_rx_distributed_sak>\S+)')

        #   MKPDUs Transmitted......... 8749133
        p16 = re.compile(r'^MKPDUs +Transmitted\S+\s+(?P<mkpdus_tx>\S+)')

        #      "Distributed SAK"..... 111
        p17 = re.compile(r'^\"Distributed +SAK\"\S+\s+(?P<mkpdu_tx_distributed_sak>\S+)')

        #MKA Error Counter Totals
        p18 = re.compile(r'^MKA +Error +Counter +Totals')

        #Session Failures
        p19 = re.compile(r'^Session +Failures')

        #   Bring-up Failures................ 0
        p20 = re.compile(r'^Bring-up +Failures\S+\s+(?P<bringup_failures>\S+)')

        #SAK Failures
        p21 = re.compile(r'^SAK +Failures')

        #SAK Generation................... 0
        p22 = re.compile(r'^SAK +Generation\S+\s+(?P<sak_gen>\S+)')

        #Hash Key Generation.............. 0
        p23 = re.compile(r'^Hash +Key +Generation\S+\s+(?P<hash_key_gen>\S+)')

        #SAK Encryption/Wrap.............. 0
        p24 = re.compile(r'^SAK +Encryption/Wrap\S+\s+(?P<sack_ecrypt_wrap>\S+)')

        #SAK Decryption/Unwrap............ 0
        p25 = re.compile(r'^SAK +Decryption/Unwrap\S+\s+(?P<sack_decrypt_unwrap>\S+)')

        #SAK Cipher Mismatch.............. 0
        p26 = re.compile(r'^SAK +Cipher +Mismatch\S+\s+(?P<sack_cipher_mismatch>\S+)')

        #CA Failures
        p27 = re.compile(r'^CA +Failures')

        #   ICK Derivation................... 0
        p28 = re.compile(r'^ICK +Derivation\S+\s+(?P<ick_derivation>\S+)')

        #   KEK Derivation................... 0
        p29 = re.compile(r'^KEK +Derivation\S+\s+(?P<kek_derivation>\S+)')

        #   Invalid Peer MACsec Capability... 0
        p30 = re.compile(r'^Invalid +Peer +MACsec +Capability\S+\s+(?P<invalid_peer_macsec_capab>\S+)')

        #MACsec Failures
        p31 = re.compile(r'^MACsec +Failures')

        #    Rx SA Installation............... 0
        p32 = re.compile(r'^Rx +SA +Installation\S+\s+(?P<rx_sa_install>\S+)')

        #Tx SA Installation............... 0
        p33 = re.compile(r'^Tx +SA +Installation\S+\s+(?P<tx_sa_install>\S+)')

        #MKPDU Failures
        p34 = re.compile(r'^MKPDU +Failures')

        #   MKPDU Tx......................... 0
        p35 = re.compile(r'^MKPDU +Tx\S+\s+(?P<mkpdu_tx>\S+)')

        #   MKPDU Rx Validation ..................... 1
        #   MKPDU Rx Validation.............. 202
        p36 = re.compile(r'^MKPDU +Rx +Validation\s+\S+\s+(?P<mkpdu_rx_validation>\S+)')

        #   MKPDU Rx Bad Peer MN............. 0
        p37 = re.compile(r'^MKPDU +Rx +Bad +Peer +MN\S+\s+(?P<mkpdu_rx_bad_peer_mn>\S+)')

        #   MKPDU Rx Non-recent Peerlist MN.. 0
        p38 = re.compile(r'^MKPDU +Rx +Non-recent +Peerlist +MN\S+\s+(?P<mkpdu_rx_no_recent_peerlist_mn>\S+)')

        #   MKPDU Rx Drop SAKUSE, KN mismatch...... 0
        p39 = re.compile(r'^MKPDU +Rx +Drop +SAKUSE, +KN +mismatch\S+\s+(?P<mkpdu_rxdrop_sakuse_kn_mismatch>\S+)')

        #   MKPDU Rx Drop SAKUSE, Rx Not Set....... 0
        p40 = re.compile(r'^MKPDU +Rx +Drop +SAKUSE, +Rx +Not +Set\S+\s+(?P<mkpdu_rxdrop_sakuse_rx_notset>\S+)')

        #   MKPDU Rx Drop SAKUSE, Key MI mismatch.. 0
        p41 = re.compile(r'^MKPDU +Rx +Drop +SAKUSE, +Key +MI +mismatch\S+\s+(?P<mkpdu_rxdrop_sakuse_key_mi_mismatch>\S+)')

        #   MKPDU Rx Drop SAKUSE, AN Not in Use.... 0
        p42 = re.compile(r'^MKPDU +Rx +Drop +SAKUSE, +AN +Not +in +Use\S+\s+(?P<mkpdu_rxdrop_sakuse_an_not_inuse>\S+)')

        #   MKPDU Rx Drop SAKUSE, KS Rx/Tx Not Set. 0
        p43 = re.compile(r'^MKPDU +Rx +Drop +SAKUSE, +KS +Rx/Tx +Not +Set\S+\s+(?P<mkpdu_rxdrop_sakuse_ks_rxtx_notset>\S+)')

        #Global Statistics
        p44 = re.compile(r'^Global +Statistics')

        #MKPDUs Rx Invalid CKN...... 0
        p45 = re.compile(r'^MKPDUs +Rx +Invalid +CKN\S+\s+(?P<mkpdu_rx_invalid_ckn>\S+)')

        #   MKPDUs Tx Pkt Build Fail... 0
        p46 = re.compile(r'^MKPDUs +Tx +Pkt +Build +Fail\S+\s+(?P<mkpdu_tx_pkt_build_fail>\S+)')

        #Per-CA MKA Statistics for Session on interface (Ethernet1/1) with CKN 12
        p47 = re.compile(r'^Per-CA +MKA +Statistics +for +Session +on +interface +\((?P<interface>\S+)\) +with +CKN \d+')

        #MKA Statistics for Session on interface (Ethernet1/1)
        p48 = re.compile(r'^MKA +Statistics +for +Session +on +interface +\((?P<interface>\S+)\)')

        #MKA IDB Statistics
        p49 = re.compile(r'^MKA +IDB +Statistics')

        #  MKPDUs Tx Success.......... 171562
        p50 = re.compile(r'^MKPDUs +Tx +Success\S+\s+(?P<mkpdu_tx_success>\S+)')

        #   MKPDUs Tx Fail............. 0
        p51 = re.compile(r'^MKPDUs +Tx +Fail\S+\s+(?P<mkpdu_tx_fail>\S+)')

        #   MKPDUS Tx Pkt build fail... 0
        p52 = re.compile(r'^MKPDUS +Tx +Pkt +build +fail\S+\s+(?P<mkpdu_tx_build_fail>\S+)')

        #   MKPDUS No Tx on intf down.. 0
        p53 = re.compile(r'^MKPDUS +No +Tx +on +intf +down\S+\s+(?P<mkpdu_no_tx_on_intf_down>\S+)')

        #   MKPDUS No Rx on intf down.. 0
        p54 = re.compile(r'^MKPDUS +No +Rx +on +intf +down\S+\s+(?P<mkpdu_no_rx_on_intf_down>\S+)')

        #   MKPDUs Rx CA Not found..... 1
        p55 = re.compile(r'^MKPDUs +Rx +CA +Not +found\S+\s+(?P<mkpdu_rx_ca_not_found>\S+)')

        #   MKPDUs Rx Error............ 0
        p56 = re.compile(r'^MKPDUs +Rx +Error\S+\s+(?P<mkpdu_rx_error>\S+)')

        #   MKPDUs Rx Success.......... 171556
        p57 = re.compile(r'^MKPDUs +Rx +Success\S+\s+(?P<mkpdu_rx_success>\S+)')

        #   MKPDU Rx Drop Packet, Ethertype Mismatch. 0
        p58 = re.compile(r'^MKPDU +Rx +Drop +Packet, +Ethertype +Mismatch\S+\s+(?P<mkpdu_rx_drp_pkt_eth_mismatch>\S+)')

        #  MKPDU Rx Drop Packet, DestMAC Mismatch... 0
        p59 = re.compile(r'^MKPDU +Rx +Drop +Packet, +DestMAC +Mismatch\S+\s+(?P<mkpdu_rx_drp_pkt_dstmac_mismatch>\S+)')

        macSecMkaStatsDict={}
        flag_per_ca_mka_stat = 0
        flag_mka_stat = 0


        for line in output.splitlines():
            line = line.strip()

            m0 = p0.match(line)
            if m0:
                macSecMkaStatsDict['macsec_shutdown'] = True 
                return macSecMkaStatsDict
                
            m = p1.match(line)
            if m:
                global_stats_dict = macSecMkaStatsDict.setdefault('mka_global_stats', {})
                continue 

            m = p2.match(line)
            if m:
                mka_session_events_dict = global_stats_dict.setdefault('mka_session_events', {})
                continue 

            m = p3.match(line)
            if m:
                group = m.groupdict()
                mka_session_events_dict['secured_events']=int(group['secured_events'])

            m = p4.match(line)
            if m:
                group = m.groupdict()
                mka_session_events_dict['del_secured_events']=int(group['del_secured_events'])

            m = p5.match(line)
            if m:
                group = m.groupdict()
                mka_session_events_dict['keepalive_timeout_events']=int(group['keepalive_timeout_events'])

            m = p6.match(line)
            if m:
                if flag_mka_stat:
                    interface_mka_stats = interface_mka_stats.setdefault('ca_statistics', {})
                elif flag_per_ca_mka_stat:
                    interface_ca_stats = interface_per_ca_stats.setdefault('ca_statistics', {})
                else:
                    mka_global_stats = macSecMkaStatsDict.setdefault('mka_global_stats', {})
                    mka_ca_global_stats = mka_global_stats.setdefault('ca_statistics', {})

            m = p7.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mka_stats['pairwise_cak_rekeys'] = int(group['pairwise_cak_rekeys'])
                elif flag_per_ca_mka_stat:
                    interface_ca_stats['pairwise_cak_rekeys'] = int(group['pairwise_cak_rekeys'])
                else:
                    mka_ca_global_stats['pairwise_cak_rekeys'] = int(group['pairwise_cak_rekeys'])

            m = p8.match(line)
            if m:
                if flag_mka_stat:
                    interface_sa_stats = interface_mka_stats.setdefault('sa_statistics', {}) 
                elif flag_per_ca_mka_stat:
                    interface_per_sa_stats = interface_per_ca_stats.setdefault('sa_statistics', {})
                else:
                    mka_global_stats = macSecMkaStatsDict.setdefault('mka_global_stats', {})
                    mka_sa_global_stats = mka_global_stats.setdefault('sa_statistics', {}) 
                
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_sa_stats['saks_generated'] = int(group['saks_generated'])
                elif flag_per_ca_mka_stat:
                    interface_per_sa_stats['saks_generated'] = int(group['saks_generated'])
                else:
                    mka_sa_global_stats['saks_generated'] = int(group['saks_generated'])

            m = p10.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_sa_stats['saks_rekeyed'] = int(group['saks_rekeyed'])
                elif flag_per_ca_mka_stat:
                    interface_per_sa_stats['saks_rekeyed'] = int(group['saks_rekeyed'])
                else:
                    mka_sa_global_stats['saks_rekeyed'] = int(group['saks_rekeyed'])

            m = p11.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_sa_stats['saks_recieved'] = int(group['saks_recieved'])
                elif flag_per_ca_mka_stat:
                    interface_per_sa_stats['saks_recieved'] = int(group['saks_recieved'])
                else:
                    mka_sa_global_stats['saks_recieved'] = int(group['saks_recieved'])

            m = p12.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_sa_stats['sak_response_recieved'] = int(group['sak_response_recieved'])
                elif flag_per_ca_mka_stat:
                    interface_per_sa_stats['sak_response_recieved'] = int(group['sak_response_recieved'])
                else:
                    mka_sa_global_stats['sak_response_recieved'] = int(group['sak_response_recieved'])

            m = p13.match(line)
            if m:
                if flag_mka_stat:
                    interface_mkpdu_stats = interface_mka_stats.setdefault('mkpdu_statistics', {})
                elif flag_per_ca_mka_stat:
                    interface_ca_mkpdu_stats = interface_per_ca_stats('mkpdu_statistics', {})
                else:
                    mka_globals = macSecMkaStatsDict.setdefault('mka_global_stats', {})
                    global_mkpdu_stats = mka_globals.setdefault( 'mkpdu_statistics', {})

            m = p14.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_stats['mkpdu_valid_rx'] = int(group['mkpdu_valid_rx'])
                elif flag_per_ca_mka_stat:
                    interface_ca_mkpdu_stats['mkpdu_valid_rx'] = int(group['mkpdu_valid_rx'])
                else:
                    global_mkpdu_stats['mkpdu_valid_rx'] = int(group['mkpdu_valid_rx'])

            m = p15.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_stats['mkpdu_rx_distributed_sak'] = int(group['mkpdu_rx_distributed_sak'])
                elif flag_per_ca_mka_stat:
                    interface_ca_mkpdu_stats['mkpdu_rx_distributed_sak'] = int(group['mkpdu_rx_distributed_sak'])
                else:
                    global_mkpdu_stats['mkpdu_rx_distributed_sak'] = int(group['mkpdu_rx_distributed_sak'])

            m = p16.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_stats['mkpdus_tx'] = int(group['mkpdus_tx'])
                elif flag_per_ca_mka_stat:
                    interface_ca_mkpdu_stats['mkpdus_tx'] = int(group['mkpdus_tx'])
                else:
                    global_mkpdu_stats['mkpdus_tx'] = int(group['mkpdus_tx'])

            m = p17.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_stats['mkpdu_tx_distributed_sak'] = int(group['mkpdu_tx_distributed_sak'])
                elif flag_per_ca_mka_stat:
                    interface_ca_mkpdu_stats['mkpdu_tx_distributed_sak'] = int(group['mkpdu_tx_distributed_sak'])
                else:
                    global_mkpdu_stats['mkpdu_tx_distributed_sak'] = int(group['mkpdu_tx_distributed_sak'])

            m = p18.match(line)
            if m:
                mka_err_cnt_stats = macSecMkaStatsDict.setdefault('mka_error_cnt_total', {})

            m = p19.match(line)
            if m:
                mka_session_fail_stats = mka_err_cnt_stats.setdefault('session_failures', {})

            m = p20.match(line)
            if m:
                group = m.groupdict()
                mka_session_fail_stats['bringup_failures'] = int(group['bringup_failures'])

            m = p21.match(line)
            if m:
                if flag_mka_stat:
                    interface_sak_fail_stats = interface_mka_stats.setdefault('sak_failures', {})
                else:
                    mka_sak_fail_stats = mka_err_cnt_stats.setdefault('sak_failures', {})

            m = p22.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_sak_fail_stats['sak_gen'] = int(group['sak_gen'])
                else:
                    mka_sak_fail_stats['sak_gen'] = int(group['sak_gen'])

            m = p23.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_sak_fail_stats['hash_key_gen'] = int(group['hash_key_gen'])
                else:
                    mka_sak_fail_stats['hash_key_gen'] = int(group['hash_key_gen'])

            m = p24.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_sak_fail_stats['sack_ecrypt_wrap'] = int(group['sack_ecrypt_wrap'])
                else:
                    mka_sak_fail_stats['sack_ecrypt_wrap'] = int(group['sack_ecrypt_wrap'])

            m = p25.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_sak_fail_stats['sack_decrypt_unwrap'] = int(group['sack_decrypt_unwrap'])
                else:
                    mka_sak_fail_stats['sack_decrypt_unwrap'] = int(group['sack_decrypt_unwrap'])

            m = p26.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_sak_fail_stats['sack_cipher_mismatch'] = int(group['sack_cipher_mismatch'])
                else:
                    mka_sak_fail_stats['sack_cipher_mismatch'] = int(group['sack_cipher_mismatch'])

            m = p27.match(line)
            if m:
                if flag_mka_stat:
                    interface_mka_ca_fail_stats = interface_mka_stats.setdefault('ca_failures', {})
                else:
                    mka_err_ca_fail_stats =  mka_err_cnt_stats.setdefault('ca_failures', {})

            m = p28.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mka_ca_fail_stats['ick_derivation'] = int(group['ick_derivation'])
                else:
                    mka_err_ca_fail_stats['ick_derivation'] = int(group['ick_derivation'])

            m = p29.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mka_ca_fail_stats['kek_derivation'] = int(group['kek_derivation'])
                else:
                    mka_err_ca_fail_stats['kek_derivation'] = int(group['kek_derivation'])

            m = p30.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mka_ca_fail_stats['invalid_peer_macsec_capab'] = int(group['invalid_peer_macsec_capab'])
                else:
                    mka_err_ca_fail_stats['invalid_peer_macsec_capab'] = int(group['invalid_peer_macsec_capab'])

            m = p31.match(line)
            if m:
                if flag_mka_stat:
                    interface_mka_macsec_fail_stats = interface_mka_stats.setdefault('macsec_failures', {})
                else:
                    mka_err_macsec_fail_stats = mka_err_cnt_stats.setdefault('macsec_failures', {})

            m = p32.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mka_macsec_fail_stats['rx_sa_install'] = int(group['rx_sa_install'])
                else:
                    mka_err_macsec_fail_stats['rx_sa_install'] = int(group['rx_sa_install'])

            m = p33.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mka_macsec_fail_stats['tx_sa_install'] = int(group['tx_sa_install'])
                else:
                    mka_err_macsec_fail_stats['tx_sa_install'] = int(group['tx_sa_install'])

            m = p34.match(line)
            if m:
                if flag_mka_stat:
                    interface_mkpdu_fail_stats = interface_mka_stats.setdefault('mkpdu_failures', {})
                else:
                    mka_err_mkpdu_fail_stats = mka_err_cnt_stats.setdefault('mkpdu_failures', {})

            m = p35.match(line)
            if m:
                group = m.groupdict()
                if group['mkpdu_tx']:
                    mka_err_mkpdu_fail_stats['mkpdu_tx'] = int(group['mkpdu_tx'])

            m = p36.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_fail_stats['mkpdu_rx_validation'] = int(group['mkpdu_rx_validation'])
                else:
                    mka_err_mkpdu_fail_stats['mkpdu_rx_validation'] = int(group['mkpdu_rx_validation'])

            m = p37.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_fail_stats['mkpdu_rx_bad_peer_mn'] = int(group['mkpdu_rx_bad_peer_mn'])
                else:
                    mka_err_mkpdu_fail_stats['mkpdu_rx_bad_peer_mn'] = int(group['mkpdu_rx_bad_peer_mn'])

            m = p38.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_fail_stats['mkpdu_rx_no_recent_peerlist_mn'] = int(group['mkpdu_rx_no_recent_peerlist_mn'])
                else:
                    mka_err_mkpdu_fail_stats['mkpdu_rx_no_recent_peerlist_mn'] = int(group['mkpdu_rx_no_recent_peerlist_mn'])

            m = p39.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_fail_stats['mkpdu_rxdrop_sakuse_kn_mismatch'] = int(group['mkpdu_rxdrop_sakuse_kn_mismatch'])
                else:
                    mka_err_mkpdu_fail_stats['mkpdu_rxdrop_sakuse_kn_mismatch'] = int(group['mkpdu_rxdrop_sakuse_kn_mismatch'])

            m = p40.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_fail_stats['mkpdu_rxdrop_sakuse_rx_notset'] = int(group['mkpdu_rxdrop_sakuse_rx_notset'])
                else:
                    mka_err_mkpdu_fail_stats['mkpdu_rxdrop_sakuse_rx_notset'] = int(group['mkpdu_rxdrop_sakuse_rx_notset'])

            m = p41.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_fail_stats['mkpdu_rxdrop_sakuse_key_mi_mismatch'] = int(group['mkpdu_rxdrop_sakuse_key_mi_mismatch'])
                else:
                    mka_err_mkpdu_fail_stats['mkpdu_rxdrop_sakuse_key_mi_mismatch'] = int(group['mkpdu_rxdrop_sakuse_key_mi_mismatch'])

            m = p42.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_fail_stats['mkpdu_rxdrop_sakuse_an_not_inuse'] = int(group['mkpdu_rxdrop_sakuse_an_not_inuse'])
                else:
                    mka_err_mkpdu_fail_stats['mkpdu_rxdrop_sakuse_an_not_inuse'] = int(group['mkpdu_rxdrop_sakuse_an_not_inuse'])

            m = p43.match(line)
            if m:
                group = m.groupdict()
                if flag_mka_stat:
                    interface_mkpdu_fail_stats['mkpdu_rxdrop_sakuse_ks_rxtx_notset'] = int(group['mkpdu_rxdrop_sakuse_ks_rxtx_notset'])
                else:
                    mka_err_mkpdu_fail_stats['mkpdu_rxdrop_sakuse_ks_rxtx_notset'] = int(group['mkpdu_rxdrop_sakuse_ks_rxtx_notset'])


            m = p44.match(line)
            if m:
                mka_err_global_stats = mka_err_cnt_stats.setdefault('global_stats', {})

            m = p45.match(line)
            if m:
                group = m.groupdict()
                mka_err_global_stats['mkpdu_rx_invalid_ckn'] = int(group['mkpdu_rx_invalid_ckn'])

            m = p46.match(line)
            if m:
                group = m.groupdict()
                mka_err_global_stats['mkpdu_tx_pkt_build_fail'] = int(group['mkpdu_tx_pkt_build_fail'])

            m = p47.match(line)
            if m:
                group = m.groupdict()
                interface=group['interface']
                per_ca_mka_stats = macSecMkaStatsDict.setdefault('per_ca_mka_stats', {})
                interface_per_ca_stats = per_ca_mka_stats.setdefault(interface, {})
                flag_per_ca_mka_stat = 1

            m = p48.match(line)
            if m:
                group = m.groupdict()
                interface=group['interface']
                mka_stats = macSecMkaStatsDict.setdefault('mka_stats', {})
                interface_mka_stats = mka_stats.setdefault(interface, {})
                flag_per_ca_mka_stat = 0
                flag_mka_stat = 1

            m = p49.match(line)
            if m:
                #interface_mka_idb_stats = {}
                interface_mka_idb_stats = interface_mka_stats.setdefault('mka_idb_stat', {})

            m = p50.match(line)
            if m:
                group = m.groupdict()
                interface_mka_idb_stats['mkpdu_tx_success'] = int(group['mkpdu_tx_success'])

            m = p51.match(line)
            if m:
                group = m.groupdict()
                interface_mka_idb_stats['mkpdu_tx_fail'] = int(group['mkpdu_tx_fail'])

            m = p52.match(line)
            if m:
                group = m.groupdict()
                interface_mka_idb_stats['mkpdu_tx_build_fail'] = int(group['mkpdu_tx_build_fail'])

            m = p53.match(line)
            if m:
                group = m.groupdict()
                interface_mka_idb_stats['mkpdu_no_tx_on_intf_down'] = int(group['mkpdu_no_tx_on_intf_down'])

            m = p54.match(line)
            if m:
                group = m.groupdict()
                interface_mka_idb_stats['mkpdu_no_rx_on_intf_down'] = int(group['mkpdu_no_rx_on_intf_down'])

            m = p55.match(line)
            if m:
                group = m.groupdict()
                interface_mka_idb_stats['mkpdu_rx_ca_not_found'] = int(group['mkpdu_rx_ca_not_found'])

            m = p56.match(line)
            if m:
                group = m.groupdict()
                interface_mka_idb_stats['mkpdu_rx_error'] = int(group['mkpdu_rx_error'])

            m = p57.match(line)
            if m:
                group = m.groupdict()
                interface_mka_idb_stats['mkpdu_rx_success'] = int(group['mkpdu_rx_success'])

            m = p58.match(line)
            if m:
                group = m.groupdict()
                interface_mkpdu_fail_stats['mkpdu_rx_drp_pkt_eth_mismatch'] = int(group['mkpdu_rx_drp_pkt_eth_mismatch'])

            m = p59.match(line)
            if m:
                group = m.groupdict()
                interface_mkpdu_fail_stats['mkpdu_rx_drp_pkt_dstmac_mismatch'] = int(group['mkpdu_rx_drp_pkt_dstmac_mismatch'])
        return macSecMkaStatsDict

