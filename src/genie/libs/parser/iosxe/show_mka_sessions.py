''' show_mka_sessions.py

IOSXE parsers for the following show commands:
    * show mka sessions
    * show mka sessions interface {interface}
    * show mka sessions interface {interface} detail
    * show macsec interface {interface}
'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    Optional, \
    Or, \
    And, \
    Default, \
    Use

# import parser utils
from genie.libs.parser.utils.common import Common

'''
Device#sh mka sessions

Total MKA Sessions....... 1
      Secured Sessions... 1
      Pending Sessions... 0

====================================================================================================
Interface      Local-TxSCI         Policy-Name      Inherited         Key-Server
Port-ID        Peer-RxSCI          MACsec-Peers     Status            CKN
====================================================================================================
Hu2/6/0/39     70b3.171e.b282/0103 *DEFAULT POLICY* NO                NO
259            00a7.42ce.d57f/0074 1                Secured           10                                                      

'''

# ==============================================
# Parser for 'show mka sessions'
# ==============================================
class ShowMkaSessionsSchema(MetaParser):
    """Schema for show mka sessions
                  show mka sessions interface {interface}
    """
    schema = {
        'sessions': {
            Any(): {
                'interface': str,
                'local-txsci': str,
                'policy-name': str,
                'inherited': str,
                'key-server': str,
                'port-id': str,
                'peer-rxsci': str,
                'macsec-peers': str,
                'status': str,
                'ckn': str
            },
        Optional('total-mka-sessions'): int,
        Optional('secured-mka-sessions'): int,
        Optional('pending-mka-sessions'): int
    }
    }

class ShowMkaSessions(ShowMkaSessionsSchema):
    """Parser for 'show mka sessions'
                  'show mka sessions interface {interface}''
    """

    cli_command = ['show mka sessions', 'show mka sessions interface {interface}']
    def cli(self, interface=None, output=None):
        if interface:
            cmd = self.cli_command[1].format(interface=interface)
        else:
            cmd = self.cli_command[0]

        if output is None:
            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}
  
        p1 = re.compile('^Total MKA Sessions\.+ (?P<total_mka_sessions>\d+)$')
        p2 = re.compile('^Secured Sessions\.+ (?P<secured_mka_sessions>\d+)$')
        p3 = re.compile('^Pending Sessions\.+ (?P<pending_mka_sessions>\d+)$')

        # Matching patterns
        #Hu2/6/0/39     70b3.171e.b282/0103 *DEFAULT POLICY* NO                NO
        p4 = re.compile(r'(?P<interface>\S+\/\S+) +'
                    '(?P<local_txsci>\w+\.\w+\.\w+\/\w+) +'
                    '(?P<policy_name>\S+(?: +\S+)?) +'
                    '(?P<inherited>\w+) +'
                    '(?P<key_server>\w+(?: +\w+)?)')

        # Matching patterns
        #259            00a7.42ce.d57f/0074 1                Secured           10
        p5 = re.compile(r'(?P<port_id>\d+) +'
                        '(?P<peer_rxsci>\w+\.\w+\.\w+\/\w+) +'
                        '(?P<macsec_peers>\w+) +'
                        '(?P<status>.*) '
                        '(?P<ckn>\d+)')

        session_count = 0
        for line in out.splitlines():
            out_dict = ret_dict.setdefault('sessions', {})
            line = line.strip()
            m1=p1.match(line)
            if m1:
                  group = m1.groupdict()
                  out_dict['total-mka-sessions'] = int(group['total_mka_sessions'])
            m2=p2.match(line)
            if m2:
                  group = m2.groupdict()
                  out_dict['secured-mka-sessions'] = int(group['secured_mka_sessions'])
            m3=p3.match(line)
            if m3:
                  group = m3.groupdict()
                  out_dict['pending-mka-sessions'] = int(group['pending_mka_sessions'])
               
            m4=p4.match(line)
            if m4:
                  group = m4.groupdict()
                  session_count+=1
                  sess_dict = out_dict.setdefault(session_count, {})
                  sess_dict['interface'] = group['interface']
                  sess_dict['local-txsci'] = group['local_txsci']
                  sess_dict['policy-name'] = group['policy_name']
                  sess_dict['inherited'] = group['inherited']
                  sess_dict['key-server'] = group['key_server']

            m5=p5.match(line)
            if m5:
                  group = m5.groupdict()
                  sess_dict = out_dict.setdefault(session_count, {})
                  sess_dict['port-id'] = group['port_id']
                  sess_dict['peer-rxsci'] = group['peer_rxsci']
                  sess_dict['macsec-peers'] = group['macsec_peers']
                  sess_dict['status'] = group['status'].strip()
                  sess_dict['ckn'] = group['ckn']
        return ret_dict


# ==================================================================================
# Parser for 'show mka sessions interface {interface} detail'
# ==================================================================================
class ShowMkaSessionsInterfaceDetailsSchema(MetaParser):
    """Schema for 'show mka sessions interface {interface} detail'
    """
    schema = {
             'sessions': {
               'status': str,
               'local-txsci': str,
               'interface-mac-address': str,
               'mka-port-identifier': str,
               'interface-name': str,
               Optional('audit-session-id'): str,
               'ckn': str,
               'member-identifier': str,
               'message-number': str,
               'eap-role': str,
               'key-server': str,
               'mka-cipher-suite': str,
               'latest-sak-status': str,
               'latest-sak-an': str,
               'latest-sak-ki': str,
               'old-sak-status': str,
               'old-sak-an': str,
               'old-sak-ki': str,
               'sak-transmit-wait-time': str,
               'sak-retire-time': str,
               'sak-rekey-time': str,
               'mka-policy-name': str,
               'key-server-priority': str,
               'delay-protection': str,
               'delay-protection-timer': str,
               'confidentiality-offset': str,
               'algorithm-agility': str,
               'sak-rekey-on-live-peer-loss': str,
               'send-secure-announcement': str,
               'sci-based-ssci-computation': str,
               'sak-cipher-suite': str,
               'macsec-capability': str,
               'macsec-desired': str,
               'macsec-capable-live-peers': str,
               'macsec-capable-live-peers-responded': str,
               Optional('live-peers'): {
                                 Any(): {
                                    'mi': str,
                                    'mn': str,
                                    'rx-sci': str,
                                    'ks-priority': str,
                                    'rxsa-installed': str,
                                    'ssci': str
                                 }
               },
               Optional('potential-peers') : {
                                 Any(): {
                                    'mi': str,
                                    'mn': str,
                                    'rx-sci': str,
                                    'ks-priority': str,
                                    'rxsa-installed': str,
                                    'ssci': str
                                 }
                },
                Optional('dormant-peers') : {
                                 Any(): {
                                    'mi': str,
                                    'mn': str,
                                    'rx-sci': str,
                                    'ks-priority': str,
                                    'rxsa-installed': str,
                                    'ssci': str
                                 }
    }}}


class ShowMkaSessionsInterfaceDetails(ShowMkaSessionsInterfaceDetailsSchema):
    """Parser for 'show mka sessions interface {interface} detail'
    """
    cli_command = 'show mka sessions interface {interface} detail'

    def cli(self, interface, output=None):
        if not output:
            # get output from device
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        #Matching the below lines one by one
        '''
        Local Tx-SCI............. 70b3.171e.b282/0103
        Interface MAC Address.... 70b3.171e.b282
        MKA Port Identifier...... 259
        Interface Name........... HundredGigE2/6/0/39
        Audit Session ID.........
        CAK Name (CKN)........... 10
        Member Identifier (MI)... B271E451F722674FE69DF8FE
        Message Number (MN)...... 258834
        EAP Role................. NA
        Key Server............... NO
        MKA Cipher Suite......... AES-256-CMAC

        Latest SAK Status........ Rx & Tx
        Latest SAK AN............ 0
        Latest SAK KI (KN)....... 9F334340CD9A81C2624FE7A0000001E1 (481)
        Old SAK Status........... No Rx, No Tx
        Old SAK AN............... 3
        Old SAK KI (KN).......... RETIRED (480)

        SAK Transmit Wait Time... 0s (Not waiting for any peers to respond)
        SAK Retire Time.......... 0s (No Old SAK to retire)
        SAK Rekey Time........... 0s (SAK Rekey interval not applicable)

        MKA Policy Name.......... *DEFAULT POLICY*
        Key Server Priority...... 0
        Delay Protection......... NO
        Delay Protection Timer.......... 0s (Not enabled)

        Confidentiality Offset... 0
        Algorithm Agility........ 80C201
        SAK Rekey On Live Peer Loss........ NO
        Send Secure Announcement.. DISABLED
        SCI Based SSCI Computation.... NO
        SAK Cipher Suite......... 0080C20001000001 (GCM-AES-128)
        MACsec Capability........ 3 (MACsec Integrity, Confidentiality, & Offset)
        MACsec Desired........... YES
        '''

        ret_dict = {}
        peer='None'
        live_peer_count=0
        potential_peer_count=0
        dormant_peer_count=0        
        p1 = re.compile(r'^Status\: (?P<status>\S+)')
        p2 = re.compile(r'^Local Tx-SCI.+ (?P<local_txsci>\S+)$')
        p3 = re.compile(r'^Interface MAC Address.+ (?P<interface_mac>\S+\.\S+\.\S+)$')
        p4 = re.compile(r'^MKA Port Identifier.+ (?P<mka_port_id>\S+)$')
        p5 = re.compile(r'^Interface Name.+ (?P<int_name>\S+)$')
        p6 = re.compile(r'^Audit Session ID.+ (?P<audit_sess>\S+)$')
        p7 = re.compile(r'^CAK Name \(CKN\).+ (?P<ckn>\S+)$')
        p8 = re.compile(r'^Member Identifier \(MI\).+ (?P<mi>\S+)$')
        p9 = re.compile(r'^Message Number \(MN\).+ (?P<mn>\S+)$')
        p10 = re.compile(r'^EAP Role.+ (?P<eap_role>\S+)$')
        p11 = re.compile(r'^Key Server\.+ (?P<key_server>\w+)$')
        p12 = re.compile(r'^MKA Cipher Suite.+ (?P<mka_cipher_suite>\S+)$')
        p13 = re.compile(r'^Latest SAK Status\.+ +(?P<latest_sak_status>\S+(?: +\S+)*)')
        p14 = re.compile(r'^Latest SAK AN.+ (?P<latest_sak_an>\w+)$')
        p15 = re.compile(r'^Latest SAK KI \(KN\)\.+ (?P<latest_sak_ki>(.*))')
        p16 = re.compile(r'^Old SAK Status\.+ (?P<old_sak_status>(.*))')
        p17 = re.compile(r'^Old SAK AN.+ (?P<old_sak_an>\w+)$')
        p18 = re.compile(r'^Old SAK KI \(KN\)\.+ (?P<old_sak_ki>(.*))')
        p19 = re.compile(r'^SAK Transmit Wait Time\.+ (?P<sak_transmit_wait_time>(.*))')
        p20 = re.compile(r'^SAK Retire Time\.+ (?P<sak_retire_time>(.*))')
        p21 = re.compile(r'^SAK Rekey Time\.+ (?P<sak_rekey_time>(.*))')
        p22 = re.compile(r'^MKA Policy Name\.+ (?P<mka_policy_name>(.*))')
        p23 = re.compile(r'^Delay Protection\.+ (?P<delay_protection>\w+)$')
        p24 = re.compile(r'^Confidentiality Offset\.+ (?P<confidentiality_offset>\w+)$')
        p25 = re.compile(r'^Algorithm Agility\.+ (?P<algorithm_agility>\w+)$')
        p26 = re.compile(r'^SAK Rekey On Live Peer Loss\.+ (?P<sak_rekey_on_live_peer_loss>\w+)$')
        p27 = re.compile(r'^Send Secure Announcement\.+ (?P<send_secure_announcement>\w+)$')
        p28 = re.compile(r'^SCI Based SSCI Computation\.+ (?P<sci_based_ssci_computation>\w+)$')
        p29 = re.compile(r'^SAK Cipher Suite\.+ (?P<sak_cipher_suite>(.*))')
        p30 = re.compile(r'^MACsec Capability\.+ (?P<macsec_capability>(.*))')
        p31 = re.compile(r'^MACsec Desired\.+ (?P<macsec_desired>\w+)$')
        p32 = re.compile(r'^\# of MACsec Capable Live Peers\.+ (?P<macsec_capable_live_peers>\w+)$')
        p33 = re.compile(r'^\# of MACsec Capable Live Peers Responded\.+ (?P<macsec_capable_live_peers_responded>\w+)$')
        p34 = re.compile(r'^Delay Protection Timer\.+ (?P<delay_protection_timer>(.*))')
        p35 = re.compile(r'^Key Server Priority\.+ (?P<key_server_priority>\S+)')

        #Matching the below peer list line by line
        '''
        Live Peers List:
        MI                        MN          Rx-SCI (Peer)        KS        RxSA          SSCI
                                                                   Priority  Installed
        ---------------------------------------------------------------------------------------
        9F334340CD9A81C2624FE7A0  258375      00a7.42ce.d57f/0074  0         YES            0

        Potential Peers List:
        MI                        MN          Rx-SCI (Peer)        KS        RxSA          SSCI
                                                                   Priority  Installed
        ---------------------------------------------------------------------------------------

        Dormant Peers List:
        MI                        MN          Rx-SCI (Peer)        KS        RxSA          SSCI
                                                                   Priority  Installed
        ---------------------------------------------------------------------------------------
        '''

        p36 = re.compile(r'^Live Peers List:')
        p37 = re.compile(r'^Potential Peers List:')
        p38 = re.compile(r'^Dormant Peers List:')
        p39 = re.compile(re.compile(r'(?P<mi>\S+) +'
                            '(?P<mn>\S+) +'
                        '(?P<rx_sci>\w+\.\w+\.\w+\/\w+) +'
                        '(?P<ks_priority>\w+) +'
                        '(?P<rxsa_installed>\w+) +'
                        '(?P<ssci>\w+)')) 

        for line in out.splitlines():
            out_dict = ret_dict.setdefault('sessions', {})
            line=line.strip()
            m1=p1.match(line)
            if m1:
                group = m1.groupdict()
                out_dict['status'] = group['status']
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                out_dict['local-txsci'] = group['local_txsci']
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                out_dict['interface-mac-address'] = group['interface_mac']
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                out_dict['mka-port-identifier'] = group['mka_port_id']
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                out_dict['interface-name'] = group['int_name']
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                out_dict['audit-sess'] = group['audit_sess']
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                out_dict['ckn'] = group['ckn']
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                out_dict['member-identifier'] = group['mi']
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                out_dict['message-number'] = group['mn']
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                out_dict['eap-role'] = group['eap_role']
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                out_dict['key-server'] = group['key_server']
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                out_dict['mka-cipher-suite'] = group['mka_cipher_suite']
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                out_dict['latest-sak-status'] = group['latest_sak_status']
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                out_dict['latest-sak-an'] = group['latest_sak_an']
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                out_dict['latest-sak-ki'] = group['latest_sak_ki']
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                out_dict['old-sak-status'] = group['old_sak_status']
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                out_dict['old-sak-an'] = group['old_sak_an']
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                out_dict['old-sak-ki'] = group['old_sak_ki']
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                out_dict['sak-transmit-wait-time'] = group['sak_transmit_wait_time']
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                out_dict['sak-retire-time'] = group['sak_retire_time']
            m21 = p21.match(line)
            if m21:
                group = m21.groupdict()
                out_dict['sak-rekey-time'] = group['sak_rekey_time']
            m22 = p22.match(line)
            if m22:
                group = m22.groupdict()
                out_dict['mka-policy-name'] = group['mka_policy_name']
            m23 = p23.match(line)
            if m23:
                group = m23.groupdict()
                out_dict['delay-protection'] = group['delay_protection']
            m24 = p24.match(line)
            if m24:
                 group = m24.groupdict()
                 out_dict['confidentiality-offset'] = group['confidentiality_offset']
            m25 = p25.match(line)
            if m25:
                 group = m25.groupdict()
                 out_dict['algorithm-agility'] = group['algorithm_agility']
            m26 = p26.match(line)
            if m26:
                 group = m26.groupdict()
                 out_dict['sak-rekey-on-live-peer-loss'] = group['sak_rekey_on_live_peer_loss']
            m27 = p27.match(line)
            if m27:
                 group = m27.groupdict()
                 out_dict['send-secure-announcement'] = group['send_secure_announcement']
            m28 = p28.match(line)
            if m28:
                group = m28.groupdict()
                out_dict['sci-based-ssci-computation'] = group['sci_based_ssci_computation']
            m29 = p29.match(line)
            if m29:
                 group = m29.groupdict()
                 out_dict['sak-cipher-suite'] = group['sak_cipher_suite']
            m30 = p30.match(line)
            if m30:
                 group = m30.groupdict()
                 out_dict['macsec-capability'] = group['macsec_capability']
            m31 = p31.match(line)
            if m31:
                group = m31.groupdict()
                out_dict['macsec-desired'] = group['macsec_desired']
            m32 = p32.match(line)
            if m32:
                 group = m32.groupdict()
                 out_dict['macsec-capable-live-peers'] = group['macsec_capable_live_peers']
            m33 = p33.match(line)
            if m33:
                group = m33.groupdict()
                out_dict['macsec-capable-live-peers-responded'] = group['macsec_capable_live_peers_responded']
            m34 = p34.match(line)
            if m34:
                group = m34.groupdict()
                out_dict['delay-protection-timer'] = group['delay_protection_timer']
            m35 = p35.match(line)
            if m35:
                group = m35.groupdict()
                out_dict['key-server-priority'] = group['key_server_priority']

            m36 = p36.match(line)
            if m36:
               peer='Live'
               live_peers = out_dict.setdefault('live-peers', {})
            m37 = p37.match(line)
            if m37:
               peer='Potential'
               potential_peers = out_dict.setdefault('potential-peers', {})
            m38 = p38.match(line)
            if m38:
               peer='Dormant'
               dormant_peers = out_dict.setdefault('dormant-peers', {})
            m39 = p39.match(line)
            if m39:
               group = m39.groupdict()
               if peer == 'Live':
                   live_peer_count+=1
                   live_dict = live_peers.setdefault(live_peer_count, {})
                   live_dict['mi'] = group['mi']
                   live_dict['mn'] = group['mn']
                   live_dict['rx-sci'] = group['rx_sci']
                   live_dict['ks-priority'] = group['ks_priority']
                   live_dict['rxsa-installed'] = group['rxsa_installed']
                   live_dict['ssci'] = group['ssci']
               elif peer == 'Potential':
                   potential_peer_count+=1
                   potential_dict = potential_peers.setdefault(potential_peer_count, {})
                   potential_dict['mi'] = group['mi']
                   potential_dict['mn'] = group['mn']
                   potential_dict['rx-sci'] = group['rx_sci']
                   potential_dict['ks-priority'] = group['ks_priority']
                   potential_dict['rxsa-installed'] = group['rxsa_installed']
                   potential_dict['ssci'] = group['ssci']
               elif peer == 'Dormant':
                   dormant_peer_count+=1
                   dormant_dict = dormant_peers.setdefault(dormant_peer_count, {})
                   dormant_dict['mi'] = group['mi']
                   dormant_dict['mn'] = group['mn']
                   dormant_dict['rx-sci'] = group['rx_sci']
                   dormant_dict['ks-priority'] = group['ks_priority']
                   dormant_dict['rxsa-installed'] = group['rxsa_installed']
                   dormant_dict['ssci'] = group['ssci']
        return ret_dict


# ==============================================
# Parser for 'show macsec interface {interface}'
# ==============================================
class ShowMacsecInterfaceSchema(MetaParser):
    """Schema for show macsec interface {interface}
    """
    schema = {
        'macsec-data': {
                 'admin-pt2pt-mac': str,
                 'cipher': str,
                 'confidentiality-offset': str,
                 'include-sci': str,
                 'status': str,
                 'pt2pt-mac-operational': str,
                 'replay-protect-status': str,
                 Optional('replay-window'): str,
                 'use-es-enable': str,
                 'use-scb-enable': str
                       },
        'capabilities': {
                  'data-length-change-supported': str,
                  'icv-length': str,
                  'max-rx-sa': str,
                  'max-rx-sc': str,
                  'max-tx-sa': str,
                  'max-tx-sc': str,
                  'pn-threshold-notification-support': str,
                  'validate-frames': str,
                  'ciphers-supported': list
                        },
        'access-control': str,
         Optional('cleartag-details'): {
             'type': str,
             'vlanid1': str
                            },
         Optional('transmit-secure-channels'): {
                              'confidentiality': str,
                              'current-an': str,
                              'elapsed-time': str,
                              'next-pn': str,
                              'previous-an': str,
                              'sak-unchanged': str,
                              'sa-create-time': str,
                              'sa-start-time': str,
                              'sa-state': str,
                              'sci': str,
                              'sc-state': str,
                              'start-time': str,
                              'sa-statistics': {
                                                'auth-only-bytes': str,
                                                'auth-only-pkts': str,
                                                'encrypted-bytes': str,
                                                'encrypted-pkts': str
                                               },
                              'sc-statistics': {'auth-only-bytes': str,
                                                'auth-only-pkts': str,
                                                'encrypted-bytes': str,
                                                'encrypted-pkts': str
                                               },
                              'port-statistics': {'egress-long-pkts': str,
                                                  'egress-untag-pkts': str
                                               }
                                     },
         Optional('receive-secure-channels'):{
                     Any():{
                             'current-an': str,
                             'elapsed-time': str,
                             'next-pn': str,
                             'sc-state': str,
                             'start-time': str,
                             'previous-an': str,
                             'rx-sa-count': str,
                             'sak-unchanged': str,
                             'sa-create-time': str,
                             'sa-start-time': str,
                             'sa-state': str,
                             'sa-statistics': {'decrypted-bytes': str,
                                               'invalid-pkts': str,
                                               'notvalid-pkts': str,
                                               'nousingsa-pkts': str,
                                               'unusedsa-pkts': str,
                                               'valid-pkts': str,
                                               'validated-bytes': str},
                             'sc-statistics': {'decrypted-bytes': str,
                                               'delay-pkts': str,
                                               'invalid-pkts': str,
                                               'late-pkts': str,
                                               'notvalid-pkts': str,
                                               'nousingsa-pkts': str,
                                               'uncheck-pkts': str,
                                               'unusedsa-pkts': str,
                                               'valid-pkts': str,
                                               'validated-bytes': str}
                                        },
                             'port-statistics': {'ingress-badtag-pkts': str,
                                                 'ingress-nosci-pkts': str,
                                                 'ingress-notag-pkts': str,
                                                 'ingress-overrun-pkts': str,
                                                 'ingress-unknownsci-pkts': str,
                                                 'ingress-untag-pkts': str}
                             }
                     }


class ShowMacsecInterface(ShowMacsecInterfaceSchema):
    'Parser for show macsec interface {interface}'

    cli_command = 'show macsec interface {interface}'
    def cli(self, interface=None, output=None):

        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        ret_dict = {}
        #MACsec is enabled
        p1 = re.compile(r'^MACsec is (?P<status>\S+)$')

        #Replay protect : enabled
        p2 = re.compile(r'^Replay protect \: (?P<replay_protect_status>\S+)$')

        #Replay window : 4294967295
        p3 = re.compile(r'^Replay window \: (?P<replay_window>\S+)$')

        #Include SCI : yes
        p4 = re.compile(r'^Include SCI \: (?P<include_sci>\S+)$')

        #Use ES Enable : no
        p5 = re.compile(r'^Use ES Enable \: (?P<use_es_enable>\S+)$')

        #Use SCB Enable : no
        p6 = re.compile(r'^Use SCB Enable \: (?P<use_scb_enable>\S+)$')

        #Admin Pt2Pt MAC : forceTrue(1)
        p7 = re.compile(r'^Admin Pt2Pt MAC \: (?P<admin_pt2pt_mac>(.*))')

        #Pt2Pt MAC Operational : no
        p8 = re.compile(r'^Pt2Pt MAC Operational \: (?P<pt2pt_mac_operational>\S+)$')

        #Cipher : GCM-AES-XPN-256
        p9 = re.compile(r'^Cipher \: (?P<cipher>\S+)$')

        #Confidentiality Offset : 0
        p10 = re.compile(r'^Confidentiality Offset \: (?P<confidentiality_offset>\S+)$')

        #Capabilities
        p11 = re.compile(r'^Capabilities$')

        #ICV length : 16
        p12 = re.compile(r'^ICV length \: (?P<icv_length>\S+)$')

        #Data length change supported: yes
        p13 = re.compile(r'^Data length change supported\: (?P<data_length_change_supported>\S+)$')

        #Max. Rx SA : 16
        p14 = re.compile(r'^Max\. Rx SA \: (?P<max_rx_sa>\S+)$')

        #Max. Tx SA : 16
        p15 = re.compile(r'^Max\. Tx SA \: (?P<max_tx_sa>\S+)$')

        #Max. Rx SC : 8
        p16 = re.compile(r'^Max\. Rx SC \: (?P<max_rx_sc>\S+)$')

        #Max. Tx SC : 8
        p17 = re.compile(r'^Max\. Tx SC \: (?P<max_tx_sc>\S+)$')

        #Validate Frames : strict
        p18 = re.compile(r'^Validate Frames \: (?P<validate_frames>\S+)$')

        #PN threshold notification support : Yes
        p19 = re.compile(r'^PN threshold notification support \: (?P<pn_threshold_notification_support>\S+)$')

        #Ciphers supported : GCM-AES-128
        p20 = re.compile(r'^Ciphers supported \: (?P<ciphers_supported>\S+)$')

        #GCM-AES-256
        p21 = re.compile(r'^GCM.+(?P<ciphers>128|256)$')

        #Access control : must secure
        p22 = re.compile(r'^Access control \: (?P<access_control>(.*))$')

        #Type    : one dot1q in clear
        p23 = re.compile(r'^Type    \: (?P<type>(.*))$')

        #VlanId1 : 111
        p24 = re.compile(r'^VlanId1 \: (?P<vlanid1>\S+)$')

        #Transmit Secure Channels
        p25 = re.compile(r'^Transmit Secure Channels$')

        #SCI : F87A412527020488
        p26 = re.compile(r'^SCI \: (?P<sci>\S+)$')

        #SC state : inUse(1)
        p27 = re.compile(r'^SC state \: (?P<sc_state>\S+)$')

        #Elapsed time : 7w0d
        p28 = re.compile(r'^Elapsed time \: (?P<elapsed_time>\S+)$')

        #Start time : 7w0d
        p29 = re.compile(r'^Start time \: (?P<start_time>\S+)$')

        #Current AN: 0
        p30 = re.compile(r'^Current AN\: (?P<current_an>\S+)$')

        #Previous AN: -
        p31 = re.compile(r'^Previous AN\: (?P<previous_an>\S+)$')

        #Next PN: 250
        p32 = re.compile(r'^Next PN\: (?P<next_pn>\S+)$')

        #SA State: inUse(1)
        p33 = re.compile(r'^SA State\: (?P<sa_state>\S+)$')

        #Confidentiality : yes
        p34 = re.compile(r'^Confidentiality \: (?P<confidentiality>\S+)$')

        #SAK Unchanged : yes
        p35 = re.compile(r'^SAK Unchanged \: (?P<sak_unchanged>\S+)$')

        #SA Create time : 01:32:52
        p36 = re.compile(r'^SA Create time \: (?P<sa_create_time>(.*))$')

        #SA Start time : 7w0d
        p37 = re.compile(r'^SA Start time \: (?P<sa_start_time>\S+)$')

        #SC Statistics
        p38 = re.compile(r'^SC Statistics$')

        #Auth-only Pkts : 0
        p39 = re.compile(r'^Auth\-only Pkts \: (?P<auth_only_pkts>\d+)$')

        #Auth-only Bytes : 0
        p40 = re.compile(r'^Auth\-only Bytes \: (?P<auth_only_bytes>\d+)$')

        #Encrypted Pkts : 0
        p41 = re.compile(r'^Encrypted Pkts \: (?P<encrypted_pkts>\d+)$')

        #Encrypted Bytes : 0
        p42 = re.compile(r'^Encrypted Bytes \: (?P<encrypted_bytes>\d+)$')

        #SA Statistics
        p43 = re.compile(r'^SA Statistics$')

        #Port Statistics
        p44 = re.compile(r'^Port Statistics$')

        #Egress untag pkts  0
        p45 = re.compile(r'^Egress untag pkts  (?P<egress_untag_pkts>\d+)$')

        #Egress long pkts  0
        p46 = re.compile(r'^Egress long pkts  (?P<egress_long_pkts>\d+)$')

        #Receive Secure Channels
        p47 = re.compile(r'^Receive Secure Channels$')

        #RX SA Count: 0
        p48 = re.compile(r'^RX SA Count\: (?P<rx_sa_count>\d+)$')

        #Notvalid pkts 0
        p49 = re.compile(r'^Notvalid pkts (?P<notvalid_pkts>\d+)$')

        #Invalid pkts 0
        p50 = re.compile(r'^Invalid pkts (?P<invalid_pkts>\d+)$')

        #Valid pkts 0
        p51 = re.compile(r'^Valid pkts (?P<valid_pkts>\d+)$')

        #UnusedSA pkts 0
        p52 = re.compile(r'^UnusedSA pkts (?P<unusedsa_pkts>\d+)$')

        #NousingSA pkts 0
        p53 = re.compile(r'^NousingSA pkts (?P<nousingsa_pkts>\d+)$')

        #Validated Bytes 0
        p54 = re.compile(r'^Validated Bytes (?P<validated_bytes>\d+)$')

        #Decrypted Bytes 0
        p55 = re.compile(r'^Decrypted Bytes (?P<decrypted_bytes>\d+)$')

        #Late pkts 0
        p56 = re.compile(r'^Late pkts (?P<late_pkts>\d+)$')

        #Uncheck pkts 0
        p57 = re.compile(r'^Uncheck pkts (?P<uncheck_pkts>\d+)$')

        #Delay pkts 0
        p58 = re.compile(r'^Delay pkts (?P<delay_pkts>\d+)$')

        #Ingress untag pkts  0
        p59 = re.compile(r'^Ingress untag pkts  (?P<ingress_untag_pkts>\d+)$')

        #Ingress notag pkts  54
        p60 = re.compile(r'^Ingress notag pkts  (?P<ingress_notag_pkts>\d+)$')

        #Ingress badtag pkts  0
        p61 = re.compile(r'^Ingress badtag pkts  (?P<ingress_badtag_pkts>\d+)$')

        #Ingress unknownSCI pkts  0
        p62 = re.compile(r'^Ingress unknownSCI pkts  (?P<ingress_unknownsci_pkts>\d+)$')

        #Ingress noSCI pkts  0
        p63 = re.compile(r'^Ingress noSCI pkts  (?P<ingress_nosci_pkts>\d+)$')

        #Ingress overrun pkts  0
        p64 = re.compile(r'^Ingress overrun pkts  (?P<ingress_overrun_pkts>\d+)$')

        for line in out.splitlines():
            macsec_dict = ret_dict.setdefault('macsec-data', {})
            line=line.strip()
            m1=p1.match(line)
            if m1:
                group = m1.groupdict()
                macsec_dict['status'] = group['status']
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                macsec_dict['replay-protect-status'] = group['replay_protect_status']
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                macsec_dict['replay-window'] = group['replay_window']
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                macsec_dict['include-sci'] = group['include_sci']
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                macsec_dict['use-es-enable'] = group['use_es_enable']
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                macsec_dict['use-scb-enable'] = group['use_scb_enable']
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                macsec_dict['admin-pt2pt-mac'] = group['admin_pt2pt_mac']
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                macsec_dict['pt2pt-mac-operational'] = group['pt2pt_mac_operational']
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                macsec_dict['cipher'] = group['cipher']
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                macsec_dict['confidentiality-offset'] = group['confidentiality_offset']

            m11 = p11.match(line)
            if m11:
                capab_dict = ret_dict.setdefault('capabilities', {})
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                capab_dict['icv-length'] = group['icv_length']
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                capab_dict['data-length-change-supported'] = group['data_length_change_supported']
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                capab_dict['max-rx-sa'] = group['max_rx_sa']
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                capab_dict['max-tx-sa'] = group['max_tx_sa']
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                capab_dict['max-rx-sc'] = group['max_rx_sc']
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                capab_dict['max-tx-sc'] = group['max_tx_sc']
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                capab_dict['validate-frames'] = group['validate_frames']
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                capab_dict['pn-threshold-notification-support'] = group['pn_threshold_notification_support']
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                ciphers_list = capab_dict.setdefault('ciphers-supported', [])
                ciphers_list.append(group['ciphers_supported'])
            m21 = p21.match(line)
            if m21:
                ciphers_list = capab_dict.setdefault('ciphers-supported', [])
                ciphers_list.append(m21.group())
            m22 = p22.match(line)
            if m22:
                ret_dict['access-control'] = m22.groupdict()['access_control']
            m23 = p23.match(line)
            if m23:
                group = m23.groupdict()
                cleartag_details = ret_dict.setdefault('cleartag-details', {})
                cleartag_details['type'] = group['type']
            m24 = p24.match(line)
            if m24:
                group = m24.groupdict()
                cleartag_details = ret_dict.setdefault('cleartag-details', {})
                cleartag_details['vlanid1'] = group['vlanid1']

            m25 = p25.match(line)
            if m25:
                transmit_dict = ret_dict.setdefault('transmit-secure-channels', {})
                secure_ch = 'transmit'
            m26 = p26.match(line)
            if m26:
                group = m26.groupdict()
                if secure_ch == 'transmit':
                    transmit_dict['sci'] = group['sci']
                elif secure_ch == 'receive':
                    recv_dict = receive_dict.setdefault(group['sci'], {})
            m27 = p27.match(line)
            if m27:
                group = m27.groupdict()
                if secure_ch == 'transmit':
                    transmit_dict['sc-state'] = group['sc_state']
                elif secure_ch == 'receive':
                    recv_dict['sc-state'] = group['sc_state']
            m28 = p28.match(line)
            if m28:
                group = m28.groupdict()
                if secure_ch == 'transmit':
                    transmit_dict['elapsed-time'] = group['elapsed_time']
                elif secure_ch == 'receive':
                    recv_dict['elapsed-time'] = group['elapsed_time']
            m29 = p29.match(line)
            if m29:
                group = m29.groupdict()
                if secure_ch == 'transmit':
                    transmit_dict['start-time'] = group['start_time']
                elif secure_ch == 'receive':
                    recv_dict['start-time'] = group['start_time']
            m30 = p30.match(line)
            if m30:
                group = m30.groupdict()
                if secure_ch == 'transmit':
                    transmit_dict['current-an'] = group['current_an']
                elif secure_ch == 'receive':
                    recv_dict['current-an'] = group['current_an']

            m31 = p31.match(line)
            if m31:
                group = m31.groupdict()
                if secure_ch == 'transmit':
                    transmit_dict['previous-an'] = group['previous_an']
                elif secure_ch == 'receive':
                    recv_dict['previous-an'] = group['previous_an']
            m32 = p32.match(line)
            if m32:
                group = m32.groupdict()
                if secure_ch == 'transmit':
                     transmit_dict['next-pn'] = group['next_pn']
                elif secure_ch == 'receive':
                     recv_dict['next-pn'] = group['next_pn']
            m33 = p33.match(line)
            if m33:
                group = m33.groupdict()
                if secure_ch == 'transmit':
                    transmit_dict['sa-state'] = group['sa_state']
                elif secure_ch == 'receive':
                    recv_dict['sa-state'] = group['sa_state']
            m34 = p34.match(line)
            if m34:
                group = m34.groupdict()
                if secure_ch == 'transmit':
                     transmit_dict['confidentiality'] = group['confidentiality']
            m35 = p35.match(line)
            if m35:
                group = m35.groupdict()
                if secure_ch == 'transmit':
                   transmit_dict['sak-unchanged'] = group['sak_unchanged']
                elif secure_ch == 'receive':
                   recv_dict['sak-unchanged'] = group['sak_unchanged']
            m36 = p36.match(line)
            if m36:
                group = m36.groupdict()
                if secure_ch == 'transmit':
                     transmit_dict['sa-create-time'] = group['sa_create_time']
                elif secure_ch == 'receive':
                     recv_dict['sa-create-time'] = group['sa_create_time']
            m37 = p37.match(line)
            if m37:
                 group = m37.groupdict()
                 if secure_ch == 'transmit':
                      transmit_dict['sa-start-time'] = group['sa_start_time']
                 elif secure_ch == 'receive':
                      recv_dict['sa-start-time'] = group['sa_start_time']

            m38 = p38.match(line)
            if m38:
                sub_dict = 'sc'
                if secure_ch == 'transmit':
                    transmit_sc_dict = transmit_dict.setdefault('sc-statistics', {})
                elif secure_ch == 'receive':
                    receive_sc_dict = recv_dict.setdefault('sc-statistics', {})
            m39 = p39.match(line)
            if m39:
                group = m39.groupdict()
                if sub_dict == 'sc':
                    transmit_sc_dict['auth-only-pkts'] = group['auth_only_pkts']
                elif sub_dict == 'sa':
                    transmit_sa_dict['auth-only-pkts'] = group['auth_only_pkts']
            m40 = p40.match(line)
            if m40:
                 group = m40.groupdict()
                 if sub_dict == 'sc':
                     transmit_sc_dict['auth-only-bytes'] = group['auth_only_bytes']
                 elif sub_dict == 'sa':
                     transmit_sa_dict['auth-only-bytes'] = group['auth_only_bytes']
            m41 = p41.match(line)
            if m41:
                group = m41.groupdict()
                if sub_dict == 'sc':
                     transmit_sc_dict['encrypted-pkts'] = group['encrypted_pkts']
                elif sub_dict == 'sa':
                     transmit_sa_dict['encrypted-pkts'] = group['encrypted_pkts']
            m42 = p42.match(line)
            if m42:
                group = m42.groupdict()
                if sub_dict == 'sc':
                    transmit_sc_dict['encrypted-bytes'] = group['encrypted_bytes']
                elif sub_dict == 'sa':
                    transmit_sa_dict['encrypted-bytes'] = group['encrypted_bytes']
            m43 = p43.match(line)
            if m43:
                sub_dict = 'sa'
                if secure_ch == 'transmit':
                    transmit_sa_dict = transmit_dict.setdefault('sa-statistics', {})
                elif secure_ch == 'receive':
                    receive_sa_dict = recv_dict.setdefault('sa-statistics', {})
            m44 = p44.match(line)
            if m44:
               sub_dict = 'port'
               if secure_ch == 'transmit':
                   transmit_port_dict = transmit_dict.setdefault('port-statistics', {})
               elif secure_ch == 'receive':
                   receive_port_dict = receive_dict.setdefault('port-statistics', {})
            m45 = p45.match(line)
            if m45:
                group = m45.groupdict()
                transmit_port_dict['egress-untag-pkts'] = group['egress_untag_pkts']
            m46 = p46.match(line)
            if m46:
                group = m46.groupdict()
                transmit_port_dict['egress-long-pkts'] = group['egress_long_pkts']
            m47 = p47.match(line)
            if m47:
                receive_dict = ret_dict.setdefault('receive-secure-channels', {})
                secure_ch = 'receive'
            m48 = p48.match(line)
            if m48:
               group = m48.groupdict()
               recv_dict['rx-sa-count'] = group['rx_sa_count']

            m49 = p49.match(line)
            if m49:
                group = m49.groupdict()
                if sub_dict == 'sc':
                    receive_sc_dict['notvalid-pkts'] = group['notvalid_pkts']
                elif sub_dict == 'sa':
                    receive_sa_dict['notvalid-pkts'] = group['notvalid_pkts']
            m50 = p50.match(line)
            if m50:
                group = m50.groupdict()
                if sub_dict == 'sc':
                    receive_sc_dict['invalid-pkts'] = group['invalid_pkts']
                elif sub_dict == 'sa':
                    receive_sa_dict['invalid-pkts'] = group['invalid_pkts']
            m51 = p51.match(line)
            if m51:
                group = m51.groupdict()
                if sub_dict == 'sc':
                    receive_sc_dict['valid-pkts'] = group['valid_pkts']
                elif sub_dict == 'sa':
                    receive_sa_dict['valid-pkts'] = group['valid_pkts']
            m52 = p52.match(line)
            if m52:
                group = m52.groupdict()
                if sub_dict == 'sc':
                    receive_sc_dict['unusedsa-pkts'] = group['unusedsa_pkts']
                elif sub_dict == 'sa':
                    receive_sa_dict['unusedsa-pkts'] = group['unusedsa_pkts']
            m53 = p53.match(line)
            if m53:
                group = m53.groupdict()
                if sub_dict == 'sc':
                     receive_sc_dict['nousingsa-pkts'] = group['nousingsa_pkts']
                elif sub_dict == 'sa':
                     receive_sa_dict['nousingsa-pkts'] = group['nousingsa_pkts']
            m54 = p54.match(line)
            if m54:
                group = m54.groupdict()
                if sub_dict == 'sc':
                      receive_sc_dict['validated-bytes'] = group['validated_bytes']
                elif sub_dict == 'sa':
                     receive_sa_dict['validated-bytes'] = group['validated_bytes']
            m55 = p55.match(line)
            if m55:
               group = m55.groupdict()
               if sub_dict == 'sc':
                  receive_sc_dict['decrypted-bytes'] = group['decrypted_bytes']
               elif sub_dict == 'sa':
                  receive_sa_dict['decrypted-bytes'] = group['decrypted_bytes']
            m56 = p56.match(line)
            if m56:
                group = m56.groupdict()
                receive_sc_dict['late-pkts'] = group['late_pkts']
            m57 = p57.match(line)
            if m57:
                group = m57.groupdict()
                receive_sc_dict['uncheck-pkts'] = group['uncheck_pkts']
            m58 = p58.match(line)
            if m58:
                group = m58.groupdict()
                receive_sc_dict['delay-pkts'] = group['delay_pkts']
            m59 = p59.match(line)
            if m59:
                group = m59.groupdict()
                receive_port_dict['ingress-untag-pkts'] = group['ingress_untag_pkts']
            m60 = p60.match(line)
            if m60:
                group = m60.groupdict()
                receive_port_dict['ingress-notag-pkts'] = group['ingress_notag_pkts']
            m61 = p61.match(line)
            if m61:
                group = m61.groupdict()
                receive_port_dict['ingress-badtag-pkts'] = group['ingress_badtag_pkts']
            m62 = p62.match(line)
            if m62:
                group = m62.groupdict()
                receive_port_dict['ingress-unknownsci-pkts'] = group['ingress_unknownsci_pkts']
            m63 = p63.match(line)
            if m63:
                group = m63.groupdict()
                receive_port_dict['ingress-nosci-pkts'] = group['ingress_nosci_pkts']
            m64 = p64.match(line)
            if m64:
                 group = m64.groupdict()
                 receive_port_dict['ingress-overrun-pkts'] = group['ingress_overrun_pkts']
        return ret_dict



# ==============================================
# Parser for 'show mka summary'
# ==============================================
class ShowMkaSummarySchema(MetaParser):
    """Schema for show mka summary
    """
    schema = {
        'ca-statistics': {'group-caks-generated': int,
                   'group-caks-received': int,
                   'pairwaise-cak-rekeys': int,
                   'pairwise-caks-derived': int},
        'deleted-secured': int,
        'keepalive-timeouts': int,
        'mka-error-counters': {'ca-failures': {'ckn-derivation': int,
                                        'group-cak-decryption-unwrap': int,
                                        'group-cak-encryption-wrap': int,
                                        'group-sak-generation': int,
                                        'ick-derivation': int,
                                        'invalid-peer-macsec-capability': int,
                                        'kek-derivation': int,
                                        'pairwise-cak-derivation': int},
        'macsec-failures': {'rx-sa-installation': int,
                                            'rx-sc-creation': int,
                                            'tx-sa-installation': int,
                                            'tx-sc-creation': 0},
        'mkpdu-failures': {'mkpdu-rx-bad-peer-mn': int,
                                           'mkpdu-rx-icv-verification': int,
                                           'mkpdu-rx-nonrecent-peerlist-mn': int,
                                           'mkpdu-rx-validation': int,
                                           'mkpdu_tx': int},
        'sak-failures': {'hash-key-generation': int,
                                         'sak-cipher-mismatch': int,
                                         'sak-decryption-unwrap': int,
                                         'sak-encryption-wrap': int,
                                         'sak-generation': int},
        'session-failures': {'bringup-failures': int,
                                             'duplicate-auth-mgr-handle': int,
                                             'reauthentication-failures': int}},
        'mkpdu-statistics': {'mkpdu-received': {'distributed-cak': int,
                                         'distributed-sak': int},
                      'mkpdu-transmitted': {'distributed-cak': int,
                                            'distributed-sak': int},
                      'mkpdus-transmitted': int,
                      'mkpdus-validated-received': int},
         'reauthentication-attempts': int,
         'sa-statistics': {'sak-responses-received': int,
                   'saks-generated': int,
                   'saks-received': int,
                   'saks-rekeyed': int},
         'secured': int,
         'sessions': {
                Any(): {'ckn': str,
                  'inherited': str,
                  'interface': str,
                  'key-server': str,
                  'local-txsci': str,
                  'macsec-peers': str,
                  'peer-rxsci': str,
                  'policy-name': str,
                  'port-id': str,
                  'status': str},
         'pending-mka-sessions': int,
         'secured-mka-sessions': int,
         'total-mka-sessions': int}}


class ShowMkaSummary(ShowMkaSummarySchema):
    """Parser for 'show mka summary'
    """

    cli_command = 'show mka summary'
    def cli(self, interface=None, output=None):
        cmd = self.cli_command

        if output is None:
            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}
        p1 = re.compile('^Total MKA Sessions\.+ (?P<total_mka_sessions>\d+)$')
        p2 = re.compile('^Secured Sessions\.+ (?P<secured_mka_sessions>\d+)$')
        p3 = re.compile('^Pending Sessions\.+ (?P<pending_mka_sessions>\d+)$')
        p4 = re.compile(r'(?P<interface>\S+\/\S+) +'
                    '(?P<local_txsci>\w+\.\w+\.\w+\/\w+) +'
                    '(?P<policy_name>\S+(?: +\S+)?) +'
                    '(?P<inherited>\w+) +'
                    '(?P<key_server>\w+(?: +\w+)?)')
        p5 = re.compile(r'(?P<port_id>\d+) +'
                        '(?P<peer_rxsci>\w+\.\w+\.\w+\/\w+) +'
                        '(?P<macsec_peers>\w+) +'
                        '(?P<status>.*) '
                        '(?P<ckn>\d+)')
        p6 = re.compile('^Secured\.+ (?P<secured>\d+)$')
        p7 = re.compile('^Reauthentication Attempts\.+ (?P<reauthentication_attempts>\d+)$')
        p8 = re.compile('^Deleted \(Secured\)\.+ (?P<deleted_secured>\d+)$')
        p9 = re.compile('^Keepalive Timeouts\.+ (?P<keepalive_timeouts>\d+)$')
        p10 = re.compile('^CA Statistics$')
        p11 = re.compile('^Pairwise CAKs Derived\.+ (?P<pairwise_caks_derived>\d+)$')
        p12 = re.compile('^Pairwise CAK Rekeys\.+ (?P<pairwaise_cak_rekeys>\d+)$')
        p13 = re.compile('^Group CAKs Generated\.+ (?P<group_caks_generated>\d+)$')
        p14 = re.compile('^Group CAKs Received\.+ (?P<group_caks_received>\d+)$')
        p15 = re.compile('^SA Statistics$')
        p16 = re.compile('^SAKs Generated\.+ (?P<saks_generated>\d+)$')
        p17 = re.compile('^SAKs Rekeyed\.+ (?P<saks_rekeyed>\d+)$')
        p18 = re.compile('^SAKs Received\.+ (?P<saks_received>\d+)$')
        p19 = re.compile('^SAK Responses Received\.+ (?P<sak_responses_received>\d+)$')
        p20 = re.compile('^MKPDU Statistics$')
        p21 = re.compile('^MKPDUs Validated \& Rx\.+ (?P<mkpdus_validated>\d+)$')
        p22 = re.compile('^\"Distributed SAK\"\.+ (?P<distributed_sak>\d+)$')
        p23 = re.compile('^\"Distributed CAK\"\.+ (?P<distributed_cak>\d+)$')
        p24 = re.compile('^MKPDUs Transmitted\.+ (?P<mkpdus_transmitted>\d+)$')

        p25 = re.compile('^Bring\-up Failures\.+ (?P<bringup_failures>\d+)$')
        p26 = re.compile('^Reauthentication Failures\.+ (?P<reauthentication_failures>\d+)$')
        p27 = re.compile('^Duplicate Auth\-Mgr Handle\.+ (?P<duplicate_auth_mgr_handle>\d+)$')
        p28 = re.compile('^SAK Generation\.+ (?P<sak_generation>\d+)$')
        p29 = re.compile('^Hash Key Generation\.+ (?P<hash_key_generation>\d+)$')
        p30 = re.compile('^SAK Encryption\/Wrap\.+ (?P<sak_encryption_wrap>\d+)$')
        p31 = re.compile('^SAK Decryption\/Unwrap\.+ (?P<sak_decryption_unwrap>\d+)$')
        p32 = re.compile('^SAK Cipher Mismatch\.+ (?P<sak_cipher_mismatch>\d+)$')
        p33 = re.compile('^Group CAK Generation\.+ (?P<group_cak_generation>\d+)$')
        p34 = re.compile('^Group CAK Encryption\/Wrap\.+ (?P<group_cak_encryption_wrap>\d+)$')
        p35 = re.compile('^Group CAK Decryption\/Unwrap\.+ (?P<group_cak_decryption_unwrap>\d+)$')
        p36 = re.compile('^Pairwise CAK Derivation\.+ (?P<pairwise_cak_derivation>\d+)$')
        p37 = re.compile('^CKN Derivation\.+ (?P<ckn_derivation>\d+)$')
        p38 = re.compile('^ICK Derivation\.+ (?P<ick_derivation>\d+)$')
        p39 = re.compile('^KEK Derivation\.+ (?P<kek_derivation>\d+)$')
        p40 = re.compile('^Invalid Peer MACsec Capability\.+ (?P<invalid_peer_macsec_capability>\d+)$')

        p41 = re.compile('^Rx SC Creation\.+ (?P<rx_sc_creation>\d+)$')
        p42 = re.compile('^Tx SC Creation\.+ (?P<tx_sc_creation>\d+)$')
        p43 = re.compile('^Rx SA Installation\.+ (?P<rx_sa_installation>\d+)$')
        p44 = re.compile('^Tx SA Installation\.+ (?P<tx_sa_installation>\d+)$')
        p45 = re.compile('^MKPDU Tx\.+ (?P<mkpdu_tx>\d+)$')
        p46 = re.compile('^MKPDU Rx ICV Verification\.+ (?P<mkpdu_rx_icv_verification>\d+)$')
        p47 = re.compile('^MKPDU Rx Validation\.+ (?P<mkpdu_rx_validation>\d+)$')
        p48 = re.compile('^MKPDU Rx Bad Peer MN\.+ (?P<mkpdu_rx_bad_peer_mn>\d+)$')
        p49 = re.compile('^MKPDU Rx Non\-recent Peerlist MN\.+ (?P<mkpdu_rx_nonrecent_peerlist_mn>\d+)$')

        session_count = 0
        for line in out.splitlines():
            out_dict = ret_dict.setdefault('sessions', {})
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                out_dict['total-mka-sessions'] = int(group['total_mka_sessions'])
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                out_dict['secured-mka-sessions'] = int(group['secured_mka_sessions'])
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                out_dict['pending-mka-sessions'] = int(group['pending_mka_sessions'])
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                session_count += 1
                sess_dict = out_dict.setdefault(session_count, {})
                sess_dict['interface'] = group['interface']
                sess_dict['local-txsci'] = group['local_txsci']
                sess_dict['policy-name'] = group['policy_name']
                sess_dict['inherited'] = group['inherited']
                sess_dict['key-server'] = group['key_server']

            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                sess_dict = out_dict.setdefault(session_count, {})
                sess_dict['port-id'] = group['port_id']
                sess_dict['peer-rxsci'] = group['peer_rxsci']
                sess_dict['macsec-peers'] = group['macsec_peers']
                sess_dict['status'] = group['status'].strip()
                sess_dict['ckn'] = group['ckn']

            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                ret_dict['secured'] = int(group['secured'])
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                ret_dict['reauthentication-attempts'] = int(group['reauthentication_attempts'])
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                ret_dict['deleted-secured'] = int(group['deleted_secured'])
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                ret_dict['keepalive-timeouts'] = int(group['keepalive_timeouts'])

            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                ca_statistics = ret_dict.setdefault('ca-statistics', {})
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                ca_statistics['pairwise-caks-derived'] = int(group['pairwise_caks_derived'])
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                ca_statistics['pairwaise-cak-rekeys'] = int(group['pairwaise_cak_rekeys'])
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                ca_statistics['group-caks-generated'] = int(group['group_caks_generated'])
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                ca_statistics['group-caks-received'] = int(group['group_caks_received'])
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                sa_statistics = ret_dict.setdefault('sa-statistics', {})
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                sa_statistics['saks-generated'] = int(group['saks_generated'])
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                sa_statistics['saks-rekeyed'] = int(group['saks_rekeyed'])
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                sa_statistics['saks-received'] = int(group['saks_received'])
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                sa_statistics['sak-responses-received'] = int(group['sak_responses_received'])
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                mkpdu_statistics = ret_dict.setdefault('mkpdu-statistics', {})
            m21 = p21.match(line)
            if m21:
                group = m21.groupdict()
                mkpdu_received = mkpdu_statistics.setdefault('mkpdu-received', {})
                mkpdu = 'received'
                mkpdu_statistics['mkpdus-validated-received'] = int(group['mkpdus_validated'])
            m22 = p22.match(line)
            if m22:
                group = m22.groupdict()
                if mkpdu == 'received':
                    mkpdu_received['distributed-sak'] = int(group['distributed_sak'])
                elif mkpdu == 'transmitted':
                    mkpdu_transmitted['distributed-sak'] = int(group['distributed_sak'])
            m23 = p23.match(line)
            if m23:
                group = m23.groupdict()
                if mkpdu == 'received':
                    mkpdu_received['distributed-cak'] = int(group['distributed_cak'])
                elif mkpdu == 'transmitted':
                    mkpdu_transmitted['distributed-cak'] = int(group['distributed_cak'])
            m24 = p24.match(line)
            if m24:
                group = m24.groupdict()
                mkpdu_transmitted = mkpdu_statistics.setdefault('mkpdu-transmitted', {})
                mkpdu = 'transmitted'
                mkpdu_statistics['mkpdus-transmitted'] = int(group['mkpdus_transmitted'])

            m25 = p25.match(line)
            if m25:
                group = m25.groupdict()
                mka_error = ret_dict.setdefault('mka-error-counters', {})
                sess_fail = mka_error.setdefault('session-failures', {})
                sess_fail['bringup-failures'] = int(group['bringup_failures'])
            m26 = p26.match(line)
            if m26:
                group = m26.groupdict()
                sess_fail['reauthentication-failures'] = int(group['reauthentication_failures'])
            m27 = p27.match(line)
            if m27:
                group = m27.groupdict()
                sess_fail['duplicate-auth-mgr-handle'] = int(group['duplicate_auth_mgr_handle'])

            m28 = p28.match(line)
            if m28:
                group = m28.groupdict()
                sak_fail = mka_error.setdefault('sak-failures', {})
                sak_fail['sak-generation'] = int(group['sak_generation'])
            m29 = p29.match(line)
            if m29:
                group = m29.groupdict()
                sak_fail['hash-key-generation'] = int(group['hash_key_generation'])
            m30 = p30.match(line)
            if m30:
                group = m30.groupdict()
                sak_fail['sak-encryption-wrap'] = int(group['sak_encryption_wrap'])
            m31 = p31.match(line)
            if m31:
                group = m31.groupdict()
                sak_fail['sak-decryption-unwrap'] = int(group['sak_decryption_unwrap'])
            m32 = p32.match(line)
            if m32:
                group = m32.groupdict()
                sak_fail['sak-cipher-mismatch'] = int(group['sak_cipher_mismatch'])

            m33 = p33.match(line)
            if m33:
                group = m33.groupdict()
                ca_fail = mka_error.setdefault('ca-failures', {})
                ca_fail['group-sak-generation'] = int(group['group_cak_generation'])
            m34 = p34.match(line)
            if m34:
                group = m34.groupdict()
                ca_fail['group-cak-encryption-wrap'] = int(group['group_cak_encryption_wrap'])
            m35 = p35.match(line)
            if m35:
                group = m35.groupdict()
                ca_fail['group-cak-decryption-unwrap'] = int(group['group_cak_decryption_unwrap'])
            m36 = p36.match(line)
            if m36:
                group = m36.groupdict()
                ca_fail['pairwise-cak-derivation'] = int(group['pairwise_cak_derivation'])
            m37 = p37.match(line)
            if m37:
                group = m37.groupdict()
                ca_fail['ckn-derivation'] = int(group['ckn_derivation'])
            m38 = p38.match(line)
            if m38:
                group = m38.groupdict()
                ca_fail['ick-derivation'] = int(group['ick_derivation'])
            m39 = p39.match(line)
            if m39:
                group = m39.groupdict()
                ca_fail['kek-derivation'] = int(group['kek_derivation'])
            m40 = p40.match(line)
            if m40:
                group = m40.groupdict()
                ca_fail['invalid-peer-macsec-capability'] = int(group['invalid_peer_macsec_capability'])

            m41 = p41.match(line)
            if m41:
                group = m41.groupdict()
                macsec_fail = mka_error.setdefault('macsec-failures', {})
                macsec_fail['rx-sc-creation'] = int(group['rx_sc_creation'])
            m42 = p42.match(line)
            if m42:
                group = m42.groupdict()
                macsec_fail['tx-sc-creation'] = int(group['tx_sc_creation'])
            m43 = p43.match(line)
            if m43:
                group = m43.groupdict()
                macsec_fail['rx-sa-installation'] = int(group['rx_sa_installation'])
            m44 = p44.match(line)
            if m44:
                group = m44.groupdict()
                macsec_fail['tx-sa-installation'] = int(group['tx_sa_installation'])

            m45 = p45.match(line)
            if m45:
                group = m45.groupdict()
                mkpdu_fail = mka_error.setdefault('mkpdu-failures', {})
                mkpdu_fail['mkpdu_tx'] = int(group['mkpdu_tx'])
            m46 = p46.match(line)
            if m46:
                group = m46.groupdict()
                mkpdu_fail['mkpdu-rx-icv-verification'] = int(group['mkpdu_rx_icv_verification'])
            m47 = p47.match(line)
            if m47:
                group = m47.groupdict()
                mkpdu_fail['mkpdu-rx-validation'] = int(group['mkpdu_rx_validation'])
            m48 = p48.match(line)
            if m48:
                group = m48.groupdict()
                mkpdu_fail['mkpdu-rx-bad-peer-mn'] = int(group['mkpdu_rx_bad_peer_mn'])
            m49 = p49.match(line)
            if m49:
                group = m49.groupdict()
                mkpdu_fail['mkpdu-rx-nonrecent-peerlist-mn'] = int(group['mkpdu_rx_nonrecent_peerlist_mn'])
        return ret_dict



# ==============================================
# Parser for 'show mka statistics'
# ==============================================

''' 
Sample command output
Device#show mka statistics 

MKA Global Statistics
=====================
MKA Session Totals
   Secured.................... 3
   Fallback Secured........... 2
   Reauthentication Attempts.. 4

   Deleted (Secured).......... 2
   Keepalive Timeouts......... 0

CA Statistics
   Pairwise CAKs Derived...... 4
   Pairwise CAK Rekeys........ 4
   Group CAKs Generated....... 0
   Group CAKs Received........ 0

SA Statistics
   SAKs Generated............. 0
   SAKs Rekeyed............... 1479
   SAKs Received.............. 1480
   SAK Responses Received..... 0

MKPDU Statistics
   MKPDUs Validated & Rx...... 44937
      "Distributed SAK"..... 1480
      "Distributed CAK"..... 0
   MKPDUs Transmitted......... 91067
      "Distributed SAK"..... 0
      "Distributed CAK"..... 0

MKA Error Counter Totals
========================
Session Failures
   Bring-up Failures................ 0
   Reauthentication Failures........ 0
   Duplicate Auth-Mgr Handle........ 0

SAK Failures
   SAK Generation................... 0
   Hash Key Generation.............. 0
   SAK Encryption/Wrap.............. 0
   SAK Decryption/Unwrap............ 0
   SAK Cipher Mismatch.............. 0

CA Failures
   Group CAK Generation............. 0
   Group CAK Encryption/Wrap........ 0
   Group CAK Decryption/Unwrap...... 0
   Pairwise CAK Derivation.......... 0
   CKN Derivation................... 0
   ICK Derivation................... 0
   KEK Derivation................... 0
   Invalid Peer MACsec Capability... 0

MACsec Failures
   Rx SC Creation................... 0
   Tx SC Creation................... 0
   Rx SA Installation............... 0
   Tx SA Installation............... 0

MKPDU Failures
   MKPDU Tx............................... 0
   MKPDU Rx ICV Verification.............. 44647
   MKPDU Rx Fallback ICV Verification..... 0
   MKPDU Rx Validation.................... 0
   MKPDU Rx Bad Peer MN................... 0
   MKPDU Rx Non-recent Peerlist MN........ 0
'''


class ShowMkaStatisticsSchema(MetaParser):
    """Schema for show mka statistics
    """
    schema = {
        'mka-session-totals': {'secured': int,
                    Optional('fallback-secured'): int,
                    'reauthentication-attempts': int,
                    'deleted-secured': int,
                    'keepalive-timeouts': int},
        'ca-statistics': {'group-caks-generated': int,
                    'group-caks-received': int,
                    'pairwaise-cak-rekeys': int,
                    'pairwise-caks-derived': int},
        'mka-error-counters': {'ca-failures': {'ckn-derivation': int,
                                        'group-cak-decryption-unwrap': int,
                                        'group-cak-encryption-wrap': int,
                                        'group-sak-generation': int,
                                        'ick-derivation': int,
                                        'invalid-peer-macsec-capability': int,
                                        'kek-derivation': int,
                                        'pairwise-cak-derivation': int},
                                'macsec-failures': {'rx-sa-installation': int,
                                        'rx-sc-creation': int,
                                        'tx-sa-installation': int,
                                        'tx-sc-creation': 0},
                                'mkpdu-failures': {'mkpdu-rx-bad-peer-mn': int,
                                        'mkpdu-rx-icv-verification': int,
                                        Optional('mkpdu-rx-fallback-icv-ver'): int,
                                        'mkpdu-rx-nonrecent-peerlist-mn': int,
                                        'mkpdu-rx-validation': int,
                                        'mkpdu_tx': int},
                                'sak-failures': {'hash-key-generation': int,
                                        'sak-cipher-mismatch': int,
                                        'sak-decryption-unwrap': int,
                                        'sak-encryption-wrap': int,
                                        'sak-generation': int},
                                'session-failures': {'bringup-failures': int,
                                        'duplicate-auth-mgr-handle': int,
                                        'reauthentication-failures': int}},
        'mkpdu-statistics': {'mkpdu-received': {'distributed-cak': int,
                                          'distributed-sak': int},
                    'mkpdu-transmitted': {'distributed-cak': int,
                                          'distributed-sak': int},
                    'mkpdus-transmitted': int,
                    'mkpdus-validated-received': int},
        'sa-statistics': {'sak-responses-received': int,
                    'saks-generated': int,
                    'saks-received': int,
                    'saks-rekeyed': int}}


class ShowMkaStatistics(ShowMkaStatisticsSchema):
    """Parser for 'show mka statistics'
    """

    cli_command = 'show mka statistics'
    def cli(self, interface=None, output=None):
        cmd = self.cli_command

        if output is None:
            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}

        # MKA Session Totals
        p0 = re.compile('^MKA Session Totals$')

        #Secured.................... 3
        p1 = re.compile('^Secured\.+ (?P<secured>\d+)$')

        #Fallback Secured........... 2
        p2 = re.compile('^Fallback Secured\.+ (?P<fallback_secured>\d+)$')

        #Reauthentication Attempts.. 4
        p3 = re.compile('^Reauthentication Attempts\.+ (?P<reauthentication_attempts>\d+)$')

        #Deleted (Secured).......... 2
        p4 = re.compile('^Deleted \(Secured\)\.+ (?P<deleted_secured>\d+)$')

        #Keepalive Timeouts......... 0
        p5 = re.compile('^Keepalive Timeouts\.+ (?P<keepalive_timeouts>\d+)$')

        #CA Statistics
        p6 = re.compile('^CA Statistics$')

        #Pairwise CAKs Derived...... 4
        p7 = re.compile('^Pairwise CAKs Derived\.+ (?P<pairwise_caks_derived>\d+)$')

        #Pairwise CAK Rekeys........ 4
        p8 = re.compile('^Pairwise CAK Rekeys\.+ (?P<pairwaise_cak_rekeys>\d+)$')

        #Group CAKs Generated....... 0
        p9 = re.compile('^Group CAKs Generated\.+ (?P<group_caks_generated>\d+)$')

        #Group CAKs Received........ 0
        p10 = re.compile('^Group CAKs Received\.+ (?P<group_caks_received>\d+)$')

        #SA Statistics
        p11 = re.compile('^SA Statistics$')

        #SAKs Generated............. 0
        p12 = re.compile('^SAKs Generated\.+ (?P<saks_generated>\d+)$')

        #SAKs Rekeyed............... 1479
        p13 = re.compile('^SAKs Rekeyed\.+ (?P<saks_rekeyed>\d+)$')

        #SAKs Received.............. 1480
        p14 = re.compile('^SAKs Received\.+ (?P<saks_received>\d+)$')

        #SAK Responses Received..... 0
        p15 = re.compile('^SAK Responses Received\.+ (?P<sak_responses_received>\d+)$')

        #MKPDU Statistics
        p16 = re.compile('^MKPDU Statistics$')

        #MKPDUs Validated & Rx...... 44937
        p17 = re.compile('^MKPDUs Validated \& Rx\.+ (?P<mkpdus_validated>\d+)$')

        #"Distributed SAK"..... 1480
        p18 = re.compile('^\"Distributed SAK\"\.+ (?P<distributed_sak>\d+)$')

        #"Distributed CAK"..... 0
        p19 = re.compile('^\"Distributed CAK\"\.+ (?P<distributed_cak>\d+)$')

        #MKPDUs Transmitted......... 91067
        p20 = re.compile('^MKPDUs Transmitted\.+ (?P<mkpdus_transmitted>\d+)$')

        #Bring-up Failures................ 0
        p21 = re.compile('^Bring\-up Failures\.+ (?P<bringup_failures>\d+)$')

        #Reauthentication Failures........ 0
        p22 = re.compile('^Reauthentication Failures\.+ (?P<reauthentication_failures>\d+)$')

        #Duplicate Auth-Mgr Handle........ 0
        p23 = re.compile('^Duplicate Auth\-Mgr Handle\.+ (?P<duplicate_auth_mgr_handle>\d+)$')

        #SAK Generation................... 0
        p24 = re.compile('^SAK Generation\.+ (?P<sak_generation>\d+)$')

        #Hash Key Generation.............. 0
        p25 = re.compile('^Hash Key Generation\.+ (?P<hash_key_generation>\d+)$')

        #SAK Encryption/Wrap.............. 0
        p26 = re.compile('^SAK Encryption\/Wrap\.+ (?P<sak_encryption_wrap>\d+)$')

        #SAK Decryption/Unwrap............ 0
        p27 = re.compile('^SAK Decryption\/Unwrap\.+ (?P<sak_decryption_unwrap>\d+)$')

        #SAK Cipher Mismatch.............. 0
        p28 = re.compile('^SAK Cipher Mismatch\.+ (?P<sak_cipher_mismatch>\d+)$')

        #Group CAK Generation............. 0
        p29 = re.compile('^Group CAK Generation\.+ (?P<group_cak_generation>\d+)$')

        #Group CAK Encryption/Wrap........ 0
        p30 = re.compile('^Group CAK Encryption\/Wrap\.+ (?P<group_cak_encryption_wrap>\d+)$')

        #Group CAK Decryption/Unwrap...... 0
        p31 = re.compile('^Group CAK Decryption\/Unwrap\.+ (?P<group_cak_decryption_unwrap>\d+)$')
        
        #Pairwise CAK Derivation.......... 0
        p32 = re.compile('^Pairwise CAK Derivation\.+ (?P<pairwise_cak_derivation>\d+)$')

        #CKN Derivation................... 0
        p33 = re.compile('^CKN Derivation\.+ (?P<ckn_derivation>\d+)$')

        #ICK Derivation................... 0
        p34 = re.compile('^ICK Derivation\.+ (?P<ick_derivation>\d+)$')

        #KEK Derivation................... 0
        p35 = re.compile('^KEK Derivation\.+ (?P<kek_derivation>\d+)$')

        #Invalid Peer MACsec Capability... 0
        p36 = re.compile('^Invalid Peer MACsec Capability\.+ (?P<invalid_peer_macsec_capability>\d+)$')

        #Rx SC Creation................... 0
        p37 = re.compile('^Rx SC Creation\.+ (?P<rx_sc_creation>\d+)$')

        #Tx SC Creation................... 0
        p38 = re.compile('^Tx SC Creation\.+ (?P<tx_sc_creation>\d+)$')

        #Rx SA Installation............... 0
        p39 = re.compile('^Rx SA Installation\.+ (?P<rx_sa_installation>\d+)$')

        #Tx SA Installation............... 0
        p40 = re.compile('^Tx SA Installation\.+ (?P<tx_sa_installation>\d+)$')

        #MKPDU Tx............................... 0
        p41 = re.compile('^MKPDU Tx\.+ (?P<mkpdu_tx>\d+)$')

        #MKPDU Rx ICV Verification.............. 44647
        p42 = re.compile('^MKPDU Rx ICV Verification\.+ (?P<mkpdu_rx_icv_verification>\d+)$')

        #MKPDU Rx Fallback ICV Verification..... 0
        p43 = re.compile('^MKPDU Rx Fallback ICV Verification\.+ (?P<mkpdu_rx_icv_fallback_ver>\d+)$')
        
        #MKPDU Rx Validation.................... 0
        p44 = re.compile('^MKPDU Rx Validation\.+ (?P<mkpdu_rx_validation>\d+)$')
        
        #MKPDU Rx Bad Peer MN................... 0
        p45 = re.compile('^MKPDU Rx Bad Peer MN\.+ (?P<mkpdu_rx_bad_peer_mn>\d+)$')

        #MKPDU Rx Non-recent Peerlist MN........ 0
        p46 = re.compile('^MKPDU Rx Non\-recent Peerlist MN\.+ (?P<mkpdu_rx_nonrecent_peerlist_mn>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            m0 = p0.match(line)
            if m0:
                group = m0.groupdict()
                mka_session_totals = ret_dict.setdefault('mka-session-totals', {})
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                mka_session_totals['secured'] = int(group['secured'])
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                mka_session_totals['fallback-secured'] = int(group['fallback_secured'])
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                mka_session_totals['reauthentication-attempts'] = int(group['reauthentication_attempts'])
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                mka_session_totals['deleted-secured'] = int(group['deleted_secured'])
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                mka_session_totals['keepalive-timeouts'] = int(group['keepalive_timeouts'])

            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                ca_statistics = ret_dict.setdefault('ca-statistics', {})
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                ca_statistics['pairwise-caks-derived'] = int(group['pairwise_caks_derived'])
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                ca_statistics['pairwaise-cak-rekeys'] = int(group['pairwaise_cak_rekeys'])
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                ca_statistics['group-caks-generated'] = int(group['group_caks_generated'])
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                ca_statistics['group-caks-received'] = int(group['group_caks_received'])
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                sa_statistics = ret_dict.setdefault('sa-statistics', {})
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                sa_statistics['saks-generated'] = int(group['saks_generated'])
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                sa_statistics['saks-rekeyed'] = int(group['saks_rekeyed'])
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                sa_statistics['saks-received'] = int(group['saks_received'])
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                sa_statistics['sak-responses-received'] = int(group['sak_responses_received'])
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                mkpdu_statistics = ret_dict.setdefault('mkpdu-statistics', {})
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                mkpdu_received = mkpdu_statistics.setdefault('mkpdu-received', {})
                mkpdu = 'received'
                mkpdu_statistics['mkpdus-validated-received'] = int(group['mkpdus_validated'])
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                if mkpdu == 'received':
                    mkpdu_received['distributed-sak'] = int(group['distributed_sak'])
                elif mkpdu == 'transmitted':
                    mkpdu_transmitted['distributed-sak'] = int(group['distributed_sak'])
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                if mkpdu == 'received':
                    mkpdu_received['distributed-cak'] = int(group['distributed_cak'])
                elif mkpdu == 'transmitted':
                    mkpdu_transmitted['distributed-cak'] = int(group['distributed_cak'])
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                mkpdu_transmitted = mkpdu_statistics.setdefault('mkpdu-transmitted', {})
                mkpdu = 'transmitted'
                mkpdu_statistics['mkpdus-transmitted'] = int(group['mkpdus_transmitted'])

            m21 = p21.match(line)
            if m21:
                group = m21.groupdict()
                mka_error = ret_dict.setdefault('mka-error-counters', {})
                sess_fail = mka_error.setdefault('session-failures', {})
                sess_fail['bringup-failures'] = int(group['bringup_failures'])
            m22 = p22.match(line)
            if m22:
                group = m22.groupdict()
                sess_fail['reauthentication-failures'] = int(group['reauthentication_failures'])
            m23 = p23.match(line)
            if m23:
                group = m23.groupdict()
                sess_fail['duplicate-auth-mgr-handle'] = int(group['duplicate_auth_mgr_handle'])

            m24 = p24.match(line)
            if m24:
                group = m24.groupdict()
                sak_fail = mka_error.setdefault('sak-failures', {})
                sak_fail['sak-generation'] = int(group['sak_generation'])
            m25 = p25.match(line)
            if m25:
                group = m25.groupdict()
                sak_fail['hash-key-generation'] = int(group['hash_key_generation'])
            m26 = p26.match(line)
            if m26:
                group = m26.groupdict()
                sak_fail['sak-encryption-wrap'] = int(group['sak_encryption_wrap'])
            m27 = p27.match(line)
            if m27:
                group = m27.groupdict()
                sak_fail['sak-decryption-unwrap'] = int(group['sak_decryption_unwrap'])
            m28 = p28.match(line)
            if m28:
                group = m28.groupdict()
                sak_fail['sak-cipher-mismatch'] = int(group['sak_cipher_mismatch'])

            m29 = p29.match(line)
            if m29:
                group = m29.groupdict()
                ca_fail = mka_error.setdefault('ca-failures', {})
                ca_fail['group-sak-generation'] = int(group['group_cak_generation'])
            m30 = p30.match(line)
            if m30:
                group = m30.groupdict()
                ca_fail['group-cak-encryption-wrap'] = int(group['group_cak_encryption_wrap'])
            m31 = p31.match(line)
            if m31:
                group = m31.groupdict()
                ca_fail['group-cak-decryption-unwrap'] = int(group['group_cak_decryption_unwrap'])
            m32 = p32.match(line)
            if m32:
                group = m32.groupdict()
                ca_fail['pairwise-cak-derivation'] = int(group['pairwise_cak_derivation'])
            m33 = p33.match(line)
            if m33:
                group = m33.groupdict()
                ca_fail['ckn-derivation'] = int(group['ckn_derivation'])
            m34 = p34.match(line)
            if m34:
                group = m34.groupdict()
                ca_fail['ick-derivation'] = int(group['ick_derivation'])
            m35 = p35.match(line)
            if m35:
                group = m35.groupdict()
                ca_fail['kek-derivation'] = int(group['kek_derivation'])
            m36 = p36.match(line)
            if m36:
                group = m36.groupdict()
                ca_fail['invalid-peer-macsec-capability'] = int(group['invalid_peer_macsec_capability'])

            m37 = p37.match(line)
            if m37:
                group = m37.groupdict()
                macsec_fail = mka_error.setdefault('macsec-failures', {})
                macsec_fail['rx-sc-creation'] = int(group['rx_sc_creation'])
            m38 = p38.match(line)
            if m38:
                group = m38.groupdict()
                macsec_fail['tx-sc-creation'] = int(group['tx_sc_creation'])
            m39 = p39.match(line)
            if m39:
                group = m39.groupdict()
                macsec_fail['rx-sa-installation'] = int(group['rx_sa_installation'])
            m40 = p40.match(line)
            if m40:
                group = m40.groupdict()
                macsec_fail['tx-sa-installation'] = int(group['tx_sa_installation'])

            m41 = p41.match(line)
            if m41:
                group = m41.groupdict()
                mkpdu_fail = mka_error.setdefault('mkpdu-failures', {})
                mkpdu_fail['mkpdu_tx'] = int(group['mkpdu_tx'])
            m42 = p42.match(line)
            if m42:
                group = m42.groupdict()
                mkpdu_fail['mkpdu-rx-icv-verification'] = int(group['mkpdu_rx_icv_verification'])
            m43 = p43.match(line)
            if m43:
                group = m43.groupdict()
                mkpdu_fail['mkpdu-rx-fallback-icv-ver'] = int(group['mkpdu_rx_icv_fallback_ver'])
            m44 = p44.match(line)
            if m44:
                group = m44.groupdict()
                mkpdu_fail['mkpdu-rx-validation'] = int(group['mkpdu_rx_validation'])
            m45 = p45.match(line)
            if m45:
                group = m45.groupdict()
                mkpdu_fail['mkpdu-rx-bad-peer-mn'] = int(group['mkpdu_rx_bad_peer_mn'])
            m46 = p46.match(line)
            if m46:
                group = m46.groupdict()
                mkpdu_fail['mkpdu-rx-nonrecent-peerlist-mn'] = int(group['mkpdu_rx_nonrecent_peerlist_mn'])
        return ret_dict
