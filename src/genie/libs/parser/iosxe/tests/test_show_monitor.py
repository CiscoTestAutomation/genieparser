# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,SchemaMissingKeyError

# iosxe show_monitor
from genie.libs.parser.iosxe.show_monitor import ShowMonitor


# ============================
# Unit test for 'show monitor'
# ============================
class test_show_monitor(unittest.TestCase):
    '''Unit test for "show monitor" '''

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

    golden_output1 ={'execute.return_value':
                         '''
                           Router#show monitor 
                           Load for five secs: 16%/0%; one minute: 4%; five minutes: 4%
                           Time source is NTP, 17:34:06.635 JST Fri Oct 21 2016
                   
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
                  'destination_ip_address': '55.1.1.2',
                  'mtu': 1464,
                  'origin_ip_address': '55.1.1.1',
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

    golden_output2={'execute.return_value':
                        '''
                          Router#show monitor session all
                          Load for five secs: 15%/0%; one minute: 13%; five minutes: 7%
                          Time source is NTP, 19:54:41.566 JST Fri Oct 21 2016
                          
                          Session 1
                          ---------
                          Type                   : ERSPAN Source Session
                          Status                 : Admin Enabled
                          Source Ports           :
                              Both               : Gi0/1/4
                          Destination IP Address : 55.1.1.2
                          MTU                    : 1464
                          Destination ERSPAN ID  : 1
                          Origin IP Address      : 55.1.1.1
                          
                          
                          Session 2
                          ---------
                          Type                   : ERSPAN Destination Session
                          Status                 : Admin Disabled
                          Destination Ports      : Gi0/1/6
                          Source IP Address      : 172.18.197.254
                          Source ERSPAN ID       : 1
                          MTU                    : 1464
            
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
        parsed_output = obj.parse(session='all')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_monitor_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMonitor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()
