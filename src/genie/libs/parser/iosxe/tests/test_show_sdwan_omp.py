import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_omp import (ShowSdwanOmpSummary,
                                                    ShowSdwanOmpTlocs,
                                                    ShowSdwanOmpTlocPath,
                                                    ShowSdwanOmpPeers)


# ============================================
# Parser for the following commands
#   * 'show bfd sessions'
# ============================================
class TestShowSdwanOmpSummary(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
    #show sdwan omp summary 
oper-state             UP
admin-state            UP
personality            vedge
omp-uptime             34:03:00:35
routes-received        5
routes-installed       3
routes-sent            2
tlocs-received         3
tlocs-installed        2
tlocs-sent             1
services-received      3
services-installed     0
services-sent          3
mcast-routes-received  0
mcast-routes-installed 0
mcast-routes-sent      0
hello-sent             146344
hello-received         146337
handshake-sent         2
handshake-received     2
alert-sent             1
alert-received         0
inform-sent            16
inform-received        16
update-sent            79
update-received        157
policy-sent            0
policy-received        2
total-packets-sent     146442
total-packets-received 146514
vsmart-peers           1
'''}

    golden_parsed_output = {
        'oper_state': 'UP',
        'admin_state': 'UP',
        'personality': 'vedge',
        'omp_uptime': '34:03:00:35',
        'routes_received': 5,
        'routes_installed': 3,
        'routes_sent': 2,
        'tlocs_received': 3,
        'tlocs_installed': 2,
        'tlocs_sent': 1,
        'services_received': 3,
        'services_installed': 0,
        'services_sent': 3,
        'mcast_routes_received': 0,
        'mcast_routes_sent': 0,
        'hello_sent': 146344,
        'hello_received': 146337,
        'handshake_sent': 2,
        'handshake_received': 2,
        'alert_sent': 1,
        'alert_received': 0,
        'inform_sent': 16,
        'inform_received': 16,
        'update_sent': 79,
        'update_received': 157,
        'policy_sent': 0,
        'policy_received': 2,
        'total_packets_sent': 146442,
         'vsmart_peers': 1}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanOmpSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanOmpSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

class TestShowSdwanOmpTlocPath(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        show omp tloc-paths
        tloc-paths entries 100.100.100.10 default ipsec
        tloc-paths entries 100.100.100.20 default ipsec
        tloc-paths entries 100.100.100.30 default ipsec
    '''}

    golden_parsed_output = {
        'tloc_path': {
            '100.100.100.10': {
            'tloc': {
                'default': {
                    'transport': 'ipsec'
                }
            }
            },
            '100.100.100.20': {
            'tloc': {
                'default': {
                    'transport': 'ipsec'
                }
            }
            },
            '100.100.100.30': {
            'tloc': {
                'default': {
                    'transport': 'ipsec'
                }
            }
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanOmpTlocPath(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanOmpTlocPath(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
        #self.assertDictEqual(parsed_output,self.golden_parsed_output)

class TestShowSdwanOmpPeers(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
    R -> routes received
    I -> routes installed
    S -> routes sent

    DOMAIN OVERLAY SITE
    PEER TYPE ID ID ID STATE UPTIME R/I/S
    ------------------------------------------------------------------------------------------
    1.1.1.4 vsmart 1 1 4 up 6:13:57:28 4/0/4
    55.55.55.5 vedge 1 1 55 up 0:01:24:29 1/0/1
    105.105.105.6 vedge 1 1 6 up 6:13:58:46 1/0/1
    177.177.175.170 vedge 1 1 170 up 6:13:58:47 0/0/2
    192.168.254.100 vedge 1 1 100 up 0:09:28:48 0/0/0
    192.168.254.101 vedge 1 1 101 up 0:09:27:33 0/0/0
    192.168.254.102 vedge 1 1 102 up 0:09:29:00 0/0/0
    192.168.255.2 vedge 1 1 200 up 0:04:14:12 2/0/0
    '''}

    golden_parsed_output = {
        'peer': {
            '1.1.1.4': {
                'type': 'vsmart',
                'domain_id': 1,
                'overlay_id': 1,
                'site_id': 4,
                'state': 'up',
                'uptime': '6:13:57:28',
                'route': {
                    'recv': 4,
                    'install': 0,
                    'sent': 4
                }
            },
            '55.55.55.5': {
                'type': 'vedge',
                'domain_id': 1,
                'overlay_id': 1,
                'site_id': 55,
                'state': 'up',
                'uptime': '0:01:24:29',
                'route': {
                    'recv': 1,
                    'install': 0,
                    'sent': 1
                }
            },
            '105.105.105.6': {
                'type': 'vedge',
                'domain_id': 1,
                'overlay_id': 1,
                'site_id': 6,
                'state': 'up',
                'uptime': '6:13:58:46',
                'route': {
                    'recv': 1,
                    'install': 0,
                    'sent': 1
                }
            },
            '177.177.175.170': {
                'type': 'vedge',
                'domain_id': 1,
                'overlay_id': 1,
                'site_id': 170,
                'state': 'up',
                'uptime': '6:13:58:47',
                'route': {
                    'recv': 0,
                    'install': 0,
                    'sent': 2
                }
            },
            '192.168.254.100': {
                'type': 'vedge',
                'domain_id': 1,
                'overlay_id': 1,
                'site_id': 100,
                'state': 'up',
                'uptime': '0:09:28:48',
                'route': {
                    'recv': 0,
                    'install': 0,
                    'sent': 0
                }
            },
            '192.168.254.101': {
                'type': 'vedge',
                'domain_id': 1,
                'overlay_id': 1,
                'site_id': 101,
                'state': 'up',
                'uptime': '0:09:27:33',
                'route': {
                    'recv': 0,
                    'install': 0,
                    'sent': 0
                }
            },
            '192.168.254.102': {
                'type': 'vedge',
                'domain_id': 1,
                'overlay_id': 1,
                'site_id': 102,
                'state': 'up',
                'uptime': '0:09:29:00',
                'route': {
                    'recv': 0,
                    'install': 0,
                    'sent': 0
                }
            },
            '192.168.255.2': {
                'type': 'vedge',
                'domain_id': 1,
                'overlay_id': 1,
                'site_id': 200,
                'state': 'up',
                'uptime': '0:04:14:12',
                'route': {
                    'recv': 2,
                    'install': 0,
                    'sent': 0
                }
            }
        }
    }
 
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanOmpPeers(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanOmpPeers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
        #self.assertDictEqual(parsed_output,self.golden_parsed_output)

class TestShowSdwanOmpTlocs(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        ---------------------------------------------------
        tloc entries for 100.100.100.10
                        default
                        ipsec
        ---------------------------------------------------
                    RECEIVED FROM:                   
        peer            0.0.0.0
        status          C,Red,R
        loss-reason     not set
        lost-to-peer    not set
        lost-to-path-id not set
            Attributes:
            attribute-type    installed
            encap-key         not set
            encap-proto       0
            encap-spi         365
            encap-auth        sha1-hmac,ah-sha1-hmac
            encap-encrypt     aes256
            public-ip         12.12.12.2
            public-port       12426
            private-ip        12.12.12.2
            private-port      12426
            public-ip         ::
            public-port       0
            private-ip        ::
            private-port      0
            bfd-status        up
            domain-id         not set
            site-id           101
            overlay-id        not set
            preference        0
            tag               not set
            stale             not set
            weight            1
            version           3
            gen-id             0x80000003
            carrier           default
            restrict          0
            on-demand          0
            groups            [ 0 ]
            bandwidth         0
            qos-group         default-group
            border             not set
            unknown-attr-len  not set

        ---------------------------------------------------
        tloc entries for 100.100.100.20
                        default
                        ipsec
        ---------------------------------------------------
                    RECEIVED FROM:                   
        peer            100.100.100.3
        status          C,I,R
        loss-reason     not set
        lost-to-peer    not set
        lost-to-path-id not set
            Attributes:
            attribute-type    installed
            encap-key         not set
            encap-proto       0
            encap-spi         355
            encap-auth        sha1-hmac,ah-sha1-hmac
            encap-encrypt     aes256
            public-ip         12.12.13.2
            public-port       12426
            private-ip        12.12.13.2
            private-port      12426
            public-ip         ::
            public-port       0
            private-ip        ::
            private-port      0
            bfd-status        up
            domain-id         not set
            site-id           102
            overlay-id        not set
            preference        0
            tag               not set
            stale             not set
            weight            1
            version           3
            gen-id             0x80000011
            carrier           default
            restrict          0
            on-demand          0
            groups            [ 0 ]
            bandwidth         0
            qos-group         default-group
            border             not set
            unknown-attr-len  not set

        ---------------------------------------------------
        tloc entries for 100.100.100.30
                        default
                        ipsec
        ---------------------------------------------------
                    RECEIVED FROM:                   
        peer            100.100.100.3
        status          C,I,R
        loss-reason     not set
        lost-to-peer    not set
        lost-to-path-id not set
            Attributes:
            attribute-type    installed
            encap-key         not set
            encap-proto       0
            encap-spi         359
            encap-auth        sha1-hmac,ah-sha1-hmac
            encap-encrypt     aes256
            public-ip         11.11.11.10
            public-port       12426
            private-ip        11.11.11.10
            private-port      12426
            public-ip         ::
            public-port       0
            private-ip        ::
            private-port      0
            bfd-status        up
            domain-id         not set
            site-id           103
            overlay-id        not set
            preference        0
            tag               not set
            stale             not set
            weight            1
            version           3
            gen-id             0x80000022
            carrier           default
            restrict          0
            on-demand          0
            groups            [ 0 ]
            bandwidth         0
            qos-group         default-group
            border             not set
            unknown-attr-len  not set
     '''}
     
    golden_parsed_output = {
        'tloc_data': {
            '100.100.100.10': {
                'tloc': {
                    'default': {
                        'transport': 'ipsec',
                        'received_from': {
                            'peer': '0.0.0.0',
                            'status': ['C', 'Red', 'R'],
                            'loss_reason': 'not_set',
                            'lost_to_peer': 'not_set',
                            'lost_to_path_id': 'not_set',
                            'attributes': {
                            'attribute_type': 'installed',
                            'encap_key': 'not_set',
                            'encap_proto': 0,
                            'encap_spi': 365,
                            'encap_auth': ['sha1-hmac', 'ah-sha1-hmac'],
                            'encap_encrypt': 'aes256',
                            'public_ip': '::',
                            'public_port': 0,
                            'private_ip': '::',
                            'private_port': 0,
                            'bfd_status': 'up',
                            'site_id': 101,
                            'preference': 0,
                            'tag': 'not_set',
                            'stale': 'not_set',
                            'weight': 1,
                            'version': 3,
                            'gen_id': '0x80000003',
                            'carrier': 'default',
                            'restrict': 0,
                            'on_demand': 0,
                            'groups': [0],
                            'bandwidth': 0,
                            'qos_group': 'default_group',
                            'border': 'not_set',
                            'unknown_attr_len': 'not_set'
                            }
                        }
                    }
                }
            },
            '100.100.100.20': {
                'tloc': {
                    'default': {
                        'transport': 'ipsec',
                        'received_from': {
                            'peer': '100.100.100.3',
                            'status': ['C', 'I', 'R'],
                            'loss_reason': 'not_set',
                            'lost_to_peer': 'not_set',
                            'lost_to_path_id': 'not_set',
                            'attributes': {
                            'attribute_type': 'installed',
                            'encap_key': 'not_set',
                            'encap_proto': 0,
                            'encap_spi': 355,
                            'encap_auth': ['sha1-hmac', 'ah-sha1-hmac'],
                            'encap_encrypt': 'aes256',
                            'public_ip': '::',
                            'public_port': 0,
                            'private_ip': '::',
                            'private_port': 0,
                            'bfd_status': 'up',
                            'site_id': 102,
                            'preference': 0,
                            'tag': 'not_set',
                            'stale': 'not_set',
                            'weight': 1,
                            'version': 3,
                            'gen_id': '0x80000011',
                            'carrier': 'default',
                            'restrict': 0,
                            'on_demand': 0,
                            'groups': [0],
                            'bandwidth': 0,
                            'qos_group': 'default_group',
                            'border': 'not_set',
                            'unknown_attr_len': 'not_set'
                            }
                        }
                    }
                }
            },
            '100.100.100.30': {
                'tloc': {
                    'default': {
                        'transport': 'ipsec',
                        'received_from': {
                            'peer': '100.100.100.3',
                            'status': ['C', 'I', 'R'],
                            'loss_reason': 'not_set',
                            'lost_to_peer': 'not_set',
                            'lost_to_path_id': 'not_set',
                            'attributes': {
                            'attribute_type': 'installed',
                            'encap_key': 'not_set',
                            'encap_proto': 0,
                            'encap_spi': 359,
                            'encap_auth': ['sha1-hmac', 'ah-sha1-hmac'],
                            'encap_encrypt': 'aes256',
                            'public_ip': '::',
                            'public_port': 0,
                            'private_ip': '::',
                            'private_port': 0,
                            'bfd_status': 'up',
                            'site_id': 103,
                            'preference': 0,
                            'tag': 'not_set',
                            'stale': 'not_set',
                            'weight': 1,
                            'version': 3,
                            'gen_id': '0x80000022',
                            'carrier': 'default',
                            'restrict': 0,
                            'on_demand': 0,
                            'groups': [0],
                            'bandwidth': 0,
                            'qos_group': 'default_group',
                            'border': 'not_set',
                            'unknown_attr_len': 'not_set'
                            }
                        }
                    }
                }
            }
        }
    }                    

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanOmpTlocs(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanOmpTlocs(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
		unittest.main()        
