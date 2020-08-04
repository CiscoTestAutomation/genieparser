import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_omp import ShowSdwanOmpSummary


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


if __name__ == '__main__':
		unittest.main()        
