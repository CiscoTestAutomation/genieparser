# Import the Python mock functionality
import unittest
from unittest.mock import Mock

  
# pyATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_ssh1
from genie.libs.parser.iosxr.show_ssh_history import ShowSshHistory

class test_show_ssh_history(unittest.TestCase):

    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 ={
        'session':{
            'incoming': 
                 {1:
                  {'chan': 1,
                   'pty' : 'vty0',
                   'location':'0/RP0/CPU0',
                   'userid':'admin',
                   'host':'172.16.1.254',
                   'ver': 'v2',
                   'authentication':'key-intr',
                   'connection_type':'Command-Line-Interface'
                   },
                  2:
                   {'chan': 1,
                    'pty' : 'vty0',
                    'location':'0/RP0/CPU0',
                    'userid':'admin',
                    'host':'172.16.1.254',
                    'ver': 'v2',
                    'authentication':'key-intr',
                    'connection_type':'Command-Line-Interface'
                    }
                }
        } 
    }
    # Specify the expected unparsed output
    golden_output1 = {'execute.return_value': '''
    id       chan pty     location        userid    host                  ver authentication connection type
    ---------------------------------------------------------------------------------------------------------------
    Incoming sessions
    1        1    vty0    0/RP0/CPU0      admin     172.16.1.254          v2  key-intr       Command-Line-Interface
    2        1    vty0    0/RP0/CPU0      admin     172.16.1.254          v2  key-intr       Command-Line-Interface
    '''}
    
    def test_show_ssh_history_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowSshHistory(device=self.device)
        parsed_output = obj.parse()  
        self.assertEqual(parsed_output, self.golden_parsed_output1)
    
    def test_show_ssh_history_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowSshHistory(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
        
if __name__ == '__main__':
    unittest.main()