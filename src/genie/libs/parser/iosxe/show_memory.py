"""show_memory.py

"""
# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use


class ShowMemoryStatisticsSchema(MetaParser):
    """Schema for show memory statistics"""
    schema = {
        Optional('tracekey'): str,
        'name': {
            Any(): {
                'head': str,
                'total': int,
                'used': int,
                'free': int,
                'lowest': int,
                'largest': int,
            }
        }
    }


class ShowMemoryStatistics(ShowMemoryStatisticsSchema):
    """Parser for show memory statistics"""

    cli_command = 'show memory statistics'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<name>\S+) +(?P<head>\w+) +(?P<total>\d+) +'
                         '(?P<used>\d+) +(?P<free>\d+) +'
                         '(?P<lowest>\d+) +(?P<largest>\d+)$')

        p2 = re.compile(r'^Tracekey *: +(?P<tracekey>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            #                 Head    Total(b)     Used(b)     Free(b)   Lowest(b)  Largest(b)
            # Processor  FF86F21010   856541768   355116168   501425600   499097976   501041348
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group.pop('name').lower()
                name_dict = ret_dict.setdefault('name', {}).setdefault(name, {})
                name_dict['head'] = group.pop('head')
                name_dict.update({k:int(v) for k, v in group.items()})
                continue

            # Tracekey : 1#f8e3c2db7822c04e58ce2bd2fc7e476a
            m = p2.match(line)
            if m:
                ret_dict['tracekey'] = m.groupdict()['tracekey']
                continue
        return ret_dict
        