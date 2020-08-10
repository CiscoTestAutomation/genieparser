# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_ipsec import ShowSdwanIpsecInboundConnections,\
ShowSdwanIpsecOutboundConnections,ShowSdwanIpsecLocalsa


# ============================================
# Parser for the following commands
#   * 'show sdwan ipsec inbound-connections'
#   * 'show sdwan ipsec outbound-connections'
#   * 'show sdwan ipsec local-sa <WORD>'
# ============================================

class TestShowSdwanIpsecInboundConnections(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
    #show sdwan ipsec inbound-connections 
    SOURCE                                  SOURCE  DEST                                    DEST    REMOTE           REMOTE           LOCAL            LOCAL            NEGOTIATED                   
    IP                                      PORT    IP                                      PORT    TLOC ADDRESS     TLOC COLOR       TLOC ADDRESS     TLOC COLOR       ENCRYPTION ALGORITHM  TC SPIs
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    77.27.2.2                               12366   77.27.8.2                               12346   78.78.0.6        biz-internet     78.78.0.9        biz-internet     AES-GCM-256           8      
    '''}

    golden_parsed_output = {
        'source_ip': {
            '77.27.2.2': {
                'destination_ip': {
                    '77.27.8.2': {
                        'local_tloc_color': 'biz-internet',
                        'destination_port': 12346,
                        'local_tloc': '78.78.0.9',
                        'remote_tloc_color': 'biz-internet',
                        'remote_tloc': '78.78.0.6',
                        'source_port': 12366,
                        'encryption_algorithm': 'AES-GCM-256',
                        'tc_spi': 8,
                    },
                },
            },
        },    
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanIpsecInboundConnections(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanIpsecInboundConnections(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
        
class TestShowSdwanIpsecOutboundConnections(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
    #show sdwan ipsec outbound-connections 
    SOURCE                                  SOURCE  DEST                                    DEST                        REMOTE           REMOTE           AUTHENTICATION            NEGOTIATED                   
    IP                                      PORT    IP                                      PORT    SPI     TUNNEL MTU  TLOC ADDRESS     TLOC COLOR       USED           KEY HASH   ENCRYPTION ALGORITHM  TC SPIs
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    77.27.8.2                               12346   77.27.2.2                               12366   271     1438        78.78.0.6        biz-internet     AH_SHA1_HMAC   *****b384  AES-GCM-256           8
    77.27.8.2                               12346   77.27.3.2                               12366   271     1438        78.78.0.6        biz-internet     AH_SHA1_HMAC   *****b384  AES-GCM-256           8
    77.27.9.2                               12346   77.27.2.2                               12366   271     1438        78.78.0.6        biz-internet     AH_SHA1_HMAC   *****b384  AES-GCM-256           8
    '''}

    golden_parsed_output = {
        'source_ip': {
            '77.27.8.2': {
                'destination_ip': {
                    '77.27.2.2': {
                        'destination_port': 12366,
                        'authentication': 'AH_SHA1_HMAC',
                        'remote_tloc_color': 'biz-internet',
                        'key_hash': '*****b384',
                        'spi': 271,
                        'source_port': 12346,
                        'remote_tloc': '78.78.0.6',
                        'encryption_algorithm': 'AES-GCM-256',
                        'tunnel_mtu': 1438,
                        'tc_spi': 8,
                    },
                    '77.27.3.2': {
                        'destination_port': 12366,
                        'authentication': 'AH_SHA1_HMAC',
                        'remote_tloc_color': 'biz-internet',
                        'key_hash': '*****b384',
                        'spi': 271,
                        'source_port': 12346,
                        'remote_tloc': '78.78.0.6',
                        'encryption_algorithm': 'AES-GCM-256',
                        'tunnel_mtu': 1438,
                        'tc_spi': 8,
                    },
                },
            },
            '77.27.9.2': {
                'destination_ip': {
                    '77.27.2.2': {
                        'destination_port': 12366,
                        'authentication': 'AH_SHA1_HMAC',
                        'remote_tloc_color': 'biz-internet',
                        'key_hash': '*****b384',
                        'spi': 271,
                        'source_port': 12346,
                        'remote_tloc': '78.78.0.6',
                        'encryption_algorithm': 'AES-GCM-256',
                        'tunnel_mtu': 1438,
                        'tc_spi': 8,
                    },
                },
            },
        },    
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanIpsecOutboundConnections(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanIpsecOutboundConnections(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowSdwanIpsecLocalsa(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
    #show sdwan ipsec local-sa 78.78.0.9
                                              SOURCE           SOURCE                                  SOURCE            
    TLOC ADDRESS     TLOC COLOR       SPI     IPv4             IPv6                                    PORT    KEY HASH  
    ----------------------------------------------------------------------------------------------------------------------
    78.78.0.9        biz-internet     259     77.27.8.2        ::                                      12346   *****8d95 
    78.78.0.9        biz-internet     260     77.27.8.2        ::                                      12346   *****4447'''}

    golden_parsed_output = {
        'local_sa': {
            'inbound':
                {
                 'spi': 259,
                 'source_ipv4': '77.27.8.2',
                 'source_port': 12346,
                 'source_ipv6': '::',
                 'tloc_color': 'biz-internet',
                 'key_hash': '*****8d95',
                },
            'outbound':
                {
                 'spi': 260,
                 'source_ipv4': '77.27.8.2',
                 'source_port': 12346,
                 'source_ipv6': '::',
                 'tloc_color': 'biz-internet',
                 'key_hash': '*****4447',
                },
            },
        }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanIpsecLocalsa(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanIpsecLocalsa(device=self.device)
        parsed_output = obj.parse(tloc_address='78.78.0.9')
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
		unittest.main()     
