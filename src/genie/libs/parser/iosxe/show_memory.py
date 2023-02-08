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

class ShowMemoryDebugLeaksChunksSchema(MetaParser):
    '''
       Schema for 
           * show memory debug leaks chunks
    '''
    schema = {
        Optional('tracekey'): str,
        'memory': {
            str: {
                Optional(str): {
                    Optional('size'): int,
                    Optional('parent'): str,
                    Optional('name'): str,
                    Optional('alloc_pc'): str,
                },
            }
        }
    }

class ShowMemoryDebugLeaksChunks(ShowMemoryDebugLeaksChunksSchema):
    '''
       Parser for
           * show memory debug leaks chunks
    '''

    cli_command = 'show memory debug leaks chunks'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Tracekey : 1#cc860b27cccff1817bea87604823f7be
        p1 = re.compile(r'^Tracekey *:\s+(?P<tracekey>\S+)$')

        # Processor memory
        # reserve Processor memory
        # lsmpi_io memory
        p2 = re.compile(r'^(?P<memory>[\w\s]* memory)$')

        # 7F129EC22658    76 7F129EF46108 (MallocLite)     :55D8C0A61000+E0D8F11
        p3 = re.compile(r'^(?P<address>\S+)\s+(?P<size>\d+)\s+(?P<parent>\S+)\s+\((?P<name>\S+)\)\s+(?P<alloc_pc>\S+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Tracekey : 1#cc860b27cccff1817bea87604823f7be
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
                memory = memories.setdefault(group['memory'].lower().replace(' ','_'), {})
                continue

            # 7F129EC22658    76 7F129EF46108 (MallocLite)     :55D8C0A61000+E0D8F11
            m = p3.match(line)
            if m:
                group = m.groupdict()
                address = memory.setdefault(group['address'], {})
                address.update({
                    'size' : int(group['size']),
                    'parent' : group['parent'],
                    'name' : group['name'],
                    'alloc_pc' : group['alloc_pc'],
                })
                continue
        
        return ret_dict

# ======================================================================================
# Parser Schema for 'show memory dead total'
# ======================================================================================

class ShowMemoryDeadTotalSchema(MetaParser):
    """Schema for "show memory dead total" """

    schema = {
            'memory': {
                'tracekey': str,
                    Any(): {
                            'head': str,
                            'total_in_bits': int,
                            'used_in_bits': int,
                            'free_in_bits': int,
                            'lowest_in_bits': int,
                            'largest_in_bits': int
                    },
                    'dynamic_heap': {
                            'dynamic_heap_limit_in_megabyte': int,
                            'use': int
                    },
                    'dead_proc': {
                             Any(): {
                                    Any(): {
                                            'total': int,
                                            'count': int,
                                            'name': str
                                    }
                             },
                             'reserve_processor': {},
                             'lsmpi_io': {}
                    }
            } 
    }

# ================================================================================
# Parser for 'show memory dead total'
# ================================================================================

class ShowMemoryDeadTotal(ShowMemoryDeadTotalSchema):
    """ parser for "show memory dead total" """

    cli_command = "show memory dead total"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Tracekey : 1#50bb0560a294e78d5c720c4dd666d9f5
        p1 = re.compile(r'^Tracekey *: +(?P<tracekey>\S+)$')

        # Processor  7F5B2B4FD048   3791419980   281368020   3510051960   645435404   3145727908
        p2 = re.compile(r'^Processor\s+(?P<head>\w+)\s+(?P<total>\d+)\s+(?P<used>\d+)\s+(?P<free>\d+)\s+(?P<lowest>\d+)\s+(?P<largest>\d+)$')

        # reserve P  7F5B2B4FD0A0      102404          92      102312      102312      102312
        p3 = re.compile(r'^reserve\s+P\s+(?P<head>\w+)\s+(?P<total>\d+)\s+(?P<used>\d+)\s+(?P<free>\d+)\s+(?P<lowest>\d+)\s+(?P<largest>\d+)$')

        #  lsmpi_io  7F5B292CD1A8     6295128     6294304         824         824         412
        p4 = re.compile(r'^lsmpi_io\s+(?P<head>\w+)\s+(?P<total>\d+)\s+(?P<used>\d+)\s+(?P<free>\d+)\s+(?P<lowest>\d+)\s+(?P<largest>\d+)$')

        # Dynamic heap limit(MB) 3000      Use(MB) 0
        p5 = re.compile(r'^Dynamic\s+heap\s+limit\(MB\)\s+(?P<dynamic_heap_limit>\d+)\s+Use\(MB\)\s+(?P<use>\d+)$')
        
        # Dead Proc Summary for: Processor
        # Dead Proc Summary for: reserve Processor
        # Dead Proc Summary for: lsmpi_io
        p6 = re.compile(r'^Dead\sProc\sSummary\sfor:\s(?P<name>[A-Za-z _]+)$')
        
        # # 10.0.0.1        80  1234   Placeholder_proc        Placeholder_name               Placeholder_pc
        # p3 = re.compile(r'^(?P<address>\S+) +(?P<size>\d+) +(?P<pid>\d+) +'
        #               r'(?P<alloc_proc>\S+) +(?P<name>\S+) +(?P<alloc_pc>.*)$')
        
        p7 = re.compile(r'^(?P<total>\d+)\s+(?P<count>\d+)\s+(?P<name>[A-Za-z_0-9:-]+ ?[A-Za-z_0-9-:]+ ?[A-Za-z_0-9:-]+ ?[A-Za-z_:0-9]+)\s+:(?P<pc>[A-Z0-9+]+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            # Tracekey : 1#50bb0560a294e78d5c720c4dd666d9f5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                memory_dict = ret_dict.setdefault('memory',{})
                memory_dict['tracekey'] = group['tracekey']
                continue

            # Processor  7F5B2B4FD048   3791419980   281368020   3510051960   645435404   3145727908
            m = p2.match(line)
            if m:
                group = m.groupdict()
                processor_dict = memory_dict.setdefault('processor',{})
                processor_dict['head'] = group['head']
                processor_dict['total_in_bits'] = int(group['total'])
                processor_dict['used_in_bits'] = int(group['used'])
                processor_dict['free_in_bits'] = int(group['free'])
                processor_dict['lowest_in_bits'] = int(group['lowest'])
                processor_dict['largest_in_bits'] = int(group['largest'])
                continue
            
            # reserve P  7F5B2B4FD0A0      102404          92      102312      102312      102312
            m = p3.match(line)
            if m:
                group = m.groupdict()
                reserve_dict = memory_dict.setdefault('reserve_p',{})
                reserve_dict['head'] = group['head']
                reserve_dict['total_in_bits'] = int(group['total'])
                reserve_dict['used_in_bits'] = int(group['used'])
                reserve_dict['free_in_bits'] = int(group['free'])
                reserve_dict['lowest_in_bits'] = int(group['lowest'])
                reserve_dict['largest_in_bits'] = int(group['largest'])
                continue
            
            # lsmpi_io  7F5B292CD1A8     6295128     6294304         824         824         412
            m = p4.match(line)
            if m:
                group = m.groupdict()
                lsmpi_io_dict = memory_dict.setdefault('lsmpi_io',{})
                lsmpi_io_dict['head'] = group['head']
                lsmpi_io_dict['total_in_bits'] = int(group['total'])
                lsmpi_io_dict['used_in_bits'] = int(group['used'])
                lsmpi_io_dict['free_in_bits'] = int(group['free'])
                lsmpi_io_dict['lowest_in_bits'] = int(group['lowest'])
                lsmpi_io_dict['largest_in_bits'] = int(group['largest'])
                continue
            
            # Dynamic heap limit(MB) 3000      Use(MB) 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                dynamic_heap_dict = memory_dict.setdefault('dynamic_heap',{})
                dynamic_heap_dict['dynamic_heap_limit_in_megabyte'] = int(group['dynamic_heap_limit'])
                dynamic_heap_dict['use'] = int(group['use'])
                continue
            
            # Dead Proc Summary for: Processor
            # Dead Proc Summary for: reserve Processor
            # Dead Proc Summary for: lsmpi_io
            m = p6.match(line)
            if m:
                group = m.groupdict()
                name  = group['name'].lower().replace(' ','_')
                dead_proc_dict = memory_dict.setdefault('dead_proc',{}).setdefault(name, {})
                continue

            # Total      Count     Name               PC
            # 1818512      96  Virtual Exec           :56306D5BA000+5ED0DFD
            # 1648000     100  ch_check_profile_url   :56306D5BA000+6C2D241

            m = p7.match(line)
            if m:
                group = m.groupdict()
                pc_dict = dead_proc_dict.setdefault(group['pc'], {})
                pc_dict['total'] = int(group['total'])
                pc_dict['count'] = int(group['count'])
                pc_dict['name'] = group['name']
                continue

        return ret_dict

# ======================================================================================
# Parser Schema for 'show memory platform information'
# ======================================================================================

class ShowMemoryPlatformInformationSchema(MetaParser):
    """Schema for "show memory platform information" """

    schema = {
	'memory_platform_info': {
		'virtual_memory': int,
		'pages_resident': int,
		'major_page_faults': int,
		'minor_page_faults': int,
		'architecture': str,
		'memory_(kb)': {
			'physical': int,
			'total': int,
			'used': int,
			'free': int,
			'active': int,
			'inactive': int,
			'inact_dirty': int,
			'inact_clean': int,
			'dirty': int,
			'anonpages': int,
			'bounce': int,
			'cached': int,
			'commit_limit': int,
			'committed_as': int,
			'high_total': int,
			'high_free': int,
			'low_total': int,
			'low_free': int,
			'mapped': int,
			'nfs_unstable': int,
			'page_tables': int,
			'slab': int,
			'writeback': int,
			'hugepages_total': int,
			'hugepages_free': int,
			'hugepages_rsvd': int,
			'hugepage_size': int
		},
		'swap_(kb)': {
			'total': int,
			'used': int,
			'free': int,
			'cached': int
		},
		'buffers_(kb)': int,
		'load_average': {
			'1_min': float,
			'5_min': float,
			'15_min': float
		}
	}
}

# ================================================================================
# Parser for 'show memory platform information'
# ================================================================================

class ShowMemoryPlatformInformation(ShowMemoryPlatformInformationSchema):
    """ parser for "show memory platform information" """

    cli_command = "show memory platform information"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
    
        # Virtual memory   : 49030533120
        p1 = re.compile(r'^(?P<name>[A-Z][a-z]+\s+[a-z]+)\s+:\s(?P<size>\d+)$')
        
        # Major page faults: 6958
        p2 = re.compile(r'^(?P<name>[A-Z][a-z]+\s+\w+\s+\w+):\s(?P<size>\d+)$')
        
        # Architecture     : x86_64
        p3 = re.compile(r'^Architecture\s+:\s+(?P<architecture>\w+)$')
        
        # Memory (kB)
        p4 = re.compile(r'^(?P<block_name>\w+(\s\w+|\s+\(\w+\)))$')
        
        # Physical       : 7748808
        p5 = re.compile(r'^(?P<name>[A-Za-z0-9-]+|[A-Za-z]+(-| )+\w+)(\s+:|:)\s+(?P<size>\d+|\d.+)$')
        
        # Buffers (kB)     : 389964
        p6 = re.compile(r'^(?P<block_name>\w+(\s\w+|\s+\(\w+\)))\s+:\s+(?P<buffer>\d+)$')
        
       
        for line in output.splitlines():
            line = line.strip()
            
            # Virtual memory   : 49030533120
            m = p1.match(line)
            if m:
                group = m.groupdict()
                memory_platform_info_dict = parsed_dict.setdefault('memory_platform_info', {})
                memory_platform_info_dict[(group['name'].lower()).replace(' ','_')] = int(group['size'])
                continue
            
            # Major page faults: 6958
            m = p2.match(line)
            if m:
                group = m.groupdict()
                memory_platform_info_dict[(group['name'].lower()).replace(' ','_')]= int(group['size'])
                continue

            # Architecture     : x86_64
            m = p3.match(line)
            if m:
                group = m.groupdict()
                memory_platform_info_dict['architecture'] = group['architecture']
                continue
            
            # Memory (kB)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                block_dict = memory_platform_info_dict.setdefault((group['block_name']).lower().replace(' ','_'),{})
                block_name = group['block_name']
                continue
            
            # Physical       : 7748808
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if block_name == 'Load Average':
                   block_dict[((group['name']).lower()).replace('-','_').replace(' ','_')] = float(group['size'])
                else:
                    block_dict[((group['name']).lower()).replace('-','_').replace(' ','_')] = int(group['size'])
                continue
            
            # Buffers (kB)     : 389964
            m = p6.match(line)
            if m:
                group = m.groupdict()
                memory_platform_info_dict[group['block_name'].lower().replace(' ','_')] = int(group['buffer'])
                continue
            
        return parsed_dict


class ShowMemoryDebugIncrementalLeaksSchema(MetaParser):
    '''schema for
        * show memory debug incremental leaks
    '''

    schema = {
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

class ShowMemoryDebugIncrementalLeaks(ShowMemoryDebugLeaksSchema):                                                            

    '''parser for
        * show memory debug incremental leaks
    '''

    cli_command = 'show memory debug incremental leaks'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Processor memory
        # reserve Processor memory
        # lsmpi_io memory
        p1 = re.compile(r'^(?P<memory>[\w\s]*memory)$')

        # 10.0.0.1        80  1234   Placeholder_proc        Placeholder_name               Placeholder_pc
        p2 = re.compile(r'^(?P<address>\S+) +(?P<size>\d+) +(?P<pid>\d+) +'
                       r'(?P<alloc_proc>\S+) +(?P<name>\S+) +(?P<alloc_pc>.*)$')

        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()


            # Processor memory
            # reserve Processor memory
            # lsmpi_io memory
            m = p1.match(line)
            if m:
                group = m.groupdict()
                memories = ret_dict.setdefault('memory', {})
                memory = memories.setdefault(group['memory'].lower().replace(' ', '_'), {})
                continue


            # 7F7B27188F98 448 86 IOSD ipc task IOSD ipc task :560DB012A000+A66ECD0 
            # 7F7B275FE3D0 360 86 IOSD ipc task IOSD ipc task :560DB012A000+A66ECD0 
            m = p2.match(line)
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
