#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_mpls import ShowMplsLdpParameters


class test_show_mpls_ldp_parameters(unittest.TestCase):
    dev1 = Device(name='empty')
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'ldp_featureset_manager': {
            'State Initialized': {
                'ldp_features': [
                    'Auto-Configuration',
                    'Basic',
                    'ICPM',
                    'IP-over-MPLS',
                    'IGP-Sync',
                    'LLAF',
                    'TCP-MD5-Rollover',
                    'TDP',
                    'NSR'],
            },
        },
        'ldp_backoff': {
            'initial': 15,
            'maximum': 120,
        },
        'ldp_loop_detection': "off",
        'ldp_nsr': 'disabled',
        'ldp_for_targeted_sessions': True,
        'version': 1,
        'session_hold_time': 180,
        'keep_alive_interval': 60,
        'discovery_targeted_hello': {
            'holdtime': 90,
            'interval': 10,
        },
        'discovery_hello': {
            'holdtime': 15,
            'interval': 5,
        },
        'downstream_on_demand_max_hop_count': 255,
    }


    golden_output = {'execute.return_value': '''\

    Router#show mpls ldp parameters
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:10.454 JST Tue Nov 8 2016
    LDP Feature Set Manager: State Initialized
      LDP features:
        Auto-Configuration
        Basic
        ICPM
        IP-over-MPLS
        IGP-Sync
        LLAF
        TCP-MD5-Rollover
        TDP
        NSR
    Protocol version: 1
    Session hold time: 180 sec; keep alive interval: 60 sec
    Discovery hello: holdtime: 15 sec; interval: 5 sec
    Discovery targeted hello: holdtime: 90 sec; interval: 10 sec
    Downstream on Demand max hop count: 255
    LDP for targeted sessions
    LDP initial/maximum backoff: 15/120 sec
    LDP loop detection: off
    LDP NSR: Disabled
    Router#
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpParameters(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpParameters(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()