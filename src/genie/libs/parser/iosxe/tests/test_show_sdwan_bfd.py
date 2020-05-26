# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_bfd import ShowSdwanBfdSessions, ShowSdwanBfdSummary


# ============================================
# Parser for the following commands
#   * 'show sdwan bfd sessions'
# ============================================
class TestShowSdwanBfdSessions(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
    # show bfd sessions
                                        SOURCE TLOC      REMOTE TLOC                       DST PUBLIC       DST PUBLIC         DETECT      TX                              
    SYSTEM IP        SITE ID  STATE       COLOR            COLOR            SOURCE IP        IP               PORT        ENCAP  MULTIPLIER  INTERVAL(msec)  UPTIME        TRANSITIONS
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    172.16.241.1     30001001 up          mpls             mpls             184.116.102.2    174.11.1.2       12346       ipsec  20          1000           0:01:46:50      0           
    172.16.241.1     30001001 up          private1         mpls             186.116.102.2    174.11.1.2       12346       ipsec  20          1000           0:01:46:51      0           
    172.16.241.2     30001002 up          mpls             mpls             184.116.102.2    174.11.2.2       12346       ipsec  20          1000           0:01:41:27      2           
    172.16.241.2     30001002 up          private1         mpls             186.116.102.2    174.11.2.2       12346       ipsec  20          1000           0:01:41:28      2         
    '''}

    golden_parsed_output = {
        'system_ip': {
            '172.16.241.1': {
                'source_tloc_color': {
                    'mpls': {
                        'destination_public_ip': '174.11.1.2',
                        'destination_public_port': '12346',
                        'detect_multiplier': '20',
                        'encapsulation': 'ipsec',
                        'remote_tloc_color': 'mpls',
                        'site_id': '30001001',
                        'source_ip': '184.116.102.2',
                        'state': 'up',
                        'transitions': '0',
                        'tx_interval': '1000',
                        'uptime': '0:01:46:50',
                    },
                    'private1': {
                        'destination_public_ip': '174.11.1.2',
                        'destination_public_port': '12346',
                        'detect_multiplier': '20',
                        'encapsulation': 'ipsec',
                        'remote_tloc_color': 'mpls',
                        'site_id': '30001001',
                        'source_ip': '186.116.102.2',
                        'state': 'up',
                        'transitions': '0',
                        'tx_interval': '1000',
                        'uptime': '0:01:46:51',
                    },
                },
            },
            '172.16.241.2': {
                'source_tloc_color': {
                    'mpls': {
                        'destination_public_ip': '174.11.2.2',
                        'destination_public_port': '12346',
                        'detect_multiplier': '20',
                        'encapsulation': 'ipsec',
                        'remote_tloc_color': 'mpls',
                        'site_id': '30001002',
                        'source_ip': '184.116.102.2',
                        'state': 'up',
                        'transitions': '2',
                        'tx_interval': '1000',
                        'uptime': '0:01:41:27',
                    },
                    'private1': {
                        'destination_public_ip': '174.11.2.2',
                        'destination_public_port': '12346',
                        'detect_multiplier': '20',
                        'encapsulation': 'ipsec',
                        'remote_tloc_color': 'mpls',
                        'site_id': '30001002',
                        'source_ip': '186.116.102.2',
                        'state': 'up',
                        'transitions': '2',
                        'tx_interval': '1000',
                        'uptime': '0:01:41:28',
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanBfdSessions(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanBfdSessions(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ============================================
# Parser for the following commands
#   * 'show sdwan bfd summary'
# ============================================
class TestShowSdwanBfdSummary(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}

    golden_output = {'execute.return_value': '''
        # show bfd summary
        sessions-total         4
        sessions-up            4
        sessions-max           4
        sessions-flap          4
        poll-interval          600000
    '''}

    golden_parsed_output = {
        'poll_interval': 600000,
        'sessions_flap': 4,
        'sessions_max': 4,
        'sessions_total': 4,
        'sessions_up': 4
        }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanBfdSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanBfdSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
		unittest.main()        