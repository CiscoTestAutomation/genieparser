import unittest
from unittest.mock import Mock

from pyats.topology import Device
from pyats.topology import loader
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ospf3 import ShowOspf3Interface, \
                                               ShowOspf3Overview, \
                                               ShowOspf3OverviewExtensive

class TestShowOspf3Interface(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ospf3 interface | no-more
        Interface           State   Area            DR ID           BDR ID          Nbrs
        ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        ge-0/0/1.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        lo0.0               DR      0.0.0.8         10.189.5.252    0.0.0.0            0
    '''}

    golden_parsed_output = {
            "ospf3-interface-information": {
                "ospf3-interface": [
                    {
                        "bdr-id": "0.0.0.0",
                        "dr-id": "0.0.0.0",
                        "interface-name": "ge-0/0/0.0",
                        "neighbor-count": "1",
                        "ospf-area": "0.0.0.8",
                        "ospf-interface-state": "PtToPt"
                    },
                    {
                        "bdr-id": "0.0.0.0",
                        "dr-id": "0.0.0.0",
                        "interface-name": "ge-0/0/1.0",
                        "neighbor-count": "1",
                        "ospf-area": "0.0.0.8",
                        "ospf-interface-state": "PtToPt"
                    },
                    {
                        "bdr-id": "0.0.0.0",
                        "dr-id": "10.189.5.252",
                        "interface-name": "lo0.0",
                        "neighbor-count": "0",
                        "ospf-area": "0.0.0.8",
                        "ospf-interface-state": "DR"
                    }
                ]
            }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3Interface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3Interface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspf3Overview(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ospf3 overview
        Instance: master
          Router ID: 111.87.5.252
          Route table index: 0
          AS boundary router
          LSA refresh time: 50 minutes
          Post Convergence Backup: Disabled
          Area: 0.0.0.8
            Stub type: Not Stub
            Area border routers: 0, AS boundary routers: 5
            Neighbors
              Up (in full state): 2
            Topology: default (ID 0)
              Prefix export count: 1
              Full SPF runs: 1934
              SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
              Backup SPF: Not Needed
    '''}

    golden_parsed_output = {
            "ospf3-overview-information": {
                "ospf-overview": {
                    "instance-name": "master",
                    "ospf-area-overview": {
                        "ospf-abr-count": "0",
                        "ospf-area": "0.0.0.8",
                        "ospf-asbr-count": "5",
                        "ospf-nbr-overview": {
                            "ospf-nbr-up-count": "2"
                        },
                        "ospf-stub-type": "Not Stub"
                    },
                    "ospf-lsa-refresh-time": "50",
                    "ospf-route-table-index": "0",
                    "ospf-router-id": "111.87.5.252",
                    "ospf-tilfa-overview": {
                        "ospf-tilfa-enabled": "Disabled"
                    },
                    "ospf-topology-overview": {
                        "ospf-backup-spf-status": "Not Needed",
                        "ospf-full-spf-count": "1934",
                        "ospf-prefix-export-count": "1",
                        "ospf-spf-delay": "0.200000",
                        "ospf-spf-holddown": "2",
                        "ospf-spf-rapid-runs": "3",
                        "ospf-topology-id": "0",
                        "ospf-topology-name": "default"
                    }
            }
        }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3Overview(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3Overview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowOspf3OverviewExtensive(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ospf3 overview extensive
        Instance: master
          Router ID: 111.87.5.252
          Route table index: 0
          AS boundary router
          LSA refresh time: 50 minutes
          Post Convergence Backup: Disabled
          Area: 0.0.0.8
            Stub type: Not Stub
            Area border routers: 0, AS boundary routers: 5
            Neighbors
              Up (in full state): 2
          Topology: default (ID 0)
            Prefix export count: 1
            Full SPF runs: 1934
            SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
            Backup SPF: Not Needed
    '''}

    golden_parsed_output = {
            "ospf3-overview-information": {
            "ospf-overview": {
                "instance-name": "master",
                "ospf-area-overview": {
                    "ospf-abr-count": "0",
                    "ospf-area": "0.0.0.8",
                    "ospf-asbr-count": "5",
                    "ospf-nbr-overview": {
                        "ospf-nbr-up-count": "2"
                    },
                    "ospf-stub-type": "Not Stub"
                },
                "ospf-lsa-refresh-time": "50",
                "ospf-route-table-index": "0",
                "ospf-router-id": "111.87.5.252",
                "ospf-tilfa-overview": {
                    "ospf-tilfa-enabled": "Disabled"
                },
                "ospf-topology-overview": {
                    "ospf-backup-spf-status": "Not Needed",
                    "ospf-full-spf-count": "1934",
                    "ospf-prefix-export-count": "1",
                    "ospf-spf-delay": "0.200000",
                    "ospf-spf-holddown": "2",
                    "ospf-spf-rapid-runs": "3",
                    "ospf-topology-id": "0",
                    "ospf-topology-name": "default"
                }
            }
        }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3OverviewExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3OverviewExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()