''' show_logging.py

IOSXE C9400 parsers for the following show commands:

    * 'show logging onboard rp active clilog detail '
    * 'show logging onboard rp active environment detail '
    * 'show logging onboard rp active counter detail '
    * 'show logging onboard rp active message detail '

'''

# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowLoggingOnboardSwitchMessageDetailSchema(MetaParser):
    '''Schema for:
        'show logging onboard rp active message detail'
    '''   
    schema = {
        'error_message_summary':{
            Any(): {
                'count': int,
                'date': str,
                'facility_sev_name': str,
                'persistence_flag': str,
                'time': str,
            },
        }, 
        'error_message_continous':{
            Any(): {
                'con_facility_sev_name': str,
                'date': str,
                'time': str,
            },
        },
    }


class ShowLoggingOnboardSwitchMessageDetail(ShowLoggingOnboardSwitchMessageDetailSchema):
    '''Schema for:
        'show logging onboard rp active message detail'
    ''' 
    cli_command = 'show logging onboard rp {switch_type} message detail'
				   
    def cli(self, switch_type="active", output=None): 

        if output is None: 
            # Build and Execute the command
            output = self.device.execute(self.cli_command.format(switch_type=switch_type))
        
        # init variables
        ret_dict = {}
        # count=0

        # regex pattern

        # ERROR MESSAGE SUMMARY INFORMATION
        p1 = re.compile(r'^ERROR MESSAGE SUMMARY INFORMATION$')

        # MM/DD/YYYY HH:MM:SS Facility-Sev-Name | Count | Persistence Flag
        # --------------------------------------------------------------------------------
        # 04/05/2023 06:57:30 %IOSXE-2-SPA_INSERTED :   168  : LAST :  SPA inserted in subslot 1/0
        p2 = re.compile(r'^(?P<date>\d{2}\/\d{2}\/\d{4})\s(?P<time>\d+:\d+:\d+)\s+(?P<facility_sev_name>.\w+.\w.\w+)\s.\s+(?P<count>\d+)\s+:\s+(?P<persistence_flag>\S+\s+\:+.*)$')

        # ERROR MESSAGE CONTINUOUS INFORMATION
        p3 = re.compile(r'^ERROR MESSAGE CONTINUOUS INFORMATION$')

        # MM/DD/YYYY HH:MM:SS Facility-Sev-Name
        # --------------------------------------------------------------------------------
        # 03/30/2023 02:32:41 %Unrecognized message ID 2504
        # 03/30/2023 03:16:41 %IOSXE-2-DIAGNOSTICS_PASSED : Diagnostics Thermal passed
        p4= re.compile(r'^(?P<date>\d{2}\/\d{2}\/\d{4})\s(?P<time>\d+:\d+:\d+)\s+(?P<con_facility_sev_name>%.*)$')

        for line in output.splitlines():
            line = line.strip()

            # ERROR MESSAGE SUMMARY INFORMATION
            m = p1.match(line)
            if m:
                count = 0
                ret_dict.setdefault('error_message_summary', {})
                continue

            # MM/DD/YYYY HH:MM:SS Facility-Sev-Name | Count | Persistence Flag
            # --------------------------------------------------------------------------------
            # 04/05/2023 06:57:30 %IOSXE-2-SPA_INSERTED :   168  : LAST :  SPA inserted in subslot 1/0
            m = p2.match(line)
            if m:
                count += 1
                group = m.groupdict()
                count_value= group['count']
                sum_dict_child = group.pop('count')
                sum_dict_child = ret_dict.setdefault('error_message_summary', {}).setdefault(count, {})
                sum_dict_child['count']=int(count_value)
                sum_dict_child.update({k: v for k, v in group.items()})
                continue

            # ERROR MESSAGE CONTINUOUS INFORMATION
            m = p3.match(line)
            if m:
                count = 0
                ret_dict.setdefault('error_message_continous', {})
                continue

            # MM/DD/YYYY HH:MM:SS Facility-Sev-Name
            # --------------------------------------------------------------------------------
            # 03/30/2023 02:32:41 %Unrecognized message ID 2504
            # 03/30/2023 03:16:41 %IOSXE-2-DIAGNOSTICS_PASSED : Diagnostics Thermal passed
            m = p4.match(line)
            if m:
                group= m.groupdict()
                count += 1
                con_dict_child = ret_dict.setdefault('error_message_continous', {}).setdefault(count, {})
                con_dict_child.update({k: v for k, v in group.items()})
                continue
        return ret_dict
    

class ShowLoggingOnboardSwitchEnvironmentDetailSchema(MetaParser):
    '''Schema for:
        'show logging onboard rp active environment detail'
    '''   
    schema = {
        'env_summary_info':{
            Any(): {
                'pid': str,
                'serial_no': str,
                'tan': str,
                'vid': str,
                'date': str,
                'ins_count': int,
                'rem_count': int,
                'time': str,
            },
        }, 
        'env_continous_info':{
            Any(): {
                'bios_ver': str,
                'device_name': str,
                'event': str,
                'ios_version': str,
                'pid': str,
                'serial_no': str,
                'tan': str,
                'vid': str,
                'date': str,
                'fw_version': int,
                'ram_size': int,
                'time': str,
            },
        },

    }


class ShowLoggingOnboardSwitchEnvironmentDetail(ShowLoggingOnboardSwitchEnvironmentDetailSchema):
    '''Schema for:
        'show logging onboard rp active environment detail'
    ''' 
    cli_command = 'show logging onboard rp {switch_type} environment detail'
				   
    def cli(self, switch_type="active", output=None): 

        if output is None: 
            # Build and Execute the command
            output = self.device.execute(self.cli_command.format(switch_type=switch_type))
        # init variables
        ret_dict = {}
        counter=0

        # regex pattern

        #ENVIRONMENT SUMMARY INFORMATION
        p1 = re.compile(r'^^ENVIRONMENT SUMMARY INFORMATION$$')


        # MM/DD/YYYY HH:MM:SS   Ins count  Rem count  
        # 04/04/2023 10:36:47    27         0        
        p2_1 = re.compile(r'^(?P<date>\d{2}\/\d{2}\/\d{4})\s+(?P<time>(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d))\s+(?P<ins_count>\d+)\s+(?P<rem_count>\d+)$')

        #  VID    PID                  TAN          Serial No
        #  V01    C9407-FAN            C1           FXS222800XL
        p2_2 = re.compile(r'(?P<vid>\w+)\s+(?P<pid>\w+\-\w+)\s+(?P<tan>\w+)\s+(?P<serial_no>\w+)')
        # ENVIRONMENT CONTINUOUS INFORMATION
        p3 = re.compile(r'^ENVIRONMENT CONTINUOUS INFORMATION$')

        # MM/DD/YYYY  HH:MM:SS   Device Name        IOS Version   F/W Ver   BIOSVer  RAM(KB)     Event  
        # ----------------------------------------------------------------------------------------------
        # 04/04/2023   03:27:36  obfl0:             17.06.04      386204    17.10.1r    0        Ins    
        # 04/05/2023   07:33:49  obfl0:             17.06.04      386204    17.10.1r    0        Ins     
        p4_1= re.compile(r'^(?P<date>\d{2}\/\d{2}\/\d{4})\s+(?P<time>(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d))\s+(?P<device_name>\w+)\:\s+(?P<ios_version>\d+.\d+.\d+)\s+(?P<fw_version>\d+)\s+(?P<bios_ver>\w+.\w+.\w+)\s+(?P<ram_size>\d+)\s+(?P<event>\w+)$')

        #  VID   PID           TAN   Serial No
        # --------------------------------------
        #  V01   C9407-FAN     C1    FXS222800XL
        #  V01   C9407-FAN     C1   FXS222800XL
        p4_2= re.compile(r'(?P<vid>\w+)\s+(?P<pid>\w+\-\w+)\s+(?P<tan>\w+)\s+(?P<serial_no>\w+)')

        for line in output.splitlines():
            line = line.strip()

            # ENVIRONMENT SUMMARY INFORMATION
            m = p1.match(line)
            if m:
                count = 0
                ret_dict.setdefault('env_summary_info', {})
                continue

            # MM/DD/YYYY HH:MM:SS   Ins count  Rem count  
            # 04/04/2023 10:36:47    27         0    
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                count += 1
                ins_count= group['ins_count']
                rem_count= group['rem_count']
                sum_dict_child = group.pop('ins_count')
                sum_dict_child = group.pop('rem_count')
                sum_dict_child = ret_dict.setdefault('env_summary_info', {}).setdefault(count, {})
                sum_dict_child.update({k: v for k, v in group.items()})
                sum_dict_child['ins_count']=int(ins_count)
                sum_dict_child['rem_count']=int(rem_count)
                continue

            #  VID    PID                  TAN          Serial No
            #  V01    C9407-FAN            C1           FXS222800XL
            m= p2_2.match(line)
            if m and counter ==0:
                group =m.groupdict()
                sum_dict_child = ret_dict.setdefault('env_summary_info', {}).setdefault(count, {})
                sum_dict_child.update({k: v for k, v in group.items()})
                continue

            # ENVIRONMENT CONTINUOUS INFORMATION
            m = p3.match(line)
            if m:
                ret_dict.setdefault('env_continous_info', {})
                continue

            # MM/DD/YYYY  HH:MM:SS   Device Name        IOS Version   F/W Ver   BIOSVer  RAM(KB)     Event
            # --------------------------------------------------------------------------------------------
            # 04/04/2023   03:27:36  obfl0:             17.06.04      386204    17.10.1r    0        Ins  
            # 04/05/2023   07:33:49  obfl0:             17.06.04      386204    17.10.1r    0        Ins   
            m = p4_1.match(line)
            if m:
                group= m.groupdict()
                counter += 1
                fw_version= group['fw_version']
                ram_size= group['ram_size']
                con_dict_child = group.pop('fw_version')
                con_dict_child = group.pop('ram_size')
                con_dict_child = ret_dict.setdefault('env_continous_info', {}).setdefault(counter, {})
                con_dict_child.update({k: v for k, v in group.items()})
                con_dict_child['fw_version']=int(fw_version)
                con_dict_child['ram_size']=int(ram_size)
                continue

            #  VID   PID           TAN   Serial No
            # --------------------------------------
            #  V01   C9407-FAN     C1    FXS222800XL
            #  V01   C9407-FAN     C1   FXS222800XL
            m = p4_2.match(line)
            if m:
                group= m.groupdict()
                con_dict_child = ret_dict.setdefault('env_continous_info', {}).setdefault(counter, {})
                con_dict_child.update({k: v for k, v in group.items()})
                continue
        return ret_dict
    
class ShowLoggingOnboardSwitchCounterDetailSchema(MetaParser):
    '''Schema for:
        'show logging onboard rp active counter detail'
    '''   
    schema = {
        'counter_summary_info':{
            Any(): {
                Optional('count'): int,
                Optional('error_type'): int,
                Optional('pid'): str,
                Optional('sno'): str,
                Optional('tan'): str,
                Optional('vid'): str,
            },
        }, 
        'counter_logging_continous_info':{
            Any(): {
                'serial_no': str,
                'count': int,
                'date': str,
                'devname': str,
                'pid': str,
                'slot': int,
                'tan': str,
                'time': str,
                'typ': int,
                'vid': str,
            },
        },
    }

class ShowLoggingOnboardSwitchCounterDetail(ShowLoggingOnboardSwitchCounterDetailSchema):
    '''Schema for:
        'show logging onboard rp active counter detail'
    ''' 
    cli_command = 'show logging onboard rp {switch_type} counter detail'
				   
    def cli(self, switch_type="active", output=None): 

        if output is None: 
            # Build and Execute the command
            output = self.device.execute(self.cli_command.format(switch_type=switch_type))

        # init variables
        ret_dict = {}
        counter= 0

        # regex pattern

        # COUNTER SUMMARY INFORMATION
        p1 = re.compile(r'^COUNTER SUMMARY INFORMATION$')

        # ERROR TYPE | VID  |     PID    |      TAN    SNO         |  COUNT
        # -----------------------------------------------------------------
        # 1            ,V02,    C9400-SUP-1XL   ,A0  ,JAE22300GFU,     20
        p2_1 = re.compile(r'^(?P<error_type>\d+).(?P<vid>\w+).(?P<pid>\w+\-\w+\-\w+)\s+.(?P<tan>\w+)\s+.(?P<sno>\w+).(?P<count>\d+)$')

        # ERROR TYPE | VID  |     PID    |      TAN    SNO         |  COUNT
        # -----------------------------------------------------------------
        # 1            ,,    C9400-SUP-1XL   ,A0  ,JAE22300GFU,     20
        p2_2 = re.compile(r'^(?P<error_type>\d+)..(?P<pid>\w+\-\w+\-\w+)\s+.(?P<tan>\w+)\s+.(?P<sno>\w+).(?P<count>\d+)$')

        # ERROR TYPE | VID  |     PID    |      TAN    SNO         |  COUNT
        # -----------------------------------------------------------------
        # No historical data
        p2_3= re.compile(r'^(?P<no_data>No historical data)$')
        # COUNTER LOGGING CONTINUOUS INFORMATION
        p3 = re.compile(r'^COUNTER LOGGING CONTINUOUS INFORMATION$')

        # MM/DD/YYYY HH:MM:SS  | DEVNAME            | SLOT | TYP | COUNT  
        # --------------------------------------------------------------
        #  04/01/2023 09:04:24   obfl0:                3      1     20 
        #  04/03/2023 19:34:23   obfl0:                3      1     20
        p4_1= re.compile(r'^(?P<date>\d{2}\/\d{2}\/\d{4})\s(?P<time>\d+:\d+:\d+)\s(?P<devname>\w+)\:\s+(?P<slot>\d+)\s+(?P<typ>\d+)\s+(?P<count>\d+)$')

        # VID | PID                | TAN        | S.NO
        # ---------------------------------------------------
        # V02   C9400-SUP-1XL        A0           JAE22350Z2M
        # V02   C9400-SUP-1XL        A0           JAE22350Z2M
        p4_2= re.compile(r'^(?P<vid>\w+)\s+(?P<pid>\w+\-\w+\-\w+)\s+(?P<tan>\w+)\s+(?P<serial_no>\w+)$')
        for line in output.splitlines():
            line = line.strip()

            # COUNTER SUMMARY INFORMATION
            m = p1.match(line)
            if m:
                count = 0
                ret_dict.setdefault('counter_summary_info', {})
                continue

            # ERROR TYPE | VID  |     PID    |      TAN    SNO         |  COUNT
            # ------------------------------------------------------------------
            # 1            ,V02,    C9400-SUP-1XL   ,A0  ,JAE22300GFU,     20
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                count += 1
                count_value= group['count']
                error_type= group['error_type']
                sum_dict_child = group.pop('error_type')
                sum_dict_child = group.pop('count')
                sum_dict_child = ret_dict.setdefault('counter_summary_info', {}).setdefault(count, {})
                sum_dict_child['count']=int(count_value)
                sum_dict_child['error_type']=int(error_type)
                sum_dict_child.update({k: v for k, v in group.items()})
                continue

            # ERROR TYPE | VID  |     PID    |      TAN    SNO         |  COUNT
            # -----------------------------------------------------------------
            # 1            ,,    C9400-SUP-1XL   ,  A0  ,JAE22300GFU,      20
            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                count += 1
                count_value= group['count']
                error_type= group['error_type']
                sum_dict_child = group.pop('count')
                sum_dict_child = group.pop('error_type')
                sum_dict_child = ret_dict.setdefault('counter_summary_info', {}).setdefault(count, {})
                sum_dict_child['count']=int(count_value)
                sum_dict_child['error_type']=int(error_type)
                sum_dict_child['vid']= ""
                sum_dict_child.update({k: v for k, v in group.items()})
                continue

            # ERROR TYPE | VID  |     PID    |      TAN    SNO         |  COUNT
            # -----------------------------------------------------------------
            # No historical data
            m = p2_3.match(line)
            if m:
                group= m.groupdict()
                no_data = group['no_data']
                sum_dict_child = ret_dict.setdefault('counter_summary_info', {}).setdefault(no_data, {})
                continue

            # COUNTER LOGGING CONTINUOUS INFORMATION
            m = p3.match(line)
            if m:
                ret_dict.setdefault('counter_logging_continous_info', {})
                continue

            # MM/DD/YYYY HH:MM:SS  | DEVNAME            | SLOT | TYP | COUNT  
            # --------------------------------------------------------------
            #  04/01/2023 09:04:24   obfl0:                3      1     20 
            #  04/03/2023 19:34:23   obfl0:                3      1     20
            m = p4_1.match(line)
            if m:
                group= m.groupdict()
                counter += 1
                typ= group['typ']
                slot= group['slot']
                count_value= group['count']
                con_dict_child = group.pop('typ')
                con_dict_child = group.pop('slot')
                con_dict_child = group.pop('count')
                con_dict_child = ret_dict.setdefault('counter_logging_continous_info', {}).setdefault(counter, {})
                con_dict_child.update({k: v for k, v in group.items()})
                con_dict_child['slot']=int(slot)
                con_dict_child['typ']=int(typ)
                con_dict_child['count']=int(count_value)
                continue

            # VID | PID                | TAN        | S.NO
            # ---------------------------------------------------
            # V02   C9400-SUP-1XL        A0           JAE22350Z2M
            # V02   C9400-SUP-1XL        A0           JAE22350Z2M
            m = p4_2.match(line)
            if m:
                group= m.groupdict()
                con_dict_child = ret_dict.setdefault('counter_logging_continous_info', {}).setdefault(counter, {})
                con_dict_child.update({k: v for k, v in group.items()})
                continue
        return ret_dict

class ShowLoggingOnboardSwitchClilogDetailSchema(MetaParser):
    '''Schema for:
        'show logging onboard rp active clilog detail'
    '''   
    schema = {
        'cli_summary_info':{
            Any(): {
                Optional('command'): str,
                Optional('count'): int,
            },
        }, 
        'cli_continuous_info':{
            Any(): {
                Optional('command'): str,
                Optional('date'): str,
                Optional('time'): str,
            },
        },

    }
class ShowLoggingOnboardSwitchClilogDetail(ShowLoggingOnboardSwitchClilogDetailSchema):
    
    '''Schema for:
        'show logging onboard rp active clilog detail'
    ''' 
    cli_command = 'show logging onboard rp {switch_type} clilog detail'
				   
    def cli(self, switch_type="active", output=None): 

        if output is None: 
            # Build and Execute the command
            output = self.device.execute(self.cli_command.format(switch_type=switch_type))
        # init variables
        ret_dict = {}
        counter= 0

        # regex pattern

        # CLI LOGGING SUMMARY INFORMATION
        p1 = re.compile(r'^CLI LOGGING SUMMARY INFORMATION$')

        # COUNT COMMAND
        # --------------------------------------------------------------------------------
        # No summary data to display

        p2_1= re.compile(r'^(?P<no_sum_data>No summary data to display)$')

        # COUNT COMMAND
        # --------------------------------------------------
        #  1    show logging onboard RP active clilog detail
        #  1    show logging onboard RP active counter detail
        p2_2 = re.compile(r'^(?P<count>\d+)\s+(?P<command>show.*)$')

        # COUNTER LOGGING CONTINUOUS INFORMATION
        p3 = re.compile(r'^CLI LOGGING CONTINUOUS INFORMATION$')


        # --------------------------------------------------------------------------------
        # MM/DD/YYYY HH:MM:SS COMMAND
        # --------------------------------------------------------------------------------

        # No continuous data
        p4_1 = re.compile(r'^(?P<no_cont_data>No continuous data)$')

        # MM/DD/YYYY HH:MM:SS COMMAND
        # -----------------------------------------------------------------
        #  03/30/2023 02:41:08 show logging onboard RP active clilog detail
        #  03/30/2023 02:41:43 show logging onboard RP active counter detail
        p4_2= re.compile(r'^(?P<date>\d{2}\/\d{2}\/\d{4})\s(?P<time>\d+:\d+:\d+)\s(?P<command>show.*)$')

        for line in output.splitlines():
            line = line.strip()

            # CLI LOGGING SUMMARY INFORMATION
            m = p1.match(line)
            if m:
                count = 0
                ret_dict.setdefault('cli_summary_info', {})
                continue

            # COUNT COMMAND
            # ----------------------------------------------------------------
            # No summary data to display
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                no_sum_data= group['no_sum_data']
                sum_dict_child = ret_dict.setdefault('cli_summary_info', {}).setdefault(no_sum_data, {})
                continue

            # COUNT COMMAND
            # --------------------------------------------------
            #  1    show logging onboard RP active clilog detail
            #  1    show logging onboard RP active counter detail
            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                count_value= group['count']
                sum_dict_child = group.pop('count')
                count += 1
                sum_dict_child = ret_dict.setdefault('cli_summary_info', {}).setdefault(count, {})
                sum_dict_child.update({k: v for k, v in group.items()})
                sum_dict_child['count']=int(count_value)
                continue


            # CLI LOGGING CONTINUOUS INFORMATION
            m = p3.match(line)
            if m:
                ret_dict.setdefault('cli_continuous_info', {})
                continue
            # MM/DD/YYYY HH:MM:SS COMMAND
            # --------------------------------------------------------------------------------
            # No continuous data
            m = p4_1.match(line)
            if m:
                group= m.groupdict()
                no_cont_data= group['no_cont_data']
                con_dict_child = ret_dict.setdefault('cli_continuous_info', {}).setdefault(no_cont_data, {})
                continue

            # MM/DD/YYYY HH:MM:SS COMMAND
            # -----------------------------------------------------------------
            #  03/30/2023 02:41:08 show logging onboard RP active clilog detail
            #  03/30/2023 02:41:43 show logging onboard RP active counter detail
            m = p4_2.match(line)
            if m:
                group= m.groupdict()
                counter +=1
                con_dict_child = ret_dict.setdefault('cli_continuous_info', {}).setdefault(counter, {})
                con_dict_child.update({k: v for k, v in group.items()})
                continue
        return ret_dict