#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from parser.iosxe.show_memory import ShowMemoryStatistics, \
                                     ShowProcessesCpuSorted


class test_show_memory_statistics(unittest.TestCase):

    dev = Device(name='c3850')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "tracekey": "1#f8e3c2db7822c04e58ce2bd2fc7e476a",
        "name": {
            "processor": {
               "total": 856541768,
               "free": 501425640,
               "largest": 501041348,
               "head": "FF86F21010",
               "lowest": 499097976,
               "used": 355116128
            },
            "lsmpi_io": {
               "total": 6295128,
               "free": 824,
               "largest": 412,
               "head": "FF867C51A8",
               "lowest": 824,
               "used": 6294304
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Tracekey : 1#f8e3c2db7822c04e58ce2bd2fc7e476a   

                        Head    Total(b)     Used(b)     Free(b)   Lowest(b)  Largest(b)
        Processor  FF86F21010   856541768   355116128   501425640   499097976   501041348
         lsmpi_io  FF867C51A8     6295128     6294304         824         824         412'''
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMemoryStatistics(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMemoryStatistics(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_processes_cpu_sorted_CPU(unittest.TestCase):

    dev = Device(name='c3850')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "five_sec_cpu_high": 7,
        "five_min_cpu": 6,
        "one_min_cpu": 6,
        "five_sec_cpu_low": 1
    }

    golden_output = {'execute.return_value': '''\
        show processes cpu sorted 5min | inc CPU
        CPU utilization for five seconds: 7%/1%; one minute: 6%; five minutes: 6%
    '''
    }

    golden_parsed_output_1 = {
        "five_min_cpu": 6,
        "five_sec_cpu_low": 1,
        "one_min_cpu": 6,
        "nonzero_cpu_processes": [
          "PLFM-MGR IPC pro",
          "Spanning Tree"
        ],
        "zero_cpu_processes": [
          "IPC Seat TX Cont"
        ],
        "five_sec_cpu_high": 5,
        "sort": {
            1: {
               "five_min_cpu": 0.54,
               "invoked": 6437005,
               "usecs": 1236,
               "one_min_cpu": 0.53,
               "tty": 0,
               "process": "PLFM-MGR IPC pro",
               "five_sec_cpu": 0.31,
               "runtime": 7962054,
               "pid": 152
            },
            2: {
               "five_min_cpu": 0.31,
               "invoked": 14602032,
               "usecs": 336,
               "one_min_cpu": 0.31,
               "tty": 0,
               "process": "Spanning Tree",
               "five_sec_cpu": 0.23,
               "runtime": 4915791,
               "pid": 242
            },
            3: {
               "five_min_cpu": 0.0,
               "invoked": 1,
               "usecs": 0,
               "one_min_cpu": 0.0,
               "tty": 0,
               "process": "IPC Seat TX Cont",
               "five_sec_cpu": 0.0,
               "runtime": 0,
               "pid": 32
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        CPU utilization for five seconds: 5%/1%; one minute: 6%; five minutes: 6%
         PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process          
         152     7962054     6437005       1236  0.31%  0.53%  0.54%   0 PLFM-MGR IPC pro 
         242     4915791    14602032        336  0.23%  0.31%  0.31%   0 Spanning Tree    
          32           0           1          0  0.00%  0.00%  0.00%   0 IPC Seat TX Cont
    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowProcessesCpuSorted(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowProcessesCpuSorted(device=self.dev)
        parsed_output = obj.parse(key_word='CPU', sort_time='5min')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_1)
        obj = ShowProcessesCpuSorted(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()

