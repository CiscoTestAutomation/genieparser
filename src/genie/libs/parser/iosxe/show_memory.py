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
    exclude = ['free', 'used']

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
            
        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<name>\S+( \w)?) +(?P<head>\w+) +(?P<total>\d+) +'
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
        

class ShowMemoryDebugLeaksSchema(MetaParser):
    '''schema for
        * show memory debug leaks
    '''

    schema = {
        Optional('tracekey'): str,
        'memory': {
            str: {
                Optional(str): {
                    'size': int,
                    'pid': int,
                    'alloc_proc': str,
                    'name': str,
                    'alloc_pc': str,
                }
            }
        }
    }

class ShowMemoryDebugLeaks(ShowMemoryDebugLeaksSchema):                                                            

    '''parser for
        * show memory debug leaks
    '''

    cli_command = 'show memory debug leaks'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Tracekey : 1#50bb0560a294e78d5c720c4dd666d9f5
        p1 = re.compile(r'^Tracekey *: +(?P<tracekey>\S+)$')

        # Processor memory
        # reserve Processor memory
        # lsmpi_io memory
        p2 = re.compile(r'^(?P<memory>[\w\s]*memory)$')

        # 10.0.0.1        80  1234   Placeholder_proc        Placeholder_name               Placeholder_pc
        p3 = re.compile(r'^(?P<address>\S+) +(?P<size>\d+) +(?P<pid>\d+) +'
                       r'(?P<alloc_proc>\S+) +(?P<name>\S+) +(?P<alloc_pc>.*)$')

        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()

            # Tracekey : 1#50bb0560a294e78d5c720c4dd666d9f5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tracekey'] = group['tracekey']
                continue

            # Processor memory
            # reserve Processor memory
            # lsmpi_io memory
            m = p2.match(line)
            if m:
                group = m.groupdict()
                memories = ret_dict.setdefault('memory', {})
                memory = memories.setdefault(group['memory'].lower().replace(' ', '_'), {})
                continue


            # 7F7B27188F98 448 86 IOSD ipc task IOSD ipc task :560DB012A000+A66ECD0 
            # 7F7B275FE3D0 360 86 IOSD ipc task IOSD ipc task :560DB012A000+A66ECD0 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                address = memory.setdefault(group['address'], {})
                address.update({
                    'size': int(group['size']),
                    'pid': int(group['pid']),
                    'alloc_proc': group['alloc_proc'],
                    'name': group['name'],
                    'alloc_pc': group['alloc_pc'],
                })
                continue

        return ret_dict
