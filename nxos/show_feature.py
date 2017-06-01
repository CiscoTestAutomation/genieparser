''' show_feaature.py

NXOS parsers for the following show commands:
    * 'show feature'
'''

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


# =====================================
# Parser for 'show feature'
# =====================================
class ShowFeatureSchema(MetaParser):    
    '''Schema for show feature'''    
    '''Schema for show feature-set'''
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
    '''Parser for show feature'''
    '''Parser for show feature-set'''

    def cli(self):
        cmd = 'show feature'
        out1 = self.device.execute(cmd)
        cmd = 'show feature-set'
        out2 = self.device.execute(cmd)
        f_dict = {}

        for line in (out1 + out2).splitlines():
            line = line.strip()
            # 1) feature1:
            p1 = re.compile(r'^(?P<name>[a-z0-9\-_]+) +(?P<inst>\d+) '
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
