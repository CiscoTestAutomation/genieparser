#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_memory import ShowMemoryStatistics


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

        
if __name__ == '__main__':
    unittest.main()

