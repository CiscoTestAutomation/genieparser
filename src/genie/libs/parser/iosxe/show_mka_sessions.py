''' show_mka_sessions.py

IOSXE parsers for the following show commands:
    * show mka sessions
    * show mka sessions interface {interface}
    * show mka sessions interface {interface} detail

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
            Any(): {
                'Interface': str,
                'Local-TxSCI': str,
                'Policy-Name': str,
                'Inherited': str,
                'Key-Server': str,
                'Port-ID': str,
                'Peer-RxSCI': str,
                'MACsec-Peers': str,
                'Status': str,
                'CKN': str
            },
        Optional('Total MKA Sessions'): int,
        Optional('Secured MKA Sessions'): int,
        Optional('Pending MKA Sessions'): int
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
        out=out.replace('\r','')
        # initial return dictionary
        ret_dict = {}
        p1 = re.compile('Total MKA Sessions....... (.*)')
        p2 = re.compile('Secured Sessions... (.*)')
        p3 = re.compile('Pending Sessions... (.*)')

        if p1.search(out):
            ret_dict.update({'Total MKA Sessions': int(p1.search(out).group(1))})
        if p2.search(out):
            ret_dict.update({'Secured MKA Sessions': int(p2.search(out).group(1))})
        if p3.search(out):
            ret_dict.update({'Pending MKA Sessions': int(p3.search(out).group(1))})
        # Matching patterns
        #Hu2/6/0/39     70b3.171e.b282/0103 *DEFAULT POLICY* NO                NO
        #259            00a7.42ce.d57f/0074 1                Secured           10 
        p4 = re.compile(r'(\S+\/\S+) +'
                        '(\w+\.\w+\.\w+\/\w+) +'
                        '(\S+(?: +\S+)?) +'
                        '(\w+) +'
                        '(\w+(?: +\w+)?) +\n'
                        '(\w+) +'
                        '(\w+\.\w+\.\w+\/\w+) +'
                        '(\w+) +'
                        '(\w+) +'
                        '(\w+)',re.MULTILINE)

        sess=p1.search(out)
        if sess==None or int(sess.group(1)) != 0:
            i = 1
            for line in p4.findall(out):
                 #Hu2/6/0/39     70b3.171e.b282/0103 *DEFAULT POLICY* NO                NO
                 #259            00a7.42ce.d57f/0074 1                Secured           10
                 dict_temp = {}
                 dict_temp['Interface'] = line[0]
                 dict_temp['Local-TxSCI'] = line[1]
                 dict_temp['Policy-Name'] = line[2]
                 dict_temp['Inherited'] = line[3]  
                 dict_temp['Key-Server'] = line[4]
                 dict_temp['Port-ID'] = line[5]
                 dict_temp['Peer-RxSCI'] = line[6]
                 dict_temp['MACsec-Peers'] = line[7]
                 dict_temp['Status'] = line[8]
                 dict_temp['CKN'] = line[9]
                 ret_dict['Session-%s'%i] = dict_temp
                 i+=1
        return ret_dict


# ==================================================================================
# Parser for 'show mka sessions interface {interface} detail'
# ==================================================================================
class ShowMkaSessionsInterfaceDetailsSchema(MetaParser):
    """Schema for 'show mka sessions interface {interface} detail'
    """
    schema = {
               'Local Tx-SCI': str,
               'Interface MAC Address': str,
               'MKA Port Identifier': str,
               'Interface Name': str,
               'Audit Session ID': str,
               'CAK Name (CKN)': str,
               'Member Identifier (MI)': str,
               'Message Number (MN)': str,
               'EAP Role': str,
               'Key Server': str,
               'MKA Cipher Suite': str,
               'Latest SAK Status': str,
               'Latest SAK AN': str,
               'Latest SAK KI (KN)': str,
               'Old SAK Status': str,
               'Old SAK AN': str,
               'Old SAK KI (KN)': str,
               'SAK Transmit Wait Time': str,
               'SAK Retire Time': str,
               'SAK Rekey Time': str,
               'MKA Policy Name': str,
               'Key Server Priority': str,
               'Delay Protection': str,
               'Delay Protection Timer': str,
               'Confidentiality Offset': str,
               'Algorithm Agility': str,
               'SAK Rekey On Live Peer Loss': str,
               'Send Secure Announcement': str,
               'SCI Based SSCI Computation': str,
               'SAK Cipher Suite': str,
               'MACsec Capability': str,
               'MACsec Desired': str,
               '# of MACsec Capable Live Peers': str,
               '# of MACsec Capable Live Peers Responded': str,
        
               'Live_peers_dict' : {
                                 Any(): {
                                    'MI': str,
                                    'MN': str,
                                    'Rx-SCI (Peer)': str,
                                    'KS Priority': str,
                                    'RxSA Installed': str,
                                    'SSCI': str
                                 }
               },
               'Potential_peers_dict' : {
                                 Any(): {
                                    'MI': str,
                                    'MN': str,
                                    'Rx-SCI (Peer)': str,
                                    'KS Priority': str,
                                    'RxSA Installed': str,
                                    'SSCI': str
                                 }
                },
                'Dormant_peers_dict' : {
                                 Any(): {
                                    'MI': str,
                                    'MN': str,
                                    'Rx-SCI (Peer)': str,
                                    'KS Priority': str,
                                    'RxSA Installed': str,
                                    'SSCI': str
                                 }
                }
    }


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
        for line in out.splitlines():
            elem=line.split('..')
            if len(elem) > 1:
                if elem[-1] == ' ' or  elem[-1] == '.' or  elem[-1] == '. ':
                    ret_dict[elem[0]] = ''
                else:
                    ret_dict[elem[0]] = elem[-1].strip().strip('. ')


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

        start1 = out.find("Live Peers List") + len("Live Peers List")
        end1 = out.find("Potential Peers List:")
        peer_out = out[start1:end1]

        start2 = out.find("Potential Peers List") + len("Potential Peers List")
        end2 = out.find("Dormant Peers List:")
        potential_out = out[start2:end2]

        start3 = out.find("Dormant Peers List") + len("Dormant Peers List")
        dormant_out = out[start3:]

        p1 = re.compile(r'(\S+) +'
                '(\S+) +'
                '(\w+\.\w+\.\w+\/\w+) +'
                '(\w+) +'
                '(\w+) +'
                '(\w+)',re.MULTILINE)

        i=1
        live_peers_dict = {}
        for line in p1.findall(peer_out):
            peer_dict={}
            peer_dict['MI'] = line[0]
            peer_dict['MN'] = line[1]
            peer_dict['Rx-SCI (Peer)'] = line[2]
            peer_dict['KS Priority'] = line[3]
            peer_dict['RxSA Installed'] = line[4]
            peer_dict['SSCI'] = line[5]
            live_peers_dict['Session-%s'%i] = peer_dict
            i+=1

        i=1
        potential_peers_dict = {}
        for line in p1.findall(potential_out):
            potential_dict={}
            potential_dict['MI'] = line[0]
            potential_dict['MN'] = line[1]
            potential_dict['Rx-SCI (Peer)'] = line[2]
            potential_dict['KS Priority'] = line[3]
            potential_dict['RxSA Installed'] = line[4]
            potential_dict['SSCI'] = line[5]
            potential_peers_dict['Session-%s'%i] = potential_dict
            i+=1

        i=1
        dormant_peers_dict = {}
        for line in p1.findall(dormant_out):
            dormant_dict={}
            dormant_dict['MI'] = line[0]
            dormant_dict['MN'] = line[1]
            dormant_dict['Rx-SCI (Peer)'] = line[2]
            dormant_dict['KS Priority'] = line[3]
            dormant_dict['RxSA Installed'] = line[4]
            dormant_dict['SSCI'] = line[5]
            dormant_peers_dict['Session-%s'%i] = dormant_dict
            i+=1

        if len(live_peers_dict) == 0 and len(potential_peers_dict) == 0 and len(dormant_peers_dict) == 0:
            pass
        else:
            ret_dict['Live_peers_dict'] = live_peers_dict
            ret_dict['Potential_peers_dict'] = potential_peers_dict
            ret_dict['Dormant_peers_dict'] = dormant_peers_dict
        return ret_dict


# ==============================================
# Parser for 'show macsec interface <interface>'
# ==============================================
class ShowMacsecInterfaceSchema(MetaParser):
    """Schema for show macsec interface <interface>
    """
    schema = {
        'Macsec_Data': {
                 'Admin_Pt2Pt_MAC': str,
                 'Cipher': str,
                 'Confidentiality_Offset': str,
                 'Include_SCI': str,
                 'Macsec_status': str,
                 'Pt2Pt_MAC_Operational': str,
                 'Replay_protect_status': str,
                 'Replay_window': str,
                 'Use_ES_Enable': str,
                 'Use_SCB_Enable': str
                       },
        'Capabilities': {
                  'Data_length_change_supported': str,
                  'ICV_length': str,
                  'Max_Rx_SA': str,
                  'Max_Rx_SC': str,
                  'Max_Tx_SA': str,
                  'Max_Tx_SC': str,
                  'PN_threshold_notification_support': str,
                  'Validate_Frames': str,
                  'Ciphers_supported': list
                        },
        'Access_control': str,
         Optional('Cleartag_details'): {
             'Type': str,
             'VlanId1': str
                            },
         Optional('Transmit_Secure_Channels'): {
                              'Confidentiality': str,
                              'Current_AN': str,
                              'Elapsed_time': str,
                              'Next_PN': str,
                              'Previous_AN': str,
                              'SAK_Unchanged': str,
                              'SA_Create_time': str,
                              'SA_Start_time': str,
                              'SA_State': str,
                              'SCI': str,
                              'SC_state': str,
                              'Start_time': str,
                              'SA_Statistics': {
                                                'Auth_only_Bytes': str,
                                                'Auth_only_Pkts': str,
                                                'Encrypted_Bytes': str,
                                                'Encrypted_Pkts': str
                                               },
                              'SC_Statistics': {'Auth_only_Bytes': str,
                                                'Auth_only_Pkts': str,
                                                'Encrypted_Bytes': str,
                                                'Encrypted_Pkts': str
                                               },
                              'Port_Statistics': {'Egress_long_pkts': str,
                                                  'Egress_untag_pkts': str
                                               }
                                     },
         Optional('Receive_Secure_Channels'): {'Current_AN': str,
                             'Elapsed_time': str,
                             'Next_PN': str,
                             'SC_state': str,
                             'Start_time': str,
                             'Port_Statistics': {'Ingress_badtag_pkts': str,
                                                 'Ingress_noSCI_pkts': str,
                                                 'Ingress_notag_pkts': str,
                                                 'Ingress_overrun_pkts': str,
                                                 'Ingress_unknownSCI_pkts': str,
                                                 'Ingress_untag_pkts': str},
                             'Previous_AN': str,
                             'RX_SA_Count': str,
                             'SAK_Unchanged': str,
                             'SA_Create_time': str,
                             'SA_Start_time': str,
                             'SA_State': str,
                             'SA_Statistics': {'Decrypted_Bytes': str,
                                               'Invalid_pkts': str,
                                               'Notvalid_pkts': str,
                                               'NousingSA_pkts': str,
                                               'UnusedSA_pkts': str,
                                               'Valid_pkts': str,
                                               'Validated_Bytes': str},
                             'SCI': str,
                             'SC_Statistics': {'Decrypted_Bytes': str,
                                               'Delay_pkts': str,
                                               'Invalid_pkts': str,
                                               'Late_pkts': str,
                                               'Notvalid_pkts': str,
                                               'NousingSA_pkts': str,
                                               'Uncheck_pkts': str,
                                               'UnusedSA_pkts': str,
                                               'Valid_pkts': str,
                                               'Validated_Bytes': str}
                                        }
                     }


class ShowMacsecInterface(ShowMacsecInterfaceSchema):
    'Parser for show macsec interface <interface>'

    cli_command = 'show macsec interface {interface}'
    def cli(self, interface=None, output=None):

        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        ret_dict={}
        out=out.replace('\r','')
        '''
        MACsec is enabled
        Replay protect : enabled
        Replay window : 0
        Include SCI : yes
        Use ES Enable : no
        Use SCB Enable : no
        Admin Pt2Pt MAC : forceTrue(1)
        Pt2Pt MAC Operational : no
        Cipher : GCM-AES-256
        Confidentiality Offset : 30
        '''
        p1 = re.compile(r'MACsec is +(?P<Macsec_status>\w+)\n'
                r' +Replay protect : +(?P<Replay_protect_status>\w+)\n'
                r' +Replay window : +(?P<Replay_window>\w+)\n'
                r' +Include SCI : +(?P<Include_SCI>\w+)\n'
                r' +Use ES Enable : +(?P<Use_ES_Enable>\w+)\n'
                r' +Use SCB Enable : +(?P<Use_SCB_Enable>\w+)\n'
                r' +Admin Pt2Pt MAC : +(?P<Admin_Pt2Pt_MAC>\S+)\n'
                r' +Pt2Pt MAC Operational : +(?P<Pt2Pt_MAC_Operational>\w+)\n'
                r' +Cipher : +(?P<Cipher>\S+)\n'
                r' +Confidentiality Offset : +(?P<Confidentiality_Offset>\w+)\n', re.MULTILINE)
        m1 = p1.search(out)
        if m1:
            group1 = m1.groupdict()
            macsec_values = {}
            macsec_values['Macsec_status'] = group1['Macsec_status']
            macsec_values['Replay_protect_status'] = group1['Replay_protect_status']
            macsec_values['Replay_window'] = group1['Replay_window']
            macsec_values['Include_SCI'] = group1['Include_SCI']
            macsec_values['Use_ES_Enable'] = group1['Use_ES_Enable']
            macsec_values['Use_SCB_Enable'] = group1['Use_SCB_Enable']
            macsec_values['Admin_Pt2Pt_MAC'] = group1['Admin_Pt2Pt_MAC']
            macsec_values['Pt2Pt_MAC_Operational'] = group1['Pt2Pt_MAC_Operational']
            macsec_values['Cipher'] = group1['Cipher']
            macsec_values['Confidentiality_Offset'] = group1['Confidentiality_Offset']
            ret_dict['Macsec_Data'] = macsec_values

        '''
    Capabilities
    ICV length : 16
    Data length change supported: yes
    Max. Rx SA : 16
    Max. Tx SA : 16
    Max. Rx SC : 8
    Max. Tx SC : 8
    Validate Frames : strict
    PN threshold notification support : Yes
        '''
        p2 = re.compile(r'Capabilities\n'
                r' +ICV length : +(?P<ICV_length>\w+)\n'
                r' +Data length change supported: +(?P<Data_length_change_supported>\w+)\n'
                r' +Max. Rx SA : +(?P<Max_Rx_SA>\w+)\n'
                r' +Max. Tx SA : +(?P<Max_Tx_SA>\w+)\n'
                r' +Max. Rx SC : +(?P<Max_Rx_SC>\w+)\n'
                r' +Max. Tx SC : +(?P<Max_Tx_SC>\w+)\n'
                r' +Validate Frames : +(?P<Validate_Frames>\w+)\n'
                r' +PN threshold notification support : +(?P<PN_threshold_notification_support>\w+)\n', re.MULTILINE)
        m2 = p2.search(out)
        capabilities_values = {}
        if m2:
            group2 = m2.groupdict()
            capabilities_values['ICV_length'] = group2['ICV_length']
            capabilities_values['Data_length_change_supported'] = group2['Data_length_change_supported']
            capabilities_values['Max_Rx_SA'] = group2['Max_Rx_SA']
            capabilities_values['Max_Tx_SA'] = group2['Max_Tx_SA']
            capabilities_values['Max_Rx_SC'] = group2['Max_Rx_SC']
            capabilities_values['Max_Tx_SC'] = group2['Max_Tx_SC']
            capabilities_values['Validate_Frames'] = group2['Validate_Frames']
            capabilities_values['PN_threshold_notification_support'] = group2['PN_threshold_notification_support']

        '''
        Ciphers supported : GCM-AES-128
                      GCM-AES-256
                      GCM-AES-XPN-128
                      GCM-AES-XPN-256
        '''
        start1 = out.find("Ciphers supported : ") + len("Ciphers supported : ")
        end1 = out.find("Access control ")
        ciphers_out = out[start1:end1]
        ciphers_list =[]
        for elem in ciphers_out.splitlines():
            if elem != '' and elem != ' ':
                ciphers_list.append(elem.strip())
        capabilities_values['Ciphers_supported'] = ciphers_list
        ret_dict['Capabilities'] = capabilities_values

        #Access control : must secure
        p3 = re.search('Access control : (.*)', out)
        ret_dict['Access_control'] = p3.group(1)

        '''
        Cleartag Details
        Type    : one dot1q in clear
        VlanId1 : 5
        '''
        p4 = re.compile(r'Cleartag Details\n'
                 r' +Type    : (?P<Type>(.*))\n'
                 r' +VlanId1 : +(?P<VlanId1>\w+)\n', re.MULTILINE)
        m4 = p4.search(out)
        if m4:
            group4 = m4.groupdict()
            cleartag_values = {}
            cleartag_values['Type'] = group4['Type']
            cleartag_values['VlanId1'] = group4['VlanId1']
            ret_dict['Cleartag_details'] = cleartag_values

        '''
    Transmit Secure Channels
  SCI : F87A41252702008C
  SC state : inUse(1)
   Elapsed time : 7w0d
   Start time : 7w0d
   Current AN: 3
   Previous AN: 2
   Next PN: 874
   SA State: inUse(1)
   Confidentiality : yes
   SAK Unchanged : no
   SA Create time : 07:51:09
   SA Start time : 7w0d
   SC Statistics
    Auth-only Pkts : 0
    Auth-only Bytes : 0
    Encrypted Pkts : 1776012104
    Encrypted Bytes : 15955677638612
   SA Statistics
    Auth-only Pkts : 0
    Auth-only Bytes : 0
    Encrypted Pkts : 873
    Encrypted Bytes : 123706

  Port Statistics
   Egress untag pkts  0
   Egress long pkts  0
       '''

        if 'No Transmit Secure Channels' not in out:
            transmit_ch = {}
            p5 = re.compile(r'Transmit Secure Channels\n'
                    r' +SCI : +(?P<SCI>\w+)\n'
                    r' +SC state : +(?P<SC_state>\S+)\n'
                    r' +Elapsed time : +(?P<Elapsed_time>\w+)\n'
                    r' +Start time : +(?P<Start_time>\w+)\n'
                    r' +Current AN: +(?P<Current_AN>\w+)\n'
                    r' +Previous AN: +(?P<Previous_AN>\S+)\n'
                    r' +Next PN: +(?P<Next_PN>\w+)\n'
                    r' +SA State: +(?P<SA_State>\S+)\n'
                    r' +Confidentiality : +(?P<Confidentiality>\w+)\n'
                    r' +SAK Unchanged : +(?P<SAK_Unchanged>\w+)\n'
                    r' +SA Create time : +(?P<SA_Create_time>\S+)\n'
                    r' +SA Start time : +(?P<SA_Start_time>\w+)\n', re.MULTILINE)
            p6 = re.compile(r'SC Statistics\n'
                    r' +Auth-only Pkts : +(?P<Auth_only_Pkts>\w+)\n'
                    r' +Auth-only Bytes : +(?P<Auth_only_Bytes>\w+)\n'
                    r' +Encrypted Pkts : +(?P<Encrypted_Pkts>\w+)\n'
                    r' +Encrypted Bytes : +(?P<Encrypted_Bytes>\w+)\n', re.MULTILINE)
            p7 = re.compile(r'SA Statistics\n'
                    r' +Auth-only Pkts : +(?P<Auth_only_Pkts>\w+)\n'
                    r' +Auth-only Bytes : +(?P<Auth_only_Bytes>\w+)\n'
                    r' +Encrypted Pkts : +(?P<Encrypted_Pkts>\w+)\n'
                    r' +Encrypted Bytes : +(?P<Encrypted_Bytes>\w+)\n', re.MULTILINE)
            p8 = re.compile(r'Port Statistics\n'
                    r' +Egress untag pkts  +(?P<Egress_untag_pkts>\w+)\n'
                    r' +Egress long pkts  +(?P<Egress_long_pkts>\w+)\n', re.MULTILINE)
            m5 = p5.search(out)
            if m5:
                group5 = m5.groupdict()
                transmit_ch['SCI'] = group5['SCI']
                transmit_ch['SC_state'] = group5['SC_state']
                transmit_ch['Elapsed_time'] = group5['Elapsed_time']
                transmit_ch['Start_time'] = group5['Start_time']
                transmit_ch['Current_AN'] = group5['Current_AN']
                transmit_ch['Previous_AN'] = group5['Previous_AN']
                transmit_ch['Next_PN'] = group5['Next_PN']
                transmit_ch['SA_State'] = group5['SA_State']
                transmit_ch['Confidentiality'] = group5['Confidentiality']
                transmit_ch['SAK_Unchanged'] = group5['SAK_Unchanged']
                transmit_ch['SA_Create_time'] = group5['SA_Create_time']
                transmit_ch['SA_Start_time'] = group5['SA_Start_time']

            m6 = p6.search(out)
            if m6:
                group6 = m6.groupdict()
                transmit_sc = {}
                transmit_sc['Auth_only_Pkts'] = group6['Auth_only_Pkts']
                transmit_sc['Auth_only_Bytes'] = group6['Auth_only_Bytes']
                transmit_sc['Encrypted_Pkts'] = group6['Encrypted_Pkts']
                transmit_sc['Encrypted_Bytes'] = group6['Encrypted_Bytes']
                transmit_ch['SC_Statistics'] = transmit_sc
            m7 = p7.search(out)
            if m7:
                group7 = m7.groupdict()
                transmit_sa = {}
                transmit_sa['Auth_only_Pkts'] = group7['Auth_only_Pkts']
                transmit_sa['Auth_only_Bytes'] = group7['Auth_only_Bytes']
                transmit_sa['Encrypted_Pkts'] = group7['Encrypted_Pkts']
                transmit_sa['Encrypted_Bytes'] = group7['Encrypted_Bytes']
                transmit_ch['SA_Statistics'] = transmit_sa
            m8 = p8.search(out)
            if m8:
                group8 = m8.groupdict()
                transmit_port = {}
                transmit_port['Egress_untag_pkts'] = group8['Egress_untag_pkts']
                transmit_port['Egress_long_pkts'] = group8['Egress_long_pkts']
                transmit_ch['Port_Statistics'] = transmit_port
            ret_dict['Transmit_Secure_Channels'] = transmit_ch

        '''
    Receive Secure Channels
  SCI : ECCE1346F902008C
  SC state : inUse(1)
   Elapsed time : 7w0d
   Start time : 7w0d
   Current AN: 3
   Previous AN: 2
   Next PN: 876
   RX SA Count: 0
   SA State: inUse(1)
   SAK Unchanged : no
   SA Create time : 07:51:07
   SA Start time : 7w0d
   SC Statistics
    Notvalid pkts 0
    Invalid pkts 0
    Valid pkts 1776339674
    Late pkts 0
    Uncheck pkts 0
    Delay pkts 0
    UnusedSA pkts 0
    NousingSA pkts 0
    Validated Bytes 0
    Decrypted Bytes 15958621049438
   SA Statistics
    Notvalid pkts 0
    Invalid pkts 0
    Valid pkts 874
    UnusedSA pkts 0
    NousingSA pkts 0
    Validated Bytes 0
    Decrypted Bytes 123888

  Port Statistics
   Ingress untag pkts  0
   Ingress notag pkts  16957
   Ingress badtag pkts  0
   Ingress unknownSCI pkts  0
   Ingress noSCI pkts  0
   Ingress overrun pkts  0
        '''
        if 'No Receive Secure Channels' not in out:
            receive_ch = {}
            p9 = re.compile(r'Receive Secure Channels\n'
                    r' +SCI : +(?P<SCI>\w+)\n'
                    r' +SC state : +(?P<SC_state>\S+)\n'
                    r' +Elapsed time : +(?P<Elapsed_time>\w+)\n'
                    r' +Start time : +(?P<Start_time>\w+)\n'
                    r' +Current AN: +(?P<Current_AN>\w+)\n'
                    r' +Previous AN: +(?P<Previous_AN>\S+)\n'
                    r' +Next PN: +(?P<Next_PN>\w+)\n'
                    r' +RX SA Count: +(?P<RX_SA_Count>\w+)\n'
                    r' +SA State: +(?P<SA_State>\S+)\n'
                    r' +SAK Unchanged : +(?P<SAK_Unchanged>\w+)\n'
                    r' +SA Create time : +(?P<SA_Create_time>\S+)\n'
                    r' +SA Start time : +(?P<SA_Start_time>\w+)\n', re.MULTILINE)
            p10 = re.compile(r'SC Statistics\n'
                    r' +Notvalid pkts +(?P<Notvalid_pkts>\w+)\n'
                    r' +Invalid pkts +(?P<Invalid_pkts>\w+)\n'
                    r' +Valid pkts +(?P<Valid_pkts>\w+)\n'
                    r' +Late pkts +(?P<Late_pkts>\w+)\n'
                    r' +Uncheck pkts +(?P<Uncheck_pkts>\w+)\n'
                    r' +Delay pkts +(?P<Delay_pkts>\w+)\n'
                    r' +UnusedSA pkts +(?P<UnusedSA_pkts>\w+)\n'
                    r' +NousingSA pkts +(?P<NousingSA_pkts>\w+)\n'
                    r' +Validated Bytes +(?P<Validated_Bytes>\w+)\n'
                    r' +Decrypted Bytes +(?P<Decrypted_Bytes>\w+)\n', re.MULTILINE)
            p11 = re.compile(r'SA Statistics\n'
                    r' +Notvalid pkts +(?P<Notvalid_pkts>\w+)\n'
                    r' +Invalid pkts +(?P<Invalid_pkts>\w+)\n'
                    r' +Valid pkts +(?P<Valid_pkts>\w+)\n'
                    r' +UnusedSA pkts +(?P<UnusedSA_pkts>\w+)\n'
                    r' +NousingSA pkts +(?P<NousingSA_pkts>\w+)\n'
                    r' +Validated Bytes +(?P<Validated_Bytes>\w+)\n'
                    r' +Decrypted Bytes +(?P<Decrypted_Bytes>\w+)\n', re.MULTILINE)
            p12 = re.compile(r'Port Statistics\n'
                    r' +Ingress untag pkts  +(?P<Ingress_untag_pkts>\w+)\n'
                    r' +Ingress notag pkts  +(?P<Ingress_notag_pkts>\w+)\n'
                    r' +Ingress badtag pkts  +(?P<Ingress_badtag_pkts>\w+)\n'
                    r' +Ingress unknownSCI pkts  +(?P<Ingress_unknownSCI_pkts>\w+)\n'
                    r' +Ingress noSCI pkts  +(?P<Ingress_noSCI_pkts>\w+)\n'
                    r' +Ingress overrun pkts  +(?P<Ingress_overrun_pkts>\w+)', re.MULTILINE)
            m9 = p9.search(out)
            if m9:
                group9 = m9.groupdict()
                receive_ch['SCI'] = group9['SCI']
                receive_ch['SC_state'] = group9['SC_state']
                receive_ch['Elapsed_time'] = group9['Elapsed_time']
                receive_ch['Start_time'] = group9['Start_time']
                receive_ch['Current_AN'] = group9['Current_AN']
                receive_ch['Previous_AN'] = group9['Previous_AN']
                receive_ch['Next_PN'] = group9['Next_PN']
                receive_ch['SA_State'] = group9['SA_State']
                receive_ch['RX_SA_Count'] = group9['RX_SA_Count']
                receive_ch['SAK_Unchanged'] = group9['SAK_Unchanged']
                receive_ch['SA_Create_time'] = group9['SA_Create_time']
                receive_ch['SA_Start_time'] = group9['SA_Start_time']

            m10 = p10.search(out)
            if m10:
                group10 = m10.groupdict()
                receive_sc = {}
                receive_sc['Notvalid_pkts'] = group10['Notvalid_pkts']
                receive_sc['Invalid_pkts'] = group10['Invalid_pkts']
                receive_sc['Valid_pkts'] = group10['Valid_pkts']
                receive_sc['Late_pkts'] = group10['Late_pkts']
                receive_sc['Uncheck_pkts'] = group10['Uncheck_pkts']
                receive_sc['Delay_pkts'] = group10['Delay_pkts']
                receive_sc['UnusedSA_pkts'] = group10['UnusedSA_pkts']
                receive_sc['NousingSA_pkts'] = group10['NousingSA_pkts']
                receive_sc['Validated_Bytes'] = group10['Validated_Bytes']
                receive_sc['Decrypted_Bytes'] = group10['Decrypted_Bytes']
                receive_ch['SC_Statistics'] = receive_sc
            m11 = p11.search(out)
            if m11:
                group11 = m11.groupdict()
                receive_sa = {}
                receive_sa['Notvalid_pkts'] = group11['Notvalid_pkts']
                receive_sa['Invalid_pkts'] = group11['Invalid_pkts']
                receive_sa['Valid_pkts'] = group11['Valid_pkts']
                receive_sa['UnusedSA_pkts'] = group11['UnusedSA_pkts']
                receive_sa['NousingSA_pkts'] = group11['NousingSA_pkts']
                receive_sa['Decrypted_Bytes'] = group11['Decrypted_Bytes']
                receive_sa['Validated_Bytes'] = group11['Validated_Bytes']
                receive_ch['SA_Statistics'] = receive_sa
            m12 = p12.search(out)
            if m12:
                group12 = m12.groupdict()
                receive_port = {}
                receive_port['Ingress_untag_pkts'] = group12['Ingress_untag_pkts']
                receive_port['Ingress_notag_pkts'] = group12['Ingress_notag_pkts']
                receive_port['Ingress_badtag_pkts'] = group12['Ingress_badtag_pkts']
                receive_port['Ingress_unknownSCI_pkts'] = group12['Ingress_unknownSCI_pkts']
                receive_port['Ingress_noSCI_pkts'] = group12['Ingress_noSCI_pkts']
                receive_port['Ingress_overrun_pkts'] = group12['Ingress_overrun_pkts']
                receive_ch['Port_Statistics'] = receive_port
            ret_dict['Receive_Secure_Channels'] = receive_ch
        return ret_dict 
