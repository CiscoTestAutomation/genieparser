# Import the Python mock functionality
import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_crypto
from genie.libs.parser.iosxe.show_crypto import ShowCryptoIkev2SaDetail

# =================================
# Unit test for 'show crypto ikev2 sa detail'
# =================================
class test_show_crypto_ikev2_sa_detail(unittest.TestCase):

    '''Unit test for "show crypto ikev2 sa detail"'''

    empty_output = {'execute.return_value': ''}

    # Specify the expected result for the parsed output
    golden_parsed_output1 = {
        'tunnel_id': {
            1: {
                'local': '10.146.0.154/500',
                'remote': '107.90.29.85/500',
                'fvrf': 'gre',
                'ivrf': 'gre',
                'status': 'ready',
                'remote_subnets': ['10.255.1.238 255.255.255.255'],
                'encryption': 'aes-gcm',
                'keysize': 256,
                'prf': 'sha512',
                'hash': 'none',
                'dh_grp': 21,
                'auth_sign': 'psk',
                'auth_verify': 'psk',
                'life_time': 86400,
                'active_time': 20635,
                'ce_id': 53247,
                'session_id': 494,
                'local_spi': '26E77925771B44B1',
                'remote_spi': '4785C18DB784C439',
                'status_description': 'negotiation done',
                'local_id': 'cedar.flex.example.com',
                'remote_id': 'example-r46.flex.example.com',
                'local_reg_msg_id': 3,
                'remote_req_msg_id': 5,
                'local_next_msg_id': 3,
                'remote_next_msg_id': 5,
                'local_req_queued': 3,
                'remote_req_queued': 5,
                'local_window': 5,
                'remote_window': 5,
                'dpd_configured_time': 10,
                'retry': 2,
                'fragmentation': 'not  configured',
                'dynamic_route_update': 'enabled',
                'extended_authentication': 'not configured',
                'nat_t': 'not detected',
                'cisco_trust_security_sgt': 'disabled',
                'initiator_of_sa': 'no'
            },
            8: {
                'local': '10.146.0.154/4500',
                'remote': '3.130.109.2/4500',
                'fvrf': 'gre',
                'ivrf': 'gre',
                'status': 'ready',
                'remote_subnets': ['172.31.0.4 255.255.255.255'],
                'encryption': 'aes-cbc',
                'keysize': 128,
                'prf': 'sha256',
                'hash': 'sha256',
                'dh_grp': 19,
                'auth_sign': 'psk',
                'auth_verify': 'psk',
                'life_time': 86400,
                'active_time': 16301,
                'ce_id': 0,
                'session_id': 470,
                'local_spi': 'B3A917AB8A5F68A9',
                'remote_spi': 'FBAFD8516EA9D5E8',
                'status_description': 'negotiation done',
                'local_id': 'cedar.flex.example.com',
                'remote_id': 'test-r1.flex.example.com',
                'local_reg_msg_id': 0,
                'remote_req_msg_id': 16,
                'local_next_msg_id': 0,
                'remote_next_msg_id': 16,
                'local_req_queued': 0,
                'remote_req_queued': 16,
                'local_window': 5,
                'remote_window': 5,
                'dpd_configured_time': 10,
                'retry': 2,
                'fragmentation': 'not  configured',
                'dynamic_route_update': 'enabled',
                'extended_authentication': 'not configured',
                'nat_t': 'detected  outside',
                'cisco_trust_security_sgt': 'disabled',
                'initiator_of_sa': 'no'
            },
            9: {
                'local': '10.146.0.154/500',
                'remote': '65.27.58.179/500',
                'fvrf': 'gre',
                'ivrf': 'gre',
                'status': 'ready',
                'remote_subnets': ['10.255.3.229 255.255.255.255'],
                'encryption': 'aes-cbc',
                'keysize': 256,
                'prf': 'sha512',
                'hash': 'sha512',
                'dh_grp': 19,
                'auth_sign': 'psk',
                'auth_verify': 'psk',
                'life_time': 86400,
                'active_time': 16298,
                'ce_id': 0,
                'session_id': 471,
                'local_spi': 'EA7CC2DFCC83A760',
                'remote_spi': 'E4D5BDA3B19BBD80',
                'status_description': 'negotiation done',
                'local_id': 'cedar.flex.example.com',
                'remote_id': 'test2-r1.split.flex.example.com',
                'local_reg_msg_id': 0,
                'remote_req_msg_id': 15,
                'local_next_msg_id': 0,
                'remote_next_msg_id': 15,
                'local_req_queued': 0,
                'remote_req_queued': 15,
                'local_window': 5,
                'remote_window': 5,
                'dpd_configured_time': 10,
                'retry': 2,
                'fragmentation': 'not  configured',
                'dynamic_route_update': 'enabled',
                'extended_authentication': 'not configured',
                'nat_t': 'not detected',
                'cisco_trust_security_sgt': 'disabled',
                'initiator_of_sa': 'no'
            }
        }
    }

    # Specify the expected unparsed output
    golden_output1 = {'execute.return_value': '''
        Tunnel-id Local                 Remote                fvrf/ivrf            Status 
1         10.146.0.154/500     107.90.29.85/500      gre/gre              READY  
      Encr: AES-GCM, keysize: 256, PRF: SHA512, Hash: None, DH Grp:21, Auth sign: PSK, Auth verify: PSK
      Life/Active Time: 86400/20635 sec
      CE id: 53247, Session-id: 494
      Local spi: 26E77925771B44B1       Remote spi: 4785C18DB784C439
      Status Description: Negotiation done
      Local id: cedar.flex.example.com
      Remote id: example-r46.flex.example.com
      Local req msg id:  3              Remote req msg id:  5         
      Local next msg id: 3              Remote next msg id: 5         
      Local req queued:  3              Remote req queued:  5         
      Local window:      5              Remote window:      5         
      DPD configured for 10 seconds, retry 2
      Fragmentation not  configured.
      Dynamic Route Update: enabled
      Extended Authentication not configured.
      NAT-T is not detected  
      Cisco Trust Security SGT is disabled
      Initiator of SA : No
      Remote subnets:
      10.255.1.238 255.255.255.255
      PEER TYPE: IOS-XE

Tunnel-id Local                 Remote                fvrf/ivrf            Status 
8         10.146.0.154/4500    3.130.109.2/4500      gre/gre              READY  
      Encr: AES-CBC, keysize: 128, PRF: SHA256, Hash: SHA256, DH Grp:19, Auth sign: PSK, Auth verify: PSK
      Life/Active Time: 86400/16301 sec
      CE id: 0, Session-id: 470
      Local spi: B3A917AB8A5F68A9       Remote spi: FBAFD8516EA9D5E8
      Status Description: Negotiation done
      Local id: cedar.flex.example.com
      Remote id: test-r1.flex.example.com
      Local req msg id:  0              Remote req msg id:  16        
      Local next msg id: 0              Remote next msg id: 16        
      Local req queued:  0              Remote req queued:  16        
      Local window:      5              Remote window:      5         
      DPD configured for 10 seconds, retry 2
      Fragmentation not  configured.
      Dynamic Route Update: enabled
      Extended Authentication not configured.
      NAT-T is detected  outside
      Cisco Trust Security SGT is disabled
      Initiator of SA : No
      Remote subnets:
      172.31.0.4 255.255.255.255
      PEER TYPE: Other

Tunnel-id Local                 Remote                fvrf/ivrf            Status 
9         10.146.0.154/500     65.27.58.179/500      gre/gre              READY  
      Encr: AES-CBC, keysize: 256, PRF: SHA512, Hash: SHA512, DH Grp:19, Auth sign: PSK, Auth verify: PSK
      Life/Active Time: 86400/16298 sec
      CE id: 0, Session-id: 471
      Local spi: EA7CC2DFCC83A760       Remote spi: E4D5BDA3B19BBD80
      Status Description: Negotiation done
      Local id: cedar.flex.example.com
      Remote id: test2-r1.split.flex.example.com
      Local req msg id:  0              Remote req msg id:  15        
      Local next msg id: 0              Remote next msg id: 15        
      Local req queued:  0              Remote req queued:  15        
      Local window:      5              Remote window:      5         
      DPD configured for 10 seconds, retry 2
      Fragmentation not  configured.
      Dynamic Route Update: enabled
      Extended Authentication not configured.
      NAT-T is not detected  
      Cisco Trust Security SGT is disabled
      Initiator of SA : No
      Remote subnets:
      10.255.3.229 255.255.255.255
      PEER TYPE: Other
        '''}

    def test_show_crypto_ikev2_sa_detail(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowCryptoIkev2SaDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()