"""show_alignment.py

IOS parsers for the following show commands:
    * show alignment
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
                                         Use, \
                                         ListOf


class ShowAlignmentSchema(MetaParser):
    """Schema for show alignment"""
    schema = {
        Optional('alignment_data'): {
            'software_version': str,
            'compiled_date': str,
            'compiled_by': str,
            Optional('total_corrections'): int,
            Optional('recorded_corrections'): int,
            Optional('reads'): int,
            Optional('writes'): int,
            Optional('alignment_records'): {
                Any(): {  # address
                    'count': int,
                    'access_type': str,
                    'operation': str,
                    'traceback': ListOf(str),
                }
            }
        },
        Optional('spurious_memory'): {
            Optional('total_spurious_accesses'): int,
            Optional('recorded_spurious_accesses'): int,
            Optional('spurious_records'): {
                Any(): {  # address
                    'count': int,
                    'traceback': ListOf(str),
                }
            }
        },
        Optional('no_alignment_data'): bool,
        Optional('no_spurious_references'): bool,
    }


class ShowAlignment(ShowAlignmentSchema):
    """Parser for show alignment"""

    cli_command = 'show alignment'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
            
        # initial return dictionary
        ret_dict = {}

        # Regex patterns
        # No alignment data recorded
        p1 = re.compile(r'^No alignment data recorded$')
        
        # No spurious memory references have been recorded
        p2 = re.compile(r'^No spurious memory references have been recorded\.?$')
        
        # Alignment data for:
        p3 = re.compile(r'^Alignment data for:?\s*$')
        
        # RSP Software (RSP-ISV-M), Version 11.3(3a), RELEASE SOFTWARE (fc1)
        p4 = re.compile(r'^(?P<software>.*Software.*), Version (?P<version>[\d\.\(\)a-zA-Z]+), (?P<release>.*)$')
        
        # Compiled Fri 01-May-98 18:28 by phanguye
        p5 = re.compile(r'^Compiled (?P<date>.*) by (?P<compiled_by>\S+)$')
        
        # Total Corrections 6, Recorded 2, Reads 6, Writes 0
        p6 = re.compile(r'^Total Corrections (?P<corrections>\d+), Recorded (?P<recorded>\d+), Reads (?P<reads>\d+), Writes (?P<writes>\d+)$')
        
        # No alignment data has been recorded
        p7 = re.compile(r'^No alignment data has been recorded\.?$')
        
        # 60EF3765   3      32bit   read  0x60262474 0x601AC594 0x601AC580
        p8 = re.compile(r'^(?P<address>[0-9A-Fa-f]+)\s+(?P<count>\d+)\s+(?P<access_type>\S+)\s+(?P<operation>\S+)\s+(?P<traceback>.*)$')
        
        # Total Spurious Accesses 26, Recorded 14
        p9 = re.compile(r'^Total Spurious Accesses (?P<total>\d+), Recorded (?P<recorded>\d+)$')
        
        # 1DC8      1  0x60299BF4 0x6061B010 0x60334FB8 0x6061D8E0
        p10 = re.compile(r'^(?P<address>[0-9A-Fa-f]+)\s+(?P<count>\d+)\s+(?P<traceback>.*)$')
        
        # 0x6062065C 0x60519A70 0x6051913C 0x6050BE88 [Continuation of traceback]
        p11 = re.compile(r'^\s+(?P<traceback>.*)$')

        current_traceback = []
        last_address = None
        is_spurious_section = False
        
        for line in out.splitlines():
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
                
            # No alignment data recorded
            m = p1.match(line)
            if m:
                ret_dict['no_alignment_data'] = True
                continue
                
            # No spurious memory references have been recorded
            m = p2.match(line)
            if m:
                ret_dict['no_spurious_references'] = True
                continue
                
            # Alignment data for:
            m = p3.match(line)
            if m:
                is_spurious_section = False
                continue
                
            # RSP Software (RSP-ISV-M), Version 11.3(3a), RELEASE SOFTWARE (fc1)
            m = p4.match(line)
            if m:
                alignment_dict = ret_dict.setdefault('alignment_data', {})
                software_info = f"{m.groupdict()['software']}, Version {m.groupdict()['version']}, {m.groupdict()['release']}"
                alignment_dict['software_version'] = software_info
                continue
                
            # Compiled Fri 01-May-98 18:28 by phanguye
            m = p5.match(line)
            if m:
                alignment_dict = ret_dict.setdefault('alignment_data', {})
                alignment_dict['compiled_date'] = m.groupdict()['date']
                alignment_dict['compiled_by'] = m.groupdict()['compiled_by']
                continue
                
            # Total Corrections 6, Recorded 2, Reads 6, Writes 0
            m = p6.match(line)
            if m:
                alignment_dict = ret_dict.setdefault('alignment_data', {})
                alignment_dict['total_corrections'] = int(m.groupdict()['corrections'])
                alignment_dict['recorded_corrections'] = int(m.groupdict()['recorded'])
                alignment_dict['reads'] = int(m.groupdict()['reads'])
                alignment_dict['writes'] = int(m.groupdict()['writes'])
                continue
                
            # No alignment data has been recorded
            m = p7.match(line)
            if m:
                alignment_dict = ret_dict.setdefault('alignment_data', {})
                # This indicates no alignment records exist
                continue
                
            if 'Total Spurious Accesses' in line:
                is_spurious_section = True
                # Total Spurious Accesses 26, Recorded 14
                m = p9.match(line)
                if m:
                    spurious_dict = ret_dict.setdefault('spurious_memory', {})
                    spurious_dict['total_spurious_accesses'] = int(m.groupdict()['total'])
                    spurious_dict['recorded_spurious_accesses'] = int(m.groupdict()['recorded'])
                continue
                
            if not is_spurious_section:
                # 60EF3765   3      32bit   read  0x60262474 0x601AC594 0x601AC580 
                m = p8.match(line)
                if m:
                    alignment_dict = ret_dict.setdefault('alignment_data', {})
                    records_dict = alignment_dict.setdefault('alignment_records', {})
                    address = m.groupdict()['address']
                    last_address = address
                    
                    record_dict = records_dict.setdefault(address, {})
                    record_dict['count'] = int(m.groupdict()['count'])
                    record_dict['access_type'] = m.groupdict()['access_type']
                    record_dict['operation'] = m.groupdict()['operation']
                    
                    # Parse traceback addresses
                    traceback_str = m.groupdict()['traceback']
                    traceback_addrs = traceback_str.split()
                    record_dict['traceback'] = traceback_addrs
                    current_traceback = traceback_addrs
                    continue
            else:
                # 1DC8      1  0x60299BF4 0x6061B010 0x60334FB8 0x6061D8E0
                m = p10.match(line)
                if m:
                    spurious_dict = ret_dict.setdefault('spurious_memory', {})
                    records_dict = spurious_dict.setdefault('spurious_records', {})
                    address = m.groupdict()['address']
                    last_address = address
                    
                    record_dict = records_dict.setdefault(address, {})
                    record_dict['count'] = int(m.groupdict()['count'])
                    
                    # Parse traceback addresses
                    traceback_str = m.groupdict()['traceback']
                    traceback_addrs = traceback_str.split()
                    record_dict['traceback'] = traceback_addrs
                    current_traceback = traceback_addrs
                    continue
                    
            # 0x6062065C 0x60519A70 0x6051913C 0x6050BE88
            m = p11.match(line)
            if m and last_address:
                traceback_str = m.groupdict()['traceback']
                traceback_addrs = traceback_str.split()
                current_traceback.extend(traceback_addrs)
                
                # Update the appropriate record
                if not is_spurious_section and 'alignment_data' in ret_dict and 'alignment_records' in ret_dict['alignment_data']:
                    ret_dict['alignment_data']['alignment_records'][last_address]['traceback'] = current_traceback
                elif is_spurious_section and 'spurious_memory' in ret_dict and 'spurious_records' in ret_dict['spurious_memory']:
                    ret_dict['spurious_memory']['spurious_records'][last_address]['traceback'] = current_traceback
                continue

        return ret_dict
