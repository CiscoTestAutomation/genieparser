''' show_feaature.py

NXOS parsers for the following show commands:
    * 'show feature'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


# =====================================
# Parser for 'show feature'
# =====================================
class ShowFeatureSchema(MetaParser):    
    """Schema for:
        show feature
        show feature-set"""

    schema = {'feature':
                {Any():
                    {'instance':
                        {Any():
                            {'state': str,
                             Optional('running'): str}
                        },
                    }
                },
            }

class ShowFeature(ShowFeatureSchema):
    """Parser for show feature"""

    def cli(self, cmd='show feature'):
        out = self.device.execute(cmd)
        f_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # 1) bash-shell             1          disabled
            p1 = re.compile(r'^(?P<name>[\w\-]+) +(?P<inst>\d+) '
                             '+(?P<state>\w+)\(?(?P<run>not-running)?\)?$')
            m = p1.match(line)
            if m:
                if 'feature' not in f_dict:
                    f_dict['feature'] = {}

                name = m.groupdict()['name']
                if name not in f_dict['feature']:
                    f_dict['feature'][name] = {}
                    f_dict['feature'][name]['instance'] = {}

                inst = m.groupdict()['inst']
                if inst not in f_dict['feature'][name]['instance']:
                    f_dict['feature'][name]['instance'][inst] = {}

                state = m.groupdict()['state']
                if state:
                    f_dict['feature'][name]['instance'][inst]['state'] = state

                run = m.groupdict()['run']
                if run:
                    f_dict['feature'][name]['instance'][inst]['running'] = 'no'
                continue
        return f_dict



class ShowFeatureSet(ShowFeature):
    """Parser for show feature-set"""
    pass

    def cli(self):
        cmd = 'show feature-set'
        return super().cli(cmd)

# vim: ft=python et sw=4
