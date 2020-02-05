
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.nxos.show_logging import ShowLoggingLogfile


# ==============================================
# Unittest for:
#   * 'show logging logfile'
#   * 'show logging logfile | include {include}'
# ==============================================
class test_show_logging(unittest.TestCase):

    '''Unittest for:
        * 'show logging logfile'
        * 'show logging logfile | include {include}'
    '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        'logs': [
            '2019 May 22 16:20:45 ha01-n7010-01 %ACLLOG-5-ACLLOG_FLOW_INTERVAL: Src IP: 172.30.10.100, Dst IP: 10.135.15.2, Src Port: 0, Dst Port: 0, Src Intf: Ethernet3/3, Protocol: "IP"(253), ACL Name: match-ef-acl, ACE Action: Permit, Appl Intf: Vlan10, Hit-count: 600',
            '2019 May 22 16:20:50 ha01-n7010-01 %ACLLOG-5-ACLLOG_FLOW_INTERVAL: Src IP: 172.30.10.100, Dst IP: 10.135.15.2, Src Port: 0, Dst Port: 0, Src Intf: Ethernet3/3, Protocol: "IP"(253), ACL Name: match-ef-acl, ACE Action: Permit, Appl Intf: Vlan10, Hit-count: 500',
            ],
        }

    golden_output_1 = {'execute.return_value': '''
        show logging logfile | include ACL
        2019 May 22 16:20:45 ha01-n7010-01 %ACLLOG-5-ACLLOG_FLOW_INTERVAL: Src IP: 172.30.10.100, Dst IP: 10.135.15.2, Src Port: 0, Dst Port: 0, Src Intf: Ethernet3/3, Protocol: "IP"(253), ACL Name: match-ef-acl, ACE Action: Permit, Appl Intf: Vlan10, Hit-count: 600
        2019 May 22 16:20:50 ha01-n7010-01 %ACLLOG-5-ACLLOG_FLOW_INTERVAL: Src IP: 172.30.10.100, Dst IP: 10.135.15.2, Src Port: 0, Dst Port: 0, Src Intf: Ethernet3/3, Protocol: "IP"(253), ACL Name: match-ef-acl, ACE Action: Permit, Appl Intf: Vlan10, Hit-count: 500
        '''}

    def test_show_logging_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLoggingLogfile(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_logging_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowLoggingLogfile(device=self.device)
        parsed_output = obj.parse(include='acl')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()
