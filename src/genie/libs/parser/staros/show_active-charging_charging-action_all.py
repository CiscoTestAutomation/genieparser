"""starOS implementation of show_active-charging_charging-action_all.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowActiveChargingSchema(MetaParser):
    """Schema for show active-charging charging-action all"""

    schema = {
        'charging-action': {
            Any():{
                Optional('Content ID'): int,
                Optional('EGCDRs'): str,
                Optional('Limit For Uplink Bandwidth'): str,
                Optional('Peak Data Rate Uplink'): str,
                Optional('Peak Burst Size Uplink'): str,
                Optional('Limit For Downlink Bandwidth'): str,
                Optional('Peak Data Rate Downlink'): str,
                Optional('Peak Burst Size Downlink'): str,
                Optional('Credit-Control'): str,
                Optional('Xheader-Insert'): str,
                Optional('Encryption Type'): str,
                Optional('Encryption Key'): str,
                Optional('Redirect URL'): str,
                Optional('Discard'): str,
            },
        }
    }


class ShowActiveCharging(ShowActiveChargingSchema):
    """Parser for show active-charging charging-action all"""

    cli_command = 'show active-charging charging-action all'

    """
   Charging Action Name: namecg
     Content ID: 100
     Service ID: 0
     EDRs: Disabled
     EGCDRs: Enabled 
         Rf: Disabled
       UDRs: Enabled
     Flow Idle Timeout: 300 (secs)
     Limit For Flow Type: Disabled
     Bandwidth ID: 0
     Limit For Uplink Bandwidth: Enabled 
       Peak Data Rate : 512000 bits/second
       Peak Burst Size: 48000 bytes
       Violate Action : Discard
     Limit For Downlink Bandwidth: Enabled 
       Peak Data Rate : 512000 bits/second
       Peak Burst Size: 48000 bytes
       Violate Action : Discard
     Throttle-Suppress Timeout: n/a
     QoS Renegotiate Traffic-Class: Disabled
     QoS Class Identifier: Not Configured
     IP Type of Service: Not Configured
     Tethering Block Feature: Not Configured
        IP-TTL Value: n/a
     Content Filtering: Enabled 
     Service Chain:     Not Configured
     UP Service Chain:   Not Configured
     Credit-Control: Enabled 
     Xheader-Insert: Xheadername
        Encryption Type: rc4md5  
        Encryption Key : Funa82FaCH1s3fev
        Message Type:    Request 
     Flow Action:
       Redirect URL: Disabled
       Redirect URL from OCS: Disabled
       Redirect to Video Server: Disabled
       Clear Quota Retry Timer: Disabled
       Conditional Redirect: Disabled
       Discard: Disabled
       Terminate-Flow: Disabled
       Terminate-Session: Disabled
       Rulebase Change: Disabled
     Billing Action:
       Event Data Record: Disabled
       GGSN charging Data Record: Enabled 
       Rf Accounting: Disabled
       User Data Record: Enabled 
       Radius Accounting Record: Disabled
     Charge Volume: ip bytes  
     PCO-Custom1 value: n/a
     Flow-Mapping Idle Timeout: 300 (secs)
     DNS Proxy Bypass: Disabled
     Discard on Readdressing Failure: Disabled
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        cca_dict = {}
        result_dict = {}

        # Define regular expression patterns
        p0 = re.compile(r'Charging Action Name:\s+(?P<name>\S+)')
        p1 = re.compile(r'Content ID:\s+(?P<content_id>\d+)')
        p2 = re.compile(r'EGCDRs:\s+(?P<egcdrs>\S+)')
        p3 = re.compile(r'Limit For Uplink Bandwidth:\s+(?P<enabled_ul>\S+)')
        p4 = re.compile(r'Peak Data Rate\s+:\s+(?P<peak_data_rate_ul>\S+\s+bits/second)')
        p5 = re.compile(r'Peak Burst Size:\s+(?P<peak_burst_size_ul>\S+\s+bytes)')
        p6 = re.compile(r'Limit For Downlink Bandwidth:\s+(?P<enabled_dl>\w+)')
        p7 = re.compile(r'Peak Data Rate\s+:\s+(?P<peak_data_rate_dl>\S+\s+bits/second)')
        p8 = re.compile(r'Peak Burst Size:\s+(?P<peak_burst_size_dl>\S+\s+bytes)')
        p9 = re.compile(r'Credit-Control:\s+(?P<credit_control>\S+)')
        p10 = re.compile(r'Xheader-Insert:\s+(?P<xheader_insert>\S+)')
        p11 = re.compile(r'Encryption Type:\s+(?P<encryption_type>\S+)')
        p12 = re.compile(r'Encryption Key\s+:\s+(?P<encryption_key>\S+)')
        p13 = re.compile(r'Redirect URL: (?P<redirect_url>\S+)')
        p14 = re.compile(r'Discard: (?P<discard>\S+)')

        # Split output by lines and iterate
        for line in out.splitlines():
            line = line.strip()
            
            # Charging Action Name
            m = p0.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                charging_action = m.groupdict()['name']
                result_dict[charging_action] = {}
                continue
            
            # Content ID
            m = p1.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                content_id = m.groupdict()['content_id']
                result_dict[charging_action]["Content ID"] = int(content_id)
                continue

            # EGCDRs
            m = p2.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                egcdrs = m.groupdict()['egcdrs']
                result_dict[charging_action]["EGCDRs"] = egcdrs
                continue

            # Limit For Uplink Bandwidth
            m = p3.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                limit_for_uplink = m.groupdict()['enabled_ul']
                result_dict[charging_action]["Limit For Uplink Bandwidth"] = limit_for_uplink
                continue

            # Peak Data Rate Uplink
            m = p4.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                peak_data_rate_ul = m.groupdict()['peak_data_rate_ul']
                result_dict[charging_action]["Peak Data Rate Uplink"] = peak_data_rate_ul
                continue

            # Peak Burst Size Uplink
            m = p5.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                peak_burst_size_ul = m.groupdict()['peak_burst_size_ul']
                result_dict[charging_action]["Peak Burst Size Uplink"] = peak_burst_size_ul
                continue

            # Limit For Downlink Bandwidth
            m = p6.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                limit_for_downlink = m.groupdict()['enabled_dl']
                result_dict[charging_action]["Limit For Downlink Bandwidth"] = limit_for_downlink
                continue

            # Peak Data Rate Downlink
            m = p7.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                peak_data_rate_dl = m.groupdict()['peak_data_rate_dl']
                result_dict[charging_action]["Peak Data Rate Downlink"] = peak_data_rate_dl
                continue

            # Peak Burst Size Downlink
            m = p8.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                peak_burst_size_dl = m.groupdict()['peak_burst_size_dl']
                result_dict[charging_action]["Peak Burst Size Downlink"] = peak_burst_size_dl
                continue

            # Credit-Control
            m = p9.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                credit_control = m.groupdict()['credit_control']
                result_dict[charging_action]["Credit-Control"] = credit_control
                continue

            # Xheader-Insert
            m = p10.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                xheader_insert = m.groupdict()['xheader_insert']
                result_dict[charging_action]["Xheader-Insert"] = xheader_insert
                continue

            # Encryption Type
            m = p11.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                encryption_type = m.groupdict()['encryption_type']
                result_dict[charging_action]["Encryption Type"] = encryption_type
                continue

            # Encryption Key
            m = p12.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                encryption_key = m.groupdict()['encryption_key']
                result_dict[charging_action]["Encryption Key"] = encryption_key
                continue

            # Redirect URL
            m = p13.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                redirect_url = m.groupdict()['redirect_url']
                result_dict[charging_action]["Redirect URL"] = redirect_url
                continue

            # Discard
            m = p14.match(line)
            if m:
                if 'charging-action' not in cca_dict:
                    result_dict = cca_dict.setdefault('charging-action', {})
                discard = m.groupdict()['discard']
                result_dict[charging_action]["Discard"] = discard
                continue

        return cca_dict