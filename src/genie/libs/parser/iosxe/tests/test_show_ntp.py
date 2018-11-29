# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_ntp import ShowNtpAssociations, \
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
            {'associations_address': '127.127.1.1',
             'associations_local_mode': 'client',
             'clock_offset': 0.0,
             'clock_refid': '.LOCL.',
             'clock_state': 'unsynchronized',
             'clock_stratum': 0,
             'root_delay': 0.0}
            },
    'peer':
        {'1.1.1.1':
            {'local_mode':
                {'client':
                    {'delay': 0.0,
                    'jitter': 15937.0,
                    'mode': 'configured',
                    'offset': 0.0,
                    'poll': 1024,
                    'reach': 0,
                    'receive_time': '-',
                    'refid': '.INIT.',
                    'remote': '1.1.1.1',
                    'stratum': 16,
                    'local_mode': 'client'}
                }
            },
        '127.127.1.1':
            {'local_mode':
                {'client':
                    {'delay': 0.0,
                    'jitter': 1.204,
                    'mode': 'synchronized',
                    'offset': 0.0,
                    'poll': 16,
                    'reach': 377,
                    'receive_time': 6,
                    'refid': '.LOCL.',
                    'remote': '127.127.1.1',
                    'stratum': 0,
                    'local_mode': 'client'}
                }
            },
        '2.2.2.2':
            {'local_mode':
                {'client':
                    {'delay': 0.0,
                    'jitter': 15937.0,
                    'mode': 'configured',
                    'offset': 0.0,
                    'poll': 1024,
                    'reach': 0,
                    'receive_time': '-',
                    'refid': '.INIT.',
                    'remote': '2.2.2.2',
                    'stratum': 16,
                    'local_mode': 'client'}
                }
            }
        }
    }


    golden_output_1 = {'execute.return_value': '''
        R1#show ntp associations

          address         ref clock       st   when   poll reach  delay  offset   disp
        *~127.127.1.1     .LOCL.           0      6     16   377  0.000   0.000  1.204
         ~1.1.1.1         .INIT.          16      -   1024     0  0.000   0.000 15937.
         ~1.1.1.1         .INIT.          16      -   1024     0  0.000   0.000 15937.
         ~2.2.2.2         .INIT.          16      -   1024     0  0.000   0.000 15937.
         ~2.2.2.2         .INIT.          16      -   1024     0  0.000   0.000 15937.
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

# ==============================================
# Unit test for 'show ntp status'
# ==============================================
class test_show_ntp_status(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output_1 = {
        'clock_state': {'system_status': {'act_freq': 250.0,
                                   'drift': '0.000000000 s/s',
                                   'last_update': '9 sec ago',
                                   'leap_status': "'CTRL' (Normal "
                                                  'Controlled Loop)',
                                   'nom_freq': 250.0,
                                   'offset': 0.0,
                                   'peerdispersion': 1.2,
                                   'poll': 16,
                                   'precision': '2**10',
                                   'refid': '.LOCL.',
                                   'reftime': 'DF9FFBA0.8B020DC8 '
                                              '(15:43:28.543 UTC Wed Nov '
                                              '21 2018)',
                                   'resolution': 4000,
                                   'rootdelay': 0.0,
                                   'rootdispersion': 2.31,
                                   'status': 'synchronized',
                                   'stratum': 1,
                                   'uptime': '1921500 (1/100 of seconds)'}}
    }

    golden_output_1 = {'execute.return_value': '''\
        R1#show ntp status
        Clock is synchronized, stratum 1, reference is .LOCL.
        nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
        ntp uptime is 1921500 (1/100 of seconds), resolution is 4000
        reference time is DF9FFBA0.8B020DC8 (15:43:28.543 UTC Wed Nov 21 2018)
        clock offset is 0.0000 msec, root delay is 0.00 msec
        root dispersion is 2.31 msec, peer dispersion is 1.20 msec
        loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000000000 s/s
        system poll interval is 16, last update was 9 sec ago.
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


# ===========================================================
# Unit test for 'show ntp config'
# ===========================================================
class test_show_ntp_config(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output_1 = {
        'vrf': {
            'VRF1': {
                'address': {
                    '4.4.4.4': {
                        'isconfigured': {
                            'True': {
                                'address': '4.4.4.4',
                                'isconfigured': True}
                        },
                        'type': {
                            'server': {
                                'address': '4.4.4.4',
                                'type': 'server',
                                'vrf': 'VRF1'}
                        }
                    }
                }
            },
            'default': {
                'address': {
                    '1.1.1.1': {
                        'isconfigured': {
                            'True': {
                                'address': '1.1.1.1',
                                'isconfigured': True}
                            },
                        'type': {
                            'server': {
                                'address': '1.1.1.1',
                                'type': 'server',
                                'vrf': 'default'}
                        }
                    },
                    '2.2.2.2': {
                        'isconfigured': {
                            'True': {
                                'address': '2.2.2.2',
                                'isconfigured': True}
                        },
                        'type': {
                            'server': {
                                'address': '2.2.2.2',
                                'type': 'server',
                                'vrf': 'default'}
                        }
                    }
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        R1#show ntp config
        ntp server 1.1.1.1
        ntp server 2.2.2.2
        ntp server vrf VRF1 4.4.4.4
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