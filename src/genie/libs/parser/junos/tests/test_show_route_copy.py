'''
Unit test for:
    * show route summary
'''
class TestShowRouteSummary(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show route summary
        Autonomous system number: 65171
        Router ID: 111.87.5.252

        inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
                    Direct:      6 routes,      6 active
                    Local:      5 routes,      5 active
                        OSPF:    236 routes,    234 active
                        BGP:   1366 routes,    682 active
                    Static:      1 routes,      1 active
                        LDP:      1 routes,      1 active

        inet.3: 11 destinations, 11 routes (11 active, 0 holddown, 0 hidden)
                        BGP:      2 routes,      2 active
                        LDP:      1 routes,      1 active
                    L-OSPF:      8 routes,      8 active

        mpls.0: 44 destinations, 44 routes (44 active, 0 holddown, 0 hidden)
                        MPLS:      6 routes,      6 active
                        LDP:     15 routes,     15 active
                    L-OSPF:     23 routes,     23 active

        inet6.0: 22 destinations, 23 routes (22 active, 0 holddown, 0 hidden)
                    Direct:      4 routes,      4 active
                    Local:      4 routes,      4 active
                    OSPF3:     13 routes,     12 active
                    Static:      1 routes,      1 active
                    INET6:      1 routes,      1 active
    '''}

    golden_parsed_output = {
        "route-summary-information": {
            "as-number": "65171",
            "route-table": [
                {
                    "active-route-count": "929",
                    "destination-count": "929",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "protocols": [
                        {
                            "active-route-count": "6",
                            "protocol-name": "Direct",
                            "protocol-route-count": "6"
                        },
                        {
                            "active-route-count": "5",
                            "protocol-name": "Local",
                            "protocol-route-count": "5"
                        },
                        {
                            "active-route-count": "234",
                            "protocol-name": "OSPF",
                            "protocol-route-count": "236"
                        },
                        {
                            "active-route-count": "682",
                            "protocol-name": "BGP",
                            "protocol-route-count": "1366"
                        },
                        {
                            "active-route-count": "1",
                            "protocol-name": "Static",
                            "protocol-route-count": "1"
                        },
                        {
                            "active-route-count": "1",
                            "protocol-name": "LDP",
                            "protocol-route-count": "1"
                        }
                    ],
                    "table-name": "inet.0",
                    "total-route-count": "1615"
                },
                {
                    "active-route-count": "11",
                    "destination-count": "11",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "protocols": [
                        {
                            "active-route-count": "2",
                            "protocol-name": "BGP",
                            "protocol-route-count": "2"
                        },
                        {
                            "active-route-count": "1",
                            "protocol-name": "LDP",
                            "protocol-route-count": "1"
                        },
                        {
                            "active-route-count": "8",
                            "protocol-name": "L-OSPF",
                            "protocol-route-count": "8"
                        }
                    ],
                    "table-name": "inet.3",
                    "total-route-count": "11"
                },
                {
                    "active-route-count": "44",
                    "destination-count": "44",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "protocols": [
                        {
                            "active-route-count": "6",
                            "protocol-name": "MPLS",
                            "protocol-route-count": "6"
                        },
                        {
                            "active-route-count": "15",
                            "protocol-name": "LDP",
                            "protocol-route-count": "15"
                        },
                        {
                            "active-route-count": "23",
                            "protocol-name": "L-OSPF",
                            "protocol-route-count": "23"
                        }
                    ],
                    "table-name": "mpls.0",
                    "total-route-count": "44"
                },
                {
                    "active-route-count": "22",
                    "destination-count": "22",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "protocols": [
                        {
                            "active-route-count": "4",
                            "protocol-name": "Direct",
                            "protocol-route-count": "4"
                        },
                        {
                            "active-route-count": "4",
                            "protocol-name": "Local",
                            "protocol-route-count": "4"
                        },
                        {
                            "active-route-count": "12",
                            "protocol-name": "OSPF3",
                            "protocol-route-count": "13"
                        },
                        {
                            "active-route-count": "1",
                            "protocol-name": "Static",
                            "protocol-route-count": "1"
                        },
                        {
                            "active-route-count": "1",
                            "protocol-name": "INET6",
                            "protocol-route-count": "1"
                        }
                    ],
                    "table-name": "inet6.0",
                    "total-route-count": "23"
                }
            ],
            "router-id": "111.87.5.252"
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRouteSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowRouteSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
