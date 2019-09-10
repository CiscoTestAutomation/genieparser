# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,SchemaMissingKeyError

# iosxe show_monitor
from genie.libs.parser.iosxe.show_monitor import ShowMonitor,ShowMonitorCapture


# ============================
# Unit test for 'show monitor'
# ============================
class test_show_monitor(unittest.TestCase):
    '''Unit test for "show monitor"
                     "show monitor session all"
                     "show monitor session {session}"
    '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'session':
            {'1':
                 {'destination_erspan_id': '1',
                  'destination_ip_address': '172.18.197.254',
                  'mtu': 1464,
                  'origin_ip_address': '172.18.197.254',
                  'source_ports':
                      {'tx_only': 'Gi0/1/4'},
                  'status': 'Admin Enabled',
                  'type': 'ERSPAN Source Session'},
            '2':
                 {'destination_ports': 'Gi0/1/6',
                  'mtu': 1464,
                  'source_erspan_id': '1',
                  'source_ip_address': '172.18.197.254',
                  'status': 'Admin Enabled',
                  'type': 'ERSPAN Destination Session'}}}

    golden_output1 ={'execute.return_value':'''
        Router#show monitor 
        Load for five secs: 16%/0%; one minute: 4%; five minutes: 4%
        Time source is NTP, 17:34:06.635 EST Fri Oct 21 2016

        Session 1
        ---------
        Type                   : ERSPAN Source Session
        Status                 : Admin Enabled
        Source Ports           : 
            TX Only            : Gi0/1/4
        Destination IP Address : 172.18.197.254
        MTU                    : 1464
        Destination ERSPAN ID  : 1
        Origin IP Address      : 172.18.197.254


        Session 2
        ---------
        Type                   : ERSPAN Destination Session
        Status                 : Admin Enabled
        Destination Ports      : Gi0/1/6
        Source IP Address      : 172.18.197.254
        Source ERSPAN ID       : 1
        MTU                    : 1464
            
        Router#
        '''}

    golden_parsed_output2 = {
        'session':
            {'1':
                 {'destination_erspan_id': '1',
                  'destination_ip_address': '10.76.1.2',
                  'mtu': 1464,
                  'origin_ip_address': '10.76.1.1',
                  'source_ports':
                      {'both': 'Gi0/1/4'},
                  'status': 'Admin Enabled',
                  'type': 'ERSPAN Source Session'},
            '2':
                 {'destination_ports': 'Gi0/1/6',
                  'mtu': 1464,
                  'source_erspan_id': '1',
                  'source_ip_address': '172.18.197.254',
                  'status': 'Admin Disabled',
                  'type': 'ERSPAN Destination Session'}}}

    golden_output2={'execute.return_value': '''
        Router#show monitor session all
        Load for five secs: 15%/0%; one minute: 13%; five minutes: 7%
        Time source is NTP, 19:54:41.566 EST Fri Oct 21 2016
        
        Session 1
        ---------
        Type                   : ERSPAN Source Session
        Status                 : Admin Enabled
        Source Ports           :
            Both               : Gi0/1/4
        Destination IP Address : 10.76.1.2
        MTU                    : 1464
        Destination ERSPAN ID  : 1
        Origin IP Address      : 10.76.1.1
        
        
        Session 2
        ---------
        Type                   : ERSPAN Destination Session
        Status                 : Admin Disabled
        Destination Ports      : Gi0/1/6
        Source IP Address      : 172.18.197.254
        Source ERSPAN ID       : 1
        MTU                    : 1464
            
        '''}

    golden_parsed_output3 = {
        'session':
            {'2':
                {'destination_ports': 'Gi0/0/1',
                 'mtu': 1464,
                 'source_ports':
                     {'both': 'Gi0/0/1'},
                 'source_rspan_vlan': 100,
                 'status': 'Admin Enabled',
                 'type': 'Remote Destination Session'}}}

    golden_output3 = {'execute.return_value': '''
        Router  # show monitor session 2
        Session 2
        ---------
        Type                   : Remote Source Session
        Status                 : Admin Enabled
        Source Ports           :
            Both               : Gi0/0/1
        MTU                    : 1464
        Session 2
        ---------
        Type                   : Remote Destination Session
        Status                 : Admin Enabled
        Destination Ports      : Gi0/0/1
        MTU                    : 1464
        Source RSPAN VLAN : 100
       
        '''}

    golden_parsed_output4 = {
        'session': 
            {'1': 
                {'destination_erspan_id': '10',
                'destination_ip_address': '10.12.12.2',
                'filter_access_group': 100,
                'origin_ip_address': '10.12.12.1',
                'source_subinterfaces': 
                    {'both': 'Gi2/2/0.100'},
                'status': 'Admin Enabled',
                'type': 'ERSPAN Source Session'}}}

    golden_output4 = {'execute.return_value': '''
        Router#show monitor session 1

        Session 1
        ---------
        Type: ERSPAN Source Session
        Status: Admin Enabled
        Source Subinterfaces:
            Both: Gi2/2/0.100
        Filter Access-Group: 100
        Destination IP Address : 10.12.12.2
        Destination ERSPAN ID  : 10
        Origin IP Address: 10.12.12.1
        '''}

    def test_show_monitor_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMonitor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_monitor_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMonitor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_monitor_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowMonitor(device=self.device)
        parsed_output = obj.parse(session='2')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_monitor_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowMonitor(device=self.device)
        parsed_output = obj.parse(session='1')
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_monitor_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMonitor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ============================================
# Unit test for 'show monitor capture '
# ============================================
class test_show_monitor_capture(unittest.TestCase):

    '''Unit test for "show monitor capture" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 ={
        'status_information':
            {'CAPTURE':
                {'target_type':
                    {'interface': 'Control Plane',
                     'direction': 'both',
                     'status': 'Inactive'},
                'filter_details':
                    {'filter_details_type': 'Capture all packets'},
                'buffer_details':
                     {'buffer_type': 'LINEAR (default)',
                      'buffer_size': 10
                     },
                'limit_details':
                     {'packets_number': 0,
                      'packets_capture_duaration': 0,
                      'packets_size': 0,
                      'maximum_packets_number': 1000,
                      'packet_sampling_rate': 0}}}}

    golden_output1 = {'execute.return_value':'''
        Router#show monitor capture 
        Load for five secs: 2%/0%; one minute: 7%; five minutes: 8%
        Time source is NTP, 18:31:17.685 EST Thu Sep 8     
        Status Information for Capture CAPTURE
          Target Type: 
           Interface: Control Plane, Direction : both
           Status : Inactive
          Filter Details:
            Capture all packets
          Buffer Details: 
           Buffer Type: LINEAR (default)
           Buffer Size (in MB): 10
          Limit Details: 
           Number of Packets to capture: 0 (no limit)
           Packet Capture duration: 0 (no limit)
           Packet Size to capture: 0 (no limit)
           Maximum number of packets to capture per second: 1000
           Packet sampling rate: 0 (no sampling)
        Router#
        
        '''}

    golden_parsed_output2 ={
        'status_information':
            {'NTP':
                {'target_type':
                    {'interface': 'GigabitEthernet0/0/0',
                     'direction': 'both',
                     'status': 'Active'
                    },
                'filter_details':
                    {'filter_details_type': 'Capture all packets'},
                'buffer_details':
                    {'buffer_type': 'LINEAR (default)',
                     'buffer_size': 10
                    },
                'limit_details':
                    {'packets_number': 0,
                     'packets_capture_duaration': 0,
                     'packets_size': 0,
                     'maximum_packets_number': 1000,
                     'packet_sampling_rate': 0}}}}

    golden_output2 = {'execute.return_value':'''
        Router#show monitor capture
        Load for five secs: 1%/0%; one minute: 17%; five minutes: 8%
        Time source is NTP, 16:22:09.994 EST Fri Oct 14 2016
        
        
        Status Information for Capture NTP
          Target Type: 
           Interface: GigabitEthernet0/0/0, Direction: both
           Status : Active
          Filter Details: 
            Capture all packets
          Buffer Details: 
           Buffer Type: LINEAR (default)
           Buffer Size (in MB): 10
          Limit Details: 
           Number of Packets to capture: 0 (no limit)
           Packet Capture duration: 0 (no limit)
           Packet Size to capture: 0 (no limit)
           Maximum number of packets to capture per second: 1000
           Packet sampling rate: 0 (no sampling)
        Router#
         '''}

    golden_parsed_output3={
        'status_information':
            {'mycap':
                {'target_type':
                    {'interface': 'GigabitEthernet1/0/3',
                     'direction': 'both',
                     'status': 'Inactive'
                },
                'filter_details':
                    {'filter_details_type': 'IPv4',
                     'source_ip': 'any',
                     'destination_ip': 'any',
                     'protocol': 'any'},
                'buffer_details':
                    {'buffer_type': 'LINEAR (default)'
                    },
                'file_details':
                    {'file_name': 'flash:mycap.pcap',
                     'file_size': 5,
                     'file_number': 2,
                     'size_of_buffer': 10
                    },
                'limit_details':
                    {'packets_number': 0,
                     'packets_capture_duaration': 0,
                     'packets_size': 0,
                     'packets_per_second': 0,
                     'packet_sampling_rate': 0}}}}

    golden_output3={'execute.return_value':'''
        SWITCH#show monitor capture mycap
        Status Information for Capture mycap
          Target Type: 
           Interface: GigabitEthernet1/0/3, Direction: both
           Status : Inactive
          Filter Details: 
           IPv4 
            Source IP:  any
            Destination IP:  any
           Protocol: any
          Buffer Details: 
           Buffer Type: LINEAR (default)
          File Details: 
           Associated file name: flash:mycap.pcap
           Total size of files(in MB): 5
           Number of files in ring: 2
           Size of buffer(in MB): 10
          Limit Details: 
           Number of Packets to capture: 0 (no limit)
           Packet Capture duration: 0 (no limit)
           Packet Size to capture: 0 (no limit)
           Packets per second: 0 (no limit)
           Packet sampling rate: 0 (no sampling)
        '''}
    

    def test_show_monitor_capture_empty(self):
        self.maxDiff= None
        self.device = Mock(**self.empty_output)
        obj = ShowMonitorCapture(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_monitor_capture_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMonitorCapture(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_monitor_capture_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMonitorCapture(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_monitor_capture_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowMonitorCapture(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)


if __name__ == '__main__':
    unittest.main()