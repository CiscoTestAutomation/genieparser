# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_license import ShowLicense


# ============================
# Unit test for 'show license'
# ============================


class test_show_license(unittest.TestCase):
    """Unit test for 'show license'"""
    maxDiff = None
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
    "licenses": {
        1: {
            "feature": "appxk9",
            "period_left": "Life time",
            "license_type": "Permanent",
            "license_state": "Active, In Use",
            "count": "Non-Counted",
            "license_priority": "Medium",
        },
        2: {
            "feature": "uck9",
            "period_left": "Not Activated",
            "period_minutes": 0,
            "period_seconds": 0,
            "license_type": "EvalRightToUse",
            "license_state": "Active, Not in Use, EULA not accepted",
            "count": "Non-Counted",
            "license_priority": "None"
        },
        3: {
            "feature": "securityk9",
            "period_left": "Life time",
            "license_type": "Permanent",
            "license_state": "Active, In Use",
            "count": "Non-Counted",
            "license_priority": "Medium"
        },
        4: {
            "feature": "ipbasek9",
            "period_left": "Life time",
            "license_type": "Permanent",
            "license_state": "Active, In Use",
            "count": "Non-Counted",
            "license_priority": "Medium"
        },
        5: {
            "feature": "FoundationSuiteK9",
            "period_left": "Not Activated",
            "period_minutes": 0,
            "period_seconds": 0,
            "license_type": "EvalRightToUse",
            "license_state": "Active, Not in Use, EULA not accepted",
            "count": "Non-Counted",
            "license_priority": "None"
        },
        6: {
            "feature": "AdvUCSuiteK9",
            "period_left": "Not Activated",
            "period_minutes": 0,
            "period_seconds": 0,
            "license_type": "EvalRightToUse",
            "license_state": "Active, Not in Use, EULA not accepted",
            "count": "Non-Counted",
            "license_priority": "None"
        },
        7: {
            "feature": "cme-srst",
            "period_left": "Not Activated",
            "period_minutes": 0,
            "period_seconds": 0,
            "license_type": "EvalRightToUse",
            "license_state": "Active, Not in Use, EULA not accepted",
            "count_in_use": 0,
            "count_violation": 0,
            "license_priority": "None"
        },
        8: {
            "feature": "hseck9",
            "period_left": "Life time",
            "license_type": "Permanent",
            "license_state": "Active, In Use",
            "count": "Non-Counted",
            "license_priority": "Medium"
        },
        9: {
            "feature": "throughput",
            "period_left": "Not Activated",
            "period_minutes": 0,
            "period_seconds": 0,
            "license_type": "EvalRightToUse",
            "license_state": "Active, Not in Use, EULA not accepted",
            "count": "Non-Counted",
            "license_priority": "None"
        }
    }
}

    golden_output1 = {'execute.return_value': '''
Index 1 Feature: appxk9                         
        Period left: Life time
        License Type: Permanent
        License State: Active, In Use
        License Count: Non-Counted
        License Priority: Medium
Index 2 Feature: uck9                           
        Period left: Not Activated
        Period Used: 0  minute  0  second
        License Type: EvalRightToUse
        License State: Active, Not in Use, EULA not accepted
        License Count: Non-Counted
        License Priority: None
Index 3 Feature: securityk9                     
        Period left: Life time
        License Type: Permanent
        License State: Active, In Use
        License Count: Non-Counted
        License Priority: Medium
Index 4 Feature: ipbasek9                       
        Period left: Life time
        License Type: Permanent
        License State: Active, In Use
        License Count: Non-Counted
        License Priority: Medium
Index 5 Feature: FoundationSuiteK9              
        Period left: Not Activated
        Period Used: 0  minute  0  second
        License Type: EvalRightToUse
        License State: Active, Not in Use, EULA not accepted
        License Count: Non-Counted
        License Priority: None
Index 6 Feature: AdvUCSuiteK9                   
        Period left: Not Activated
        Period Used: 0  minute  0  second
        License Type: EvalRightToUse
        License State: Active, Not in Use, EULA not accepted
        License Count: Non-Counted
        License Priority: None
Index 7 Feature: cme-srst                       
        Period left: Not Activated
        Period Used: 0  minute  0  second
        License Type: EvalRightToUse
        License State: Active, Not in Use, EULA not accepted
        License Count: 0/0  (In-use/Violation)
        License Priority: None
Index 8 Feature: hseck9                         
        Period left: Life time
        License Type: Permanent
        License State: Active, In Use
        License Count: Non-Counted
        License Priority: Medium
Index 9 Feature: throughput                     
        Period left: Not Activated
        Period Used: 0  minute  0  second
        License Type: EvalRightToUse
        License State: Active, Not in Use, EULA not accepted
        License Count: Non-Counted
        License Priority: None
    '''
                      }

    def test_show_license_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowLicense(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_license_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLicense(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
