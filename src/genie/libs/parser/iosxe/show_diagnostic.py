"""show_diagnostics.py
   supported commands:
     * show diagnostic events
     * show diagnostic description module {include} test all
     * show diagnostic content module {mod_num}
     * show diagnostic result module {mod_num} test {include} detail
     
"""


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowDiagnosticEventSchema(MetaParser):
    """
    Schema for show diagnostic events 
    """

    schema = {
        'events':{
            Any():{
                Any():{
                    'status':bool,
                    'card':str,
                    'type':str,
                },
            },  
        }  
    }

class ShowDiagnosticEvent(ShowDiagnosticEventSchema):
    """ Parser for show diagnostic events """

    # Parser for 'show diagnostic events'
    cli_command = 'show diagnostic events'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)
            
        # initial variables
        ret_dict = {}
        
        #10/18 11:45:38.819 I  [1]    TestPhyLoopback Passed
        p1 = re.compile(r'^(?P<timestamp>[\d/: .]+) +(?P<types>\w+) +\[(?P<card>\d+)\] +(?P<name>\w+) +(?P<status>\w+)$')
        
        for line in output.splitlines():
            line = line.strip()
            
            #10/15 13:02:21.495 E  [1]    TestFantray Passed
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict1 = ret_dict.setdefault('events',{}).setdefault(group['name'],{}).setdefault(group['timestamp'],{})
                status = True if \
                    group['status'] == 'Passed' else\
                    False
                root_dict1.setdefault('status',status)
                root_dict1.setdefault('card',group['card'])
                root_dict1.setdefault('type',group['types'])
                continue
             
        return ret_dict 
        
        
class ShowDiagnosticDescriptionModuleTestAllSchema(MetaParser):
    """
    Schema for show diagnostic description module {include} test all
    """

    schema = {
        'diag_test':{
            'module':{
                int:{
                    Any():str,
                },
            },
        },        
    }


class ShowDiagnosticDescriptionModuleTestAll(ShowDiagnosticDescriptionModuleTestAllSchema):
    """ Parser for show diagnostic description module {include} test all"""

    cli_command = 'show diagnostic description module {include} test all'

    def cli(self, include, output=None): 
        if output is None:
            output = self.device.execute(self.cli_command.format(include=include))

        # initial variables
        ret_dict = {}
        
        # TestPhyLoopback :
        p1 = re.compile('^(?P<test_name>\w+)\s+\:$')
        
        # The PHY Loopback test verifies the PHY level loopback
        p2 = re.compile('^(?P<description>[\w\s\.,-]+)$')

        for line in output.splitlines():
            line=line.strip()
            
            root_dict1 = ret_dict.setdefault('diag_test',{}).setdefault('module',{}).setdefault(int(include),{})
            
            # TestPhyLoopback :
            m=p1.match(line)
            if m:
                group1=m.groupdict()
                root_dict1[group1['test_name']] = ''
                continue
            
            # The PHY Loopback test verifies the PHY level loopback
       
            m=p2.match(line)
            if m:
                group=m.groupdict()
                root_dict1[group1['test_name']] = root_dict1[group1['test_name']] + group['description']
                continue
                
        return ret_dict
        
        
class ShowDiagnosticContentModuleSchema(MetaParser):
    """
    Schema for show diagnostic content module {mod_num}
    """

    schema = {
        'diag_test':{
            'module':{
                int:{
                    Any():{
                       'test_id' : int,
                        'attributes':str,
                        'test_interval':str,
                        'threshold':str,
                    },
                },
            },
        }
    }


class ShowDiagnosticContentModule(ShowDiagnosticContentModuleSchema):
    """ Parser for show diagnostic content module {mod_num}"""

    # Parser for 'show diagnostic content module {mod_num}'
    cli_command = 'show diagnostic content module {mod_num}'

    def cli(self, mod_num, output=None): 

        if output is None:
            output = self.device.execute(self.cli_command.format(mod_num=mod_num))
        
        # initial variables
        ret_dict = {}
        
        #1) TestGoldPktLoopback -------------> *BPN*X**I       not configured  n/a
        p1 = re.compile('^(?P<test_id>\d+)\) (?P<test_name>\w+) -+> (?P<attributes>\S+)\s+(?P<test_interval>(not configured)|[\d \:\.]+)\s+(?P<threshold>(n\/a)|\d+)$')

        for line in output.splitlines():
            line = line.strip()
            
            root_dict1 = ret_dict.setdefault('diag_test',{}).setdefault('module',{}).setdefault(int(mod_num),{})
            
            #1) TestGoldPktLoopback -------------> *BPN*X**I       not configured  n/a
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict1 = root_dict1.setdefault(group['test_name'], {})
                test_name = group.pop('test_name')
                root_dict1.update({k: v for k, v in group.items()})
                root_dict1['test_id']=int(group['test_id'])
                continue    
                
        return ret_dict
         
        
class ShowDiagnosticResultModuleTestDetailSchema(MetaParser):
    """
    Schema for show diagnostic result module {mod_num} test {include} detail 
    show diagnostic result module {mod_num} test {include} detail 
    """

    schema = {
        'diag_tests':{
            'module':{
                int:{
                    Any():{
                        'test_id' : int,
                        'result' : str,
                        'error_code':str,
                        'total_run_count':int,
                        'testing_type':str,
                        'test_execution_time':str,
                        'first_test_failure':str,
                        'last_test_failure':str,
                        'last_test_pass':str,
                        'total_failure_count':int,
                        'consecutive_failure_count':int,
                    }
                }
            }
        }
    }


class ShowDiagnosticResultModuleTestDetail(ShowDiagnosticResultModuleTestDetailSchema):
    """ Parser for show diagnostic result module {mod_num} test {include} detail """

    # Parser for 'show diagnostic result module {mod_num} test {include} detail'
    cli_command = 'show diagnostic result module {mod_num} test {include} detail'

    def cli(self, mod_num, include, output=None): 

        if output is None:
           
                output = self.device.execute(self.cli_command.format(mod_num=mod_num,include=include))
               
        # initial variables
        ret_dict = {}

        #Error code ------------------> 1 (DIAG_FAILURE)
        p1 = re.compile('^Error code [-> ]+(?P<error_code>(.*))$')
        
        #Total run count -------------> 8160 
        p2 = re.compile('^Total run count [-> ]+(?P<total_run_count>\d+)$')
        
        #Last test testing type ------> Health Monitoring
        p3 = re.compile('^Last test testing type[-> ]+(?P<testing_type>[A-Z a-z]+)$')
        
        #Last test execution time ----> Oct 15 2019 13:02:21 
        p4 = re.compile('^Last \w+ execution \w+[ ->]+(?P<test_execution_time>(\w+ \d+ \d+ \d+:\d+:\d+)|n/a)$')
        
        #First test failure time -----> Oct 06 2019 01:30:37 
        p5 = re.compile('^First test failure time [-> ]+(?P<first_test_failure>(\w+ \d+ \d+ \d+:\d+:\d+)|n/a)$')
        
        #Last test failure time ------> Oct 15 2019 13:02:21
        p6 = re.compile('^Last test failure time[-> ]+(?P<last_test_failure>(\w+ \d+ \d+ \d+:\d+:\d+)|n/a)$')
        
        #Last test pass time ---------> n/a 
        p7 = re.compile('^Last test pass time [ ->]+(?P<last_test_pass>(\w+ \d+ \d+ \d+:\d+:\d+)|n/a)$')
        
        #Total failure count ---------> 8160 
        p8 = re.compile('^Total failure count [-> ]+(?P<total_failure_count>\d+)$')
        
        #Consecutive failure count ---> 8160 
        p9 = re.compile('^Cons\w+ fail\w+ \w+[ ->]+ (?P<consecutive_failure_count>\d+)$')
        
        #2) TestFantray ---------------------> .
        p10 = re.compile('^(?P<test_id>\d+)\) \w+ -+> (?P<result>.*)$')

        for line in output.splitlines():
            line = line.strip()
            
            root_dict1 = ret_dict.setdefault('diag_tests',{}).setdefault('module',{}).setdefault(int(mod_num),{}).setdefault(include,{})
            
            #Error code ------------------> 1 (DIAG_FAILURE)
            m = p1.match(line)
            if m:
               root_dict1.setdefault('error_code',m.group('error_code'))
               continue
               
            #Total run count -------------> 8160 
            m = p2.match(line)
            if m:
               root_dict1.setdefault('total_run_count',int(m.group('total_run_count')))
               continue
               
            #Last test testing type ------> Health Monitoring
            m = p3.match(line)
            if m:
               root_dict1.setdefault('testing_type',m.group('testing_type'))
               continue
               
            #Last test execution time ----> Oct 15 2019 13:02:21 
            m = p4.match(line)
            if m:
               root_dict1.setdefault('test_execution_time',m.group('test_execution_time'))
               continue
               
            #First test failure time -----> Oct 06 2019 01:30:37 
            m = p5.match(line)
            if m: 
               root_dict1.setdefault('first_test_failure',m.group('first_test_failure'))
               continue
               
            #Last test failure time ------> Oct 15 2019 13:02:21
            m = p6.match(line)
            if m:
               root_dict1.setdefault('last_test_failure',m.group('last_test_failure'))
               continue
               
            #Last test pass time ---------> n/a 
            m = p7.match(line)
            if m:
               root_dict1.setdefault('last_test_pass',m.group('last_test_pass'))
               continue
               
            #Total failure count ---------> 8160 
            m = p8.match(line)
            if m:
               root_dict1.setdefault('total_failure_count',int(m.group('total_failure_count')))
               continue
               
            #Consecutive failure count ---> 8160 
            m = p9.match(line)
            if m:
               root_dict1.setdefault('consecutive_failure_count',int(m.group('consecutive_failure_count')))
               continue
              
            #2) TestFantray ---------------------> .
            m = p10.match(line)
            if m:
                group=m.groupdict()
                if group['result']==".":
                    result = "Passed"
                elif group['result']=="F":
                    result = "Failed"
                else:
                    result = "Untested"
                root_dict1.setdefault('test_id',int(group['test_id']))
                root_dict1.setdefault('result',result)
                continue
               
        return ret_dict