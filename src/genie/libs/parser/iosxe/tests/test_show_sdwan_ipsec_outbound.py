# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_ipsec_outbound import ShowSdwanIpsecOutboundConnections


# ============================================
# Parser for the following commands
#   * 'show bfd sessions'
# ============================================
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
                        'destination_port': '12366',
                        'authentication': 'AH_SHA1_HMAC',
                        'remote_tloc_color': 'biz-internet',
                        'key_hash': '*****b384',
                        'spi': '271',
                        'source_port': '12346',
                        'remote_tloc': '78.78.0.6',
                        'encryption_algorithm': 'AES-GCM-256',
                        'tunnel_mtu': '1438',
                        'tc_spi': '8',
                    },
                    '77.27.3.2': {
                        'destination_port': '12366',
                        'authentication': 'AH_SHA1_HMAC',
                        'remote_tloc_color': 'biz-internet',
                        'key_hash': '*****b384',
                        'spi': '271',
                        'source_port': '12346',
                        'remote_tloc': '78.78.0.6',
                        'encryption_algorithm': 'AES-GCM-256',
                        'tunnel_mtu': '1438',
                        'tc_spi': '8',
                    },
                },
            },
            '77.27.9.2': {
                'destination_ip': {
                    '77.27.2.2': {
                        'destination_port': '12366',
                        'authentication': 'AH_SHA1_HMAC',
                        'remote_tloc_color': 'biz-internet',
                        'key_hash': '*****b384',
                        'spi': '271',
                        'source_port': '12346',
                        'remote_tloc': '78.78.0.6',
                        'encryption_algorithm': 'AES-GCM-256',
                        'tunnel_mtu': '1438',
                        'tc_spi': '8',
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


if __name__ == '__main__':
		unittest.main()     
