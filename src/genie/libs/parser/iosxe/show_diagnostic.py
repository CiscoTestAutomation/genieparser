"""show_diagnostics.py
   supported commands:
     * show diagnostic events
     * show diagnostic description module {include} test all
     * show diagnostic content module {mod_num}
     * show diagnostic result module {mod_num} test {include} detail
     * show diagnostic result switch {switch_number} test {include} detail
     * show diagnostic post
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
                        Optional('port_status'):{
                            int: str
                            },
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
        list1 = []
        list2 = []
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
        #3) DiagPhyLoopbackTest:
        p10 = re.compile('^(?P<test_id>\d+)\)\s+(?P<test_name>\w+):?\s*-*>*\s*(?P<result>.*)$')

        #Port 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
        p11 = re.compile(r'^Port +(?P<ports>[\d\s]+)')
        
        #U . . . . U . . . . . . . . . . . . . . . . . .
        p12 = re.compile(r'(?P<port_state>[UF.\s]+)')

        for line in output.splitlines():
            line = line.strip()
            
            
            #2) TestFantray ---------------------> .
            #3) DiagPhyLoopbackTest:
            m = p10.match(line)
            if m:
                group=m.groupdict()
                if group['result'] == ".":
                    result = "Passed"
                elif group['result'] == "F":
                    result = "Failed"

                else:
                    result = "Untested"
                test_id = int(group['test_id'])
                test_name = group['test_name']
                root_dict1 = ret_dict.setdefault('diag_tests',{}).setdefault('module',{}).setdefault(int(mod_num),{}).setdefault(test_name,{})
                root_dict1.setdefault('test_id', test_id)
                root_dict1.setdefault('result',result)
                continue
            
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
              
            
            
            #Port 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
            m = p11.match(line)
            if m:
                group = m.groupdict()
                l1 = group['ports'].split()

                list1.extend(l1)
                list1 = list(map(int, list1))
                continue

            #U . . . . U . . . . . . . . . . . . . . . . . .
            m = p12.match(line)
            if m:
                group = m.groupdict()
                port_dict = root_dict1.setdefault('port_status',{})
                l2 = group['port_state'].split()

                list2.extend(l2)
                result_dict = dict(zip(list1,list2))
                root_dict1.update({'port_status':result_dict})
                continue
            
        return ret_dict


class ShowDiagnosticResultSwitchModuleTestDetailSchema(MetaParser):
    """
    Schema for show diagnostic result switch {switch_num} module {mod_num} test {include} detail 
    
    """

    schema = {
        'switch': int,
        'diag_tests': {
            'module': {
               Any(): {
                    Any(): {
                        'test_id': int,
                        'result': str,
                        Optional('port_status'):{
                            int: str
                            },
                        'error_code': str,
                        'total_run_count': int,
                        'testing_type': str,
                        'test_execution_time': str,
                        'first_test_failure': str,
                        'last_test_failure': str,
                        'last_test_pass': str,
                        'total_failure_count': int,
                        'consecutive_failure_count': int
                    }
                }
            }
        }
    }

class ShowDiagnosticResultSwitchModuleTestDetail(ShowDiagnosticResultSwitchModuleTestDetailSchema):
    """ Parser for show diagnostic result switch {switch_num} module {mod_num} test {include} detail """

    cli_command = 'show diagnostic result switch {switch_num} module {mod_num} test {include} detail'


    def cli(self, switch_num, mod_num, include, output=None): 

        if output is None:
            cmd = self.cli_command.format(switch_num=switch_num,mod_num=mod_num,include=include)

            output = self.device.execute(cmd)
               
        # initial variables
        list1 = []
        list2 = []

        ret_dict = {}

        #2) TestFantray ---------------------> .
        p1 = re.compile('^(?P<test_id>\d+)\)\s+(?P<test_name>\w+):?\s*-*>*\s*(?P<result>.*)$')

        #Error code ------------------> 1 (DIAG_FAILURE)
        p2 = re.compile('^Error code [-> ]+(?P<error_code>(.*))$')

        #Total run count -------------> 8160 
        p3 = re.compile('^Total run count [-> ]+(?P<total_run_count>\d+)$')

        #Last test testing type ------> Health Monitoring
        p4 = re.compile('^Last test testing type[-> ]+(?P<testing_type>[A-Z a-z]+|n/a)$')

        #Last test execution time ----> Oct 15 2019 13:02:21 
        p5 = re.compile('^Last \w+ execution \w+[ ->]+(?P<test_execution_time>(\w+ \d+ \d+ \d+:\d+:\d+)|n/a)$')

        #First test failure time -----> Oct 06 2019 01:30:37 
        p6 = re.compile('^First test failure time [-> ]+(?P<first_test_failure>(\w+ \d+ \d+ \d+:\d+:\d+)|n/a)$')

        #Last test failure time ------> Oct 15 2019 13:02:21
        p7 = re.compile('^Last test failure time[-> ]+(?P<last_test_failure>(\w+ \d+ \d+ \d+:\d+:\d+)|n/a)$')

        #Last test pass time ---------> n/a 
        p8 = re.compile('^Last test pass time [ ->]+(?P<last_test_pass>(\w+ \d+ \d+ \d+:\d+:\d+)|n/a)$')

        #Total failure count ---------> 8160 
        p9 = re.compile('^Total failure count [-> ]+(?P<total_failure_count>\d+)$')

        #Consecutive failure count ---> 8160 
        p10 = re.compile('^Cons\w+ fail\w+ \w+[ ->]+ (?P<consecutive_failure_count>\d+)$')

        #Port 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
        p11 = re.compile(r'^Port +(?P<ports>[\d\s]+)')
        
        #U . . . . U . . . . . . . . . . . . . . . . . .
        p12 = re.compile(r'(?P<port_state>[UF.\s]+)')


        for line in output.splitlines():
            line = line.strip()
            
            ret_dict['switch'] = int(switch_num)            
            diag_dict = ret_dict.setdefault('diag_tests',{})
            diag_dict = diag_dict.setdefault('module',{}).setdefault(int(mod_num),{})                
 

            #2) TestFantray ---------------------> .
            #3) TestPhyLoopback:
            m = p1.match(line)
            if m:
                group=m.groupdict()
                test_dict = diag_dict.setdefault((group['test_name']),{})
                test_dict['test_id'] = int(group['test_id'])
                if group['result']==".":
                    result = "Passed"
                elif group['result']=="F":
                    result = "Failed"
                else:
                    result = "Untested"
                test_dict['result'] = result
                
                    

            #Error code ------------------> 1 (DIAG_FAILURE)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                test_dict['error_code']= group['error_code']
                continue
               
            #Total run count -------------> 8160 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                test_dict['total_run_count']= int(group['total_run_count'])
                continue
               
            #Last test testing type ------> Health Monitoring
            m = p4.match(line)
            if m:
                group = m.groupdict()
                test_dict['testing_type']= group['testing_type']
                continue
                
            #Last test execution time ----> Oct 15 2019 13:02:21 
            m = p5.match(line)
            if m:
                group = m.groupdict()
                test_dict['test_execution_time']= group['test_execution_time']
                continue
                
            #First test failure time -----> Oct 06 2019 01:30:37 
            m = p6.match(line)
            if m: 
                group = m.groupdict()
                test_dict['first_test_failure']= group['first_test_failure']
                continue
               
            #Last test failure time ------> Oct 15 2019 13:02:21
            m = p7.match(line)
            if m:
                group = m.groupdict()
                test_dict['last_test_failure']= group['last_test_failure']
                continue
                
            #Last test pass time ---------> n/a 
            m = p8.match(line)
            if m:
                group = m.groupdict()
                test_dict['last_test_pass']= group['last_test_pass']
                continue
              
            #Total failure count ---------> 8160 
            m = p9.match(line)
            if m:
                group = m.groupdict()
                test_dict['total_failure_count']= int(group['total_failure_count'])
                continue
                
            #Consecutive failure count ---> 8160 
            m = p10.match(line)
            if m:
                group = m.groupdict()
                test_dict['consecutive_failure_count']= int(group['consecutive_failure_count'])
                continue

            #Port 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
            m = p11.match(line)
            if m:
                group =m.groupdict()
                l1=group['ports'].split()
                list1.extend(l1)
                list1 = list(map(int, list1))
                continue

            #U . . . . U . . . . . . . . . . . . . . . . . .
            m = p12.match(line)
            if m:
                group =m.groupdict()
                port_dict = test_dict.setdefault('port_status',{})
                l2=group['port_state'].split()
                list2.extend(l2)
                result_dict = dict(zip(list1,list2))
                test_dict.update({'port_status':result_dict})
                continue
                
        return ret_dict

class ShowDiagnosticResultSwitchTestDetailSchema(MetaParser):
    """
    Schema for show diagnostic result switch {switch_number} test {include} detail 
    show diagnostic result switch {switch_number} test {include} detail  
    """

    schema = {
        'diag_tests':{
            'switch':{
                int:{          
                    Any():{
                        'test_id' : int,
                        'result' : str,
                        Optional('port_status'):{
                            int: str
                            },
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

class ShowDiagnosticResultSwitchTestDetail(ShowDiagnosticResultSwitchTestDetailSchema):
    """ Parser for show diagnostic result switch {switch_number} test {include} detail """

    # Parser for 'show diagnostic result switch {switch_number} test {include} detail'
    cli_command = 'show diagnostic result switch {switch_number} test {include} detail'

    def cli(self, switch_number, include, output=None): 

        if output is None:
                output = self.device.execute(self.cli_command.format(switch_number=switch_number,include=include))
               
        # initial variables
        list1 = []
        list2 = [] 
      
        ret_dict = {}

        #2) TestFantray ---------------------> .
        p1 = re.compile('^(?P<test_id>\d+)\)\s+(?P<test_name>\w+):?\s*-*>*\s*(?P<result>.*)$') 

        #Error code ------------------> 1 (DIAG_FAILURE)
        p2 = re.compile('^Error code [-> ]+(?P<error_code>(.*))$')
        
        #Total run count -------------> 8160 
        p3 = re.compile('^Total run count [-> ]+(?P<total_run_count>\d+)$')
        
        #Last test testing type ------> Health Monitoring
        p4 = re.compile('^Last test testing type[-> ]+(?P<testing_type>[A-Z a-z]+|n/a)$')
        
        #Last test execution time ----> Oct 15 2019 13:02:21 
        p5 = re.compile('^Last \w+ execution \w+[ ->]+(?P<test_execution_time>.*|n/a)$')
        
        #First test failure time -----> Oct 06 2019 01:30:37 
        p6 = re.compile('^First test failure time [-> ]+(?P<first_test_failure>.*|n/a)$')
        
        #Last test failure time ------> Oct 15 2019 13:02:21
        p7 = re.compile('^Last test failure time[-> ]+(?P<last_test_failure>.*|n/a)$')
        
        #Last test pass time ---------> n/a 
        p8 = re.compile('^Last test pass time [ ->]+(?P<last_test_pass>.*|n/a)$')
        
        #Total failure count ---------> 8160 
        p9 = re.compile('^Total failure count [-> ]+(?P<total_failure_count>\d+)$')
        
        #Consecutive failure count ---> 8160 
        p10 = re.compile('^Cons\w+ fail\w+ \w+[ ->]+ (?P<consecutive_failure_count>\d+)$')
        
        #Port 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
        p11 = re.compile(r'^Port +(?P<ports>[\d\s]+)')
        
        #U . . . . U . . . . . . . . . . . . . . . . . .
        p12 = re.compile(r'(?P<port_state>[UF.\s]+)')


        for line in output.splitlines():
            line = line.strip()

            root_dict = ret_dict.setdefault('diag_tests',{}).setdefault('switch',{}).setdefault(int(switch_number),{})

            #2) TestFantray ---------------------> .
            #3) TestPhyLoopback:           
            m = p1.match(line)
            if m:
                group=m.groupdict()
                root_dict1 = root_dict.setdefault((group['test_name']),{})
                root_dict1['test_id'] = int(group['test_id'])
                if group['result']==".":
                    result = "Passed"
                elif group['result']=="F":
                    result = "Failed"
                else:
                    result = "Untested"
                root_dict1['result'] = result
                continue

            #Error code ------------------> 1 (DIAG_FAILURE)
            m = p2.match(line)
            if m:
               group = m.groupdict()
               root_dict1.setdefault('error_code',m.group('error_code'))
               continue
               
            #Total run count -------------> 8160 
            m = p3.match(line)
            if m:
               group = m.groupdict()
               root_dict1.setdefault('total_run_count',int(m.group('total_run_count')))
               continue
               
            #Last test testing type ------> Health Monitoring
            m = p4.match(line)
            if m:
               group = m.groupdict()
               root_dict1.setdefault('testing_type',m.group('testing_type'))
               continue
               
            #Last test execution time ----> Oct 15 2019 13:02:21 
            m = p5.match(line)
            if m:
               group = m.groupdict()
               root_dict1.setdefault('test_execution_time',m.group('test_execution_time'))
               continue
               
            #First test failure time -----> Oct 06 2019 01:30:37 
            m = p6.match(line)
            if m: 
               group = m.groupdict()
               root_dict1.setdefault('first_test_failure',m.group('first_test_failure'))
               continue
               
            #Last test failure time ------> Oct 15 2019 13:02:21
            m = p7.match(line)
            if m:
               group = m.groupdict()
               root_dict1.setdefault('last_test_failure',m.group('last_test_failure'))
               continue
               
            #Last test pass time ---------> n/a 
            m = p8.match(line)
            if m:
               group = m.groupdict()
               root_dict1.setdefault('last_test_pass',m.group('last_test_pass'))
               continue
               
            #Total failure count ---------> 8160 
            m = p9.match(line)
            if m:
               group = m.groupdict()
               root_dict1.setdefault('total_failure_count',int(m.group('total_failure_count')))
               continue
               
            #Consecutive failure count ---> 8160 
            m = p10.match(line)
            if m:
               group = m.groupdict()
               root_dict1.setdefault('consecutive_failure_count',int(m.group('consecutive_failure_count')))
               continue
              

             #Port 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
            m = p11.match(line)
            if m:
                group =m.groupdict()
                l1=group['ports'].split()
                list1.extend(l1)
                list1 = list(map(int, list1))
                continue

            #U . . . . U . . . . . . . . . . . . . . . . . .
            m = p12.match(line)
            if m:
                group =m.groupdict()
                port_dict = root_dict1.setdefault('port_status',{})
                l2=group['port_state'].split()
                list2.extend(l2)
                result_dict = dict(zip(list1,list2))
                root_dict1.update({'port_status':result_dict})
                continue
               
        return ret_dict


class ShowDiagnosticPostSchema(MetaParser):
    """
    Schema for show diagnostic post
    """

    schema = {
        Optional('load'): {
            'five_seconds': str,
            'one_minute': str,
            'five_minutes': str
        },
        Optional('ntp_time'): str,
        'switch': {
            Any(): {
                Optional('load'): {
                    'five_seconds': str,
                    'one_minute': str,
                    'five_minutes': str
                },
                Optional('ntp_time'): str,
                'test': {
                    Any(): {
                        'initial_state': str,
                        'final_state': str,
                        'status': str
                    }
                }
            }
        } 
    }


class ShowDiagnosticPost(ShowDiagnosticPostSchema):
    """Parser for show diagnostic post"""

    cli_command = 'show diagnostic post'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        ret_dict = switch_dict = {}
        
        # Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
        p1 = re.compile(r'^Load for five secs: (?P<five_seconds>\S+); one minute: (?P<one_minute>\S+); five minutes: (?P<five_minutes>\S+)$')

        # Time source is NTP, .08:55:28.918 UTC Mon Mar 13 2023
        p2 = re.compile(r'^Time source is NTP, (?P<ntp_time>.+)$')
        
        # Switch 1
        p3 = re.compile(r'^Switch (?P<switch>\d+)$')

        # POST: MBIST Tests : Begin
        # POST: PHY Loopback: loopback Test : Begin
        # POST: Thermal, Temperature Tests : Begin
        p4 = re.compile(r'^POST:\s(?P<test>[\w\s\,]+)(:\sloopback )?Tests*\s:\s(?P<initial_state>[\w\s]+)$')

        # POST: PHY Loopback: loopback Test : End, Status Passed
        # POST: Thermal, Fan Tests : End, Status Passed
        p5 = re.compile(r'^POST:\s(?P<test>[\w\s\,]+)(:\sloopback )?Tests*\s:\s(?P<final_state>[\w\s]+), Status (?P<status>[\w\s]+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
            m = p1.match(line)
            if m:
                load_dict = switch_dict.setdefault('load', {})
                load_dict['five_seconds'] = m.groupdict()['five_seconds']
                load_dict['one_minute'] = m.groupdict()['one_minute']
                load_dict['five_minutes'] = m.groupdict()['five_minutes']
                continue

            # Time source is NTP, .08:55:28.918 UTC Mon Mar 13 2023
            m = p2.match(line)
            if m:
                switch_dict['ntp_time'] = m.groupdict()['ntp_time']
                continue

            # Switch 1
            m = p3.match(line)
            if m:
                switch_dict = ret_dict.setdefault('switch', {}).setdefault(m.groupdict()['switch'], {})
                continue

            # POST: MBIST Tests : Begin
            # POST: PHY Loopback: loopback Test : Begin
            # POST: Thermal, Temperature Tests : Begin
            m = p4.match(line)
            if m:
                test_name = m.groupdict()['test'].strip().lower().replace(' ', '_').replace(',', '')
                test_dict = switch_dict.setdefault('test', {}).setdefault(test_name, {})
                test_dict['initial_state'] = m.groupdict()['initial_state']
                continue

            # POST: PHY Loopback: loopback Test : End, Status Passed
            # POST: Thermal, Fan Tests : End, Status Passed
            m = p5.match(line)
            if m:
                test_name = m.groupdict()['test'].strip().lower().replace(' ', '_').replace(',', '')
                test_dict = switch_dict.setdefault('test', {}).setdefault(test_name, {})
                test_dict['final_state'] = m.groupdict()['final_state']
                test_dict['status'] = m.groupdict()['status']
                continue

        return ret_dict
