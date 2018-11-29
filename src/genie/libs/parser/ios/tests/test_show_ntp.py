# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.ios.show_ntp import ShowNtpAssociations, \
                                           ShowNtpStatus, \
                                           ShowNtpConfig

#=========================================================
# Unit test for show ntp associations
#=========================================================
class test_show_ntp_associations(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
    'clock_state':
        {'system_status':
            {'associations_address': '2.2.2.2',
             'associations_local_mode': 'client',
             'clock_offset': 27.027,
             'clock_refid': '127.127.1.1',
             'clock_state': 'unsynchronized',
             'clock_stratum': 3,
             'root_delay': 5.61}
        },
    'peer':
        {'2.2.2.2':
            {'local_mode':
                {'client':
                    {'delay': 5.61,
                    'jitter': 3.342,
                    'mode': 'synchronized',
                    'offset': 27.027,
                    'poll': 64,
                    'reach': 7,
                    'receive_time': 25,
                    'refid': '127.127.1.1',
                    'remote': '2.2.2.2',
                    'stratum': 3,
                    'local_mode': 'client'}
                }
            },
        '3.3.3.3':
            {'local_mode':
                {'client':
                    {'delay': 0.0,
                    'jitter': 15937.0,
                    'mode': 'configured',
                    'offset': 0.0,
                    'poll': 512,
                    'reach': 0,
                    'receive_time': '-',
                    'refid': '.STEP.',
                    'remote': '3.3.3.3',
                    'stratum': 16,
                    'local_mode': 'client'}
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        iosv-1#show ntp associations 

          address         ref clock       st   when   poll reach  delay  offset   disp
        *~2.2.2.2         127.127.1.1      3     25     64     7  5.610  27.027  3.342
         ~3.3.3.3         .STEP.          16      -    512     0  0.000   0.000 15937.
         * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
    '''
    }

    golden_parsed_output_2 = {
        'clock_state': {
            'system_status': {
                'associations_address': '2.2.2.2',
                'associations_local_mode': 'client',
                'clock_offset': 27.027,
                'clock_refid': '127.127.1.1',
                'clock_state': 'unsynchronized',
                'clock_stratum': 3,
                'root_delay': 5.61}
        },
        'peer': {
            '2.2.2.2': {
                'local_mode': {
                    'client': {
                        'delay': 5.61,
                        'jitter': 3.342,
                        'local_mode': 'client',
                        'mode': 'synchronized',
                        'offset': 27.027,
                        'poll': 64,
                        'reach': 7,
                        'receive_time': 25,
                        'refid': '127.127.1.1',
                        'remote': '2.2.2.2',
                        'stratum': 3}
                }
            },
            '3.3.3.3': {
                'local_mode': {
                    'client': {
                        'delay': 0.0,
                        'jitter': 15937.0,
                        'local_mode': 'client',
                        'mode': 'configured',
                        'offset': 0.0,
                        'poll': 512,
                        'reach': 0,
                        'receive_time': '-',
                        'refid': '.STEP.',
                        'remote': '3.3.3.3',
                        'stratum': 16}
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
        show ntp associations

          address         ref clock       st   when   poll reach  delay  offset   disp
         ~2.2.2.2         127.127.1.1      3     41     64     0  0.000   0.000 15937.
         ~3.3.3.3         .INIT.          16      -     64     0  0.000   0.000 15937.
         * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNtpAssociations(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowNtpAssociations(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowNtpAssociations(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


# ==============================================
# Unit test for 'show ntp status'
# ==============================================
class test_show_ntp_status(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output_1 = {
        'clock_state': {
            'system_status': {
                'act_freq': 1000.4589,
                'last_update': '182 sec ago',
                'nom_freq': 1000.0003,
                'offset': 27.0279,
                'peerdispersion': 3.34,
                'poll': 64,
                'precision': '2**14',
                'refid': '2.2.2.2',
                'reftime': 'DFA02517.D2F7B9F6 '
                           '(13:40:23.824 EST Wed Nov '
                           '21 2018)',
                'resolution': 1000,
                'rootdelay': 5.61,
                'rootdispersion': 273.61,
                'status': 'synchronized',
                'stratum': 4,
                'uptime': '239700 (1/100 of seconds)'}
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        iosv-1#show ntp status 
        Clock is synchronized, stratum 4, reference is 2.2.2.2        
        nominal freq is 1000.0003 Hz, actual freq is 1000.4589 Hz, precision is 2**14
        ntp uptime is 239700 (1/100 of seconds), resolution is 1000
        reference time is DFA02517.D2F7B9F6 (13:40:23.824 EST Wed Nov 21 2018)
        clock offset is 27.0279 msec, root delay is 5.61 msec
        root dispersion is 273.61 msec, peer dispersion is 3.34 msec
        loopfilter state is 'CTRL' (Normal Controlled Loop), drift is -0.000458631 s/s
        system poll interval is 64, last update was 182 sec ago.
    '''
    }

    golden_parsed_output_2 = {
        'clock_state': {
            'system_status': {
                'act_freq': 1000.4923,
                'last_update': '1301 sec ago',
                'nom_freq': 1000.0003,
                'offset': 0.0,
                'peerdispersion': 0.0,
                'poll': 64,
                'precision': '2**13',
                'reftime': 'DFA98D6B.F2F229A7 '
                           '(16:55:55.949 EST Wed Nov '
                           '28 2018)',
                'resolution': 1000,
                'rootdelay': 0.0,
                'rootdispersion': 18.84,
                'status': 'unsynchronized',
                'stratum': 16,
                'uptime': '1938800 (1/100 of seconds)'}
        }
    }

    golden_output_2 = {'execute.return_value': '''\
        show ntp status
        Clock is unsynchronized, stratum 16, no reference clock
        nominal freq is 1000.0003 Hz, actual freq is 1000.4923 Hz, precision is 2**13
        ntp uptime is 1938800 (1/100 of seconds), resolution is 1000
        reference time is DFA98D6B.F2F229A7 (16:55:55.949 EST Wed Nov 28 2018)
        clock offset is 0.0000 msec, root delay is 0.00 msec
        root dispersion is 18.84 msec, peer dispersion is 0.00 msec
        loopfilter state is 'SPIK' (Spike), drift is -0.000491998 s/s
        system poll interval is 64, last update was 1301 sec ago.
        iosv-1
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNtpStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowNtpStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowNtpStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)


# ===========================================================
# Unit test for 'show ntp config'
# ===========================================================
class test_show_ntp_config(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output_1 = {
        'vrf': {
            'default': {
                'address': {
                    '2.2.2.2': {
                        'isconfigured': {
                            'True': {
                                'address': '2.2.2.2',
                                'isconfigured': True}
                        },
                        'type': {
                            'server': {
                                'address': '2.2.2.2',
                                'source': 'Loopback0',
                                'type': 'server',
                                'vrf': 'default'}
                        }
                    },
                    '3.3.3.3': {
                        'isconfigured': {
                            'True': {
                                'address': '3.3.3.3',
                                'isconfigured': True}
                        },
                        'type': {
                            'server': {
                                'address': '3.3.3.3',
                                'type': 'server',
                                'vrf': 'default'}
                        }
                    }
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        iosv-1#show ntp config
         ntp server 2.2.2.2 source Loopback0
         ntp server 3.3.3.3
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNtpConfig(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowNtpConfig(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()