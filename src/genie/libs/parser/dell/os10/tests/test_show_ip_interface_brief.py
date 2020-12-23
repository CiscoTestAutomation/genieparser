
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# iosxe show_ospf
from genie.libs.parser.dell.os10.show_ip_interface_brief import ShowIPInterfaceBrief


class test_show_ip_interface_brief(unittest.TestCase):
    '''Unit test for "show ip interface brief" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = {
    'ints': {
        'Ethernet 1/1/1': {
            'ip_address': 'unassigned',
            'ok': True,
            'method': 'unset',
            'status': 'up',
            'protocol': 'up'
        },
        'Ethernet 1/1/2': {
            'ip_address': 'unassigned',
            'ok': True,
            'method': 'unset',
            'status': 'up',
            'protocol': 'up'
        },
        'Ethernet 1/1/3': {
            'ip_address': 'unassigned',
            'ok': True,
            'method': 'unset',
            'status': 'up',
            'protocol': 'up'
        },
        'Ethernet 1/1/4': {
            'ip_address': 'unassigned',
            'ok': True,
            'method': 'unset',
            'status': 'up',
            'protocol': 'up'
        },
        'Ethernet 1/1/5': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/6': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/7': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/8': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/9': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/10': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/11': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/12': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/13': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/14': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/15': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/16': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/17': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/18': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/19': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/20': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/21': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/22': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/23': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/24': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/25': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/26': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/27': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/28': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/29': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/30': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/31': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Ethernet 1/1/32': {
            'ip_address': 'unassigned',
            'ok': False,
            'method': 'unset',
            'status': 'up',
            'protocol': 'down'
        },
        'Management 1/1/1': {
            'ip_address': '10.10.21.16/24',
            'ok': True,
            'method': 'manual',
            'status': 'up',
            'protocol': 'up'
        },
        'Vlan 1': {
            'ip_address': 'unassigned',
            'ok': True,
            'method': 'unset',
            'status': 'up',
            'protocol': 'up'
        }
    }
}

    golden_output_brief = {'execute.return_value': '''
    Interface Name            IP-Address          OK       Method       Status     Protocol 
    =========================================================================================
    Ethernet 1/1/1            unassigned          YES      unset        up          up       
    Ethernet 1/1/2            unassigned          YES      unset        up          up       
    Ethernet 1/1/3            unassigned          YES      unset        up          up       
    Ethernet 1/1/4            unassigned          YES      unset        up          up       
    Ethernet 1/1/5            unassigned          NO       unset        up          down     
    Ethernet 1/1/6            unassigned          NO       unset        up          down     
    Ethernet 1/1/7            unassigned          NO       unset        up          down     
    Ethernet 1/1/8            unassigned          NO       unset        up          down     
    Ethernet 1/1/9            unassigned          NO       unset        up          down     
    Ethernet 1/1/10           unassigned          NO       unset        up          down     
    Ethernet 1/1/11           unassigned          NO       unset        up          down     
    Ethernet 1/1/12           unassigned          NO       unset        up          down     
    Ethernet 1/1/13           unassigned          NO       unset        up          down     
    Ethernet 1/1/14           unassigned          NO       unset        up          down     
    Ethernet 1/1/15           unassigned          NO       unset        up          down     
    Ethernet 1/1/16           unassigned          NO       unset        up          down     
    Ethernet 1/1/17           unassigned          NO       unset        up          down     
    Ethernet 1/1/18           unassigned          NO       unset        up          down     
    Ethernet 1/1/19           unassigned          NO       unset        up          down     
    Ethernet 1/1/20           unassigned          NO       unset        up          down     
    Ethernet 1/1/21           unassigned          NO       unset        up          down     
    Ethernet 1/1/22           unassigned          NO       unset        up          down     
    Ethernet 1/1/23           unassigned          NO       unset        up          down     
    Ethernet 1/1/24           unassigned          NO       unset        up          down     
    Ethernet 1/1/25           unassigned          NO       unset        up          down     
    Ethernet 1/1/26           unassigned          NO       unset        up          down     
    Ethernet 1/1/27           unassigned          NO       unset        up          down     
    Ethernet 1/1/28           unassigned          NO       unset        up          down     
    Ethernet 1/1/29           unassigned          NO       unset        up          down     
    Ethernet 1/1/30           unassigned          NO       unset        up          down     
    Ethernet 1/1/31           unassigned          NO       unset        up          down     
    Ethernet 1/1/32           unassigned          NO       unset        up          down     
    Management 1/1/1          10.10.21.16/24      YES      manual       up          up       
    Vlan 1                    unassigned          YES      unset        up          up
    '''}

    def test_show_ip_interface_brief(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowIPInterfaceBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main()