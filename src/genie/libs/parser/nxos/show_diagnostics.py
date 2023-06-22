"""show_diagnostics.py
   supported commands:
     * show diagnostic content module {mod_num}
     * show diagnostic result module {mod_num} test {include} detail
     
"""


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
        
        
        
class ShowDiagnosticContentModuleSchema(MetaParser):
    """
    Schema for show diagnostic content module {mod_num}
    """

    schema = {
        'diag_test':{
            'module':{
                Any():{
                    Any():{
                       'test_id' : int,
                       'attributes':str,
                       'test_interval':str
                    },
                },
            },
        }
    }


class ShowDiagnosticContentModule(ShowDiagnosticContentModuleSchema):
    """ Parser for show diagnostic content module {mod_num}"""

    # Parser for 'show diagnostic content module {mod_num}'
    cli_command = 'show diagnostic content module {mod_num}'

    def cli(self, mod_num = None, output=None): 

        if output is None:
            output = self.device.execute(self.cli_command.format(mod_num=mod_num))
        
        # initial variables
        out_dict = {}
        
        #Module 2: 48x10/25G + 4x40/100G Ethernet Module
        p1 = re.compile('^Module\s+(?P<module_num>\d+).*')
        #1)    ASICRegisterCheck------------->     ***N******A     00:01:00
        p2 = re.compile('^(?P<test_id>\d+)\)\s+(?P<test_name>\w+)-+>\s+(?P<attributes>\S+)\s+(?P<test_interval>(-NA-)|[\d \:\.]+)')

        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                temp_dict = out_dict.setdefault('diag_test',{}).setdefault('module',{}).setdefault(group.get('module_num'),{})
            #1)    ASICRegisterCheck------------->     ***N******A     00:01:00
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict = temp_dict.setdefault(group['test_name'], {})
                test_name = group.pop('test_name')
                ret_dict.update({k: v for k, v in group.items()})
                ret_dict['test_id']=int(group['test_id'])   
        return out_dict
         
        
class ShowDiagnosticResultModuleTestDetailSchema(MetaParser):
    """
    Schema for show diagnostic result module {mod_num} test {include} detail 
    show diagnostic result module {mod_num} test {include} detail 
    """

    schema = {
        'diag_tests':{
            'module':{
                Any():{
                    'test_id' : int,
                    'result' : str,
                    'testname':str,
                    'error_code':str,
                    'total_run_count':int,
                    'test_execution_time':str,
                    'first_test_failure':str,
                    'last_test_failure':str,
                    'last_test_pass':str,
                    'total_failure_count':int,
                    'consecutive_failure_count':int,
                    'last_failure_reason':str,
                    Optional  ('port') : dict,
                    }
                }
            }
        }


class ShowDiagnosticResultModuleTestDetail(ShowDiagnosticResultModuleTestDetailSchema):
    """ Parser for show diagnostic result module {mod_num} test {include} detail """

    # Parser for 'show diagnostic result module {mod_num} test {include} detail'
    cli_command = 'show diagnostic result module {mod_num} test {include} detail'

    def cli(self, mod_num = None, include = None, output=None): 

        if output is None:
           
                output = self.device.execute(self.cli_command.format(mod_num=mod_num,include=include))
               
        # initial variables
        ret_dict = {}

        #Error code ------------------> 1 (DIAG_FAILURE)
        p1 = re.compile('^Error code [-> ]+(?P<error_code>(.*))$')
        
        #Total run count -------------> 1
        p2 = re.compile('^Total run count [-> ]+(?P<total_run_count>\d+)$')
        
        # Last test execution time ----> Mon Oct 31 12:45:02 2022 
        p3 = re.compile('^Last test execution time [ ->]+(?P<test_execution_time>(\w+\s+\w+\s+\d+\s+\d+:\d+:\d+ \d+)|n/a)$')
        
        #First test failure time ----->  n/a 
        p4 = re.compile('^First test failure time [-> ]+(?P<first_test_failure>(\w+\s+\w+\s+\d+\s+\d+:\d+:\d+\s+\d+)|n/a)$')
        
        #Last test failure time ------>  n/a
        p5 = re.compile('^Last test failure time[-> ]+(?P<last_test_failure>(\w+\s+\w+\s+\d+\s+\d+:\d+:\d+\s+\d+)|n/a)$')
        
        #Last test pass time ---------> Mon Oct 31 12:45:05 2022
        p6 = re.compile('^Last test pass time [ ->]+(?P<last_test_pass>(\w+\s+\w+\s+\d+\s+\d+:\d+:\d+\s+\d+)|n/a)$')
        
        # Total failure count ---------> 0 
        p7 = re.compile('^Total failure count [-> ]+(?P<total_failure_count>\d+)$')
        
        #Consecutive failure count ---> 0 
        p8 = re.compile('^Cons\w+ fail\w+ \w+[ ->]+ (?P<consecutive_failure_count>\d+)$')
        
        # 13) BootupPortLoopback: .
        p9 = re.compile('^(?P<test_id>\d+)\) (?P<testname>\w+):?\s(?P<result>.*)$')

        #Last failure reason
        p10 = re.compile('^Last failure reason [-> ]+(?P<last_failure_reason>(.*))$')
        
        #Module 2: 48x10/25G + 4x40/100G Ethernet Module
        p0 = re.compile('^Module\s+(?P<module_num>\d+).*')
        
        for line in output.splitlines():
            line = line.strip()
            m = p0.match(line)
            if m:
                group = m.groupdict()
                root_dict1 = ret_dict.setdefault('diag_tests',{}).setdefault('module',{}).setdefault(group.get('module_num'),{})
                continue
            
            #Error code ------------------> 1 (DIAG_FAILURE)
            m = p1.match(line)
            if m:
               root_dict1.setdefault('error_code',m.group('error_code'))
               continue
               
            #Total run count -------------> 1
            m = p2.match(line)
            if m:
               root_dict1.setdefault('total_run_count',int(m.group('total_run_count')))
               continue

            # Last test execution time ----> Mon Oct 31 12:45:02 2022 
            m = p3.match(line)
            if m:
               root_dict1.setdefault('test_execution_time',m.group('test_execution_time'))
               continue
               
            #First test failure time ----->  n/a 
            m = p4.match(line)
            if m: 
               root_dict1.setdefault('first_test_failure',m.group('first_test_failure'))
               continue
               
            #Last test failure time ------>  n/a
            m = p5.match(line)
            if m:
               root_dict1.setdefault('last_test_failure',m.group('last_test_failure'))
               continue
               
            #Last test pass time ---------> Mon Oct 31 12:45:05 2022
            m = p6.match(line)
            if m:
               root_dict1.setdefault('last_test_pass',m.group('last_test_pass'))
               continue
               
            # Total failure count ---------> 0 
            m = p7.match(line)
            if m:
               root_dict1.setdefault('total_failure_count',int(m.group('total_failure_count')))
               continue
               
            #Consecutive failure count ---> 0 
            m = p8.match(line)
            if m:
               root_dict1.setdefault('consecutive_failure_count',int(m.group('consecutive_failure_count')))
               continue
              
            # 13) BootupPortLoopback: .
            m = p9.match(line)
            if m:
                group=m.groupdict()
                result_dict = {"." : "Passed", "F" : "Failed", "A" : "Abort","U" : "Untested","I" : "Incomplete","E" : "Error disabled"}
                result = result_dict.get(group['result'])
                root_dict1.setdefault('test_id',int(group['test_id']))
                root_dict1.setdefault('result',result_dict.get(group['result']))
                root_dict1.setdefault('testname',group['testname'])
                if m.group('testname') in ['PortLoopback','BootupPortLoopback']:
                    port_list = []
                    status_list = []
                    flag = False
                    for line in output.splitlines():
                        if "--" in line:
                            continue
                        elif "Port " in line:
                            port_list.extend(line.split()[1:])
                            flag = True
                        elif flag:
                            status_list.extend(line.split())
                            flag = False
                    ports = dict(zip(port_list, status_list))
                    root_dict1.setdefault('port',ports)
                    continue

            m = p10.match(line)
            if m:
               root_dict1.setdefault('last_failure_reason',m.group('last_failure_reason'))
               continue
               
        return ret_dict
