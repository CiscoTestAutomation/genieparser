# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.junos.show_task import ShowTaskReplication, \
                                              ShowTaskMemory

#=========================================================
# Unit test for show task replication
#=========================================================
class TestShowTaskReplication(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output_1 = {
        "task-replication-state": {
            "task-gres-state": "Disabled",
            "task-re-mode": "Master"
        }
    }


    golden_output_1 = {'execute.return_value': '''
        show task replication
            Stateful Replication: Disabled
            RE mode: Master
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowTaskReplication(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowTaskReplication(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


class TestShowTaskReplication(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output_1 = {   
        "task-memory-information":{
            "task-memory-free-size":"2078171",
            "task-memory-free-size-avail":"100",
            "task-memory-free-size-status":"now",
            "task-memory-in-use-avail":"1",
            "task-memory-in-use-size":"26857",
            "task-memory-in-use-size-status":"now",
            "task-memory-max-avail":"1",
            "task-memory-max-size":"27300",
            "task-memory-max-when":"20/10/01 01:27:19"
        }

    }


    golden_output_1 = {'execute.return_value': '''
        show task memory
        Memory                 Size (kB)  Percentage  When
        Currently In Use:        26857          1%  now
        Maximum Ever Used:       27300          1%  20/10/01 01:27:19
        Available:             2078171        100%  now
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowTaskMemory(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowTaskMemory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
