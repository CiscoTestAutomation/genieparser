# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxr.show_ntp import ShowNtpAssociations, \
                                             ShowNtpStatus, \
                                             ShowRunningConfigNtp

#=========================================================
# Unit test for show ntp associations
#=========================================================
class test_show_ntp_associations(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'clock_state': {
            'system_status': {
                'associations_address': '172.19.69.1',
                'associations_local_mode': 'client',
                'clock_offset': 67.16,
                'clock_refid': '172.24.114.33',
                'clock_state': 'synchronized',
                'clock_stratum': 3,
                'root_delay': 2.0}
        },
        'peer': {
            '127.127.1.1': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 0.0,
                        'jitter': 438.3,
                        'local_mode': 'client',
                        'mode': 'candidate',
                        'offset': 0.0,
                        'poll': 1024,
                        'reach': 37,
                        'receive_time': 5,
                        'refid': '127.127.1.1',
                        'remote': '127.127.1.1',
                        'stratum': 5}
                }
            },
            '172.19.69.1': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 2.0,
                        'jitter': 0.0,
                        'local_mode': 'client',
                        'mode': 'synchronized',
                        'offset': 67.16,
                        'poll': 1024,
                        'reach': 1,
                        'receive_time': 13,
                        'refid': '172.24.114.33',
                        'remote': '172.19.69.1',
                        'stratum': 3}
                }
            }
        },
        'vrf': {
            'default': {
                'address': {
                    '127.127.1.1': {
                        'isconfigured': {
                            True: {
                                'address': '127.127.1.1',
                                'isconfigured': True}
                        },
                        'type': {
                            'peer': {
                                'address': '127.127.1.1',
                                'type': 'peer',
                                'vrf': 'default'}
                        }
                    },
                    '172.19.69.1': {
                        'isconfigured': {
                            True: {
                                'address': '172.19.69.1',
                                'isconfigured': True}
                        },
                        'type': {
                            'peer': {
                                'address': '172.19.69.1',
                                'type': 'peer',
                                'vrf': 'default'}
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show ntp associations

              address         ref clock     st  when  poll reach  delay  offset    disp
        +~127.127.1.1      127.127.1.1       5     5  1024   37     0.0    0.00   438.3
        *~172.19.69.1      172.24.114.33     3    13  1024    1     2.0   67.16     0.0
         * master (synced), # master (unsynced), + selected, - candidate, ~ configured
    '''
    }

    golden_parsed_output_1 = {
        'clock_state': {
            'system_status': {
                'clock_state': 'unsynchronized'}
        },
        'peer': {
            '10.4.1.1': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 0.0,
                        'jitter': 15937.0,
                        'local_mode': 'client',
                        'mode': 'unsynchronized',
                        'offset': 0.0,
                        'poll': 1024,
                        'reach': 0,
                        'receive_time': '-',
                        'refid': '.AUTH.',
                        'remote': '10.4.1.1',
                        'stratum': 16}
                }
            },
            '10.16.2.2': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 69.18,
                        'jitter': 4.702,
                        'local_mode': 'client',
                        'mode': 'unsynchronized',
                        'offset': -518066.0,
                        'poll': 64,
                        'reach': 377,
                        'receive_time': 52,
                        'refid': '127.127.1.1',
                        'remote': '10.16.2.2',
                        'stratum': 9}
                }
            },
            '10.64.4.4': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 0.0,
                        'jitter': 15937.0,
                        'local_mode': 'client',
                        'mode': 'unsynchronized',
                        'offset': 0.0,
                        'poll': 1024,
                        'reach': 0,
                        'receive_time': '-',
                        'refid': '.AUTH.',
                        'remote': '10.64.4.4',
                        'stratum': 16}
                }
            },
            '10.100.5.5': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 0.0,
                        'jitter': 15937.0,
                        'local_mode': 'client',
                        'mode': 'unsynchronized',
                        'offset': 0.0,
                        'poll': 1024,
                        'reach': 0,
                        'receive_time': '-',
                        'refid': '.AUTH.',
                        'remote': '10.100.5.5',
                        'stratum': 16}
                }
            },
            '10.144.6.6': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 0.0,
                        'jitter': 15937.0,
                        'local_mode': 'client',
                        'mode': 'unsynchronized',
                        'offset': 0.0,
                        'poll': 1024,
                        'reach': 0,
                        'receive_time': '-',
                        'refid': '.AUTH.',
                        'remote': '10.144.6.6',
                        'stratum': 16}
                }
            }
        },
        'vrf': {
            'VRF1': {
                'address': {
                    '10.4.1.1': {
                        'isconfigured': {
                            True: {
                                'address': '10.4.1.1',
                                'isconfigured': True}
                        },
                        'type': {
                            'peer': {
                                'address': '10.4.1.1',
                                'type': 'peer',
                                'vrf': 'VRF1'}
                        }
                    },
                    '10.100.5.5': {
                        'isconfigured': {
                            True: {
                                'address': '10.100.5.5',
                                'isconfigured': True}
                        },
                        'type': {
                            'peer': {
                                'address': '10.100.5.5',
                                'type': 'peer',
                                'vrf': 'VRF1'}
                        }
                    },
                    '10.144.6.6': {
                        'isconfigured': {
                            True: {
                                'address': '10.144.6.6',
                                'isconfigured': True}
                        },
                        'type': {
                            'peer': {
                                'address': '10.144.6.6',
                                'type': 'peer',
                                'vrf': 'VRF1'}
                        }
                    }
                }
            },
            'default': {
                'address': {
                    '10.4.1.1': {
                        'isconfigured': {
                            True: {
                                'address': '10.4.1.1',
                                'isconfigured': True}
                        },
                        'type': {
                            'peer': {
                                'address': '10.4.1.1',
                                'type': 'peer',
                                'vrf': 'default'}
                        }
                    },
                    '10.16.2.2': {
                        'isconfigured': {
                            True: {
                                'address': '10.16.2.2',
                                'isconfigured': True}
                        },
                        'type': {
                            'peer': {
                                'address': '10.16.2.2',
                                'type': 'peer',
                                'vrf': 'default'}
                        }
                    },
                    '10.64.4.4': {
                        'isconfigured': {
                            True: {
                                'address': '10.64.4.4',
                                'isconfigured': True}
                        },
                        'type': {
                            'peer': {
                                'address': '10.64.4.4',
                                'type': 'peer',
                                'vrf': 'default'}
                        }
                    }
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:iosxrv9000-1#show ntp associations 
        Mon Nov  5 23:22:25.521 UTC

              address         ref clock     st  when  poll reach  delay  offset    disp
         ~10.4.1.1 vrf VRF1
                           .INIT.           16     -  1024    0    0.00   0.000   15937
         ~10.4.1.1          .AUTH.           16     -  1024    0    0.00   0.000   15937
         ~10.16.2.2          127.127.1.1       9    52    64  377   69.18  -518066   4.702
         ~10.64.4.4          .AUTH.           16     -  1024    0    0.00   0.000   15937
         ~10.100.5.5 vrf VRF1
                           .AUTH.           16     -  1024    0    0.00   0.000   15937
         ~10.144.6.6 vrf VRF1
                           .AUTH.           16     -  1024    0    0.00   0.000   15937
         * sys_peer, # selected, + candidate, - outlayer, x falseticker, ~ configured
    '''
    }

    golden_parsed_output_2 = {
        'clock_state': {
            'system_status': {
                'associations_address': '192.168.128.5',
                'associations_local_mode': 'client',
                'clock_offset': -0.56,
                'clock_refid': '10.81.254.131',
                'clock_state': 'synchronized',
                'clock_stratum': 2,
                'root_delay': 7.98}
        },
        'peer': {
            '192.168.128.5': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 7.98,
                        'jitter': 0.108,
                        'local_mode': 'client',
                        'mode': 'synchronized',
                        'offset': -0.56,
                        'poll': 64,
                        'reach': 377,
                        'receive_time': 1,
                        'refid': '10.81.254.131',
                        'remote': '192.168.128.5',
                        'stratum': 2}
                }
            },
            '2001:db8:429a:3189::2': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 6.0,
                        'jitter': 0.046,
                        'local_mode': 'client',
                        'mode': 'candidate',
                        'offset': -2.832,
                        'poll': 64,
                        'reach': 377,
                        'receive_time': 20,
                        'refid': '172.16.36.80',
                        'remote': '2001:db8:429a:3189::2',
                        'stratum': 3}
                }
            }
        },
        'vrf': {
            'default': {
                'address': {
                    '192.168.128.5': {
                        'isconfigured': {
                            True: {
                                'address': '192.168.128.5',
                                'isconfigured': True}
                        },
                        'type': {
                            'peer': {
                                'address': '192.168.128.5',
                                'type': 'peer',
                                'vrf': 'default'}
                        }
                    }
                }
            },
            'testAA': {
                'address': {
                    '2001:db8:429a:3189::2': {
                        'isconfigured': {
                            True: {
                                'address': '2001:db8:429a:3189::2',
                                'isconfigured': True}
                        },
                        'type': {
                            'peer': {
                                'address': '2001:db8:429a:3189::2',
                                'type': 'peer',
                                'vrf': 'testAA'}
                        }
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show ntp associations 
          
        Tue Oct  7 11:22:46.839 EST 
           
              address         ref clock     st  when  poll reach  delay  offset    disp
        *~192.168.128.5    10.81.254.131     2     1    64  377    7.98  -0.560   0.108
        +~2001:db8:429a:3189::2 vrf testAA
                           172.16.36.80      3    20    64  377    6.00  -2.832   0.046
        * sys_peer, # selected, + candidate, - outlayer, x falseticker, ~ configured
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNtpAssociations(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowNtpAssociations(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowNtpAssociations(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowNtpAssociations(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# ==============================================
# Unit test for 'show ntp status'
# ==============================================
class test_show_ntp_status(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'clock_state': {
            'system_status': {
                'act_freq': 1000.2725,
                'drift': '-0.0002724105 s/s',
                'last_update': '66 sec ago',
                'leap_status': "'CTRL' (Normal "
                                'Controlled Loop)',
                'nom_freq': 1000.0,
                'offset': -1.738,
                'peerdispersion': 0.09,
                'poll': 64,
                'precision': '2**24',
                'refid': '192.168.128.5',
                'reftime': 'CC95463C.9B964367 '
                           '(11:21:48.607 EST Tue Oct  '
                           '7 2008)',
                'rootdelay': 186.05,
                'rootdispersion': 53.86,
                'status': 'synchronized',
                'stratum': 3}
        }
    }

    golden_output = {'execute.return_value': '''\
        RP/0/RP0/CPU0:router# show ntp status 
          
        Tue Oct  7 11:22:54.023 EST 
          
        Clock is synchronized, stratum 3, reference is 192.168.128.5
        nominal freq is 1000.0000 Hz, actual freq is 1000.2725 Hz, precision is 2**24
        reference time is CC95463C.9B964367 (11:21:48.607 EST Tue Oct  7 2008)
        clock offset is -1.738 msec, root delay is 186.050 msec
        root dispersion is 53.86 msec, peer dispersion is 0.09 msec
        loopfilter state is 'CTRL' (Normal Controlled Loop), drift is -0.0002724105 s/s
        system poll interval is 64, last update was 66 sec ago
    '''
    }

    golden_parsed_output_1 = {
        'clock_state': {
            'system_status': {
                'act_freq': 999.9988,
                'nom_freq': 1000.0,
                'offset': 66.3685,
                'peerdispersion': 3.38,
                'precision': '2**26',
                'refid': '172.19.69.1',
                'reftime': 'C54C131B.9EECF6CA '
                           '(07:26:19.620 UTC Mon Nov '
                           '24 2008)',
                'rootdelay': 7.8,
                'rootdispersion': 950.04,
                'status': 'synchronized',
                'stratum': 4}
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        RP/0/RP0/CPU0:router# show ntp status

        Clock is synchronized, stratum 4, reference is 172.19.69.1
        nominal freq is 1000.0000 Hz, actual freq is 999.9988 Hz, precision is 2**26
        reference time is C54C131B.9EECF6CA (07:26:19.620 UTC Mon Nov 24 2008)
        clock offset is 66.3685 msec, root delay is 7.80 msec
        root dispersion is 950.04 msec, peer dispersion is 3.38 msec
    '''
    }

    golden_parsed_output_2 = {
        'clock_state': {
            'system_status': {
                'act_freq': 1000000000.0,
                'drift': '0.0000000000 s/s',
                'last_update': 'never updated',
                'leap_status': "'NSET' (Never set)",
                'nom_freq': 1000000000.0,
                'offset': 0.0,
                'peerdispersion': 0.0,
                'poll': 64,
                'precision': '2**23',
                'reftime': '00000000.00000000 '
                           '(00:00:00.000 UTC Thu Jan  '
                           '1 1970)',
                'rootdelay': 0.0,
                'rootdispersion': 101.71,
                'status': 'unsynchronized',
                'stratum': 16}
        }
    }

    golden_output_2 = {'execute.return_value': '''\
        RP/0/RP0/CPU0:iosxrv9000-1#show ntp status
        Mon Nov  5 23:23:09.761 UTC

        Clock is unsynchronized, stratum 16, no reference clock
        nominal freq is 1000000000.0000 Hz, actual freq is 1000000000.0000 Hz, precision is 2**23
        reference time is 00000000.00000000 (00:00:00.000 UTC Thu Jan  1 1970)
        clock offset is 0.000 msec, root delay is 0.000 msec
        root dispersion is 101.71 msec, peer dispersion is 0.00 msec
        loopfilter state is 'NSET' (Never set), drift is 0.0000000000 s/s
        system poll interval is 64, never updated
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNtpStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowNtpStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

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


# ==============================================
# Unit test for 'show running-config ntp'
# ==============================================
class test_show_run_ntp(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'vrf': {
            'default': {
                'address': {
                    '10.4.1.1': {
                        'type': 'server'}
                }
            },
            'management': {
                'address': {
                    '10.4.1.1': {
                        'type': 'server'}
                }
            }
        }
    }


    golden_output = {'execute.return_value': '''\
        +++ dev: executing command 'show running-config ntp' +++
        show running-config ntp

        Thu Sep 26 18:20:16.484 EDT
        ntp
         server 10.4.1.1
         server vrf management 10.4.1.1
        !
    '''
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRunningConfigNtp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowRunningConfigNtp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()