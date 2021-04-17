import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use


class ShowVersionSchema(MetaParser):
    """Schema for show version"""
    schema = {
        'pod': {
            Any(): {
                'node': {
                    Any(): {
                        'name': str,
                        'role': str,
                        'version': str,
                        'node': int,
                        'pod': int
                    }
                }
            }
        }
    }


class ShowVersion(ShowVersionSchema):
    """ Parser class for:
        * 'show version'
    """

    cli_command = 'show version'

    def cli(self, output=None):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #  Role        Pod         Node        Name                      Version              
        #  ----------  ----------  ----------  ------------------------  -------------------- 
        #  controller  1           1           msl-ifav205-ifc1          5.1(2e)              
        #  leaf        1           101         msl-ifav205-leaf1         n9000-15.1(2e)       
        #  spine       1           201         msl-ifav205-spine1        n9000-15.1(2e)       
        #  spine       1           202         msl-ifav205-spine2        n9000-14.2(2e)       
        p1 = re.compile(r"^(?P<role>\S+)  +(?P<pod>\d+)  +(?P<node>\d+)  +(?:(?P<name>\S+)  +)?(?P<version>\S+)")

        version_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()

                node_dict = version_dict.setdefault(
                    'pod', {}).setdefault(
                        int(groups['pod']), {}).setdefault(
                            'node', {}).setdefault(
                                int(groups['node']), {})
                node_dict.update({'role': groups['role']})
                node_dict.update({'pod': int(groups['pod'])})
                node_dict.update({'node': int(groups['node'])})
                node_dict.update({'name': groups['name']})
                node_dict.update({'version': groups['version']})

        return version_dict
