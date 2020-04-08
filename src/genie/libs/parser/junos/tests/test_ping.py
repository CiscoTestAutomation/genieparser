# Python
import unittest
from unittest.mock import Mock

# PyATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos ping
from genie.libs.parser.junos.ping import (Ping)


class TestPing(unittest.TestCase):
    """ Unit tests for:
            * ping {addr} count {count}
    """

    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        ping 10.189.5.94 count 5
        PING 10.189.5.94 (10.189.5.94): 56 data bytes
        64 bytes from 10.189.5.94: icmp_seq=0 ttl=62 time=2.261 ms
        64 bytes from 10.189.5.94: icmp_seq=1 ttl=62 time=1.823 ms
        64 bytes from 10.189.5.94: icmp_seq=2 ttl=62 time=2.399 ms
        64 bytes from 10.189.5.94: icmp_seq=3 ttl=62 time=2.218 ms
        64 bytes from 10.189.5.94: icmp_seq=4 ttl=62 time=2.173 ms

        --- 10.189.5.94 ping statistics ---
        5 packets transmitted, 5 packets received, 0% packet loss
        round-trip min/avg/max/stddev = 1.823/2.175/2.399/0.191 ms
    '''}
    
    golden_parsed_output = {
        "ping": {
            "address": "10.189.5.94",
            "data-bytes": 56,
            "result": [
                {
                    "bytes": 64,
                    "from": "10.189.5.94",
                    "icmp-seq": 0,
                    "time": "2.261",
                    "ttl": 62
                },
                {
                    "bytes": 64,
                    "from": "10.189.5.94",
                    "icmp-seq": 1,
                    "time": "1.823",
                    "ttl": 62
                },
                {
                    "bytes": 64,
                    "from": "10.189.5.94",
                    "icmp-seq": 2,
                    "time": "2.399",
                    "ttl": 62
                },
                {
                    "bytes": 64,
                    "from": "10.189.5.94",
                    "icmp-seq": 3,
                    "time": "2.218",
                    "ttl": 62
                },
                {
                    "bytes": 64,
                    "from": "10.189.5.94",
                    "icmp-seq": 4,
                    "time": "2.173",
                    "ttl": 62
                }
            ],
            "source": "10.189.5.94",
            "statistics": {
                "loss-rate": 0,
                "received": 5,
                "round-trip": {
                    "avg": "2.175",
                    "max": "2.399",
                    "min": "1.823",
                    "stddev": "0.191"
                },
                "send": 5
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
        ping 2001:db8:223c:2c16::2 count 10
        PING6(56=40+8+8 bytes) 2001:db8:223c:2c16::1 --> 2001:db8:223c:2c16::2
        16 bytes from 2001:db8:223c:2c16::2, icmp_seq=0 hlim=64 time=973.514 ms
        16 bytes from 2001:db8:223c:2c16::2, icmp_seq=1 hlim=64 time=0.993 ms
        16 bytes from 2001:db8:223c:2c16::2, icmp_seq=2 hlim=64 time=1.170 ms
        16 bytes from 2001:db8:223c:2c16::2, icmp_seq=3 hlim=64 time=0.677 ms
        16 bytes from 2001:db8:223c:2c16::2, icmp_seq=4 hlim=64 time=0.914 ms
        16 bytes from 2001:db8:223c:2c16::2, icmp_seq=5 hlim=64 time=0.814 ms
        16 bytes from 2001:db8:223c:2c16::2, icmp_seq=6 hlim=64 time=0.953 ms
        16 bytes from 2001:db8:223c:2c16::2, icmp_seq=7 hlim=64 time=1.140 ms
        16 bytes from 2001:db8:223c:2c16::2, icmp_seq=8 hlim=64 time=0.800 ms
        16 bytes from 2001:db8:223c:2c16::2, icmp_seq=9 hlim=64 time=0.881 ms

        --- 2001:db8:223c:2c16::2 ping6 statistics ---
        10 packets transmitted, 10 packets received, 0% packet loss
        round-trip min/avg/max/std-dev = 0.677/98.186/973.514/291.776 ms
    '''}

    golden_parsed_output_2 = {
        "ping": {
            "address": "2001:db8:223c:2c16::2",
            "data-bytes": 56,
            "result": [
                {
                    "bytes": 16,
                    "from": "2001:db8:223c:2c16::2",
                    "hlim": 64,
                    "icmp-seq": 0,
                    "time": "973.514"
                },
                {
                    "bytes": 16,
                    "from": "2001:db8:223c:2c16::2",
                    "hlim": 64,
                    "icmp-seq": 1,
                    "time": "0.993"
                },
                {
                    "bytes": 16,
                    "from": "2001:db8:223c:2c16::2",
                    "hlim": 64,
                    "icmp-seq": 2,
                    "time": "1.170"
                },
                {
                    "bytes": 16,
                    "from": "2001:db8:223c:2c16::2",
                    "hlim": 64,
                    "icmp-seq": 3,
                    "time": "0.677"
                },
                {
                    "bytes": 16,
                    "from": "2001:db8:223c:2c16::2",
                    "hlim": 64,
                    "icmp-seq": 4,
                    "time": "0.914"
                },
                {
                    "bytes": 16,
                    "from": "2001:db8:223c:2c16::2",
                    "hlim": 64,
                    "icmp-seq": 5,
                    "time": "0.814"
                },
                {
                    "bytes": 16,
                    "from": "2001:db8:223c:2c16::2",
                    "hlim": 64,
                    "icmp-seq": 6,
                    "time": "0.953"
                },
                {
                    "bytes": 16,
                    "from": "2001:db8:223c:2c16::2",
                    "hlim": 64,
                    "icmp-seq": 7,
                    "time": "1.140"
                },
                {
                    "bytes": 16,
                    "from": "2001:db8:223c:2c16::2",
                    "hlim": 64,
                    "icmp-seq": 8,
                    "time": "0.800"
                },
                {
                    "bytes": 16,
                    "from": "2001:db8:223c:2c16::2",
                    "hlim": 64,
                    "icmp-seq": 9,
                    "time": "0.881"
                }
            ],
            "source": "2001:db8:223c:2c16::1",
            "statistics": {
                "loss-rate": 0,
                "received": 10,
                "round-trip": {
                    "avg": "98.186",
                    "max": "973.514",
                    "min": "0.677",
                    "stddev": "291.776"
                },
                "send": 10
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = Ping(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse(addr='10.189.5.94', count='5')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Ping(device=self.device)
        parsed_output = obj.parse(addr='10.189.5.94', count='5')
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = Ping(device=self.device)
        parsed_output = obj.parse(addr='2001:db8:223c:2c16::2', count='10')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

if __name__ == '__main__':
    unittest.main()