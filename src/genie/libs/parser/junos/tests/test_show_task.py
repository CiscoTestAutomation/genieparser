# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.junos.show_task import ShowTaskReplication

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

if __name__ == '__main__':
    unittest.main()
