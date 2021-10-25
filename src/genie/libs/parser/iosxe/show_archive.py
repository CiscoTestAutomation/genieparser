''' show_archive.py

IOSXE parsers for the following show commands:
    * show archive
    * show archive config differences
    * show archive config differences <fileA> <fileB>
    * show archive config differences <fileA>
    * show archive config incremental-diffs <fileA>
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# =============================================
# Parser for 'show archive'
# =============================================

class ShowArchiveSchema(MetaParser):
    """
    Schema for show archive
    """

    schema = {
        'archive': {
            'total': int,
            Optional('max_archive_configurations'): int,
            'most_recent_file': str,
            Any(): {
                'file': str,
            },
        }
    }

class ShowArchive(ShowArchiveSchema):
    """ Parser for show archive """

    # Parser for 'show archive'
    cli_command = 'show archive'

    def cli(self,output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # The maximum archive configurations allowed is 10.
            p1 = re.compile(r'^The +maximum +archive +configurations +allowed +is +(?P<max>\d+)\.$')
            m = p1.match(line)
            if m:
                if 'archive' not in ret_dict:
                    ret_dict['archive'] = {}
                ret_dict['archive']['max_archive_configurations'] = int(m.groupdict()['max'])
                continue

            # There are currently 1 archive configurations saved.
            p2 = re.compile(r'^There +are +currently +(?P<total>\d+) +archive +configurations +saved\.$')
            m = p2.match(line)
            if m:
                if 'archive' not in ret_dict:
                    ret_dict['archive'] = {}
                    
                ret_dict['archive']['total'] = int(m.groupdict()['total'])
                continue

            # 1        bootflash:uncfgIntfgigabitethernet0_0_0-Sep-27-15-04-18.414-PDT-0 <- Most Recent
            p3 = re.compile(r'^(?P<num>[0-9]+) +(?P<file>[\w\:\-\.]+)(?P<recent> +\<\- +Most +Recent)?$')
            m = p3.match(line)
            if m:
                num = m.groupdict()['num']
                file = m.groupdict()['file']
                recent = m.groupdict()['recent']

                if 'archive' not in ret_dict:
                    ret_dict['archive'] = {}

                if num not in ret_dict['archive']:
                    ret_dict['archive'][num] = {}

                ret_dict['archive'][num]['file'] = file
                if recent:
                    ret_dict['archive']['most_recent_file'] = file                
                continue

        return ret_dict

# ====================================================
# Parser for 'show archive config differences'
# ====================================================
class ShowArchiveConfigDifferencesSchema(MetaParser):
    """
    Schema for the following commands
    * show archive config differences
    * show archive config differences {fileA} {fileB}
    * show archive config differences {fileA}
    * show archive config incremental-diff {fileA}
    """
    
    schema = {
        Optional('diff'): list,
        Optional('list_of_commands'): list
    }

class ShowArchiveConfigDifferences(ShowArchiveConfigDifferencesSchema):
    """ Parser for the following commands:
        * show archive config differences
        * show archive config differences {fileA} {fileB}
        * show archive config differences {fileA}
    """

    cli_command = [
        'show archive config differences', 
        'show archive config differences {fileA} {fileB}',
        'show archive config differences {fileA}'
    ]

    def cli(self, fileA='', fileB='', cmd='', output=None):
        if output is None:
            # execute command to get output
            if not cmd:
                if fileA:
                    if fileB:
                        command = self.cli_command[1].format(fileA=fileA, fileB=fileB)
                    else:
                        command = self.cli_command[2].format(fileA=fileA)
                else:
                    command = self.cli_command[0]
            else:
                if fileA:
                    command = cmd.format(fileA=fileA)
            out = self.device.execute(command)
        else:
            out = output

        # initial varaiables
        ret_dict = {}
        contextual_found = False
        
        # !Contextual Config Diffs:
        p1 = re.compile(r'^\s*!Contextual +Config +Diffs:$')
        
        # +hostname Router
        # -hostname Test4
        p2 = re.compile(r'^\s*(?P<line_info>(\+|\-)[\w\W]+)$')
        
        # !List of commands:
        p3 = re.compile(r'^\s*!List +of +(C|c)ommands:$')
        
        # Load for five secs: 16%/0%; one minute: 30%; five minutes: 23%
        p4 = re.compile(r'^Load +for +five +secs: +\d+%\/\d+%; +one +minute:' \
            ' +\d+%; +five +minutes: +\d+%$')
        
        # Time source is NTP, 19:16:19.992 EST Thu Sep 15 2016
        # Time source is NTP, *02:20:46.845 EST Thu May 16 2019
        p5 = re.compile(r'^Time +source +is +\w+, +\*?\d+:\d+:\d+\.\d+ +\w+ +' \
            '\w+ +\w+ +\d+ +\d+$')
        
        # test#show archive config incremental-diffs bootflash:A.cfg
        p6 = re.compile(r'^(test#|Device#|Router#)')
        
        # hostname Router3
        p7 = re.compile(r'^\s*(?P<line_info>([\w\W]+))$')

        for line in out.splitlines():
            line = line.strip()
            
            if not cmd:
                if not contextual_found:
                    #!Contextual Config Diffs
                    m = p1.match(line)
                    if m:
                        contextual_found = True
                        contextual_config_diff = ret_dict.setdefault('diff',[])
                        continue
                else:
                    # +hostname Router
                    # -hostname Test4
                    m = p2.match(line)
                    if m:
                        group = m.groupdict()
                        contextual_config_diff.append(group['line_info'])
                        continue
            else:
                # !List of Commands:
                m = p3.match(line)
                if m:
                    incremental_diff = ret_dict.setdefault('list_of_commands',[])
                    continue
                
                # Load for five secs: 16%/0%; one minute: 30%; five minutes: 23%
                m = p4.match(line)
                if m:
                    continue
                
                # Time source is NTP, 19:16:19.992 EST Thu Sep 15 2016
                # Time source is NTP, *02:20:46.845 EST Thu May 16 2019
                m = p5.match(line)
                if m:
                    continue
                
                # test#show archive config incremental-diffs bootflash:A.cfg
                m = p6.match(line)
                if m:
                    continue
                
                # hostname router 192.168.5.2/22
                # end
                m = p7.match(line)
                if m:
                    group = m.groupdict()
                    incremental_diff = ret_dict.setdefault('list_of_commands',[])
                    incremental_diff.append(group['line_info'])
                    continue
        return ret_dict

class ShowArchiveConfigIncrementalDiffs(ShowArchiveConfigDifferences):
    """ Parser for show archive config incremental-diffs <fileA>"""
    
    cli_command = 'show archive config incremental-diffs {fileA}'
    
    def cli(self, fileA, output=None):
        return super().cli(fileA=fileA, cmd=self.cli_command, output=output)

class ShowArchiveLogConfigSchema(MetaParser):

    '''Schema for:
        * show archive log config all
        * schema for show archive log config {include}
    '''
    
    schema = {   
        'idx':{
            int: { 
                'sess' : int,
                'userline' : str,
                'logged_command' : str, 
            }
        }
    } 
     
class ShowArchiveLogConfig(ShowArchiveLogConfigSchema):

    ''' Parser for:
        * show archive log config all
        * show archive log config {include}
    '''

    cli_command = [
        'show archive log config {include}',
        'show archive log config all' 
    ]
        
    def cli(self, include='', output=None):
    
        if output is None:          
            if include:            
                output = self.device.execute(self.cli_command[0].format(include=include))
            else:
                output = self.device.execute(self.cli_command[1])
              
        ret_dict = {}
        
        #idx   sess           user@line      Logged command 
        #610     1        console@console  |  logging enable 
        p1 = re.compile(r'^(?P<idx>\d+)\s+(?P<sess>\d+)\s+(?P<userline>[\w\@]+)\s+\|(\s+)?(?P<logged_command>[\w(\-)?\s]+)$')
        
        for line in output.splitlines():     
            line = line.strip()
            
            #idx   sess           user@line      Logged command 
            #609     1        console@console  | log config            
            m = p1.match(line)                      
            if m: 
                group = m.groupdict()  
                idx = int(group['idx'])              
                idx_dict = ret_dict.setdefault('idx', {}).setdefault(idx, {})
                idx_dict['sess'] = int(group['sess'])                    
                idx_dict['userline'] = group['userline']  
                idx_dict['logged_command'] = group['logged_command']
                continue
                
        return ret_dict
        
        
class ShowArchiveLogStatisticsSchema(MetaParser): 

    '''schema for:
       * show archive log config statistics
    '''
    
    schema = {
        'log':{
            Any():{           
                'num_entries_in_log': int,
                'memory_held_bytes': int, 
                'memory_allocated_bytes': int, 
                'memory_free_bytes': int
            }
        }
    }
            
                        
class ShowArchiveLogStatistics(ShowArchiveLogStatisticsSchema):

    ''' Parser for: 
        * show archive log config statistics'''

    cli_command = 'show archive log config statistics'
    
    def cli(self,output=None):
    
        if output is None:
            output = self.device.execute(self.cli_command)
 
        ret_dict = {}  
         
        #Config Log Session Info:
        #Config Log log-queue Info:
        p1  =  re.compile(r'^Config Log (?P<log>[\s\w(\-)?]+\:)$')

        #Number of sessions being tracked: 1
        #Number of entries in the log-queue: 472
        p2 = re.compile(r'^Number of [\w\s(\-)?]+: +(?P<num_entries_in_log>[\d]+)$')

        #Memory being held: 3934 bytes
        #Memory being held by the log-queue: 186617 bytes
        p3 = re.compile(r'^Memory being [\w\s(\-)?]+\: (?P<memory_held_bytes>[\d]+)[\w\s]+$')

        #Total memory allocated for session tracking: 11793 bytes
        #Total memory allocated for log entries: 186617 bytes
        p4 = re.compile(r'^Total memory allocated for [\w\s]+: +(?P<memory_allocated_bytes>[\d]+)[\w\s]+$')
        
        #Total memory freed from session tracking: 7859 bytes
        #Total memory freed from log entries: 0 bytes
        p5 = re.compile(r'^Total memory freed from [\w\s]+: +(?P<memory_free_bytes>[\d]+)[\w\s]+$')
        
        for line in output.splitlines():
            line=line.strip()
            
            #Config Log Session Info:
            #Config Log log-queue Info:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                log=group['log']
                root_dict = ret_dict.setdefault('log', {}).setdefault(log, {})
                continue
            
            #Number of sessions being tracked: 1
            #Number of entries in the log-queue: 472
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict.setdefault('num_entries_in_log', int(group['num_entries_in_log']))
                continue
                
            #Memory being held: 3934 bytes
            #Memory being held by the log-queue: 186617 bytes           
            m = p3.match(line)                                                                                                                                               
            if m:
                group = m.groupdict() 
                root_dict.setdefault('memory_held_bytes', int(group['memory_held_bytes']))
                continue
            
            #Total memory allocated for session tracking: 11793 bytes
            #Total memory allocated for log entries: 186617 bytes
            m = p4.match(line)
            if m:
                group = m.groupdict() 
                root_dict.setdefault('memory_allocated_bytes', int(group['memory_allocated_bytes']))
                continue
            
            #Total memory freed from session tracking: 7859 bytes
            #Total memory freed from log entries: 0 bytes
            m = p5.match(line)
            if m:
                group = m.groupdict() 
                root_dict.setdefault('memory_free_bytes', int(group['memory_free_bytes']))
                continue
        
        return ret_dict

