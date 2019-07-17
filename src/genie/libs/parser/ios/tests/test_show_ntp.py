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
            {'associations_address': '10.16.2.2',
             'associations_local_mode': 'client',
             'clock_offset': 27.027,
             'clock_refid': '127.127.1.1',
             'clock_state': 'synchronized',
             'clock_stratum': 3,
             'root_delay': 5.61}
        },
    'peer':
        {'10.16.2.2':
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
                    'remote': '10.16.2.2',
                    'stratum': 3,
                    'configured': True,
                    'local_mode': 'client'}
                }
            },
        '10.36.3.3':
            {'local_mode':
                {'client':
                    {'delay': 0.0,
                    'jitter': 15937.0,
                    'mode': 'unsynchronized',
                    'offset': 0.0,
                    'poll': 512,
                    'reach': 0,
                    'receive_time': '-',
                    'refid': '.STEP.',
                    'remote': '10.36.3.3',
                    'stratum': 16,
                    'configured': True,
                    'local_mode': 'client'}
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        iosv-1#show ntp associations 

          address         ref clock       st   when   poll reach  delay  offset   disp
        *~10.16.2.2       127.127.1.1      3     25     64     7  5.610  27.027  3.342
         ~10.36.3.3       .STEP.          16      -    512     0  0.000   0.000 15937.
         * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
    '''}

    golden_parsed_output_2 = {
        'clock_state': {
            'system_status': {
                'clock_state': 'unsynchronized'
            }
        },
        'peer': {
            '10.16.2.2': {
                'local_mode': {
                    'client': {
                        'delay': 0.0,
                        'jitter': 15937.0,
                        'local_mode': 'client',
                        'mode': 'unsynchronized',
                        'offset': 0.0,
                        'poll': 64,
                        'reach': 0,
                        'receive_time': 41,
                        'refid': '127.127.1.1',
                        'remote': '10.16.2.2',
                        'configured': True,
                        'stratum': 3}
                }
            },
            '10.36.3.3': {
                'local_mode': {
                    'client': {
                        'delay': 0.0,
                        'jitter': 15937.0,
                        'local_mode': 'client',
                        'mode': 'unsynchronized',
                        'offset': 0.0,
                        'poll': 64,
                        'reach': 0,
                        'receive_time': '-',
                        'refid': '.INIT.',
                        'remote': '10.36.3.3',
                        'configured': True,
                        'stratum': 16}
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
        show ntp associations

          address         ref clock       st   when   poll reach  delay  offset   disp
         ~10.16.2.2       127.127.1.1      3     41     64     0  0.000   0.000 15937.
         ~10.36.3.3       .INIT.          16      -     64     0  0.000   0.000 15937.
         * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
    '''}

    golden_parsed_output_3 = {
        'clock_state': {
            'system_status': {
                'associations_address': '192.168.13.57',
                                     'associations_local_mode': 'client',
                                     'clock_offset': 11.18,
                                     'clock_refid': '192.168.1.111',
                                     'clock_state': 'synchronized',
                                     'clock_stratum': 3,
                                     'root_delay': 7.9}},
        'peer': {
            '172.31.32.2': {
                'local_mode': {
                    'client': {
                        'configured': True,
                             'delay': 4.2,
                             'jitter': 1.6,
                             'local_mode': 'client',
                             'mode': 'None',
                             'offset': -8.59,
                             'poll': 1024,
                             'reach': 377,
                             'receive_time': 29,
                             'refid': '172.31.32.1',
                             'remote': '172.31.32.2',
                             'stratum': 5
                    }
                }
            },
            '192.168.13.33': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 4.1,
                        'jitter': 2.3,
                        'local_mode': 'client',
                        'mode': 'selected',
                        'offset': 3.48,
                        'poll': 128,
                        'reach': 377,
                        'receive_time': 69,
                        'refid': '192.168.1.111',
                        'remote': '192.168.13.33',
                        'stratum': 3
                    }
                }
            },
            '192.168.13.57': {
                'local_mode': {
                    'client': {
                        'configured': True,
                        'delay': 7.9,
                        'jitter': 3.6,
                        'local_mode': 'client',
                        'mode': 'synchronized',
                        'offset': 11.18,
                        'poll': 128,
                        'reach': 377,
                        'receive_time': 32,
                        'refid': '192.168.1.111',
                        'remote': '192.168.13.57',
                        'stratum': 3
                    }
                }
            }
        }
    }

    golden_output_3 = {'execute.return_value': '''
        Router#show ntp associations 

        address            ref clock         st      when    poll   reach   delay   offset    disp
        *~192.168.13.57    192.168.1.111     3       32      128    377     7.9     11.18     3.6  
        ~172.31.32.2       172.31.32.1       5       29      1024   377     4.2     -8.59     1.6 
        +~192.168.13.33    192.168.1.111     3       69      128    377     4.1     3.48      2.3 
        * master (synced), # master (unsynced), + selected, - candidate, ~ configured
    '''}

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
        self.device = Mock(**self.golden_output_2)
        obj = ShowNtpAssociations(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowNtpAssociations(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)


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
                'refid': '10.16.2.2',
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
        Clock is synchronized, stratum 4, reference is 10.16.2.2        
        nominal freq is 1000.0003 Hz, actual freq is 1000.4589 Hz, precision is 2**14
        ntp uptime is 239700 (1/100 of seconds), resolution is 1000
        reference time is DFA02517.D2F7B9F6 (13:40:23.824 EST Wed Nov 21 2018)
        clock offset is 27.0279 msec, root delay is 5.61 msec
        root dispersion is 273.61 msec, peer dispersion is 3.34 msec
        loopfilter state is 'CTRL' (Normal Controlled Loop), drift is -0.000458631 s/s
        system poll interval is 64, last update was 182 sec ago.
    '''}

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
    '''}

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
                    '10.16.2.2': {
                        'isconfigured': {
                            'True': {
                                'address': '10.16.2.2',
                                'isconfigured': True}
                        },
                        'type': {
                            'server': {
                                'address': '10.16.2.2',
                                'source': 'Loopback0',
                                'type': 'server',
                                'vrf': 'default'}
                        }
                    },
                    '10.36.3.3': {
                        'isconfigured': {
                            'True': {
                                'address': '10.36.3.3',
                                'isconfigured': True}
                        },
                        'type': {
                            'server': {
                                'address': '10.36.3.3',
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
         ntp server 10.16.2.2 source Loopback0
         ntp server 10.36.3.3
    '''}

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


class test_show_ntp_associations_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Device> show ntp associations detail
        172.31.32.2 configured, insane, invalid, stratum 5
        ref ID 172.31.32.1, time AFE252C1.6DBDDFF2 (00:12:01.428 PDT Mon Jul 5 1993)
        our mode active, peer mode active, our poll intvl 1024, peer poll intvl 64
        root delay 137.77 msec, root disp 142.75, reach 376, sync dist 215.363
        delay 4.23 msec, offset -8.587 msec, dispersion 1.62
        precision 2**19, version 4
        assoc ID 1, assoc name 192.168.1.55,
        assoc in packets 60, assoc out packets 60, assoc error packets 0
        org time AFE252E2.3AC0E887 (00:12:34.229 PDT Tue Oct 4 2011)
        rcv time AFE252E2.3D7E464D (00:12:34.240 PDT Mon Jan 1 1900)
        xmt time AFE25301.6F83E753 (00:13:05.435 PDT Tue Oct 4 2011)
        filtdelay =     4.23    4.14    2.41    5.95    2.37    2.33    4.26    4.33
        filtoffset =   -8.59   -8.82   -9.91   -8.42  -10.51  -10.77  -10.13  -10.11
        filterror =     0.50    1.48    2.46    3.43    4.41    5.39    6.36    7.34

        192.168.13.33 configured, selected, sane, valid, stratum 3
        ref ID 192.168.1.111, time AFE24F0E.14283000 (23:56:14.078 PDT Sun Jul 4 1993)
        our mode client, peer mode server, our poll intvl 128, peer poll intvl 128
        root delay 83.72 msec, root disp 217.77, reach 377, sync dist 264.633
        delay 4.07 msec, offset 3.483 msec, dispersion 2.33
        precision 2**6, version 3
        assoc ID 2, assoc name myserver
        assoc in packets 0, assoc out packets 0, assoc error packets 0
        org time AFE252B9.713E9000 (00:11:53.442 PDT Tue Oct 4 2011)
        rcv time AFE252B9.7124E14A (00:11:53.441 PDT Mon Jan 1 1900)
        xmt time AFE252B9.6F625195 (00:11:53.435 PDT Mon Jan 1 1900)
        filtdelay =     6.47    4.07    3.94    3.86    7.31    7.20    9.52    8.71
        filtoffset =    3.63    3.48    3.06    2.82    4.51    4.57    4.28    4.59
        filterror =     0.00    1.95    3.91    4.88    5.84    6.82    7.80    8.77
        
        192.168.13.57 configured, our_master, sane, valid, stratum 3
        ref ID 192.168.1.111, time AFE252DC.1F2B3000 (00:12:28.121 PDT Mon Jul 5 1993)
        our mode client, peer mode server, our poll intvl 128, peer poll intvl 128
        root delay 125.50 msec, root disp 115.80, reach 377, sync dist 186.157
        delay 7.86 msec, offset 11.176 msec, dispersion 3.62
        precision 2**6, version 2
        assoc ID 2, assoc name myserver
        assoc in packets 0, assoc out packets 0, assoc error packets 0
        org time AFE252DE.77C29000 (00:12:30.467 PDT Tue Oct 4 2011)
        rcv time AFE252DE.7B2AE40B (00:12:30.481 PDT Mon Jan 1 1900)
        xmt time AFE252DE.6E6D12E4 (00:12:30.431 PDT Mon Jan 1 1900)
        filtdelay =    49.21    7.86    8.18    8.80    4.30    4.24    7.58    6.42
        filtoffset =   11.30   11.18   11.13   11.28    8.91    9.09    9.27    9.57
        filterror =     0.00    1.95    3.91    4.88    5.78    6.76    7.74    8.71
    '''}

    golden_parsed_output = {
        "vrf": {
            "default": {
                "associations": {
                    "address": {
                        "172.31.32.2": {
                            "local_mode": {
                                "active": {
                                    "isconfigured": {
                                        "True": {
                                            "selected": False,
                                            "unsynced": False,
                                            "address": "172.31.32.2",
                                            "isconfigured": True,
                                            "authenticated": False,
                                            "sane": False,
                                            "valid": False,
                                            "master": False,
                                            "stratum": 5,
                                            "refid": "172.31.32.1",
                                            "input_time": "AFE252C1.6DBDDFF2 (00:12:01.428 PDT Mon Jul 5 1993)",
                                            "peer_interface": "172.31.32.1",
                                            "poll": "1024",
                                            "vrf": "default",
                                            "local_mode": "active",
                                            "peer": {
                                                "172.31.32.1": {
                                                    "local_mode": {
                                                        "active": {
                                                            "poll": 64,
                                                            "local_mode": "active"
                                                        }
                                                    }
                                                }
                                            },
                                            "root_delay_msec": "137.77",
                                            "root_disp": "142.75",
                                            "reach": "376",
                                            "sync_dist": "215.363",
                                            "delay_msec": "4.23",
                                            "offset_msec": "-8.587",
                                            "dispersion": "1.62",
                                            "jitter_msec": "None",
                                            "precision": "2**19",
                                            "version": 4,
                                            "assoc_name": "192.168.1.55",
                                            "assoc_id": 1,
                                            "ntp_statistics": {
                                                "packet_received": 60,
                                                "packet_sent": 60,
                                                "packet_dropped": 0
                                            },
                                            "originate_time": "AFE252E2.3AC0E887 (00:12:34.229 PDT Tue Oct 4 2011)",
                                            "receive_time": "AFE252E2.3D7E464D (00:12:34.240 PDT Mon Jan 1 1900)",
                                            "transmit_time": "AFE25301.6F83E753 (00:13:05.435 PDT Tue Oct 4 2011)",
                                            "filtdelay": "4.23    4.14    2.41    5.95    2.37    2.33    4.26    4.33",
                                            "filtoffset": "-8.59   -8.82   -9.91   -8.42  -10.51  -10.77  -10.13  -10.11",
                                            "filterror": "0.50    1.48    2.46    3.43    4.41    5.39    6.36    7.34"
                                        }
                                    }
                                }
                            }
                        },
                        "192.168.13.33": {
                            "local_mode": {
                                "client": {
                                    "isconfigured": {
                                        "True": {
                                            "selected": True,
                                            "unsynced": False,
                                            "address": "192.168.13.33",
                                            "isconfigured": True,
                                            "authenticated": False,
                                            "sane": True,
                                            "valid": True,
                                            "master": False,
                                            "stratum": 3,
                                            "refid": "192.168.1.111",
                                            "input_time": "AFE24F0E.14283000 (23:56:14.078 PDT Sun Jul 4 1993)",
                                            "peer_interface": "192.168.1.111",
                                            "poll": "128",
                                            "vrf": "default",
                                            "local_mode": "client",
                                            "peer": {
                                                "192.168.1.111": {
                                                    "local_mode": {
                                                        "server": {
                                                            "poll": 128,
                                                            "local_mode": "server"
                                                        }
                                                    }
                                                }
                                            },
                                            "root_delay_msec": "83.72",
                                            "root_disp": "217.77",
                                            "reach": "377",
                                            "sync_dist": "264.633",
                                            "delay_msec": "4.07",
                                            "offset_msec": "3.483",
                                            "dispersion": "2.33",
                                            "jitter_msec": "None",
                                            "precision": "2**6",
                                            "version": 3,
                                            "assoc_name": "myserver",
                                            "assoc_id": 2,
                                            "ntp_statistics": {
                                                "packet_received": 0,
                                                "packet_sent": 0,
                                                "packet_dropped": 0
                                            },
                                            "originate_time": "AFE252B9.713E9000 (00:11:53.442 PDT Tue Oct 4 2011)",
                                            "receive_time": "AFE252B9.7124E14A (00:11:53.441 PDT Mon Jan 1 1900)",
                                            "transmit_time": "AFE252B9.6F625195 (00:11:53.435 PDT Mon Jan 1 1900)",
                                            "filtdelay": "6.47    4.07    3.94    3.86    7.31    7.20    9.52    8.71",
                                            "filtoffset": "3.63    3.48    3.06    2.82    4.51    4.57    4.28    4.59",
                                            "filterror": "0.00    1.95    3.91    4.88    5.84    6.82    7.80    8.77"
                                        }
                                    }
                                }
                            }
                        },
                        "192.168.13.57": {
                            "local_mode": {
                                "client": {
                                    "isconfigured": {
                                        "True": {
                                            "selected": False,
                                            "unsynced": False,
                                            "address": "192.168.13.57",
                                            "isconfigured": True,
                                            "authenticated": False,
                                            "sane": True,
                                            "valid": True,
                                            "master": True,
                                            "stratum": 3,
                                            "refid": "192.168.1.111",
                                            "input_time": "AFE252DC.1F2B3000 (00:12:28.121 PDT Mon Jul 5 1993)",
                                            "peer_interface": "192.168.1.111",
                                            "poll": "128",
                                            "vrf": "default",
                                            "local_mode": "client",
                                            "peer": {
                                                "192.168.1.111": {
                                                    "local_mode": {
                                                        "server": {
                                                            "poll": 128,
                                                            "local_mode": "server"
                                                        }
                                                    }
                                                }
                                            },
                                            "root_delay_msec": "125.50",
                                            "root_disp": "115.80",
                                            "reach": "377",
                                            "sync_dist": "186.157",
                                            "delay_msec": "7.86",
                                            "offset_msec": "11.176",
                                            "dispersion": "3.62",
                                            "jitter_msec": "None",
                                            "precision": "2**6",
                                            "version": 2,
                                            "assoc_name": "myserver",
                                            "assoc_id": 2,
                                            "ntp_statistics": {
                                                "packet_received": 0,
                                                "packet_sent": 0,
                                                "packet_dropped": 0
                                            },
                                            "originate_time": "AFE252DE.77C29000 (00:12:30.467 PDT Tue Oct 4 2011)",
                                            "receive_time": "AFE252DE.7B2AE40B (00:12:30.481 PDT Mon Jan 1 1900)",
                                            "transmit_time": "AFE252DE.6E6D12E4 (00:12:30.431 PDT Mon Jan 1 1900)",
                                            "filtdelay": "49.21    7.86    8.18    8.80    4.30    4.24    7.58    6.42",
                                            "filtoffset": "11.30   11.18   11.13   11.28    8.91    9.09    9.27    9.57",
                                            "filterror": "0.00    1.95    3.91    4.88    5.78    6.76    7.74    8.71"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowNtpAssociationsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowNtpAssociationsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()
