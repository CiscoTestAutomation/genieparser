# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_system_status import ShowSdwanSystemStatus


# ============================================
# Parser for the following commands
#   * 'show sdwan system status'
# ============================================
class TestShowSdwanSystemStatus(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        srp_vedge# show system status

        Viptela (tm) vedge Operating System Software
        Copyright (c) 2013-2020 by Viptela, Inc.
        Controller Compatibility: 20.3
        Version: 99.99.999-4567
        Build: 4567


        System logging to host  is disabled
        System logging to disk is enabled

        System state:            GREEN. All daemons up
        System FIPS state:       Enabled
        Testbed mode:            Enabled
        Engineering Signed       True

        Last reboot:             Initiated by user - activate 99.99.999-4567.
        CPU-reported reboot:     Not Applicable
        Boot loader version:     Not applicable
        System uptime:           0 days 21 hrs 35 min 28 sec
        Current time:            Thu Aug 06 02:49:25 PDT 2020

        Load average:            1 minute: 3.20, 5 minutes: 3.13, 15 minutes: 3.10
        Processes:               250 total
        CPU allocation:          4 total,   1 control,   3 data
        CPU states:              1.25% user,   5.26% system,   93.48% idle
        Memory usage:            1907024K total,    1462908K used,   444116K free
                                0K buffers,  0K cache

        Disk usage:              Filesystem      Size   Used  Avail   Use %  Mounted on
                                /dev/root       7615M  447M  6741M   6%   /


        Personality:             vedge
        Model name:              vedge-cloud
        Services:                None
        vManaged:                true
        Commit pending:          false
        Configuration template:  CLItemplate_srp_vedge
        Chassis serial number:   None
    '''}

    golden_parsed_output = {'boot_loader_version': 'Not applicable',
                            'build': '4567',
                            'chassis_serial_number': 'None',
                            'commit_pending': 'false',
                            'configuration_template': 'CLItemplate_srp_vedge',
                            'controller_compatibility': '20.3',
                            'cpu_allocation': {'control': 1, 'data': 3, 'total': 4},
                            'cpu_reported_reboot': 'Not Applicable',
                            'engineering_signed': True,
                            'cpu_states': {'idle': 93.48, 'system': 5.26, 'user': 1.25},
                            'current_time': 'Thu Aug 06 02:49:25 PDT 2020',
                            'disk_usage': {'avail_mega': 6741,
                                            'filesystem': '/dev/root',
                                            'mounted_on': '/',
                                            'size_mega': 7615,
                                            'use_pc': 6,
                                            'used_mega': 447},
                            'last_reboot': 'Initiated by user - activate 99.99.999-4567.',
                            'load_average': {'minute_1': 3.20, 'minute_15': 3.10, 'minute_5': 3.13},
                            'memory_usage': {'buffers_kilo': 0,
                                            'cache_kilo': 0,
                                            'free_kilo': 444116,
                                            'total_kilo': 1907024,
                                            'used_kilo': 1462908},
                            'model_name': 'vedge-cloud',
                            'personality': 'vedge',
                            'processes': 250,
                            'services': 'None',
                            'system_fips_state': 'Enabled',
                            'system_logging_disk': 'enabled',
                            'system_logging_host': 'disabled',
                            'system_state': 'GREEN. All daemons up',
                            'system_uptime': '0 days 21 hrs 35 min 28 sec',
                            'testbed_mode': 'Enabled',
                            'version': '99.99.999-4567',
                            'vmanaged': 'true'}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanSystemStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanSystemStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
		unittest.main()   