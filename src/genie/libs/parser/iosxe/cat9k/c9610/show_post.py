"""show_post.py
   supported commands:
     * show post
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowPostSchema(MetaParser):
    """Schema for show post"""

    schema = {
        Optional('switch'): {
            Any(): {
                Optional('no_post_information'): bool,
                Optional('modules'): {
                    Any(): {
                        'tests': {
                            Any(): {
                                'status': bool,
                                'begin_timestamp': str,
                                'end_timestamp': str,
                            }
                        }
                    }
                }
            }
        }
    }

class ShowPost(ShowPostSchema):
    """ Parser for show post """

    cli_command = [
        'show post', 
        'show post switch {switch_num}'
    ]

    def cli(self, switch_num=None, output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[1].format(switch_num=switch_num)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
       
        ret_dict = {}
        current_switch = None
        pending_tests = {}

        # Switch C9610R
        p1 = re.compile(r'^Switch\s+(?P<switch_name>\S+)$')

        # No POST information
        p2 = re.compile(r'^No POST information$')

        # Wed Nov 15 12:22:03 2023 POST: Module: 9 Mac Loopback Begin
        p3 = re.compile(r'^(?P<timestamp>\w+\s+\w+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+POST:\s+Module:\s+(?P<module>\d+)\s+(?P<test_name>[\w\s]+)\s+Begin$')

        # Wed Nov 15 12:22:06 2023 POST: Module: 3 Mac Loopback: loopback Test: End, Status Passed
        p4 = re.compile(r'^(?P<timestamp>\w+\s+\w+\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+POST:\s+Module:\s+(?P<module>\d+)\s+[\w\s]+:\s+(?P<test_name>\w+\s+Test):\s+End,\s+Status\s+(?P<test_status>Passed|Failed)$')

        for line in output.splitlines():
            line = line.strip()
                
            # Switch C9610R
            match = p1.match(line)
            if match:
                current_switch = match.group('switch_name')
                ret_dict.setdefault('switch', {})[current_switch] = {}
                pending_tests = {}
                continue
                
            # No POST information
            match = p2.match(line)
            if match and current_switch:
                ret_dict['switch'][current_switch]['no_post_information'] = True
                continue

            # Wed Nov 15 12:22:03 2023 POST: Module: 9 Mac Loopback Begin
            match = p3.match(line)
            if match and current_switch:
                match_data = match.groupdict()
                test_key = f"{match_data['module']}_Mac Loopback"
                pending_tests[test_key] = match_data['timestamp'].strip()
                continue
                
            # Wed Nov 15 12:22:06 2023 POST: Module: 3 Mac Loopback: loopback Test: End, Status Passed
            match = p4.match(line)
            if match and current_switch:
                match_data = match.groupdict()
                test_key = f"{match_data['module']}_Mac Loopback"
                if test_key in pending_tests:
                    module_dict = ret_dict['switch'][current_switch].setdefault('modules', {}).setdefault(match_data['module'], {})
                    module_dict.setdefault('tests', {})[match_data['test_name']] = {
                        'status': match_data['test_status'] == 'Passed',
                        'begin_timestamp': pending_tests.pop(test_key),
                        'end_timestamp': match_data['timestamp'].strip()
                    }
                continue
                
        return ret_dict
