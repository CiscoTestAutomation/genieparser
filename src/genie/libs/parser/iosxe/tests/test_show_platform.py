import unittest
from unittest.mock import Mock
from ats.topology import Device
from ats.topology import loader
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
from genie.libs.parser.iosxe.show_platform import ShowPlatformSoftwareFedIpsecCounterIfId
from genie.libs.parser.iosxe.show_platform import ShowPlatformSoftwareFedIpsecResourceIfId

# =================================
# Unit test for 'show platform'
# =================================

class test_show_platform(unittest.TestCase):
    '''Unit test for "sh platform"'''

    empty_output = {'execute.return_value': ''}

    # Specify the expected result for the parsed output
    golden_parsed_output1 = {
            "if-id":"0x5c",
            "inbound_flow":{
                "anti_replay_fail":0,
                "asic_instance":"SA Stats",
                "auth_fail":0,
                "byte_count":81982020,
                "flow_id":54,
                "fvrf_id":0,
                "invalid_sa":0,
                "ivrf_id":0,
                "packet_count":683184,
                "packet_format_check_error":0,
                "sa_index":23,
                "sequence_number_overflows":0
            },
            "outbound_flow":{
                "anti_replay_fail":0,
                "asic_instance":"SA Stats",
                "auth_fail":0,
                "byte_count":974181368,
                "flow_id":53,
                "fvrf_id":0,
                "invalid_sa":0,
                "ivrf_id":0,
                "packet_count":6840571,
                "packet_format_check_error":0,
                "sa_index":1069,
                "sequence_number_overflows":0
            }
        }
    
    
     # Specify the expected unparsed output
    golden_output1 = {'execute.return_value': '''
        show platform software fed sw active ipsec counters if-id 0x5c
        ########################################
        Flow Stats for if-id 0x5c
        ########################################
        -----------------------------------
        Inbound Flow Info for flow id: 54
        FVRF ID: 0  IVRF ID: 0
        ------------------------------
        SA Index: 23
        --------------------
        Asic Instance 0: SA Stats 
        Packet Format Check Error:	0
        Invalid SA:			0
        Auth Fail:			0
        Sequence Number Overflows:	0
        Anti-Replay Fail:		0
        Packet Count:			683184
        Byte Count:			81982020
        -----------------------------------
        Outbound Flow Info for flow id: 53
        FVRF ID: 0  IVRF ID: 0
        ------------------------------
        SA Index: 1069
        --------------------
        Asic Instance 0: SA Stats 
        Packet Format Check Error:	0
        Invalid SA:			0
        Auth Fail:			0
        Sequence Number Overflows:	0
        Anti-Replay Fail:		0
        Packet Count:			6840571
        Byte Count:			974181368
     '''}


    def test_show_platform_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowPlatformSoftwareFedIpsecCounterIfId(device=self.device)
        parsed_output = obj.parse(if_id='0x5c')
        self.assertEqual(parsed_output, self.golden_parsed_output1)
   
    def test_show_platform_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowPlatformSoftwareFedIpsecCounterIfId(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(if_id='0x5c')

    
# =================================
# Unit test for 'show platform'
# =================================

class test_show_platform_res(unittest.TestCase):
    '''Unit test for "sh platform"'''
    empty_output1 = {'execute.return_value': ''}

    golden_parsed_output1 = {
            'Tunnel': {
                'Decap_Pass': {
                0: {'RI': '0x1b2',
                                'SI': '0x3d4',
                                'SI_DI': '0x5012',
                                'SI_RI': '0x1b2',
                                'asic_instance': 0,
                                'rcpServiceID': '0',
                                'replication_bitmap': 'LD'
                },
                1: {'RI': '0x1b2',
                                'SI': '0x3d4',
                                'SI_DI': '0x5012',
                                'SI_RI': '0x1b2',
                                'asic_instance': 1,
                                'rcpServiceID': '0',
                                'replication_bitmap': 'RD'
                },
                            'DI': '0x5012'
            },
                'Decrypt_Pass': {
                0: {'RI': '0x1b0',
                                    'SI': '0x3d1',
                                    'SI_DI': '0x5112',
                                    'SI_RI': '0x1b0',
                                    'asic_instance': 0,
                                    'rcpServiceID': '0x33',
                                    'replication_bitmap': 'LD'
                },
                1: {'RI': '0x1b0',
                                    'SI': '0x3d1',
                                    'SI_DI': '0x5112',
                                    'SI_RI': '0x1b0',
                                    'asic_instance': 1,
                                    'rcpServiceID': '0x33',
                                    'replication_bitmap': 'RD'
                },
                                'DI': '0x5112'
            },
                'Encrypt_Pass': {
                0: {'RI': '0x1b4',
                                    'SI': '0xbc',
                                    'SI_DI': '0x5112',
                                    'SI_RI': '0x1b4',
                                    'asic_instance': 0,
                                    'rcpServiceID': '0x30',
                                    'replication_bitmap': 'LD'
                },
                1: {'RI': '0x1b4',
                                    'SI': '0xbc',
                                    'SI_DI': '0x5112',
                                    'SI_RI': '0x1b4',
                                    'asic_instance': 1,
                                    'rcpServiceID': '0x30',
                                    'replication_bitmap': 'RD'
                },
                                'DI': '0x5112'
            },
        'Total-asic-instance': 2,
        'Tunnel-id': 'Tunnel222',
        'fvrf_id': 0,
        'if-id': '0x5c',
        'inbound_flow_id': 1928,
        'ivrf_id': 0,
        'outbound_flow_id': 1927
        }
    }

    golden_output1 = {'execute.return_value': '''
show platform software fed sw active ipsec resources if-id 0x5c
########################################
Tunnel222 IF ID 0x5c 
VTI-Flags 0x8 bit3:ADJ_SYNC_DONE
 CEF ADJ ID (0xf80005c6) Info:
   IF ID 0x5c ADJ-Flags 0x0 NO_FLAGS_SET AAL adj_id 0x410004dc
 Inbound Flow ID 1928 :
   FVRF ID: 0  IVRF ID: 0
   DB Entry: 0x0x7a34a7bb3a88
    Flag: 0x0 DB_FLAG_NOT_SET Decap L3IFLE: 0x7a34a506e458
   Decrypt Pass:
    Decrypt DI handle: 0x7a34a5ff6bf8
    Decrypt RI handle: 0x7a34a4f19998
    Decrypt SI handle: 0x7a34a6143ea8
    Decrypt Termination entry: 0x7a34a5acb8c8
    Decrypt SA Index: 54
    Decrypt RCP Service ID: 51
    Decrypt SPI 0xcd9786f/215578735

Handle:0x7a34a5ff6bf8 Res-Type:ASIC_RSC_DI Res-Switch-Num:1 Asic-Num:0 Feature-ID:AL_FID_IPSEC Lkp-ftr-id:LKP_FEAT_INVALID ref_count:74934
priv_ri/priv_si Handle:(nil) Hardware Indices/Handles: index0:0x5112  mtu_index/l3u_ri_index0:0x0 
Features sharing this resource:100 (74934), 

Brief Resource Information (ASIC_INSTANCE# 0)
----------------------------------------
Destination index   = 0x5112 DI_RCP_PORT3
pmap                = 0x00000000 0x00000000
rcp_pmap            = 0x4
==============================================================
Handle:0x7a34a4f19998 Res-Type:ASIC_RSC_RI Res-Switch-Num:255 Asic-Num:255 Feature-ID:AL_FID_IPSEC Lkp-ftr-id:LKP_FEAT_INVALID ref_count:1
priv_ri/priv_si Handle:0x7a34a5936348 Hardware Indices/Handles: index0:0x1b0  mtu_index/l3u_ri_index0:0x0  index1:0x1b0  mtu_index/l3u_ri_index1:0x0 
Features sharing this resource:100 (1), 

Brief Resource Information (ASIC_INSTANCE# 0)
----------------------------------------
ASIC#:0 RI:432 Rewrite_type:AL_RRM_REWRITE_INGRESS_L3_RECIRC(35) Mapped_rii:INGRESS_L3_RECIRC(79)


Brief Resource Information (ASIC_INSTANCE# 1)
----------------------------------------
ASIC#:1 RI:432 Rewrite_type:AL_RRM_REWRITE_INGRESS_L3_RECIRC(35) Mapped_rii:INGRESS_L3_RECIRC(79)


==============================================================
Handle:0x7a34a6143ea8 Res-Type:ASIC_RSC_SI Res-Switch-Num:255 Asic-Num:255 Feature-ID:AL_FID_IPSEC Lkp-ftr-id:LKP_FEAT_INVALID ref_count:1
priv_ri/priv_si Handle:0x7a34a4f19998 Hardware Indices/Handles: index0:0x3d1  mtu_index/l3u_ri_index0:0x0  index1:0x3d1  mtu_index/l3u_ri_index1:0x0 

Brief Resource Information (ASIC_INSTANCE# 0)
----------------------------------------
Station Index (SI) [0x3d1]
RI = 0x1b0
DI = 0x5112
stationTableGenericLabel = 0
stationFdConstructionLabel = 0x2
lookupSkipIdIndex = 0
rcpServiceId = 0x33
dejaVuPreCheckEn = 0
Replication Bitmap: LD 

Brief Resource Information (ASIC_INSTANCE# 1)
----------------------------------------
Station Index (SI) [0x3d1]
RI = 0x1b0
DI = 0x5112
stationTableGenericLabel = 0
stationFdConstructionLabel = 0x2
lookupSkipIdIndex = 0
rcpServiceId = 0x33
dejaVuPreCheckEn = 0
Replication Bitmap: RD 

==============================================================


   Decap Pass:
    Decap DI handle: 0x7a34a448a928
    Decap RI handle: 0x7a34a7114568
    Decap SI handle: 0x7a34a67a9db8
    Decap Termination entry: 0x7a34a6145a88
    Encap Termination entry: 0x0
    Decap RCP Service ID: 0


Handle:0x7a34a7114568 Res-Type:ASIC_RSC_RI Res-Switch-Num:255 Asic-Num:255 Feature-ID:AL_FID_IPSEC Lkp-ftr-id:LKP_FEAT_INVALID ref_count:1
priv_ri/priv_si Handle:0x7a34a7755d58 Hardware Indices/Handles: index0:0x1b2  mtu_index/l3u_ri_index0:0x0  index1:0x1b2  mtu_index/l3u_ri_index1:0x0 
Features sharing this resource:100 (1), 

Brief Resource Information (ASIC_INSTANCE# 0)
----------------------------------------
ASIC#:0 RI:434 Rewrite_type:AL_RRM_REWRITE_IPSEC_TUNNEL_MODE_DECAP_SECONDPASS_INNERV4(47) Mapped_rii:IPSEC_TUNNEL_MODE_DECAP_SECONDPASS_INNERV4(247)


Brief Resource Information (ASIC_INSTANCE# 1)
----------------------------------------
ASIC#:1 RI:434 Rewrite_type:AL_RRM_REWRITE_IPSEC_TUNNEL_MODE_DECAP_SECONDPASS_INNERV4(47) Mapped_rii:IPSEC_TUNNEL_MODE_DECAP_SECONDPASS_INNERV4(247)


==============================================================
Handle:0x7a34a67a9db8 Res-Type:ASIC_RSC_SI Res-Switch-Num:255 Asic-Num:255 Feature-ID:AL_FID_IPSEC Lkp-ftr-id:LKP_FEAT_INVALID ref_count:1
priv_ri/priv_si Handle:0x7a34a7114568 Hardware Indices/Handles: index0:0x3d4  mtu_index/l3u_ri_index0:0x0  index1:0x3d4  mtu_index/l3u_ri_index1:0x0 

Brief Resource Information (ASIC_INSTANCE# 0)
----------------------------------------
Station Index (SI) [0x3d4]
RI = 0x1b2
DI = 0x5012
stationTableGenericLabel = 0
stationFdConstructionLabel = 0x2
lookupSkipIdIndex = 0
rcpServiceId = 0
dejaVuPreCheckEn = 0
Replication Bitmap: LD 

Brief Resource Information (ASIC_INSTANCE# 1)
----------------------------------------
Station Index (SI) [0x3d4]
RI = 0x1b2
DI = 0x5012
stationTableGenericLabel = 0
stationFdConstructionLabel = 0x2
lookupSkipIdIndex = 0
rcpServiceId = 0
dejaVuPreCheckEn = 0
Replication Bitmap: RD 

==============================================================
Handle:0x7a34a448a928 Res-Type:ASIC_RSC_DI Res-Switch-Num:1 Asic-Num:0 Feature-ID:AL_FID_LISP Lkp-ftr-id:LKP_FEAT_INVALID ref_count:75216
priv_ri/priv_si Handle:(nil) Hardware Indices/Handles: index0:0x5012  mtu_index/l3u_ri_index0:0x0 
Features sharing this resource:109 (1), 152 (2), 107 (1518), 100 (73695), 

Brief Resource Information (ASIC_INSTANCE# 0)
----------------------------------------
Destination index   = 0x5012 DI_RCP_PORT1
pmap                = 0x00000000 0x00000000
rcp_pmap            = 0x1
==============================================================


 Outbound Flow ID 1927 :
   FVRF ID: 0  IVRF ID: 0
   DB Entry: 0x0x7a34a6128188
    Flag: 0x0 DB_FLAG_NOT_SET AAL adj_id: 0x410004dc
    Encap L3IFLE: 0x7a34a506e248
    Hash Entry: 0x0x7a34a696dbb8
      Key: adj_id 0x410004dc spi 0x0 if_id 0x5c
      db entry: 0x0x7a34a6128188 
   Encrypt/Encap Pass:
    Encrypt DI handle: 0x7a34a5ff6bf8
    Encrypt RI handle: 0x7a34a60040b8
    Encrypt SI handle: 0x7a34a5686a28
    Encrypt SA Index: 1044
    Encrypt RCP Service ID: 48
    Encap Termination entry: 0x0
    Encrypt SPI 0x7385c88e/1938147470


Handle:0x7a34a5ff6bf8 Res-Type:ASIC_RSC_DI Res-Switch-Num:1 Asic-Num:0 Feature-ID:AL_FID_IPSEC Lkp-ftr-id:LKP_FEAT_INVALID ref_count:74934
priv_ri/priv_si Handle:(nil) Hardware Indices/Handles: index0:0x5112  mtu_index/l3u_ri_index0:0x0 
Features sharing this resource:100 (74934), 

Brief Resource Information (ASIC_INSTANCE# 0)
----------------------------------------
Destination index   = 0x5112 DI_RCP_PORT3
pmap                = 0x00000000 0x00000000
rcp_pmap            = 0x4
==============================================================
Handle:0x7a34a60040b8 Res-Type:ASIC_RSC_RI Res-Switch-Num:255 Asic-Num:255 Feature-ID:AL_FID_IPSEC Lkp-ftr-id:LKP_FEAT_INVALID ref_count:1
priv_ri/priv_si Handle:0x7a34a6a38f38 Hardware Indices/Handles: index0:0x1b4  mtu_index/l3u_ri_index0:0x0  index1:0x1b4  mtu_index/l3u_ri_index1:0x0 
Features sharing this resource:100 (1), 

Brief Resource Information (ASIC_INSTANCE# 0)
----------------------------------------
ASIC#:0 RI:436 Rewrite_type:AL_RRM_REWRITE_IPSEC_TUNNEL_MODE_ENCAP_FIRSTPASS_OUTERV4_INNERV4(49) Mapped_rii:IPSEC_TUNNEL_MODE_ENCAP_FIRSTPASS_OUTERV4_INNERV4(242)


Brief Resource Information (ASIC_INSTANCE# 1)
----------------------------------------
ASIC#:1 RI:436 Rewrite_type:AL_RRM_REWRITE_IPSEC_TUNNEL_MODE_ENCAP_FIRSTPASS_OUTERV4_INNERV4(49) Mapped_rii:IPSEC_TUNNEL_MODE_ENCAP_FIRSTPASS_OUTERV4_INNERV4(242)


==============================================================
Handle:0x7a34a5686a28 Res-Type:ASIC_RSC_SI Res-Switch-Num:255 Asic-Num:255 Feature-ID:AL_FID_IPSEC Lkp-ftr-id:LKP_FEAT_INVALID ref_count:1
priv_ri/priv_si Handle:0x7a34a60040b8 Hardware Indices/Handles: index0:0xbc  mtu_index/l3u_ri_index0:0x0  index1:0xbc  mtu_index/l3u_ri_index1:0x0 

Brief Resource Information (ASIC_INSTANCE# 0)
----------------------------------------
Station Index (SI) [0xbc]
RI = 0x1b4
DI = 0x5112
stationTableGenericLabel = 0
stationFdConstructionLabel = 0x2
lookupSkipIdIndex = 0
rcpServiceId = 0x30
dejaVuPreCheckEn = 0
Replication Bitmap: LD 

Brief Resource Information (ASIC_INSTANCE# 1)
----------------------------------------
Station Index (SI) [0xbc]
RI = 0x1b4
DI = 0x5112
stationTableGenericLabel = 0
stationFdConstructionLabel = 0x2
lookupSkipIdIndex = 0
rcpServiceId = 0x30
dejaVuPreCheckEn = 0
Replication Bitmap: RD 

==============================================================
    '''}
    
    def test_show_platform_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowPlatformSoftwareFedIpsecResourceIfId(device=self.device)
        parsed_output = obj.parse(if_id='0x5c')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_platform_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output1)
        obj = ShowPlatformSoftwareFedIpsecResourceIfId(device=self.device)
        # with self.assertRaises(SchemaEmptyParserError):
        parsed_output = obj.parse(if_id='0x5c')
    
    
if __name__ == '__main__':
    unittest.main()