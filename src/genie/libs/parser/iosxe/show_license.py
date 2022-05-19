''' show_license.py

IOSXE parsers for the following show commands:
    * show license
    * show license udi
    * show license summary
    * show license rum id all
    * show license status
    * show license rum id detail
    * show license all
    * show license eventlog 2
    * show license usage
    * show license tech support

'''

#Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or, ListOf

# parser utils
from genie.libs.parser.utils.common import Common

# =================
# Schema for:
#  * 'show license'
# =================

class ShowLicenseSchema(MetaParser):
    """Schema for show license."""

    schema = {
        'licenses': {
            int: {
                'feature': str,
                Optional('period_left'): str,
                Optional('period_minutes'): int,
                Optional('period_seconds'): int,
                Optional('license_type'): str,
                Optional('license_state'): str,
                Optional('count_in_use'): int,
                Optional('count_violation'): int,
                Optional('count'): str,
                Optional('license_priority'): str

            }
        }
    }



# =================
# Parser for:
#  * 'show license'
# =================
class ShowLicense(ShowLicenseSchema):
    """Parser for show license"""

    cli_command = 'show license'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Index 1 Feature: appxk9
        p1 = re.compile(r"Index\s+(?P<id>\d+)\s+Feature:\s+(?P<feature>\S+)")
        #         Period left: Life time
        p2 = re.compile(r"\s+(?P<period_left>(Life\s+time|Not\s+Activated))")
        #           Period Used: 0  minute  0  second
        p3 = re.compile(r"\s+(?P<period_minutes>\d+)\s+minute\s+(?P<period_seconds>\d+)\s+second")
        #         License Type: Permanent
        p4 = re.compile(r"\s+(?P<license_type>(Permanent|EvalRightToUse))")
        #         License State: Active, In Use
        p5 = re.compile(r"\s+((?P<count_in_use>\d+)/(?P<count_violation>\d+)\s+\(In-use/Violation\)|(?P<count>\S+))")
        #         License Priority: None
        p6 = re.compile(r"\s+(?P<license_priority>\S+)")
        #         License State: Active, Not in Use
        #         License State: Active, Not in Use, EULA not accepted
        p7 = re.compile(r"\s+(?P<license_state>(Active,\s+Not\s+in\s+Use,\s+EULA\s+not\s+accepted|Active,\s+In\s+Use|Active,\s+Not in\s+Use))")

        regex_map = {
            "Period left": p2,
            "Period Used": p3,
            "License Type": p4,
            "License Count": p5,
            "License Priority": p6,
            "License State": p7,
        }

        # initial variables
        license_dict = {}
        # Index 1 Feature: appxk9
        #         Period left: Life time
        #         License Type: Permanent
        #         License State: Active, In Use
        #         License Count: Non-Counted
        #         License Priority: Medium

        for line in out.splitlines():
            line_strip = line.strip()
            if not line_strip.startswith("Index"):
                try:
                    data_type, value = line_strip.split(":", 1)
                    regex = regex_map.get(data_type)
                except ValueError:
                    continue
            else:
                match = p1.match(line_strip)
                # Index 1 Feature: appxk9
                groups = match.groupdict()
                group_id = int(groups['id'])
                license_dict.update({group_id: {'feature': groups['feature']}})
                continue

            if regex:
                match = regex.match(value)
                groups = match.groupdict()
                for k, v in groups.items():
                    if v is None:
                        continue
                    if v.isdigit():
                        v = int(v)
                    license_dict[group_id].update({k: v})

        if license_dict:
            return {"licenses": license_dict}
        else:
            return {}
# ----------------------
# ==================================
#  Schema for: 'show license udi'   
# ==================================

class ShowLicenseUdiSchema(MetaParser):
    """Schema for show license udi"""
    schema = {
        Optional('slotid'): str,
        Optional('pid'): str,
        Optional('sn'): str,
        Optional('udi'): str,
        Optional('primary_load_time_percent'): int,
        Optional('secondary_load_time_percent'): int,
        Optional('one_minute_load_percent'): int,
        Optional('five_minute_load_percent'): int,
        Optional('udi_details'):{
            Optional('pid'):str,
            Optional('sn'):str,
        },
        Optional('ha_udi_list'): {
            Optional('active'):{
                Optional('pid'):str,
                Optional('sn'):str,
            },
            Optional('standby'):{
                Optional('pid'):str,
                Optional('sn'):str,
            },
            Optional('member'):{
                Optional('pid'):str,
                Optional('sn'):str,
            }
        }
    }
       
# ==================================
#  Parser for: 'show license udi'   
# ==================================

class ShowLicenseUdi(ShowLicenseUdiSchema):
    """Parser for show license udi"""
    cli_command = 'show license udi'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict={}

        #Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
        p1 = re.compile(r'^Load for five secs:\s*(?P<primary_load_time_percent>[0-9])\%\/(?P<secondary_load_time_percent>[0-9])\%\;\s*one minute:\s*(?P<one_minute_load_percent>[0-9])\%\;\s*five minutes:\s*(?P<five_minute_load_percent>[0-9])\%')

        #Time source is NTP, .06:17:59.041 UTC Thu Sep 9 2021
        p2 = re.compile(r'^Time source is NTP, +(?P<time_source_is_ntp>.*)$')

        #UDI: PID:C9300-24UX,SN:FCW2303D16Y
        p3 = re.compile(r'^UDI: PID:(?P<pid>.*),SN:(?P<sn>.*)$')

        #Active: PID:C9300-24UX,SN:FCW2303D16Y
        p4 = re.compile(r'^Active:PID:(?P<pid>.*),SN:(?P<sn>.*)$')

        #Standby: PID:C9300-24U,SN:FHH2043P09E
        p5 = re.compile(r'^Standby:PID:(?P<pid>.*),SN:(?P<sn>.*)$')

        #Member: PID:C9300-48T,SN:FCW2139L056
        p6 = re.compile(r'^Member:PID:(?P<pid>.*),SN:(?P<sn>.*)$')

        #*        ASR1001-X             JAF211403VH     ASR1001-X:JAF211403VH
        p7 = re.compile(r'^(?P<slotid>\S+)\s+(?P<pid>\S+)\s+(?P<sn>\S+)\s+(?P<udi>\S+)')

        for line in output.splitlines():
          line = line.strip()

          #Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
          m = p1.match(line)
          if m:
            group = m.groupdict()
            group['primary_load_time_percent'] = int(group['primary_load_time_percent'])
            group['secondary_load_time_percent'] = int(group['secondary_load_time_percent'])
            group['one_minute_load_percent'] = int(group['one_minute_load_percent'])
            group['five_minute_load_percent'] = int(group['five_minute_load_percent'])
            ret_dict.update(group)
            continue

          #Time source is NTP, .06:17:59.041 UTC Thu Sep 9 2021
          m = p2.match(line)
          if m:
            continue

          #UDI: PID:C9300-24UX,SN:FCW2303D16Y
          m = p3.match(line)
          if m:
            group = m.groupdict()
            udi_dict = ret_dict.setdefault('udi_details', {})
            udi_dict.update(group)
            continue

          #Active: PID:C9300-24UX,SN:FCW2303D16Y
          m = p4.match(line)
          if m:
            group = m.groupdict()
            active_dict = ret_dict.setdefault('ha_udi_list', {})\
                                   .setdefault('active', {})
            active_dict.update(group)
            continue

          #Standby: PID:C9300-24U,SN:FHH2043P09E
          m = p5.match(line)
          if m:
            group = m.groupdict()
            standby_dict = ret_dict.setdefault('ha_udi_list', {})\
                                   .setdefault('standby', {})
            standby_dict.update(group)
            continue

          #Member: PID:C9300-48T,SN:FCW2139L056
          m = p6.match(line)
          if m:
            group = m.groupdict()
            member_dict = ret_dict.setdefault('ha_udi_list', {})\
                                   .setdefault('member', {})
            member_dict.update(group)
            continue

          #*        ASR1001-X             JAF211403VH     ASR1001-X:JAF211403VH
          m = p7.match(line)
          if m:
            group = m.groupdict()
            ret_dict.update(group)
            continue

        return ret_dict

# ----------------------
# =================
# Schema for:
#  * 'show license summary'
# =================
class ShowLicenseSummarySchema(MetaParser):
    """Schema for show license summary"""
    schema = {
        Optional('account_information'): {
            Optional('smart_account'): str,
            Optional('virtual_account'): str,
        },
        Optional('license_usage'): {
            Any():{
                'license': str,
                'entitlement': str,
                'count': str,
                'status': str,
            }
        }
    }

# =================
# Parser for:
#  * 'show license summary'
# =================
class ShowLicenseSummary(ShowLicenseSummarySchema):
    """Parser for show license summary"""
    cli_command = 'show license summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict={}

        #Smart Account: SA-Switching-Polaris As of Jul 16 07:08:31 2021 PST
        p1 = re.compile(r'^Smart +Account: +(?P<smart_account>.*)$')

        #Virtual Account: SLE_Test
        p2 = re.compile(r'^Virtual +Account: +(?P<virtual_account>.*)$')

        #network-advantage       (C9300-48 Network Advan...)       1 IN USE
        p3 = re.compile(r'^(?P<license>.+?)\s+\((?P<entitlement>.+)\)\s+(?P<count>\d+)\s+(?P<status>.+)$')

        for line in output.splitlines():
            line=line.strip()

            #Smart Account: SA-Switching-Polaris As of Jul 16 07:08:31 2021 PST
            m=p1.match(line)
            if m:
                group = m.groupdict()
                account_information_dict=ret_dict.setdefault('account_information',{})
                account_information_dict.setdefault('smart_account',group['smart_account'])
                continue

            #Virtual Account: SLE_Test
            m=p2.match(line)
            if m:
                group=m.groupdict()
                account_information_dict.setdefault('virtual_account',group['virtual_account'])
                continue

            #network-advantage       (C9300-48 Network Advan...)       1 IN USE
            m=p3.match(line)
            if m:
                group=m.groupdict()
                entitlement=group.setdefault('entitlement',{})
                license_usage_dict=ret_dict.setdefault('license_usage', {})
                license_usage_dict[entitlement]={k:v for k,v in group.items()}

        return ret_dict

# =================
# Schema for:
#  * 'show license rum id all'
# =================

class ShowLicenseRumIdAllSchema(MetaParser):
    """Schema for show license rum id all."""
    schema = {
        'smart_license_usage_reports': {
            Any(): {
                'state': str,
                'flag': str,
                'feature_name': str
                }
        }
    }

# =================
# Parser for:
#  * 'show license rum id all'
# =================
class ShowLicenseRumIdAll(ShowLicenseRumIdAllSchema):
    """Parser for show license rum id all"""

    cli_command = 'show license rum id all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}

        # 1629870048          CLOSED    N     network-premier_2.5G
        p1 = re.compile(r'^(?P<report_id>\d+)\s+(?P<state>\S+)\s+(?P<flag>\w+)\s+(?P<feature_name>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            m =p1.match(line)
            if m:
                groups =m.groupdict()
                report_id = int(groups['report_id'])
                rum_id_dict = ret_dict.setdefault('smart_license_usage_reports', {}).setdefault(report_id, {})
                rum_id_dict['state'] = groups['state']
                rum_id_dict['flag'] =  groups['flag']
                rum_id_dict['feature_name'] = groups['feature_name']
                continue
        return ret_dict
        
# --------------------------------------------------------------------------------------------------------------
# ======================================
#  Schema for: 'show license status'   
# ======================================

class ShowLicenseStatusSchema(MetaParser):
    schema={
      Optional('load_for_five_secs'): str,
      Optional('one_minute'): str,
      Optional('five_minutes'): str,
      Optional('time_source_is_ntp'): str,
      Optional('utility'):{
        'status':str,
      },
      Optional('smart_licensing_using_policy'):{
        'status':str,
      },
      Optional('account_information'):{
       'smart_account':str,
       'virtual_account':str,
      },
      Optional('data_privacy'):{
       'sending_hostname':str,
       'callhome_hostname_privacy':str,
       'smart_licensing_hostname_privacy':str,
       'version_privacy':str,
      },
      Optional('transport'):{
       'type':str,
       Optional('url'):str,
       Optional('cslu_address'):str,
       Optional('proxy'):str,
       Optional('vrf'):str,
      },
      Optional('policy'):{
       'policy_in_use':str,
       Optional('policy_name'):str,
       'reporting_ack_required':str,
       'unenforced_non_export_perpetual_attributes':{
          'first_report_requirement_days':str,
          'reporting_frequency_days':str,
          'report_on_change_days':str,
        },
       'unenforced_non_export_subscription_attributes':{
          'first_report_requirement_days':str,
          'reporting_frequency_days':str,
          'report_on_change_days':str,
        },
       'enforced_perpetual_subscription_license_attributes':{
          'first_report_requirement_days':str,
          'reporting_frequency_days':str,
          'report_on_change_days':str,
        },
       'export_perpetual_subscription_license_attributes':{
          'first_report_requirement_days':str,
          'reporting_frequency_days':str,
          'report_on_change_days':str,
        },
      },
      Optional('miscellaneous'):{
       'custom_id':str,
      },
      Optional('usage_reporting'):{
       'last_ack_received':str,
       'next_ack_deadline':str,
       'reporting_push_interval':str,
       'next_ack_push_check':str,
       'next_report_push':str,
       'last_report_push':str,
       'last_report_file_write':str,
      },
      Optional('trust_code_installed'):Or(str, dict),
       Optional('active'):{
          Optional('pid'):str,
          Optional('sn'):str,
          Optional('info'):str,
       },
       Optional('standby'):{
          Optional('pid'):str,
          Optional('sn'):str,
          Optional('info'):str,
       },
       Optional('member'):{
          Optional('pid'):str,
          Optional('sn'):str,
          Optional('info'):str,
       }
    }
  
# ======================================
#  Parser for: 'show license status'   
# ======================================

class ShowLicenseStatus(ShowLicenseStatusSchema):
    """ Parser for show license status """
   
    cli_command = 'show license status'

    def cli(self, output=None):
        if output is None:        
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict={}
        result_dict={}
        res=out.splitlines()

        #Load for five secs: 2%/0%; one minute: 2%; five minutes: 3%
        p1=re.compile(r'^Load for five secs: +(?P<load_for_five_secs>.*); +one +minute: +(?P<one_minute>.*); +five +minutes: +(?P<five_minutes>.*)$')

        #Time source is NTP, 11:41:04.102 UTC Mon Sep 13 2021
        p2=re.compile(r'^Time source is NTP, +(?P<time_source_is_ntp>.*)$')

        #Utility:
        p3= re.compile(r'^Utility:+(?P<utility>.*)$')
        #Status: DISABLED
        p3_1= re.compile(r'^Status: +(?P<status>(ENABLED|DISABLED))$')

        #Smart Licensing Using Policy:
        p4= re.compile(r'^Smart +Licensing +Using +Policy:+(?P<smart_licensing_using_policy>.*)$')

        #Account Information:
        p5= re.compile(r'^Account +Information:+(?P<account_information>.*)$')
        #Smart Account: SA-Switching-Polaris As of Sep 27 12:59:45 2021 UTC
        p5_1= re.compile(r'^Smart +Account: +(?P<smart_account>.*)$')
        # Virtual Account: SLE_Test
        p5_2= re.compile(r'^Virtual +Account: +(?P<virtual_account>.*)$')

        #Data Privacy:
        p6= re.compile(r'^Data +Privacy:+(?P<data_privacy>.*)$')
        #Sending Hostname: yes
        p6_1= re.compile(r'^Sending +Hostname: +(?P<sending_hostname>.*)$')
        #Callhome hostname privacy: DISABLED
        p6_2= re.compile(r'^Callhome +hostname +privacy: +(?P<callhome_hostname_privacy>.*)$')
        #Smart Licensing hostname privacy: DISABLED
        p6_3= re.compile(r'^Smart +Licensing +hostname +privacy: +(?P<smart_licensing_hostname_privacy>.*)$')
        #Version privacy: DISABLED
        p6_4= re.compile(r'^Version +privacy: +(?P<version_privacy>.*)$')

        #Transport:
        p7= re.compile(r'^Transport:+(?P<transport>.*)$')
        #Type: cslu
        p7_1 = re.compile(r'^Type: +(?P<type>.*)$')
        #URL: https://smartreceiver-stage.cisco.com/licservice/license
        p7_2 = re.compile(r'^URL: +(?P<url>.*)$')
        #Cslu address: <empty>
        p7_3 = re.compile(r'^Cslu +address: +(?P<cslu_address>.*)$')
        #Proxy:
        p7_4 = re.compile(r'^Proxy:+(?P<proxy>.*)$')
        #Not Configured
        p7_5=re.compile(r'^Not +Configured$')
        #VRF:
        p7_6 = re.compile(r'^VRF:+(?P<vrf>.*)$')


        #Policy:
        p8 = re.compile(r'^Policy:+(?P<policy>.*)$')
        #Policy in use: Installed On Sep 27 12:22:33 2021 UTC
        p8_1 = re.compile(r'^Policy +in +use: +(?P<policy_in_use>.*)$')
        #Policy name: Custom Policy
        p8_2 = re.compile(r'^Policy +name: +(?P<policy_name>.*)$')
        #Reporting ACK required: yes (Customer Policy)
        p8_3 = re.compile(r'^Reporting +ACK +required: +(?P<reporting_ack_required>.*)$')
        #Unenforced/Non-Export Perpetual Attributes:
        p8_4 = re.compile(r'^Unenforced/Non-Export +Perpetual +Attributes:+(?P<unenforced_non_export_perpetual_attributes>.*)$')
        #First report requirement (days): 365 (Customer Policy)
        p8_5 = re.compile(r'^First +report +requirement +\(days\): +(?P<first_report_requirement_days>.*)$')
        #Reporting frequency (days): 0 (Customer Policy)
        p8_6 = re.compile(r'^Reporting +frequency +\(days\): +(?P<reporting_frequency_days>.*)$')
        #Report on change (days): 90 (Customer Policy)
        p8_7 = re.compile(r'^Report +on +change +\(days\): +(?P<report_on_change_days>.*)$')
        #Unenforced/Non-Export Subscription Attributes:
        p8_8 = re.compile(r'^Unenforced/Non-Export +Subscription +Attributes:+(?P<unenforced_non_export_subscription_attributes>.*)$')
        #Enforced (Perpetual/Subscription) License Attributes:
        p8_9 = re.compile(r'^Enforced +\(Perpetual/Subscription\) +License +Attributes:+(?P<enforced_perpetual_subscription_license_attributes>.*)$')
        #Export (Perpetual/Subscription) License Attributes:
        p8_10 = re.compile(r'^Export +\(Perpetual/Subscription\) +License +Attributes:+(?P<export_perpetual_subscription_license_attributes>.*)$')


        #Miscellaneous:
        p9 = re.compile(r'^Miscellaneous:+(?P<miscellaneous>.*)$')
        #Custom Id: <empty>
        p9_1 = re.compile(r'^Custom +Id: +(?P<custom_id>.*)$')

        #Usage Reporting:
        p10 = re.compile(r'^Usage +Reporting:+(?P<usage_reporting>.*)$')
        #Last ACK received: <none>
        p10_1 = re.compile(r'^Last +ACK +received: +(?P<last_ack_received>.*)$')
        #Next ACK deadline: Dec 26 12:32:14 2021 UTC
        p10_2 = re.compile(r'^Next +ACK +deadline: +(?P<next_ack_deadline>.*)$')
        #Reporting push interval: 30  days
        p10_3 = re.compile(r'^Reporting +push +interval: +(?P<reporting_push_interval>.*)$')
        #Next ACK push check: Sep 29 16:39:27 2021 UTC
        p10_4 = re.compile(r'^Next +ACK +push +check: +(?P<next_ack_push_check>.*)$')
        #Next report push: Sep 29 13:51:16 2021 UTC
        p10_5 = re.compile(r'^Next +report +push: +(?P<next_report_push>.*)$')
        #Last report push: Sep 27 12:59:50 2021 UTC
        p10_6= re.compile(r'^Last +report +push: +(?P<last_report_push>.*)$')
        #Last report file write: <none>
        p10_7 = re.compile(r'^Last +report +file +write: +(?P<last_report_file_write>.*)$')

        #Trust Code Installed:
        p11 = re.compile(r'^Trust +Code +Installed:+(?P<trust_code_installed>.*)$')
        #Active:
        p11_1=re.compile(r'^Active: +(?P<active>)')
        #Active: PID:C9300-24UX,SN:FCW2303D16Y
        p11_2=re.compile(r'^Active: +(?P<active>)+PID:+(?P<pid>.*),+SN:+(?P<sn>.*)$')
        #INSTALLED on Sep 27 12:22:33 2021 UTC
        p11_3=re.compile(r'^INSTALLED +on +.*|^<none>.*')
        #Standby:
        p11_4=re.compile(r'^Standby: +(?P<standby>)')
        # Standby: PID:C9300-24U,SN:FHH2043P09E
        p11_5=re.compile(r'^Standby: +(?P<standby>)+PID:+(?P<pid>.*),+SN:+(?P<sn>.*)$')
        #Member:
        p11_6=re.compile(r'^Member: +(?P<member>)')
        #Member: PID:C9300-48T,SN:FCW2139L056
        p11_7=re.compile(r'^Member: +(?P<member>)+PID:+(?P<pid>.*),+SN:+(?P<sn>.*)$')

        for line in res:
          line=line.strip()

          #Load for five secs: 2%/0%; one minute: 2%; five minutes: 3%
          m=p1.match(line)
          if m:
              group=m.groupdict()
              ret_dict.update(group)
              continue

          #Time source is NTP, 11:41:04.102 UTC Mon Sep 13 2021
          m=p2.match(line)
          if m:
              group=m.groupdict()
              ret_dict.update(group)
              continue

          #Utility:
          m = p3.match(line)
          if m:   
            group = m.groupdict()
            result_dict.update(group)
            continue

          #Status: DISABLED
          m = p3_1.match(line)
          if m:   
            group = m.groupdict()
            if result_dict.get('utility')=='':
              result_dict['utility']=group
            else:
              ret_dict['smart_licensing_using_policy']=group
            if result_dict:
              ret_dict.update(result_dict)
              result_dict={}
            continue

          #Smart Licensing Using Policy:
          m = p4.match(line)
          if m:
            group = m.groupdict()
            ret_dict.update(group)
            continue

          #Account Information:
          m = p5.match(line)
          if m:
            group = m.groupdict()
            result_dict.update(group)
            continue

          #Smart Account: SA-Switching-Polaris As of Sep 27 12:59:45 2021 UTC
          m = p5_1.match(line)
          if m:
            group = m.groupdict()
            result_dict['account_information']=group
            ret_dict.update(result_dict)
            continue

          #Virtual Account: SLE_Test
          m = p5_2.match(line)
          if m:
            group = m.groupdict() 
            result_dict['account_information'].update(group)
            ret_dict.update(result_dict)
            result_dict={}
            continue

          #Data Privacy:
          m = p6.match(line)
          if m:
            group = m.groupdict()
            result_dict.update(group)
            continue

          #Sending Hostname: yes
          m = p6_1.match(line)
          if m:
            group = m.groupdict()
            result_dict['data_privacy']=group
            continue

          #Callhome hostname privacy: DISABLED
          m = p6_2.match(line)
          if m:
            group = m.groupdict()
            result_dict['data_privacy'].update(group)
            ret_dict.update(result_dict)
            continue

          #Smart Licensing hostname privacy: DISABLED
          m = p6_3.match(line)
          if m:
            group = m.groupdict()
            result_dict['data_privacy'].update(group)
            ret_dict.update(result_dict)
            continue

          #Version privacy: DISABLED
          m = p6_4.match(line)
          if m:
            group = m.groupdict()
            result_dict['data_privacy'].update(group)
            ret_dict.update(result_dict)
            result_dict={}
            continue

          #Transport:
          m = p7.match(line)
          if m:
            group = m.groupdict()
            result_dict.update(group)
            continue

          #Type: cslu
          m = p7_1.match(line)
          if m:
            group = m.groupdict()
            result_dict['transport']=group
            continue

          #URL: https://smartreceiver-stage.cisco.com/licservice/license
          m = p7_2.match(line)
          if m:
            group = m.groupdict()
            result_dict['transport'].update(group)
            continue

          #Cslu address: <empty>
          m = p7_3.match(line)
          if m:
            group = m.groupdict()
            result_dict['transport'].update(group)
            continue

          #Proxy:
          m = p7_4.match(line)
          if m:
            group = m.groupdict()
            result_dict['transport'].update(group)
            continue

          #Not Configured
          m = p7_5.match(line)
          if m:
            if result_dict['transport'].get('proxy')=='':
              result_dict['transport']['proxy']=m.group(0)
            else:
              result_dict['transport']['vrf']=m.group(0)
              ret_dict.update(result_dict)
              result_dict={}
            continue

          #VRF:
          m = p7_6.match(line)
          if m:
            group = m.groupdict()
            result_dict['transport'].update(group)
            continue


          #Policy:
          m = p8.match(line)
          if m:
            group = m.groupdict()
            result_dict.update(group)
            continue

          #Policy in use: Installed On Aug 04 04:03:37 2021 UTC
          m = p8_1.match(line)
          if m:
            group = m.groupdict()
            result_dict['policy']=group
            ret_dict.update(result_dict)
            continue

          #Policy name: Custom Policy
          m = p8_2.match(line)
          if m:
            group = m.groupdict()
            result_dict['policy'].update(group)
            ret_dict.update(result_dict)
            continue

          #Reporting ACK required: yes (Customer Policy)
          m = p8_3.match(line)
          if m:
            group = m.groupdict()
            result_dict['policy'].update(group)
            ret_dict.update(result_dict)
            continue

          #Unenforced/Non-Export Perpetual Attributes:
          m = p8_4.match(line)
          if m:
            group = m.groupdict()
            result_dict['policy'].update(group)
            ret_dict.update(result_dict)
            continue

          #First report requirement (days): 365 (Customer Policy)
          m = p8_5.match(line)
          if m:
            group = m.groupdict()
            if result_dict['policy'].get('unenforced_non_export_perpetual_attributes')=='':
              result_dict['policy']['unenforced_non_export_perpetual_attributes']=group
            if result_dict['policy'].get('unenforced_non_export_subscription_attributes')=='':
              result_dict['policy']['unenforced_non_export_subscription_attributes']=group
            if result_dict['policy'].get('enforced_perpetual_subscription_license_attributes')=='':
              result_dict['policy']['enforced_perpetual_subscription_license_attributes']=group
            if result_dict['policy'].get('export_perpetual_subscription_license_attributes')=='':
              result_dict['policy']['export_perpetual_subscription_license_attributes']=group
            continue

          #Reporting frequency (days): 0 (Customer Policy)
          m = p8_6.match(line)
          if m:
            group = m.groupdict()
            if result_dict['policy'].get('unenforced_non_export_perpetual_attributes').get('reporting_frequency_days'):
              if result_dict['policy'].get('unenforced_non_export_subscription_attributes').get('reporting_frequency_days'):
                if result_dict['policy'].get('enforced_perpetual_subscription_license_attributes').get('reporting_frequency_days'):
                  if result_dict['policy'].get('export_perpetual_subscription_license_attributes').get('reporting_frequency_days'):
                    continue
                  else:
                    result_dict['policy']['export_perpetual_subscription_license_attributes'].update(group)
                else:
                  result_dict['policy']['enforced_perpetual_subscription_license_attributes'].update(group)
              else:  
                result_dict['policy']['unenforced_non_export_subscription_attributes'].update(group)
            else:  
              result_dict['policy']['unenforced_non_export_perpetual_attributes'].update(group)
            continue

          #Report on change (days): 90 (Customer Policy)
          m = p8_7.match(line)
          if m:
            group = m.groupdict()
            if result_dict['policy'].get('unenforced_non_export_perpetual_attributes').get('report_on_change_days'): 
              if result_dict['policy'].get('unenforced_non_export_subscription_attributes').get('report_on_change_days'):
                if result_dict['policy'].get('enforced_perpetual_subscription_license_attributes').get('report_on_change_days'):
                  if result_dict['policy'].get('export_perpetual_subscription_license_attributes').get('report_on_change_days'):
                    continue
                  else:
                    result_dict['policy']['export_perpetual_subscription_license_attributes'].update(group)
                else:
                  result_dict['policy']['enforced_perpetual_subscription_license_attributes'].update(group)
              else:
                result_dict['policy']['unenforced_non_export_subscription_attributes'].update(group)
            else:
              result_dict['policy']['unenforced_non_export_perpetual_attributes'].update(group)
            continue

          #Unenforced/Non-Export Subscription Attributes:
          m = p8_8.match(line)
          if m:
            group = m.groupdict()
            result_dict['policy'].update(group)
            continue

          #Enforced (Perpetual/Subscription) License Attributes:
          m = p8_9.match(line)
          if m:
            group = m.groupdict()
            result_dict['policy'].update(group)
            continue
          
          #Export (Perpetual/Subscription) License Attributes:
          m = p8_10.match(line)
          if m:
            group = m.groupdict()
            result_dict['policy'].update(group)
            ret_dict.update(result_dict)
            continue

          #Miscellaneous:
          m = p9.match(line)
          if m:
            result_dict={}
            group = m.groupdict()
            result_dict.update(group)
            continue

          #Custom Id: <empty>
          m = p9_1.match(line)
          if m:
            group = m.groupdict()
            result_dict['miscellaneous']=group
            ret_dict.update(result_dict)
            continue

          #Usage Reporting:
          m = p10.match(line)
          if m:
            result_dict={}
            group = m.groupdict()
            result_dict.update(group)
            continue

          #Last ACK received: Aug 04 04:03:37 2021 UTC
          m = p10_1.match(line)
          if m:
            group = m.groupdict()
            result_dict['usage_reporting']=group
            ret_dict.update(result_dict)
            continue

          #Next ACK deadline: Nov 02 04:03:37 2021 UTC
          m = p10_2.match(line)
          if m:
            group = m.groupdict()
            result_dict['usage_reporting'].update(group)
            ret_dict.update(result_dict)
            continue

          #Reporting push interval: 30  days
          m = p10_3.match(line)
          if m:
            group = m.groupdict()
            result_dict['usage_reporting'].update(group)
            ret_dict.update(result_dict)
            continue

          #Next ACK push check: <none>
          m = p10_4.match(line)
          if m:
            group = m.groupdict()
            result_dict['usage_reporting'].update(group)
            ret_dict.update(result_dict)
            continue

          #Next report push: Aug 04 05:35:24 2021 UTC
          m = p10_5.match(line)
          if m:
            group = m.groupdict()
            result_dict['usage_reporting'].update(group)
            ret_dict.update(result_dict)
            continue

          #Last report push: <none>
          m = p10_6.match(line)
          if m:
            group = m.groupdict()
            result_dict['usage_reporting'].update(group)
            ret_dict.update(result_dict)
            continue

          #Last report file write: <none>
          m = p10_7.match(line)
          if m:
            group = m.groupdict()
            result_dict['usage_reporting'].update(group)
            ret_dict.update(result_dict)
            continue

          #Trust Code Installed:
          m = p11.match(line)
          if m:
            result_dict={}
            group = m.groupdict()
            result_dict.update(group)
            continue

          #Active:
          m = p11_1.match(line)
          if m:
            active=m.groupdict()
            #Active: PID:C9300-24UX,SN:FCW2303D16Y
            m=p11_2.match(line)
            if m:
              group=m.groupdict()
              group.pop('active')
              active['active']=group
              result_dict['trust_code_installed']=active
              continue
          #INSTALLED on Sep 27 12:22:33 2021 UTC | <none>
          m = p11_3.match(line)
          if m:
            group = m.group(0)
            if not result_dict['trust_code_installed']['active'].get('info'):
              result_dict['trust_code_installed']['active'].update({'info':group})
            elif not result_dict['trust_code_installed']['standby'].get('info'):
              result_dict['trust_code_installed']['standby'].update({'info':group})
            else:
              result_dict['trust_code_installed']['member'].update({'info':group})
            continue

          #Standby:
          m=p11_4.match(line)
          if m:
            standby=m.groupdict()
            #Standby: PID:C9300-24U,SN:FHH2043P09E
            m=p11_5.match(line)
            if m:
              group=m.groupdict()
              group.pop('standby')
              standby['standby']=group
              result_dict['trust_code_installed'].update(standby)
              continue

          #Member:
          m=p11_6.match(line)
          if m:
            member=m.groupdict()
            #Member: PID:C9300-48T,SN:FCW2139L056
            m=p11_7.match(line)
            if m:
              group=m.groupdict()
              group.pop('member')
              member['member']=group
              result_dict['trust_code_installed'].update(member)
              ret_dict.update(result_dict)
              continue

        if result_dict:
          ret_dict.update(result_dict)
        return ret_dict

# =========================================
# Schema for: 'show license rum id detail'
# =========================================

class ShowLicenseRumIdDetailSchema(MetaParser):
    """Schema for show license rum id detail"""
    schema = {
      Optional('report_id'): {
        Any():{
          'metric_name': str,
          'feature_name': str,
          'metric_value': str,
          Optional('udi'): {
            Optional('pid'): str,
            Optional('sn'): str,
          },
          'previous_report_id': str,
          'next_report_id': str,
          'state': str,
          'state_change_reason': str,
          'start_time': str,
          'end_time': str,
          'storage_state': str,
          'transaction_id': str,
          'transaction_message': str,
        }
      }
    }
    
# ==========================================
#  Parser for: 'show license rum id detail'   
# ==========================================           

class ShowLicenseRumIdDetail(ShowLicenseRumIdDetailSchema):
    """Parser for show license rum id detail"""
    
    cli_command = 'show license rum id {report} detail'

    def cli(self, report = "",  output=None):
        if output is None:
            cmd = self.cli_command.format(report=report)
            output = self.device.execute(cmd)
            
        ret_dict={}

        #Report Id: 1631796710
        p1 = re.compile(r'^Report +Id: +(?P<report_id>.*)$')

        #Feature Name: dna-advantage
        p2 = re.compile(r'^Feature +Name: +(?P<feature_name>.*)$')

        #Metric Name: ENTITLEMENT
        p3 = re.compile(r'^Metric +Name: +(?P<metric_name>.*)$')

        #UDI:
        p4=re.compile(r'^UDI:+(?P<udi>)')
        #UDI: PID:C9300-24UX,SN:FCW2303D16Y
        p4_1=re.compile(r'^UDI:+(?P<udi>) +PID:+(?P<pid>.*),+SN:+(?P<sn>.*)$')

        #Metric Value: regid.2017-05.com.cisco.C9300_48P_Dna_Advantage,1.0_60783b06-53ee-484c-b21e-615d3cf6837a
        p5 = re.compile(r'^Metric +Value: +(?P<metric_value>.*)$')

        #Previous Report Id: 1631796706,    Next Report Id: 1631796714
        p6 = re.compile(r'^Previous +Report +Id: +(?P<previous_report_id>[\S ]+), +'
                        r'Next +Report +Id: +(?P<next_report_id>.*)$')

        #State: CLOSED,      State Change Reason: REPORTING
        p7 = re.compile(r'^State: +(?P<state>[\S ]+), +'
                        r'State +Change +Reason: +(?P<state_change_reason>.*)$')

        #Start Time: Sep 19 05:12:48 2021 UTC,      End Time: Sep 19 05:21:41 2021 UTC
        p8 = re.compile(r'^Start +Time: +(?P<start_time>[\S ]+), +'
                        r'End +Time: +(?P<end_time>.*)$')

        #Storage State: EXIST
        p9 = re.compile(r'^Storage +State: +(?P<storage_state>.*)$')

        #Transaction ID: 0
        p10 = re.compile(r'^Transaction +ID: +(?P<transaction_id>.*)$')

        #Transaction Message: <none>
        p11 = re.compile(r'^Transaction +Message: +(?P<transaction_message>.*)$')

        for line in output.splitlines():
          line = line.strip()

          #Report Id: 1631796710
          m = p1.match(line)
          if m:
            group = m.groupdict()
            report_id=group['report_id']
            report_dict=ret_dict.setdefault('report_id', {}).setdefault(report_id,{})
            continue

          #Feature Name: dna-advantage
          m = p2.match(line)
          if m:
            group = m.groupdict()
            report_dict.update({'feature_name':group['feature_name']})
            continue

          #Metric Name: ENTITLEMENT
          m = p3.match(line)
          if m:
            group = m.groupdict()
            report_dict.update({'metric_name':group['metric_name']})
            continue

          #UDI:
          m=p4.match(line)
          if m:
            udi=m.groupdict()
            m=p4_1.match(line)
            #UDI: PID:C9300-24UX,SN:FCW2303D16Y
            if m:
              group=m.groupdict()
              group.pop('udi')
              udi['udi']=group
              report_dict.update(udi)
              continue

          #Metric Value: regid.2017-05.com.cisco.C9300_48P_Dna_Advantage,1.0_60783b06-53ee-484c-b21e-615d3cf6837a
          m = p5.match(line)
          if m:
            group = m.groupdict()
            report_dict.update({'metric_value': group['metric_value']})
            continue

          #Previous Report Id: 1631796706,    Next Report Id: 1631796714
          m = p6.match(line)
          if m:
            group = m.groupdict()
            report_dict.update({'previous_report_id': group['previous_report_id']})
            next_report_id=group.get('next_report_id',None)
            if next_report_id:
              report_dict.update({'next_report_id': next_report_id})
              continue

          #State: CLOSED,      State Change Reason: REPORTING
          m = p7.match(line)
          if m:
            group = m.groupdict()
            report_dict.update({'state': group['state']})
            state_change_reason=group.get('state_change_reason',None)
            if state_change_reason:
              report_dict.update({'state_change_reason': state_change_reason})
              continue

          #Start Time: Sep 19 05:12:48 2021 UTC,      End Time: Sep 19 05:21:41 2021 UTC
          m = p8.match(line)
          if m:
            group = m.groupdict()
            report_dict.update({'start_time': group['start_time']})
            end_time=group.get('end_time',None)
            if end_time:
              report_dict.update({'end_time': end_time})
              continue

          #Storage State: EXIST
          m = p9.match(line)
          if m:
            group = m.groupdict()
            report_dict.update({'storage_state': group['storage_state']})
            continue

          #Transaction ID: 0
          m = p10.match(line)
          if m:
            group = m.groupdict()
            report_dict.update({'transaction_id': group['transaction_id']})
            continue

          #Transaction Message: <none>
          m = p11.match(line)
          if m:
            group = m.groupdict()
            report_dict.update({'transaction_message': group['transaction_message']})
            continue

        return ret_dict
        
#-------------------------------------------
# ======================================
#  Schema for: 'show license all'
# ======================================

class ShowLicenseAllSchema(MetaParser):
    schema={
      Optional('load_time'): str,
      Optional('one_minute'): str,
      Optional('five_minutes'): str,
      Optional('ntp_time'): str,
      Optional('smart_licensing_status'):{
        Optional('export_authorization_key'):{
            Optional('features_authorized'):str,
        },
        'utility':{
           'status':str,
        },
        Optional('smart_licensing_using_policy'):{
           'status':str,
        },
        Optional('account_information'):{
           'smart_account':str,
           'virtual_account':str,
        },
        'data_privacy':{
           'sending_hostname':str,
           'callhome_hostname_privacy':str,
           'smart_licensing_hostname_privacy':str,
           'version_privacy':str,
        },
        'transport':{
           Optional('type'):str,
           Optional('url'):str,
           Optional('cslu_address'):str,
           Optional('proxy'):str,
           Optional('vrf'):str,
        },
        'miscellaneous':{
           'custom_id':str,
        },
        'policy':{
           'policy_in_use':str,
           Optional('policy_name'):str,
           'reporting_ack_required':str,
           'unenforced_non_export_perpetual_attributes':{
              'first_report_requirement_days':str,
              'reporting_frequency_days':str,
              'report_on_change_days':str,
            },
           'unenforced_non_export_subscription_attributes':{
              'first_report_requirement_days':str,
              'reporting_frequency_days':str,
              'report_on_change_days':str,
            },
           'enforced_perpetual_subscription_license_attributes':{
              'first_report_requirement_days':str,
              'reporting_frequency_days':str,
              'report_on_change_days':str,
            },
           'export_perpetual_subscription_license_attributes':{
              'first_report_requirement_days':str,
              'reporting_frequency_days':str,
              'report_on_change_days':str,
            },
        },
        'usage_reporting':{
           'last_ack_received':str,
           'next_ack_deadline':str,
           'reporting_push_interval':str,
           'next_ack_push_check':str,
           'next_report_push':str,
           'last_report_push':str,
           'last_report_file_write':str,
        },
        Optional('trust_code_installed'):{
          Optional('active'):{
            Optional('pid'):str,
            Optional('sn'):str,
            Optional('info'):str,
          },
         Optional('standby'):{
            Optional('pid'):str,
            Optional('sn'):str,
            Optional('info'):str,
          },
         Optional('member'):{
            Optional('pid'):str,
            Optional('sn'):str,
            Optional('info'):str,
          },
        },
      },
      Optional('license_usage'):{
        Optional('license_name'):{
          Any():{
            Optional('description'): str,
            Optional('count'): int,
            Optional('version'): str,
            Optional('status'): str,
            Optional('export_status'): str,
            Optional('feature_name'): str,
            Optional('feature_description'): str,
            Optional('enforcement_type'): str,
            Optional('license_type'): str,
          },
        },
      },
      Optional('product_information'):{
        Optional('udi'):{
           Optional('pid'):str,
           Optional('sn'):str,
        },
        Optional('ha_udi_list'):{
          Optional('active'):{
            Optional('pid'):str,
            Optional('sn'):str,
          },
          Optional('standby'):{
            Optional('pid'):str,
            Optional('sn'):str,
          },
          Optional('member'):{
            Optional('pid'):str,
            Optional('sn'):str,
          },
        },
      },
      'agent_version':{
        'smart_agent_for_licensing':str,
      },
      Optional('license_authorizations'):{
        Optional('overall_status'):{
          Optional('active'):{
            Optional('pid'):str,
            Optional('sn'):str,
            Optional('status'):str,
            Optional('last_return_code'):str,
            Optional('last_confirmation_code'):str,
          },
          Optional('standby'):{
            Optional('pid'):str,
            Optional('sn'):str,
            Optional('status'):str,
            Optional('last_return_code'):str,
            Optional('last_confirmation_code'):str,
          },
          Optional('member'):{
            Optional('pid'):str,
            Optional('sn'):str,
            Optional('status'):str,
            Optional('last_return_code'):str,
            Optional('last_confirmation_code'):str,
          },
        },
        Optional('authorizations'):{
          Optional('description'):str,
          Optional('total_available_count'):str,
          Optional('enforcement_type'):str,
          Optional('term_information'):{
            Optional('active'):{
              Optional('pid'):str,
              Optional('sn'):str,
              Optional('authorization_type'):str,
              Optional('license_type'):str,
              Optional('term_count'):str,
            },
            Optional('standby'):{
              Optional('pid'):str,
              Optional('sn'):str,
              Optional('authorization_type'):str,
              Optional('license_type'):str,
              Optional('term_count'):str,
            },
            Optional('member'):{
              Optional('pid'):str,
              Optional('sn'):str,
              Optional('authorization_type'):str,
              Optional('license_type'):str,
              Optional('term_count'):str,
            },
          },
        },
        'purchased_licenses':str,
      },
      Optional('usage_report_summary'):{
        'total':str,
        'purged':str,
        'total_acknowledged_received':str,
        'waiting_for_ack':str,
        'available_to_report':str,
        'collecting_data':str,
      }
    }

# ======================================
#  Parser for: 'show license all'   
# ======================================

class ShowLicenseAll(ShowLicenseAllSchema):
    """ Parser for show license all """

    cli_command = 'show license all'

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict={}
        
        #Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
        p1=re.compile(r'^Load for five secs: +(?P<load_time>.*); +one +minute: +(?P<one_minute>.*); +five +minutes: +(?P<five_minutes>.*)$')
        #Time source is NTP, .16:22:51.426 UTC Wed Sep 29 2021
        p2=re.compile(r'^Time source is NTP, +(?P<ntp_time>.*)$')

        #INSTALLED on Sep 27 12:22:33 2021 UTC|<none>
        p3=re.compile(r'^INSTALLED +on +.*|^<none>.*')

        #Status: DISABLED
        p4= re.compile(r'^Status: +(?P<status>(ENABLED|DISABLED))$')

        #Smart Account: SA-Switching-Polaris As of Sep 27 12:59:45 2021 UTC
        p5= re.compile(r'^Smart +Account: +(?P<smart_account>.*)$')
        # Virtual Account: SLE_Test
        p5_1= re.compile(r'^Virtual +Account: +(?P<virtual_account>.*)$')

        #Sending Hostname: yes
        p6= re.compile(r'^Sending +Hostname: +(?P<sending_hostname>.*)$')
        #Callhome hostname privacy: DISABLED
        p6_1= re.compile(r'^Callhome +hostname +privacy: +(?P<callhome_hostname_privacy>.*)$')
        #Smart Licensing hostname privacy: DISABLED
        p6_2= re.compile(r'^Smart +Licensing +hostname +privacy: +(?P<smart_licensing_hostname_privacy>.*)$')
        #Version privacy: DISABLED
        p6_3= re.compile(r'^Version +privacy: +(?P<version_privacy>.*)$')

        #Type: cslu
        p7 = re.compile(r'^Type: +(?P<type>.*)$')
        #URL: https://smartreceiver-stage.cisco.com/licservice/license
        p7_1 = re.compile(r'^URL: +(?P<url>.*)$')
        #Cslu address: <empty>
        p7_2 = re.compile(r'^Cslu +address: +(?P<cslu_address>.*)$')
        #Proxy:
        p7_3 = re.compile(r'^Proxy:+(?P<proxy>.*)$')
        #Not Configured
        p7_4=re.compile(r'^Not +Configured$')
        #VRF:
        p7_5 = re.compile(r'^VRF:+(?P<vrf>.*)$')

        #Policy in use: Installed On Sep 27 12:22:33 2021 UTC
        p8 = re.compile(r'^Policy +in +use: +(?P<policy_in_use>.*)$')
        #Policy name: Custom Policy
        p8_1 = re.compile(r'^Policy +name: +(?P<policy_name>.*)$')
        #Reporting ACK required: yes (Customer Policy)
        p8_2 = re.compile(r'^Reporting +ACK +required: +(?P<reporting_ack_required>.*)$')
        #Unenforced/Non-Export Perpetual Attributes:
        p8_3 = re.compile(r'^Unenforced/Non-Export +Perpetual +Attributes:+(?P<unenforced_non_export_perpetual_attributes>.*)$')
        #First report requirement (days): 365 (Customer Policy)
        p8_4 = re.compile(r'^First +report +requirement +\(days\): +(?P<first_report_requirement_days>.*)$')
        #Reporting frequency (days): 0 (Customer Policy)
        p8_5 = re.compile(r'^Reporting +frequency +\(days\): +(?P<reporting_frequency_days>.*)$')
        #Report on change (days): 90 (Customer Policy)
        p8_6 = re.compile(r'^Report +on +change +\(days\): +(?P<report_on_change_days>.*)$')
        #Unenforced/Non-Export Subscription Attributes:
        p8_7 = re.compile(r'^Unenforced/Non-Export +Subscription +Attributes:+(?P<unenforced_non_export_subscription_attributes>.*)$')
        #Enforced (Perpetual/Subscription) License Attributes:
        p8_8 = re.compile(r'^Enforced +\(Perpetual/Subscription\) +License +Attributes:+(?P<enforced_perpetual_subscription_license_attributes>.*)$')
        #Export (Perpetual/Subscription) License Attributes:
        p8_9 = re.compile(r'^Export +\(Perpetual/Subscription\) +License +Attributes:+(?P<export_perpetual_subscription_license_attributes>.*)$')

        #Custom Id: <empty>
        p9 = re.compile(r'^Custom +Id: +(?P<custom_id>.*)$')

        #Last ACK received: <none>
        p10 = re.compile(r'^Last +ACK +received: +(?P<last_ack_received>.*)$')
        #Next ACK deadline: Dec 26 12:32:14 2021 UTC
        p10_1 = re.compile(r'^Next +ACK +deadline: +(?P<next_ack_deadline>.*)$')
        #Reporting push interval: 30  days
        p10_2 = re.compile(r'^Reporting +push +interval: +(?P<reporting_push_interval>.*)$')
        #Next ACK push check: Sep 29 16:39:27 2021 UTC
        p10_3 = re.compile(r'^Next +ACK +push +check: +(?P<next_ack_push_check>.*)$')
        #Next report push: Sep 29 13:51:16 2021 UTC
        p10_4 = re.compile(r'^Next +report +push: +(?P<next_report_push>.*)$')
        #Last report push: Sep 27 12:59:50 2021 UTC
        p10_5= re.compile(r'^Last +report +push: +(?P<last_report_push>.*)$')
        #Last report file write: <none>
        p10_6 = re.compile(r'^Last +report +file +write: +(?P<last_report_file_write>.*)$')

        #Trust Code Installed:
        p11 = re.compile(r'^Trust +Code +Installed:+(?P<trust_code_installed>.*)$')
        #Active: PID:C9300-24UX,SN:FCW2303D16Y
        p11_1=re.compile(r'^Active: PID:(?P<pid>.*),SN:(?P<sn>.*)$')
        #Standby: PID:C9300-24U,SN:FHH2043P09E
        p11_2=re.compile(r'^Standby: PID:(?P<pid>.*),SN:(?P<sn>.*)$')
        #Member: PID:C9300-48T,SN:FCW2139L056
        p11_3=re.compile(r'^Member: PID:(?P<pid>.*),SN:(?P<sn>.*)$')

        #(C9300-24 Network Advantage):
        p12=re.compile(r'^.*\(.*:+(?P<license_name>.*)$')
        #Description: C9300-24 Network Advantage
        p12_1 = re.compile(r'^Description: +(?P<description>.*)$')
        #Count: 2
        p12_2 = re.compile(r'^Count: +(?P<count>.*)$')
        #Version: 1.0
        p12_3 = re.compile(r'^Version: +(?P<version>.*)$')
        #Status: IN USE
        p12_4 = re.compile(r'^Status: +(?P<status>.*)$')
        #Export status: NOT RESTRICTED
        p12_5 = re.compile(r'^Export +status: +(?P<export_status>.*)$')
        #Feature Name: network-advantage
        p12_6 = re.compile(r'^Feature +Name: +(?P<feature_name>.*)$')
        #Feature Description: C9300-24 Network Advantage
        p12_7 = re.compile(r'^Feature +Description: +(?P<feature_description>.*)$')
        #Enforcement type: NOT ENFORCED
        p12_8 = re.compile(r'^Enforcement +type: +(?P<enforcement_type>.*)$')
        #License type: Perpetual
        p12_9 = re.compile(r'^License +type: +(?P<license_type>.*)$')

        #UDI: PID:C9300-24UX,SN:FCW2303D16Y
        p13 = re.compile(r'^UDI: PID:(?P<pid>.*),SN:(?P<sn>.*)$')
        #Active: PID:C9300-24UX,SN:FCW2303D16Y
        p13_1=re.compile(r'^Active:PID:(?P<pid>.*),SN:(?P<sn>.*)$')
        #Standby: PID:C9300-24U,SN:FHH2043P09E
        p13_2=re.compile(r'^Standby:PID:(?P<pid>.*),SN:(?P<sn>.*)$')
        #Member: PID:C9300-48T,SN:FCW2139L056
        p13_3=re.compile(r'^Member:PID:(?P<pid>.*),SN:(?P<sn>.*)$')

        #Smart Agent for Licensing: 5.3.10_rel/25
        p14= re.compile(r'^Smart +Agent +for +Licensing: +(?P<smart_agent_for_licensing>.*)$')

        #License Authorizations
        p15= re.compile(r'^License +Authorizations+(?P<license_authorizations>)$')
        #Overall status:
        p15_1= re.compile(r'^Overall +status:+(?P<overall_status>)$')
        #Last return code: CEL7AU-RaGyRi-dGWrct-Mex5qo-hZbfKf-Pp84Vg-m3QZre-FXjAbH-59J
        p15_2= re.compile(r'^Last +return +code: +(?P<last_return_code>.*)$')
        #Last Confirmation code: <none>
        p15_3= re.compile(r'^Last +Confirmation +code: +(?P<last_confirmation_code>.*)$')

        #Authorizations:
        p16_1=re.compile(r'^Authorizations:+(?P<authorizations>)$')
        #Total available count: 3
        p16_2= re.compile(r'^Total +available +count: +(?P<total_available_count>.*)$')
        #Term information:
        p16_3= re.compile(r'^Term +information:+(?P<term_information>)$')
        #Authorization type: SMART AUTHORIZATION INSTALLED 
        p16_4= re.compile(r'^Authorization +type: +(?P<authorization_type>.*)$')
        #Term Count: 1
        p16_5= re.compile(r'^Term +Count: +(?P<term_count>.*)$')

        #Purchased Licenses:
        p17= re.compile(r'^Purchased +Licenses:+(?P<purchased_licenses>)$')
        #No Purchase Information Available
        p17_1= re.compile(r'^No +Purchase +Information +Available$')

        #Total: 44,  Purged: 0
        p18 = re.compile(r'^Total: +(?P<total>[\S ]+), +'
                        r'Purged: +(?P<purged>.*)$')
        #Total Acknowledged Received: 0,  Waiting for Ack: 36
        p18_1= re.compile(r'^Total +Acknowledged +Received: +(?P<total_acknowledged_received>[\S ]+), +'
                        r'Waiting +for +Ack: +(?P<waiting_for_ack>.*)$')
        #Available to Report: 8  Collecting Data: 0
        p18_2= re.compile(r'^Available +to +Report: +(?P<available_to_report>[\S ]+)  +'
                        r'Collecting +Data: +(?P<collecting_data>.*)$')

        license_authorizations_dict=None
        overall_status_dict=None
        authorizations_dict=None
        trust_code_installed_dict=None

        for line in output.splitlines():
          line=line.strip()
          
          #Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
          m=p1.match(line)
          if m:
              group=m.groupdict()
              ret_dict.update(group)
              continue

          #Time source is NTP, 11:41:04.102 UTC Mon Sep 13 2021
          m=p2.match(line)
          if m:
              group=m.groupdict()
              ret_dict.update(group)
              continue

          #INSTALLED on Sep 27 12:22:33 2021 UTC|<none>
          m = p3.match(line)
          if m:
            group=m.group(0)
            smart_licensing_status_dict=ret_dict.setdefault('smart_licensing_status',{})
            if trust_code_installed_dict:
              if not trust_code_installed_dict['active'].get('info'):
                trust_code_installed_dict['active'].setdefault('info',group)
                continue
              elif not trust_code_installed_dict['standby'].get('info'):
                trust_code_installed_dict['standby'].setdefault('info',group)
                continue
              else:
                trust_code_installed_dict['member'].setdefault('info',group)
                continue
            else:
              smart_licensing_status_dict.setdefault('export_authorization_key',{}).setdefault('features_authorized',group)
              continue

          #Status: DISABLED
          m = p4.match(line)
          if m:
            group = m.groupdict()
            if not smart_licensing_status_dict.get('utility'):
              smart_licensing_status_dict.setdefault('utility',{}).setdefault('status',group['status'])
            else:
              smart_licensing_status_dict.setdefault('smart_licensing_using_policy',{}).setdefault('status',group['status'])
            continue

          #Smart Account: SA-Switching-Polaris As of Sep 27 12:59:45 2021 UTC
          m = p5.match(line)
          if m:
            group = m.groupdict()
            smart_licensing_status_dict.setdefault('account_information',{}).setdefault('smart_account',group['smart_account'])
            continue
          #Virtual Account: SLE_Test
          m = p5_1.match(line)
          if m:
            group = m.groupdict()
            smart_licensing_status_dict.setdefault('account_information',{}).setdefault('virtual_account',group['virtual_account'])
            continue

          #Sending Hostname: yes
          m = p6.match(line)
          if m:
            group = m.groupdict()
            data_privacy_dict=smart_licensing_status_dict.setdefault('data_privacy',{})
            data_privacy_dict.setdefault('sending_hostname',group['sending_hostname'])
            continue
          #Callhome hostname privacy: DISABLED
          m = p6_1.match(line)
          if m:
            group = m.groupdict()
            data_privacy_dict.setdefault('callhome_hostname_privacy',group['callhome_hostname_privacy'])
            continue
          #Smart Licensing hostname privacy: DISABLED
          m = p6_2.match(line)
          if m:
            group = m.groupdict()
            data_privacy_dict.setdefault('smart_licensing_hostname_privacy',group['smart_licensing_hostname_privacy'])
            continue
          #Version privacy: DISABLED
          m = p6_3.match(line)
          if m:
            group = m.groupdict()
            data_privacy_dict.setdefault('version_privacy',group['version_privacy'])
            continue

          #Type: cslu
          m = p7.match(line)
          if m:
            group = m.groupdict()
            transport_dict=smart_licensing_status_dict.setdefault('transport',{})
            transport_dict.setdefault('type',group['type'])
            continue
          #URL: https://smartreceiver-stage.cisco.com/licservice/license
          m = p7_1.match(line)
          if m:
            group = m.groupdict()
            transport_dict.setdefault('url',group['url'])
            continue
          #Cslu address: <empty>
          m = p7_2.match(line)
          if m:
            group = m.groupdict()
            transport_dict.setdefault('cslu_address',group['cslu_address'])
            continue
          #Proxy:
          m = p7_3.match(line)
          if m:
            group = m.groupdict()
            transport_dict.setdefault('proxy',group['proxy'])
            continue
          #Not Configured
          m = p7_4.match(line)
          if m:
            if transport_dict.get('proxy')=='':
              transport_dict['proxy']=m.group(0)
            else:
              transport_dict['vrf']=m.group(0)
            continue
          #VRF:
          m = p7_5.match(line)
          if m:
            group = m.groupdict()
            smart_licensing_status_dict.setdefault('transport',group)
            continue

          #Policy in use: Installed On Aug 04 04:03:37 2021 UTC
          m = p8.match(line)
          if m:
            group = m.groupdict()
            policy_dict=smart_licensing_status_dict.setdefault('policy',{})
            policy_dict.setdefault('policy_in_use',group['policy_in_use'])
            continue
          #Policy name: Custom Policy
          m = p8_1.match(line)
          if m:
            group = m.groupdict()
            policy_dict.setdefault('policy_name',group['policy_name'])
            continue
          #Reporting ACK required: yes (Customer Policy)
          m = p8_2.match(line)
          if m:
            group = m.groupdict()
            policy_dict.setdefault('reporting_ack_required',group['reporting_ack_required'])
            continue
          #Unenforced/Non-Export Perpetual Attributes:
          m = p8_3.match(line)
          if m:
            group = m.groupdict()
            report_attributes_dict=policy_dict.setdefault('unenforced_non_export_perpetual_attributes',{})
            continue
          #First report requirement (days): 365 (Customer Policy)
          m = p8_4.match(line)
          if m:
            group = m.groupdict()
            report_attributes_dict.setdefault('first_report_requirement_days', group['first_report_requirement_days'])
            continue
          #Reporting frequency (days): 0 (Customer Policy)
          m = p8_5.match(line)
          if m:
            group = m.groupdict()
            report_attributes_dict.setdefault('reporting_frequency_days', group['reporting_frequency_days'])
            continue
          #Report on change (days): 90 (Customer Policy)
          m = p8_6.match(line)
          if m:
            group = m.groupdict()
            report_attributes_dict.setdefault('report_on_change_days', group['report_on_change_days'])
            continue
          #Unenforced/Non-Export Subscription Attributes:
          m = p8_7.match(line)
          if m:
            group = m.groupdict()
            report_attributes_dict= policy_dict.setdefault('unenforced_non_export_subscription_attributes',{})
            continue
          #Enforced (Perpetual/Subscription) License Attributes:
          m = p8_8.match(line)
          if m:
            group = m.groupdict()
            report_attributes_dict= policy_dict.setdefault('enforced_perpetual_subscription_license_attributes',{})
            continue 
          #Export (Perpetual/Subscription) License Attributes:
          m = p8_9.match(line)
          if m:
            group = m.groupdict()
            report_attributes_dict= policy_dict.setdefault('export_perpetual_subscription_license_attributes',{})
            continue

          #Custom Id: <empty>
          m = p9.match(line)
          if m:
            group = m.groupdict()
            smart_licensing_status_dict.setdefault('miscellaneous',{}).setdefault('custom_id',group['custom_id'])
            continue

          #Last ACK received: Aug 04 04:03:37 2021 UTC
          m = p10.match(line)
          if m:
            group = m.groupdict()
            usage_reporting_dict=smart_licensing_status_dict.setdefault('usage_reporting',{})
            usage_reporting_dict.setdefault('last_ack_received',group['last_ack_received'])
            continue
          #Next ACK deadline: Nov 02 04:03:37 2021 UTC
          m = p10_1.match(line)
          if m:
            group = m.groupdict()
            usage_reporting_dict.setdefault('next_ack_deadline',group['next_ack_deadline'])
            continue
          #Reporting push interval: 30  days
          m = p10_2.match(line)
          if m:
            group = m.groupdict()
            usage_reporting_dict.setdefault('reporting_push_interval',group['reporting_push_interval'])
            continue
          #Next ACK push check: <none>
          m = p10_3.match(line)
          if m:
            group = m.groupdict()
            usage_reporting_dict.setdefault('next_ack_push_check',group['next_ack_push_check'])
            continue
          #Next report push: Aug 04 05:35:24 2021 UTC
          m = p10_4.match(line)
          if m:
            group = m.groupdict()
            usage_reporting_dict.setdefault('next_report_push',group['next_report_push'])
            continue
          #Last report push: <none>
          m = p10_5.match(line)
          if m:
            group = m.groupdict()
            usage_reporting_dict.setdefault('last_report_push',group['last_report_push'])
            continue
          #Last report file write: <none>
          m = p10_6.match(line)
          if m:
            group = m.groupdict()
            usage_reporting_dict.setdefault('last_report_file_write',group['last_report_file_write'])
            continue

          #Trust Code Installed:
          m = p11.match(line)
          if m:
            group = m.groupdict()
            if group['trust_code_installed']:
              if group['trust_code_installed'].strip()=='<none>':
                continue
              # else:
                # trust_code_installed_dict=smart_licensing_status_dict.setdefault('trust_code_installed',group['trust_code_installed'].strip())
                # continue
            else:
              trust_code_installed_dict=smart_licensing_status_dict.setdefault('trust_code_installed',{})
              continue
          #Active: PID:C9300-24UX,SN:FCW2303D16Y
          m = p11_1.match(line)
          if m:
            group = m.groupdict()
            if not ret_dict['smart_licensing_status'].get('trust_code_installed'):
              if trust_code_installed_dict!=None:
                active_dict = trust_code_installed_dict.setdefault('active', {})
                active_dict['pid'] = group['pid']
                active_dict['sn'] = group['sn']
                continue
            if not overall_status_dict:
              active_dict = overall_status_dict.setdefault('active', {})
              active_dict['pid'] = group['pid']
              active_dict['sn'] = group['sn']
              continue
            if not term_information_dict:
                active_dict = term_information_dict.setdefault('active', {})
                active_dict['pid'] = group['pid']
                active_dict['sn'] = group['sn']
                continue
          #Standby: PID:C9300-24U,SN:FHH2043P09E
          m = p11_2.match(line)
          if m:
            group = m.groupdict()
            if ret_dict['smart_licensing_status'].get('trust_code_installed'):
              if not trust_code_installed_dict.get('standby'):
                standby_dict = trust_code_installed_dict.setdefault('standby', {})
                standby_dict['pid'] = group['pid']
                standby_dict['sn'] = group['sn']
                continue
            if not overall_status_dict.get('standby'):
              standby_dict = overall_status_dict.setdefault('standby', {})
              standby_dict['pid'] = group['pid']
              standby_dict['sn'] = group['sn']
              continue
            if not term_information_dict.get('standby'):
              standby_dict = term_information_dict.setdefault('standby', {})
              standby_dict['pid'] = group['pid']
              standby_dict['sn'] = group['sn']
              continue
          #Member: PID:C9300-48T,SN:FCW2139L056
          m = p11_3.match(line)
          if m:
            group = m.groupdict()
            if ret_dict['smart_licensing_status'].get('trust_code_installed'):
              if not trust_code_installed_dict.get('member'):
                member_dict = trust_code_installed_dict.setdefault('member', {})
                member_dict['pid'] = group['pid']
                member_dict['sn'] = group['sn']
                continue
            if not overall_status_dict.get('member'):
              member_dict = overall_status_dict.setdefault('member', {})
              member_dict['pid'] = group['pid']
              member_dict['sn'] = group['sn']
              continue
            if not term_information_dict.get('member'):
                member_dict = term_information_dict.setdefault('member', {})
                member_dict['pid'] = group['pid']
                member_dict['sn'] = group['sn']
                continue

          #(C9300-24 Network Advantage):
          m = p12.match(line)
          if m:
            group_na = m.group(0)
            license_name_dict=ret_dict.setdefault('license_usage',{}).setdefault('license_name',{}).setdefault(group_na,{})
            if ret_dict.get('license_authorizations'):
              continue
            else:
              continue
          #Description: C9300-24 Network Advantage
          m = p12_1.match(line)
          if m:
            group = m.groupdict()
            if ret_dict.get('license_authorizations'):
              authorizations_dict.setdefault('description',group['description'])
              continue
            else:
              license_name_dict.setdefault('description',group['description'])
              continue
          #Count: 2
          m = p12_2.match(line)
          if m:
            group = m.groupdict() 
            group['count']=int(group['count'])
            license_name_dict.setdefault('count',group['count'])
            continue
          #Version: 1.0
          m = p12_3.match(line)
          if m:
            group = m.groupdict()
            license_name_dict.setdefault('version',group['version'])
            continue
          #Status: IN USE
          m = p12_4.match(line)
          if m:
            group = m.groupdict()
            if ret_dict.get('license_usage'):
              if ret_dict.get('license_authorizations'):
                if overall_status_dict:
                  if not overall_status_dict['active'].get('status'):
                    overall_status_dict['active'].setdefault('status',group['status'])
                    continue
                  if not overall_status_dict['standby'].get('status'):
                    overall_status_dict['standby'].setdefault('status',group['status'])
                    continue
                  if not overall_status_dict['member'].get('status'):
                   overall_status_dict['member'].setdefault('status',group['status'])
                   continue
              else:
                license_name_dict.setdefault('status',group['status'])
                continue
          #Export status: NOT RESTRICTED
          m = p12_5.match(line)
          if m:
            group = m.groupdict() 
            license_name_dict.setdefault('export_status',group['export_status'])
            continue
          #Feature Name: network-advantage
          m = p12_6.match(line)
          if m:
            group = m.groupdict()
            license_name_dict.setdefault('feature_name',group['feature_name'])
            continue
          #Feature Description: C9300-24 Network Advantage
          m = p12_7.match(line)
          if m:
            group = m.groupdict()
            license_name_dict.setdefault('feature_description',group['feature_description'])
            continue
          #Enforcement type: NOT ENFORCED
          m = p12_8.match(line)
          if m:
            group = m.groupdict()
            if ret_dict.get('license_authorizations'):
                authorizations_dict.setdefault('enforcement_type',group['enforcement_type'])
                continue
            else:
                license_name_dict.setdefault('enforcement_type',group['enforcement_type'])
                continue
          #License type: Perpetual
          m = p12_9.match(line)
          if m:
            group = m.groupdict()
            if ret_dict.get('license_authorizations'):
                if authorizations_dict['term_information']:
                  if not authorizations_dict['term_information']['active'].get('license_type'):
                    authorizations_dict['term_information']['active'].setdefault('license_type',group['license_type'])
                    continue
                  elif not authorizations_dict['term_information']['standby'].get('license_type'):
                      authorizations_dict['term_information']['standby'].setdefault('license_type',group['license_type'])
                      continue
                  else:
                      authorizations_dict['term_information']['member'].setdefault('license_type',group['license_type'])
                      continue
            else:
                license_name_dict.setdefault('license_type',group['license_type'])
                continue

          #UDI: PID:C9300-24UX,SN:FCW2303D16Y
          m = p13.match(line)
          if m:
            group = m.groupdict()
            product_information_dict=ret_dict.setdefault('product_information',{})
            udi_dict = product_information_dict.setdefault('udi', {})
            udi_dict['pid'] = group['pid']
            udi_dict['sn'] = group['sn']
            continue
          #Active: PID:C9300-24UX,SN:FCW2303D16Y
          m = p13_1.match(line)
          if m:
            group = m.groupdict()
            active_dict = product_information_dict.setdefault('ha_udi_list', {})\
                                   .setdefault('active', {})
            active_dict['pid'] = group['pid']
            active_dict['sn'] = group['sn']
            continue
          #Standby: PID:C9300-24U,SN:FHH2043P09E
          m = p13_2.match(line)
          if m:
            group = m.groupdict()
            standby_dict = product_information_dict.setdefault('ha_udi_list', {})\
                                   .setdefault('standby', {})
            standby_dict['pid'] = group['pid']
            standby_dict['sn'] = group['sn']
            continue
          #Member: PID:C9300-48T,SN:FCW2139L056
          m = p13_3.match(line)
          if m:
            group = m.groupdict()
            member_dict = product_information_dict.setdefault('ha_udi_list', {})\
                                   .setdefault('member', {})
            member_dict['pid'] = group['pid']
            member_dict['sn'] = group['sn']
            continue

          #Smart Agent for Licensing: 5.3.10_rel/25
          m = p14.match(line)
          if m:
            group = m.groupdict()
            ret_dict.setdefault('agent_version',{}).setdefault('smart_agent_for_licensing',group['smart_agent_for_licensing'])
            continue

          #License Authorizations
          m = p15.match(line)
          if m:
            group = m.groupdict()
            license_authorizations_dict=ret_dict.setdefault('license_authorizations',{})
            continue
          #Overall status:
          m = p15_1.match(line)
          if m:
            group = m.groupdict()
            overall_status_dict = license_authorizations_dict.setdefault('overall_status', {})
            continue
          #Last return code: CEL7AU-RaGyRi-dGWrct-Mex5qo-hZbfKf-Pp84Vg-m3QZre-FXjAbH-59J
          m = p15_2.match(line)
          if m:
            group = m.groupdict()
            if overall_status_dict:
              if not overall_status_dict['active'].get('last_return_code'):
                overall_status_dict['active'].setdefault('last_return_code',group['last_return_code'])
                continue
              elif not overall_status_dict['standby'].get('last_return_code'):
                overall_status_dict['standby'].setdefault('last_return_code',group['last_return_code'])
                continue
              else:
                overall_status_dict['member'].setdefault('last_return_code',group['last_return_code'])
                continue
          #Last confirmation code: <none>
          m = p15_3.match(line)
          if m:
            group = m.groupdict()
            if overall_status_dict:
              if not overall_status_dict['active'].get('last_confirmation_code'):
                overall_status_dict['active'].setdefault('last_confirmation_code',group['last_confirmation_code'])
                continue
              elif not overall_status_dict['standby'].get('last_confirmation_code'):
                overall_status_dict['standby'].setdefault('last_confirmation_code',group['last_confirmation_code'])
                continue
              else:
                overall_status_dict['member'].setdefault('last_confirmation_code',group['last_confirmation_code'])
                continue

          #Authorizations:
          m = p16_1.match(line)
          if m:
            group = m.groupdict()
            authorizations_dict=license_authorizations_dict.setdefault('authorizations',{})
            continue
          #Total available count: 3
          m = p16_2.match(line)
          if m:
            group = m.groupdict()
            authorizations_dict.setdefault('total_available_count',group['total_available_count'])
            continue
          #Term information:
          m = p16_3.match(line)
          if m:
            group = m.groupdict()
            term_information_dict=authorizations_dict.setdefault('term_information',{})
            continue
          #Authorization type: SMART AUTHORIZATION INSTALLED
          m = p16_4.match(line)
          if m:
            group = m.groupdict()
            if term_information_dict:
              if not term_information_dict['active'].get('authorization_type'):
                  term_information_dict['active'].update(group)
                  continue
              elif not term_information_dict['standby'].get('authorization_type'):
                  term_information_dict['standby'].update(group)
                  continue
              else:
                term_information_dict['member'].update(group)
                continue
          #Term Count: 1
          m = p16_5.match(line)
          if m:
            group = m.groupdict() 
            if authorizations_dict['term_information']:
              if not authorizations_dict['term_information']['active'].get('term_count'):
                  authorizations_dict['term_information']['active'].update(group)
                  continue
              elif not authorizations_dict['term_information']['standby'].get('term_count'):
                  authorizations_dict['term_information']['standby'].update(group)
                  continue
              else:
                  authorizations_dict['term_information']['member'].update(group)
                  continue

          #Purchased Licenses:
          m = p17.match(line)
          if m:
            group = m.groupdict()
            purchased_licenses_dict=license_authorizations_dict.setdefault('purchased_licenses',{})
            continue
          #No Purchase Information Available
          m = p17_1.match(line)
          if m:
            group = m.group(0)
            license_authorizations_dict['purchased_licenses']=group
            continue

          #Total: 52,  Purged: 0
          m = p18.match(line)
          if m:
            group = m.groupdict()
            usage_report_summary_dict=ret_dict.setdefault('usage_report_summary',{})
            usage_report_summary_dict.update(group)
            continue
          #Total Acknowledged Received: 47,  Waiting for Ack: 0
          m = p18_1.match(line)
          if m:
            group = m.groupdict()
            usage_report_summary_dict.update(group)
            continue
          #Available to Report: 4  Collecting Data: 4
          m = p18_2.match(line)
          if m:
            group = m.groupdict() 
            usage_report_summary_dict.update(group)
            continue

        return ret_dict
        
# ======================================
#  Schema for: 'show license usage'   
# ======================================

class ShowLicenseUsageSchema(MetaParser):
    schema = {
        Optional('license_name'):{
            Any():{
                'description': str,
                'count': int,
                'version': str,
                'status': str,
                'export_status': str,
                'feature_name': str,
                'feature_description': str,
                'enforcement_type': str,
                'license_type': str,
            },
        },
       Optional('license_authorization'):{
           Optional('status'): str
        }
    }

# ======================================
#  Parser for: 'show license usage'   
# ======================================

class ShowLicenseUsage(ShowLicenseUsageSchema):
    """ Parser for show license usage """

    cli_command = 'show license usage'

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict={}
        
        #C9300-24 Network Advantage):
        p1 = re.compile(r'^.*\(.*:+(?P<license_name>.*)$')

        #Status: Not Applicable
        p2 = re.compile(r'^Status: +(?P<status>.*)$')

        #Description: C9300-24 Network Advantage
        p3 = re.compile(r'^Description: +(?P<description>.*)$')

        #Count: 1
        p4 = re.compile(r'^Count: +(?P<count>\d+)$')

        #Version: 1.0
        p5 = re.compile(r'^Version: +(?P<version>.*)$')

        #Export status: NOT RESTRICTED
        p6 = re.compile(r'^Export +status: +(?P<export_status>.*)$')

        #Feature Name: dna-advantage
        p7 = re.compile(r'^Feature +Name: +(?P<feature_name>.*)$')

        #Feature Description: C9300-48 DNA Advantage
        p8 = re.compile(r'^Feature +Description: +(?P<feature_description>.*)$')

        #Enforcement type: NOT ENFORCED
        p9 = re.compile(r'^Enforcement +type: +(?P<enforcement_type>.*)$')

        #License type: Subscription
        p10 = re.compile(r'^License +type: +(?P<license_type>.*)$')

        license_name_dict=None

        for line in output.splitlines():
          line=line.strip()

          #(C9300-24 Network Advantage):
          m = p1.match(line)
          if m:
            diff_license=m.group()
            license_name_dict=ret_dict.setdefault('license_name',{}).setdefault(diff_license,{})
            continue

          #Status: Not Applicable
          m = p2.match(line)
          if m:
            group = m.groupdict()
            if license_name_dict:
              license_name_dict.setdefault('status',group['status'])
            else:
              ret_dict.setdefault('license_authorization',{}).setdefault('status',group['status'])  
            continue

          #Description: C9300-24 Network Advantage
          m = p3.match(line)
          if m:
            group = m.groupdict()
            license_name_dict.setdefault('description',group['description'])
            continue

          #Count: 1
          m = p4.match(line)
          if m:
            group = m.groupdict()
            group['count']=int(group['count'])
            license_name_dict.setdefault('count',group['count'])
            continue

          #Version: 1.0
          m = p5.match(line)
          if m:
            group = m.groupdict()
            license_name_dict.setdefault('version',group['version'])
            continue

          #Export status: NOT RESTRICTED
          m = p6.match(line)
          if m:
            group = m.groupdict()
            license_name_dict.setdefault('export_status',group['export_status'])
            continue

          #Feature Name: dna-advantage
          m = p7.match(line)
          if m:
            group = m.groupdict()
            license_name_dict.setdefault('feature_name',group['feature_name'])
            continue

          #Feature Description: C9300-48 DNA Advantage
          m = p8.match(line)
          if m:
            group = m.groupdict()
            license_name_dict.setdefault('feature_description',group['feature_description'])
            continue

          #Enforcement type: NOT ENFORCED  
          m = p9.match(line)
          if m:
            group = m.groupdict()
            license_name_dict.setdefault('enforcement_type',group['enforcement_type'])
            continue

          #License type: Subscription
          m = p10.match(line)
          if m:
            group = m.groupdict()
            license_name_dict.setdefault('license_type',group['license_type'])
            continue

        return ret_dict
# =========================================
#  Schema for: 'show license eventlog 2'   
# =========================================

class ShowLicenseEventlog2Schema(MetaParser):
    schema = {
        Optional('load_time'): str,
        Optional('one_minute'): str,
        Optional('five_minutes'): str,
        Optional('ntp_time'): str,
        Optional('no_eventlog_found'): bool,
        Optional('event_log'): ListOf(
            {'log_message': str}
        )
    }

# =========================================
#  Parser for: 'show license eventlog 2'   
# =========================================

class ShowLicenseEventlog2(ShowLicenseEventlog2Schema):
    """ Parser for show license eventlog 2 """

    cli_command = 'show license eventlog 2'

    def cli(self,output=None):
        if output is None:          
            output = self.device.execute(self.cli_command)

        ret_dict={}

        #Load for five secs: 2%/0%; one minute: 2%; five minutes: 3%
        p1 = re.compile(r'^Load for five secs: +(?P<load_time>.*); +one +minute: +(?P<one_minute>.*); +five +minutes: +(?P<five_minutes>.*)$')

        #Time source is NTP, 11:41:04.102 UTC Mon Sep 13 2021
        p2 = re.compile(r'^Time source is NTP, +(?P<ntp_time>.*)$')

        #No EventLog Found.
        p3 = re.compile(r'^No EventLog Found\.$')

        #**** Event Log ****
        p4 = re.compile(r'^\*+\s+Event Log\s+\*+$')

        #2021-10-30 04:32:38.266 UTC SAEVT_ENDPOINT_USAGE count="0" entitlementTag="regid.2018-06.com.cisco.DNA_NWStack,1.0_e7244e71-3ad5-4608-8bf0-d12f67c80896"
        p5 = re.compile(r'^[\d-]+\s[\d:\.]+\s\w+\s+(?P<log_message>.*)$')

        for line in output.splitlines():
            line=line.strip()

            #Load for five secs: 2%/0%; one minute: 2%; five minutes: 3%
            m=p1.match(line)
            if m:
                group=m.groupdict()
                ret_dict.update(group)
                continue

            #Time source is NTP, 11:41:04.102 UTC Mon Sep 13 2021
            m=p2.match(line)
            if m:
                group=m.groupdict()
                ret_dict.update(group)
                continue

            #No EventLog Found.
            m=p3.match(line)
            if m:
                ret_dict['no_eventlog_found'] = True
                continue

            #**** Event Log ****
            m=p4.match(line)
            if m:
                ret_dict.setdefault('event_log', [])
                continue

            #2021-10-30 04:32:38.266 UTC SAEVT_ENDPOINT_USAGE count="0" entitlementTag="regid.2018-06.com.cisco.DNA_NWStack,1.0_e7244e71-3ad5-4608-8bf0-d12f67c80896"
            m=p5.match(line)
            if m:
                ret_dict['event_log'].append({"log_message":m.groupdict()['log_message']})
                continue

        return ret_dict     

# ===========================================
#  Schema for: 'show license tech support'   
# ===========================================

class ShowLicenseTechSupportSchema(MetaParser):
    schema={
        Optional('primary_load_time_percent'): int,
        Optional('secondary_load_time_percent'): int,
        Optional('one_minute_load_percent'): int,
        Optional('five_minute_load_percent'): int,
        Optional('ntp_time'): str,
        Optional('smart_licensing_status'):{
            Optional('export_authorization_key'):{
            Optional('features_authorized'):str,
            },
            'utility':{
                'status':str,
            },
            Optional('smart_licensing_using_policy'):{
                'status':str,
            },
            Optional('account_information'):{
                Optional('smart_account'):str,
                Optional('virtual_account'):str,
            },
            'data_privacy':{
                'sending_hostname':str,
                'callhome_hostname_privacy':str,
                'smart_licensing_hostname_privacy':str,
                'version_privacy':str,
            },
            'transport':{
                Optional('type'):str,
                Optional('cslu_address'):str,
                Optional('url'):str,
                Optional('proxy'):{
                    Optional('address'):str,
                    Optional('port'):str,
                    Optional('username'):str,
                    Optional('password'):str,
                },
                Optional('server_identity_check'):str,
                Optional('vrf'):str,
            },
            'miscellaneous':{
                'custom_id':str,
            },
            'policy':{
                'policy_in_use':str,
                Optional('policy_name'):str,
                'reporting_ack_required':str,
                Any():{
                    'first_report_requirement_days':str,
                    'reporting_frequency_days':str,
                    'report_on_change_days':str,
                },
            },
            'usage_reporting':{
                'last_ack_received':str,
                'next_ack_deadline':str,
                'reporting_push_interval':str,
                'next_ack_push_check':str,
                'next_report_push':str,
                'last_report_push':str,
                'last_report_file_write':str,
            },
        },
        'license_usage':{
            'handle':{
                int:{
                    'license':str,
                    'entitlement_tag':str,
                    'description': str,
                    'count': int,
                    'version': str,
                    'status': str,
                    'status_time':str,
                    'request_time':str,
                    'export_status': str,
                    'feature_name': str,
                    'feature_description': str,
                    Optional('enforcement_type'): str,
                    Optional('license_type'): str,
                    Optional('measurements'):{
                        Optional('entitlement'):{
                              Optional('interval'):str,
                              Optional('current_value'):int,
                              Optional('current_report'):int,
                              Optional('previous'):int,
                          },
                    },
                    Optional('soft_enforced'):str,
                },
            },
        },
        Optional('product_information'):{
            Optional('udi'):{
                Optional('pid'):str,
                Optional('sn'):str,
            },
            Optional('ha_udi_list'):{
                Any():{
                    Optional('pid'):str,
                    Optional('sn'):str,
                },
            },
        },
        'agent_version':{
            'smart_agent_for_licensing':str,
        },
        'upcoming_scheduled_jobs':{
            'current_time':str,
            'daily':str,
            Optional('authorization_renewal'):str,
            'init_flag_check':str,
            Optional('register_period_expiration_check'):str,
            Optional('ack_expiration_check'):str,
            'reservation_configuration_mismatch_between_nodes_in_ha_mode':str,
            Optional('retrieve_data_processing_result'):str,
            'start_utility_measurements':str,
            'send_utility_rum_reports':str,
            'save_unreported_rum_reports':str,
            Optional('process_utility_rum_reports'):str,
            Optional('authorization_code_process'):str,
            Optional('authorization_confirmation_code_process'):str,
            'data_synchronization':str,
            'external_event':str,
            Optional('operational_model'):str,
            Optional('hello_message'):str,
        },
        Optional('communication_statistics'):{
            'communication_level_allowed':str,
            'overall_state':str,
            Any():{
                'attempts':str,
                'ongoing_failure':str,
                'last_response':str,
                Optional('failure_reason'):str,
                'last_success_time':str,
                'last_failure_time':str,
            },
        }, 
        'license_certificates':{
            'production_cert':str,
        },
        'ha_info':{
            'rp_role':str,
            'chassis_role':str,
            'behavior_role':str,
            'rmf':str,
            'cf':str,
            'cf_state':str,
            'message_flow_allowed':str,
        },
        'reservation_info':{
            'license_reservation':str,
            'overall_status':{
                Any():{
                    Optional('pid'):str,
                    Optional('sn'):str,
                    'reservation_status':str,
                    'request_code':str,
                    'last_return_code':str,
                    'last_confirmation_code':str,                    
                    'reservation_authorization_code':str,
                }, 
            },
            Optional('authorizations'):{
                Optional('description'):str,
                Optional('total_available_count'):str,
                Optional('enforcement_type'):str,
                Optional('term_information'):{
                    Any():{
                        Optional('pid'):str,
                        Optional('sn'):str,
                        Optional('authorization_type'):str,
                        Optional('license_type'):str,
                        Optional('start_date'):str,
                        Optional('end_date'):str,
                        Optional('term_count'):str,
                        Optional('subscription_id'):str,
                    },
                },
            },
            'purchased_licenses':str,
            Optional('last_reporting_not_required'):{
                Optional('entitlement_tag'):str,
            }   
        },
        Optional('usage_report_summary'):{
            'total':int,
            'purged':str,
            'total_acknowledged_received':int,
            'waiting_for_ack':str,
            'available_to_report':int,
            'collecting_data':int,
            Optional('maximum_display'):int,
            Optional('in_storage'):int,
            Optional('mia'):str,
            Optional('report_module_status'):str,
        },
        'other_info':{
            'software_id':str,
            'agent_state':str,
            'ts_enable':str,
            'transport':str,
            Optional('default_url'):str,
            'locale':str,
            'debug_flags':str,
            'privacy_send_hostname':str,
            'privacy_send_ip':str,
            Optional('build_type'):str,
            'sizeof_char':int,
            'sizeof_int':int,
            'sizeof_long':int,
            'sizeof_char_*':int,
            'sizeof_time_t':int,
            'sizeof_size_t':int,
            'endian':str,
            'write_erase_occurred':str,
            'xos_version':str,
            'config_persist_received':str,
            'message_version':str,
            Optional('connect_info_name'):str,
            Optional('connect_info_version'):str,
            Optional('connect_info_additional'):str,
            Optional('connect_info_prod'):str,
            Optional('connect_info_capabilities'):str,
            'agent_capabilities':str,
            'check_point_interface':str,
            'config_management_interface':str,
            'license_map_interface':str,
            'ha_interface':str,
            'trusted_store_interface':str,
            'platform_data_interface':str,
            'crypto_version_2_interface':str,
            'sapluginmgmtinterfacemutex':str,
            'sapluginmgmtipdomainname':str,
            Optional('smarttransportvrfsupport'):str,
            'smartagentclientwaitforserver':int,
            'smartagentcmretrysend':str,
            'smartagentclientisunified':str,
            'smartagentcmclient':str,
            'smartagentclientname':str,
            'builtinencryption':str,
            'enableoninit':str,
            'routingreadybyevent':str,
            'systeminitbyevent':str,
            'smarttransportserveridcheck':str,
            'smarttransportproxysupport':str,
            Optional('smartagentusagestatisticsenable'):str,
            Optional('smartagentpolicydisplayformat'):int,
            Optional('smartagentreportonupgrade'):str,
            Optional('smartagentindividualrumencrypt'):int,
            'smartagentmaxrummemory':int,
            'smartagentconcurrentthreadmax':int,
            'smartagentpolicycontrollermodel':str,
            'smartagentpolicymodel':str,
            'smartagentfederallicense':str,
            'smartagentmultitenant':str,
            'attr365dayevalsyslog':str,
            'checkpointwriteonly':str,
            'smartagentdelaycertvalidation':str,
            'enablebydefault':str,
            'conversionautomatic':str,
            'conversionallowed':str,
            'storageencryptdisable':str,
            'storageloadunencrypteddisable':str,
            'tsplugindisable':str,
            'bypassudicheck':str,
            'loggingaddtstamp':str,
            'loggingaddtid':str,
            'highavailabilityoverrideevent':str,
            'platformindependentoverrideevent':str,
            'platformoverrideevent':str,
            'waitforharole':str,
            'standbyishot':str,
            'chkpttype':int,
            'delaycomminit':str,
            'rolebyevent':str,
            'maxtracelength':int,
            'tracealwayson':str,
            'debugflags':int,
            Optional('error'):str,
            'event_log_max_size':str,
            'event_log_current_size':str,
            Optional('trust_data'):{
                Any():{
                Optional('p'):str,  
                Optional('trustvalue'):str,
                Optional('trustid'):int,
                },
            },
            Optional('local_device'):str,
            'overall_trust':str,
            Optional('clock_synced_with_ntp'):str,
        },
        Optional('platform_provided_mapping_table'):{
            Optional('pid'):str,
            Optional('total_licenses_found'):int,
            Optional('enforced_licenses'):{
                Any():{
                Optional('pid'):str,
                Optional('hseck9_entitlement_tag'):str,
                Optional('hseck9_no'):int,
                Optional('hseck9'):str,
                }
            },
        },
    }
    
# ===========================================
#  Parser for: 'show license tech support'   
# =========================================== 

class ShowLicenseTechSupport(ShowLicenseTechSupportSchema):
    """ Parser for show license tech support """

    cli_command = 'show license tech support'

    def cli(self,output=None):
        if output is None: 
            output = self.device.execute(self.cli_command)

        ret_dict={}
        
        #Below code for handling special NTP lines 
        #Load for five secs: 0%/0%; one minute: 0%; five minutes: 0%
        p0 = re.compile(r'^Load for five secs:\s*(?P<primary_load_time_percent>[0-9]+)\%\/(?P<secondary_load_time_percent>[0-9]+)\%\;\s*one minute:\s*(?P<one_minute_load_percent>[0-9]+)\%\;\s*five minutes:\s*(?P<five_minute_load_percent>[0-9]+)\%')
        #Time source is NTP, .06:17:59.041 UTC Thu Sep 9 2021
        p0_1 = re.compile(r'^Time source is NTP, +(?P<ntp_time>.*)$')
        
        #Below set of regular expressions to match headings and sub headings from output
        #Smart Licensing Status
        p1 = re.compile(r'^(?P<smart_licensing_status_dict>Smart +Licensing +Status)$')
        #Export Authorization Key:
        p1_1 = re.compile(r'^(?P<export_authorization_key>Export +Authorization +Key)\:$')
        #Utility:
        p1_2 = re.compile(r'^(?P<utility>Utility)\:$')
        #Smart Licensing Using Policy:
        p1_3 = re.compile(r'^(?P<smart_licensing_using_policy>Smart +Licensing +Using +Policy)\:$')
        #Account Information:
        p1_4 = re.compile(r'^(?P<account_information>Account +Information)\:$')
        #Data Privacy:
        p1_5 = re.compile(r'^(?P<data_privacy>Data +Privacy)\:$')
        #Transport:
        p1_6 = re.compile(r'^(?P<transport>Transport)\:$')
        #Proxy:
        p1_6_1 = re.compile(r'^\s*(?P<proxy>Proxy)\:$')
        #Miscellaneous:
        p1_7 = re.compile(r'^(?P<miscellaneous>Miscellaneous)\:$')
        #Policy:
        p1_8 = re.compile(r'^(?P<policy>Policy)\:$')
        #Unenforced/Non-Export Perpetual Attributes:
        #Unenforced/Non-Export Subscription Attributes:
        #Enforced (Perpetual/Subscription) License Attributes:
        #Export (Perpetual/Subscription) License Attributes:
        p1_8_1 = re.compile(r'^\s*(?P<policy_sub_header>[Unenforced|Enforced|Export]+[\/]*[\w\-\w]* +[\(]*[Perpetual|Subscription]+[\/]*[Perpetual|Subscription]*[\)]*.*Attributes)\:$')
        #Usage Reporting:
        p1_9 = re.compile(r'^(?P<usage_reporting>Usage Reporting)\:$')
        
        #License Usage
        p2 = re.compile(r'^(?P<license_usage>License +Usage)$')
        #Handle: 1
        p2_1 = re.compile(r'^(?P<handle>Handle)\: +(?P<value>\d+)$')
        #Measurements:
        p2_1_1 = re.compile(r'^\s*(?P<measurements>Measurements)\:$')
        #ENTITLEMENT:
        p2_1_1_1 = re.compile(r'^\s*(?P<entitlement>ENTITLEMENT)\:$')
        
        #Product Information
        p3 = re.compile(r'^(?P<product_information>Product +Information)$')
        #UDI: PID:C9410R,SN:FXS2202037E  
        #Added this regexp  to update the data with heading.
        p3_1 = re.compile(r'^(?P<udi>UDI)\:\s*PID:(?P<pid>\S+),SN:(?P<sn>\S+)$') 
        #HA UDI List:
        p3_2 = re.compile(r'^(?P<ha_udi_list>HA UDI List)\:$')
        
        #Agent Version
        p4 = re.compile(r'^(?P<agent_version>Agent +Version)$')
        
        #Upcoming Scheduled Jobs
        p5 = re.compile(r'^(?P<upcoming_scheduled_jobs>Upcoming +Scheduled +Jobs)$')
        
        #Communication Statistics:
        p6 = re.compile(r'^(?P<communication_statistics>Communication +Statistics)\:$')
        #Trust Establishment:
        p6_1 = re.compile(r'^(?P<trust_establishment>Trust +Establishment)\:$')
        #Trust Acknowledgement:
        p6_2 = re.compile(r'^(?P<trust_acknowledgement>Trust +Acknowledgement)\:$')     
        #Result Polling:
        p6_4 = re.compile(r'^(?P<result_polling>Result +Polling)\:$')
        #Authorization Request:
        p6_5 = re.compile(r'^(?P<authorization_request>Authorization +Request)\:$')
        #Authorization Confirmation:
        p6_6 = re.compile(r'^(?P<authorization_confirmation>Authorization +Confirmation)\:$')
        #Authorization Return:
        p6_7 = re.compile(r'^(?P<authorization_return>Authorization +Return)\:$')
        #Trust Sync:
        p6_8 = re.compile(r'^(?P<trust_sync>Trust +Sync)\:$')
        #Hello Message:
        p6_9 = re.compile(r'^(?P<hello_message>Hello +Message)\:$')
        
        #License Certificates
        p7 = re.compile(r'^(?P<license_certificates>License +Certificates)$')
        
        #HA Info
        p8 = re.compile(r'^(?P<ha_info>HA +Info)$')
        
        #Reservation Info
        p9 = re.compile(r'^(?P<reservation_info>Reservation +Info)$')
        #Overall status:
        p9_1 = re.compile(r'^(?P<overall_status>Overall +status)\:$')
        #Authorizations:
        p9_2 = re.compile(r'^(?P<authorizations>Authorizations)\:$')
        #C9K HSEC (Cat9K HSEC):
        p9_2_1 = re.compile(r'^(?P<c9k_hsec>C9K HSEC)\s*\(Cat9K +HSEC\)\:$')
        #Term information:
        p9_2_1_1 = re.compile(r'^(?P<term_information>Term +information)\:$')
        #Last Reporting Not Required:
        p9_3 = re.compile(r'^(?P<last_reporting_not_required>Last +Reporting +Not +Required)\:$')
        
        #Usage Report Summary:
        p10 = re.compile(r'^(?P<usage_report_summary>Usage +Report +Summary)\:$')
        
        #Other Info
        p11 = re.compile(r'^(?P<other_info>Other +Info)$')
        
        #Platform Provided Mapping Table
        p12 = re.compile(r'^(?P<platform_provided_mapping_table>Platform +Provided +Mapping +Table)$')
        #Enforced Licenses:
        p12_1 = re.compile(r'^(?P<enforced_licenses>Enforced +Licenses)\:$')

        #Below set of expressions are for capturing data lines (For eg. key-value pairs)
        #<none>
        p0_2 = re.compile(r'^\s*\<(?P<value>none)\>$')

        #No Purchase Information Available
        p0_5 = re.compile(r'^\s*(?P<value>No +Purchase +Information +Available)$')

        #Generalised expression for all lines in <Key>: <Value> format
        p0_3=re.compile(r'^(?P<key>[\s*\w]+.*)\: +(?P<value>[\S\s]+.*)$')

        #Active: PID:C9300-24UX,SN:FCW2134L00C
        #Standby: PID:C9300-24U,SN:FOC2129Z02H
        #Member: PID:C9300-24T,SN:FCW2125L07Y
        p0_4=re.compile(r'^\s*(?P<member_type>\S+):\s*PID:(?P<pid>\S+),SN:(?P<sn>\S+)$')

        #Below set of regular expressions are for special cases which could not be handled in above generic expressions
        #In variable name, the digit next to p identifies the heading under which this output line appears
        #For eg. p2_data1, this output line comes under heading matched with variable p2
        #Current Report: 1640690706       Previous: 1640626219
        p2_data1 = re.compile(r'^Current +Report: +(?P<current_report>[\S ]+)  +'r'Previous: +(?P<previous>.*)$')

        #Attempts: Total=0, Success=0, Fail=0  Ongoing Failure: Overall=0 Communication=0
        p6_data1= re.compile(r'^\s*(?P<key1>Attempts)\:\s+(?P<value1>.*)\s*(?P<key2>Ongoing Failure)\:\s*(?P<value2>.*)$')

        #Total: 88,  Purged: 0(0)
        p10_data1 = re.compile(r'^Total: +(?P<total>[\S ]+), +'r'Purged: +(?P<purged>.*)$')

        #Total Acknowledged Received: 0,  Waiting for Ack: 0(4)
        p10_data2= re.compile(r'^Total +Acknowledged +Received: +(?P<total_acknowledged_received>[\S ]+), +'r'Waiting +for +Ack: +(?P<waiting_for_ack>.*)$')

        #Available to Report: 8  Collecting Data: 0
        p10_data3= re.compile(r'^Available +to +Report: +(?P<available_to_report>[\S ]+)  +'r'Collecting +Data: +(?P<collecting_data>.*)$')

        #Maximum Display: 40  In Storage: 36,  MIA: 0(0)
        p10_data4= re.compile(r'^Maximum +Display: +(?P<maximum_display>[\S ]+)  +'r'In +Storage: +(?P<in_storage>[\S ]+), +'r'MIA: +(?P<mia>.*)$')

        #P:C9300-24UX,S:FCW2134L00C: P:C9300-24UX,S:FCW2134L00C, state[2], Trust Data INSTALLED  TrustId:903
        p11_data1 = re.compile(r'^[\w\s]*\:*\s*P\:+(?P<p>\S+).S\:+(?P<s>\S+)\:*.*TrustId\:+(?P<trustid>\d+)$')
        #P:C9300-24UX,S:FCW2134L00C: No Trust Data
        p11_data1_2 = re.compile(r'^[\w\s]*\:*\s*P\:+(?P<p>\S+).S\:+(?P<s>\S+)\: +(?P<trustvalue>No +Trust +Data)$')
        #P:C9300-24UX,S:FCW2134L00C: P:C9300-24UX,S:FCW2134L00C, state[2], Trust Data INSTALLED
        p11_data1_3 = re.compile(r'^[\w\s]*\:*\s*P\:+(?P<p>\S+).S\:+(?P<s>\S+)\:*.*(?P<trustvalue>Trust +Data +INSTALLED)$')
        
        #C9300-24UX: Total licenses found: 198
        p12_data1 = re.compile(r'^\s*(?P<pid>\S+)\: +Total licenses found\: +(?P<total_licenses_found>\d+)$')
        #P:C9300-24UX,S:FCW2134L00C:
        p12_data2 = re.compile(r'^\s*P\:(?P<pid>\S+)\,S\:(?P<sn>\S+)\:$')
        #hseck9: regid.2021-05.com.cisco.C9K_HSEC,1.0_90fdf411-3823-45bd-bd8c-5a5d0e0e1ea2 (3)
        p12_data3 = re.compile(r'^\s*hseck9\: +(?P<hseck9_entitlement_tag>regid\.\S.*) +\((?P<hseck9_no>\d+)\)$')

        for line in output.splitlines():
            line=line.strip()            
            m = p0.match(line)
            if m:
                group = m.groupdict()
                group['primary_load_time_percent'] = int(group['primary_load_time_percent'])
                group['secondary_load_time_percent'] = int(group['secondary_load_time_percent'])
                group['one_minute_load_percent'] = int(group['one_minute_load_percent'])
                group['five_minute_load_percent'] = int(group['five_minute_load_percent'])
                ret_dict.update(group)
                continue
            
            m = p0_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update(group)
                continue    
            
            #Set the dictionary position for main headings 
            m = p1.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('smart_licensing_status', {})
                continue
            
            m = p2.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('license_usage', {})
                continue

            m = p3.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('product_information', {})
                continue

            m = p4.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('agent_version', {})
                continue

            m = p5.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('upcoming_scheduled_jobs', {})
                continue

            m = p6.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('communication_statistics', {})
                continue

            m = p7.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('license_certificates', {})
                continue

            m = p8.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('ha_info', {})
                continue

            m = p9.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('reservation_info', {})
                continue

            m = p10.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('usage_report_summary', {})
                continue

            m = p11.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('other_info', {})
                continue

            m = p12.match(line)
            if m:
                group=m.groupdict()
                current_dict=ret_dict.setdefault('platform_provided_mapping_table', {})           
                continue

            #Setting the dictionary position for sub headings (2nd level and further levels down)
            m = p1_1.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('export_authorization_key', {})
                continue

            #In current output there is no data (key, value pairs) under sub heading "Features Authorized", so creating 
            #dictionary after checking the match for next data line. This is a special case and hence handled seperately
            m = p0_2.match(line)
            if m:
                group = m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('export_authorization_key',{}).setdefault('features_authorized', group['value'])
                continue
            
            m = p1_2.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('utility', {})
                continue    

            m = p1_3.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('smart_licensing_using_policy', {})
                continue    

            m = p1_4.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('account_information', {})
                continue    
         
            m = p1_5.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('data_privacy', {})
                continue     
            
            m = p1_6.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('transport', {})
                continue     
            
            m = p1_6_1.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('transport',{}).setdefault('proxy', {})
                continue     

            m = p1_7.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('miscellaneous', {})
                continue     

            m = p1_8.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('policy', {})
                continue     

            m = p1_8_1.match(line)
            if m:
                group=m.groupdict()
                group['policy_sub_header'] = group['policy_sub_header'].replace(' ','_').replace('(', "").replace(')', "").replace('/', '_').replace('-', '_')
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('policy',{}).setdefault(group['policy_sub_header'].lower(), {})
                continue 
            
            m = p1_9.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('usage_reporting', {})
                if ret_dict.get('communication_statistics'):
                    current_dict = ret_dict.setdefault('communication_statistics',{}).setdefault('usage_reporting', {})       
                continue 

            m = p2_1.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('license_usage',{}).setdefault(group['handle'].lower(), {}).setdefault(int(group['value']),{})
                handle_dict = current_dict
                continue 

            m = p2_1_1.match(line)
            if m:
                group=m.groupdict()
                current_dict = handle_dict.setdefault('measurements',{})
                continue 

            m = p2_1_1_1.match(line)
            if m:
                group=m.groupdict()
                current_dict = handle_dict.setdefault('measurements',{}).setdefault('entitlement',{})
                continue 

            m = p3_1.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('product_information',{}).setdefault('udi', {})
                current_dict.update({
                        'pid': group['pid'],
                        'sn': group['sn']})
                continue     

            m = p3_2.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('product_information',{}).setdefault('ha_udi_list', {})
                continue     

            m = p6_1.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('communication_statistics',{}).setdefault('trust_establishment', {})
                continue     

            m = p6_2.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('communication_statistics',{}).setdefault('trust_acknowledgement', {})
                continue     

            m = p6_4.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('communication_statistics',{}).setdefault('result_polling', {})
                continue     

            m = p6_5.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('communication_statistics',{}).setdefault('authorization_request', {})
                continue     

            m = p6_6.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('communication_statistics',{}).setdefault('authorization_confirmation', {})
                continue     

            m = p6_7.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('communication_statistics',{}).setdefault('authorization_return', {})
                continue     

            m = p6_8.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('communication_statistics',{}).setdefault('trust_sync', {})
                continue     

            m = p6_9.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('communication_statistics',{}).setdefault('hello_message', {})
                continue     

            m = p9_1.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('reservation_info',{}).setdefault('overall_status', {})
                continue

            #In current output there is no data (key, value pairs) under sub heading "Purchased Licenses", so creating 
            #dictionary after checking the match for next data line. This is a special case and hence handled seperately
            m = p0_5.match(line)
            if m:
                group = m.groupdict()
                current_dict = ret_dict.setdefault('reservation_info',{}).setdefault('purchased_licenses', group['value'])
                continue
            
            m = p9_2.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('reservation_info',{}).setdefault('authorizations', {})
                continue
            
            m = p9_2_1.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('reservation_info',{}).setdefault('authorizations',{}).setdefault('c9k_hsec' ,{})
                continue
            
            m = p9_2_1_1.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('reservation_info',{}).setdefault('authorizations',{}).setdefault('c9k_hsec' ,{}).setdefault('term_information' ,{})
                continue
                
            m = p9_3.match(line)
            if m:
                group=m.groupdict()
                current_dict = ret_dict.setdefault('reservation_info',{}).setdefault('last_reporting_not_required',{})
                continue
                
            m = p12_1.match(line)
            if m:
                group = m.groupdict()
                current_dict = ret_dict.setdefault('platform_provided_mapping_table',{}).setdefault('enforced_licenses',{})
                continue

            #Handling of header section ends here
            #Code sections below are for handling data lines
            
            #Dictionary for member types (Active, Standby, Member) needs to be created under two different sub headings
            #These subheadings contain different information for each member
            #To ensure these information (lines) are added to the dictionary under correct sub heading flags are used in
            #below section
            flag_term_information = False
            flag_overall_status = False
            m = p0_4.match(line)
            if m:
                group = m.groupdict()
                try:
                    temp_dict = ret_dict.get('reservation_info').get('authorizations').get('c9k_hsec')
                    if temp_dict.get('term_information') is not None:
                        flag_term_information = True
                        flag_overall_status = False
                except KeyError:
                    pass
                except AttributeError:
                    pass
                
                if not flag_term_information:
                    try:    
                        temp_dict = ret_dict.get('reservation_info')
                        if temp_dict.get('overall_status') is not None:
                            flag_overall_status = True
                        
                    except KeyError:
                        pass
                    except AttributeError:
                        pass
                
                if flag_term_information:
                    current_dict = ret_dict.setdefault('reservation_info',{}).setdefault('authorizations', {}).setdefault('c9k_hsec' ,{}).setdefault('term_information' ,{}).setdefault(group['member_type'].lower(),{})
                    current_dict.update({
                            'pid': group['pid'],
                            'sn': group['sn']})
                    continue    
                if flag_overall_status:
                    current_dict = ret_dict.setdefault('reservation_info',{}).setdefault('overall_status', {}).setdefault(group['member_type'].lower(),{})
                    current_dict.update({
                            'pid': group['pid'],
                            'sn': group['sn']})
                    continue   

                if group['member_type'] == 'UDI':
                    current_dict.update({
                        'pid': group['pid'],
                        'sn': group['sn']})
                    continue
                else:
                    current_dict = ret_dict.setdefault('product_information',{}).setdefault('ha_udi_list', {}).setdefault(group['member_type'].lower(),{})
                    current_dict.update({
                        'pid': group['pid'],
                        'sn': group['sn']})
                    continue

            #Below sections are to handle data lines
            #P:C9300-24UX,S:FCW2134L00C:
            m = p12_data2.match(line)
            if m:
                group = m.groupdict()
                current_dict = ret_dict.setdefault('platform_provided_mapping_table', {}).setdefault('enforced_licenses', {}).setdefault(group['sn'].lower(), {})
                current_dict.update({'pid': group['pid']})
                continue
            
            #Generalised expression for handling <key>:<value> paired lines
            #Data lines that required special handling are done below with further checks and regular expressions
            m = p0_3.match(line)
            if m:
            
                m1 = p12_data3.match(line)
                if m1:
                    group = m1.groupdict()
                    current_dict.update({'hseck9_entitlement_tag': group['hseck9_entitlement_tag'],
                                         'hseck9_no': int(group['hseck9_no'])})
                    continue                     
                
                m1 = p12_data1.match(line)
                if m1:
                    group = m1.groupdict()          
                    current_dict.update({'pid': group['pid'] , 'total_licenses_found': int(group['total_licenses_found'])})
                    continue
                    
                m1 = p11_data1_2.match(line)
                if m1:
                    group = m1.groupdict()
                    current_dict = ret_dict.setdefault('other_info', {}).setdefault('trust_data', {}).setdefault(group['s'].lower(), {})
                    current_dict.update({'p': group['p'], 'trustvalue':group['trustvalue']})
                    current_dict = ret_dict.setdefault('other_info', {})
                    continue                
                    
                m1 = p11_data1.match(line)
                if m1:
                    group = m1.groupdict()
                    group['s'] = group['s'].replace(':',"").replace(',',"")
                    current_dict = ret_dict.setdefault('other_info', {}).setdefault('trust_data', {}).setdefault(group['s'].lower(), {})
                    group['trustid'] = int(group['trustid'])
                    current_dict.update({'p': group['p'], 'trustid':group['trustid']})
                    current_dict = ret_dict.setdefault('other_info', {})
                    continue    
                    
                m1 = p11_data1_3.match(line)
                if m1:
                    group = m1.groupdict()
                    current_dict = ret_dict.setdefault('other_info', {}).setdefault('trust_data', {}).setdefault(group['s'].lower(), {})
                    current_dict.update({'p': group['p'], 'trustvalue':group['trustvalue']})
                    current_dict = ret_dict.setdefault('other_info', {})
                    continue
                    
                m1= p10_data1.match(line)
                if m1:
                    group = m1.groupdict()            
                    group['total'] = int(group['total'])
                    current_dict.update(group)
                    continue

                m1= p10_data2.match(line)
                if m1:
                    group = m1.groupdict()
                    group['total_acknowledged_received'] = int(group['total_acknowledged_received'])
                    current_dict.update(group)
                    continue

                m1 = p10_data3.match(line)
                if m1:
                    group = m1.groupdict()
                    group['available_to_report'] = int(group['available_to_report'])
                    group['collecting_data'] = int(group['collecting_data'])
                    current_dict.update(group)
                    continue

                m1 = p10_data4.match(line)
                if m1:
                    group = m1.groupdict()
                    group['maximum_display'] = int(group['maximum_display'])
                    group['in_storage'] = int(group['in_storage'])
                    current_dict.update(group)
                    continue

                m1 = p6_data1.match(line)        
                if m1:
                    group = m1.groupdict()
                    key1 = group['key1'].replace(' ', '_').lower()
                    key2 = group['key2'].replace(' ', '_').lower()
                    value1 = group['value1'].strip()
                    value2 = group['value2'].strip()
                    current_dict.update({key1: value1})
                    current_dict.update({key2: value2})
                    continue

                m1 = p2_data1.match(line)
                if m1:
                    group = m1.groupdict()          
                    group['current_report'] = int(group['current_report'].strip())
                    group['previous'] = int(group['previous'].strip())
                    current_dict.update(group)
                    current_dict = handle_dict
                    continue
                else:
                    group = m.groupdict()
                    if 'sizeof' in group['key']:
                        key = group['key'].strip().replace('(', "_").replace(' ','_').replace(')', "").lower()
                        current_dict.update({key: int(group['value'])})              
                        continue
                    key = group['key'].replace(' ', '_').replace('.', '_').replace('-', "").replace(':', "").replace('(', "").replace(')', "").lower()
                    if key == 'server_identity_check' or key == 'vrf':
                        current_dict = ret_dict.setdefault('smart_licensing_status',{}).setdefault('transport',{})   
                    if key == 'soft_enforced':
                        current_dict = handle_dict
                        
                    if group['value'].isdigit():
                        current_dict.update({key: int(group['value'])}) 
                        continue
                    else:
                        #ForkedPdb().set_trace()
                        current_dict.update({key: group['value']})
                        continue                   

        return ret_dict
        
