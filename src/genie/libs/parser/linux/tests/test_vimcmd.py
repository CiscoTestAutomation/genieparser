# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.linux.vimcmd import (VimCmdVmsvcGetAllVms,
                                            VimCmdVmsvcSnapshotGetVmId)

# ===========================
# Unit tests for:
#   'vim-cmd vmsvc/getallvms'
# ===========================
class TestVimCmdVmsvcGetAllVms(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_output = {'execute.return_value': '''
         42     P1-4          [VM_storage] P1-4/P1-4.vmx                 other26xLinuxGuest     vmx-07              
         43     PE1-4_old     [VM_storage] PE1-4/PE1-4.vmx               other26xLinuxGuest     vmx-07              
         45     N7K-PE1-2     [VM_storage] N7K-PE1-2/N7K-PE1-2.vmx       other24xLinuxGuest     vmx-08              
         51     n9kv1_1       [VM_storage] n9kv1_1/n9kv1_1.vmx           otherGuest64           vmx-10              
         52     n9kv2_1       [VM_storage] n9kv2_1/n9kv2_1.vmx           otherGuest64           vmx-10              
          9     PE1-2         [VM_storage] PE1/PE1.vmx                   other24xLinuxGuest     vmx-08
    '''}
    
    golden_parsed_output = {
        'vmid': {
            '42': {
                'vmid': '42',
                'name': 'P1-4',
                'file': '[VM_storage] P1-4/P1-4.vmx',
                'guest_os': 'other26xLinuxGuest',
                'version': 'vmx-07'
            },
            '43': {
                'vmid': '43',
                'name': 'PE1-4_old',
                'file': '[VM_storage] PE1-4/PE1-4.vmx',
                'guest_os': 'other26xLinuxGuest',
                'version': 'vmx-07'
            },
            '45': {
                'vmid': '45',
                'name': 'N7K-PE1-2',
                'file': '[VM_storage] N7K-PE1-2/N7K-PE1-2.vmx',
                'guest_os': 'other24xLinuxGuest',
                'version': 'vmx-08'
            },
            '51': {
                'vmid': '51',
                'name': 'n9kv1_1',
                'file': '[VM_storage] n9kv1_1/n9kv1_1.vmx',
                'guest_os': 'otherGuest64',
                'version': 'vmx-10'
            },
            '52': {
                'vmid': '52',
                'name': 'n9kv2_1',
                'file': '[VM_storage] n9kv2_1/n9kv2_1.vmx',
                'guest_os': 'otherGuest64',
                'version': 'vmx-10'
            },
            '9': {
                'vmid': '9',
                'name': 'PE1-2',
                'file': '[VM_storage] PE1/PE1.vmx',
                'guest_os': 'other24xLinuxGuest',
                'version': 'vmx-08' 
            }
        }
    }

    def test_getallvms_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = VimCmdVmsvcGetAllVms(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, {'vmid': {}})

    def test_getallvms_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = VimCmdVmsvcGetAllVms(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ======================================
# Unit tests for:
#   'vim-cmd vmsvc/snapshot.get {vmid}'
# ======================================
class TestVimCmdVmsvcSnapshotGetVmId(unittest.TestCase):    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}        
    
    golden_output = {'execute.return_value': '''
        Get Snapshot:
        |-ROOT
        --Snapshot Name        : P1_4_golden
        --Snapshot Id        : 8
        --Snapshot Desciption  :
        --Snapshot Created On  : 2/10/2016 11:10:47
        --Snapshot State       : powered off
    '''}
    
    golden_parsed_output = {
        "vmid": {
            "42": {
                "snapshot": {
                    '8': {
                        "created": "2/10/2016 11:10:47",
                        "id": "8",
                        "name": "P1_4_golden",
                        "state": "powered off"
                    }
                }
            }
        }        
    }
    
    def test_get_snapshot_vmid_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = VimCmdVmsvcSnapshotGetVmId(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, {'vmid': {}})

    def test_get_snapshot_vmid_golden(self):
        self.device = Mock(**self.golden_output)
        obj = VimCmdVmsvcSnapshotGetVmId(device=self.device)
        parsed_output = obj.parse(vmid='42')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)    

if __name__ == '__main__':
    unittest.main()
