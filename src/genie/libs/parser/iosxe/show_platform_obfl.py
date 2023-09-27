''' show_platform_oblf.py
IOSXE parsers for the following show commands:
    
    * 'show logging onboard switch <switch_num> clilog'  
    * 'show logging onboard rp <rp> clilog'  
    * 'show logging onboard Switch <switch_num> status'
    * 'show logging onboard switch <switch_num> uptime detail'
    * 'show logging onboard rp <rp> message detail'
    * 'show logging onboard switch <switch_num> <include> continuous'
    * 'show logging onboard switch rp <rp> environment continuous'
'''

# Python
import re
import logging
from collections import OrderedDict
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, ListOf 
from genie.libs.parser.utils.common import Common
from genie.parsergen import oper_fill_tabular

try:
    import genie.parsergen
except (ImportError, OSError):
    pass

from pyats.utils.exceptions import SchemaTypeError

log = logging.getLogger(__name__)


class ShowLoggingOnboardSwitchClilogSchema(MetaParser):
    '''Schema for:
        Show logging onboard switch 1 clilog
    '''
    schema={
        'command_count':{
            Any():{
                'count': int,            
            },
        }, 
    }


class ShowLoggingOnboardSwitchClilog(ShowLoggingOnboardSwitchClilogSchema):
    """
    Parser for :
        'Show logging onboard switch 1 clilog'
    """
    cli_command = 'show logging onboard switch {switch} clilog'
    
    def cli(self,switch="",output=None): 

        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch))
        
        ret_dict = {}

        # 1    clear obfl switch 3 environment
        # 1    clear obfl switch 1
        p1 = re.compile(r'(?P<count>\d)\s+(?P<command>clear+\s+obfl+\s+switch+\s+\d+(\s+.*)?)')
        
        for line in output.splitlines():
            line = line.strip()
            #1    clear obfl switch 3 environment
            m = p1.match(line)
            if m:
                group = m.groupdict()
                command_count = group["command"]
                sub_dict = ret_dict.setdefault('command_count', {}).setdefault(command_count, {})
                count = group['count']
                sub_dict['count'] = int(count)
                continue
        
        return ret_dict

class ShowLoggingOnboardSwitchActiveStatusSchema(MetaParser):
    '''Schema for:
        show logging onboard switch {switch_num} status
    '''
    schema={
        'application':{
            Any():{
                'path': str,
                'status': bool,            
            },
        }, 
    }
        
        
class ShowLoggingOnboardSwitchActiveStatus(ShowLoggingOnboardSwitchActiveStatusSchema):
    """
    Parser for :
        'show logging onboard Switch {switch_num} status'
    """
    
    cli_command = 'show logging onboard switch {switch_num} status'
    
    def cli(self,switch_num="",output=None): 

        if output is None:
            output = self.device.execute(self.cli_command.format(switch_num=switch_num))
            
        ret_dict ={}
        #Application Clilog:
        p1 = re.compile('^Application (?P<application>\S+):$')
        
        #Cli enable status: enabled
        p2 = re.compile('^Cli (?P<enable_status>enable status): (?P<status>\S+)$')
        
        # Path: /obfl0/
        p3 = re.compile('^Path\: (?P<path>\S+)$')
        
        for line in output.splitlines():
            line=line.strip()

            #Application Clilog:
            m=p1.match(line)
            if m:
                group = m.groupdict()
                root_dict=ret_dict.setdefault('application', {}).setdefault(group['application'].lower(), {})
                continue
                
            #Cli enable status: enabled
            m=p2.match(line)
            if m:
                group = m.groupdict()
                status = True if \
                    group['status'].lower() == 'enabled' else\
                    False
                root_dict.setdefault('status', status)
                
            ## Path: /obfl0/ 
            m=p3.match(line)
            if m:
                group=m.groupdict()
                root_dict.setdefault('path', group['path'])
                continue
                
        return ret_dict

class ShowLoggingOnboardSwitchActiveUptimeDetailSchema(MetaParser):

    '''Schema for:
        'show logging onboard switch {switch_num} uptime detail'
    '''
    
    schema={
        "uptime_detail":{
          "uptime_summary":{
              "first_customer_power_on":str,
              "number_of_reset":int,
              "number_of_slot_changes":int,
              "current_reset_reason":str,
              "current_reset_timestamp":str,
              "current_slot":int,
              "chassis_type":str,
              Any():{
                "years":int,
                "weeks":int,
                "days":int,
                "hours":int,
                "minutes":int
              }
          },
          "uptime_continuous":{
              "time":{
                Any():{
                    "date":str,
                    "reason":str,
                    "years":int,
                    "weeks":int,
                    "days":int,
                    "hours":int,
                    "minutes":int
                }
              }
          }
        }
    }
  
class ShowLoggingOnboardSwitchActiveUptimeDetail(ShowLoggingOnboardSwitchActiveUptimeDetailSchema):
    """
    Parser for :
        'show logging onboard switch {switch_num} uptime detail'
    """

    cli_command = "show logging onboard switch {switch_num} uptime detail"
    
    
    def cli(self,switch_num="",output=None): 

        if output is None: 
            # Build and Execute the command 
            output = self.device.execute(self.cli_command.format(switch_num=switch_num))
       
        ret_dict ={}
        
        #First customer power on : 06/22/2021 12:35:40
        p1 = re.compile('^First customer power on :?\s?(?P<first_customer_poweron>(\d+\/){2}\d+ \d+:\d+:\d+)$')
        
        #Total uptime            :  0  years  12 weeks  1  days  17 hours  55 minutes
        p2 = re.compile('^Total uptime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')
        
        #Total downtime          :  2177 years  8  weeks  0  days  2  hours  29 minutes
        p3 = re.compile('^Total downtime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')
        
        #Number of resets        : 630
        p4 = re.compile('^Number of resets\s+: (?P<numberof_reset>\d+)$')
        
        #Number of slot changes  : 1
        p5 = re.compile('^Number of slot changes\s+: (?P<numberof_slot_changes>\d+)$')
        
        #Current reset reason    : Reload Command
        p6 = re.compile('^Current reset reason\s+: (?P<current_reset_reason>[A-Z a-z\S]+)$')
        
        #Current reset timestamp : 10/06/2019 01:28:26
        p7 = re.compile('^Current reset timestamp\s+: (?P<current_reset_timestamp>(\d+\/){2}\d+.*)$')
        
        #Current slot            : 1
        p8 = re.compile('^Current slot\s+: (?P<current_slot>\d+)$')
        
        #Chassis type            : 80
        p9 = re.compile('^Chassis type\s+: (?P<chassis_type>\w+)$')
        
        #Current uptime          :  0  years  1  weeks  1  days  0  hours  0  minutes
        p10 = re.compile('^Current uptime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')
        
        #05/16/2015 16:31:49   Reload Command                0     0     0     0     0
        p11 = re.compile('^(?P<date>\d+/+\d+/+\d+)+\s+(?P<time>\d+:+\d+:+\d+)+\s+(?P<reason>\S+\s+\D+)+\s+(?P<years>\d)+\s+(?P<weeks>\d)+\s+(?P<days>\d)+\s+(?P<hours>\d)+\s+(?P<minutes>\d+)$')
       
        for line in output.splitlines():
            line = line.strip()
            
            root_dict=ret_dict.setdefault('uptime_detail',{}).setdefault('uptime_summary',{})
            sub_dict=ret_dict.setdefault('uptime_detail',{}).setdefault('uptime_continuous',{})
            
            #First customer power on : 06/22/2021 12:35:40
            m=p1.match(line)
            if m:
                group=m.groupdict()
                root_dict['first_customer_power_on']= group['first_customer_poweron']
                continue
                
            #Total uptime            :  0  years  12 weeks  1  days  17 hours  55 minutes
            m=p2.match(line)
            if m:
                group=m.groupdict()
                root_dict1=root_dict.setdefault('total_uptime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue
                
            #Total downtime          :  2177 years  8  weeks  0  days  2  hours  29 minutes
            m=p3.match(line)
            if m:
                group=m.groupdict()
                root_dict1=root_dict.setdefault('total_downtime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue
                
            #Number of resets        : 630
            m=p4.match(line)
            if m:
                group=m.groupdict()
                root_dict['number_of_reset']=int(group['numberof_reset'])
                continue
                
            #Number of slot changes  : 1
            m=p5.match(line)
            if m:
                group=m.groupdict()
                root_dict['number_of_slot_changes']=int(group['numberof_slot_changes'])
                continue
                
            #Current reset reason    : Reload Command
            m=p6.match(line)
            if m:
                group=m.groupdict()
                root_dict['current_reset_reason'] =group['current_reset_reason']
                continue
                
            #Current reset timestamp : 10/06/2019 01:28:26
            m=p7.match(line)
            if m:
                group=m.groupdict()
                root_dict['current_reset_timestamp'] =group['current_reset_timestamp']
                continue
                
            #Current slot            : 1
            m=p8.match(line)
            if m:
                group=m.groupdict()
                root_dict['current_slot'] =int(group['current_slot'])
                continue
                
            ##Chassis type            : 80
            m=p9.match(line)
            if m:
                group=m.groupdict()
                root_dict['chassis_type'] = str(group['chassis_type'])
                continue
                
            #Current uptime          :  0  years  1  weeks  1  days  0  hours  0  minutes
            m=p10.match(line)
            if m:
                group=m.groupdict()
                root_dict1=root_dict.setdefault('current_uptime',{})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            m=p11.match(line)
            if m:
                group=m.groupdict()
                time = group['time']
                sub_dict1 = sub_dict.setdefault('time',{}).setdefault(time,{})
                sub_dict1['date'] = group['date']
                sub_dict1['reason'] = (group['reason']).strip()
                sub_dict1['years'] = int(group['years'])
                sub_dict1['weeks'] = int(group['weeks'])
                sub_dict1['days'] = int(group['days'])
                sub_dict1['hours'] = int(group['hours'])
                sub_dict1['minutes'] = int(group['minutes'])
                continue
        
        return ret_dict

class ShowLoggingOnboardSwitchContinuousSchema(MetaParser):
    '''Schema for:

	'show logging onboard switch <switch_num> temperature continuous'
        'show logging onboard switch <switch_num> voltage continuous'
        'show logging onboard switch <switch_num> message continuous'
        
    '''

    schema={
        Optional('application'):str,
        Optional('temperature_sensors'):{
            Any():{
                'id': int,
                'history':{
                    Any():int,
                },
            },
        },
        Optional('voltage_sensors'):{
            Any():{
                'id': int,
                'history':{
                    Any():int,
                },
            },
        },  
        Optional('error_message'):{
            Any():ListOf(str),
        },        
    }
 
class ShowLoggingOnboardSwitchContinuous(ShowLoggingOnboardSwitchContinuousSchema):
    """
    Parser for :
        'show logging onboard switch <switch_num> <temperature> continuous'
        'show logging onboard switch <switch_num> <voltage> continuous'
        'show logging onboard switch <switch_num> <message> continuous'
    """
   
    cli_command = 'show logging onboard switch {switch_num} {include} continuous'
				   
    def cli(self, include="", switch_num="", output=None): 

        if output is None: 
            # Build and Execute the command 
            output = self.device.execute(self.cli_command.format(switch_num=switch_num,include=include))
			
        #VOLTAGE CONTINUOUS INFORMATION
        p1 = re.compile('^(?P<continuous_info>[A-Z ]+) CONTINUOUS INFORMATION$')

        #PS1 Vout 0
        p2 = re.compile('^(\w+\: )?(?P<sensor_name>\w+.*?)\s+(?P<sensor_count>\d+)$')

        #05/25/2015 04:09:00  56  210  10  28  177  157   0   0   0   0   0   0   0   0   0   0   0   0   0   0
        p3 = re.compile('^(?P<time>\d+\/\d+\/\d+ \d+:\d+:\d+)\s+(?P<sensor_value>[\d\s]+).*$')
        
        #05/16/2015 15:57:21 %NYQ-2-PLATFORM_PSFAN_NOT_PRESENT : OBFL PS-FAN NOT PRESENT : FEP fan PS-2
        p4 = re.compile('^(?P<time>\d+\/\d+\/\d+ \d+:\d+:\d+)\s+%(?P<info>\S+\s+\:+.*)$')

        sensor_list=[]
        ret_dict = {}
        sensor_name_list=[]

        for line in output.splitlines():
            line = line.strip()                        
                
            #TEMPERATURE CONTINUOUS INFORMATION
            m=p1.match(line)
            if m:
                group1 = m.groupdict()
                ret_dict.setdefault('application', group1['continuous_info'])
                continue
            
            #05/25/2015 04:09:00  56  210  10  28  177  157   0   0   0   0   0   0   0   0   0   0   0   0   0   0  
            m=p3.match(line)
            if m:
                group = m.groupdict()
                root_dict=ret_dict.setdefault((group1['continuous_info'].lower()).replace(' ','_')+"_sensors",{})
                if group['sensor_value']:
                    sensor_list=[]
                    for value in group['sensor_value'].split(" "):
                        if value.isdigit():
                            sensor_list.append(int(value))
                if len(sensor_list)==len(sensor_name_list):
                    for i in range(0,len(sensor_name_list)):
                        root_dict1=root_dict.setdefault(sensor_name_list[i],{})
                        root_dict1['id']=i
                        root_dict1.setdefault('history',{}).setdefault(group['time'],sensor_list[i]) 
                continue
            
            #PS1 Vout 0
            m=p2.match(line)
            if m:
                group = m.groupdict()
                sensor_name_list.append(group['sensor_name'])
                continue

            #05/16/2015 15:57:21 %NYQ-2-PLATFORM_PSFAN_NOT_PRESENT : OBFL PS-FAN NOT PRESENT : FEP fan PS-2
            m=p4.match(line)
            if m:
                group=m.groupdict()
                root_dict=ret_dict.setdefault((group1['continuous_info'].lower()).replace(' ','_'),{})
                if group['time'] not in root_dict.keys():
                    root_dict[group['time']]=[group['info']]
                else:
                    root_dict[group['time']].append(group['info'])
                continue
                
        return ret_dict

class ShowLoggingOnboardSwitchEnvironmentContinuousSchema(MetaParser):
    ''' Schema for: 'show logging onboard switch <switch_num> environment continuous'
                    'show logging onboard rp active environment continuous'
                    'show logging onboard rp {rp_standby} environment continuous' 
                    '''

    schema={
        "event":{
            Any():{
                "time":str,
                "device_name":str,
                "date":str,
                "ios_version":str,
                "fw_ver_bias_ver":int,
                Any():{
                    "tan":str,
                    "serial_no":str
                }
            },
        }
    }

class ShowLoggingOnboardSwitchEnvironmentContinuous(ShowLoggingOnboardSwitchEnvironmentContinuousSchema):
    """
    Parser for :
        'show logging onboard switch <switch_num> environment continuous'
        'show logging onboard rp active environment continuous'
        'show logging onboard rp {rp_standby} environment continuous'
    """

    cli_command = ['show logging onboard switch {switch_num} environment continuous',
                   'show logging onboard rp active environment continuous',
                   'show logging onboard rp {rp_standby} environment continuous']

    def cli(self, switch_num="", rp_standby="", output=None): 

        if output is None: 
            # Build and Execute the command 
            if switch_num:
                output = self.device.execute(self.cli_command[0].format(switch_num=switch_num))
            elif rp_standby:
                output = self.device.execute(self.cli_command[2].format(rp_standby=rp_standby))
            else:
                output = self.device.execute(self.cli_command[1])

        ret_dict = {}

        #11/24/2022 05:56:13                    NA          Port-0          0       Rmv 
        p1=re.compile(r'^(?P<date>\d+/+\d+/\d+)+\s+(?P<time>\d+.+\d+.\d+)\s+(?P<device_name>\S+)\s+(?P<ios_version>\S+)\s+(?P<fw_ver_bias_ver>\S+)\s+(?P<event>\S+)$')

        #V01 STACK-T1-50CM         Stack-Cable LCC2131G3TH 
        p2=re.compile(r'^(?P<vid_pid>\S+\s+STACK+.\S+)+\s+(?P<tan>\S+)+\s(?P<serial_no>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            #11/24/2022 05:56:13                    NA          Port-0          0       Rmv 
            m = p1.match(line)
            if m :
                group = m.groupdict()
                event = group['event']
                sub_dict = ret_dict.setdefault("event",{}).setdefault(event,{})
                sub_dict['time'] = group['time']
                sub_dict['device_name'] = group['device_name']
                sub_dict['date'] = group['date']
                sub_dict['ios_version'] = group['ios_version']
                sub_dict['fw_ver_bias_ver'] = int(group['fw_ver_bias_ver'])
                continue

            #V01 STACK-T1-50CM         Stack-Cable LCC2131G3TH  
            m = p2.match(line)
            if m :
                group = m.groupdict()
                vid_pid = group['vid_pid']  
                sub_dict1 = sub_dict.setdefault(vid_pid,{})
                sub_dict1['tan'] = group['tan']
                sub_dict1['serial_no'] = group['serial_no']
                continue
            
        return ret_dict

class ShowLoggingOnboardSwitchDetailSchema(MetaParser):
    """Schema for show logging onboard switch [switch_num|Active] [temperature|voltage] detail
                """

    schema = {
        Optional('number_of_sensors'): int,
        'sensors': {
            Any(): {
                'sensor_id': int,
                'normal_range_min': int,
                'normal_range_max': int,
                'maximum_sensor_value': int
            },
        }
    }

class ShowLoggingOnboardSwitchDetail(ShowLoggingOnboardSwitchDetailSchema):
    """Schema for show logging onboard switch [switch_num|Active] [temperature|voltage|poe] detail
                """

    cli_command = 'show logging onboard switch {switch_num} {feature} detail'

    def cli(self, switch_num="" , feature="" , output=None):
        if output is None:
            # Build and Execute the command
            output = self.device.execute(self.cli_command.format(switch_num=switch_num,feature=feature))

        ret_dict = {}

        #Number of sensors          : 20
        p1 = re.compile(r'^Number +of +sensors +: +(?P<number_of_sensors>\d+)$')

        #--------------------------------------------------------------------------------
        #Sensor                    ID         Normal Range          Maximum Sensor Value
        #--------------------------------------------------------------------------------
        #PS1 Vout                  0          0 - 5                 56
        #PS1 Vin                   1          0 - 5                 215
        #PS1 CURin                 2          0 - 5                 16
        #PS1 Curout                3          0 - 5                 31
        #PS1 POWin                 4          0 - 5                 202

        p2 = re.compile(r'^(?P<sensors>.+?)\s+(?P<sensor_id>\d+)\s+(?P<normal_range_min>\d+) - (?P<normal_range_max>\d+)\s+(?P<maximum_sensor_value>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #Number of sensors          : 20
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['number_of_sensors'] = int(group['number_of_sensors'])
                continue

            #PS1 POWin                 4          0 - 5                 202
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sensors = group.pop('sensors')
                temp_dict = ret_dict.setdefault('sensors', {}).setdefault(sensors, {})
                temp_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowLoggingOnboardSwitch(ShowLoggingOnboardSwitchDetail):
    '''
        Parser for show logging onboard switch [switch_num|Active] [temperature|voltage|poe]
    '''

    cli_command = 'show logging onboard switch {switch_num} {feature}'

    def cli(self, switch_num="" , feature="" , output=None):
        return super().cli(switch_num=switch_num, feature=feature, output=output)


class ShowLoggingOnboardSwitchMessageDetailSchema(MetaParser):
    '''Schema for:
        'show logging onboard switch 1 message detail'
        'show logging onboard rp {rp} message detail'
    '''   
    schema={
        'message_summary':{
            Any():ListOf(str),
          },        
    }

class ShowLoggingOnboardSwitchMessageDetail(ShowLoggingOnboardSwitchMessageDetailSchema):
    '''Schema for:
        'show logging onboard switch 1 message detail'
        'show logging onboard rp {rp} message detail'
    ''' 
    cli_command = ['show logging onboard switch {switch_num} message detail',
                   'show logging onboard rp {rp} message detail']
				   
    def cli(self,switch_num="", rp="", output=None): 

        if output is None: 
            # Build and Execute the command
            if switch_num:
                output = self.device.execute(self.cli_command[0].format(switch_num=switch_num))
            else:
                output = self.device.execute(self.cli_command[1].format(rp=rp))
                
        ret_dict = {}

        #05/16/2015 21:39:57 %NYQ-2-PLATFORM_PSFAN_NOT_PRESENT :  >254 LAST  OBFL PS-FAN NOT PRESENT : FEP fan PS-2
        #05/16/2015 21:39:57 %NYQ-2-PLATFORM_PSFAN_PRESENT :  >254 LAST  OBFL PS-FAN PRESENT : FEP fan PS-1

        p1 = re.compile('^(?P<time>\d+\/\d+\/\d+ \d+:\d+:\d+)\s+%(?P<info>\S+\s+\:+.*)$')		
	
        for line in output.splitlines():
            line = line.strip()
            sub_dict = ret_dict.setdefault("message_summary",{})

            #05/16/2015 21:39:57 %NYQ-2-PLATFORM_PSFAN_PRESENT :  >254 LAST  OBFL PS-FAN PRESENT : FEP fan PS-1
            m=p1.match(line)
            if m:
                group=m.groupdict()
                if group['time'] not in sub_dict.keys():
                    sub_dict[group['time']]=[group['info']]
                else:
                    sub_dict[group['time']].append(group['info'])
                continue

        return ret_dict

class ShowEnvironmentFanSchema(MetaParser):

    schema = {
        "switch": {
            Any(): {
                "fan": {
                    Any(): {
                        "speed": int,
                        "state": str,
                        "airflow_direction": str
                    },
                    
                },
                "fan_ps1": str,
                "fan_ps2": str
            }
        }
    }

class ShowEnvironmentFan(ShowEnvironmentFanSchema):
    """
    Parser for :
        'ShowEnvironmentFan'
    """
    cli_command = 'show environment fan'
    
    def cli(self,switch="",output=None): 

        if output is None:
            # Build the command
            output = self.device.execute(self.cli_command.format(switch=switch))
     
        ret_dict = {}
        for line in output.splitlines():
            line=line.strip()
            
            #Switch   FAN     Speed   State   Airflow direction
            #---------------------------------------------------
            # 1       1     5600      OK     Front to Back
            # 1       2     5600      OK     Front to Back

            p1=re.compile(r'^(?P<switch>\d)+\s+(?P<fan>\d)+\s+(?P<speed>\d+)\s+(?P<state>\S+)\s+(?P<airflow_direction>\S+\s+\S+\s+\S+)$')

            #FAN PS-1 is OK
            p2=re.compile(r'^FAN+\s+PS-1+\s+\S+\s+(?P<fan_ps1>\S+)$')

            #FAN PS-2 is NOT PRESENT
            p3=re.compile(r'^FAN+\s+PS-2+\s+\S+\s+(?P<fan_ps2>\S+.*)$')

            # 1       2     5600      OK     Front to Back
            m = p1.match(line)
            if m:
                group = m.groupdict()
                fan = int(group["fan"])
                switch = int(group["switch"])
                sub_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                sub_dict1 = sub_dict.setdefault('fan', {}).setdefault(fan, {})
                sub_dict1.setdefault('speed', int(group['speed']))
                sub_dict1.setdefault('state', group['state'])
                sub_dict1.setdefault('airflow_direction', group['airflow_direction'])
                continue
            
            #FAN PS-1 is OK    
            m = p2.match(line)
            if m:
                group = m.groupdict()
                fan_ps1 = group['fan_ps1'] 
                sub_dict['fan_ps1'] = fan_ps1
                continue
            
            #FAN PS-2 is NOT PRESENT
            m = p3.match(line)
            if m:
                group = m.groupdict()
                fan_ps2 = group['fan_ps2']
                sub_dict['fan_ps2'] = fan_ps2
                continue
    
        return ret_dict

class ShowEnvironmentPowerAllSchema(MetaParser):

    schema={
        "switch": {
            Any(): {
                "pid": str,
                "serial": str,
                "status": str,
                "sys_pwr": str,
                "poe_pwr": str,
                "watts": int,
                "switch": {
                    Any(): {
                        "pid": str
                    }
                }
            },
            
        }
    }

class ShowEnvironmentPowerAll(ShowEnvironmentPowerAllSchema):
    """
    Parser for :
        'show environment power all'
    """
    cli_command = ['show environment power all','show environment power switch {switch_num}']
    
    def cli(self,switch_num="",output=None): 

        if output is None:
            # Build the command
            if switch_num:
                output = self.device.execute(self.cli_command[1].format(switch_num=switch_num))
            else:
                output = self.device.execute(self.cli_command[0])

        ret_dict={}
        for line in output.splitlines():
            line=line.strip()

            #1A  PWR-C1-1100WAC      DTN2129V1AG  OK              Good     Good     1100
            p1=re.compile(r'^(?P<sw>\d\S)+\s+(?P<pid>\S+)\s+(?P<serial>\S+)\s+(?P<status>\S+)\s+(?P<sys_pwr>\w+)+\s+(?P<poe_pwr>\S+)\s+(?P<watts>\S+)$')
       
            #1B  Not Present
            p2=re.compile(r'^(?P<sw>\d+\S)\s+(?P<pid>Not Present)$')

            #1A  PWR-C1-1100WAC      DTN2129V1AG  OK              Good     Good     1100
            m = p1.match(line)
            if m:
                group=m.groupdict()
                switch = group['sw']
                sub_dict = ret_dict.setdefault('switch',{}).setdefault(switch,{})
                sub_dict['pid'] = group['pid'] 
                sub_dict['serial'] = group['serial']
                sub_dict['status'] = group['status']
                sub_dict['sys_pwr'] = group['sys_pwr']
                sub_dict['poe_pwr'] = group['poe_pwr']
                sub_dict['watts'] = int(group['watts'])
                continue
            
            #1B  Not Present
            m = p2.match(line)
            if m:
                group=m.groupdict()
                switch = group['sw']
                sub_dict1 = sub_dict.setdefault('switch', {}).setdefault(switch, {})
                sub_dict1['pid'] = group['pid']
                continue

        return ret_dict


class ShowLoggingOnboardRpClilogSchema(MetaParser):
    '''Schema for:
        Show logging onboard rp active clilog
        Show logging onboard rp standby clilog
    '''
    schema={
        'command_count':{
            Any():{
                'count': int,            
            },
        }, 
    }

class ShowLoggingOnboardRpClilog(ShowLoggingOnboardSwitchClilogSchema):
    """
    Parser for :
        'Show logging onboard rp active clilog'
        'Show logging onboard rp standby clilog'
    """
    cli_command = 'show logging onboard rp {rp} clilog'
    
    def cli(self,rp="",output=None): 

        if output is None:
        
            if rp:
                output = self.device.execute(self.cli_command)
                
        ret_dict = {}

        # 1    clear obfl RP active
        p1 = re.compile(r'(?P<count>\d)\s+(?P<command>clear\s+logging\s+onboard\s+RP\s+.*)')
        
        for line in output.splitlines():
            line = line.strip()
            #1    clear obfl RP active
            m = p1.match(line)
            if m:
                group = m.groupdict()
                command_count = group["command"]
                sub_dict = ret_dict.setdefault('command_count', {}).setdefault(command_count, {})
                count = group['count']
                sub_dict['count'] = int(count)
                continue
        
        return ret_dict