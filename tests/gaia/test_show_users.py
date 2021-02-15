#Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# Parser
from genie.libs.parser.gaia.show_users import ShowUsers

class test_show_users(unittest.TestCase):
    device = Device(name='gw')
    
    golden_output = {'execute.return_value': '''\

    User             Uid       Gid       Home Dir.        Shell            Real Name               Privileges
    admin            0         0         /home/admin      /etc/cli.sh      Admin                   Access to Expert features
    monitor          102       100       /home/monitor    /etc/cli.sh      Monitor                 None
    somedude         10        20        /home/somewhere  /bin/bash        Some Dude               None
    '''}

    golden_parsed_output = {
        'users': { 
            'admin': {
                'uid': '0',
                'gid': '0',
                'home': '/home/admin',
                'shell': '/etc/cli.sh',
                'name': 'Admin ',
                'privileges': 'Access to Expert features'
            },
            'monitor': {
                'uid': '102',
                'gid': '100',
                'home': '/home/monitor',
                'shell': '/etc/cli.sh',
                'name': 'Monitor ',
                'privileges': 'None' 
            },
            'somedude': {
                'uid': '10',
                'gid': '20',
                'home': '/home/somewhere',
                'shell': '/bin/bash',
                'name': 'Some Dude',
                'privileges': 'None' 
            }
        }
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        self.maxDiff = None
        obj = ShowUsers(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)