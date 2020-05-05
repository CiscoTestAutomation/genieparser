# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import (
    SchemaEmptyParserError,
    SchemaMissingKeyError,
)

# Parser
from genie.libs.parser.junos.show_system import (
    ShowSystemUptime,
    ShowSystemUptimeNoForwarding,
    ShowSystemBuffers,
    ShowSystemCommit,
    ShowSystemQueues,
    ShowSystemQueuesNoForwarding,
    ShowSystemUsers,
    ShowSystemBuffersNoForwarding,
    ShowSystemUsers,
    ShowSystemStorage,
    ShowSystemCoreDumps,
    ShowSystemCoreDumpsNoForwarding,
    ShowSystemStorageNoForwarding
)

# =========================================================
# Unit test for show system buffers
# =========================================================
class TestShowSystemBuffers(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None
    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "memory-statistics": {
            "cached-bytes": "1971",
            "cached-jumbo-clusters-16k": "0",
            "cached-jumbo-clusters-4k": "2",
            "cached-jumbo-clusters-9k": "0",
            "cached-mbuf-clusters": "714",
            "cached-mbufs": "2142",
            "cluster-failures": "0",
            "current-bytes-in-use": "1179",
            "current-jumbo-clusters-16k": "0",
            "current-jumbo-clusters-4k": "0",
            "current-jumbo-clusters-9k": "0",
            "current-mbuf-clusters": "516",
            "current-mbufs": "588",
            "io-initiated": "0",
            "jumbo-cluster-failures-16k": "0",
            "jumbo-cluster-failures-4k": "0",
            "jumbo-cluster-failures-9k": "0",
            "max-jumbo-clusters-16k": "10396",
            "max-jumbo-clusters-4k": "62377",
            "max-jumbo-clusters-9k": "18482",
            "max-mbuf-clusters": "124756",
            "mbuf-failures": "0",
            "packet-count": "513",
            "packet-failures": "0",
            "packet-free": "499",
            "sfbuf-requests-delayed": "0",
            "sfbuf-requests-denied": "0",
            "total-bytes": "3150",
            "total-jumbo-clusters-16k": "0",
            "total-jumbo-clusters-4k": "2",
            "total-jumbo-clusters-9k": "0",
            "total-mbuf-clusters": "1230",
            "total-mbufs": "2730",
        }
    }

    golden_output_1 = {
        "execute.return_value": """
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

    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemBuffers(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemBuffers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =========================================================
# Unit test for show system Users
# =========================================================
class TestShowSystemUsers(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "execute.return_value": """
        show system users
        9:38AM  up 209 days, 37 mins, 3 users, load averages: 0.28, 0.39, 0.37
        USER     TTY      FROM                              LOGIN@  IDLE WHAT
        cisco     pts/0    10.1.0.1                          2:35AM      - -cl
        cisco     pts/1    10.1.0.1                          8:31AM     56 -cl
        cisco     pts/2    10.1.0.1                          7:45AM      3 -cl
        """
    }

    golden_output_1 = {
        "system-users-information": {
            "uptime-information": {
                "active-user-count": {"#text": "3"},
                "date-time": {"#text": "9:38AM"},
                "load-average-1": "0.28",
                "load-average-15": "0.39",
                "load-average-5": "0.37",
                "up-time": {"#text": "209 days, 37 mins"},
                "user-table": {
                    "user-entry": [
                        {
                            "command": "-cl",
                            "from": "10.1.0.1",
                            "idle-time": {"#text": "-"},
                            "login-time": {"#text": "2:35AM"},
                            "tty": "pts/0",
                            "user": "cisco",
                        },
                        {
                            "command": "-cl",
                            "from": "10.1.0.1",
                            "idle-time": {"#text": "56"},
                            "login-time": {"#text": "8:31AM"},
                            "tty": "pts/1",
                            "user": "cisco",
                        },
                        {
                            "command": "-cl",
                            "from": "10.1.0.1",
                            "idle-time": {"#text": "3"},
                            "login-time": {"#text": "7:45AM"},
                            "tty": "pts/2",
                            "user": "cisco",
                        },
                    ]
                },
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


# =========================================================
# Unit test for show system commit
# =========================================================
class TestShowSystemCommit(unittest.TestCase):

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    maxDiff = None

    golden_parsed_output_1 = {
        "commit-information": {
            "commit-history": [
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 16:04:34 UTC",},
                    "sequence-number": "0",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 16:01:49 UTC",},
                    "sequence-number": "1",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 15:53:03 UTC",},
                    "sequence-number": "2",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 15:51:16 UTC",},
                    "sequence-number": "3",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 15:02:37 UTC",},
                    "sequence-number": "4",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 15:00:57 UTC",},
                    "sequence-number": "5",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 14:58:06 UTC",},
                    "sequence-number": "6",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 14:49:36 UTC",},
                    "sequence-number": "7",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 14:47:49 UTC",},
                    "sequence-number": "8",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 00:07:34 UTC",},
                    "sequence-number": "9",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-05 00:04:48 UTC",},
                    "sequence-number": "10",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-04 23:58:42 UTC",},
                    "sequence-number": "11",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-04 21:58:30 UTC",},
                    "sequence-number": "12",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-04 02:27:13 UTC",},
                    "sequence-number": "13",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-04 02:11:40 UTC",},
                    "sequence-number": "14",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-04 01:50:35 UTC",},
                    "sequence-number": "15",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-04 01:06:08 UTC",},
                    "sequence-number": "16",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-04 00:23:13 UTC",},
                    "sequence-number": "17",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 23:15:16 UTC",},
                    "sequence-number": "18",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 18:32:59 UTC",},
                    "sequence-number": "19",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 18:30:05 UTC",},
                    "sequence-number": "20",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 18:24:06 UTC",},
                    "sequence-number": "21",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 15:58:04 UTC",},
                    "sequence-number": "22",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 15:46:09 UTC",},
                    "sequence-number": "23",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 15:26:19 UTC",},
                    "sequence-number": "24",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 15:07:59 UTC",},
                    "sequence-number": "25",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 14:48:07 UTC",},
                    "sequence-number": "26",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 14:22:09 UTC",},
                    "sequence-number": "27",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 14:20:28 UTC",},
                    "sequence-number": "28",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 14:17:33 UTC",},
                    "sequence-number": "29",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 14:15:45 UTC",},
                    "sequence-number": "30",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 11:10:33 UTC",},
                    "sequence-number": "31",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 11:08:14 UTC",},
                    "sequence-number": "32",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 08:41:29 UTC",},
                    "sequence-number": "33",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 08:25:57 UTC",},
                    "sequence-number": "34",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 08:09:34 UTC",},
                    "sequence-number": "35",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 07:49:00 UTC",},
                    "sequence-number": "36",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 07:39:35 UTC",},
                    "sequence-number": "37",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 07:23:14 UTC",},
                    "sequence-number": "38",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 05:41:34 UTC",},
                    "sequence-number": "39",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-03 04:23:30 UTC",},
                    "sequence-number": "40",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-02 19:05:48 UTC",},
                    "sequence-number": "41",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-02 19:02:29 UTC",},
                    "sequence-number": "42",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-02 16:34:53 UTC",},
                    "sequence-number": "43",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-02 16:26:08 UTC",},
                    "sequence-number": "44",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-02 16:10:44 UTC",},
                    "sequence-number": "45",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-02 16:04:23 UTC",},
                    "sequence-number": "46",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-02 15:45:11 UTC",},
                    "sequence-number": "47",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-02 09:28:52 UTC",},
                    "sequence-number": "48",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {"#text": "2020-03-02 08:42:26 UTC",},
                    "sequence-number": "49",
                    "user": "cisco",
                },
            ]
        }
    }

    golden_output_1 = {
        "execute.return_value": """
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

    """
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


# =========================================================
# Unit test for show system queues
# =========================================================
class TestShowSystemQueues(unittest.TestCase):

    maxDiff = None

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

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
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "dsc",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "lo0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "gre",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "ipip",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "tap",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "pime",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "pimd",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "fxp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "em1",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "mtun",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "demux0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "cbp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "pip0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "125000",
                        "max-packets-allowed": "416",
                        "name": "pp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "irb",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "vtep",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "esi",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "rbeb",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti1",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti2",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti3",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti4",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti5",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti6",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti7",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "jsrv",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "lc-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "pfh-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "pfe-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/0",
                        "number-of-queue-drops": "3",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/1",
                        "number-of-queue-drops": "3",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/2",
                        "number-of-queue-drops": "132",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/3",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/4",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/5",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/6",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/7",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/8",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/9",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
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
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1000000",
                        "max-packets-allowed": "1000",
                        "name": "splnetq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1000000",
                        "max-packets-allowed": "1000",
                        "name": "optionq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "50000",
                        "max-packets-allowed": "50",
                        "name": "icmpq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "frlmiq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "25000",
                        "max-packets-allowed": "1000",
                        "name": "spppintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "atmctlpktq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "atmoamq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "tnpintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "200000",
                        "max-packets-allowed": "200",
                        "name": "tagintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "200000",
                        "max-packets-allowed": "200",
                        "name": "tagfragq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                ]
            },
        }
    }

    golden_output_1 = {
        "execute.return_value": """
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
    """
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


# =========================================================
# Unit test for show system queues no-forwarding
# =========================================================
class TestShowSystemQueuesNoForwarding(unittest.TestCase):

    maxDiff = None

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

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
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "dsc",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "lo0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "gre",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "ipip",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "tap",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "pime",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "pimd",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "fxp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "em1",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500",
                        "max-packets-allowed": "41",
                        "name": "mtun",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "demux0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "cbp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "pip0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "125000",
                        "max-packets-allowed": "416",
                        "name": "pp0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "irb",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "vtep",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "esi",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "rbeb",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti1",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti2",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti3",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti4",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti5",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti6",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "fti7",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "12500000",
                        "max-packets-allowed": "41666",
                        "name": "jsrv",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "lc-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "pfh-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "pfe-0/0/0",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/0",
                        "number-of-queue-drops": "3",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/1",
                        "number-of-queue-drops": "3",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/2",
                        "number-of-queue-drops": "132",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/3",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/4",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/5",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/6",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/7",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/8",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "ge-0/0/9",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
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
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1000000",
                        "max-packets-allowed": "1000",
                        "name": "splnetq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1000000",
                        "max-packets-allowed": "1000",
                        "name": "optionq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "50000",
                        "max-packets-allowed": "50",
                        "name": "icmpq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "frlmiq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "25000",
                        "max-packets-allowed": "1000",
                        "name": "spppintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "atmctlpktq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "0",
                        "max-packets-allowed": "0",
                        "name": "atmoamq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "1250000",
                        "max-packets-allowed": "4166",
                        "name": "tnpintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "200000",
                        "max-packets-allowed": "200",
                        "name": "tagintrq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                    {
                        "max-octets-allowed": "200000",
                        "max-packets-allowed": "200",
                        "name": "tagfragq",
                        "number-of-queue-drops": "0",
                        "octets-in-queue": "0",
                        "packets-in-queue": "0",
                    },
                ]
            },
        }
    }

    golden_output_1 = {
        "execute.return_value": """
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
    """
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


# =========================================================
# Unit test for show system storage
# =========================================================
class TestShowSystemStorage(unittest.TestCase):

    maxDiff = None

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "system-storage-information": {
            "filesystem": [
                {
                    "available-blocks": {"junos:format": "17G"},
                    "filesystem-name": "/dev/gpt/junos",
                    "mounted-on": "/.mount",
                    "total-blocks": {"junos:format": "20G"},
                    "used-blocks": {"junos:format": "1.2G"},
                    "used-percent": "7%",
                },
                {
                    "available-blocks": {"junos:format": "730M"},
                    "filesystem-name": "/dev/gpt/config",
                    "mounted-on": "/.mount/config",
                    "total-blocks": {"junos:format": "793M"},
                    "used-blocks": {"junos:format": "60K"},
                    "used-percent": "0%",
                },
                {
                    "available-blocks": {"junos:format": "6.3G"},
                    "filesystem-name": "/dev/gpt/var",
                    "mounted-on": "/.mount/var",
                    "total-blocks": {"junos:format": "7.0G"},
                    "used-blocks": {"junos:format": "117M"},
                    "used-percent": "2%",
                },
                {
                    "available-blocks": {"junos:format": "3.2G"},
                    "filesystem-name": "tmpfs",
                    "mounted-on": "/.mount/tmp",
                    "total-blocks": {"junos:format": "3.2G"},
                    "used-blocks": {"junos:format": "196K"},
                    "used-percent": "0%",
                },
                {
                    "available-blocks": {"junos:format": "333M"},
                    "filesystem-name": "tmpfs",
                    "mounted-on": "/.mount/mfs",
                    "total-blocks": {"junos:format": "334M"},
                    "used-blocks": {"junos:format": "748K"},
                    "used-percent": "0%",
                },
            ]
        }
    }

    golden_output_1 = {
        "execute.return_value": """
                show system storage | no-more
        Filesystem              Size       Used      Avail  Capacity   Mounted on
        /dev/gpt/junos           20G       1.2G        17G        7%  /.mount
        /dev/gpt/config         793M        60K       730M        0%  /.mount/config
        /dev/gpt/var            7.0G       117M       6.3G        2%  /.mount/var
        tmpfs                   3.2G       196K       3.2G        0%  /.mount/tmp
        tmpfs                   334M       748K       333M        0%  /.mount/mfs
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemStorage(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemStorage(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =========================================================
# Unit test for show system storage no-forwarding
# =========================================================
class TestShowSystemStorageNoForwarding(unittest.TestCase):

    maxDiff = None

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "system-storage-information": {
            "filesystem": [
                {
                    "available-blocks": {"junos:format": "17G"},
                    "filesystem-name": "/dev/gpt/junos",
                    "mounted-on": "/.mount",
                    "total-blocks": {"junos:format": "20G"},
                    "used-blocks": {"junos:format": "1.2G"},
                    "used-percent": "7%",
                },
                {
                    "available-blocks": {"junos:format": "730M"},
                    "filesystem-name": "/dev/gpt/config",
                    "mounted-on": "/.mount/config",
                    "total-blocks": {"junos:format": "793M"},
                    "used-blocks": {"junos:format": "60K"},
                    "used-percent": "0%",
                },
                {
                    "available-blocks": {"junos:format": "6.3G"},
                    "filesystem-name": "/dev/gpt/var",
                    "mounted-on": "/.mount/var",
                    "total-blocks": {"junos:format": "7.0G"},
                    "used-blocks": {"junos:format": "117M"},
                    "used-percent": "2%",
                },
                {
                    "available-blocks": {"junos:format": "3.2G"},
                    "filesystem-name": "tmpfs",
                    "mounted-on": "/.mount/tmp",
                    "total-blocks": {"junos:format": "3.2G"},
                    "used-blocks": {"junos:format": "196K"},
                    "used-percent": "0%",
                },
                {
                    "available-blocks": {"junos:format": "333M"},
                    "filesystem-name": "tmpfs",
                    "mounted-on": "/.mount/mfs",
                    "total-blocks": {"junos:format": "334M"},
                    "used-blocks": {"junos:format": "748K"},
                    "used-percent": "0%",
                },
            ]
        }
    }

    golden_output_1 = {
        "execute.return_value": """
                show system storage no-forwarding
        Filesystem              Size       Used      Avail  Capacity   Mounted on
        /dev/gpt/junos           20G       1.2G        17G        7%  /.mount
        /dev/gpt/config         793M        60K       730M        0%  /.mount/config
        /dev/gpt/var            7.0G       117M       6.3G        2%  /.mount/var
        tmpfs                   3.2G       196K       3.2G        0%  /.mount/tmp
        tmpfs                   334M       748K       333M        0%  /.mount/mfs
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemStorageNoForwarding(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemStorageNoForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =========================================================
# Unit test for show system buffers no-forwarding
# =========================================================
class TestShowSystemBufferNoForwarding(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "memory-statistics": {
            "cached-bytes": "1975",
            "cached-jumbo-clusters-16k": "0",
            "cached-jumbo-clusters-4k": "3",
            "cached-jumbo-clusters-9k": "0",
            "cached-mbuf-clusters": "714",
            "cached-mbufs": "2142",
            "cluster-failures": "0",
            "current-bytes-in-use": "1179",
            "current-jumbo-clusters-16k": "0",
            "current-jumbo-clusters-4k": "0",
            "current-jumbo-clusters-9k": "0",
            "current-mbuf-clusters": "516",
            "current-mbufs": "588",
            "io-initiated": "0",
            "jumbo-cluster-failures-16k": "0",
            "jumbo-cluster-failures-4k": "0",
            "jumbo-cluster-failures-9k": "0",
            "max-jumbo-clusters-16k": "10396",
            "max-jumbo-clusters-4k": "62377",
            "max-jumbo-clusters-9k": "18482",
            "max-mbuf-clusters": "124756",
            "mbuf-failures": "0",
            "packet-count": "513",
            "packet-failures": "0",
            "packet-free": "499",
            "sfbuf-requests-delayed": "0",
            "sfbuf-requests-denied": "0",
            "total-bytes": "3154",
            "total-jumbo-clusters-16k": "0",
            "total-jumbo-clusters-4k": "3",
            "total-jumbo-clusters-9k": "0",
            "total-mbuf-clusters": "1230",
            "total-mbufs": "2730",
        }
    }

    golden_output_1 = {
        "execute.return_value": """
        show system buffers no-forwarding
        588/2142/2730 mbufs in use (current/cache/total)
        516/714/1230/124756 mbuf clusters in use (current/cache/total/max)
        513/499 mbuf+clusters out of packet secondary zone in use (current/cache)
        0/3/3/62377 4k (page size) jumbo clusters in use (current/cache/total/max)
        0/0/0/18482 9k (page size) jumbo clusters in use (current/cache/total/max)
        0/0/0/10396 16k (page size) jumbo clusters in use (current/cache/total/max)
        1179K/1975K/3154K bytes allocated to network (current/cache/total)
        0/0/0 requests for mbufs denied (mbufs/clusters/mbuf+clusters)
        0/0/0 requests for jumbo clusters denied (4k/9k/16k)
        0 requests for sfbufs denied
        0 requests for sfbufs delayed
        0 requests for I/O initiated by sendfile

    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemBuffersNoForwarding(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemBuffersNoForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =========================================================
# Unit test for show system core-dumps
# =========================================================
class TestShowSystemCoreDumps(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "directory-list": {
            "directory": {
                "file-information": [
                    {
                        "file-date": {"@junos:format": "Aug 8   2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.riot.mpc0.1565307741.1716.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "1252383",
                    },
                    {
                        "file-date": {"@junos:format": "Aug 8   2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565307747.1791.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "4576464",
                    },
                    {
                        "file-date": {"@junos:format": "Aug 15  2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565841060.1528.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "1139316",
                    },
                    {
                        "file-date": {"@junos:format": "Aug 15  2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565841991.4312.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "1139249",
                    },
                    {
                        "file-date": {"@junos:format": "Aug 15  2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565842608.6212.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "1139299",
                    },
                    {
                        "file-date": {"@junos:format": "Aug 15  2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565892564.3392.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "1139321",
                    },
                ],
                "output": [
                    "/var/tmp/*core*: No such file or directory",
                    "/var/tmp/pics/*core*: No such file or directory",
                    "/var/crash/kernel.*: No such file or directory",
                    "/var/jails/rest-api/tmp/*core*: No such file or directory",
                    "/tftpboot/corefiles/*core*: No such file or directory",
                ],
                "total-files": "6",
            }
        }
    }

    golden_output_1 = {
        "execute.return_value": """
                show system core-dumps
                -rw-r--r--  1 root  wheel    1252383 Aug 8   2019 /var/crash/core.riot.mpc0.1565307741.1716.gz
                -rw-r--r--  1 root  wheel    4576464 Aug 8   2019 /var/crash/core.vmxt.mpc0.1565307747.1791.gz
                -rw-r--r--  1 root  wheel    1139316 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565841060.1528.gz
                -rw-r--r--  1 root  wheel    1139249 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565841991.4312.gz
                -rw-r--r--  1 root  wheel    1139299 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565842608.6212.gz
                -rw-r--r--  1 root  wheel    1139321 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565892564.3392.gz
                /var/tmp/*core*: No such file or directory
                /var/tmp/pics/*core*: No such file or directory
                /var/crash/kernel.*: No such file or directory
                /var/jails/rest-api/tmp/*core*: No such file or directory
                /tftpboot/corefiles/*core*: No such file or directory
                total files: 6

    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemCoreDumps(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemCoreDumps(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =========================================================
# Unit test for show system core-dumps no-forwarding
# =========================================================
class TestShowSystemCoreDumpsNoForwarding(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "directory-list": {
            "directory": {
                "file-information": [
                    {
                        "file-date": {"@junos:format": "Aug 8   2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.riot.mpc0.1565307741.1716.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "1252383",
                    },
                    {
                        "file-date": {"@junos:format": "Aug 8   2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565307747.1791.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "4576464",
                    },
                    {
                        "file-date": {"@junos:format": "Aug 15  2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565841060.1528.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "1139316",
                    },
                    {
                        "file-date": {"@junos:format": "Aug 15  2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565841991.4312.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "1139249",
                    },
                    {
                        "file-date": {"@junos:format": "Aug 15  2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565842608.6212.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "1139299",
                    },
                    {
                        "file-date": {"@junos:format": "Aug 15  2019"},
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565892564.3392.gz",
                        "file-owner": "root",
                        "file-permissions": {"@junos:format": "-rw-r--r--"},
                        "file-size": "1139321",
                    },
                ],
                "output": [
                    "/var/tmp/*core*: No such file or directory",
                    "/var/tmp/pics/*core*: No such file or directory",
                    "/var/crash/kernel.*: No such file or directory",
                    "/var/jails/rest-api/tmp/*core*: No such file or directory",
                    "/tftpboot/corefiles/*core*: No such file or directory",
                ],
                "total-files": "6",
            }
        }
    }

    golden_output_1 = {
        "execute.return_value": """
                show system core-dumps  no-forwarding
                -rw-r--r--  1 root  wheel    1252383 Aug 8   2019 /var/crash/core.riot.mpc0.1565307741.1716.gz
                -rw-r--r--  1 root  wheel    4576464 Aug 8   2019 /var/crash/core.vmxt.mpc0.1565307747.1791.gz
                -rw-r--r--  1 root  wheel    1139316 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565841060.1528.gz
                -rw-r--r--  1 root  wheel    1139249 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565841991.4312.gz
                -rw-r--r--  1 root  wheel    1139299 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565842608.6212.gz
                -rw-r--r--  1 root  wheel    1139321 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565892564.3392.gz
                /var/tmp/*core*: No such file or directory
                /var/tmp/pics/*core*: No such file or directory
                /var/crash/kernel.*: No such file or directory
                /var/jails/rest-api/tmp/*core*: No such file or directory
                /tftpboot/corefiles/*core*: No such file or directory
                total files: 6

    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemCoreDumpsNoForwarding(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemCoreDumpsNoForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =========================================================
# Unit test for show system buffer
# =========================================================
class TestShowSystemUptime(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "execute.return_value": """
        show system uptime
        Current time: 2020-03-26 08:16:41 UTC
        Time Source:  LOCAL CLOCK
        System booted: 2019-08-29 09:02:22 UTC (29w6d 23:14 ago)
        Protocols started: 2019-08-29 09:03:25 UTC (29w6d 23:13 ago)
        Last configured: 2020-03-05 16:04:34 UTC (2w6d 16:12 ago) by cisco
        8:16AM  up 209 days, 23:14, 5 users, load averages: 0.43, 0.43, 0.42
    """
    }

    golden_output_1 = {
        "system-uptime-information": {
            "current-time": {"date-time": {"#text": "2020-03-26 08:16:41 UTC"}},
            "last-configured-time": {
                "date-time": {"#text": "2020-03-05 16:04:34 UTC "},
                "time-length": {"#text": "2w6d 16:12"},
                "user": "cisco",
            },
            "protocols-started-time": {
                "date-time": {"#text": "2019-08-29 09:03:25 UTC"},
                "time-length": {"#text": "29w6d 23:13"},
            },
            "system-booted-time": {
                "date-time": {"#text": "2019-08-29 09:02:22 UTC"},
                "time-length": {"#text": "29w6d 23:14"},
            },
            "time-source": "LOCAL CLOCK",
            "uptime-information": {
                "active-user-count": {"#text": "5"},
                "date-time": {"#text": "8:16AM"},
                "load-average-1": "0.43",
                "load-average-15": "0.43",
                "load-average-5": "0.42",
                "up-time": {"#text": "209 days, 23:14 mins,"},
            },
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemUptime(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_parsed_output_1)
        obj = ShowSystemUptime(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_output_1)


class TestShowSystemUptimeNoForwarding(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "execute.return_value": """
        show system uptime no-forwarding
        Current time: 2020-03-25 09:38:14 UTC
        Time Source:  LOCAL CLOCK
        System booted: 2019-08-29 09:02:22 UTC (29w6d 00:35 ago)
        Protocols started: 2019-08-29 09:03:25 UTC (29w6d 00:34 ago)
        Last configured: 2020-03-05 16:04:34 UTC (2w5d 17:33 ago) by cisco
        9:38AM  up 209 days, 36 mins, 3 users, load averages: 0.29, 0.41, 0.38
    """
    }

    golden_output_1 = {
        "system-uptime-information": {
            "current-time": {"date-time": {"#text": "2020-03-25 09:38:14 UTC"}},
            "last-configured-time": {
                "date-time": {"#text": "2020-03-05 16:04:34 UTC "},
                "time-length": {"#text": "2w5d 17:33"},
                "user": "cisco",
            },
            "protocols-started-time": {
                "date-time": {"#text": "2019-08-29 09:03:25 UTC"},
                "time-length": {"#text": "29w6d 00:34"},
            },
            "system-booted-time": {
                "date-time": {"#text": "2019-08-29 09:02:22 UTC"},
                "time-length": {"#text": "29w6d 00:35"},
            },
            "time-source": "LOCAL CLOCK",
            "uptime-information": {
                "active-user-count": {"#text": "3"},
                "date-time": {"#text": "9:38AM"},
                "load-average-1": "0.29",
                "load-average-15": "0.41",
                "load-average-5": "0.38",
                "up-time": {"#text": "209 days, 36 mins,"},
            },
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemUptimeNoForwarding(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_parsed_output_1)
        obj = ShowSystemUptimeNoForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_output_1)


if __name__ == "__main__":
    unittest.main()
