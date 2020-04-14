# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.junos.show_system import ShowSystemBuffer, ShowSystemCommit

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
# Unit test for show system commit
#=========================================================
class test_show_system_commit(unittest.TestCase):

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
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 16:01:49 UTC",
                    },
                    "sequence-number": "1",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:53:03 UTC",
                    },
                    "sequence-number": "2",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:51:16 UTC",
                    },
                    "sequence-number": "3",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:02:37 UTC",
                    },
                    "sequence-number": "4",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:00:57 UTC",
                    },
                    "sequence-number": "5",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 14:58:06 UTC",
                    },
                    "sequence-number": "6",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 14:49:36 UTC",
                    },
                    "sequence-number": "7",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 14:47:49 UTC",
                    },
                    "sequence-number": "8",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 00:07:34 UTC",
                    },
                    "sequence-number": "9",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 00:04:48 UTC",
                    },
                    "sequence-number": "10",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 23:58:42 UTC",
                    },
                    "sequence-number": "11",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 21:58:30 UTC",
                    },
                    "sequence-number": "12",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 02:27:13 UTC",
                    },
                    "sequence-number": "13",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 02:11:40 UTC",
                    },
                    "sequence-number": "14",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 01:50:35 UTC",
                    },
                    "sequence-number": "15",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 01:06:08 UTC",
                    },
                    "sequence-number": "16",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 00:23:13 UTC",
                    },
                    "sequence-number": "17",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 23:15:16 UTC",
                    },
                    "sequence-number": "18",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 18:32:59 UTC",
                    },
                    "sequence-number": "19",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 18:30:05 UTC",
                    },
                    "sequence-number": "20",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 18:24:06 UTC",
                    },
                    "sequence-number": "21",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:58:04 UTC",
                    },
                    "sequence-number": "22",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:46:09 UTC",
                    },
                    "sequence-number": "23",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:26:19 UTC",
                    },
                    "sequence-number": "24",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:07:59 UTC",
                    },
                    "sequence-number": "25",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:48:07 UTC",
                    },
                    "sequence-number": "26",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:22:09 UTC",
                    },
                    "sequence-number": "27",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:20:28 UTC",
                    },
                    "sequence-number": "28",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:17:33 UTC",
                    },
                    "sequence-number": "29",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:15:45 UTC",
                    },
                    "sequence-number": "30",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 11:10:33 UTC",
                    },
                    "sequence-number": "31",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 11:08:14 UTC",
                    },
                    "sequence-number": "32",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 08:41:29 UTC",
                    },
                    "sequence-number": "33",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 08:25:57 UTC",
                    },
                    "sequence-number": "34",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 08:09:34 UTC",
                    },
                    "sequence-number": "35",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 07:49:00 UTC",
                    },
                    "sequence-number": "36",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 07:39:35 UTC",
                    },
                    "sequence-number": "37",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 07:23:14 UTC",
                    },
                    "sequence-number": "38",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 05:41:34 UTC",
                    },
                    "sequence-number": "39",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 04:23:30 UTC",
                    },
                    "sequence-number": "40",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 19:05:48 UTC",
                    },
                    "sequence-number": "41",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 19:02:29 UTC",
                    },
                    "sequence-number": "42",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:34:53 UTC",
                    },
                    "sequence-number": "43",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:26:08 UTC",
                    },
                    "sequence-number": "44",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:10:44 UTC",
                    },
                    "sequence-number": "45",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:04:23 UTC",
                    },
                    "sequence-number": "46",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 15:45:11 UTC",
                    },
                    "sequence-number": "47",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 09:28:52 UTC",
                    },
                    "sequence-number": "48",
                    "user": "kddi"
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 08:42:26 UTC",
                    },
                    "sequence-number": "49",
                    "user": "kddi"
                }
            ]
        }
    }


    golden_output_1 = {'execute.return_value': '''
                show system commit
                0   2020-03-05 16:04:34 UTC by kddi via cli
                1   2020-03-05 16:01:49 UTC by kddi via cli
                2   2020-03-05 15:53:03 UTC by kddi via cli
                3   2020-03-05 15:51:16 UTC by kddi via cli
                4   2020-03-05 15:02:37 UTC by kddi via cli
                5   2020-03-05 15:00:57 UTC by kddi via cli
                6   2020-03-05 14:58:06 UTC by kddi via cli
                7   2020-03-05 14:49:36 UTC by kddi via cli
                8   2020-03-05 14:47:49 UTC by kddi via cli
                9   2020-03-05 00:07:34 UTC by kddi via cli
                10  2020-03-05 00:04:48 UTC by kddi via cli
                11  2020-03-04 23:58:42 UTC by kddi via cli
                12  2020-03-04 21:58:30 UTC by kddi via cli
                13  2020-03-04 02:27:13 UTC by kddi via cli
                14  2020-03-04 02:11:40 UTC by kddi via cli
                15  2020-03-04 01:50:35 UTC by kddi via cli
                16  2020-03-04 01:06:08 UTC by kddi via cli
                17  2020-03-04 00:23:13 UTC by kddi via cli
                18  2020-03-03 23:15:16 UTC by kddi via cli
                19  2020-03-03 18:32:59 UTC by kddi via cli
                20  2020-03-03 18:30:05 UTC by kddi via cli
                21  2020-03-03 18:24:06 UTC by kddi via cli
                22  2020-03-03 15:58:04 UTC by kddi via cli
                23  2020-03-03 15:46:09 UTC by kddi via cli
                24  2020-03-03 15:26:19 UTC by kddi via cli
                25  2020-03-03 15:07:59 UTC by kddi via cli
                26  2020-03-03 14:48:07 UTC by kddi via cli
                27  2020-03-03 14:22:09 UTC by kddi via cli
                28  2020-03-03 14:20:28 UTC by kddi via cli
                29  2020-03-03 14:17:33 UTC by kddi via cli
                30  2020-03-03 14:15:45 UTC by kddi via cli
                31  2020-03-03 11:10:33 UTC by kddi via cli
                32  2020-03-03 11:08:14 UTC by kddi via cli
                33  2020-03-03 08:41:29 UTC by kddi via cli
                34  2020-03-03 08:25:57 UTC by kddi via cli
                35  2020-03-03 08:09:34 UTC by kddi via cli
                36  2020-03-03 07:49:00 UTC by kddi via cli
                37  2020-03-03 07:39:35 UTC by kddi via cli
                38  2020-03-03 07:23:14 UTC by kddi via cli
                39  2020-03-03 05:41:34 UTC by kddi via cli
                40  2020-03-03 04:23:30 UTC by kddi via cli
                41  2020-03-02 19:05:48 UTC by kddi via cli
                42  2020-03-02 19:02:29 UTC by kddi via cli
                43  2020-03-02 16:34:53 UTC by kddi via cli
                44  2020-03-02 16:26:08 UTC by kddi via cli
                45  2020-03-02 16:10:44 UTC by kddi via cli
                46  2020-03-02 16:04:23 UTC by kddi via cli
                47  2020-03-02 15:45:11 UTC by kddi via cli
                48  2020-03-02 09:28:52 UTC by kddi via cli
                49  2020-03-02 08:42:26 UTC by kddi via cli

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