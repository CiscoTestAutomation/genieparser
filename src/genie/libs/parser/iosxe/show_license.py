''' show_license.py

IOSXE parsers for the following show commands:
    * show license
    * show license udi
    * show license summary
    * show license rum id all
    * show license status
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or

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
        # 	        Period Used: 0  minute  0  second
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
class ShowLicenseUdiSchema(MetaParser):
    """Schema for show license udi"""
    schema = {
            'slotid': str,
            'pid': str,
            'sn': str,
            'udi': str
            }

class ShowLicenseUdi(ShowLicenseUdiSchema):
    """Parser for show license udi"""
    cli_command = 'show license udi'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # slotid pid sn udi
        p1 = re.compile(r"(?P<slotid>\S+)\s+(?P<pid>\S+)\s+(?P<sn>\S+)\s+(?P<udi>\S+)")
        # fixed length strings on third line
        # slotid: 9
        # pid   : 23
        # sn    : 15
        # udi   : 33
        # total 80 chars
        #SlotID   PID                    SN                      UDI
        #--------------------------------------------------------------------------------
        #*        ASR1001-X             JAF211403VH     ASR1001-X:JAF211403VH
        ret_dict={}
        for line in out.splitlines():
            line=line.strip()

            # udi line
            m=p1.match(line)
            if m:
                group=m.groupdict()
                ret_dict.update({k:str(v) for k, v in group.items()})
                continue
            '''
            if line.startswith('SlotID') or line.startswith('------'):
              continue
            else:
              ret_dict.update({'slotid':line[0:9].strip()})
              ret_dict.update({'pid':line[9:30].strip()})
              ret_dict.update({'sn':line[30:47].strip()})
              ret_dict.update({'udi':line[47:].strip()})
            ''' 

        return ret_dict

# ----------------------
# =================
# Schema for:
#  * 'show license summary'
# =================
class ShowLicenseSummarySchema(MetaParser):
    """Schema for show license udi"""
    schema = {
        'license_usage': {
            Any(): {
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
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        license_summ_dict = {}
        
        result_dict = {}

        # network-advantage       (C9300-48 Network Advan...)       1 IN USE
        # dna-advantage           (C9300-48 DNA Advantage)          1 IN USE

        # C9300 48P DNA Advantage  (C9300-48 DNA Advantage)          2 AUTHORIZED
        p0 = re.compile(r"^(?P<license>.+?)\s+\((?P<entitlement>.+)\)\s+(?P<count>\d+)\s+(?P<status>.+)$")

        for line in out.splitlines():
            line=line.strip()

            # udi line
            m=p0.match(line)
            if m:
                if 'license_usage' not in license_summ_dict:
                    result_dict = license_summ_dict.setdefault('license_usage', {})
                license = m.groupdict()['license']
                entitlement = m.groupdict()['entitlement']
                count = m.groupdict()['count']
                status = m.groupdict()['status']
                result_dict[license] = {}
                result_dict[license]['entitlement'] = entitlement
                result_dict[license]['count'] = count
                result_dict[license]['status'] = status
                continue
        return license_summ_dict

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
