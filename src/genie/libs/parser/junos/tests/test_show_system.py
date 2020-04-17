# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.junos.show_system import (ShowSystemBuffer,
                                                ShowSystemUsers)

#=========================================================
# Unit test for show system buffer
#=========================================================
class test_show_system_buffer(unittest.TestCase):

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        'memory-statistics': {
            'cached-bytes': '1971',
            'cached-jumbo-clusters-16k': '0',
            'cached-jumbo-clusters-4k': '2',
            'cached-jumbo-clusters-9k': '0',
            'cached-mbuf-clusters': '714',
            'cached-mbufs': '2142',
            'cluster-failures': '0',
            'current-bytes-in-use': '1179',
            'current-jumbo-clusters-16k': '0',
            'current-jumbo-clusters-4k': '0',
            'current-jumbo-clusters-9k': '0',
            'current-mbuf-clusters': '516',
            'current-mbufs': '588',
            'io-initiated': '0',
            'jumbo-cluster-failures-16k': '0',
            'jumbo-cluster-failures-4k': '0',
            'jumbo-cluster-failures-9k': '0',
            'max-jumbo-clusters-16k': '10396',
            'max-jumbo-clusters-4k': '62377',
            'max-jumbo-clusters-9k': '18482',
            'max-mbuf-clusters': '124756',
            'mbuf-failures': '0',
            'packet-count': '513',
            'packet-failures': '0',
            'packet-free': '499',
            'sfbuf-requests-delayed': '0',
            'sfbuf-requests-denied': '0',
            'total-bytes': '3150',
            'total-jumbo-clusters-16k': '0',
            'total-jumbo-clusters-4k': '2',
            'total-jumbo-clusters-9k': '0',
            'total-mbuf-clusters': '1230',
            'total-mbufs': '2730'
        }
    }


    golden_output_1 = {'execute.return_value': '''
                show system buffers
                588/2142/2730 mbufs in use (current/cache/total)
                516/714/1230/124756 mbuf clusters in use (current/cache/total/max)
                513/499 mbuf+clusters out of packet secondary zone in use (current/cache)
                0/2/2/62377 4k (page size) jumbo clusters in use (current/cache/total/max)
                0/0/0/18482 9k (page size) jumbo clusters in use (current/cache/total/max)
                0/0/0/10396 16k (page size) jumbo clusters in use (current/cache/total/max)
                1179K/1971K/3150K bytes allocated to network (current/cache/total)
                0/0/0 requests for mbufs denied (mbufs/clusters/mbuf+clusters)
                0/0/0 requests for jumbo clusters denied (4k/9k/16k)
                0 requests for sfbufs denied
                0 requests for sfbufs delayed
                0 requests for I/O initiated by sendfile

    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemBuffer(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemBuffer(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


#=========================================================
# Unit test for show system Users
#=========================================================
class TestShowSystemUsers(unittest.TestCase):

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {'execute.return_value': '''
        show system users 
        9:38AM  up 209 days, 37 mins, 3 users, load averages: 0.28, 0.39, 0.37
        USER     TTY      FROM                              LOGIN@  IDLE WHAT
        kddi     pts/0    10.1.0.1                          2:35AM      - -cl           
        kddi     pts/1    10.1.0.1                          8:31AM     56 -cl           
        kddi     pts/2    10.1.0.1                          7:45AM      3 -cl
        '''}


    golden_output_1 = {
        "system-users-information": {
        "uptime-information": {
            "active-user-count": {
                "#text": "3"
            },
            "date-time": {
                "#text": "9:38AM"
            },
            "load-average-1": "0.28",
            "load-average-15": "0.39",
            "load-average-5": "0.37",
            "up-time": {
                "#text": "209 days, 37 mins"
            },
            "user-table": {
                "user-entry": [
                    {
                        "command": "-cl",
                        "from": "10.1.0.1",
                        "idle-time": {
                            "#text": "-"
                        },
                        "login-time": {
                            "#text": "2:35AM"
                        },
                        "tty": "pts/0",
                        "user": "kddi"
                    },
                    {
                        "command": "-cl",
                        "from": "10.1.0.1",
                        "idle-time": {
                            "#text": "56"
                        },
                        "login-time": {
                            "#text": "8:31AM"
                        },
                        "tty": "pts/1",
                        "user": "kddi"
                    },
                    {
                        "command": "-cl",
                        "from": "10.1.0.1",
                        "idle-time": {
                            "#text": "3"
                        },
                        "login-time": {
                            "#text": "7:45AM"
                        },
                        "tty": "pts/2",
                        "user": "kddi"
                    }
                ]
            }
        }
    }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemUsers(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_parsed_output_1)
        obj = ShowSystemUsers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_output_1)

if __name__ == '__main__':
    unittest.main()