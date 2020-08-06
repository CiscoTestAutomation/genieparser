# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_ipsec_inbound import ShowSdwanIpsecInboundConnections


# ============================================
# Parser for the following commands
#   * 'show bfd sessions'
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
                        'destination_port': '12346',
                        'local_tloc': '78.78.0.9',
                        'remote_tloc_color': 'biz-internet',
                        'remote_tloc': '78.78.0.6',
                        'source_port': '12366',
                        'encryption_algorithm': 'AES-GCM-256',
                        'spi': '8',
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


if __name__ == '__main__':
		unittest.main()     
