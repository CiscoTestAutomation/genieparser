# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_control_connections import ShowSdwanControlConnections


# ============================================
# Parser for the following commands
#   * 'show bfd connections'
# ============================================
class TestShowControlConnections(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}

    golden_output = {'execute.return_value': '''
        vEdge# show control connections
                                                                                               PEER                                          PEER                                          CONTROLLER 
        PEER    PEER PEER            SITE       DOMAIN PEER                                    PRIV  PEER                                    PUB                                           GROUP      
        TYPE    PROT SYSTEM IP       ID         ID     PRIVATE IP                              PORT  PUBLIC IP                               PORT  LOCAL COLOR     PROXY STATE UPTIME      ID         
        ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        vsmart  tls  172.16.255.20   200        1      10.0.12.20                              23556 10.0.12.20                              23556 mpls            No    up     0:00:16:30  0           
        vsmart  tls  172.16.255.20   200        1      10.0.12.20                              23556 10.0.37.20                              23556 lte             Yes   up     0:00:16:22  0           
        vsmart  tls  172.16.255.19   300        1      10.0.12.19                              23556 10.0.12.19                              23556 mpls            No    up     0:00:16:30  0           
        vsmart  tls  172.16.255.19   300        1      10.0.12.19                              23556 10.0.37.19                              23556 lte             Yes   up     0:00:16:22  0        
    '''}

    golden_parsed_output = {
        'local_color': {
            'lte': {
                'peer_system_ip': {
                    '172.16.255.19': {
                        'controller_group_id': '0',
                        'domain_id': '1',
                        'peer_private_ip': '10.0.12.19',
                        'peer_private_port': '23556',
                        'peer_protocol': 'tls',
                        'peer_public_ip': '10.0.37.19',
                        'peer_public_port': '23556',
                        'peer_type': 'vsmart',
                        'proxy_state': 'Yes',
                        'site_id': '300',
                        'state': 'up',
                        'uptime': '0:00:16:22',
                    },
                    '172.16.255.20': {
                        'controller_group_id': '0',
                        'domain_id': '1',
                        'peer_private_ip': '10.0.12.20',
                        'peer_private_port': '23556',
                        'peer_protocol': 'tls',
                        'peer_public_ip': '10.0.37.20',
                        'peer_public_port': '23556',
                        'peer_type': 'vsmart',
                        'proxy_state': 'Yes',
                        'site_id': '200',
                        'state': 'up',
                        'uptime': '0:00:16:22',
                    },
                },
            },
            'mpls': {
                'peer_system_ip': {
                    '172.16.255.19': {
                        'controller_group_id': '0',
                        'domain_id': '1',
                        'peer_private_ip': '10.0.12.19',
                        'peer_private_port': '23556',
                        'peer_protocol': 'tls',
                        'peer_public_ip': '10.0.12.19',
                        'peer_public_port': '23556',
                        'peer_type': 'vsmart',
                        'proxy_state': 'No',
                        'site_id': '300',
                        'state': 'up',
                        'uptime': '0:00:16:30',
                    },
                    '172.16.255.20': {
                        'controller_group_id': '0',
                        'domain_id': '1',
                        'peer_private_ip': '10.0.12.20',
                        'peer_private_port': '23556',
                        'peer_protocol': 'tls',
                        'peer_public_ip': '10.0.12.20',
                        'peer_public_port': '23556',
                        'peer_type': 'vsmart',
                        'proxy_state': 'No',
                        'site_id': '200',
                        'state': 'up',
                        'uptime': '0:00:16:30',
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanControlConnections(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanControlConnections(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
		unittest.main()   
