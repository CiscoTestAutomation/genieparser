# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.junos.show_ntp import ShowNtpAssociations, \
                                             ShowNtpStatus, \
                                             ShowConfigurationSystemNtpSet

#=========================================================
# Unit test for show ntp associations
#=========================================================
class test_show_ntp_associations(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        'clock_state': {'system_status': {'associations_address': '172.16.229.65',
                                          'associations_local_mode': 'active',
                                          'clock_offset': 73.819,
                                          'clock_refid': '.GNSS.',
                                          'clock_state': 'synchronized',
                                          'clock_stratum': 1,
                                          'root_delay': 1.436}},
        'peer': {'10.2.2.2': {'local_mode': {'active': {'delay': 1.47,
                                                        'jitter': 52.506,
                                                        'mode': 'falseticker',
                                                        'offset': -46.76,
                                                        'poll': 128,
                                                        'reach': 271,
                                                        'receive_time': 84,
                                                        'refid': '172.16.229.65',
                                                        'remote': '10.2.2.2',
                                                        'stratum': 2,
                                                        'type': 'active'}}},
                '172.16.229.65': {'local_mode': {'active': {'delay': 1.436,
                                                            'jitter': 10.905,
                                                            'mode': 'synchronized',
                                                            'offset': 73.819,
                                                            'poll': 64,
                                                            'reach': 377,
                                                            'receive_time': 59,
                                                            'refid': '.GNSS.',
                                                            'remote': '172.16.229.65',
                                                            'stratum': 1,
                                                            'type': 'active'}}},
                '172.16.229.66': {'local_mode': {'active': {'delay': 0.969,
                                                            'jitter': 8.964,
                                                            'mode': 'final '
                                                                    'selection '
                                                                    'set',
                                                            'offset': 59.428,
                                                            'poll': 64,
                                                            'reach': 377,
                                                            'receive_time': 63,
                                                            'refid': '.GNSS.',
                                                            'remote': '172.16.229.66',
                                                            'stratum': 1,
                                                            'type': 'active'}}},
                '10.145.32.44': {'local_mode': {'active': {'delay': 42.72,
                                                            'jitter': 6.228,
                                                            'mode': 'final '
                                                                    'selection '
                                                                    'set',
                                                            'offset': 64.267,
                                                            'poll': 64,
                                                            'reach': 377,
                                                            'receive_time': 61,
                                                            'refid': '.GNSS.',
                                                            'remote': '10.145.32.44',
                                                            'stratum': 1,
                                                            'type': 'active'}}}}
    }


    golden_output_1 = {'execute.return_value': '''
        root@junos_vmx1> show ntp associations
           remote         refid           st t when poll reach   delay   offset  jitter
        ===============================================================================
        x10.2.2.2         172.16.229.65     2 -   84  128  271    1.470  -46.760  52.506
        *172.16.229.65     .GNSS.           1 -   59   64  377    1.436   73.819  10.905
        +172.16.229.66     .GNSS.           1 -   63   64  377    0.969   59.428   8.964
        +10.145.32.44     .GNSS.           1 -   61   64  377   42.720   64.267   6.228
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
        'clock_state': {'system_status': {'clock': 'df981ae8.eb6e7ee8  Thu, Nov 15 2018 11:18:48.919',
                                          'frequency': 4.968,
                                          'jitter': 12.27,
                                          'leap_status': 'leap_none',
                                          'number_of_events': 4,
                                          'offset': 67.812,
                                          'peer': 22765,
                                          'poll': 6,
                                          'precision': -23.0,
                                          'processor': 'amd64',
                                          'recent_event': 'event_peer/strat_chg',
                                          'refid': '172.16.229.65',
                                          'reftime': 'df981acf.bfa97435  Thu, Nov 15 2018 11:18:23.748',
                                          'rootdelay': 1.434,
                                          'rootdispersion': 82.589,
                                          'stability': 0.89,
                                          'state': 4,
                                          'status': '0644',
                                          'stratum': 2,
                                          'leap': '00',
                                          'synch_source': 'sync_ntp',
                                          'system': 'FreeBSDJNPR-11.0-20171206.f4cad52_buil',
                                          'version': 'ntpd 4.2.0-a Tue Dec 19 '
                                                     '21:12:44  2017 (1)'}}
    }

    golden_output_1 = {'execute.return_value': '''\
        root@junos_vmx1> show ntp status
        status=0644 leap_none, sync_ntp, 4 events, event_peer/strat_chg,
        version="ntpd 4.2.0-a Tue Dec 19 21:12:44  2017 (1)", processor="amd64",
        system="FreeBSDJNPR-11.0-20171206.f4cad52_buil", leap=00, stratum=2,
        precision=-23, rootdelay=1.434, rootdispersion=82.589, peer=22765,
        refid=172.16.229.65,
        reftime=df981acf.bfa97435  Thu, Nov 15 2018 11:18:23.748, poll=6,
        clock=df981ae8.eb6e7ee8  Thu, Nov 15 2018 11:18:48.919, state=4,
        offset=67.812, frequency=4.968, jitter=12.270, stability=0.890
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
# Unit test for 'show configuration system ntp | display set'
# ===========================================================
class test_show_configuration_system_ntp_display_set(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output_1 = {'vrf': {'default': {'address': {'10.2.2.2': {'isconfigured': {'True': {'address': '10.2.2.2',
                                                                        'isconfigured': True}},
                                              'type': {'peer': {'address': '10.2.2.2',
                                                                'type': 'peer',
                                                                'vrf': 'default'}}}}},
         'mgmt_junos': {'address': {'172.16.229.65': {'isconfigured': {'True': {'address': '172.16.229.65',
                                                                               'isconfigured': True}},
                                                     'type': {'server': {'address': '172.16.229.65',
                                                                         'type': 'server',
                                                                         'vrf': 'mgmt_junos'}}},
                                    '172.16.229.66': {'isconfigured': {'True': {'address': '172.16.229.66',
                                                                               'isconfigured': True}},
                                                     'type': {'server': {'address': '172.16.229.66',
                                                                         'type': 'server',
                                                                         'vrf': 'mgmt_junos'}}},
                                    '10.145.32.44': {'isconfigured': {'True': {'address': '10.145.32.44',
                                                                               'isconfigured': True}},
                                                     'type': {'server': {'address': '10.145.32.44',
                                                                         'type': 'server',
                                                                         'vrf': 'mgmt_junos'}}}}}}
    }

    golden_output_1 = {'execute.return_value': '''\
        root@junos_vmx1> show configuration system ntp | display set 
        set system ntp peer 10.2.2.2
        set system ntp server 172.16.229.65 routing-instance mgmt_junos
        set system ntp server 172.16.229.66 routing-instance mgmt_junos
        set system ntp server 10.145.32.44 routing-instance mgmt_junos
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowConfigurationSystemNtpSet(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowConfigurationSystemNtpSet(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()
