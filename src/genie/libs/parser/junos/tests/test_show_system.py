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
    ShowSystemUptime, ShowSystemUptimeNoForwarding, ShowSystemBuffers,
    ShowSystemCommit, ShowSystemQueues, ShowSystemQueuesNoForwarding,
    ShowSystemUsers, ShowSystemBuffersNoForwarding, ShowSystemUsers,
    ShowSystemStorage, ShowSystemCoreDumps, ShowSystemCoreDumpsNoForwarding,
    ShowSystemStorageNoForwarding, ShowSystemStatistics,
    ShowSystemStatisticsNoForwarding)


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
        "execute.return_value":
        """
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
        "execute.return_value":
        """
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
                            "user": "cisco",
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
                            "user": "cisco",
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
                            "user": "cisco",
                        },
                    ]
                },
            }
        }
    }

    golden_parsed_output_2 = {
        "execute.return_value":
        """
        11:31PM  up 2 days,  1:04, 1 user, load averages: 0.04, 0.03, 0.01
        USER     TTY      FROM                              LOGIN@  IDLE WHAT
        cisco     d0       -                                Mon10PM     - -cli (cli)
        """
    }

    golden_output_2 = {
        "system-users-information": {
            "uptime-information": {
                "active-user-count": {
                    "#text": "1"
                },
                "date-time": {
                    "#text": "11:31PM"
                },
                "load-average-1": "0.04",
                "load-average-15": "0.03",
                "load-average-5": "0.01",
                "up-time": {
                    "#text": "2 days,  1:04"
                },
                "user-table": {
                    "user-entry": [{
                        "command": "-cli (cli)",
                        "from": "-",
                        "idle-time": {
                            "#text": "-"
                        },
                        "login-time": {
                            "#text": "Mon10PM"
                        },
                        "tty": "d0",
                        "user": "cisco",
                    }]
                },
            }
        }
    }

    golden_parsed_output_3 = {
        "execute.return_value":
        """
        11:36PM  up 2 days,  5 hrs, 2 users, load averages: 0.00, 0.00, 0.00
        USER     TTY      FROM                              LOGIN@  IDLE WHAT
        cisco     d0       -                                Mon10PM 2days -cli (cli)
        cisco     p0       255.255.255.255                     11:36PM     - -cli (cli)
        """
    }

    golden_output_3 = {
        "system-users-information": {
            "uptime-information": {
                "active-user-count": {
                    "#text": "2"
                },
                "date-time": {
                    "#text": "11:36PM"
                },
                "load-average-1": "0.00",
                "load-average-15": "0.00",
                "load-average-5": "0.00",
                "up-time": {
                    "#text": "2 days,  5 hrs"
                },
                "user-table": {
                    "user-entry": [{
                        "command": "-cli (cli)",
                        "from": "-",
                        "idle-time": {
                            "#text": "2days"
                        },
                        "login-time": {
                            "#text": "Mon10PM"
                        },
                        "tty": "d0",
                        "user": "cisco",
                    }, {
                        "command": "-cli (cli)",
                        "from": "255.255.255.255",
                        "idle-time": {
                            "#text": "-"
                        },
                        "login-time": {
                            "#text": "11:36PM"
                        },
                        "tty": "p0",
                        "user": "cisco",
                    }]
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

    def test_golden_2(self):
        self.device = Mock(**self.golden_parsed_output_2)
        obj = ShowSystemUsers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_parsed_output_3)
        obj = ShowSystemUsers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_output_3)


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
                    "date-time": {
                        "#text": "2020-03-05 16:04:34 UTC",
                    },
                    "sequence-number": "0",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 16:01:49 UTC",
                    },
                    "sequence-number": "1",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:53:03 UTC",
                    },
                    "sequence-number": "2",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:51:16 UTC",
                    },
                    "sequence-number": "3",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:02:37 UTC",
                    },
                    "sequence-number": "4",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 15:00:57 UTC",
                    },
                    "sequence-number": "5",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 14:58:06 UTC",
                    },
                    "sequence-number": "6",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 14:49:36 UTC",
                    },
                    "sequence-number": "7",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 14:47:49 UTC",
                    },
                    "sequence-number": "8",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 00:07:34 UTC",
                    },
                    "sequence-number": "9",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-05 00:04:48 UTC",
                    },
                    "sequence-number": "10",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 23:58:42 UTC",
                    },
                    "sequence-number": "11",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 21:58:30 UTC",
                    },
                    "sequence-number": "12",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 02:27:13 UTC",
                    },
                    "sequence-number": "13",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 02:11:40 UTC",
                    },
                    "sequence-number": "14",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 01:50:35 UTC",
                    },
                    "sequence-number": "15",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 01:06:08 UTC",
                    },
                    "sequence-number": "16",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-04 00:23:13 UTC",
                    },
                    "sequence-number": "17",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 23:15:16 UTC",
                    },
                    "sequence-number": "18",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 18:32:59 UTC",
                    },
                    "sequence-number": "19",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 18:30:05 UTC",
                    },
                    "sequence-number": "20",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 18:24:06 UTC",
                    },
                    "sequence-number": "21",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:58:04 UTC",
                    },
                    "sequence-number": "22",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:46:09 UTC",
                    },
                    "sequence-number": "23",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:26:19 UTC",
                    },
                    "sequence-number": "24",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 15:07:59 UTC",
                    },
                    "sequence-number": "25",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:48:07 UTC",
                    },
                    "sequence-number": "26",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:22:09 UTC",
                    },
                    "sequence-number": "27",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:20:28 UTC",
                    },
                    "sequence-number": "28",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:17:33 UTC",
                    },
                    "sequence-number": "29",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 14:15:45 UTC",
                    },
                    "sequence-number": "30",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 11:10:33 UTC",
                    },
                    "sequence-number": "31",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 11:08:14 UTC",
                    },
                    "sequence-number": "32",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 08:41:29 UTC",
                    },
                    "sequence-number": "33",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 08:25:57 UTC",
                    },
                    "sequence-number": "34",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 08:09:34 UTC",
                    },
                    "sequence-number": "35",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 07:49:00 UTC",
                    },
                    "sequence-number": "36",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 07:39:35 UTC",
                    },
                    "sequence-number": "37",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 07:23:14 UTC",
                    },
                    "sequence-number": "38",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 05:41:34 UTC",
                    },
                    "sequence-number": "39",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-03 04:23:30 UTC",
                    },
                    "sequence-number": "40",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 19:05:48 UTC",
                    },
                    "sequence-number": "41",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 19:02:29 UTC",
                    },
                    "sequence-number": "42",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:34:53 UTC",
                    },
                    "sequence-number": "43",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:26:08 UTC",
                    },
                    "sequence-number": "44",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:10:44 UTC",
                    },
                    "sequence-number": "45",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 16:04:23 UTC",
                    },
                    "sequence-number": "46",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 15:45:11 UTC",
                    },
                    "sequence-number": "47",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 09:28:52 UTC",
                    },
                    "sequence-number": "48",
                    "user": "cisco",
                },
                {
                    "client": "cli",
                    "date-time": {
                        "#text": "2020-03-02 08:42:26 UTC",
                    },
                    "sequence-number": "49",
                    "user": "cisco",
                },
            ]
        }
    }

    golden_output_1 = {
        "execute.return_value":
        """
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
        "execute.return_value":
        """
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
        "execute.return_value":
        """
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
                    "available-blocks": {
                        "junos:format": "17G"
                    },
                    "filesystem-name": "/dev/gpt/junos",
                    "mounted-on": "/.mount",
                    "total-blocks": {
                        "junos:format": "20G"
                    },
                    "used-blocks": {
                        "junos:format": "1.2G"
                    },
                    "used-percent": "7%",
                },
                {
                    "available-blocks": {
                        "junos:format": "730M"
                    },
                    "filesystem-name": "/dev/gpt/config",
                    "mounted-on": "/.mount/config",
                    "total-blocks": {
                        "junos:format": "793M"
                    },
                    "used-blocks": {
                        "junos:format": "60K"
                    },
                    "used-percent": "0%",
                },
                {
                    "available-blocks": {
                        "junos:format": "6.3G"
                    },
                    "filesystem-name": "/dev/gpt/var",
                    "mounted-on": "/.mount/var",
                    "total-blocks": {
                        "junos:format": "7.0G"
                    },
                    "used-blocks": {
                        "junos:format": "117M"
                    },
                    "used-percent": "2%",
                },
                {
                    "available-blocks": {
                        "junos:format": "3.2G"
                    },
                    "filesystem-name": "tmpfs",
                    "mounted-on": "/.mount/tmp",
                    "total-blocks": {
                        "junos:format": "3.2G"
                    },
                    "used-blocks": {
                        "junos:format": "196K"
                    },
                    "used-percent": "0%",
                },
                {
                    "available-blocks": {
                        "junos:format": "333M"
                    },
                    "filesystem-name": "tmpfs",
                    "mounted-on": "/.mount/mfs",
                    "total-blocks": {
                        "junos:format": "334M"
                    },
                    "used-blocks": {
                        "junos:format": "748K"
                    },
                    "used-percent": "0%",
                },
            ]
        }
    }

    golden_output_1 = {
        "execute.return_value":
        """
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
                    "available-blocks": {
                        "junos:format": "17G"
                    },
                    "filesystem-name": "/dev/gpt/junos",
                    "mounted-on": "/.mount",
                    "total-blocks": {
                        "junos:format": "20G"
                    },
                    "used-blocks": {
                        "junos:format": "1.2G"
                    },
                    "used-percent": "7%",
                },
                {
                    "available-blocks": {
                        "junos:format": "730M"
                    },
                    "filesystem-name": "/dev/gpt/config",
                    "mounted-on": "/.mount/config",
                    "total-blocks": {
                        "junos:format": "793M"
                    },
                    "used-blocks": {
                        "junos:format": "60K"
                    },
                    "used-percent": "0%",
                },
                {
                    "available-blocks": {
                        "junos:format": "6.3G"
                    },
                    "filesystem-name": "/dev/gpt/var",
                    "mounted-on": "/.mount/var",
                    "total-blocks": {
                        "junos:format": "7.0G"
                    },
                    "used-blocks": {
                        "junos:format": "117M"
                    },
                    "used-percent": "2%",
                },
                {
                    "available-blocks": {
                        "junos:format": "3.2G"
                    },
                    "filesystem-name": "tmpfs",
                    "mounted-on": "/.mount/tmp",
                    "total-blocks": {
                        "junos:format": "3.2G"
                    },
                    "used-blocks": {
                        "junos:format": "196K"
                    },
                    "used-percent": "0%",
                },
                {
                    "available-blocks": {
                        "junos:format": "333M"
                    },
                    "filesystem-name": "tmpfs",
                    "mounted-on": "/.mount/mfs",
                    "total-blocks": {
                        "junos:format": "334M"
                    },
                    "used-blocks": {
                        "junos:format": "748K"
                    },
                    "used-percent": "0%",
                },
            ]
        }
    }

    golden_output_1 = {
        "execute.return_value":
        """
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
        "execute.return_value":
        """
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
                        "file-date": {
                            "@junos:format": "Aug 8   2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.riot.mpc0.1565307741.1716.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1252383",
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 8   2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.vmxt.mpc0.1565307747.1791.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "4576464",
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.vmxt.mpc0.1565841060.1528.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1139316",
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.vmxt.mpc0.1565841991.4312.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1139249",
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.vmxt.mpc0.1565842608.6212.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1139299",
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.vmxt.mpc0.1565892564.3392.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
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
                "total-files":
                "6",
            }
        }
    }

    golden_output_1 = {
        "execute.return_value":
        """
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
                        "file-date": {
                            "@junos:format": "Aug 8   2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.riot.mpc0.1565307741.1716.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1252383",
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 8   2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.vmxt.mpc0.1565307747.1791.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "4576464",
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.vmxt.mpc0.1565841060.1528.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1139316",
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.vmxt.mpc0.1565841991.4312.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1139249",
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.vmxt.mpc0.1565842608.6212.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1139299",
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name":
                        "/var/crash/core.vmxt.mpc0.1565892564.3392.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
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
                "total-files":
                "6",
            }
        }
    }

    golden_output_1 = {
        "execute.return_value":
        """
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
        "execute.return_value":
        """
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
            "current-time": {
                "date-time": {
                    "#text": "2020-03-26 08:16:41 UTC"
                }
            },
            "last-configured-time": {
                "date-time": {
                    "#text": "2020-03-05 16:04:34 UTC "
                },
                "time-length": {
                    "#text": "2w6d 16:12"
                },
                "user": "cisco",
            },
            "protocols-started-time": {
                "date-time": {
                    "#text": "2019-08-29 09:03:25 UTC"
                },
                "time-length": {
                    "#text": "29w6d 23:13"
                },
            },
            "system-booted-time": {
                "date-time": {
                    "#text": "2019-08-29 09:02:22 UTC"
                },
                "time-length": {
                    "#text": "29w6d 23:14"
                },
            },
            "time-source": "LOCAL CLOCK",
            "uptime-information": {
                "active-user-count": {
                    "#text": "5"
                },
                "date-time": {
                    "#text": "8:16AM"
                },
                "load-average-1": "0.43",
                "load-average-15": "0.43",
                "load-average-5": "0.42",
                "up-time": {
                    "#text": "209 days, 23:14 mins,",
                    '@junos:seconds': '18141240'
                },
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
        "execute.return_value":
        """
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
            "current-time": {
                "date-time": {
                    "#text": "2020-03-25 09:38:14 UTC"
                }
            },
            "last-configured-time": {
                "date-time": {
                    "#text": "2020-03-05 16:04:34 UTC "
                },
                "time-length": {
                    "#text": "2w5d 17:33"
                },
                "user": "cisco",
            },
            "protocols-started-time": {
                "date-time": {
                    "#text": "2019-08-29 09:03:25 UTC"
                },
                "time-length": {
                    "#text": "29w6d 00:34"
                },
            },
            "system-booted-time": {
                "date-time": {
                    "#text": "2019-08-29 09:02:22 UTC"
                },
                "time-length": {
                    "#text": "29w6d 00:35"
                },
            },
            "time-source": "LOCAL CLOCK",
            "uptime-information": {
                "active-user-count": {
                    "#text": "3"
                },
                "date-time": {
                    "#text": "9:38AM"
                },
                "load-average-1": "0.29",
                "load-average-15": "0.41",
                "load-average-5": "0.38",
                "up-time": {
                    "#text": "209 days, 36 mins,",
                    '@junos:seconds': '18187200'
                },
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


# =========================================================
# Unit test for show system statistics
# =========================================================
class TestShowSystemStatistics(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "statistics": [
            {
                "ah": {
                    "bytes-in": "0",
                    "bytes-out": "0",
                    "crypto-processing-failure": "0",
                    "packets-blocked-due-to-policy": "0",
                    "packets-dropped-as-bad-authentication-detected": "0",
                    "packets-dropped-as-larger-than-ip-maxpacket": "0",
                    "packets-dropped-as-protocol-unsupported": "0",
                    "packets-dropped-due-to-bad-authentication-length": "0",
                    "packets-dropped-due-to-bad-kcr": "0",
                    "packets-dropped-due-to-invalid-tdb": "0",
                    "packets-dropped-due-to-no-tdb": "0",
                    "packets-dropped-due-to-no-transform": "0",
                    "packets-dropped-due-to-queue-full": "0",
                    "packets-in": "0",
                    "packets-out": "0",
                    "packets-shorter-than-header-shows": "0",
                    "possible-replay-packets-detected": "0",
                    "replay-counter-wrap": "0",
                    "tunnel-sanity-check-failures": "0",
                },
                "arp": {
                    "arp-iri-cnt":
                    "1",
                    "arp-iri-drop":
                    "0",
                    "arp-iri-max":
                    "200",
                    "arp-mgt-cnt":
                    "2",
                    "arp-mgt-drop":
                    "0",
                    "arp-mgt-max":
                    "14960",
                    "arp-packets-are-dropped-as-driver-call-failed":
                    "0",
                    "arp-packets-are-dropped-as-nexthop-allocation-failed":
                    "0",
                    "arp-packets-are-dropped-as-source-is-not-validated":
                    "0",
                    "arp-packets-are-dropped-from-peer-vrrp":
                    "0",
                    "arp-packets-are-rejected-as-target-ip-arp-resolve-is-in-progress":
                    "0",
                    "arp-packets-received-from-peer-vrrp-router-and-discarded":
                    "0",
                    "arp-packets-rejected-as-family-is-configured-with-deny-arp":
                    "0",
                    "arp-probe-for-proxy-address-reachable-from-the-incoming-interface":
                    "0",
                    "arp-public-cnt":
                    "4",
                    "arp-public-drop":
                    "0",
                    "arp-public-max":
                    "59840",
                    "arp-replies-are-rejected-as-source-and-destination-is-same":
                    "0",
                    "arp-replies-received":
                    "54355",
                    "arp-replies-sent":
                    "39895",
                    "arp-request-discarded-for-vrrp-source-address":
                    "0",
                    "arp-requests-received":
                    "39895",
                    "arp-requests-sent":
                    "55086",
                    "arp-response-packets-are-rejected-on-mace-icl-interface":
                    "0",
                    "arp-system-drop":
                    "0",
                    "arp-system-max":
                    "75000",
                    "datagrams-for-an-address-not-on-the-interface":
                    "0",
                    "datagrams-for-non-ip-protocol":
                    "0",
                    "datagrams-received":
                    "200794",
                    "datagrams-which-were-not-for-me":
                    "106457",
                    "datagrams-with-a-broadcast-source-address":
                    "0",
                    "datagrams-with-bad-hardware-address-length":
                    "0",
                    "datagrams-with-bad-protocol-address-length":
                    "0",
                    "datagrams-with-bogus-interface":
                    "0",
                    "datagrams-with-incorrect-length":
                    "0",
                    "datagrams-with-multicast-source-address":
                    "0",
                    "datagrams-with-multicast-target-address":
                    "87",
                    "datagrams-with-my-own-hardware-address":
                    "0",
                    "datagrams-with-source-address-duplicate-to-mine":
                    "0",
                    "datagrams-with-unsupported-opcode":
                    "0",
                    "grat-arp-packets-are-ignored-as-mac-address-is-not-changed":
                    "0",
                    "new-requests-on-unnumbered-interfaces":
                    "0",
                    "packets-discarded-waiting-for-resolution":
                    "7",
                    "packets-sent-after-waiting-for-resolution":
                    "15",
                    "proxy-arp-request-discarded-as-source-ip-is-a-proxy-target":
                    "0",
                    "proxy-requests-not-proxied":
                    "0",
                    "received-proxy-requests":
                    "0",
                    "replies-from-unnumbered-interface-with-non-subnetted-donor":
                    "0",
                    "replies-from-unnumbered-interfaces":
                    "0",
                    "requests-dropped-due-to-interface-deletion":
                    "0",
                    "requests-dropped-during-retry":
                    "0",
                    "requests-dropped-on-entry":
                    "0",
                    "requests-for-memory-denied":
                    "0",
                    "requests-on-unnumbered-interface-with-non-subnetted-donor":
                    "0",
                    "requests-on-unnumbered-interfaces":
                    "0",
                    "resolution-request-dropped":
                    "0",
                    "resolution-request-received":
                    "109",
                    "restricted-proxy-requests":
                    "0",
                    "restricted-proxy-requests-not-proxied":
                    "0",
                    "self-arp-request-packet-received-on-irb-interface":
                    "0",
                    "unrestricted-proxy-requests":
                    "0",
                },
                "clnl": {
                    "address-fields-were-not-reasonable": "0",
                    "bad-version-packets": "0",
                    "er-pdu-generation-failure": "0",
                    "error-pdu-rate-drops": "0",
                    "forwarded-packets": "0",
                    "fragmentation-prohibited": "0",
                    "fragments-discarded": "0",
                    "fragments-sent": "0",
                    "fragments-timed-out": "0",
                    "mcopy-failure": "0",
                    "no-free-memory-in-socket-buffer": "0",
                    "non-forwarded-packets": "0",
                    "output-packets-discarded": "0",
                    "packets-delivered": "0",
                    "packets-destined-to-dead-nexthop": "0",
                    "packets-discarded-due-to-no-route": "0",
                    "packets-fragmented": "0",
                    "packets-reconstructed": "0",
                    "packets-with-bad-checksum": "0",
                    "packets-with-bad-header-length": "0",
                    "packets-with-bogus-sdl-size": "0",
                    "sbappend-failure": "0",
                    "segment-information-forgotten": "0",
                    "send-packets-discarded": "0",
                    "too-small-packets": "0",
                    "total-clnl-packets-received": "0",
                    "total-packets-sent": "0",
                    "unknown-or-unsupported-protocol-packets": "0",
                },
                "esis": {
                    "iso-family-not-configured": "0",
                    "mcopy-failure": "0",
                    "no-free-memory-in-socket-buffer": "0",
                    "pdus-received-with-bad-checksum": "0",
                    "pdus-received-with-bad-type-field": "0",
                    "pdus-received-with-bad-version-number": "0",
                    "pdus-with-bad-header-length": "0",
                    "pdus-with-bogus-sdl-size": "0",
                    "pdus-with-unknown-or-unsupport-protocol": "0",
                    "sbappend-failure": "0",
                    "send-packets-discarded": "0",
                    "short-pdus-received": "0",
                    "total-esis-packets-received": "0",
                    "total-packets-consumed-by-protocol": "0",
                },
                "esp": {
                    "esp-bytes-in": "0",
                    "esp-bytes-out": "0",
                    "esp-crypto-processing-failure": "0",
                    "esp-packets-blocked-due-to-policy": "0",
                    "esp-packets-dropped-as-bad-authentication-detected": "0",
                    "esp-packets-dropped-as-bad-encryption-detected": "0",
                    "esp-packets-dropped-as-bad-ilen": "0",
                    "esp-packets-dropped-as-invalid-tdb": "0",
                    "esp-packets-dropped-as-larger-than-ip-maxpacket": "0",
                    "esp-packets-dropped-as-protocol-not-supported": "0",
                    "esp-packets-dropped-due-to-bad-kcr": "0",
                    "esp-packets-dropped-due-to-no-tdb": "0",
                    "esp-packets-dropped-due-to-no-transform": "0",
                    "esp-packets-dropped-due-to-queue-full": "0",
                    "esp-packets-in": "0",
                    "esp-packets-out": "0",
                    "esp-packets-shorter-than-header-shows": "0",
                    "esp-possible-replay-packets-detected": "0",
                    "esp-replay-counter-wrap": "0",
                    "esp-tunnel-sanity-check-failures": "0",
                },
                "ethoamcfm": {
                    "flood-requests-dropped": "0",
                    "flood-requests-forwarded-to-pfe": "0",
                    "input-packets-drop-bad-interface-state": "0",
                    "output-packets-drop-bad-interface-state": "0",
                    "packets-sent": "0",
                    "received-packets-forwarded": "0",
                    "total-packets-received": "0",
                    "total-packets-transmitted": "0",
                },
                "ethoamlfm": {
                    "input-packets-drop-bad-interface-state": "0",
                    "output-packets-drop-bad-interface-state": "0",
                    "packets-sent": "0",
                    "received-packets-forwarded": "0",
                    "total-packets-received": "0",
                    "total-packets-transmitted": "0",
                },
                "icmp": {
                    "calls-to-icmp-error":
                    "17647",
                    "drops-due-to-rate-limit":
                    "0",
                    "echo-drops-with-broadcast-or-multicast-destinaton-address":
                    "0",
                    "errors-not-generated-because-old-message-was-icmp":
                    "115",
                    "histogram": [
                        {
                            "destination-unreachable": "13553",
                            "icmp-echo": "15",
                            "icmp-echo-reply": "18108704",
                            "time-exceeded": "4094",
                            "type-of-histogram": "Output "
                            "Histogram",
                        },
                        {
                            "destination-unreachable": "7376316",
                            "icmp-echo": "18108704",
                            "icmp-echo-reply": "15",
                            "time-exceeded": "11308300",
                            "type-of-histogram": "Input "
                            "Histogram",
                        },
                    ],
                    "message-responses-generated":
                    "18108704",
                    "messages-less-than-the-minimum-length":
                    "0",
                    "messages-with-bad-checksum":
                    "0",
                    "messages-with-bad-code-fields":
                    "0",
                    "messages-with-bad-length":
                    "0",
                    "messages-with-bad-source-address":
                    "0",
                    "timestamp-drops-with-broadcast-or-multicast-destination-address":
                    "0",
                },
                "icmp6": {
                    "address-unreachable":
                    "31",
                    "administratively-prohibited":
                    "0",
                    "bad-checksums":
                    "0",
                    "beyond-scope":
                    "0",
                    "calls-to-icmp6-error":
                    "31",
                    "erroneous-header-field":
                    "0",
                    "errors-not-generated-because-old-message-was-icmp-error":
                    "0",
                    "errors-not-generated-because-rate-limitation":
                    "0",
                    "histogram-of-error-messages-to-be-generated":
                    "Histogram "
                    "of "
                    "error "
                    "messages "
                    "to "
                    "be "
                    "generated:",
                    "icmp6-message-responses-generated":
                    "0",
                    "icmp6-messages-with-bad-code-fields":
                    "0",
                    "icmp6-messages-with-bad-length":
                    "0",
                    "input-histogram": {
                        "histogram-type": "Input "
                        "histogram:",
                        "neighbor-advertisement": "543766",
                        "neighbor-solicitation": "544587",
                        "router-advertisement-icmp6-packets": "168",
                        "router-solicitation-icmp6-packets": "8",
                        "time-exceeded-icmp6-packets": "6773206",
                        "unreachable-icmp6-packets": "319",
                    },
                    "messages-less-than-minimum-length":
                    "0",
                    "messages-with-too-many-nd-options":
                    "0",
                    "nd-iri-cnt":
                    "1",
                    "nd-iri-drop":
                    "0",
                    "nd-iri-max":
                    "200",
                    "nd-mgt-cnt":
                    "0",
                    "nd-mgt-drop":
                    "0",
                    "nd-mgt-max":
                    "14960",
                    "nd-public-cnt":
                    "3",
                    "nd-public-drop":
                    "0",
                    "nd-public-max":
                    "59840",
                    "nd-system-drop":
                    "0",
                    "nd-system-max":
                    "75000",
                    "nd6-dad-proxy-conflicts":
                    "0",
                    "nd6-dad-proxy-eqmac-drop":
                    "0",
                    "nd6-dad-proxy-nomac-drop":
                    "543766",
                    "nd6-dad-proxy-requests":
                    "0",
                    "nd6-dad-proxy-resolve-cnt":
                    "0",
                    "nd6-dup-proxy-responses":
                    "0",
                    "nd6-ndp-proxy-requests":
                    "0",
                    "nd6-ndp-proxy-resolve-cnt":
                    "0",
                    "nd6-ndp-proxy-responses":
                    "0",
                    "nd6-requests-dropped-during-retry":
                    "0",
                    "nd6-requests-dropped-on-entry":
                    "0",
                    "no-route":
                    "0",
                    "output-histogram": {
                        "histogram-type": "Output "
                        "histogram:",
                        "neighbor-advertisement": "544593",
                        "neighbor-solicitation": "544914",
                        "unreachable-icmp6-packets": "31",
                    },
                    "port-unreachable":
                    "0",
                    "protocol-name":
                    "icmp6:",
                    "time-exceed-reassembly":
                    "0",
                    "time-exceed-transit":
                    "0",
                    "unknown":
                    "0",
                    "unrecognized-next-header":
                    "0",
                    "unrecognized-option":
                    "0",
                },
                "igmp": {
                    "membership-queries-received": "308",
                    "membership-queries-received-with-invalid-fields": "0",
                    "membership-reports-received": "0",
                    "membership-reports-received-for-groups-to-which-we-belong":
                    "0",
                    "membership-reports-received-with-invalid-fields": "0",
                    "membership-reports-sent": "943",
                    "messages-received": "310",
                    "messages-received-with-bad-checksum": "0",
                    "messages-received-with-too-few-bytes": "0",
                },
                "ip": {
                    "bad-header-checksums": "0",
                    "datagrams-that-can-not-be-fragmented": "0",
                    "fragments-created": "458290",
                    "fragments-dropped-after-timeout": "2330",
                    "fragments-dropped-due-to-outofspace-or-dup": "0",
                    "fragments-dropped-due-to-queueoverflow": "0",
                    "fragments-received": "7776172",
                    "incoming-rawip-packets-dropped-no-socket-buffer": "46",
                    "incoming-ttpoip-packets-dropped": "0",
                    "incoming-ttpoip-packets-received": "184307157",
                    "incoming-virtual-node-packets-delivered": "0",
                    "loose-source-and-record-route-options": "0",
                    "multicast-packets-dropped": "0",
                    "option-packets-dropped-due-to-rate-limit": "0",
                    "outgoing-ttpoip-packets-dropped": "0",
                    "outgoing-ttpoip-packets-sent": "185307601",
                    "output-datagrams-fragmented": "189762",
                    "output-packets-discarded-due-to-no-route": "221",
                    "output-packets-dropped-due-to-no-bufs": "0",
                    "packets-destined-to-dead-next-hop": "0",
                    "packets-dropped": "0",
                    "packets-for-this-host": "820964812",
                    "packets-for-unknown-or-unsupported-protocol": "311",
                    "packets-forwarded": "0",
                    "packets-not-forwardable": "0",
                    "packets-reassembled-ok": "3840557",
                    "packets-received": "791039285",
                    "packets-sent-from-this-host": "894567482",
                    "packets-sent-with-fabricated-ip-header": "10684334",
                    "packets-used-first-nexthop-in-ecmp-unilist": "0",
                    "packets-with-bad-options": "0",
                    "packets-with-data-length-less-than-headerlength": "0",
                    "packets-with-data-size-less-than-datalength": "0",
                    "packets-with-header-length-less-than-data-size": "0",
                    "packets-with-incorrect-version-number": "0",
                    "packets-with-options-handled-without-error": "310",
                    "packets-with-size-smaller-than-minimum": "0",
                    "record-route-options": "0",
                    "redirects-sent": "0",
                    "router-alert-options": "310",
                    "strict-source-and-record-route-options": "0",
                    "timestamp-and-address-options": "0",
                    "timestamp-and-prespecified-address-options": "0",
                    "timestamp-options": "0",
                    "transit-re-packets-dropped-on-mgmt-interface": "0",
                },
                "ip6": {
                    "duplicate-or-out-of-space-fragments-dropped":
                    "0",
                    "failures-of-source-address-selection":
                    "0",
                    "forward-cache-hit":
                    "0",
                    "forward-cache-miss":
                    "0",
                    "fragments-that-exceeded-limit":
                    "0",
                    "header-type": [
                        {
                            "globals":
                            "557",
                            "header-for-source-address-selection":
                            "source "
                            "addresses "
                            "on "
                            "an "
                            "outgoing "
                            "I/F",
                            "link-locals":
                            "1088799",
                        },
                        {
                            "globals":
                            "556",
                            "header-for-source-address-selection":
                            "source "
                            "addresses "
                            "of "
                            "same "
                            "scope",
                            "link-locals":
                            "1088799",
                        },
                        {
                            "globals":
                            "1",
                            "header-for-source-address-selection":
                            "source "
                            "addresses "
                            "of "
                            "a "
                            "different "
                            "scope",
                        },
                    ],
                    "histogram":
                    "Input histogram:",
                    "ip6-datagrams-that-can-not-be-fragmented":
                    "0",
                    "ip6-fragments-created":
                    "0",
                    "ip6-fragments-dropped-after-timeout":
                    "0",
                    "ip6-fragments-received":
                    "0",
                    "ip6-option-packets-dropped-due-to-rate-limit":
                    "0",
                    "ip6-output-datagrams-fragmented":
                    "0",
                    "ip6-output-packets-discarded-due-to-no-route":
                    "1026",
                    "ip6-output-packets-dropped-due-to-no-bufs":
                    "0",
                    "ip6-packets-destined-to-dead-next-hop":
                    "0",
                    "ip6-packets-dropped":
                    "0",
                    "ip6-packets-for-this-host":
                    "100720272",
                    "ip6-packets-forwarded":
                    "0",
                    "ip6-packets-not-forwardable":
                    "0",
                    "ip6-packets-reassembled-ok":
                    "0",
                    "ip6-packets-sent-from-this-host":
                    "101649920",
                    "ip6-packets-sent-with-fabricated-ip-header":
                    "4506372",
                    "ip6-packets-with-bad-options":
                    "0",
                    "ip6-packets-with-incorrect-version-number":
                    "0",
                    "ip6-packets-with-size-smaller-than-minimum":
                    "0",
                    "ip6-redirects-sent":
                    "0",
                    "ip6nh-icmp6":
                    "7862032",
                    "ip6nh-ospf":
                    "4501665",
                    "ip6nh-tcp":
                    "5981247",
                    "ip6nh-udp":
                    "82375306",
                    "multicast-packets-which-we-do-not-join":
                    "0",
                    "packets-discarded-due-to-too-may-headers":
                    "0",
                    "packets-dropped-due-to-bad-protocol":
                    "0",
                    "packets-that-violated-scope-rules":
                    "0",
                    "packets-whose-headers-are-not-continuous":
                    "0",
                    "packets-with-datasize-less-than-data-length":
                    "0",
                    "total-packets-received":
                    "100720281",
                    "transit-re-packet-dropped-on-mgmt-interface":
                    "0",
                    "tunneling-packets-that-can-not-find-gif":
                    "0",
                },
                "ipcomp": {
                    "ipcomp-bytes-in": "0",
                    "ipcomp-bytes-out": "0",
                    "ipcomp-crypto-processing-failure": "0",
                    "ipcomp-packets-blocked-due-to-policy": "0",
                    "ipcomp-packets-dropped-as-invalid-tdb": "0",
                    "ipcomp-packets-dropped-as-larger-than-ip-maxpacket": "0",
                    "ipcomp-packets-dropped-as-protocol-not-supported": "0",
                    "ipcomp-packets-dropped-due-to-bad-kcr": "0",
                    "ipcomp-packets-dropped-due-to-no-tdb": "0",
                    "ipcomp-packets-dropped-due-to-no-transform": "0",
                    "ipcomp-packets-dropped-due-to-queue-full": "0",
                    "ipcomp-packets-in": "0",
                    "ipcomp-packets-out": "0",
                    "ipcomp-packets-shorter-than-header-shows": "0",
                    "ipcomp-replay-counter-wrap": "0",
                    "packets-sent-uncompressed-threshold": "0",
                    "packets-sent-uncompressed-useless": "0",
                },
                "ipsec": {
                    "cluster-coalesced-during-clone": "0",
                    "cluster-copied-during-clone": "0",
                    "inbound-packets-violated-process-security-policy": "0",
                    "invalid-outbound-packets": "0",
                    "mbuf-coalesced-during-clone": "0",
                    "mbuf-inserted-during-makespace": "0",
                    "outbound-packets-failed-due-to-insufficient-memory": "0",
                    "outbound-packets-violated-process-security-policy": "0",
                    "outbound-packets-with-bundled-sa": "0",
                    "outbound-packets-with-no-route": "0",
                    "outbound-packets-with-no-sa-available": "0",
                },
                "ipsec6": {
                    "cluster-coalesced-during-clone": "0",
                    "cluster-copied-during-clone": "0",
                    "inbound-packets-violated-process-security-policy": "0",
                    "invalid-outbound-packets": "0",
                    "mbuf-coalesced-during-clone": "0",
                    "mbuf-inserted-during-makespace": "0",
                    "outbound-packets-failed-due-to-insufficient-memory": "0",
                    "outbound-packets-violated-process-security-policy": "0",
                    "outbound-packets-with-bundled-sa": "0",
                    "outbound-packets-with-no-route": "0",
                    "outbound-packets-with-no-sa-available": "0",
                },
                "mpls": {
                    "after-tagging-packets-can-not-fit-link-mtu": "0",
                    "lsp-ping-packets": "5",
                    "packets-discarded-due-to-no-route": "0",
                    "packets-dropped": "0",
                    "packets-dropped-at-mpls-socket-send": "0",
                    "packets-dropped-at-p2mp-cnh-output": "0",
                    "packets-dropped-due-to-ifl-down": "0",
                    "packets-forwarded": "6118",
                    "packets-forwarded-at-mpls-socket-send": "0",
                    "packets-used-first-nexthop-in-ecmp-unilist": "0",
                    "packets-with-header-too-small": "0",
                    "packets-with-ipv4-explicit-null-checksum-errors": "0",
                    "packets-with-ipv4-explicit-null-tag": "0",
                    "packets-with-router-alert-tag": "0",
                    "packets-with-tag-encoding-error": "0",
                    "packets-with-ttl-expired": "4209",
                    "total-mpls-packets-received": "4214",
                },
                "pfkey": {
                    "bytes-sent-from-userland": "69304",
                    "bytes-sent-to-userland": "3189032",
                    "incoming-messages-with-memory-allocation-failure": "0",
                    "input-histogram": {
                        "add": "17",
                        "dump": "10626",
                        "histogram": "histogram by "
                        "message type:",
                        "reserved": "626",
                    },
                    "messages-too-short": "0",
                    "messages-toward-all-sockets": "0",
                    "messages-toward-registered-sockets": "0",
                    "messages-toward-single-socket": "22500",
                    "messages-with-duplicate-extension": "0",
                    "messages-with-invalid-address-extension": "0",
                    "messages-with-invalid-extension-type": "0",
                    "messages-with-invalid-length-field": "0",
                    "messages-with-invalid-message-type-field": "0",
                    "messages-with-invalid-sa-type": "0",
                    "messages-with-invalid-version-field": "0",
                    "outgoing-messages-with-memory-allocation-failure": "0",
                    "output-histogram": {
                        "add": "17",
                        "dump": "626",
                        "histogram": "histogram by "
                        "message type:",
                        "reserved": "626",
                    },
                    "requests-sent-from-userland": "1269",
                    "requests-sent-to-userland": "11269",
                },
                "raw-interface": {
                    "dialer-packets-received": "0",
                    "dialer-packets-transmitted": "0",
                    "faboam-packets-dropped": "0",
                    "faboam-packets-received": "0",
                    "faboam-packets-transmitted": "0",
                    "fibre-channel-packets-dropped": "0",
                    "fibre-channel-packets-received": "0",
                    "fibre-channel-packets-transmitted": "0",
                    "fip-packets-dropped": "0",
                    "fip-packets-received": "0",
                    "fip-packets-transmitted": "0",
                    "igmpl2-packets-received": "0",
                    "igmpl2-packets-transmitted": "0",
                    "input-drops-due-to-bogus-protocol": "0",
                    "input-drops-due-to-no-mbufs-available": "0",
                    "input-drops-due-to-no-socket": "0",
                    "input-drops-due-to-no-space-in-socket": "0",
                    "isdn-packets-received": "0",
                    "isdn-packets-transmitted": "0",
                    "lacp-packets-dropped": "0",
                    "lacp-packets-received": "0",
                    "lacp-packets-transmitted": "0",
                    "mldl2-packets-received": "0",
                    "mldl2-packets-transmitted": "0",
                    "mpu-packets-received": "0",
                    "mpu-packets-transmitted": "0",
                    "output-drops-due-to-transmit-error": "0",
                    "ppoe-packets-transmitted": "0",
                    "ppp-packets-received-from-jppd": "0",
                    "ppp-packets-received-from-pppd": "0",
                    "ppp-packets-transmitted-to-jppd": "0",
                    "ppp-packets-transmitted-to-pppd": "0",
                    "pppoe-packets-received": "0",
                    "raw-packets-transmitted": "0",
                    "stp-packets-dropped": "0",
                    "stp-packets-received": "0",
                    "stp-packets-transmitted": "0",
                    "vccp-packets-dropped": "0",
                    "vccp-packets-received": "0",
                    "vccp-packets-transmitted": "0",
                },
                "rdp": {
                    "acks-received": "0",
                    "acks-sent": "0",
                    "closes": "0",
                    "connects": "0",
                    "input-packets": "0",
                    "keepalives-received": "0",
                    "keepalives-sent": "0",
                    "output-packets": "0",
                    "packets-discarded-due-to-bad-sequence-number": "0",
                    "packets-discarded-for-bad-checksum": "0",
                    "packets-dropped-due-to-full-socket-buffers": "0",
                    "packets-dropped-full-repl-sock-buf": "0",
                    "refused-connections": "0",
                    "retransmits": "0",
                },
                "tcp": {
                    "aborted": "0",
                    "ack-header-predictions": "7954887",
                    "acks-bytes": "50912129",
                    "acks-sent-in-response-but-not-exact-rsts": "0",
                    "acks-sent-in-response-to-syns-on-established-connections":
                    "0",
                    "attempts": "48561265",
                    "bad-connection-attempts": "445",
                    "badack": "0",
                    "bucket-overflow": "0",
                    "byte-retransmits": "72",
                    "bytes": "589372",
                    "cache-overflow": "0",
                    "completed": "1258",
                    "connection-accepts": "1258",
                    "connection-requests": "12181850",
                    "connections-closed": "12185111",
                    "connections-dropped-by-persist-timeout": "0",
                    "connections-dropped-by-retransmit-timeout": "162",
                    "connections-established": "1921",
                    "connections-updated-rtt-on-close": "1295",
                    "connections-updated-ssthresh-on-close": "360",
                    "connections-updated-variance-on-close": "1295",
                    "cookies-received": "0",
                    "cookies-sent": "0",
                    "data-packet-header-predictions": "50195470",
                    "data-packets-bytes": "49634888",
                    "dropped": "22",
                    "drops": "438",
                    "duplicate-in-bytes": "724472",
                    "dupsyn": "66",
                    "embryonic-connections-dropped": "12177708",
                    "icmp-packets-ignored": "1",
                    "in-sequence-bytes": "285528163",
                    "keepalive-connections-dropped": "981871",
                    "keepalive-probes-sent": "206620576",
                    "keepalive-timeouts": "207602447",
                    "listen-queue-overflows": "0",
                    "out-of-order-in-bytes": "58516475",
                    "out-of-sequence-segment-drops": "0",
                    "outgoing-segments-dropped": "0",
                    "packets-received": "568914028",
                    "packets-received-after-close": "300",
                    "packets-received-in-sequence": "66028460",
                    "packets-sent": "265063785",
                    "persist-timeouts": "20",
                    "rcv-packets-dropped": "0",
                    "rcv-packets-dropped-due-to-bad-address": "0",
                    "received-acks": "40875092",
                    "received-acks-for-unsent-data": "0",
                    "received-completely-duplicate-packet": "133612660",
                    "received-discarded-because-packet-too-short": "0",
                    "received-discarded-for-bad-checksum": "1054",
                    "received-discarded-for-bad-header-offset": "0",
                    "received-duplicate-acks": "286370388",
                    "received-old-duplicate-packets": "0",
                    "received-out-of-order-packets": "124832",
                    "received-packets-of-data-after-window": "1207",
                    "received-packets-with-some-dupliacte-data": "463",
                    "received-window-probes": "13",
                    "received-window-update-packets": "2896764",
                    "reset": "10",
                    "retransmit-timeouts": "7925644",
                    "retransmitted": "193",
                    "retransmitted-bytes": "49356338",
                    "rst-packets": "179222038",
                    "sack-opitions-sent": "112",
                    "sack-options-received": "4488",
                    "sack-recovery-episodes": "820",
                    "sack-scoreboard-overflow": "0",
                    "segment-retransmits": "7",
                    "segments-updated-rtt": "38162864",
                    "send-packets-dropped": "0",
                    "sent-ack-only-packets": "196250492",
                    "sent-control-packets": "191405194",
                    "sent-data-packets": "52538606",
                    "sent-data-packets-retransmitted": "106366",
                    "sent-packets-delayed": "48858785",
                    "sent-resends-by-mtu-discovery": "0",
                    "sent-urg-only-packets": "0",
                    "sent-window-probe-packets": "0",
                    "sent-window-update-packets": "3986235",
                    "some-duplicate-in-bytes": "79013",
                    "stale": "15",
                    "syncache-entries-added": "1283",
                    "unreach": "0",
                    "zone-failures": "0",
                },
                "tnp": {
                    "broadcast-packets-received": "18139196",
                    "broadcast-packets-sent": "18140767",
                    "control-packets-received": "0",
                    "control-packets-sent": "0",
                    "fragment-reassembly-queue-flushes": "0",
                    "fragmented-packets-received": "0",
                    "fragmented-packets-sent": "0",
                    "hello-packets-received": "18139196",
                    "hello-packets-sent": "18140767",
                    "input-packets-discarded-with-no-protocol": "0",
                    "packets-of-version-unspecified-received": "0",
                    "packets-of-version-unspecified-sent": "0",
                    "packets-of-version1-received": "0",
                    "packets-of-version1-sent": "0",
                    "packets-of-version2-received": "0",
                    "packets-of-version2-sent": "0",
                    "packets-of-version3-received": "18139196",
                    "packets-of-version3-sent": "18140767",
                    "packets-sent-with-unknown-protocol": "0",
                    "packets-with-tnp-src-address-collision-received": "0",
                    "rdp-packets-received": "0",
                    "rdp-packets-sent": "0",
                    "received-fragments-dropped": "0",
                    "received-hello-packets-dropped": "0",
                    "sent-fragments-dropped": "0",
                    "sent-hello-packets-dropped": "0",
                    "tunnel-packets-received": "0",
                    "tunnel-packets-sent": "0",
                    "udp-packets-received": "0",
                    "udp-packets-sent": "0",
                    "unicast-packets-received": "0",
                    "unicast-packets-sent": "0",
                },
                "ttp": {
                    "arp-l3-packets-received": "0",
                    "clnp-l3-packets-received": "0",
                    "cyclotron-cycle-l3-packets-received": "0",
                    "cyclotron-send-l3-packets-received": "0",
                    "input-packets-could-not-get-buffer": "0",
                    "input-packets-for-which-route-lookup-is-bypassed": "0",
                    "input-packets-tlv-dropped": "0",
                    "input-packets-with-bad-af": "0",
                    "input-packets-with-bad-tlv-header": "0",
                    "input-packets-with-bad-tlv-type": "0",
                    "input-packets-with-bad-type": "0",
                    "input-packets-with-discard-type": "0",
                    "input-packets-with-too-many-tlvs": "0",
                    "input-packets-with-ttp-tlv-p2mp-nbr-nhid-type": "0",
                    "input-packets-with-unknown-p2mp-nbr-nhid": "0",
                    "input-packets-with-vxlan-bfd-pkts": "0",
                    "ipv4-l3-packets-received": "83525851",
                    "ipv4-to-mpls-l3-packets-received": "4214",
                    "ipv6-l3-packets-received": "100720250",
                    "l2-packets-received": "56842",
                    "l3-packets-dropped": "0",
                    "l3-packets-sent-could-not-get-buffer": "0",
                    "mpls-l3-packets-received": "0",
                    "mpls-to-ipv4-l3-packets-received": "0",
                    "null-l3-packets-received": "0",
                    "openflow-packets-received": "0",
                    "packets-received-from-unknown-ifl": "0",
                    "packets-received-while-unconnected": "0",
                    "packets-sent-could-not-find-neighbor": "0",
                    "packets-sent-could-not-get-buffer": "0",
                    "packets-sent-when-host_unreachable": "0",
                    "packets-sent-when-transmit-disabled": "0",
                    "packets-sent-while-interface-down": "0",
                    "packets-sent-while-unconnected": "0",
                    "packets-sent-with-bad-af": "0",
                    "packets-sent-with-bad-ifl": "0",
                    "tnp-l3-packets-received": "0",
                    "ttp-packets-sent": "185307601",
                    "unknown-l3-packets-received": "0",
                    "vpls-l3-packets-received": "0",
                },
                "tudp": {
                    "broadcast-or-multicast-datagrams-dropped-due-to-no-socket":
                    "0",
                    "datagrams-dropped-due-to-full-socket-buffers": "0",
                    "datagrams-dropped-due-to-no-socket": "0",
                    "datagrams-output": "1",
                    "datagrams-received": "0",
                    "datagrams-with-bad-checksum": "0",
                    "datagrams-with-bad-data-length-field": "0",
                    "datagrams-with-incomplete-header": "0",
                    "delivered": "0",
                },
                "udp": {
                    "broadcast-or-multicast-datagrams-dropped-due-to-no-socket":
                    "0",
                    "datagrams-delivered": "86615318",
                    "datagrams-dropped-due-to-full-socket-buffers": "26",
                    "datagrams-dropped-due-to-no-socket": "13553",
                    "datagrams-not-for-hashed-pcb": "0",
                    "datagrams-output": "98245187",
                    "datagrams-received": "86628897",
                    "datagrams-with-bad-checksum": "0",
                    "datagrams-with-bad-datalength-field": "0",
                    "datagrams-with-incomplete-header": "0",
                },
            },
            {
                "bridge": {
                    "aging-acks-from-pfe": "0",
                    "aging-non-acks-from-pfe": "0",
                    "aging-requests-over-max-rate": "0",
                    "aging-requests-timed-out-waiting-on-fes": "0",
                    "bogus-address-in-aging-requests": "0",
                    "errors-finding-peer-fes": "0",
                    "learning-requests-over-capacity": "0",
                    "learning-requests-while-learning-disabled-on-interface":
                    "0",
                    "mac-route-aging-requests": "0",
                    "mac-route-learning-requests": "0",
                    "mac-routes-aged": "0",
                    "mac-routes-learned": "0",
                    "mac-routes-moved": "0",
                    "packets-dropped-due-to-no-l3-route-table": "0",
                    "packets-dropped-due-to-no-local-ifl": "0",
                    "packets-dropped-due-to-no-socket": "0",
                    "packets-for-this-host": "0",
                    "packets-punted": "0",
                    "packets-received": "0",
                    "packets-with-incorrect-version-number": "0",
                    "packets-with-no-auxiliary-table": "0",
                    "packets-with-no-ce-facing-entry": "0",
                    "packets-with-no-core-facing-entry": "0",
                    "packets-with-no-family": "0",
                    "packets-with-no-logical-interface": "0",
                    "packets-with-no-route-table": "0",
                    "packets-with-size-smaller-than-minimum": "0",
                    "requests-involving-multiple-peer-fes": "0",
                    "requests-to-age-static-route": "0",
                    "requests-to-learn-an-existing-route": "0",
                    "requests-to-move-static-route": "0",
                    "requests-to-re-ageout-aged-route": "0",
                    "unsupported-platform": "0",
                },
                "vpls": {
                    "aging-acks-from-pfe": "0",
                    "aging-non-acks-from-pfe": "0",
                    "aging-requests-over-max-rate": "0",
                    "aging-requests-timed-out-waiting-on-fes": "0",
                    "bogus-address-in-aging-requests": "0",
                    "errors-finding-peer-fes": "0",
                    "learning-requests-over-capacity": "0",
                    "learning-requests-while-learning-disabled-on-interface":
                    "0",
                    "mac-route-aging-requests": "0",
                    "mac-route-learning-requests": "0",
                    "mac-routes-aged": "0",
                    "mac-routes-learned": "0",
                    "mac-routes-moved": "0",
                    "packets-dropped-due-to-no-l3-route-table": "0",
                    "packets-dropped-due-to-no-local-ifl": "0",
                    "packets-dropped-due-to-no-socket": "0",
                    "packets-for-this-host": "0",
                    "packets-punted": "0",
                    "packets-received": "0",
                    "packets-with-incorrect-version-number": "0",
                    "packets-with-no-auxiliary-table": "0",
                    "packets-with-no-ce-facing-entry": "0",
                    "packets-with-no-core-facing-entry": "0",
                    "packets-with-no-family": "0",
                    "packets-with-no-logical-interface": "0",
                    "packets-with-no-route-table": "0",
                    "packets-with-size-smaller-than-minimum": "0",
                    "requests-involving-multiple-peer-fes": "0",
                    "requests-to-age-static-route": "0",
                    "requests-to-learn-an-existing-route": "0",
                    "requests-to-move-static-route": "0",
                    "requests-to-re-ageout-aged-route": "0",
                    "unsupported-platform": "0",
                },
            },
        ]
    }

    golden_output_1 = {
        "execute.return_value":
        """
            show system statistics
            Tcp:
                    265063785 packets sent
                            52538606 data packets (49634888 bytes)
                            106366 data packets retransmitted (49356338 bytes)
                            0 resends initiated by MTU discovery
                            196250492 ack only packets (48858785 packets delayed)
                            0 URG only packets
                            0 window probe packets
                            3986235 window update packets
                            191405194 control packets
                    568914028 packets received
                            40875092 acks(for 50912129 bytes)
                            286370388 duplicate acks
                            0 acks for unsent data
                            66028460  packets received in-sequence(285528163 bytes)
                            133612660 completely duplicate packets(724472 bytes)
                            0 old duplicate packets
                            463 packets with some duplicate data(79013 bytes duped)
                            124832 out-of-order packets(58516475 bytes)
                            1207 packets of data after window(589372 bytes)
                            13 window probes
                            2896764 window update packets
                            300 packets received after close
                            1054 discarded for bad checksums
                            0 discarded for bad header offset fields
                            0 discarded because packet too short
                    12181850 connection requests
                    1258 connection accepts
                    445 bad connection attempts
                    0 listen queue overflows
                    1921 connections established (including accepts)
                    12185111 connections closed (including 438 drops)
                            1295 connections updated cached RTT on close
                            1295 connections updated cached RTT variance on close
                            360 connections updated cached ssthresh on close
                    12177708 embryonic connections dropped
                    38162864 segments updated rtt(of 48561265 attempts)
                    7925644 retransmit timeouts
                            162 connections dropped by retransmit timeout
                    20 persist timeouts
                            0 connections dropped by persist timeout
                    207602447 keepalive timeouts
                            206620576 keepalive probes sent
                            981871 connections dropped by keepalive
                    7954887 correct ACK header predictions
                    50195470 correct data packet header predictions
                    1283 syncache entries added
                            193 retransmitted
                            66 dupsyn
                            22 dropped
                            1258 completed
                            0 bucket overflow
                            0 cache overflow
                            10 reset
                            15 stale
                            0 aborted
                            0 badack
                            0 unreach
                            0 zone failures
                    0 cookies sent
                    0 cookies received
                    820 SACK recovery episodes
                    7 segment retransmits in SACK recovery episodes
                    72 byte retransmits in SACK recovery episodes
                    4488 SACK options (SACK blocks) received
                    112 SACK options (SACK blocks) sent
                    0 SACK scoreboard overflow
                    0 ACKs sent in response to in-window but not exact RSTs
                    0 ACKs sent in response to in-window SYNs on established connections
                    0 rcv packets dropped by TCP due to bad address
                    0 out-of-sequence segment drops due to insufficient memory
                    179222038 RST packets
                    1 ICMP packets ignored by TCP
                    0 send packets dropped by TCP due to auth errors
                    0 rcv packets dropped by TCP due to auth errors
                    0 outgoing segments dropped due to policing
            udp:
                    86628897 datagrams received
                    0 with incomplete header
                    0 with bad data length field
                    0 with bad checksum
                    13553 dropped due to no socket
                    0 broadcast/multicast datagrams dropped due to no socket
                    26 dropped due to full socket buffers
                    0 not for hashed pcb
                    86615318 delivered
                    98245187 datagrams output
            ip:
                    791039285 total packets received
                    0 bad header checksums
                    0 with size smaller than minimum
                    0 with data size < data length
                    0 with header length < data size
                    0 with data length < header length
                    0 with incorrect version number
                    0 packets destined to dead next hop
                    7776172 fragments received
                    0 fragments dropped (dup or out of space)
                    0 fragment sessions dropped (queue overflow)
                    2330 fragments dropped after timeout
                    3840557 packets reassembled ok
                    820964812 packets for this host
                    311 packets for unknown/unsupported protocol
                    0 packets forwarded
                    0 packets not forwardable
                    0 redirects sent
                    894567482 packets sent from this host
                    10684334 packets sent with fabricated ip header
                    0 output packets dropped due to no bufs
                    221 output packets discarded due to no route
                    189762 output datagrams fragmented
                    458290 fragments created
                    0 datagrams that can't be fragmented
                    0 packets with bad options
                    310 packets with options handled without error
                    0 strict source and record route options
                    0 loose source and record route options
                    0 record route options
                    0 timestamp options
                    0 timestamp and address options
                    0 timestamp and prespecified address options
                    0 option packets dropped due to rate limit
                    310 router alert options
                    0 multicast packets dropped (no iflist)
                    0 packets dropped (src and int don't match)
                    0 transit re packets dropped on mgmt i/f
                    0 packets used first nexthop in ecmp unilist
                    184307157 incoming ttpoip packets received
                    0 incoming ttpoip packets dropped
                    185307601 outgoing TTPoIP packets sent
                    0 outgoing TTPoIP packets dropped
                    46 raw packets dropped. no space in socket recv buffer
                    0 packets consumed by virtual-node processing
            icmp:
                    0 drops due to rate limit
                    17647 calls to icmp_error
                    115 errors not generated because old message was icmp
                    Output Histogram
                            18108704 echo reply
                            13553 destination unreachable
                            15 echo
                            4094 time exceeded
                    0 messages with bad code fields
                    0 messages less than the minimum length
                    0 messages with bad checksum
                    0 messages with bad source address
                    0 messages with bad length
                    0 echo drops with broadcast or multicast destinaton address
                    0 timestamp drops with broadcast or multicast destination address
                    Input Histogram
                            15 echo reply
                            7376316 destination unreachable
                            18108704 echo
                            11308300 time exceeded
                    18108704 message responses generated
            igmp:
                    310 messages received
                    0 messages received with too few bytes
                    0 messages received with bad checksum
                    308 membership queries received
                    0 membership queries received with invalid fields
                    0 membership reports received
                    0 membership reports received with invalid fields
                    0 membership reports received for groups to which we belong
                    943 Membership reports sent
            ipsec:
                    0 inbound packets violated process security policy
                    0 Outbound packets violated process security policy
                    0 outbound packets with no SA available
                    0 outbound packets failed due to insufficient memory
                    0 outbound packets with no route
                    0 invalid outbound packets
                    0 Outbound packets with bundles SAs
                    0 mbuf coleasced during clone
                    0 Cluster coalesced during clone
                    0 Cluster copied during clone
                    0 mbuf inserted during makespace
            ah:
                    0 packets shorter than header shows
                    0 packets dropped protocol unsupported
                    0 packets dropped no TDB
                    0 packets dropped bad KCR
                    0 packets dropped queue full
                    0 packets dropped no transform
                    0 replay counter wrap
                    0 packets dropped bad authentication detected
                    0 packets dropped bad authentication length
                    0 possible replay packets detected
                    0 packets in
                    0 packets out
                    0 packets dropped invalid TDB
                    0 bytes in
                    0 bytes out
                    0 packets dropped larger than maxpacket
                    0 packets blocked due to policy
                    0 crypto processing failure
                    0 tunnel sanity check failures
            esp:
                    0 packets shorter than header shows
                    0 packets dropped protocol not supported
                    0 packets dropped no TDB
                    0 packets dropped bad KCR
                    0 packets dropped queue full
                    0 packets dropped no transform
                    0 packets dropped bad ilen
                    0 replay counter wrap
                    0 packets dropped bad encryption detected
                    0 packets dropped bad authentication detected
                    0 possible replay packets detected
                    0 packets in
                    0 packets out
                    0 packets dropped invalid TDB
                    0 bytes in
                    0 bytes out
                    0 packets dropped larger than maxpacket
                    0 packets blocked due to policy
                    0 crypto processing failure
                    0 tunnel sanity check failures
            ipcomp:
                    0 packets shorter than header shows
                    0 packets dropped protocol not supported
                    0 packets dropped no TDB
                    0 packets dropped bad KCR
                    0 packets dropped queue full
                    0 packets dropped no transform
                    0 replay counter wrap
                    0 packets in
                    0 packets out
                    0 packets dropped invalid TDB
                    0 bytes in
                    0 bytes out
                    0 packets dropped larger than maxpacket
                    0 packets blocked due to policy
                    0 crypto processing failure
                    0 packets sent uncompressed threshold
                    0 packets sent uncompressed useless
            raw_if:
                    0 RAW packets transmitted
                    0 PPPOE packets transmitted
                    0 ISDN packets transmitted
                    0 DIALER packets transmitted
                    0 PPP packets transmitted to pppd
                    0 PPP packets transmitted to jppd
                    0 IGMPL2 packets transmitted
                    0 MLDL2 packets transmitted
                    0 Fibre Channel packets transmitted
                    0 FIP packets transmitted
                    0 STP packets transmitted
                    0 LACP packets transmitted
                    0 VCCP packets transmitted
                    0 Fabric OAM packets transmitted
                    0 output drops due to tx error
                    0 MPU packets transmitted
                    0 PPPOE packets received
                    0 ISDN packets received
                    0 DIALER packets received
                    0 PPP packets received from pppd
                    0 MPU packets received
                    0 PPP packets received from jppd
                    0 IGMPL2 packets received
                    0 MLDL2 packets received
                    0 Fibre Channel packets received
                    0 FIP packets received
                    0 STP packets received
                    0 LACP packets received
                    0 VCCP packets received
                    0 Fabric OAM packets received
                    0 Fibre Channel packets dropped
                    0 FIP packets dropped
                    0 STP packets dropped
                    0 LACP packets dropped
                    0 Fabric OAM packets dropped
                    0 VCCP packets dropped
                    0 Input drops due to bogus protocol
                    0 input drops due to no mbufs available
                    0 input drops due to no space in socket
                    0 input drops due to no socket
            arp:
                    200794 datagrams received
                    39895 ARP requests received
                    54355 ARP replies received
                    109 resolution request received
                    0 resolution request dropped
                    0 unrestricted proxy requests
                    0 restricted proxy requests
                    0 received proxy requests
                    0 unrestricted proxy requests not proxied
                    0 restricted proxy requests not proxied
                    0 datagrams with bogus interface
                    0 datagrams with incorrect length
                    0 datagrams for non-IP protocol
                    0 datagrams with unsupported op code
                    0 datagrams with bad protocol address length
                    0 datagrams with bad hardware address length
                    0 datagrams with multicast source address
                    87 datagrams with multicast target address
                    0 datagrams with my own hardware address
                    0 datagrams for an address not on the interface
                    0 datagrams with a broadcast source address
                    0 datagrams with source address duplicate to mine
                    106457 datagrams which were not for me
                    7 packets discarded waiting for resolution
                    15 packets sent after waiting for resolution
                    55086 ARP requests sent
                    39895 ARP replies sent
                    0 requests for memory denied
                    0 requests dropped on entry
                    0 requests dropped during retry
                    0 requests dropped due to interface deletion
                    0 requests on unnumbered interfaces
                    0 new requests on unnumbered interfaces
                    0 replies for from unnumbered interfaces
                    0 requests on unnumbered interface with non-subnetted donor
                    0 replies from unnumbered interface with non-subnetted donor
                    0 arp packets rejected as family is configured with deny arp
                    0 arp response packets are rejected on mace icl interface
                    0 arp replies are rejected as source and destination is same
                    0 arp probe for proxy address reachable from the incoming interface
                    0 arp request discarded for vrrp source address
                    0 self arp request packet received on irb interface
                    0 proxy arp request discarded as source ip is a proxy target
                    0 arp packets are dropped as nexthop allocation failed
                    0 arp packets received from peer vrrp rotuer and discarded
                    0 arp packets are rejected as target ip arp resolve is in progress
                    0 grat arp packets are ignored as mac address is not changed
                    0 arp packets are dropped from peer vrrp
                    0 arp packets are dropped as driver call failed
                    0 arp packets are dropped as source is not validated
                    75000 Max System ARP nh cache limit
                    59840 Max Public ARP nh cache limit
                    200 Max IRI ARP nh cache limit
                    14960 Max Management intf ARP nh cache limit
                    4 Current Public ARP nexthops present
                    1 Current IRI ARP nexthops present
                    2 Current Management ARP nexthops present
                    0 Total ARP nexthops creation failed as limit reached
                    0 Public ARP nexthops creation failed as public limit reached
                    0 IRI ARP nexthops creation failed as iri limit reached
                    0 Management ARP nexthops creation failed as mgt limit reached
            ip6:
                    100720281 total packets received
                    0 packets with size smaller than minimum
                    0 packets with data size < data length
                    0 packets with bad options
                    0 packets with incorrect version number
                    0 fragments received
                    0 fragments dropped (dup or out of space)
                    0 fragments dropped after timeout
                    0 fragment sessions dropped (queue overflow)
                    0 packets reassembled ok
                    100720272 packets for this host
                    0 packets forwarded
                    0 packets not forwardable
                    0 redirects sent
                    101649920 packets sent from this host
                    4506372 packets sent with fabricated ip header
                    0 output packets dropped due to no bufs, etc.
                    1026 output packets discarded due to no route
                    0 output datagrams fragmented
                    0 fragments created
                    0 datagrams that can't be fragmented
                    0 packets that violated scope rules
                    0 multicast packets which we don't join
                            Input histogram:
                            5981247 TCP
                            82375306 UDP
                            7862032 ICMP6
                            4501665 OSPF
                            0 packets whose headers are not continuous
                            0 tunneling packets that can't find gif
                            0 packets discarded due to too may headers
                            0 failures of source address selection
                    source addresses on an outgoing I/F
                            1088799 link-locals
                            557 globals
                    source addresses of same scope
                            1088799 link-locals
                            556 globals
                    source addresses of a different scope
                            1 globals
                            0 forward cache hit
                            0 forward cache miss
                            0 Packets destined to dead next hop
                            0 option packets dropped due to rate limit
                            0 Packets dropped (src and int don't match)
                            0 packets dropped due to bad protocol
                            0 transit re packet(null) dropped on mgmt i/f
            icmp6:
                    31 Calls to icmp_error
                    0 Errors not generated because old message was icmp error
                    0 Errors not generated because rate limitation
                    Output histogram:
                            31 unreach
                            544914 neighbor solicitation
                            544593 neighbor advertisement
                    0 Messages with bad code fields
                    0 Messages < minimum length
                    0 Bad checksums
                    0 Messages with bad length
                    Input histogram:
                            319 unreach
                            6773206 time exceeded
                            8 router solicitation
                            168 router advertisment
                            544587 neighbor solicitation
                            543766 neighbor advertisement
                    Histogram of error messages to be generated:
                            0 No route
                            0 Administratively prohibited
                            0 Beyond scope
                            31 Address unreachable
                            0 Port unreachable
                            0 Time exceed transit
                            0 Time exceed reassembly
                            0 Erroneous header field
                            0 Unrecognized next header
                            0 Unrecognized option
                            0 Unknown
                    0 Message responses generated
                    0 Messages with too many ND options
                    75000 Max System ND nh cache limit
                    59840 Max Public ND nh cache limit
                    200 Max IRI ND nh cache limit
                    14960 Max Management intf ND nh cache limit
                    3 Current Public ND nexthops present
                    1 Current IRI ND nexthops present
                    0 Current Management ND nexthops present
                    0 Total ND nexthops creation failed as limit reached
                    0 Public ND nexthops creation failed as public limit reached
                    0 IRI ND nexthops creation failed as iri limit reached
                    0 Management ND nexthops creation failed as mgt limit reached
                    0 interface-restricted ndp proxy requests
                    0 interface-restricted dad proxy requests
                    0 interface-restricted ndp proxy responses
                    0 interface-restricted dad proxy conflicts
                    0 interface-restricted dad proxy duplicates
                    0 interface-restricted ndp proxy resolve requests
                    0 interface-restricted dad proxy resolve requests
                    0 interface-restricted dad packets from same node dropped
                    543766 interface-restricted proxy packets dropped with nomac
                    0 ND hold nexthops dropped on entry by RED mark
                    0 ND hold nexthops dropped on timer expire by RED mark
            ipsec6:
                    0 Inbound packets violated process security policy
                    0 Outbound packets violated process security policy
                    0 Outbound packets with no SA available
                    0 Outbound packets failed due to insufficient memory
                    0 Outbound packets with no route
                    0 Invalid outbound packets
                    0 Outbound packets with bundles SAs
                    0 mbuf coleasced during clone
                    0 Cluster coalesced during clone
                    0 Cluster copied during clone
                    0 mbuf inserted during makespace
            pfkey:
                    1269 Requests sent from userland
                    69304 Bytes sent from userland
                    histogram by message type:
                            626 reserved
                            17 add
                            626 dump
            pfkey:
                    0 Messages with invalid length field
                    0 Messages with invalid version field
                    0 Messages with invalid message type field
                    0 Messages too short
                    0 Messages with memory allocation failure
                    0 Messages with duplicate extension
                    0 Messages with invalid extension type
                    0 Messages with invalid sa type
                    0 Messages with invalid address extension
                    11269 Requests sent to userland
                    3189032 Bytes sent to userland
                    histogram by message type:
                            626 reserved
                            17 add
                            10626 dump
            pfkey:
                    22500 Messages toward single socket
                    0 Messages toward all sockets
                    0 Messages toward registered sockets
                    0 Messages with memory allocation failure
            clnl:
                    0 Total packets received
                    0 Packets delivered
                    0 Too small packets
                    0 Packets with bad header length
                    0 Packets with bad checksum
                    0 Bad version packets
                    0 Unknown or unsupported protocol packets
                    0 Packets with bogus sdl size
                    0 No free memory in socket buffer
                    0 Send packets discarded
                    0 Sbappend failure
                    0 Mcopy failure
                    0 Address fields were not reasonable
                    0 Segment information forgotten
                    0 Forwarded packets
                    0 Total packets sent
                    0 Output packets discarded
                    0 Non-forwarded packets
                    0 Packets fragmented
                    0 Fragments sent
                    0 Fragments discarded
                    0 Fragments timed out
                    0 Fragmentation prohibited
                    0 Packets reconstructed
                    0 Packets destined to dead nexthop
                    0 Packets discarded due to no route
                    0 Error pdu rate drops
                    0 ER pdu generation failure
            esis:
                    0 Total pkts received
                    0 Total packets consumed by protocol
                    0 Pdus received with bad checksum
                    0 Pdus received with bad version number
                    0 Pdus received with bad type field
                    0 Short pdus received
                    0 Pdus withbogus sdl size
                    0 Pdus with bad header length
                    0 Pdus with unknown or unsupport protocol
                    0 No free memory in socket buffer
                    0 Send packets discarded
                    0 Sbappend failure
                    0 Mcopy failure
                    0 ISO family not configured
            tnp:
                    0 Unicast packets received
                    18139196 Broadcast packets received
                    0 Fragmented packets received
                    0 Hello packets dropped
                    0 Fragments dropped
                    0 Fragment reassembly queue flushes
                    0 Packets with tnp src address collision received
                    18139196 Hello packets received
                    0 Control packets received
                    0 Rdp packets received
                    0 Udp packets received
                    0 Tunnel packets received
                    0 Input packets discarded with no protocol
                    0 Packets of version unspecified received
                    0 Packets of version 1 received
                    0 Packets of version 2 received
                    18139196 Packets of version 3 received
                    0 Unicast packets sent
                    18140767 Broadcast packets sent
                    0 Fragmented packets sent
                    0 Hello packets dropped
                    0 Fragments dropped
                    18140767 Hello packets sent
                    0 Control packets sent
                    0 Rdp packets sent
                    0 Udp packets sent
                    0 Tunnel packets sent
                    0 Packets sent with unknown protocol
                    0 Packets of version unspecified sent
                    0 Packets of version 1 sent
                    0 Packets of version 2 sent
                    18140767 Packets of version 3 sent
            rdp:
                    0 Input packets
                    0 Packets discarded for bad checksum
                    0 Packets discarded due to bad sequence number
                    0 Refused connections
                    0 Acks received
                    0 Packets dropped due to full socket buffers
                    0 Retransmits
                    0 Output packets
                    0 Acks sent
                    0 Connects
                    0 Closes
                    0 Keepalives received
                    0 Keepalives sent
            tudp:
                    0 Datagrams received
                    0 Datagrams with incomplete header
                    0 Datagrams with bad data length field
                    0 Datagrams with bad checksum
                    0 Datagrams dropped due to no socket
                    0 Broadcast/multicast datagrams dropped due to no socket
                    0 Datagrams dropped due to full socket buffers
                    0 Delivered
                    1 Datagrams output
            ttp:
                    185307601 Packets sent
                    0 Packets sent while unconnected
                    0 Packets sent while interface down
                    0 Packets sent couldn't get buffer
                    0 Packets sent couldn't find neighbor
                    0 Packets sent when transmit is disable
                    0 Packets sent when host unreachable
                    0 L3 Packets sent could not get buffer
                    0 L3 Packets dropped
                    0 Packets sent with bad logical interface
                    0 Packets sent with bad address family
                    56842 L2 packets received
                    0 Unknown L3 packets received
                    83525851 IPv4 L3 packets received
                    0 MPLS L3 packets received
                    0 MPLS->IPV4 L3 packets received
                    4214 IPv4->MPLS L3 packets received
                    0 VPLS L3 packets received
                    100720250 IPv6 L3 packets received
                    0 ARP L3 packets received
                    0 CLNP L3 packets received
                    0 TNP L3 packets received
                    0 NULL L3 packets received
                    0 Cyclotron cycle L3 packets received
                    0 Cyclotron send L3 packets received
                    0 Openflow packets received
                    0 Packets received while unconnected
                    0 Packets received from unknown ifl
                    0 Input packets couldn't get buffer
                    0 Input packets with bad type
                    0 Input packets with discard type
                    0 Input packets with too many tlvs
                    0 Input packets with bad tlv header
                    0 Input packets with bad tlv type
                    0 Input packets dropped based on tlv result
                    0 Input packets with bad address family
                    0 Input packets for which rt lookup is bypassed
                    0 Input packets with ttp tlv of type TTP_TLV_P2MP_NBR_NHID
                    0 Input packets with unknown p2mp_nbr_nhid value
                    0 Input packets of type vxlan bfd
            mpls:
                    4214 Total MPLS packets received
                    6118 Packets forwarded
                    0 Packets dropped
                    0 Packets with header too small
                    0 After tagging, packets can't fit link MTU
                    0 Packets with IPv4 explicit NULL tag
                    0 Packets with IPv4 explicit NULL cksum errors
                    0 Packets with router alert tag
                    5 LSP ping packets (ttl-expired/router alert)
                    4209 Packets with ttl expired
                    0 Packets with tag encoding error
                    0 Packets discarded due to no route
                    0 Packets used first nexthop in ecmp unilist
                    0 Packets dropped due to ifl down
                    0 Packets dropped at mpls socket send op
                    0 Packets forwarded at mpls socket send op
                    0 Packets dropped, over p2mp composite nexthop
            ethoamlfm:
                    0 total received packets
                    0 input drops due to bad interface state
                    0 received packets forwarded
                    0 total transmitted packets
                    0 sent packets
                    0 output drops due to bad interface state
            ethoamcfm:
                    0 total received packets
                    0 input drops due to bad interface state
                    0 received packets forwarded
                    0 total transmitted packets
                    0 sent packets
                    0 output drops due to bad interface state
                    0 flood requests forwarded to PFE
                    0 flood requests dropped
            vpls:
                    0 Total packets received
                    0 Packets with size smaller than minimum
                    0 Packets with incorrect version number
                    0 Packets for this host
                    0 Packets with no logical interface
                    0 Packets with no family
                    0 Packets with no route table
                    0 Packets with no auxiliary table
                    0 Packets with no core-facing entry
                    0 packets with no CE-facing entry
                    0 MAC route learning requests
                    0 MAC routes learnt
                    0 Requests to learn an existing route
                    0 Learning requests while learning disabled on interface
                    0 Learning requests over capacity
                    0 MAC routes moved
                    0 Requests to move static route
                    0 MAC route aging requests
                    0 MAC routes aged
                    0 Bogus address in aging requests
                    0 Requests to age static route
                    0 Requests to re-ageout aged route
                    0 Requests involving multiple peer FEs
                    0 Aging acks from PFE
                    0 Aging non-acks from PFE
                    0 Aging requests timed out waiting on FEs
                    0 Aging requests over max-rate
                    0 Errors finding peer FEs
                    0 Unsupported platform
                    0 Packets dropped due to no l3 route table
                    0 Packets dropped due to no local ifl
                    0 Packets punted
                    0 Packets dropped due to no socket
            bridge:
                    0 Total packets received
                    0 Packets with size smaller than minimum
                    0 Packets with incorrect version number
                    0 Packets for this host
                    0 Packets with no logical interface
                    0 Packets with no family
                    0 Packets with no route table
                    0 Packets with no auxiliary table
                    0 Packets with no core-facing entry
                    0 packets with no CE-facing entry
                    0 MAC route learning requests
                    0 MAC routes learnt
                    0 Requests to learn an existing route
                    0 Learning requests while learning disabled on interface
                    0 Learning requests over capacity
                    0 MAC routes moved
                    0 Requests to move static route
                    0 MAC route aging requests
                    0 MAC routes aged
                    0 Bogus address in aging requests
                    0 Requests to age static route
                    0 Requests to re-ageout aged route
                    0 Requests involving multiple peer FEs
                    0 Aging acks from PFE
                    0 Aging non-acks from PFE
                    0 Aging requests timed out waiting on FEs
                    0 Aging requests over max-rate
                    0 Errors finding peer FEs
                    0 Unsupported platform
                    0 Packets dropped due to no l3 route table
                    0 Packets dropped due to no local ifl
                    0 Packets punted
                    0 Packets dropped due to no socket

    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# =========================================================
# Unit test for show system statistics no-forwarding
# =========================================================
class TestShowSystemStatisticsNoForwarding(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "statistics": [
            {
                "ah": {
                    "bytes-in": "0",
                    "bytes-out": "0",
                    "crypto-processing-failure": "0",
                    "packets-blocked-due-to-policy": "0",
                    "packets-dropped-as-bad-authentication-detected": "0",
                    "packets-dropped-as-larger-than-ip-maxpacket": "0",
                    "packets-dropped-as-protocol-unsupported": "0",
                    "packets-dropped-due-to-bad-authentication-length": "0",
                    "packets-dropped-due-to-bad-kcr": "0",
                    "packets-dropped-due-to-invalid-tdb": "0",
                    "packets-dropped-due-to-no-tdb": "0",
                    "packets-dropped-due-to-no-transform": "0",
                    "packets-dropped-due-to-queue-full": "0",
                    "packets-in": "0",
                    "packets-out": "0",
                    "packets-shorter-than-header-shows": "0",
                    "possible-replay-packets-detected": "0",
                    "replay-counter-wrap": "0",
                    "tunnel-sanity-check-failures": "0",
                },
                "arp": {
                    "arp-iri-cnt":
                    "1",
                    "arp-iri-drop":
                    "0",
                    "arp-iri-max":
                    "200",
                    "arp-mgt-cnt":
                    "2",
                    "arp-mgt-drop":
                    "0",
                    "arp-mgt-max":
                    "14960",
                    "arp-packets-are-dropped-as-driver-call-failed":
                    "0",
                    "arp-packets-are-dropped-as-nexthop-allocation-failed":
                    "0",
                    "arp-packets-are-dropped-as-source-is-not-validated":
                    "0",
                    "arp-packets-are-dropped-from-peer-vrrp":
                    "0",
                    "arp-packets-are-rejected-as-target-ip-arp-resolve-is-in-progress":
                    "0",
                    "arp-packets-received-from-peer-vrrp-router-and-discarded":
                    "0",
                    "arp-packets-rejected-as-family-is-configured-with-deny-arp":
                    "0",
                    "arp-probe-for-proxy-address-reachable-from-the-incoming-interface":
                    "0",
                    "arp-public-cnt":
                    "4",
                    "arp-public-drop":
                    "0",
                    "arp-public-max":
                    "59840",
                    "arp-replies-are-rejected-as-source-and-destination-is-same":
                    "0",
                    "arp-replies-received":
                    "54355",
                    "arp-replies-sent":
                    "39895",
                    "arp-request-discarded-for-vrrp-source-address":
                    "0",
                    "arp-requests-received":
                    "39895",
                    "arp-requests-sent":
                    "55086",
                    "arp-response-packets-are-rejected-on-mace-icl-interface":
                    "0",
                    "arp-system-drop":
                    "0",
                    "arp-system-max":
                    "75000",
                    "datagrams-for-an-address-not-on-the-interface":
                    "0",
                    "datagrams-for-non-ip-protocol":
                    "0",
                    "datagrams-received":
                    "200794",
                    "datagrams-which-were-not-for-me":
                    "106457",
                    "datagrams-with-a-broadcast-source-address":
                    "0",
                    "datagrams-with-bad-hardware-address-length":
                    "0",
                    "datagrams-with-bad-protocol-address-length":
                    "0",
                    "datagrams-with-bogus-interface":
                    "0",
                    "datagrams-with-incorrect-length":
                    "0",
                    "datagrams-with-multicast-source-address":
                    "0",
                    "datagrams-with-multicast-target-address":
                    "87",
                    "datagrams-with-my-own-hardware-address":
                    "0",
                    "datagrams-with-source-address-duplicate-to-mine":
                    "0",
                    "datagrams-with-unsupported-opcode":
                    "0",
                    "grat-arp-packets-are-ignored-as-mac-address-is-not-changed":
                    "0",
                    "new-requests-on-unnumbered-interfaces":
                    "0",
                    "packets-discarded-waiting-for-resolution":
                    "7",
                    "packets-sent-after-waiting-for-resolution":
                    "15",
                    "proxy-arp-request-discarded-as-source-ip-is-a-proxy-target":
                    "0",
                    "proxy-requests-not-proxied":
                    "0",
                    "received-proxy-requests":
                    "0",
                    "replies-from-unnumbered-interface-with-non-subnetted-donor":
                    "0",
                    "replies-from-unnumbered-interfaces":
                    "0",
                    "requests-dropped-due-to-interface-deletion":
                    "0",
                    "requests-dropped-during-retry":
                    "0",
                    "requests-dropped-on-entry":
                    "0",
                    "requests-for-memory-denied":
                    "0",
                    "requests-on-unnumbered-interface-with-non-subnetted-donor":
                    "0",
                    "requests-on-unnumbered-interfaces":
                    "0",
                    "resolution-request-dropped":
                    "0",
                    "resolution-request-received":
                    "109",
                    "restricted-proxy-requests":
                    "0",
                    "restricted-proxy-requests-not-proxied":
                    "0",
                    "self-arp-request-packet-received-on-irb-interface":
                    "0",
                    "unrestricted-proxy-requests":
                    "0",
                },
                "clnl": {
                    "address-fields-were-not-reasonable": "0",
                    "bad-version-packets": "0",
                    "er-pdu-generation-failure": "0",
                    "error-pdu-rate-drops": "0",
                    "forwarded-packets": "0",
                    "fragmentation-prohibited": "0",
                    "fragments-discarded": "0",
                    "fragments-sent": "0",
                    "fragments-timed-out": "0",
                    "mcopy-failure": "0",
                    "no-free-memory-in-socket-buffer": "0",
                    "non-forwarded-packets": "0",
                    "output-packets-discarded": "0",
                    "packets-delivered": "0",
                    "packets-destined-to-dead-nexthop": "0",
                    "packets-discarded-due-to-no-route": "0",
                    "packets-fragmented": "0",
                    "packets-reconstructed": "0",
                    "packets-with-bad-checksum": "0",
                    "packets-with-bad-header-length": "0",
                    "packets-with-bogus-sdl-size": "0",
                    "sbappend-failure": "0",
                    "segment-information-forgotten": "0",
                    "send-packets-discarded": "0",
                    "too-small-packets": "0",
                    "total-clnl-packets-received": "0",
                    "total-packets-sent": "0",
                    "unknown-or-unsupported-protocol-packets": "0",
                },
                "esis": {
                    "iso-family-not-configured": "0",
                    "mcopy-failure": "0",
                    "no-free-memory-in-socket-buffer": "0",
                    "pdus-received-with-bad-checksum": "0",
                    "pdus-received-with-bad-type-field": "0",
                    "pdus-received-with-bad-version-number": "0",
                    "pdus-with-bad-header-length": "0",
                    "pdus-with-bogus-sdl-size": "0",
                    "pdus-with-unknown-or-unsupport-protocol": "0",
                    "sbappend-failure": "0",
                    "send-packets-discarded": "0",
                    "short-pdus-received": "0",
                    "total-esis-packets-received": "0",
                    "total-packets-consumed-by-protocol": "0",
                },
                "esp": {
                    "esp-bytes-in": "0",
                    "esp-bytes-out": "0",
                    "esp-crypto-processing-failure": "0",
                    "esp-packets-blocked-due-to-policy": "0",
                    "esp-packets-dropped-as-bad-authentication-detected": "0",
                    "esp-packets-dropped-as-bad-encryption-detected": "0",
                    "esp-packets-dropped-as-bad-ilen": "0",
                    "esp-packets-dropped-as-invalid-tdb": "0",
                    "esp-packets-dropped-as-larger-than-ip-maxpacket": "0",
                    "esp-packets-dropped-as-protocol-not-supported": "0",
                    "esp-packets-dropped-due-to-bad-kcr": "0",
                    "esp-packets-dropped-due-to-no-tdb": "0",
                    "esp-packets-dropped-due-to-no-transform": "0",
                    "esp-packets-dropped-due-to-queue-full": "0",
                    "esp-packets-in": "0",
                    "esp-packets-out": "0",
                    "esp-packets-shorter-than-header-shows": "0",
                    "esp-possible-replay-packets-detected": "0",
                    "esp-replay-counter-wrap": "0",
                    "esp-tunnel-sanity-check-failures": "0",
                },
                "ethoamcfm": {
                    "flood-requests-dropped": "0",
                    "flood-requests-forwarded-to-pfe": "0",
                    "input-packets-drop-bad-interface-state": "0",
                    "output-packets-drop-bad-interface-state": "0",
                    "packets-sent": "0",
                    "received-packets-forwarded": "0",
                    "total-packets-received": "0",
                    "total-packets-transmitted": "0",
                },
                "ethoamlfm": {
                    "input-packets-drop-bad-interface-state": "0",
                    "output-packets-drop-bad-interface-state": "0",
                    "packets-sent": "0",
                    "received-packets-forwarded": "0",
                    "total-packets-received": "0",
                    "total-packets-transmitted": "0",
                },
                "icmp": {
                    "calls-to-icmp-error":
                    "17648",
                    "drops-due-to-rate-limit":
                    "0",
                    "echo-drops-with-broadcast-or-multicast-destinaton-address":
                    "0",
                    "errors-not-generated-because-old-message-was-icmp":
                    "115",
                    "histogram": [
                        {
                            "destination-unreachable": "13554",
                            "icmp-echo": "15",
                            "icmp-echo-reply": "18108802",
                            "time-exceeded": "4094",
                            "type-of-histogram": "Output "
                            "Histogram",
                        },
                        {
                            "destination-unreachable": "7376365",
                            "icmp-echo": "18108802",
                            "icmp-echo-reply": "15",
                            "time-exceeded": "11308301",
                            "type-of-histogram": "Input "
                            "Histogram",
                        },
                    ],
                    "message-responses-generated":
                    "18108802",
                    "messages-less-than-the-minimum-length":
                    "0",
                    "messages-with-bad-checksum":
                    "0",
                    "messages-with-bad-code-fields":
                    "0",
                    "messages-with-bad-length":
                    "0",
                    "messages-with-bad-source-address":
                    "0",
                    "timestamp-drops-with-broadcast-or-multicast-destination-address":
                    "0",
                },
                "icmp6": {
                    "address-unreachable":
                    "31",
                    "administratively-prohibited":
                    "0",
                    "bad-checksums":
                    "0",
                    "beyond-scope":
                    "0",
                    "calls-to-icmp6-error":
                    "31",
                    "erroneous-header-field":
                    "0",
                    "errors-not-generated-because-old-message-was-icmp-error":
                    "0",
                    "errors-not-generated-because-rate-limitation":
                    "0",
                    "histogram-of-error-messages-to-be-generated":
                    "Histogram "
                    "of "
                    "error "
                    "messages "
                    "to "
                    "be "
                    "generated:",
                    "icmp6-message-responses-generated":
                    "0",
                    "icmp6-messages-with-bad-code-fields":
                    "0",
                    "icmp6-messages-with-bad-length":
                    "0",
                    "input-histogram": {
                        "histogram-type": "Input "
                        "histogram:",
                        "neighbor-advertisement": "543769",
                        "neighbor-solicitation": "544589",
                        "router-advertisement-icmp6-packets": "168",
                        "router-solicitation-icmp6-packets": "8",
                        "time-exceeded-icmp6-packets": "6773211",
                        "unreachable-icmp6-packets": "319",
                    },
                    "messages-less-than-minimum-length":
                    "0",
                    "messages-with-too-many-nd-options":
                    "0",
                    "nd-iri-cnt":
                    "1",
                    "nd-iri-drop":
                    "0",
                    "nd-iri-max":
                    "200",
                    "nd-mgt-cnt":
                    "0",
                    "nd-mgt-drop":
                    "0",
                    "nd-mgt-max":
                    "14960",
                    "nd-public-cnt":
                    "3",
                    "nd-public-drop":
                    "0",
                    "nd-public-max":
                    "59840",
                    "nd-system-drop":
                    "0",
                    "nd-system-max":
                    "75000",
                    "nd6-dad-proxy-conflicts":
                    "0",
                    "nd6-dad-proxy-eqmac-drop":
                    "0",
                    "nd6-dad-proxy-nomac-drop":
                    "543769",
                    "nd6-dad-proxy-requests":
                    "0",
                    "nd6-dad-proxy-resolve-cnt":
                    "0",
                    "nd6-dup-proxy-responses":
                    "0",
                    "nd6-ndp-proxy-requests":
                    "0",
                    "nd6-ndp-proxy-resolve-cnt":
                    "0",
                    "nd6-ndp-proxy-responses":
                    "0",
                    "nd6-requests-dropped-during-retry":
                    "0",
                    "nd6-requests-dropped-on-entry":
                    "0",
                    "no-route":
                    "0",
                    "output-histogram": {
                        "histogram-type": "Output "
                        "histogram:",
                        "neighbor-advertisement": "544595",
                        "neighbor-solicitation": "544917",
                        "unreachable-icmp6-packets": "31",
                    },
                    "port-unreachable":
                    "0",
                    "protocol-name":
                    "icmp6:",
                    "time-exceed-reassembly":
                    "0",
                    "time-exceed-transit":
                    "0",
                    "unknown":
                    "0",
                    "unrecognized-next-header":
                    "0",
                    "unrecognized-option":
                    "0",
                },
                "igmp": {
                    "membership-queries-received": "308",
                    "membership-queries-received-with-invalid-fields": "0",
                    "membership-reports-received": "0",
                    "membership-reports-received-for-groups-to-which-we-belong":
                    "0",
                    "membership-reports-received-with-invalid-fields": "0",
                    "membership-reports-sent": "943",
                    "messages-received": "310",
                    "messages-received-with-bad-checksum": "0",
                    "messages-received-with-too-few-bytes": "0",
                },
                "ip": {
                    "bad-header-checksums": "0",
                    "datagrams-that-can-not-be-fragmented": "0",
                    "fragments-created": "458290",
                    "fragments-dropped-after-timeout": "2330",
                    "fragments-dropped-due-to-outofspace-or-dup": "0",
                    "fragments-dropped-due-to-queueoverflow": "0",
                    "fragments-received": "7776172",
                    "incoming-rawip-packets-dropped-no-socket-buffer": "46",
                    "incoming-ttpoip-packets-dropped": "0",
                    "incoming-ttpoip-packets-received": "184307870",
                    "incoming-virtual-node-packets-delivered": "0",
                    "loose-source-and-record-route-options": "0",
                    "multicast-packets-dropped": "0",
                    "option-packets-dropped-due-to-rate-limit": "0",
                    "outgoing-ttpoip-packets-dropped": "0",
                    "outgoing-ttpoip-packets-sent": "185308407",
                    "output-datagrams-fragmented": "189762",
                    "output-packets-discarded-due-to-no-route": "221",
                    "output-packets-dropped-due-to-no-bufs": "0",
                    "packets-destined-to-dead-next-hop": "0",
                    "packets-dropped": "0",
                    "packets-for-this-host": "820969848",
                    "packets-for-unknown-or-unsupported-protocol": "311",
                    "packets-forwarded": "0",
                    "packets-not-forwardable": "0",
                    "packets-reassembled-ok": "3840557",
                    "packets-received": "791044982",
                    "packets-sent-from-this-host": "894573985",
                    "packets-sent-with-fabricated-ip-header": "10684398",
                    "packets-used-first-nexthop-in-ecmp-unilist": "0",
                    "packets-with-bad-options": "0",
                    "packets-with-data-length-less-than-headerlength": "0",
                    "packets-with-data-size-less-than-datalength": "0",
                    "packets-with-header-length-less-than-data-size": "0",
                    "packets-with-incorrect-version-number": "0",
                    "packets-with-options-handled-without-error": "310",
                    "packets-with-size-smaller-than-minimum": "0",
                    "record-route-options": "0",
                    "redirects-sent": "0",
                    "router-alert-options": "310",
                    "strict-source-and-record-route-options": "0",
                    "timestamp-and-address-options": "0",
                    "timestamp-and-prespecified-address-options": "0",
                    "timestamp-options": "0",
                    "transit-re-packets-dropped-on-mgmt-interface": "0",
                },
                "ip6": {
                    "duplicate-or-out-of-space-fragments-dropped":
                    "0",
                    "failures-of-source-address-selection":
                    "0",
                    "forward-cache-hit":
                    "0",
                    "forward-cache-miss":
                    "0",
                    "fragments-that-exceeded-limit":
                    "0",
                    "header-type": [
                        {
                            "globals":
                            "557",
                            "header-for-source-address-selection":
                            "source "
                            "addresses "
                            "on "
                            "an "
                            "outgoing "
                            "I/F",
                            "link-locals":
                            "1088804",
                        },
                        {
                            "globals":
                            "556",
                            "header-for-source-address-selection":
                            "source "
                            "addresses "
                            "of "
                            "same "
                            "scope",
                            "link-locals":
                            "1088804",
                        },
                        {
                            "globals":
                            "1",
                            "header-for-source-address-selection":
                            "source "
                            "addresses "
                            "of "
                            "a "
                            "different "
                            "scope",
                        },
                    ],
                    "histogram":
                    "Input histogram:",
                    "ip6-datagrams-that-can-not-be-fragmented":
                    "0",
                    "ip6-fragments-created":
                    "0",
                    "ip6-fragments-dropped-after-timeout":
                    "0",
                    "ip6-fragments-received":
                    "0",
                    "ip6-option-packets-dropped-due-to-rate-limit":
                    "0",
                    "ip6-output-datagrams-fragmented":
                    "0",
                    "ip6-output-packets-discarded-due-to-no-route":
                    "1026",
                    "ip6-output-packets-dropped-due-to-no-bufs":
                    "0",
                    "ip6-packets-destined-to-dead-next-hop":
                    "0",
                    "ip6-packets-dropped":
                    "0",
                    "ip6-packets-for-this-host":
                    "100720775",
                    "ip6-packets-forwarded":
                    "0",
                    "ip6-packets-not-forwardable":
                    "0",
                    "ip6-packets-reassembled-ok":
                    "0",
                    "ip6-packets-sent-from-this-host":
                    "101650461",
                    "ip6-packets-sent-with-fabricated-ip-header":
                    "4506397",
                    "ip6-packets-with-bad-options":
                    "0",
                    "ip6-packets-with-incorrect-version-number":
                    "0",
                    "ip6-packets-with-size-smaller-than-minimum":
                    "0",
                    "ip6-redirects-sent":
                    "0",
                    "ip6nh-icmp6":
                    "7862042",
                    "ip6nh-ospf":
                    "4501689",
                    "ip6nh-tcp":
                    "5981275",
                    "ip6nh-udp":
                    "82375747",
                    "multicast-packets-which-we-do-not-join":
                    "0",
                    "packets-discarded-due-to-too-may-headers":
                    "0",
                    "packets-dropped-due-to-bad-protocol":
                    "0",
                    "packets-that-violated-scope-rules":
                    "0",
                    "packets-whose-headers-are-not-continuous":
                    "0",
                    "packets-with-datasize-less-than-data-length":
                    "0",
                    "total-packets-received":
                    "100720784",
                    "transit-re-packet-dropped-on-mgmt-interface":
                    "0",
                    "tunneling-packets-that-can-not-find-gif":
                    "0",
                },
                "ipcomp": {
                    "ipcomp-bytes-in": "0",
                    "ipcomp-bytes-out": "0",
                    "ipcomp-crypto-processing-failure": "0",
                    "ipcomp-packets-blocked-due-to-policy": "0",
                    "ipcomp-packets-dropped-as-invalid-tdb": "0",
                    "ipcomp-packets-dropped-as-larger-than-ip-maxpacket": "0",
                    "ipcomp-packets-dropped-as-protocol-not-supported": "0",
                    "ipcomp-packets-dropped-due-to-bad-kcr": "0",
                    "ipcomp-packets-dropped-due-to-no-tdb": "0",
                    "ipcomp-packets-dropped-due-to-no-transform": "0",
                    "ipcomp-packets-dropped-due-to-queue-full": "0",
                    "ipcomp-packets-in": "0",
                    "ipcomp-packets-out": "0",
                    "ipcomp-packets-shorter-than-header-shows": "0",
                    "ipcomp-replay-counter-wrap": "0",
                    "packets-sent-uncompressed-threshold": "0",
                    "packets-sent-uncompressed-useless": "0",
                },
                "ipsec": {
                    "cluster-coalesced-during-clone": "0",
                    "cluster-copied-during-clone": "0",
                    "inbound-packets-violated-process-security-policy": "0",
                    "invalid-outbound-packets": "0",
                    "mbuf-coalesced-during-clone": "0",
                    "mbuf-inserted-during-makespace": "0",
                    "outbound-packets-failed-due-to-insufficient-memory": "0",
                    "outbound-packets-violated-process-security-policy": "0",
                    "outbound-packets-with-bundled-sa": "0",
                    "outbound-packets-with-no-route": "0",
                    "outbound-packets-with-no-sa-available": "0",
                },
                "ipsec6": {
                    "cluster-coalesced-during-clone": "0",
                    "cluster-copied-during-clone": "0",
                    "inbound-packets-violated-process-security-policy": "0",
                    "invalid-outbound-packets": "0",
                    "mbuf-coalesced-during-clone": "0",
                    "mbuf-inserted-during-makespace": "0",
                    "outbound-packets-failed-due-to-insufficient-memory": "0",
                    "outbound-packets-violated-process-security-policy": "0",
                    "outbound-packets-with-bundled-sa": "0",
                    "outbound-packets-with-no-route": "0",
                    "outbound-packets-with-no-sa-available": "0",
                },
                "mpls": {
                    "after-tagging-packets-can-not-fit-link-mtu": "0",
                    "lsp-ping-packets": "5",
                    "packets-discarded-due-to-no-route": "0",
                    "packets-dropped": "0",
                    "packets-dropped-at-mpls-socket-send": "0",
                    "packets-dropped-at-p2mp-cnh-output": "0",
                    "packets-dropped-due-to-ifl-down": "0",
                    "packets-forwarded": "6118",
                    "packets-forwarded-at-mpls-socket-send": "0",
                    "packets-used-first-nexthop-in-ecmp-unilist": "0",
                    "packets-with-header-too-small": "0",
                    "packets-with-ipv4-explicit-null-checksum-errors": "0",
                    "packets-with-ipv4-explicit-null-tag": "0",
                    "packets-with-router-alert-tag": "0",
                    "packets-with-tag-encoding-error": "0",
                    "packets-with-ttl-expired": "4209",
                    "total-mpls-packets-received": "4214",
                },
                "pfkey": {
                    "bytes-sent-from-userland": "69304",
                    "bytes-sent-to-userland": "3189032",
                    "incoming-messages-with-memory-allocation-failure": "0",
                    "input-histogram": {
                        "add": "17",
                        "dump": "10626",
                        "histogram": "histogram by "
                        "message type:",
                        "reserved": "626",
                    },
                    "messages-too-short": "0",
                    "messages-toward-all-sockets": "0",
                    "messages-toward-registered-sockets": "0",
                    "messages-toward-single-socket": "22500",
                    "messages-with-duplicate-extension": "0",
                    "messages-with-invalid-address-extension": "0",
                    "messages-with-invalid-extension-type": "0",
                    "messages-with-invalid-length-field": "0",
                    "messages-with-invalid-message-type-field": "0",
                    "messages-with-invalid-sa-type": "0",
                    "messages-with-invalid-version-field": "0",
                    "outgoing-messages-with-memory-allocation-failure": "0",
                    "output-histogram": {
                        "add": "17",
                        "dump": "626",
                        "histogram": "histogram by "
                        "message type:",
                        "reserved": "626",
                    },
                    "requests-sent-from-userland": "1269",
                    "requests-sent-to-userland": "11269",
                },
                "raw-interface": {
                    "dialer-packets-received": "0",
                    "dialer-packets-transmitted": "0",
                    "faboam-packets-dropped": "0",
                    "faboam-packets-received": "0",
                    "faboam-packets-transmitted": "0",
                    "fibre-channel-packets-dropped": "0",
                    "fibre-channel-packets-received": "0",
                    "fibre-channel-packets-transmitted": "0",
                    "fip-packets-dropped": "0",
                    "fip-packets-received": "0",
                    "fip-packets-transmitted": "0",
                    "igmpl2-packets-received": "0",
                    "igmpl2-packets-transmitted": "0",
                    "input-drops-due-to-bogus-protocol": "0",
                    "input-drops-due-to-no-mbufs-available": "0",
                    "input-drops-due-to-no-socket": "0",
                    "input-drops-due-to-no-space-in-socket": "0",
                    "isdn-packets-received": "0",
                    "isdn-packets-transmitted": "0",
                    "lacp-packets-dropped": "0",
                    "lacp-packets-received": "0",
                    "lacp-packets-transmitted": "0",
                    "mldl2-packets-received": "0",
                    "mldl2-packets-transmitted": "0",
                    "mpu-packets-received": "0",
                    "mpu-packets-transmitted": "0",
                    "output-drops-due-to-transmit-error": "0",
                    "ppoe-packets-transmitted": "0",
                    "ppp-packets-received-from-jppd": "0",
                    "ppp-packets-received-from-pppd": "0",
                    "ppp-packets-transmitted-to-jppd": "0",
                    "ppp-packets-transmitted-to-pppd": "0",
                    "pppoe-packets-received": "0",
                    "raw-packets-transmitted": "0",
                    "stp-packets-dropped": "0",
                    "stp-packets-received": "0",
                    "stp-packets-transmitted": "0",
                    "vccp-packets-dropped": "0",
                    "vccp-packets-received": "0",
                    "vccp-packets-transmitted": "0",
                },
                "rdp": {
                    "acks-received": "0",
                    "acks-sent": "0",
                    "closes": "0",
                    "connects": "0",
                    "input-packets": "0",
                    "keepalives-received": "0",
                    "keepalives-sent": "0",
                    "output-packets": "0",
                    "packets-discarded-due-to-bad-sequence-number": "0",
                    "packets-discarded-for-bad-checksum": "0",
                    "packets-dropped-due-to-full-socket-buffers": "0",
                    "packets-dropped-full-repl-sock-buf": "0",
                    "refused-connections": "0",
                    "retransmits": "0",
                },
                "tcp": {
                    "aborted": "0",
                    "ack-header-predictions": "7954923",
                    "acks-bytes": "51344691",
                    "acks-sent-in-response-but-not-exact-rsts": "0",
                    "acks-sent-in-response-to-syns-on-established-connections":
                    "0",
                    "attempts": "48562532",
                    "bad-connection-attempts": "445",
                    "badack": "0",
                    "bucket-overflow": "0",
                    "byte-retransmits": "72",
                    "bytes": "589372",
                    "cache-overflow": "0",
                    "completed": "1258",
                    "connection-accepts": "1258",
                    "connection-requests": "12181907",
                    "connections-closed": "12185170",
                    "connections-dropped-by-persist-timeout": "0",
                    "connections-dropped-by-retransmit-timeout": "162",
                    "connections-established": "1921",
                    "connections-updated-rtt-on-close": "1295",
                    "connections-updated-ssthresh-on-close": "360",
                    "connections-updated-variance-on-close": "1295",
                    "cookies-received": "0",
                    "cookies-sent": "0",
                    "data-packet-header-predictions": "50195730",
                    "data-packets-bytes": "50070222",
                    "dropped": "22",
                    "drops": "438",
                    "duplicate-in-bytes": "724472",
                    "dupsyn": "66",
                    "embryonic-connections-dropped": "12177767",
                    "icmp-packets-ignored": "1",
                    "in-sequence-bytes": "285830455",
                    "keepalive-connections-dropped": "981880",
                    "keepalive-probes-sent": "206621688",
                    "keepalive-timeouts": "207603568",
                    "listen-queue-overflows": "0",
                    "out-of-order-in-bytes": "58516475",
                    "out-of-sequence-segment-drops": "0",
                    "outgoing-segments-dropped": "0",
                    "packets-received": "568918236",
                    "packets-received-after-close": "300",
                    "packets-received-in-sequence": "66028796",
                    "packets-sent": "265067267",
                    "persist-timeouts": "20",
                    "rcv-packets-dropped": "0",
                    "rcv-packets-dropped-due-to-bad-address": "0",
                    "received-acks": "40876471",
                    "received-acks-for-unsent-data": "0",
                    "received-completely-duplicate-packet": "133613375",
                    "received-discarded-because-packet-too-short": "0",
                    "received-discarded-for-bad-checksum": "1054",
                    "received-discarded-for-bad-header-offset": "0",
                    "received-duplicate-acks": "286371924",
                    "received-old-duplicate-packets": "0",
                    "received-out-of-order-packets": "124832",
                    "received-packets-of-data-after-window": "1207",
                    "received-packets-with-some-dupliacte-data": "463",
                    "received-window-probes": "13",
                    "received-window-update-packets": "2896764",
                    "reset": "10",
                    "retransmit-timeouts": "7925703",
                    "retransmitted": "193",
                    "retransmitted-bytes": "49357786",
                    "rst-packets": "179223021",
                    "sack-opitions-sent": "112",
                    "sack-options-received": "4489",
                    "sack-recovery-episodes": "820",
                    "sack-scoreboard-overflow": "0",
                    "segment-retransmits": "7",
                    "segments-updated-rtt": "38164243",
                    "send-packets-dropped": "0",
                    "sent-ack-only-packets": "196251531",
                    "sent-control-packets": "191406234",
                    "sent-data-packets": "52540975",
                    "sent-data-packets-retransmitted": "106367",
                    "sent-packets-delayed": "48859032",
                    "sent-resends-by-mtu-discovery": "0",
                    "sent-urg-only-packets": "0",
                    "sent-window-probe-packets": "0",
                    "sent-window-update-packets": "3986251",
                    "some-duplicate-in-bytes": "79013",
                    "stale": "15",
                    "syncache-entries-added": "1283",
                    "unreach": "0",
                    "zone-failures": "0",
                },
                "tnp": {
                    "broadcast-packets-received": "18139293",
                    "broadcast-packets-sent": "18140864",
                    "control-packets-received": "0",
                    "control-packets-sent": "0",
                    "fragment-reassembly-queue-flushes": "0",
                    "fragmented-packets-received": "0",
                    "fragmented-packets-sent": "0",
                    "hello-packets-received": "18139293",
                    "hello-packets-sent": "18140864",
                    "input-packets-discarded-with-no-protocol": "0",
                    "packets-of-version-unspecified-received": "0",
                    "packets-of-version-unspecified-sent": "0",
                    "packets-of-version1-received": "0",
                    "packets-of-version1-sent": "0",
                    "packets-of-version2-received": "0",
                    "packets-of-version2-sent": "0",
                    "packets-of-version3-received": "18139293",
                    "packets-of-version3-sent": "18140864",
                    "packets-sent-with-unknown-protocol": "0",
                    "packets-with-tnp-src-address-collision-received": "0",
                    "rdp-packets-received": "0",
                    "rdp-packets-sent": "0",
                    "received-fragments-dropped": "0",
                    "received-hello-packets-dropped": "0",
                    "sent-fragments-dropped": "0",
                    "sent-hello-packets-dropped": "0",
                    "tunnel-packets-received": "0",
                    "tunnel-packets-sent": "0",
                    "udp-packets-received": "0",
                    "udp-packets-sent": "0",
                    "unicast-packets-received": "0",
                    "unicast-packets-sent": "0",
                },
                "ttp": {
                    "arp-l3-packets-received": "0",
                    "clnp-l3-packets-received": "0",
                    "cyclotron-cycle-l3-packets-received": "0",
                    "cyclotron-send-l3-packets-received": "0",
                    "input-packets-could-not-get-buffer": "0",
                    "input-packets-for-which-route-lookup-is-bypassed": "0",
                    "input-packets-tlv-dropped": "0",
                    "input-packets-with-bad-af": "0",
                    "input-packets-with-bad-tlv-header": "0",
                    "input-packets-with-bad-tlv-type": "0",
                    "input-packets-with-bad-type": "0",
                    "input-packets-with-discard-type": "0",
                    "input-packets-with-too-many-tlvs": "0",
                    "input-packets-with-ttp-tlv-p2mp-nbr-nhid-type": "0",
                    "input-packets-with-unknown-p2mp-nbr-nhid": "0",
                    "input-packets-with-vxlan-bfd-pkts": "0",
                    "ipv4-l3-packets-received": "83526062",
                    "ipv4-to-mpls-l3-packets-received": "4214",
                    "ipv6-l3-packets-received": "100720753",
                    "l2-packets-received": "56842",
                    "l3-packets-dropped": "0",
                    "l3-packets-sent-could-not-get-buffer": "0",
                    "mpls-l3-packets-received": "0",
                    "mpls-to-ipv4-l3-packets-received": "0",
                    "null-l3-packets-received": "0",
                    "openflow-packets-received": "0",
                    "packets-received-from-unknown-ifl": "0",
                    "packets-received-while-unconnected": "0",
                    "packets-sent-could-not-find-neighbor": "0",
                    "packets-sent-could-not-get-buffer": "0",
                    "packets-sent-when-host_unreachable": "0",
                    "packets-sent-when-transmit-disabled": "0",
                    "packets-sent-while-interface-down": "0",
                    "packets-sent-while-unconnected": "0",
                    "packets-sent-with-bad-af": "0",
                    "packets-sent-with-bad-ifl": "0",
                    "tnp-l3-packets-received": "0",
                    "ttp-packets-sent": "185308407",
                    "unknown-l3-packets-received": "0",
                    "vpls-l3-packets-received": "0",
                },
                "tudp": {
                    "broadcast-or-multicast-datagrams-dropped-due-to-no-socket":
                    "0",
                    "datagrams-dropped-due-to-full-socket-buffers": "0",
                    "datagrams-dropped-due-to-no-socket": "0",
                    "datagrams-output": "1",
                    "datagrams-received": "0",
                    "datagrams-with-bad-checksum": "0",
                    "datagrams-with-bad-data-length-field": "0",
                    "datagrams-with-incomplete-header": "0",
                    "delivered": "0",
                },
                "udp": {
                    "broadcast-or-multicast-datagrams-dropped-due-to-no-socket":
                    "0",
                    "datagrams-delivered": "86615785",
                    "datagrams-dropped-due-to-full-socket-buffers": "26",
                    "datagrams-dropped-due-to-no-socket": "13554",
                    "datagrams-not-for-hashed-pcb": "0",
                    "datagrams-output": "98245707",
                    "datagrams-received": "86629365",
                    "datagrams-with-bad-checksum": "0",
                    "datagrams-with-bad-datalength-field": "0",
                    "datagrams-with-incomplete-header": "0",
                },
            },
            {
                "bridge": {
                    "aging-acks-from-pfe": "0",
                    "aging-non-acks-from-pfe": "0",
                    "aging-requests-over-max-rate": "0",
                    "aging-requests-timed-out-waiting-on-fes": "0",
                    "bogus-address-in-aging-requests": "0",
                    "errors-finding-peer-fes": "0",
                    "learning-requests-over-capacity": "0",
                    "learning-requests-while-learning-disabled-on-interface":
                    "0",
                    "mac-route-aging-requests": "0",
                    "mac-route-learning-requests": "0",
                    "mac-routes-aged": "0",
                    "mac-routes-learned": "0",
                    "mac-routes-moved": "0",
                    "packets-dropped-due-to-no-l3-route-table": "0",
                    "packets-dropped-due-to-no-local-ifl": "0",
                    "packets-dropped-due-to-no-socket": "0",
                    "packets-for-this-host": "0",
                    "packets-punted": "0",
                    "packets-received": "0",
                    "packets-with-incorrect-version-number": "0",
                    "packets-with-no-auxiliary-table": "0",
                    "packets-with-no-ce-facing-entry": "0",
                    "packets-with-no-core-facing-entry": "0",
                    "packets-with-no-family": "0",
                    "packets-with-no-logical-interface": "0",
                    "packets-with-no-route-table": "0",
                    "packets-with-size-smaller-than-minimum": "0",
                    "requests-involving-multiple-peer-fes": "0",
                    "requests-to-age-static-route": "0",
                    "requests-to-learn-an-existing-route": "0",
                    "requests-to-move-static-route": "0",
                    "requests-to-re-ageout-aged-route": "0",
                    "unsupported-platform": "0",
                },
                "vpls": {
                    "aging-acks-from-pfe": "0",
                    "aging-non-acks-from-pfe": "0",
                    "aging-requests-over-max-rate": "0",
                    "aging-requests-timed-out-waiting-on-fes": "0",
                    "bogus-address-in-aging-requests": "0",
                    "errors-finding-peer-fes": "0",
                    "learning-requests-over-capacity": "0",
                    "learning-requests-while-learning-disabled-on-interface":
                    "0",
                    "mac-route-aging-requests": "0",
                    "mac-route-learning-requests": "0",
                    "mac-routes-aged": "0",
                    "mac-routes-learned": "0",
                    "mac-routes-moved": "0",
                    "packets-dropped-due-to-no-l3-route-table": "0",
                    "packets-dropped-due-to-no-local-ifl": "0",
                    "packets-dropped-due-to-no-socket": "0",
                    "packets-for-this-host": "0",
                    "packets-punted": "0",
                    "packets-received": "0",
                    "packets-with-incorrect-version-number": "0",
                    "packets-with-no-auxiliary-table": "0",
                    "packets-with-no-ce-facing-entry": "0",
                    "packets-with-no-core-facing-entry": "0",
                    "packets-with-no-family": "0",
                    "packets-with-no-logical-interface": "0",
                    "packets-with-no-route-table": "0",
                    "packets-with-size-smaller-than-minimum": "0",
                    "requests-involving-multiple-peer-fes": "0",
                    "requests-to-age-static-route": "0",
                    "requests-to-learn-an-existing-route": "0",
                    "requests-to-move-static-route": "0",
                    "requests-to-re-ageout-aged-route": "0",
                    "unsupported-platform": "0",
                },
            },
        ]
    }

    golden_output_1 = {
        "execute.return_value":
        """
                        show system statistics no-forwarding
            Tcp:
                    265067267 packets sent
                            52540975 data packets (50070222 bytes)
                            106367 data packets retransmitted (49357786 bytes)
                            0 resends initiated by MTU discovery
                            196251531 ack only packets (48859032 packets delayed)
                            0 URG only packets
                            0 window probe packets
                            3986251 window update packets
                            191406234 control packets
                    568918236 packets received
                            40876471 acks(for 51344691 bytes)
                            286371924 duplicate acks
                            0 acks for unsent data
                            66028796  packets received in-sequence(285830455 bytes)
                            133613375 completely duplicate packets(724472 bytes)
                            0 old duplicate packets
                            463 packets with some duplicate data(79013 bytes duped)
                            124832 out-of-order packets(58516475 bytes)
                            1207 packets of data after window(589372 bytes)
                            13 window probes
                            2896764 window update packets
                            300 packets received after close
                            1054 discarded for bad checksums
                            0 discarded for bad header offset fields
                            0 discarded because packet too short
                    12181907 connection requests
                    1258 connection accepts
                    445 bad connection attempts
                    0 listen queue overflows
                    1921 connections established (including accepts)
                    12185170 connections closed (including 438 drops)
                            1295 connections updated cached RTT on close
                            1295 connections updated cached RTT variance on close
                            360 connections updated cached ssthresh on close
                    12177767 embryonic connections dropped
                    38164243 segments updated rtt(of 48562532 attempts)
                    7925703 retransmit timeouts
                            162 connections dropped by retransmit timeout
                    20 persist timeouts
                            0 connections dropped by persist timeout
                    207603568 keepalive timeouts
                            206621688 keepalive probes sent
                            981880 connections dropped by keepalive
                    7954923 correct ACK header predictions
                    50195730 correct data packet header predictions
                    1283 syncache entries added
                            193 retransmitted
                            66 dupsyn
                            22 dropped
                            1258 completed
                            0 bucket overflow
                            0 cache overflow
                            10 reset
                            15 stale
                            0 aborted
                            0 badack
                            0 unreach
                            0 zone failures
                    0 cookies sent
                    0 cookies received
                    820 SACK recovery episodes
                    7 segment retransmits in SACK recovery episodes
                    72 byte retransmits in SACK recovery episodes
                    4489 SACK options (SACK blocks) received
                    112 SACK options (SACK blocks) sent
                    0 SACK scoreboard overflow
                    0 ACKs sent in response to in-window but not exact RSTs
                    0 ACKs sent in response to in-window SYNs on established connections
                    0 rcv packets dropped by TCP due to bad address
                    0 out-of-sequence segment drops due to insufficient memory
                    179223021 RST packets
                    1 ICMP packets ignored by TCP
                    0 send packets dropped by TCP due to auth errors
                    0 rcv packets dropped by TCP due to auth errors
                    0 outgoing segments dropped due to policing
            udp:
                    86629365 datagrams received
                    0 with incomplete header
                    0 with bad data length field
                    0 with bad checksum
                    13554 dropped due to no socket
                    0 broadcast/multicast datagrams dropped due to no socket
                    26 dropped due to full socket buffers
                    0 not for hashed pcb
                    86615785 delivered
                    98245707 datagrams output
            ip:
                    791044982 total packets received
                    0 bad header checksums
                    0 with size smaller than minimum
                    0 with data size < data length
                    0 with header length < data size
                    0 with data length < header length
                    0 with incorrect version number
                    0 packets destined to dead next hop
                    7776172 fragments received
                    0 fragments dropped (dup or out of space)
                    0 fragment sessions dropped (queue overflow)
                    2330 fragments dropped after timeout
                    3840557 packets reassembled ok
                    820969848 packets for this host
                    311 packets for unknown/unsupported protocol
                    0 packets forwarded
                    0 packets not forwardable
                    0 redirects sent
                    894573985 packets sent from this host
                    10684398 packets sent with fabricated ip header
                    0 output packets dropped due to no bufs
                    221 output packets discarded due to no route
                    189762 output datagrams fragmented
                    458290 fragments created
                    0 datagrams that can't be fragmented
                    0 packets with bad options
                    310 packets with options handled without error
                    0 strict source and record route options
                    0 loose source and record route options
                    0 record route options
                    0 timestamp options
                    0 timestamp and address options
                    0 timestamp and prespecified address options
                    0 option packets dropped due to rate limit
                    310 router alert options
                    0 multicast packets dropped (no iflist)
                    0 packets dropped (src and int don't match)
                    0 transit re packets dropped on mgmt i/f
                    0 packets used first nexthop in ecmp unilist
                    184307870 incoming ttpoip packets received
                    0 incoming ttpoip packets dropped
                    185308407 outgoing TTPoIP packets sent
                    0 outgoing TTPoIP packets dropped
                    46 raw packets dropped. no space in socket recv buffer
                    0 packets consumed by virtual-node processing
            icmp:
                    0 drops due to rate limit
                    17648 calls to icmp_error
                    115 errors not generated because old message was icmp
                    Output Histogram
                            18108802 echo reply
                            13554 destination unreachable
                            15 echo
                            4094 time exceeded
                    0 messages with bad code fields
                    0 messages less than the minimum length
                    0 messages with bad checksum
                    0 messages with bad source address
                    0 messages with bad length
                    0 echo drops with broadcast or multicast destinaton address
                    0 timestamp drops with broadcast or multicast destination address
                    Input Histogram
                            15 echo reply
                            7376365 destination unreachable
                            18108802 echo
                            11308301 time exceeded
                    18108802 message responses generated
            igmp:
                    310 messages received
                    0 messages received with too few bytes
                    0 messages received with bad checksum
                    308 membership queries received
                    0 membership queries received with invalid fields
                    0 membership reports received
                    0 membership reports received with invalid fields
                    0 membership reports received for groups to which we belong
                    943 Membership reports sent
            ipsec:
                    0 inbound packets violated process security policy
                    0 Outbound packets violated process security policy
                    0 outbound packets with no SA available
                    0 outbound packets failed due to insufficient memory
                    0 outbound packets with no route
                    0 invalid outbound packets
                    0 Outbound packets with bundles SAs
                    0 mbuf coleasced during clone
                    0 Cluster coalesced during clone
                    0 Cluster copied during clone
                    0 mbuf inserted during makespace
            ah:
                    0 packets shorter than header shows
                    0 packets dropped protocol unsupported
                    0 packets dropped no TDB
                    0 packets dropped bad KCR
                    0 packets dropped queue full
                    0 packets dropped no transform
                    0 replay counter wrap
                    0 packets dropped bad authentication detected
                    0 packets dropped bad authentication length
                    0 possible replay packets detected
                    0 packets in
                    0 packets out
                    0 packets dropped invalid TDB
                    0 bytes in
                    0 bytes out
                    0 packets dropped larger than maxpacket
                    0 packets blocked due to policy
                    0 crypto processing failure
                    0 tunnel sanity check failures
            esp:
                    0 packets shorter than header shows
                    0 packets dropped protocol not supported
                    0 packets dropped no TDB
                    0 packets dropped bad KCR
                    0 packets dropped queue full
                    0 packets dropped no transform
                    0 packets dropped bad ilen
                    0 replay counter wrap
                    0 packets dropped bad encryption detected
                    0 packets dropped bad authentication detected
                    0 possible replay packets detected
                    0 packets in
                    0 packets out
                    0 packets dropped invalid TDB
                    0 bytes in
                    0 bytes out
                    0 packets dropped larger than maxpacket
                    0 packets blocked due to policy
                    0 crypto processing failure
                    0 tunnel sanity check failures
            ipcomp:
                    0 packets shorter than header shows
                    0 packets dropped protocol not supported
                    0 packets dropped no TDB
                    0 packets dropped bad KCR
                    0 packets dropped queue full
                    0 packets dropped no transform
                    0 replay counter wrap
                    0 packets in
                    0 packets out
                    0 packets dropped invalid TDB
                    0 bytes in
                    0 bytes out
                    0 packets dropped larger than maxpacket
                    0 packets blocked due to policy
                    0 crypto processing failure
                    0 packets sent uncompressed threshold
                    0 packets sent uncompressed useless
            raw_if:
                    0 RAW packets transmitted
                    0 PPPOE packets transmitted
                    0 ISDN packets transmitted
                    0 DIALER packets transmitted
                    0 PPP packets transmitted to pppd
                    0 PPP packets transmitted to jppd
                    0 IGMPL2 packets transmitted
                    0 MLDL2 packets transmitted
                    0 Fibre Channel packets transmitted
                    0 FIP packets transmitted
                    0 STP packets transmitted
                    0 LACP packets transmitted
                    0 VCCP packets transmitted
                    0 Fabric OAM packets transmitted
                    0 output drops due to tx error
                    0 MPU packets transmitted
                    0 PPPOE packets received
                    0 ISDN packets received
                    0 DIALER packets received
                    0 PPP packets received from pppd
                    0 MPU packets received
                    0 PPP packets received from jppd
                    0 IGMPL2 packets received
                    0 MLDL2 packets received
                    0 Fibre Channel packets received
                    0 FIP packets received
                    0 STP packets received
                    0 LACP packets received
                    0 VCCP packets received
                    0 Fabric OAM packets received
                    0 Fibre Channel packets dropped
                    0 FIP packets dropped
                    0 STP packets dropped
                    0 LACP packets dropped
                    0 Fabric OAM packets dropped
                    0 VCCP packets dropped
                    0 Input drops due to bogus protocol
                    0 input drops due to no mbufs available
                    0 input drops due to no space in socket
                    0 input drops due to no socket
            arp:
                    200794 datagrams received
                    39895 ARP requests received
                    54355 ARP replies received
                    109 resolution request received
                    0 resolution request dropped
                    0 unrestricted proxy requests
                    0 restricted proxy requests
                    0 received proxy requests
                    0 unrestricted proxy requests not proxied
                    0 restricted proxy requests not proxied
                    0 datagrams with bogus interface
                    0 datagrams with incorrect length
                    0 datagrams for non-IP protocol
                    0 datagrams with unsupported op code
                    0 datagrams with bad protocol address length
                    0 datagrams with bad hardware address length
                    0 datagrams with multicast source address
                    87 datagrams with multicast target address
                    0 datagrams with my own hardware address
                    0 datagrams for an address not on the interface
                    0 datagrams with a broadcast source address
                    0 datagrams with source address duplicate to mine
                    106457 datagrams which were not for me
                    7 packets discarded waiting for resolution
                    15 packets sent after waiting for resolution
                    55086 ARP requests sent
                    39895 ARP replies sent
                    0 requests for memory denied
                    0 requests dropped on entry
                    0 requests dropped during retry
                    0 requests dropped due to interface deletion
                    0 requests on unnumbered interfaces
                    0 new requests on unnumbered interfaces
                    0 replies for from unnumbered interfaces
                    0 requests on unnumbered interface with non-subnetted donor
                    0 replies from unnumbered interface with non-subnetted donor
                    0 arp packets rejected as family is configured with deny arp
                    0 arp response packets are rejected on mace icl interface
                    0 arp replies are rejected as source and destination is same
                    0 arp probe for proxy address reachable from the incoming interface
                    0 arp request discarded for vrrp source address
                    0 self arp request packet received on irb interface
                    0 proxy arp request discarded as source ip is a proxy target
                    0 arp packets are dropped as nexthop allocation failed
                    0 arp packets received from peer vrrp rotuer and discarded
                    0 arp packets are rejected as target ip arp resolve is in progress
                    0 grat arp packets are ignored as mac address is not changed
                    0 arp packets are dropped from peer vrrp
                    0 arp packets are dropped as driver call failed
                    0 arp packets are dropped as source is not validated
                    75000 Max System ARP nh cache limit
                    59840 Max Public ARP nh cache limit
                    200 Max IRI ARP nh cache limit
                    14960 Max Management intf ARP nh cache limit
                    4 Current Public ARP nexthops present
                    1 Current IRI ARP nexthops present
                    2 Current Management ARP nexthops present
                    0 Total ARP nexthops creation failed as limit reached
                    0 Public ARP nexthops creation failed as public limit reached
                    0 IRI ARP nexthops creation failed as iri limit reached
                    0 Management ARP nexthops creation failed as mgt limit reached
            ip6:
                    100720784 total packets received
                    0 packets with size smaller than minimum
                    0 packets with data size < data length
                    0 packets with bad options
                    0 packets with incorrect version number
                    0 fragments received
                    0 fragments dropped (dup or out of space)
                    0 fragments dropped after timeout
                    0 fragment sessions dropped (queue overflow)
                    0 packets reassembled ok
                    100720775 packets for this host
                    0 packets forwarded
                    0 packets not forwardable
                    0 redirects sent
                    101650461 packets sent from this host
                    4506397 packets sent with fabricated ip header
                    0 output packets dropped due to no bufs, etc.
                    1026 output packets discarded due to no route
                    0 output datagrams fragmented
                    0 fragments created
                    0 datagrams that can't be fragmented
                    0 packets that violated scope rules
                    0 multicast packets which we don't join
                            Input histogram:
                            5981275 TCP
                            82375747 UDP
                            7862042 ICMP6
                            4501689 OSPF
                            0 packets whose headers are not continuous
                            0 tunneling packets that can't find gif
                            0 packets discarded due to too may headers
                            0 failures of source address selection
                    source addresses on an outgoing I/F
                            1088804 link-locals
                            557 globals
                    source addresses of same scope
                            1088804 link-locals
                            556 globals
                    source addresses of a different scope
                            1 globals
                            0 forward cache hit
                            0 forward cache miss
                            0 Packets destined to dead next hop
                            0 option packets dropped due to rate limit
                            0 Packets dropped (src and int don't match)
                            0 packets dropped due to bad protocol
                            0 transit re packet(null) dropped on mgmt i/f
            icmp6:
                    31 Calls to icmp_error
                    0 Errors not generated because old message was icmp error
                    0 Errors not generated because rate limitation
                    Output histogram:
                            31 unreach
                            544917 neighbor solicitation
                            544595 neighbor advertisement
                    0 Messages with bad code fields
                    0 Messages < minimum length
                    0 Bad checksums
                    0 Messages with bad length
                    Input histogram:
                            319 unreach
                            6773211 time exceeded
                            8 router solicitation
                            168 router advertisment
                            544589 neighbor solicitation
                            543769 neighbor advertisement
                    Histogram of error messages to be generated:
                            0 No route
                            0 Administratively prohibited
                            0 Beyond scope
                            31 Address unreachable
                            0 Port unreachable
                            0 Time exceed transit
                            0 Time exceed reassembly
                            0 Erroneous header field
                            0 Unrecognized next header
                            0 Unrecognized option
                            0 Unknown
                    0 Message responses generated
                    0 Messages with too many ND options
                    75000 Max System ND nh cache limit
                    59840 Max Public ND nh cache limit
                    200 Max IRI ND nh cache limit
                    14960 Max Management intf ND nh cache limit
                    3 Current Public ND nexthops present
                    1 Current IRI ND nexthops present
                    0 Current Management ND nexthops present
                    0 Total ND nexthops creation failed as limit reached
                    0 Public ND nexthops creation failed as public limit reached
                    0 IRI ND nexthops creation failed as iri limit reached
                    0 Management ND nexthops creation failed as mgt limit reached
                    0 interface-restricted ndp proxy requests
                    0 interface-restricted dad proxy requests
                    0 interface-restricted ndp proxy responses
                    0 interface-restricted dad proxy conflicts
                    0 interface-restricted dad proxy duplicates
                    0 interface-restricted ndp proxy resolve requests
                    0 interface-restricted dad proxy resolve requests
                    0 interface-restricted dad packets from same node dropped
                    543769 interface-restricted proxy packets dropped with nomac
                    0 ND hold nexthops dropped on entry by RED mark
                    0 ND hold nexthops dropped on timer expire by RED mark
            ipsec6:
                    0 Inbound packets violated process security policy
                    0 Outbound packets violated process security policy
                    0 Outbound packets with no SA available
                    0 Outbound packets failed due to insufficient memory
                    0 Outbound packets with no route
                    0 Invalid outbound packets
                    0 Outbound packets with bundles SAs
                    0 mbuf coleasced during clone
                    0 Cluster coalesced during clone
                    0 Cluster copied during clone
                    0 mbuf inserted during makespace
            pfkey:
                    1269 Requests sent from userland
                    69304 Bytes sent from userland
                    histogram by message type:
                            626 reserved
                            17 add
                            626 dump
            pfkey:
                    0 Messages with invalid length field
                    0 Messages with invalid version field
                    0 Messages with invalid message type field
                    0 Messages too short
                    0 Messages with memory allocation failure
                    0 Messages with duplicate extension
                    0 Messages with invalid extension type
                    0 Messages with invalid sa type
                    0 Messages with invalid address extension
                    11269 Requests sent to userland
                    3189032 Bytes sent to userland
                    histogram by message type:
                            626 reserved
                            17 add
                            10626 dump
            pfkey:
                    22500 Messages toward single socket
                    0 Messages toward all sockets
                    0 Messages toward registered sockets
                    0 Messages with memory allocation failure
            clnl:
                    0 Total packets received
                    0 Packets delivered
                    0 Too small packets
                    0 Packets with bad header length
                    0 Packets with bad checksum
                    0 Bad version packets
                    0 Unknown or unsupported protocol packets
                    0 Packets with bogus sdl size
                    0 No free memory in socket buffer
                    0 Send packets discarded
                    0 Sbappend failure
                    0 Mcopy failure
                    0 Address fields were not reasonable
                    0 Segment information forgotten
                    0 Forwarded packets
                    0 Total packets sent
                    0 Output packets discarded
                    0 Non-forwarded packets
                    0 Packets fragmented
                    0 Fragments sent
                    0 Fragments discarded
                    0 Fragments timed out
                    0 Fragmentation prohibited
                    0 Packets reconstructed
                    0 Packets destined to dead nexthop
                    0 Packets discarded due to no route
                    0 Error pdu rate drops
                    0 ER pdu generation failure
            esis:
                    0 Total pkts received
                    0 Total packets consumed by protocol
                    0 Pdus received with bad checksum
                    0 Pdus received with bad version number
                    0 Pdus received with bad type field
                    0 Short pdus received
                    0 Pdus withbogus sdl size
                    0 Pdus with bad header length
                    0 Pdus with unknown or unsupport protocol
                    0 No free memory in socket buffer
                    0 Send packets discarded
                    0 Sbappend failure
                    0 Mcopy failure
                    0 ISO family not configured
            tnp:
                    0 Unicast packets received
                    18139293 Broadcast packets received
                    0 Fragmented packets received
                    0 Hello packets dropped
                    0 Fragments dropped
                    0 Fragment reassembly queue flushes
                    0 Packets with tnp src address collision received
                    18139293 Hello packets received
                    0 Control packets received
                    0 Rdp packets received
                    0 Udp packets received
                    0 Tunnel packets received
                    0 Input packets discarded with no protocol
                    0 Packets of version unspecified received
                    0 Packets of version 1 received
                    0 Packets of version 2 received
                    18139293 Packets of version 3 received
                    0 Unicast packets sent
                    18140864 Broadcast packets sent
                    0 Fragmented packets sent
                    0 Hello packets dropped
                    0 Fragments dropped
                    18140864 Hello packets sent
                    0 Control packets sent
                    0 Rdp packets sent
                    0 Udp packets sent
                    0 Tunnel packets sent
                    0 Packets sent with unknown protocol
                    0 Packets of version unspecified sent
                    0 Packets of version 1 sent
                    0 Packets of version 2 sent
                    18140864 Packets of version 3 sent
            rdp:
                    0 Input packets
                    0 Packets discarded for bad checksum
                    0 Packets discarded due to bad sequence number
                    0 Refused connections
                    0 Acks received
                    0 Packets dropped due to full socket buffers
                    0 Retransmits
                    0 Output packets
                    0 Acks sent
                    0 Connects
                    0 Closes
                    0 Keepalives received
                    0 Keepalives sent
            tudp:
                    0 Datagrams received
                    0 Datagrams with incomplete header
                    0 Datagrams with bad data length field
                    0 Datagrams with bad checksum
                    0 Datagrams dropped due to no socket
                    0 Broadcast/multicast datagrams dropped due to no socket
                    0 Datagrams dropped due to full socket buffers
                    0 Delivered
                    1 Datagrams output
            ttp:
                    185308407 Packets sent
                    0 Packets sent while unconnected
                    0 Packets sent while interface down
                    0 Packets sent couldn't get buffer
                    0 Packets sent couldn't find neighbor
                    0 Packets sent when transmit is disable
                    0 Packets sent when host unreachable
                    0 L3 Packets sent could not get buffer
                    0 L3 Packets dropped
                    0 Packets sent with bad logical interface
                    0 Packets sent with bad address family
                    56842 L2 packets received
                    0 Unknown L3 packets received
                    83526062 IPv4 L3 packets received
                    0 MPLS L3 packets received
                    0 MPLS->IPV4 L3 packets received
                    4214 IPv4->MPLS L3 packets received
                    0 VPLS L3 packets received
                    100720753 IPv6 L3 packets received
                    0 ARP L3 packets received
                    0 CLNP L3 packets received
                    0 TNP L3 packets received
                    0 NULL L3 packets received
                    0 Cyclotron cycle L3 packets received
                    0 Cyclotron send L3 packets received
                    0 Openflow packets received
                    0 Packets received while unconnected
                    0 Packets received from unknown ifl
                    0 Input packets couldn't get buffer
                    0 Input packets with bad type
                    0 Input packets with discard type
                    0 Input packets with too many tlvs
                    0 Input packets with bad tlv header
                    0 Input packets with bad tlv type
                    0 Input packets dropped based on tlv result
                    0 Input packets with bad address family
                    0 Input packets for which rt lookup is bypassed
                    0 Input packets with ttp tlv of type TTP_TLV_P2MP_NBR_NHID
                    0 Input packets with unknown p2mp_nbr_nhid value
                    0 Input packets of type vxlan bfd
            mpls:
                    4214 Total MPLS packets received
                    6118 Packets forwarded
                    0 Packets dropped
                    0 Packets with header too small
                    0 After tagging, packets can't fit link MTU
                    0 Packets with IPv4 explicit NULL tag
                    0 Packets with IPv4 explicit NULL cksum errors
                    0 Packets with router alert tag
                    5 LSP ping packets (ttl-expired/router alert)
                    4209 Packets with ttl expired
                    0 Packets with tag encoding error
                    0 Packets discarded due to no route
                    0 Packets used first nexthop in ecmp unilist
                    0 Packets dropped due to ifl down
                    0 Packets dropped at mpls socket send op
                    0 Packets forwarded at mpls socket send op
                    0 Packets dropped, over p2mp composite nexthop
            ethoamlfm:
                    0 total received packets
                    0 input drops due to bad interface state
                    0 received packets forwarded
                    0 total transmitted packets
                    0 sent packets
                    0 output drops due to bad interface state
            ethoamcfm:
                    0 total received packets
                    0 input drops due to bad interface state
                    0 received packets forwarded
                    0 total transmitted packets
                    0 sent packets
                    0 output drops due to bad interface state
                    0 flood requests forwarded to PFE
                    0 flood requests dropped
            vpls:
                    0 Total packets received
                    0 Packets with size smaller than minimum
                    0 Packets with incorrect version number
                    0 Packets for this host
                    0 Packets with no logical interface
                    0 Packets with no family
                    0 Packets with no route table
                    0 Packets with no auxiliary table
                    0 Packets with no core-facing entry
                    0 packets with no CE-facing entry
                    0 MAC route learning requests
                    0 MAC routes learnt
                    0 Requests to learn an existing route
                    0 Learning requests while learning disabled on interface
                    0 Learning requests over capacity
                    0 MAC routes moved
                    0 Requests to move static route
                    0 MAC route aging requests
                    0 MAC routes aged
                    0 Bogus address in aging requests
                    0 Requests to age static route
                    0 Requests to re-ageout aged route
                    0 Requests involving multiple peer FEs
                    0 Aging acks from PFE
                    0 Aging non-acks from PFE
                    0 Aging requests timed out waiting on FEs
                    0 Aging requests over max-rate
                    0 Errors finding peer FEs
                    0 Unsupported platform
                    0 Packets dropped due to no l3 route table
                    0 Packets dropped due to no local ifl
                    0 Packets punted
                    0 Packets dropped due to no socket
            bridge:
                    0 Total packets received
                    0 Packets with size smaller than minimum
                    0 Packets with incorrect version number
                    0 Packets for this host
                    0 Packets with no logical interface
                    0 Packets with no family
                    0 Packets with no route table
                    0 Packets with no auxiliary table
                    0 Packets with no core-facing entry
                    0 packets with no CE-facing entry
                    0 MAC route learning requests
                    0 MAC routes learnt
                    0 Requests to learn an existing route
                    0 Learning requests while learning disabled on interface
                    0 Learning requests over capacity
                    0 MAC routes moved
                    0 Requests to move static route
                    0 MAC route aging requests
                    0 MAC routes aged
                    0 Bogus address in aging requests
                    0 Requests to age static route
                    0 Requests to re-ageout aged route
                    0 Requests involving multiple peer FEs
                    0 Aging acks from PFE
                    0 Aging non-acks from PFE
                    0 Aging requests timed out waiting on FEs
                    0 Aging requests over max-rate
                    0 Errors finding peer FEs
                    0 Unsupported platform
                    0 Packets dropped due to no l3 route table
                    0 Packets dropped due to no local ifl
                    0 Packets punted
                    0 Packets dropped due to no socket

    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemStatisticsNoForwarding(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemStatisticsNoForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == "__main__":
    unittest.main()
