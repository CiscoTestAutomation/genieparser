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
                                             ShowNtpConfig, \
                                             ShowNtpAssociationsDetail

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
             'clock_state': 'synchronized',
             'clock_stratum': 0,
             'root_delay': 0.0}
            },
    'peer':
        {'10.4.1.1':
            {'local_mode':
                {'client':
                    {'delay': 0.0,
                    'jitter': 15937.0,
                    'mode': 'unsynchronized',
                    'offset': 0.0,
                    'poll': 1024,
                    'reach': 0,
                    'receive_time': '-',
                    'refid': '.INIT.',
                    'remote': '10.4.1.1',
                    'stratum': 16,
                    'configured': True,
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
                    'configured': True,
                    'local_mode': 'client'}
                }
            },
        '10.16.2.2':
            {'local_mode':
                {'client':
                    {'delay': 0.0,
                    'jitter': 15937.0,
                    'mode': 'unsynchronized',
                    'offset': 0.0,
                    'poll': 1024,
                    'reach': 0,
                    'receive_time': '-',
                    'refid': '.INIT.',
                    'remote': '10.16.2.2',
                    'stratum': 16,
                    'configured': True,
                    'local_mode': 'client'}
                }
            }
        }
    }


    golden_output_1 = {'execute.return_value': '''
        R1#show ntp associations

          address         ref clock       st   when   poll reach  delay  offset   disp
        *~127.127.1.1     .LOCL.           0      6     16   377  0.000   0.000  1.204
         ~10.4.1.1        .INIT.          16      -   1024     0  0.000   0.000 15937.
         ~10.4.1.1        .INIT.          16      -   1024     0  0.000   0.000 15937.
         ~10.16.2.2       .INIT.          16      -   1024     0  0.000   0.000 15937.
         ~10.16.2.2       .INIT.          16      -   1024     0  0.000   0.000 15937.
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
                    '10.64.4.4': {
                        'isconfigured': {
                            'True': {
                                'address': '10.64.4.4',
                                'isconfigured': True}
                        },
                        'type': {
                            'server': {
                                'address': '10.64.4.4',
                                'type': 'server',
                                'vrf': 'VRF1'}
                        }
                    }
                }
            },
            'default': {
                'address': {
                    '10.4.1.1': {
                        'isconfigured': {
                            'True': {
                                'address': '10.4.1.1',
                                'isconfigured': True}
                            },
                        'type': {
                            'server': {
                                'address': '10.4.1.1',
                                'type': 'server',
                                'vrf': 'default'}
                        }
                    },
                    '10.16.2.2': {
                        'isconfigured': {
                            'True': {
                                'address': '10.16.2.2',
                                'isconfigured': True}
                        },
                        'type': {
                            'server': {
                                'address': '10.16.2.2',
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
        ntp server 10.4.1.1
        ntp server 10.16.2.2
        ntp server vrf VRF1 10.64.4.4
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


#=========================================================
# Unit test for show ntp associations detail
#=========================================================
class test_show_ntp_associations_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    'vrf': {
        'default': {
            'associations': {
                'address': {
                    '192.168.255.254': {
                        'local_mode': {
                            'client': {
                                'isconfigured': {
                                    'True': {
                                        'ip_type': 'ipv4',
                                        'selected': False,
                                        'unsynced': False,
                                        'address': '192.168.255.254',
                                        'isconfigured': True,
                                        'authenticated': True,
                                        'sane': False,
                                        'valid': False,
                                        'master': False,
                                        'stratum': 3,
                                        'refid': '172.16.255.254',
                                        'input_time': 'DBAB02D6.9E354130 (16:08:06.618 EST Fri Oct 14 2016)',
                                        'peer_interface': '172.16.255.254',
                                        'poll': '512',
                                        'vrf': 'default',
                                        'local_mode': 'client',
                                        'peer': {
                                            '172.16.255.254': {
                                                'local_mode': {
                                                    'server': {
                                                        'poll': 512,
                                                        'local_mode': 'server',
                                                        },
                                                    },
                                                },
                                            },
                                        'root_delay_msec': '0.00',
                                        'root_disp': '14.52',
                                        'reach': '377',
                                        'sync_dist': '28.40',
                                        'delay_msec': '0.00',
                                        'offset_msec': '0.0000',
                                        'dispersion': '7.23',
                                        'jitter_msec': '0.97',
                                        'precision': '2**10',
                                        'version': 4,
                                        'assoc_name': '192.168.255.254',
                                        'assoc_id': 62758,
                                        'ntp_statistics': {
                                            'packet_received': 27,
                                            'packet_sent': 27,
                                            'packet_dropped': 0,
                                            },
                                        'originate_time': '00000000.00000000 (09:00:00.000 EST Mon Jan 1 1900)',
                                        'receive_time': 'DBAB046D.A8B43B28 (16:14:53.659 EST Fri Oct 14 2016)',
                                        'transmit_time': 'DBAB046D.A8B43B28 (16:14:53.659 EST Fri Oct 14 2016)',
                                        'filtdelay': '0.00    1.00    0.00    0.00    0.00    0.00    0.00    0.00',
                                        'filtoffset': '0.00    0.50    0.00    1.00    1.00    1.00    1.00    1.00',
                                        'filterror': '1.95    5.89    9.88   13.89   15.84   17.79   19.74   21.76',
                                        'minpoll': 6,
                                        'maxpoll': 10,
                                        },
                                    },
                                },
                            },
                        },
                    '172.16.255.254': {
                        'local_mode': {
                            'client': {
                                'isconfigured': {
                                    'True': {
                                        'ip_type': 'ipv4',
                                        'selected': False,
                                        'unsynced': False,
                                        'address': '172.16.255.254',
                                        'isconfigured': True,
                                        'authenticated': True,
                                        'sane': True,
                                        'valid': True,
                                        'master': True,
                                        'stratum': 2,
                                        'refid': '127.127.1.1',
                                        'input_time': 'DBAB05B9.753F7E30 (16:20:25.458 EST Fri Oct 14 2016)',
                                        'peer_interface': '127.127.1.1',
                                        'poll': '512',
                                        'vrf': 'default',
                                        'local_mode': 'client',
                                        'peer': {
                                            '127.127.1.1': {
                                                'local_mode': {
                                                    'server': {
                                                        'poll': 512,
                                                        'local_mode': 'server',
                                                        },
                                                    },
                                                },
                                            },
                                        'root_delay_msec': '0.00',
                                        'root_disp': '2.18',
                                        'reach': '177',
                                        'sync_dist': '9.47',
                                        'delay_msec': '0.00',
                                        'offset_msec': '-1.0000',
                                        'dispersion': '5.64',
                                        'jitter_msec': '0.97',
                                        'precision': '2**10',
                                        'version': 4,
                                        'assoc_name': '172.16.255.254',
                                        'assoc_id': 62756,
                                        'ntp_statistics': {
                                            'packet_received': 38,
                                            'packet_sent': 50,
                                            'packet_dropped': 0,
                                            },
                                        'originate_time': '00000000.00000000 (09:00:00.000 EST Mon Jan 1 1900)',
                                        'receive_time': 'DBAB05BA.A8B43B28 (16:20:26.659 EST Fri Oct 14 2016)',
                                        'transmit_time': 'DBAB05BA.A8B43B28 (16:20:26.659 EST Fri Oct 14 2016)',
                                        'filtdelay': '1.00    1.00    1.00    1.00    0.00    1.00    1.00    0.00',
                                        'filtoffset': '-0.50   -0.50   -0.50   -0.50   -1.00   -0.50   -0.50   -1.00',
                                        'filterror': '1.95    2.88    3.81    4.74    5.08    5.11    7.53    8.46',
                                        'minpoll': 6,
                                        'maxpoll': 10,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


    golden_output = {'execute.return_value': '''
        Router#show ntp associations detail
        Load for five secs: 1%/0%; one minute: 3%; five minutes: 4%
        Time source is NTP, 16:21:12.433 EST Fri Oct 14 2016

        192.168.255.254 configured, ipv4, authenticated (' ' reject), insane, invalid, stratum 3
        ref ID 172.16.255.254, time DBAB02D6.9E354130 (16:08:06.618 EST Fri Oct 14 2016)
        our mode client, peer mode server, our poll intvl 512, peer poll intvl 512
        root delay 0.00 msec, root disp 14.52, reach 377, sync dist 28.40
        delay 0.00 msec, offset 0.0000 msec, dispersion 7.23, jitter 0.97 msec
        precision 2**10, version 4
        assoc id 62758, assoc name 192.168.255.254
        assoc in packets 27, assoc out packets 27, assoc error packets 0
        org time 00000000.00000000 (09:00:00.000 EST Mon Jan 1 1900)
        rec time DBAB046D.A8B43B28 (16:14:53.659 EST Fri Oct 14 2016)
        xmt time DBAB046D.A8B43B28 (16:14:53.659 EST Fri Oct 14 2016)
        filtdelay =     0.00    1.00    0.00    0.00    0.00    0.00    0.00    0.00
        filtoffset =    0.00    0.50    0.00    1.00    1.00    1.00    1.00    1.00
        filterror =     1.95    5.89    9.88   13.89   15.84   17.79   19.74   21.76
        minpoll = 6, maxpoll = 10

        172.16.255.254 configured, ipv4, authenticated, our_master, sane, valid, stratum 2
        ref ID 127.127.1.1    , time DBAB05B9.753F7E30 (16:20:25.458 EST Fri Oct 14 2016)
        our mode client, peer mode server, our poll intvl 512, peer poll intvl 512
        root delay 0.00 msec, root disp 2.18, reach 177, sync dist 9.47
        delay 0.00 msec, offset -1.0000 msec, dispersion 5.64, jitter 0.97 msec
        precision 2**10, version 4
        assoc id 62756, assoc name 172.16.255.254
        assoc in packets 38, assoc out packets 50, assoc error packets 0
        org time 00000000.00000000 (09:00:00.000 EST Mon Jan 1 1900)
        rec time DBAB05BA.A8B43B28 (16:20:26.659 EST Fri Oct 14 2016)
        xmt time DBAB05BA.A8B43B28 (16:20:26.659 EST Fri Oct 14 2016)
        filtdelay =     1.00    1.00    1.00    1.00    0.00    1.00    1.00    0.00
        filtoffset =   -0.50   -0.50   -0.50   -0.50   -1.00   -0.50   -0.50   -1.00
        filterror =     1.95    2.88    3.81    4.74    5.08    5.11    7.53    8.46
        minpoll = 6, maxpoll = 10
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNtpAssociationsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowNtpAssociationsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()