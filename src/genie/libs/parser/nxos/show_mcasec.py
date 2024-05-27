'''show_macsec.py

NXOS parsers for the following show commands:
    * show macsec mka summary
    * show macsec mka session
    * show macsec mka session interface {interface} details
    * show macsec mka session interface {interface} 
    * show macsec mka session details    
    * show macsec mka statistics
    * show macsec mka statistics interface {interface}
    * show macsec policy
    * show macsec policy {policy}
    * show macsec secy statistics 
    * show macsec secy statistics interface {intf}
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

# ====================================================
# Schema for 'show macsec mka statistics interface <>'
# ====================================================
class ShowMacSecMkaStatsIntfSchema(MetaParser):
    """Schema for 
        show macsec mka statistics interface {interface}
    """

    schema = {
        Any(): {
            "per_ca_mka_stats": {
                "ca_statistics": {
                    "pairwise_cak_rekeys": int,
                },
                "sa_statistics": {
                    "saks_generated": int,
                    "saks_rekeyed": int,
                    "saks_received": int,
                    "sak_response_received": int,
                },
                "mkpdu_statistics": {
                    "mkpdu_valid_rx": int,
                    "mkpdu_rx_distributed_sak": int,
                    "mkpdus_tx": int,
                    "mkpdu_tx_distributed_sak": int,
               },
            },
            "mka_stats": {
                "ca_statistics": {
                    "pairwise_cak_rekeys": int,
                 },
                "sa_statistics": {
                    "saks_generated": int,
                    "saks_rekeyed": int,
                    "saks_received": int,
                    "sak_response_received": int,
                },
                "mkpdu_statistics": {
                    "mkpdus_tx": int,
                    "mkpdu_rx_distributed_sak": int,
                    "mkpdu_tx_distributed_sak": int,
                    "mkpdu_valid_rx": int,
                },
               "mka_idb_stat": {
                    "mkpdu_tx_success": int,
                    "mkpdu_tx_fail": int,
                    "mkpdu_tx_build_fail": int,
                    "mkpdu_no_tx_on_intf_down": int,
                    "mkpdu_no_rx_on_intf_down": int,
                    "mkpdu_rx_ca_not_found": int,
                    "mkpdu_rx_error": int,
                    "mkpdu_rx_success": int,
                },
                "mkpdu_failures": {
                    "mkpdu_rx_validation": int,
                    "mkpdu_rx_bad_peer_mn": int,
                    "mkpdu_rx_no_recent_peerlist_mn": int,
                    "mkpdu_rxdrop_sakuse_kn_mismatch": int,
                    "mkpdu_rxdrop_sakuse_rx_notset": int,
                    "mkpdu_rxdrop_sakuse_key_mi_mismatch": int,
                    "mkpdu_rxdrop_sakuse_an_not_inuse": int,
                    "mkpdu_rxdrop_sakuse_ks_rxtx_notset": int,
                    "mkpdu_rx_drp_pkt_eth_mismatch": int,
                    "mkpdu_rx_drp_pkt_dest_mac_mismatch": int,
                },
                "sak_failures": {
                    "sak_gen": int,
                    "hash_key_gen": int,
                    "sack_ecrypt_wrap": int,
                    "sack_decrypt_unwrap": int,
                },
                "ca_failures": {
                    "ick_derivation": int,
                    "kek_derivation": int,
                    "invalid_peer_macsec_capab": int,
                },
                "macsec_failures": {
                    "rx_sa_install": int,
                    "tx_sa_install": int,
                },
            },
        },
        Optional('macsec_shutdown'): bool
    }

# ====================================================
# Parser for 'show macsec mka statistics interface <>'
# ====================================================

class ShowMacSecMkaStatsIntf(ShowMacSecMkaStatsIntfSchema):
    """Parser for 
        show  macsec mka statistics interface {interface}
    """
    cli_command = ['show macsec mka statistics interface {interface}']

    def cli(self, interface='', output=None):
        
        if output is None:
            cmd = self.cli_command[0].format(interface=interface)
            output = self.device.execute(cmd)
    
        # switch# show macsec mka statistics interface Eth1/1/1
        # -----------------------------------
        # Macsec is shutdown
        # -----------------------------------
        # switch#
        p0 = re.compile(r'^Macsec is shutdown')

        # Per-CA MKA Statistics for Session on interface (Ethernet1/1/1) with CKN 10100000
        p1  = re.compile(r'^Per-CA MKA Statistics for Session on interface \((?P<intf>[Ethernet0-9/]+).*$')

        #MKA Statistics for Session on interface (Ethernet1/25)
        p2 = re.compile(r'^MKA Statistics for Session on interface \([Ethernet0-9/]+\)$')
        #########
        # CA Statistics
        p3 = re.compile(r'^CA +Statistics$')

        # Pairwise CAK Rekeys........ 0
        p4 = re.compile(r'^Pairwise +CAK +Rekeys\S+\s+(?P<pairwise_cak_rekeys>\S+)$')

        #########
        # SA Statistics
        p5 = re.compile(r'^SA +Statistics$')

        #   SAKs Generated............. 85
        p6 = re.compile(r'^SAKs +Generated\S+\s+(?P<saks_generated>\S+)$')

        #   SAKs Rekeyed............... 0
        p7 = re.compile(r'^SAKs +Rekeyed\S+\s+(?P<saks_rekeyed>\S+)$')

        #   SAKs Received.............. 0
        p8 = re.compile(r'^SAKs +Received\S+\s+(?P<saks_received>\S+)$')

        #  SAK Responses Received..... 51
        p9 = re.compile(r'^SAK +Responses +Received\S+\s+(?P<sak_response_received>\S+)$')

        #########
        # MKPDU Statistics
        p10 = re.compile(r'^MKPDU +Statistics$')

        #   MKPDUs Validated & Rx...... 8748688
        p11 = re.compile(r'^MKPDUs +Validated +& +Rx\S+\s+(?P<mkpdu_valid_rx>\S+)$')

        #   MKPDUs Transmitted......... 8749133
        p12 = re.compile(r'^MKPDUs +Transmitted\S+\s+(?P<mkpdus_tx>\S+)$')

        #      "Distributed SAK"..... 111
        p13 = re.compile(r'^\"Distributed +SAK\"\S+\s+(?P<mkpdu_distributed_sak>\S+)$')


        #########
        # MKA IDB Statistics
        p15 = re.compile(r'^MKA +IDB +Statistics$')

        #MKPDUs Tx Success.......... 171562
        p16 = re.compile(r'^MKPDUs +Tx +Success\S+\s+(?P<mkpdu_tx_success>\S+)$')

        # MKPDUs Tx Fail............. 0
        p17 = re.compile(r'^MKPDUs +Tx +Fail\S+\s+(?P<mkpdu_tx_fail>\S+)$')

        #MKPDUS Tx Pkt build fail... 0
        p18 = re.compile(r'^MKPDUS +Tx +Pkt +build +fail\S+\s+(?P<mkpdu_tx_build_fail>\S+)$')

        #MKPDUS No Tx on intf down.. 0
        p19 = re.compile(r'^MKPDUS +No +Tx +on +intf +down\S+\s+(?P<mkpdu_no_tx_on_intf_down>\S+)$')

        #MKPDUS No Rx on intf down.. 0
        p20 = re.compile(r'^MKPDUS +No +Rx +on +intf +down\S+\s+(?P<mkpdu_no_rx_on_intf_down>\S+)$')

        #MKPDUs Rx CA Not found..... 1
        p21 = re.compile(r'^MKPDUs +Rx +CA +Not +found\S+\s+(?P<mkpdu_rx_ca_not_found>\S+)$')

        #MKPDUs Rx Error............ 0
        p22 = re.compile(r'^MKPDUs +Rx +Error\S+\s+(?P<mkpdu_rx_error>\S+)$')

        #MKPDUs Rx Success.......... 171556
        p23 = re.compile(r'^MKPDUs +Rx +Success\S+\s+(?P<mkpdu_rx_success>\S+)$')

        ##########
        # MKPDU Failures
        p24 = re.compile(r'^MKPDU +Failures$')

        #MKPDU Rx Validation.............. 202
        p25 = re.compile(r'^MKPDU +Rx +Validation\s+\S+\s+(?P<mkpdu_rx_validation>\S+)$')

        #MKPDU Rx Bad Peer MN............. 0
        p26 = re.compile(r'^MKPDU +Rx +Bad +Peer +MN\S+\s+(?P<mkpdu_rx_bad_peer_mn>\S+)$')

        #MKPDU Rx Non-recent Peerlist MN.. 0
        p27 = re.compile(r'^MKPDU +Rx +Non-recent +Peerlist +MN\S+\s+(?P<mkpdu_rx_no_recent_peerlist_mn>\S+)$')

        #MKPDU Rx Drop SAKUSE, KN mismatch...... 0
        p28 = re.compile(r'^MKPDU +Rx +Drop +SAKUSE, +KN +mismatch\S+\s+(?P<mkpdu_rxdrop_sakuse_kn_mismatch>\S+)$')

        #MKPDU Rx Drop SAKUSE, Rx Not Set....... 0
        p29 = re.compile(r'^MKPDU +Rx +Drop +SAKUSE, +Rx +Not +Set\S+\s+(?P<mkpdu_rxdrop_sakuse_rx_notset>\S+)$')

        #MKPDU Rx Drop SAKUSE, Key MI mismatch.. 0
        p30 = re.compile(
            r'^MKPDU +Rx +Drop +SAKUSE, +Key +MI +mismatch\S+\s+(?P<mkpdu_rxdrop_sakuse_key_mi_mismatch>\S+)$')

        #MKPDU Rx Drop SAKUSE, AN Not in Use.... 0
        p31 = re.compile(r'^MKPDU +Rx +Drop +SAKUSE, +AN +Not +in +Use\S+\s+(?P<mkpdu_rxdrop_sakuse_an_not_inuse>\S+)$')

        #MKPDU Rx Drop SAKUSE, KS Rx/Tx Not Set. 0
        p32 = re.compile(
        r'^MKPDU +Rx +Drop +SAKUSE, +KS +Rx/Tx +Not +Set\S+\s+(?P<mkpdu_rxdrop_sakuse_ks_rxtx_notset>\S+)$')

        #MKPDU Rx Drop Packet, Ethertype Mismatch. 0
        p33 = re.compile(r'^MKPDU +Rx +Drop +Packet, +Ethertype +Mismatch\S+\s+(?P<mkpdu_rx_drp_pkt_eth_mismatch>\S+)$')

        #MKPDU Rx Drop Packet, DestMAC Mismatch... 0
        p34 = re.compile(r'^MKPDU +Rx +Drop +Packet, +DestMAC +Mismatch\S+\s+(?P<mkpdu_rx_drp_pkt_dest_mac_mismatch>\S+)$')


        ################
        # SAK Failures
        p36 = re.compile(r'^SAK +Failures$')

        # SAK Generation................... 0
        p37 = re.compile(r'^SAK +Generation\S+\s+(?P<sak_gen>\S+)$')

        # Hash Key Generation.............. 0
        p38 = re.compile(r'^Hash +Key +Generation\S+\s+(?P<hash_key_gen>\S+)$')

        # SAK Encryption/Wrap.............. 0
        p39 = re.compile(r'^SAK +Encryption/Wrap\S+\s+(?P<sack_ecrypt_wrap>\S+)$')

        # SAK Decryption/Unwrap............ 0
        p40 = re.compile(r'^SAK +Decryption/Unwrap\S+\s+(?P<sack_decrypt_unwrap>\S+)$')


        ################
        # CA Failures
        p41 = re.compile(r'^CA +Failures$')

        #   ICK Derivation................... 0
        p42 = re.compile(r'^ICK +Derivation\S+\s+(?P<ick_derivation>\S+)$')

        #   KEK Derivation................... 0
        p43 = re.compile(r'^KEK +Derivation\S+\s+(?P<kek_derivation>\S+)$')

        #   Invalid Peer MACsec Capability... 0
        p44 = re.compile(r'^Invalid +Peer +MACsec +Capability\S+\s+(?P<invalid_peer_macsec_capab>\S+)$')

        ###############
        # MACsec Failures
        p45 = re.compile(r'^MACsec +Failures$')

        #    Rx SA Installation............... 0
        p46 = re.compile(r'^Rx +SA +Installation\S+\s+(?P<rx_sa_install>\S+)$')

        # Tx SA Installation............... 0
        p47 = re.compile(r'^Tx +SA +Installation\S+\s+(?P<tx_sa_install>\S+)$')

        macsec_mka_stats_dict = {}
        distributed_rx = False  # Flag to control "Distributed SAK" data is for rx/tx direction
        
        for line in output.splitlines():
            line = line.strip()
            # -----------------------------------
            # Macsec is shutdown
            # -----------------------------------
            m = p0.match(line)
            if m:
                macsec_mka_stats_dict['macsec_shutdown'] = True
                return macsec_mka_stats_dict
            
            # Per-CA MKA Statistics for Session on interface (Ethernet1/1/1) with CKN 10100000  
            m = p1.match(line)
            if m:
                intf_dict = macsec_mka_stats_dict.setdefault(m.group('intf'), {}) 
                target_dict = intf_dict.setdefault('per_ca_mka_stats', {})
                
                continue 
            
            #MKA Statistics for Session on interface (Ethernet1/25)
            m = p2.match(line)
            if m:
                target_dict = intf_dict.setdefault('mka_stats', {})
                
                continue 
            
            # CA Statistics
            m = p3.match(line)
            if m:
                target_ca_dict = target_dict.setdefault('ca_statistics', {})
                continue
            
            # Pairwise CAK Rekeys........ 0
            m = p4.match(line) 
            if m:
                target_ca_dict.update({'pairwise_cak_rekeys' : int(m.group('pairwise_cak_rekeys'))})
                continue 
            
            # SA Statistics
            m = p5.match(line)
            if m:
                target_sa_dict = target_dict.setdefault('sa_statistics', {})
                continue 
            
            #   SAKs Generated............. 85
            m = p6.match(line)
            if m:
                target_sa_dict.update({'saks_generated': int(m.group('saks_generated'))} )
                continue 
            
            #   SAKs Rekeyed............... 0
            m = p7.match(line)
            if m:
                target_sa_dict.update({'saks_rekeyed': int(m.group('saks_rekeyed'))} )
                continue 
            
            #   SAKs Received.............. 0
            m = p8.match(line)
            if m:
                target_sa_dict.update({'saks_received': int(m.group('saks_received'))} )
                continue 
            
            #  SAK Responses Received..... 51
            m = p9.match(line)
            if m:
                target_sa_dict.update({'sak_response_received': int(m.group('sak_response_received'))} )
                continue 
            
            # MKPDU Statistics
            m = p10.match(line)
            if m:
                target_mkpdu_dict = target_dict.setdefault('mkpdu_statistics', {})
                continue 
            
            #   MKPDUs Validated & Rx...... 8748688
            m = p11.match(line)
            if m:
                distributed_rx = True
                target_mkpdu_dict.update({'mkpdu_valid_rx': int(m.group('mkpdu_valid_rx'))} )
                continue 
            
            #   MKPDUs Transmitted......... 8749133
            m = p12.match(line)
            if m:
                distributed_rx = False
                target_mkpdu_dict.update({'mkpdus_tx': int(m.group('mkpdus_tx'))} )
                continue 
            
            #      "Distributed SAK"..... 111
            m = p13.match(line)
            if m:
                if distributed_rx:
                    target_mkpdu_dict.update({'mkpdu_rx_distributed_sak' : int(m.group('mkpdu_distributed_sak'))})
                else: 
                    target_mkpdu_dict.update({'mkpdu_tx_distributed_sak' : int(m.group('mkpdu_distributed_sak'))})
                continue 
            
            # MKA IDB Statistics
            m = p15.match(line)
            if m:
                mka_idb_stats = target_dict.setdefault('mka_idb_stat', {})
                continue 
            
            #MKPDUs Tx Success.......... 171562
            m = p16.match(line) 
            if m:
                mka_idb_stats['mkpdu_tx_success'] = int(m.group('mkpdu_tx_success'))
                continue 
            
            # MKPDUs Tx Fail............. 0
            m = p17.match(line) 
            if m:
                mka_idb_stats['mkpdu_tx_fail'] = int(m.group('mkpdu_tx_fail') )
                continue 
            
            #MKPDUS Tx Pkt build fail... 0
            m = p18.match(line) 
            if m:
                mka_idb_stats['mkpdu_tx_build_fail'] =int(m.group('mkpdu_tx_build_fail'))
                continue 
            
            #MKPDUS No Tx on intf down.. 0
            m = p19.match(line) 
            if m:
                mka_idb_stats['mkpdu_no_tx_on_intf_down'] = int(m.group('mkpdu_no_tx_on_intf_down'))
                continue 
            
            #MKPDUS No Rx on intf down.. 0
            m = p20.match(line) 
            if m:
                mka_idb_stats['mkpdu_no_rx_on_intf_down'] = int(m.group('mkpdu_no_rx_on_intf_down'))
                continue 
            
            #MKPDUs Rx CA Not found..... 1
            m = p21.match(line) 
            if m:
                mka_idb_stats['mkpdu_rx_ca_not_found'] = int(m.group('mkpdu_rx_ca_not_found'))
                continue 
            
            #MKPDUs Rx Error............ 0
            m = p22.match(line) 
            if m:
                mka_idb_stats['mkpdu_rx_error'] =int(m.group('mkpdu_rx_error'))
                continue 
            
            #MKPDUs Rx Success.......... 171556
            m = p23.match(line) 
            if m:
                mka_idb_stats['mkpdu_rx_success'] = int(m.group('mkpdu_rx_success'))
                continue 
            
            # MKPDU Failures
            m = p24.match(line)
            if m:
                mka_stats_mkpdu_failures = target_dict.setdefault('mkpdu_failures', {}) 
                continue 
            
            #MKPDU Rx Validation.............. 202
            m = p25.match(line) 
            if m:
                mka_stats_mkpdu_failures['mkpdu_rx_validation'] = int(m.group('mkpdu_rx_validation'))
                continue  
            
            #MKPDU Rx Bad Peer MN............. 0
            m = p26.match(line) 
            if m:
                mka_stats_mkpdu_failures['mkpdu_rx_bad_peer_mn'] = int(m.group('mkpdu_rx_bad_peer_mn'))
                continue 
            
            #MKPDU Rx Non-recent Peerlist MN.. 0
            m = p27.match(line) 
            if m:
                mka_stats_mkpdu_failures['mkpdu_rx_no_recent_peerlist_mn'] = int(m.group('mkpdu_rx_no_recent_peerlist_mn'))
                continue 
            
            #MKPDU Rx Drop SAKUSE, KN mismatch...... 0
            m = p28.match(line) 
            if m:
                mka_stats_mkpdu_failures['mkpdu_rxdrop_sakuse_kn_mismatch'] = int(m.group('mkpdu_rxdrop_sakuse_kn_mismatch')) 
                continue 
            
            #MKPDU Rx Drop SAKUSE, Rx Not Set....... 0
            m = p29.match(line) 
            if m:
                mka_stats_mkpdu_failures['mkpdu_rxdrop_sakuse_rx_notset'] = int(m.group('mkpdu_rxdrop_sakuse_rx_notset'))
                continue 
            
            #MKPDU Rx Drop SAKUSE, Key MI mismatch.. 0
            m = p30.match(line) 
            if m:
                mka_stats_mkpdu_failures['mkpdu_rxdrop_sakuse_key_mi_mismatch'] = int(m.group('mkpdu_rxdrop_sakuse_key_mi_mismatch'))
                continue 
            
            #MKPDU Rx Drop SAKUSE, AN Not in Use.... 0
            m = p31.match(line) 
            if m:
                mka_stats_mkpdu_failures['mkpdu_rxdrop_sakuse_an_not_inuse'] = int(m.group('mkpdu_rxdrop_sakuse_an_not_inuse'))
                continue 
            
            #MKPDU Rx Drop SAKUSE, KS Rx/Tx Not Set. 0
            m = p32.match(line) 
            if m:
                mka_stats_mkpdu_failures['mkpdu_rxdrop_sakuse_ks_rxtx_notset'] = int(m.group('mkpdu_rxdrop_sakuse_ks_rxtx_notset'))
                continue 
            
            #MKPDU Rx Drop Packet, Ethertype Mismatch. 0
            m = p33.match(line) 
            if m:
                mka_stats_mkpdu_failures['mkpdu_rx_drp_pkt_eth_mismatch'] = int(m.group('mkpdu_rx_drp_pkt_eth_mismatch'))
                continue 
            
            #MKPDU Rx Drop Packet, DestMAC Mismatch... 0
            m = p34.match(line) 
            if m:
                mka_stats_mkpdu_failures['mkpdu_rx_drp_pkt_dest_mac_mismatch'] = int(m.group('mkpdu_rx_drp_pkt_dest_mac_mismatch'))
                continue 
            
            # SAK Failures
            m = p36.match(line)
            if m:
                mka_stats_sak_failures = target_dict.setdefault('sak_failures', {}) 
                continue 
            
            # SAK Generation................... 0
            m = p37.match(line) 
            if m:
                mka_stats_sak_failures['sak_gen'] = int(m.group('sak_gen'))
                continue 
            
            # Hash Key Generation.............. 0
            m = p38.match(line) 
            if m:
                mka_stats_sak_failures['hash_key_gen'] = int(m.group('hash_key_gen'))
                continue 
            
            # SAK Encryption/Wrap.............. 0
            m = p39.match(line) 
            if m:
                mka_stats_sak_failures['sack_ecrypt_wrap'] = int(m.group('sack_ecrypt_wrap'))
                continue 
            
            # SAK Decryption/Unwrap............ 0
            m = p40.match(line) 
            if m:
                mka_stats_sak_failures['sack_decrypt_unwrap'] = int(m.group('sack_decrypt_unwrap'))
                continue 
            
            # CA Failures
            m = p41.match(line)
            if m:
                mka_stats_ca_failures = target_dict.setdefault('ca_failures', {}) 
                continue 
            
            #   ICK Derivation................... 0
            m = p42.match(line)
            if m:
                mka_stats_ca_failures['ick_derivation'] = int(m.group('ick_derivation'))
                continue 
            
            #   KEK Derivation................... 0
            m = p43.match(line)
            if m:
                mka_stats_ca_failures['kek_derivation'] = int(m.group('kek_derivation'))
                continue 
            
            #   Invalid Peer MACsec Capability... 0
            m = p44.match(line)
            if m:
                mka_stats_ca_failures['invalid_peer_macsec_capab'] = int(m.group('invalid_peer_macsec_capab'))
                continue 
            
            # MACsec Failures
            m = p45.match(line)
            if m:
                mka_stats_macsec_failures = target_dict.setdefault('macsec_failures', {}) 
                continue 
            
            #    Rx SA Installation............... 0
            m = p46.match(line) 
            if m:
                mka_stats_macsec_failures['rx_sa_install'] = int(m.group('rx_sa_install'))
                continue 
            
            # Tx SA Installation............... 0
            m = p47.match(line) 
            if m:
                mka_stats_macsec_failures['tx_sa_install'] = int(m.group('tx_sa_install'))
                continue 
        return macsec_mka_stats_dict

# ===========================
# Schema for 'ShowMacsecPolicy'
# ===========================
class ShowMacSecPolicySchema(MetaParser):
    """Schema for
        show macsec policy
        show macsec policy {policy}
    """
    schema = {
        'macsec_policy':{
            Any(): {
                "cipher_suite": str,
                "priority": int,
                "window": int,
                "offset": int,
                "security": str,
                "sak_rekey_time": str,
                Optional("icv_indicator"): str,
                Optional("include_sci"): str,
                Optional("enforce_peer_cipher_suite"): str, 
                Optional('ppk_crypto_policy_name'): str
                }
            }
        }

# ===========================
# Parser for 'ShowMacsecPolicy'
# ===========================

class ShowMacSecPolicy(ShowMacSecPolicySchema):
    """
    parser :
        show macsec policy
        show macsec policy {policy}
    """
    cli_command = ["show macsec policy", "show macsec policy {policy_name}"]
    def cli(self, policy_name = None, output=None):
        if output is None: 
            if policy_name:
                cmd = self.cli_command[1].format(policy_name=policy_name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
        
        # MACSec Policy                    Cipher           Pri  Window       Offset   Security       SAK Rekey time ICV Indicator Include-SCI
        # -------------------------------- ---------------- ---- ------------ -------- -------------- -------------- ------------- -------------
        # MP1                              Enforce-Peer     32   100000       30       must-secure    70             TRUE           FALSE
        # Test-MP1                         Enforce-Peer     16   148809600    0        should-secure  pn-rollover    FALSE          TRUE
        p1 = re.compile(r'^(?P<policy_name>\S+)\s+(?P<cipher_suite>\S+)\s+(?P<priority>\d+)\s+(?P<window>\d+)\s+(?P<offset>\d+)\s+(?P<security>\S+)\s+(?P<sak_rekey_time>\S+)\s+(?P<icv_indicator>\S+)\s*(?P<include_sci>\S+)?$')
        
        # MACSec Policy                    PPK Crypto-Policy-Name
        # -------------------------------- --------------------------------
        #     OR 
        # MACSec Policy                    Cipher-Suite Enforce-Peer
        # -------------------------------- -----------------------------------------------------
        p2 = re.compile(r'^(?P<policy_header>\S+ \S+)\s+(?P<ppk_or_cipher_header>PPK Crypto-QKD-Profile Name|Cipher-Suite Enforce-Peer)$')
        
        # system-default-macsec-policy     test-ppk 
        # p1                               test-ppk-p1
        #           OR 
        # MP1                              GCM-AES-128
        # Test-MP1                         GCM-AES-256 GCM-AES-XPN-256 GCM-AES-XPN-128 GCM-AES-128
        p3 = re.compile(r'^(?P<policy_name>\S+)\s+(?P<ppk_or_cipher_policy>[A-Za-z0-9_\- ]+)$')
        
        #Flag to check header is PPK Crypto-Policy or Cipher-Suite Enforce-Peer
        cipher_ppk_header = None 
        macsec_policy_dict = {} 
        
        for line in output.splitlines():
            line = line.strip()
            if '-----' in line: 
                continue 
            
            # MP1                              Enforce-Peer     32   100000       30       must-secure    70             TRUE           FALSE
            m = p1.match(line)
            if m:
                policy_dict = macsec_policy_dict.setdefault("macsec_policy", {})
                group = m.groupdict()
                ret_dict = policy_dict.setdefault(group["policy_name"],{})
                ret_dict.update({
                    "cipher_suite": group["cipher_suite"],
                    "priority": int(group["priority"]),
                    "window": int(group["window"]),
                    "offset": int(group["offset"]),
                    "security": group["security"],
                    "sak_rekey_time": group["sak_rekey_time"],
                    "icv_indicator": group["icv_indicator"]
                })
                #optional incluce_sci
                if 'include_sci' in group:
                    ret_dict["include_sci"] = group["include_sci"]
                continue
            
            # MACSec Policy                    PPK Crypto-Policy-Name
            # MACSec Policy                    Cipher-Suite Enforce-Peer
            m = p2.match(line) 
            if m:
                cipher_ppk_header = m.group('ppk_or_cipher_header')
                continue
            
            # MP1                              GCM-AES-128
            # Test-MP1                         GCM-AES-256 GCM-AES-XPN-256 GCM-AES-XPN-128 GCM-AES-128
            m = p3.match(line) 
        
            if cipher_ppk_header:
                m = p3.match(line)
                if m:
                    policy = m.group('policy_name')
                    key = 'enforce_peer_cipher_suite' if 'Cipher-Suite Enforce-Peer' in cipher_ppk_header else  'ppk_crypto_policy_name'
                    macsec_policy_dict["macsec_policy"].setdefault(policy, {})
                    macsec_policy_dict["macsec_policy"][policy][key] = m.group('ppk_or_cipher_policy')
        return macsec_policy_dict
    


# ===========================
# Schema for 'show macsec secy statistics'
# ===========================
class ShowMacSecSecyStatisticsSchema(MetaParser):
    """Schema for 
        * show macsec secy statistics 
        * show macsec secy statistics interface {intf}
    
    """

    schema = {
        Any(): {
            "interface_rx_statistics": {
                "unicast_uncontrolled_pkts": str,
                "multicast_uncontrolled_pkts": str,
                "broadcast_uncontrolled_pkts": str,
                "uncontrolled_pkts_rx_drop": str,
                "uncontrolled_pkts_rx_error": str,
                "unicast_controlled_pkts": str,
                "multicast_controlled_pkts": str,
                "broadcast_controlled_pkts": str,
                "controlled_pkts": str,
                "controlled_pkts_rx_drop": str,
                "controlled_pkts_rx_error": str,
                "in_octets_uncontrolled": str,
                "in_octets_controlled": str,
                "input_rate_for_uncontrolled_pkts_pps": str,
                "input_rate_for_uncontrolled_pkts_bps": str,
                "input_rate_for_controlled_pkts_pps": str,
                "input_rate_for_controlled_pkts_bps": str,
            },
            "interface_tx_statistics": {
                "unicast_uncontrolled_pkts": str,
                "multicast_uncontrolled_pkts": str,
                "broadcast_uncontrolled_pkts": str,
                "uncontrolled_pkts_rx_drop": str,
                "uncontrolled_pkts_rx_error": str,
                "unicast_controlled_pkts": str,
                "multicast_controlled_pkts": str,
                "broadcast_controlled_pkts": str,
                "controlled_pkts": str,
                "controlled_pkts_rx_drop": str,
                "controlled_pkts_rx_error": str,
                "out_octets_uncontrolled": str,
                "out_octets_controlled": str,
                "out_octets_common": str,
                "output_rate_uncontrolled_pkts_pps": str,
                "output_rate_uncontrolled_pkts_bps": str,
                "output_rate_controlled_pkts_pps": str,
                "output_rate_controlled_pkts_bps": str,
            },
            "secy_rx_statistics": {
                "transform_error_pkts": str,
                "control_pkts": str,
                "untagged_pkts": str,
                "no_tag_pkts": str,
                "bad_tag_pkts": str,
                "no_sci_pkts": str,
                "unknown_sci_pkts": str,
                "tagged_control_pkts": str,
            },
            "secy_tx_statistics": {
                "transform_error_pkts": str,
                "control_pkts": str,
                "untagged_pkts": str,
            },
            Optional("sak_rx_statistics"): {
               "an_value" : int,
                "unchecked_pkts": str,
                "delayed_pkts": str,
                "late_pkts": str,
                "ok_pkts": str,
                "invalid_pkts": str,
                "not_valid_pkts": str,
                "not_using_sa_pkts": str,
                "unused_sa_pkts": str,
                "decrypted_in_octets": str,
                "validated_in_octets": str,
            },
            Optional("sak_tx_statistics"): {
                "an_value" : int,
                "encrypted_protected_pkts": str,
                "too_long_pkts": str,
                "sa_not_in_use_pkts": str,
               "encrypted_protected_out_octets": str,
            },
        },
        Optional('macsec_shutdown'): bool
    }
# ======================================== #
# Parser for 'show macsec secy statistics' #
# ======================================== #

class ShowMacSecSecyStatistics(ShowMacSecSecyStatisticsSchema):
    """
        parser for
        * show macsec secy statistics 
        * show macsec secy statistics interface {intf}
    """
    cli_command = ["show macsec secy statistics", "show macsec secy statistics interface {interface}"]
    def cli(self, interface = None, output=None):
        if output is None: 
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else :
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
        
        # -----------------------------------
        # Macsec is shutdown
        # -----------------------------------
        p0 = re.compile(r'^Macsec is shutdown$')
        #pattern to match first line of output
        #Interface Ethernet1/1 MACSEC SecY Statistics:
        p1 = re.compile(r'^Interface\s+(?P<interface>\S+)\s+MACSEC\s+SecY\s+Statistics:$')
        #Interface Rx Statistics:
        p2 = re.compile(r'^(?P<interface_rx_statistics>Interface Rx Statistics):$')
        #Unicast Uncontrolled Pkts: 478920
        p3 = re.compile(r'^Unicast Uncontrolled Pkts:\s*(?P<unicast_uncontrolled_pkts>[0-9NA/]+).*$')
        #Multicast Uncontrolled Pkts: 187186
        p4 = re.compile(r'^Multicast Uncontrolled Pkts:\s*(?P<multicast_uncontrolled_pkts>[0-9NA/]+).*$')
        #Broadcast Uncontrolled Pkts: 0
        p5 = re.compile(r'^Broadcast Uncontrolled Pkts:\s*(?P<broadcast_uncontrolled_pkts>[0-9NA/]+).*$')
        #Uncontrolled Pkts - Rx Drop: 0
        p6 = re.compile(r'^Uncontrolled Pkts - Rx Drop:\s*(?P<uncontrolled_pkts_rx_drop>[0-9NA/]+).*$')
        #Uncontrolled Pkts - Rx Error: 0
        p7 = re.compile(r'^Uncontrolled Pkts - Rx Error:\s*(?P<uncontrolled_pkts_rx_error>[0-9NA/]+).*$')
        #Unicast Controlled Pkts: 0
        p8 = re.compile(r'^Unicast Controlled Pkts:\s*(?P<unicast_controlled_pkts>[0-9NA/]+).*$')
        #Multicast Controlled Pkts: 0
        p9 = re.compile(r'^Multicast Controlled Pkts:\s*(?P<multicast_controlled_pkts>[0-9NA/]+).*$')
        #Broadcast Controlled Pkts: 0
        p10= re.compile(r'^Broadcast Controlled Pkts:\s*(?P<broadcast_controlled_pkts>[0-9NA/]+).*$')
        #Controlled Pkts: 575441
        p11= re.compile(r'^Controlled Pkts:\s*(?P<controlled_pkts>[0-9NA/]+).*$')
        #Controlled Pkts - Rx Drop: 0
        p12= re.compile(r'^Controlled Pkts - Rx Drop:\s*(?P<controlled_pkts_rx_drop>[0-9NA/]+).*$')
        #Controlled Pkts - Rx Error: 0
        p13= re.compile(r'^Controlled Pkts - Rx Error:\s*(?P<controlled_pkts_rx_error>[0-9NA/]+).*$')
        #In-Octets Uncontrolled: 285411693 bytes
        p14= re.compile(r'^In-Octets Uncontrolled:\s*(?P<in_octets_uncontrolled>[0-9NA/]+).*$') 
        #In-Octets Controlled: 238532354 bytes
        p15= re.compile(r'^In-Octets Controlled:\s*(?P<in_octets_controlled>[0-9NA/]+).*$') 
        #Input rate for Uncontrolled Pkts: 1 pps
        p16= re.compile(r'^Input rate for Uncontrolled Pkts:\s*(?P<input_rate_for_uncontrolled_pkts_pps>[0-9NA/]+) pps$') # add pps
        #Input rate for Uncontrolled Pkts: 1516 bps
        p17= re.compile(r'^Input rate for Uncontrolled Pkts:\s*(?P<input_rate_for_uncontrolled_pkts_bps>[0-9NA/]+) bps$') # add bps
        #Input rate for Controlled Pkts: 0 pps
        p18= re.compile(r'^Input rate for Controlled Pkts:\s*(?P<input_rate_for_controlled_pkts_pps>[0-9NA/]+) pps$') #add pps
        #Input rate for Controlled Pkts: 648 bps
        p19= re.compile(r'^Input rate for Controlled Pkts:\s*(?P<input_rate_for_controlled_pkts_bps>[0-9NA/]+) bps$') #add bps

        #Input rate for Uncontrolled Pkts: N/A (N9K-X9736C-FX not supported)
        p16_1= re.compile(r'^Input rate for Uncontrolled Pkts:\s*(?P<input_rate_for_uncontrolled_pkts_pps>[0-9NA/]+) .*not supported\)$') # add pps
        #Input rate for Controlled Pkts: N/A (N9K-X9736C-FX not supported)
        p18_1= re.compile(r'^Input rate for Controlled Pkts:\s*(?P<input_rate_for_controlled_pkts_pps>[0-9NA/]+) .*not supported\)$') # add pps

        #Out-Octets Uncontrolled: 0 bytes
        p20= re.compile(r'^Out-Octets Uncontrolled:\s*(?P<out_octets_uncontrolled>[0-9NA/]+).*$')
        #Out-Octets Controlled: 234992070 bytes
        p21= re.compile(r'^Out-Octets Controlled:\s*(?P<out_octets_controlled>[0-9NA/]+).*$') 
        #Out-Octets Common: 278229965 bytes
        p22= re.compile(r'^Out-Octets Common:\s*(?P<out_octets_common>[0-9NA/]+).*$')
        #Output rate for Uncontrolled Pkts: 0 pps
        p23= re.compile(r'^Output rate for Uncontrolled Pkts:\s*(?P<output_rate_uncontrolled_pkts_pps>[0-9NA/]+) pps$')
        #Output rate for Uncontrolled Pkts: 0 bps
        p24= re.compile(r'^Output rate for Uncontrolled Pkts:\s*(?P<output_rate_uncontrolled_pkts_bps>[0-9NA/]+) bps$')
        #Output rate for Controlled Pkts: 0 pps
        p25= re.compile(r'^Output rate for Controlled Pkts:\s*(?P<output_rate_controlled_pkts_pps>[0-9NA/]+) pps$') #add pps
        #Output rate for Controlled Pkts: 459 bps
        p26= re.compile(r'^Output rate for Controlled Pkts:\s*(?P<output_rate_controlled_pkts_bps>[0-9NA/]+) bps$') #add bps 
        ##Output rate for Uncontrolled Pkts: N/A (N9K-X9736C-FX not supported)
        p23_1= re.compile(r'^Output rate for Uncontrolled Pkts:\s*(?P<output_rate_uncontrolled_pkts_pps>[0-9NA/]+) .*not supported\)$') #add pps
        #Output rate for Controlled Pkts: 0 N/A (N9K-X9736C-FX not supported)
        p25_1= re.compile(r'^Output rate for Controlled Pkts:\s*(?P<output_rate_controlled_pkts_pps>[0-9NA/]+) .*not supported\)$') # add bps
        #Interface Tx Statistics:
        p27= re.compile(r'^(?P<interface_tx_statistics>Interface Tx Statistics):$')
        #SECY Rx Statistics:
        p28= re.compile(r'^(?P<secy_rx_statistics>SECY Rx Statistics):$')
        #Transform Error Pkts: 0
        p29= re.compile(r'^Transform Error Pkts:\s*(?P<transform_error_pkts>[0-9NA/]+).*$')
        #Control Pkts: 0
        p30= re.compile(r'^Control Pkts:\s*(?P<control_pkts>[0-9NA/]+).*$')
        #Untagged Pkts: 0
        p31= re.compile(r'^Untagged Pkts:\s*(?P<untagged_pkts>[0-9NA/]+).*$')
        #No Tag Pkts: 0
        p32= re.compile(r'^No Tag Pkts:\s*(?P<no_tag_pkts>[0-9NA/]+).*$')
        #Bad Tag Pkts: 0
        p33= re.compile(r'^Bad Tag Pkts:\s*(?P<bad_tag_pkts>[0-9NA/]+).*$')
        #No SCI Pkts: 0
        p34= re.compile(r'^No SCI Pkts:\s*(?P<no_sci_pkts>[0-9NA/]+).*$')
        #Unknown SCI Pkts: 0
        p35= re.compile(r'^Unknown SCI Pkts:\s*(?P<unknown_sci_pkts>[0-9NA/]+).*$')
        #Tagged Control Pkts: 0
        p36= re.compile(r'^Tagged Control Pkts:\s*(?P<tagged_control_pkts>[0-9NA/]+).*$')
        #SECY Tx Statistics:
        p37= re.compile(r'^(?P<secy_tx_statistics>SECY Tx Statistics):$')
        #SAK Rx Statistics for AN [0]:
        p38= re.compile(r'^SAK Rx Statistics for AN \[(?P<an_value>\d+)\]:$')
        #Unchecked Pkts: 0
        p39= re.compile(r'^Unchecked Pkts:\s*(?P<unchecked_pkts>[0-9NA/]+).*$')
        #Delayed Pkts: 0
        p40= re.compile(r'^Delayed Pkts:\s*(?P<delayed_pkts>[0-9NA/]+).*$')
        #Late Pkts: 0
        p41= re.compile(r'^Late Pkts:\s*(?P<late_pkts>[0-9NA/]+).*$')
        #OK Pkts: 575441
        p42= re.compile(r'^OK Pkts:\s*(?P<ok_pkts>[0-9NA/]+).*$')
        #Invalid Pkts: 0
        p43= re.compile(r'^Invalid Pkts:\s*(?P<invalid_pkts>[0-9NA/]+).*$')
        #Not Valid Pkts: 0
        p44= re.compile(r'^Not Valid Pkts:\s*(?P<not_valid_pkts>[0-9NA/]+).*$')
        # Not-Using-SA Pkts: 0
        p45= re.compile(r'^Not-Using-SA Pkts:\s*(?P<not_using_sa_pkts>[0-9NA/]+).*$')
        #Unused-SA Pkts: 0
        p46= re.compile(r'^Unused-SA Pkts:\s*(?P<unused_sa_pkts>[0-9NA/]+).*$')
        #Decrypted In-Octets: 238532354 bytes
        p47= re.compile(r'^Decrypted In-Octets:\s*(?P<decrypted_in_octets>[0-9NA/]+).*$')
        #Validated In-Octets: 0 bytes
        p48= re.compile(r'^Validated In-Octets:\s*(?P<validated_in_octets>[0-9NA/]+).*$')
        #SAK Tx Statistics for AN [0]:
        p49= re.compile(r'^SAK Tx Statistics for AN \[(?P<an_value>\d+)\]:$')
        #Encrypted Protected Pkts: 499517
        p50= re.compile(r'^Encrypted Protected Pkts:\s*(?P<encrypted_protected_pkts>[0-9NA/]+).*$')
        #Too Long Pkts: 0
        p51= re.compile(r'^Too Long Pkts:\s*(?P<too_long_pkts>[0-9NA/]+).*$')
        #SA-not-in-use Pkts: 0
        p52= re.compile(r'^SA-not-in-use Pkts:\s*(?P<sa_not_in_use_pkts>[0-9NA/]+).*$')
        #Encrypted Protected Out-Octets: 234992070 bytes
        p53= re.compile(r'^Encrypted Protected Out-Octets:\s*(?P<encrypted_protected_out_octets>[0-9NA/]+).*$')

        secy_statistics_dict = {}
        for line in output.splitlines():
            line = line.strip()
            
            # Macsec is shutdown
            m0 = p0.match(line)
            if m0:
                secy_statistics_dict['macsec_shutdown'] = True 
                return secy_statistics_dict
            
            #Interface Ethernet1/1 MACSEC SecY Statistics:
            m = p1.match(line)
            if m:
                interface = m.group("interface")
                intf_dict = secy_statistics_dict.setdefault(interface, {})
                continue 
            
            #Interface Rx Statistics:
            m = p2.match(line)
            if m:
                out_dict = intf_dict.setdefault("interface_rx_statistics",{})
                continue 
                
            #Interface Tx Statistics:
            m = p27.match(line)
            if m:
                out_dict = intf_dict.setdefault("interface_tx_statistics",{})
                continue 
            
            #Unicast Uncontrolled Pkts: 478920
            m = p3.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue
            
            #Multicast Uncontrolled Pkts: 187186
            m = p4.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Broadcast Uncontrolled Pkts: 0
            m = p5.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Uncontrolled Pkts - Rx Drop: 0
            m = p6.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Uncontrolled Pkts - Rx Error: 0
            m = p7.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Unicast Controlled Pkts: 0
            m = p8.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Multicast Controlled Pkts: 0
            m = p9.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Broadcast Controlled Pkts: 0
            m = p10.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Controlled Pkts: 575441
            m = p11.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Controlled Pkts - Rx Drop: 0
            m = p12.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Controlled Pkts - Rx Error: 0
            m = p13.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #In-Octets Uncontrolled: 285411693 bytes
            m = p14.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #In-Octets Controlled: 238532354 bytes
            m = p15.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Input rate for Uncontrolled Pkts: 1 pps
            m = p16.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Input rate for Uncontrolled Pkts: 1516 bps
            m = p17.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Input rate for Controlled Pkts: 0 pps
            m = p18.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Input rate for Controlled Pkts: 648 bps
            m = p19.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            m = p16_1.match(line)
            if m:
                #Intput rate for Uncontrolled Pkts: N/A (N9K-X9736C-FX not supported)
                #bits per second(bps) also will be NA, adding both key values into the output dict
                out_dict['input_rate_for_uncontrolled_pkts_pps'] = m.group('input_rate_for_uncontrolled_pkts_pps')
                out_dict['input_rate_for_uncontrolled_pkts_bps'] = m.group('input_rate_for_uncontrolled_pkts_pps')
                continue 
            
            m = p18_1.match(line) 
            if m:
                #Intput rate for Controlled Pkts: N/A (N9K-X9736C-FX not supported)
                #bits per second(bps) also will be NA, adding both key values into the output dict
                out_dict['input_rate_for_controlled_pkts_pps'] = m.group('input_rate_for_controlled_pkts_pps')
                out_dict['input_rate_for_controlled_pkts_bps'] = m.group('input_rate_for_controlled_pkts_pps')
                continue  
            
            #Out-Octets Uncontrolled: 0 bytes
            m = p20.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Out-Octets Controlled: 234992070 bytes
            m = p21.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Out-Octets Common: 278229965 bytes
            m = p22.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Output rate for Uncontrolled Pkts: 0 pps
            m = p23.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Output rate for Uncontrolled Pkts: 0 bps
            m = p24.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Output rate for Controlled Pkts: 0 pps
            m = p25.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Output rate for Controlled Pkts: 459 bps
            m = p26.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            m = p23_1.match(line)
            if m:
                #Output rate for Uncontrolled Pkts: N/A (N9K-X9736C-FX not supported)
                #bits per second(bps) also will be NA, adding both key values into the output dict
                out_dict['output_rate_uncontrolled_pkts_pps'] = m.group('output_rate_uncontrolled_pkts_pps')
                out_dict['output_rate_uncontrolled_pkts_bps'] = m.group('output_rate_uncontrolled_pkts_pps')
                continue 
            
            m = p25_1.match(line) 
            if m:
                #Output rate for Controlled Pkts: N/A (N9K-X9736C-FX not supported)
                #bits per second(bps) also will be NA, adding both key values into the output dict
                out_dict['output_rate_controlled_pkts_pps'] = m.group('output_rate_controlled_pkts_pps')
                out_dict['output_rate_controlled_pkts_bps'] = m.group('output_rate_controlled_pkts_pps')
                continue  
            
            #SECY Rx Statistics:
            m = p28.match(line)
            if m:
                out_dict = intf_dict.setdefault('secy_rx_statistics',{})
                continue 
            
            #SECY Tx Statistics:
            m = p37.match(line)
            if m:
                out_dict = intf_dict.setdefault('secy_tx_statistics',{})
                continue
            
            #Transform Error Pkts: 0
            m = p29.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Control Pkts: 0
            m = p30.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Untagged Pkts: 0
            m = p31.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #No Tag Pkts: 0
            m = p32.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Bad Tag Pkts: 0
            m = p33.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #No SCI Pkts: 0
            m = p34.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Unknown SCI Pkts: 0
            m = p35.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Tagged Control Pkts: 0
            m = p36.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #SAK Rx Statistics for AN [0]:
            m = p38.match(line)
            if m:
                out_dict = intf_dict.setdefault('sak_rx_statistics',{})
                out_dict['an_value'] = int(m.group('an_value'))
                continue
            
            #Unchecked Pkts: 0
            m = p39.match(line)
            if m:
                out_dict.update(m.groupdict())
                continue 
            
            #Delayed Pkts: 0
            m = p40.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Late Pkts: 0
            m = p41.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #OK Pkts: 575441
            m = p42.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Invalid Pkts: 0
            m = p43.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Not Valid Pkts: 0
            m = p44.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            # Not-Using-SA Pkts: 0
            m = p45.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Unused-SA Pkts: 0
            m = p46.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Decrypted In-Octets: 238532354 bytes
            m = p47.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Validated In-Octets: 0 bytes
            m = p48.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #SAK Tx Statistics for AN [0]:      
            m = p49.match(line)
            if m:
                out_dict = intf_dict.setdefault('sak_tx_statistics',{})
                out_dict['an_value'] = int(m.group('an_value'))
                continue
            
            #Encrypted Protected Pkts: 499517
            m = p50.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Too Long Pkts: 0
            m = p51.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #SA-not-in-use Pkts: 0
            m = p52.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 
            
            #Encrypted Protected Out-Octets: 234992070 bytes
            m = p53.match(line) 
            if m: 
                out_dict.update(m.groupdict())
                continue 

        return secy_statistics_dict

