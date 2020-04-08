import unittest
from unittest.mock import Mock

from pyats.topology import Device
from pyats.topology import loader
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_krt import ShowKrtState, \
                                             ShowKrtQueue

class TestShowKrtState(unittest.TestCase):

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show krt state
        General state:
                Install job is not running
                Number of operations queued: 0
                        Routing table adds: 0
                        Interface routes: 0
                        High pri multicast   Adds/Changes: 0
                        Indirect Next Hop    Adds/Changes: 0       Deletes: 0
                        MPLS        Adds: 0       Changes: 0
                        High pri    Adds: 0       Changes: 0       Deletes: 0
                        Normal pri Indirects: 0
                        Normal pri  Adds: 0       Changes: 0       Deletes: 0
                        GMP GENCFG Objects: 0
                        Routing Table deletes: 0
                Number of operations deferred: 0
                Number of operations canceled: 0
                Number of async queue entries: 0
                Number of async non queue entries: 0
                Time until next queue run: 0
                Routes learned from kernel: 34

Routing socket lossage:
        Time until next scan: 58
    '''}

    golden_parsed_output = {
            "krt-state-information": {
                "krt-queue-state": {
                    "krtq-async-count": "0",
                    "krtq-async-non-q-count": "0",
                    "krtq-high-mpls-adds": "0",
                    "krtq-high-mpls-changes": "0",
                    "krtq-high-multicast-adds-changes": "0",
                    "krtq-high-priority-adds": "0",
                    "krtq-high-priority-changes": "0",
                    "krtq-high-priority-deletes": "0",
                    "krtq-indirect-adds-changes": "0",
                    "krtq-indirect-deletes": "0",
                    "krtq-interface-routes": "0",
                    "krtq-kernel-rt-learnt": "34",
                    "krtq-normal-priority-adds": "0",
                    "krtq-normal-priority-changes": "0",
                    "krtq-normal-priority-deletes": "0",
                    "krtq-normal-priority-gmp": "0",
                    "krtq-normal-priority-indirects": "0",
                    "krtq-operations-canceled": "0",
                    "krtq-operations-deferred": "0",
                    "krtq-operations-queued": "0",
                    "krtq-rt-table-adds": "0",
                    "krtq-rt-table-deletes": "0",
                    "krtq-time-until-next-run": "0"
                },
                "rtsock-time-until-next-scan": "58"
            }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowKrtState(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowKrtState(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class TestShowKrtQueue(unittest.TestCase):

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show krt queue
        Routing table add queue: 0 queued
        Interface add/delete/change queue: 0 queued
        Top-priority deletion queue: 0 queued
        Top-priority change queue: 0 queued
        Top-priority add queue: 0 queued
        high priority V4oV6 tcnh delete queue: 0 queued
        high prioriy anchor gencfg delete queue: 0 queued
        High-priority multicast add/change: 0 queued
        Indirect next hop top priority add/change: 0 queued
        Indirect next hop add/change: 0 queued
        high prioriy anchor gencfg add-change queue: 0 queued
        MPLS add queue: 0 queued
        Indirect next hop delete: 0 queued
        High-priority deletion queue: 0 queued
        MPLS change queue: 0 queued
        High-priority change queue: 0 queued
        High-priority add queue: 0 queued
        Normal-priority indirect next hop queue: 0 queued
        Normal-priority deletion queue: 0 queued
        Normal-priority composite next hop deletion queue: 0 queued
        Low prioriy Statistics-id-group deletion queue: 0 queued
        Normal-priority change queue: 0 queued
        Normal-priority add queue: 0 queued
        Least-priority delete queue: 0 queued
        Least-priority change queue: 0 queued
        Least-priority add queue: 0 queued
        Normal-priority pfe table nexthop queue: 0 queued
        EVPN gencfg queue: 0 queued
        Normal-priority gmp queue: 0 queued
        Routing table delete queue: 0 queued
        Low priority route retry queue: 0 queued
    '''}

    golden_parsed_output = {
            "krt-queue-information": {
            "krt-queue": [
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Routing table add queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Interface add/delete/change queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Top-priority deletion queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Top-priority change queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Top-priority add queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "high priority V4oV6 tcnh delete queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "high prioriy anchor gencfg delete queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "High-priority multicast add/change"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Indirect next hop top priority add/change"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Indirect next hop add/change"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "high prioriy anchor gencfg add-change queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "MPLS add queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Indirect next hop delete"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "High-priority deletion queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "MPLS change queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "High-priority change queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "High-priority add queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Normal-priority indirect next hop queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Normal-priority deletion queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Normal-priority composite next hop deletion queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Low prioriy Statistics-id-group deletion queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Normal-priority change queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Normal-priority add queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Least-priority delete queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Least-priority change queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Least-priority add queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Normal-priority pfe table nexthop queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "EVPN gencfg queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Normal-priority gmp queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Routing table delete queue"
                },
                {
                    "krtq-queue-length": "0",
                    "krtq-type": "Low priority route retry queue"
                }
            ]
        }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowKrtQueue(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowKrtQueue(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()