
#=========================================================
# Unit test for show system queues
#=========================================================
class test_show_system_queues(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "queues-statistics": {
            "interface-queues-statistics": {
                "interface-queue": [
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "lsi",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "dsc",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "lo0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "gre",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "ipip",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "tap",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "pime",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "pimd",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "fxp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "em1",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "mtun",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "demux0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "cbp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "pip0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "125000",
                        "max-packets-allowed": "416",
                        "name": "pp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "irb",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "vtep",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "esi",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "rbeb",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti1",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti2",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti3",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti4",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti5",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti6",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti7",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "jsrv",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "lc-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "pfh-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "pfe-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/0",
                        "number-of-queue-drops": "3",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/1",
                        "number-of-queue-drops": "3",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/2",
                        "number-of-queue-drops": "132",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/3",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/4",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/5",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/6",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/7",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/8",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/9",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    }
                ]
            },
            "protocol-queues-statistics": {
                "protocol-queue": [
                    {
                        "max-octets-allowed": "1000000",
                        "max-packets-allowed": "1000",
                        "name": "splfwdq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1000000",
                        "max-packets-allowed": "1000",
                        "name": "splnetq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1000000",
                        "max-packets-allowed": "1000",
                        "name": "optionq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "50000",
                        "max-packets-allowed": "50",
                        "name": "icmpq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "frlmiq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "25000",
                        "max-packets-allowed": "1000",
                        "name": "spppintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "atmctlpktq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "atmoamq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "tnpintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "200000",
                        "max-packets-allowed": "200",
                        "name": "tagintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "200000",
                        "max-packets-allowed": "200",
                        "name": "tagfragq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    }
                ]
            }
        }
    }


    golden_output_1 = {'execute.return_value': '''
                show system queues
        output interface            bytes          max  packets      max    drops
        lsi                             0        12500        0       41        0
        dsc                             0            0        0        0        0
        lo0                             0            0        0        0        0
        gre                             0        12500        0       41        0
        ipip                            0        12500        0       41        0
        tap                             0            0        0        0        0
        pime                            0        12500        0       41        0
        pimd                            0        12500        0       41        0
        fxp0                            0     12500000        0    41666        0
        em1                             0     12500000        0    41666        0
        mtun                            0        12500        0       41        0
        demux0                          0            0        0        0        0
        cbp0                            0     12500000        0    41666        0
        pip0                            0     12500000        0    41666        0
        pp0                             0       125000        0      416        0
        irb                             0     12500000        0    41666        0
        vtep                            0     12500000        0    41666        0
        esi                             0     12500000        0    41666        0
        rbeb                            0     12500000        0    41666        0
        fti0                            0            0        0        0        0
        fti1                            0            0        0        0        0
        fti2                            0            0        0        0        0
        fti3                            0            0        0        0        0
        fti4                            0            0        0        0        0
        fti5                            0            0        0        0        0
        fti6                            0            0        0        0        0
        fti7                            0            0        0        0        0
        jsrv                            0     12500000        0    41666        0
        lc-0/0/0                        0            0        0        0        0
        pfh-0/0/0                       0            0        0        0        0
        pfe-0/0/0                       0            0        0        0        0
        ge-0/0/0                        0      1250000        0     4166        3
        ge-0/0/1                        0      1250000        0     4166        3
        ge-0/0/2                        0      1250000        0     4166      132
        ge-0/0/3                        0      1250000        0     4166        0
        ge-0/0/4                        0      1250000        0     4166        0
        ge-0/0/5                        0      1250000        0     4166        0
        ge-0/0/6                        0      1250000        0     4166        0
        ge-0/0/7                        0      1250000        0     4166        0
        ge-0/0/8                        0      1250000        0     4166        0
        ge-0/0/9                        0      1250000        0     4166        0
        input protocol              bytes          max  packets      max    drops
        splfwdq                         0      1000000        0     1000        0
        splnetq                         0      1000000        0     1000        0
        optionq                         0      1000000        0     1000        0
        icmpq                           0        50000        0       50        0
        frlmiq                          0            0        0        0        0
        spppintrq                       0        25000        0     1000        0
        atmctlpktq                      0            0        0        0        0
        atmoamq                         0            0        0        0        0
        tnpintrq                        0      1250000        0     4166        0
        tagintrq                        0       200000        0      200        0
        tagfragq                        0       200000        0      200        0
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemQueues(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemQueues(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


#=========================================================
# Unit test for show system queues no-forwarding
#=========================================================
class test_show_system_queues_no_forwarding(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "queues-statistics": {
            "interface-queues-statistics": {
                "interface-queue": [
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "lsi",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "dsc",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "lo0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "gre",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "ipip",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "tap",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "pime",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "pimd",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "fxp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "em1",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "mtun",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "demux0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "cbp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "pip0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "125000",
                        "max-packets-allowed": "416",
                        "name": "pp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "irb",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "vtep",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "esi",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "rbeb",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti1",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti2",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti3",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti4",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti5",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti6",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti7",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "jsrv",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "lc-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "pfh-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "pfe-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/0",
                        "number-of-queue-drops": "3",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/1",
                        "number-of-queue-drops": "3",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/2",
                        "number-of-queue-drops": "132",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/3",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/4",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/5",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/6",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/7",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/8",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/9",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    }
                ]
            },
            "protocol-queues-statistics": {
                "protocol-queue": [
                    {
                        "max-octets-allowed": "1000000",
                        "max-packets-allowed": "1000",
                        "name": "splfwdq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1000000",
                        "max-packets-allowed": "1000",
                        "name": "splnetq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1000000",
                        "max-packets-allowed": "1000",
                        "name": "optionq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "50000",
                        "max-packets-allowed": "50",
                        "name": "icmpq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "frlmiq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "25000",
                        "max-packets-allowed": "1000",
                        "name": "spppintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "atmctlpktq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "atmoamq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "tnpintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "200000",
                        "max-packets-allowed": "200",
                        "name": "tagintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    },
                    {
                        "max-octets-allowed": "200000",
                        "max-packets-allowed": "200",
                        "name": "tagfragq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0"
                    }
                ]
            }
        }
    }


    golden_output_1 = {'execute.return_value': '''
                show system queues
        output interface            bytes          max  packets      max    drops
        lsi                             0        12500        0       41        0
        dsc                             0            0        0        0        0
        lo0                             0            0        0        0        0
        gre                             0        12500        0       41        0
        ipip                            0        12500        0       41        0
        tap                             0            0        0        0        0
        pime                            0        12500        0       41        0
        pimd                            0        12500        0       41        0
        fxp0                            0     12500000        0    41666        0
        em1                             0     12500000        0    41666        0
        mtun                            0        12500        0       41        0
        demux0                          0            0        0        0        0
        cbp0                            0     12500000        0    41666        0
        pip0                            0     12500000        0    41666        0
        pp0                             0       125000        0      416        0
        irb                             0     12500000        0    41666        0
        vtep                            0     12500000        0    41666        0
        esi                             0     12500000        0    41666        0
        rbeb                            0     12500000        0    41666        0
        fti0                            0            0        0        0        0
        fti1                            0            0        0        0        0
        fti2                            0            0        0        0        0
        fti3                            0            0        0        0        0
        fti4                            0            0        0        0        0
        fti5                            0            0        0        0        0
        fti6                            0            0        0        0        0
        fti7                            0            0        0        0        0
        jsrv                            0     12500000        0    41666        0
        lc-0/0/0                        0            0        0        0        0
        pfh-0/0/0                       0            0        0        0        0
        pfe-0/0/0                       0            0        0        0        0
        ge-0/0/0                        0      1250000        0     4166        3
        ge-0/0/1                        0      1250000        0     4166        3
        ge-0/0/2                        0      1250000        0     4166      132
        ge-0/0/3                        0      1250000        0     4166        0
        ge-0/0/4                        0      1250000        0     4166        0
        ge-0/0/5                        0      1250000        0     4166        0
        ge-0/0/6                        0      1250000        0     4166        0
        ge-0/0/7                        0      1250000        0     4166        0
        ge-0/0/8                        0      1250000        0     4166        0
        ge-0/0/9                        0      1250000        0     4166        0
        input protocol              bytes          max  packets      max    drops
        splfwdq                         0      1000000        0     1000        0
        splnetq                         0      1000000        0     1000        0
        optionq                         0      1000000        0     1000        0
        icmpq                           0        50000        0       50        0
        frlmiq                          0            0        0        0        0
        spppintrq                       0        25000        0     1000        0
        atmctlpktq                      0            0        0        0        0
        atmoamq                         0            0        0        0        0
        tnpintrq                        0      1250000        0     4166        0
        tagintrq                        0       200000        0      200        0
        tagfragq                        0       200000        0      200        0
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemQueuesNoForwarding(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemQueuesNoForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)