import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxe.show_cdp import ShowCdpNeighbors


class test_show_cdp_neighbors(unittest.TestCase):

    device = Device(name='aDevice')

    expected_parsed_output = {
        'cdp': {
            'device_id': {
                'c2950-1': {'capability': 's i',
                            'hold_time': 148,
                            'local_interface': 'fas 0/0',
                            'platform': 'ws-c2950t-fas',
                            'port_id': '0/15'},
                'device2': {'capability': 'r',
                            'hold_time': 152,
                            'local_interface': 'eth 0',
                            'platform': 'as5200',
                            'port_id': 'eth 0'},
                'device3': {'capability': 'r',
                            'hold_time': 144,
                            'local_interface': 'eth 0',
                            'platform': '3640',
                            'port_id': 'eth0/0'},
                'device4': {'capability': '',
                            'hold_time': 141,
                            'local_interface': 'eth 0',
                            'platform': 'rp1',
                            'port_id': 'eth 0/0'},
                'device5': {'capability': '',
                            'hold_time': 164,
                            'local_interface': 'eth 0',
                            'platform': '7206',
                            'port_id': 'eth 1/0'},
               'device6':  {'capability': 'r s i',
                            'hold_time': 157,
                            'local_interface': 'gig 0',
                            'platform': 'c887va-w-',
                            'port_id': 'wgi 0'},
               'r5.cisco.com': {'capability': 'r b',
                                'hold_time': 125,
                                'local_interface': 'gig 0/0',
                                'platform': 'gig',
                                'port_id': '0/0'},
                'r6(9p57k4ej8ca)': {'capability': 'r s c',
                                    'hold_time': 137,
                                    'local_interface': 'gig 0/0',
                                    'platform': 'n9k-9000v',
                                    'port_id': 'mgmt0'},
               'r7(9qbdkb58f76)': {'capability': 'r s c',
                                   'hold_time': 130,
                                   'local_interface': 'gig 0/0',
                                   'platform': 'n9k-9000v',
                                   'port_id': 'mgmt0'},
               'r8.cisco.com': {'capability': 'r b',
                                'hold_time': 148,
                                'local_interface': 'gig 0/0',
                                'platform': 'gig',
                                'port_id': '0/0'},
               'r9.cisco.com': {'capability': 'r b',
                                'hold_time': 156,
                                'local_interface': 'gig 0/0',
                                'platform': 'gig',
                                'port_id': '0/0'},
               'rx-swv.cisco.com': {'capability': 't s',
                                    'hold_time': 167,
                                    'local_interface': 'fas 0/1',
                                    'platform': 'ws-c3524-xfas',
                                    'port_id': '0/13'}}}}

    empty_device_output = {'execute.return_value': '''
        [genie36] ssr-oper-gen.cisco.com:14:01> python $VIRTUAL_ENV/tools/run_''
        parsers.py --cmd 'show cdp neighbors' --os 'iosxe' --output-only
        ==========   iosxe : show cdp neighbors : show cdp neighbors ==========
        Device# show cdp neighbors


        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  Platform  ''
        Port ID

        ==========   iosxe : show cdp neighbors : show cdp neighbors ==========
        Device# show cdp neighbors

        ==========   iosxe : show cdp neighbors : show cdp neighbors ==========
        Router# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP

        Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID

        Capability Codes:R - Router, T - Trans Bridge, B - Source Route ''
        Bridge S - Switch,
        H - Host, I - IGMP, r - Repeater

        Capability Codes:R - Router, T - Trans Bridge, B - Source Route ''
        Bridge S - Switch,
        H - Host, I - IGMP, r - Repeater
        Device ID  Local Intrfce  Holdtme  Capability  Platform  Port ID

      '''}

    trimed_device_ouput = {'execute.return_value': '''
        C2950-1 Fas 0/0           148         S I       WS-C2950T-Fas 0/15
        RX-SWV.cisco.com Fas 0/1            167         T S       WS-C3524-XFas 0/13
        device2      Eth 0          152      R           AS5200    Eth 0
        device3      Eth 0          144      R           3640      Eth0/0
        device4      Eth 0          141                  RP1       Eth 0/0
        device5      Eth 0          164                  7206      Eth 1/0
        device6    Gig 0          157      R S I       C887VA-W- WGi 0
        R6(9P57K4EJ8CA)  Gig 0/0           137             R S C  N9K-9000v mgmt0
        R7(9QBDKB58F76)  Gig 0/0           130             R S C  N9K-9000v mgmt0
        R5.cisco.com     Gig 0/0           125              R B             Gig 0/0
        R8.cisco.com     Gig 0/0           148              R B             Gig 0/0
        R9.cisco.com     Gig 0/0           156              R B             Gig 0/0
        '''}

    full_device_output = {'execute.return_value': '''
        [genie36] ssr-oper-gen.cisco.com:14:01> python $VIRTUAL_ENV/tools/run''
        _parsers.py --cmd 'show cdp neighbors' --os 'iosxe' --output-only
        ==========   iosxe : show cdp neighbors : show cdp neighbors ==========
        Device# show cdp neighbors


        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP, r - Repeater

        Device ID        Local Interfce     Holdtme    Capability  ''
        Platform  Port ID
        C2950-1          Fas 0/0            148         S I       WS-C2950T-Fas 0/15
        RX-SWV.cisco.com Fas 0/1            167         T S       WS-C3524-XFas 0/13
        ==========   iosxe : show cdp neighbors : show cdp neighbors ==========
        Device# show cdp neighbors

        ==========   iosxe : show cdp neighbors : show cdp neighbors ==========
        Router# show cdp neighbors

        Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                        S - Switch, H - Host, I - IGMP

        Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID

        Capability Codes:R - Router, T - Trans Bridge, B - Source Route ''
        Bridge S - Switch,
        H - Host, I - IGMP , r - Repeater
        device2      Eth 0          152      R           AS5200    Eth 0
        device3      Eth 0          144      R           3640      Eth0/0
        device4      Eth 0          141                  RP1      Eth 0/0
        device5      Eth 0            164                  7206      Eth 1/0
        R6(9P57K4EJ8CA)  Gig 0/0           137             R S C  N9K-9000v mgmt0
        R7(9QBDKB58F76)  Gig 0/0           130             R S C  N9K-9000v mgmt0
        R5.cisco.com     Gig 0/0           125              R B             Gig 0/0
        R8.cisco.com     Gig 0/0           148              R B             Gig 0/0
        R9.cisco.com     Gig 0/0           156              R B             Gig 0/0

        Capability Codes:R - Router, T - Trans Bridge, B - Source Route Bridge ''
        S - Switch,
        H - Host, I - IGMP, r - Repeater
        Device ID  Local Intrfce  Holdtme  Capability  Platform  Port ID
        device6    Gig 0          157      R S I       C887VA-W- WGi 0
      '''}

    def test_show_cdp_neighbors(self):
        self.maxDiff = None
        self.device = Mock(**self.trimed_device_ouput)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output)

    def test_show_cdp_neighbors_full_output(self):
        self.maxDiff = None
        self.device = Mock(**self.full_device_output)
        obj = ShowCdpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output)

    def test_show_cdp_neighbors_empty_output(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_device_output)
        obj = ShowCdpNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()
