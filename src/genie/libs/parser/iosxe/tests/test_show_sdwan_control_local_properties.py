# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_control_local_properties import ShowSdwanControlLocalProperties


# ============================================
# Parser for the following commands
#   * 'show sdwan control local-properties'
# ============================================
class TestShowSdwanControlLocalProperties(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    
    golden_output = {'execute.return_value': '''
        vEdge# show control local-properties
        personality                  vedge
        organization-name            Cisco, Inc.
        certificate-status           Installed
        root-ca-chain-status         Installed

        certificate-validity         Valid
        certificate-not-valid-before Dec 15 18:06:59 2016 GMT
        certificate-not-valid-after  Dec 15 18:06:59 2017 GMT

        dns-name                     10.0.12.26
        site-id                      100
        domain-id                    1
        protocol                     dtls
        tls-port                     0
        system-ip                    172.16.255.11
        chassis-num/unique-id        b5887dd3-3d70-4987-a3a4-6e06c1d64a8c
        serial-num                   12345714
        vsmart-list-version          0
        keygen-interval              1:00:00:00
        retry-interval               0:00:00:19
        no-activity-exp-interval     0:00:00:12
        dns-cache-ttl                0:00:02:00
        port-hopped                  TRUE
        time-since-last-port-hop     0:00:43:16
        number-vbond-peers           0
        number-active-wan-interfaces 1

        NAT TYPE: E -- indicates End-point independent mapping
                A -- indicates Address-port dependent mapping
                N -- indicates Not learned
                Note: Requires minimum two vbonds to learn the NAT type
                                                                                                                                                                                            VM
                   PUBLIC          PUBLIC PRIVATE         PRIVATE                                 PRIVATE                             MAX     CONTROL/            LAST         SPI TIME   NAT  CON
        INTERFACE  IPv4            PORT   IPv4            IPv6                                    PORT    VS/VM COLOR           STATE CNTRL   STUN         LR/LB  CONNECTION   REMAINING  TYPE PRF
        ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        ge0/0      10.1.15.15      12426  10.1.15.15      ::                                      12426    0/0  lte              up    2      no/yes/no   No/No  0:00:00:16   0:11:26:41  E    5
        ge0/3      10.0.20.15      12406  10.0.20.15      ::                                      12406    0/0  3g               up    2      no/yes/no   No/No  0:00:00:13   0:11:26:45  N    5    
    '''}

    golden_parsed_output = {
        'certificate_not_valid_after': 'Dec 15 18:06:59 2017 GMT',
        'certificate_not_valid_before': 'Dec 15 18:06:59 2016 GMT',
        'certificate_status': 'Installed',
        'certificate_validity': 'Valid',
        'chassis_num_unique_id': 'b5887dd3-3d70-4987-a3a4-6e06c1d64a8c',
        'wan_interfaces': {
            'ge0/0': {
                'color': 'lte',
                'control': 'yes',
                'last_connection': '0:00:00:16',
                'lb': 'No',
                'lr': 'No',
                'max_cntrl': '2',
                'nat_type': 'E',
                'private_ipv4': '10.1.15.15',
                'private_ipv6': '::',
                'private_port': '12426',
                'public_ipv4': '10.1.15.15',
                'public_port': '12426',
                'restrict': 'no',
                'spi_time_remaining': '0:11:26:41',
                'state': 'up',
                'stun': 'no',
                'vm_con_prf': '5',
                'vmanage': '0',
                'vsmart': '0',
            },
            'ge0/3': {
                'color': '3g',
                'control': 'yes',
                'last_connection': '0:00:00:13',
                'lb': 'No',
                'lr': 'No',
                'max_cntrl': '2',
                'nat_type': 'N',
                'private_ipv4': '10.0.20.15',
                'private_ipv6': '::',
                'private_port': '12406',
                'public_ipv4': '10.0.20.15',
                'public_port': '12406',
                'restrict': 'no',
                'spi_time_remaining': '0:11:26:45',
                'state': 'up',
                'stun': 'no',
                'vm_con_prf': '5',
                'vmanage': '0',
                'vsmart': '0',
            },
        },
        'dns_cache_ttl': '0:00:02:00',
        'dns_name': '10.0.12.26',
        'domain_id': '1',
        'keygen_interval': '1:00:00:00',
        'no_activity_exp_interval': '0:00:00:12',
        'number_active_wan_interfaces': '1',
        'number_vbond_peers': '0',
        'organization_name': 'Cisco, Inc.',
        'personality': 'vedge',
        'port_hopped': 'TRUE',
        'protocol': 'dtls',
        'retry_interval': '0:00:00:19',
        'root_ca_chain_status': 'Installed',
        'serial_num': '12345714',
        'site_id': '100',
        'system_ip': '172.16.255.11',
        'time_since_last_port_hop': '0:00:43:16',
        'tls_port': '0',
    } 

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanControlLocalProperties(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanControlLocalProperties(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
		unittest.main()      