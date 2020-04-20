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
                                                ShowSystemUsers,
                                                ShowSystemCommit)

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
        cisco     pts/0    10.1.0.1                          2:35AM      - -cl
        cisco     pts/1    10.1.0.1                          8:31AM     56 -cl
        cisco     pts/2    10.1.0.1                          7:45AM      3 -cl
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
                        "user": "cisco"
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
                        "user": "cisco"
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
                        "user": "cisco"
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


#=========================================================
# Unit test for show system commit
#=========================================================
class TestShowSystemBuffer(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    maxDiff = None

    golden_parsed_output_1 = {
        "commit-information": {
            "commit-history": [
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 16:04:34 UTC",
                    },
                    "sequence-number": "0",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 16:01:49 UTC",
                    },
                    "sequence-number": "1",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:53:03 UTC",
                    },
                    "sequence-number": "2",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:51:16 UTC",
                    },
                    "sequence-number": "3",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:02:37 UTC",
                    },
                    "sequence-number": "4",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:00:57 UTC",
                    },
                    "sequence-number": "5",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 14:58:06 UTC",
                    },
                    "sequence-number": "6",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 14:49:36 UTC",
                    },
                    "sequence-number": "7",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 14:47:49 UTC",
                    },
                    "sequence-number": "8",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 00:07:34 UTC",
                    },
                    "sequence-number": "9",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 00:04:48 UTC",
                    },
                    "sequence-number": "10",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 23:58:42 UTC",
                    },
                    "sequence-number": "11",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 21:58:30 UTC",
                    },
                    "sequence-number": "12",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 02:27:13 UTC",
                    },
                    "sequence-number": "13",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 02:11:40 UTC",
                    },
                    "sequence-number": "14",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 01:50:35 UTC",
                    },
                    "sequence-number": "15",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 01:06:08 UTC",
                    },
                    "sequence-number": "16",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 00:23:13 UTC",
                    },
                    "sequence-number": "17",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 23:15:16 UTC",
                    },
                    "sequence-number": "18",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 18:32:59 UTC",
                    },
                    "sequence-number": "19",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 18:30:05 UTC",
                    },
                    "sequence-number": "20",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 18:24:06 UTC",
                    },
                    "sequence-number": "21",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:58:04 UTC",
                    },
                    "sequence-number": "22",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:46:09 UTC",
                    },
                    "sequence-number": "23",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:26:19 UTC",
                    },
                    "sequence-number": "24",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:07:59 UTC",
                    },
                    "sequence-number": "25",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:48:07 UTC",
                    },
                    "sequence-number": "26",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:22:09 UTC",
                    },
                    "sequence-number": "27",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:20:28 UTC",
                    },
                    "sequence-number": "28",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:17:33 UTC",
                    },
                    "sequence-number": "29",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:15:45 UTC",
                    },
                    "sequence-number": "30",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 11:10:33 UTC",
                    },
                    "sequence-number": "31",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 11:08:14 UTC",
                    },
                    "sequence-number": "32",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 08:41:29 UTC",
                    },
                    "sequence-number": "33",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 08:25:57 UTC",
                    },
                    "sequence-number": "34",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 08:09:34 UTC",
                    },
                    "sequence-number": "35",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 07:49:00 UTC",
                    },
                    "sequence-number": "36",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 07:39:35 UTC",
                    },
                    "sequence-number": "37",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 07:23:14 UTC",
                    },
                    "sequence-number": "38",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 05:41:34 UTC",
                    },
                    "sequence-number": "39",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 04:23:30 UTC",
                    },
                    "sequence-number": "40",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 19:05:48 UTC",
                    },
                    "sequence-number": "41",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 19:02:29 UTC",
                    },
                    "sequence-number": "42",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:34:53 UTC",
                    },
                    "sequence-number": "43",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:26:08 UTC",
                    },
                    "sequence-number": "44",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:10:44 UTC",
                    },
                    "sequence-number": "45",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:04:23 UTC",
                    },
                    "sequence-number": "46",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 15:45:11 UTC",
                    },
                    "sequence-number": "47",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 09:28:52 UTC",
                    },
                    "sequence-number": "48",
                    "user": "cisco"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 08:42:26 UTC",
                    },
                    "sequence-number": "49",
                    "user": "cisco"
                }
            ]
        }
    }


    golden_output_1 = {'execute.return_value': '''
                show system commit
                0   2020-03-05 16:04:34 UTC by cisco via cli
                1   2020-03-05 16:01:49 UTC by cisco via cli
                2   2020-03-05 15:53:03 UTC by cisco via cli
                3   2020-03-05 15:51:16 UTC by cisco via cli
                4   2020-03-05 15:02:37 UTC by cisco via cli
                5   2020-03-05 15:00:57 UTC by cisco via cli
                6   2020-03-05 14:58:06 UTC by cisco via cli
                7   2020-03-05 14:49:36 UTC by cisco via cli
                8   2020-03-05 14:47:49 UTC by cisco via cli
                9   2020-03-05 00:07:34 UTC by cisco via cli
                10  2020-03-05 00:04:48 UTC by cisco via cli
                11  2020-03-04 23:58:42 UTC by cisco via cli
                12  2020-03-04 21:58:30 UTC by cisco via cli
                13  2020-03-04 02:27:13 UTC by cisco via cli
                14  2020-03-04 02:11:40 UTC by cisco via cli
                15  2020-03-04 01:50:35 UTC by cisco via cli
                16  2020-03-04 01:06:08 UTC by cisco via cli
                17  2020-03-04 00:23:13 UTC by cisco via cli
                18  2020-03-03 23:15:16 UTC by cisco via cli
                19  2020-03-03 18:32:59 UTC by cisco via cli
                20  2020-03-03 18:30:05 UTC by cisco via cli
                21  2020-03-03 18:24:06 UTC by cisco via cli
                22  2020-03-03 15:58:04 UTC by cisco via cli
                23  2020-03-03 15:46:09 UTC by cisco via cli
                24  2020-03-03 15:26:19 UTC by cisco via cli
                25  2020-03-03 15:07:59 UTC by cisco via cli
                26  2020-03-03 14:48:07 UTC by cisco via cli
                27  2020-03-03 14:22:09 UTC by cisco via cli
                28  2020-03-03 14:20:28 UTC by cisco via cli
                29  2020-03-03 14:17:33 UTC by cisco via cli
                30  2020-03-03 14:15:45 UTC by cisco via cli
                31  2020-03-03 11:10:33 UTC by cisco via cli
                32  2020-03-03 11:08:14 UTC by cisco via cli
                33  2020-03-03 08:41:29 UTC by cisco via cli
                34  2020-03-03 08:25:57 UTC by cisco via cli
                35  2020-03-03 08:09:34 UTC by cisco via cli
                36  2020-03-03 07:49:00 UTC by cisco via cli
                37  2020-03-03 07:39:35 UTC by cisco via cli
                38  2020-03-03 07:23:14 UTC by cisco via cli
                39  2020-03-03 05:41:34 UTC by cisco via cli
                40  2020-03-03 04:23:30 UTC by cisco via cli
                41  2020-03-02 19:05:48 UTC by cisco via cli
                42  2020-03-02 19:02:29 UTC by cisco via cli
                43  2020-03-02 16:34:53 UTC by cisco via cli
                44  2020-03-02 16:26:08 UTC by cisco via cli
                45  2020-03-02 16:10:44 UTC by cisco via cli
                46  2020-03-02 16:04:23 UTC by cisco via cli
                47  2020-03-02 15:45:11 UTC by cisco via cli
                48  2020-03-02 09:28:52 UTC by cisco via cli
                49  2020-03-02 08:42:26 UTC by cisco via cli

    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemCommit(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemCommit(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()