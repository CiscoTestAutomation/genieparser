# Python
import unittest
from unittest.mock import Mock

# PyATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos ping
from genie.libs.parser.junos.monitor import (MonitorInterfaceTraffic)


class TestMonitorInterfaceTraffic(unittest.TestCase):
    """ Unit tests for:
            * monitor interface traffic
    """

    device = Device(name='aDevice')
    maxDiff = None

    golden_output = '''
        Interface    Link  Input packets        (pps)     Output packets        (pps)\r
        ge-0/0/0      Up        5641273          (0)          3945678          (0)\r
        lc-0/0/0      Up              0                             0\r
        pfh-0/0/0     Up              0                             0\r
        ge-0/0/1      Up         278323          (0)             1748          (0)\r
        ge-0/0/2      Up        5005613          (0)          5612248          (0)\r
        ge-0/0/3      Up              1          (0)                0          (0)\r
        ge-0/0/4      Up             47          (0)            13801          (0)\r
        ge-0/0/5    Down              0          (0)                0          (0)\r
        ge-0/0/6    Down              0          (0)                0          (0)\r
        ge-0/0/7    Down              0          (0)                0          (0)\r
        ge-0/0/8    Down              0          (0)                0          (0)\r
        ge-0/0/9    Down              0          (0)                0          (0)\r
        demux0        Up              0                             0\r
        dsc           Up              0                             0\r
        em1           Up              0                             0\r
        esi           Up              0                             0\r
        fti0          Up              0                             0\r
        fti1          Up              0                             0\r
        fti2          Up              0                             0\r
        fti3          Up              0                             0\r
        fti4          Up              0                             0\r
        fti5          Up              0                             0\r
        fti6          Up              0                             0\r
        fti7          Up              0                             0\r
    '''
    
    golden_parsed_output = {
        'interface': {
            'demux0': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'dsc': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'em1': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'esi': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'fti0': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'fti1': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'fti2': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'fti3': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'fti4': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'fti5': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'fti6': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'fti7': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'ge-0/0/0': {
                'input-packets': 5641273,
                'input-pps': 0,
                'link': 'Up',
                'output-packets': 3945678,
                'output-pps': 0,
            },
            'ge-0/0/1': {
                'input-packets': 278323,
                'input-pps': 0,
                'link': 'Up',
                'output-packets': 1748,
                'output-pps': 0,
            },
            'ge-0/0/2': {
                'input-packets': 5005613,
                'input-pps': 0,
                'link': 'Up',
                'output-packets': 5612248,
                'output-pps': 0,
            },
            'ge-0/0/3': {
                'input-packets': 1,
                'input-pps': 0,
                'link': 'Up',
                'output-packets': 0,
                'output-pps': 0,
            },
            'ge-0/0/4': {
                'input-packets': 47,
                'input-pps': 0,
                'link': 'Up',
                'output-packets': 13801,
                'output-pps': 0,
            },
            'ge-0/0/5': {
                'input-packets': 0,
                'input-pps': 0,
                'link': 'Down',
                'output-packets': 0,
                'output-pps': 0,
            },
            'ge-0/0/6': {
                'input-packets': 0,
                'input-pps': 0,
                'link': 'Down',
                'output-packets': 0,
                'output-pps': 0,
            },
            'ge-0/0/7': {
                'input-packets': 0,
                'input-pps': 0,
                'link': 'Down',
                'output-packets': 0,
                'output-pps': 0,
            },
            'ge-0/0/8': {
                'input-packets': 0,
                'input-pps': 0,
                'link': 'Down',
                'output-packets': 0,
                'output-pps': 0,
            },
            'ge-0/0/9': {
                'input-packets': 0,
                'input-pps': 0,
                'link': 'Down',
                'output-packets': 0,
                'output-pps': 0,
            },
            'lc-0/0/0': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
            'pfh-0/0/0': {
                'input-packets': 0,
                'link': 'Up',
                'output-packets': 0,
            },
        },
    }

    def test_golden(self):
        obj = MonitorInterfaceTraffic(device=self.device)
        parsed_output = obj.parse(output=self.golden_output)
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()