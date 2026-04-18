"""starOS implementation of show_license_info.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema, Optional, ListOf

class LicenseSchema(MetaParser):
    """Schema for show license information"""

    schema = {
        'license_info': 
        {
            'information':
            {
                'Comment': str,
                Optional('Chassis SN'): str,
                'Issued':
                {
                    'Year':str,
                    'Month':str,
                    'Day':str,
                },
                Optional('Expires'):
                {
                    Optional('Year'):str,
                    Optional('Month'):str,
                    Optional('Day'):str,
                },
                'Key Number':str,
                'Session Limits':
                {
                     Any():{
                        'Sessions':str,
                     }
                },
                'Status':
                {
                    'Chassis':ListOf(str),
                    'Status':str,
                },
            },
        },
    }


class ShowLicense(LicenseSchema):
    """Parser for show license information"""

    cli_command = 'show license information'

    """
Key Information (installed key):
  Comment       SWIFT License
  Chassis SN    FLM2039N9QG
  Issued        Monday March 28 18:22:43 CST 2022
  Expires       Wednesday September 28 19:22:43 CDT 2022
  Issued By     Cisco Systems
  Key Number    214140
Enabled Features:
  Feature                                             Applicable Part Numbers
  --------------------------------------------------  -----------------------------
  GGSN:                                               [ ASR5K-00-GN10SESS / ASR5K-00-GN01SESS ]
   + DHCP                                             [ ASR5K-00-CSXXDHCP ]
  IPv4 Routing Protocols                              [ none ]
  Enhanced Charging Bundle 2:                         [ ASR5K-00-CS01ECG2 ]
   + DIAMETER Closed-Loop Charging Interface          [ ASR5K-00-CSXXDCLI ]
   + Enhanced Charging Bundle 1                       [ ASR5K-00-CS01ECG1 ]
  IPSec                                               [ ASR5K-00-CS01I-K9 / ASR5K-00-CS10I-K9 ]
  Session Recovery                                    [ ASR5K-00-PN01REC / ASR5K-00-HA01REC 
                                                        ASR5K-00-00000000 / ASR5K-00-GN01REC 
                                                        ASR5K-00-SN01REC / ASR5K-00-IS10PXY 
                                                        ASR5K-00-IS01PXY / ASR5K-00-HWXXSREC 
                                                        ASR5K-00-PW01REC / ASR5K-00-SY01R-K9 
                                                        ASR5K-00-IG01REC / ASR5K-00-PC10SR 
                                                        ASR5K-00-EG01SR / ASR5K-00-FY01SR 
                                                        ASR5K-00-CS01LASR / ASR5K-00-FY01USR 
                                                        ASR5K-00-EW01SR / ASR5K-00-SM01SR 
                                                        ASR5K-00-S301SR ]
  Proxy MIP:                                          [ ASR5K-00-PN01PMIP / ASR5K-00-GN01PMIP 
                                                        ASR5K-00-GN10PMIP ]
   + FA                                               [ ASR5K-00-FAXXFA ]
  IPv6                                                [ N/A / N/A ]
  Lawful Intercept                                    [ ASR5K-00-CSXXLI ]
  TACACS+                                             [ ASR5K-00-CSXXTACA ]
  Inter-Chassis Session Recovery                      [ ASR5K-00-HA10GEOR / ASR5K-00-HA01GEOR 
                                                        ASR5K-00-GN10ICSR / ASR5K-00-GN01ICSR 
                                                        ASR5K-00-PW01ICSR / ASR5K-00-IGXXICSR 
                                                        ASR5K-00-PC10GR / ASR5K-00-SW01ICSR 
                                                        ASR5K-00-SG01ICSR / ASR5K-00-EG01ICSR 
                                                        ASR5K-00-EG10ICSR / ASR5K-00-SM01ICSR 
                                                        ASR5K-00-SM10ICSR / ASR5K-00-ME01ICSR 
                                                        QVPCA-00-ME10ICSR ]
  RADIUS AAA Server Groups                            [ ASR5K-00-CSXXAAA ]
  Intelligent Traffic Control:                        [ ASR5K-00-CS01ITC ]
   + Dynamic Radius extensions (CoA and PoD)          [ ASR5K-00-CSXXDYNR ]
   + Per-Subscriber Traffic Policing/Shaping          [ ASR5K-00-CSXXTRPS ]
  Enhanced Lawful Intercept                           [ ASR5K-00-CS01ELI / ASR5K-00-CS10ELI ]
  Dynamic Policy Interface:                           [ ASR5K-00-CS01PIF ]
   + DIAMETER Closed-Loop Charging Interface          [ ASR5K-00-CSXXDCLI ]
  Application Detection and Control                   [ ASR5K-00-CS01P2PD ]
  MPLS                                                [ ASR5K-00-CS01MPLS / ASR5K-00-CS10MPLS ]
  PGW                                                 [ ASR5K-00-PW10GTWY / ASR5K-00-PW01LIC ]
  SGW                                                 [ ASR5K-00-SW10LIC / ASR5K-00-SW01BASE ]
  ULI Reporting                                       [ ASR5K-00-CSXXULIR ]
  Always On Licensing                                 [ ASR5K-00-GNXXAOL ]
  Smartphone Tethering Detection                      [ ASR5K-00-CD01STD ]
  SGSN S4 Interface                                   [ ASR5K-00-SN01S4 / ASR5K-00-SN10S4 ]
  Local Policy Decision Engine                        [ ASR5K-00-PWXXDEC ]
  EPDG                                                [ ASR5K-00-EG01S-K9 / ASR5K-00-EG10S-K9 ]
  HTTP Header Enrichment and Encryption               [ ASR5K-00-CS01E-K9 ]
  DNS Snooping                                        [ ASR5K-00-CS01DNSS ]
  SAE GW Bundle                                       [ ASR5K-00-SG01 / ASR5K-00-SG10 ]
  AT&T Only License Suppression                       [ ASR5K-12-PNXXLICS ]
  Persistent Lawful Intercept                         [ ASR5K-00-CS10PLI ]
  Rate Limiting Function (Throttling)                 [ ASR5K-00-CSXGTDT ]
  Flow Aware Packet Acceleration Per ASR5500-U Syste  [ ASR55-00-CSXFAPU ]
  EPC Gw VoLTE enhancements                           [ ASR5K-00-EP01VLE ]
  Simultaneous EPC procedures per System              [ ASR5K-00-EPXSCUBR ]
  NPLI for IMS Calls, per System                      [ ASR5K-00-MPSXNPLI ]
  Separate Paging Profile for IMS Calls, 1K Sessions  [ ASR5K-00-SW01SPP ]
  EPC Support for GTP Overload Control, Per System    [ ASR5K-00-EPXGTPO ]
  EPC-GW Support for Wi-Fi Integration, 1K Sessions   [ ASR5K-00-EP01WIFI ]
  5G NSA Enablement Fee, Network Wide                 [ ASR5K-00-EP51NSE / LIF5K-00-EP51NSE 
                                                        QVPCA-00-EP51NSE / QVPCF-00-EP51NSE ]
  5G NSA Feature Set 100K Sess VPCSW Active           [ ASR5K-00-EP51NSLP / LIF5K-00-EP51NSLP 
                                                        QVPCA-00-EP51NSLP / QVPCF-00-EP51NSLP ]
Session Limits:
                 Sessions  Session Type
               ----------  -----------------------
                 10000000  GGSN
                 10000000  ECS
                  6500000  Application Detection and Control
                 10000000  PGW
                 10000000  SGW
                    10000  EPDG
                 10000000  SAE GW Bundle
                     1000  5G NSA Feature Set 100K Sess VPCSW Active
CARD License Counts:
  [none]
Status:
  Chassis MEC SN         Matches
  License Status         Good
    
#Virtual
Key Information (installed key):
  Comment       SWIFT License
  Device 1      None Specified
  Device 2      None Specified
  Chassis Type Any Hardware
  Issued        Wednesday March 29 05:24:21 ART 2023
  Issued By     Cisco Systems
  Key Number    810295
Enabled Features:
  Feature                                             Applicable Part Numbers
  --------------------------------------------------  -----------------------------
  GGSN:                                               [ ASR5K-00-GN10SESS / ASR5K-00-GN01SESS ]
   + DHCP                                             [ ASR5K-00-CSXXDHCP ]
  IPv4 Routing Protocols                              [ none ]
  Enhanced Charging Bundle 2:                         [ ASR5K-00-CS01ECG2 ]
   + DIAMETER Closed-Loop Charging Interface          [ ASR5K-00-CSXXDCLI ]
   + Enhanced Charging Bundle 1                       [ ASR5K-00-CS01ECG1 ]
  IPSec                                               [ ASR5K-00-CS01I-K9 / ASR5K-00-CS10I-K9 ]
  Proxy MIP:                                          [ ASR5K-00-PN01PMIP / ASR5K-00-GN01PMIP 
                                                        ASR5K-00-GN10PMIP ]
   + FA                                               [ ASR5K-00-FAXXFA ]
  IPv6                                                [ N/A / N/A ]
  Lawful Intercept                                    [ ASR5K-00-CSXXLI ]
  Layer 2 Traffic Management                          [ ASR5K-00-CS01VLAN ]
  GGSN Dynamic QoS Renegotiation                      [ ASR5K-00-GN01DQSR ]
  Inter-Chassis Session Recovery                      [ ASR5K-00-HA10GEOR / ASR5K-00-HA01GEOR 
                                                        ASR5K-00-GN10ICSR / ASR5K-00-GN01ICSR 
                                                        ASR5K-00-PW01ICSR / ASR5K-00-IGXXICSR 
                                                        ASR5K-00-PC10GR / ASR5K-00-SW01ICSR 
                                                        ASR5K-00-SG01ICSR / ASR5K-00-EG01ICSR 
                                                        ASR5K-00-EG10ICSR / ASR5K-00-SM01ICSR 
                                                        ASR5K-00-SM10ICSR / ASR5K-00-ME01ICSR 
                                                        QVPCA-00-ME10ICSR ]
  RADIUS AAA Server Groups                            [ ASR5K-00-CSXXAAA ]
  Intelligent Traffic Control:                        [ ASR5K-00-CS01ITC ]
   + Dynamic Radius extensions (CoA and PoD)          [ ASR5K-00-CSXXDYNR ]
   + Per-Subscriber Traffic Policing/Shaping          [ ASR5K-00-CSXXTRPS ]
  Dynamic Policy Interface:                           [ ASR5K-00-CS01PIF ]
   + DIAMETER Closed-Loop Charging Interface          [ ASR5K-00-CSXXDCLI ]
  Application Detection and Control                   [ ASR5K-00-CS01P2PD ]
  Per Subscriber Stateful Firewall                    [ ASR5K-00-CS01FW ]
  SGSN Software License                               [ ASR5K-00-SN10SESS / ASR5K-00-SN01SESS ]
  PGW                                                 [ ASR5K-00-PW10GTWY / ASR5K-00-PW01LIC ]
  SGW                                                 [ ASR5K-00-SW10LIC / ASR5K-00-SW01BASE ]
  MME license:                                        [ ASR5K-00-ME01BASE / ASR5K-00-ME10LIC ]
   + Session Recovery                                 [ ASR5K-00-PN01REC / ASR5K-00-HA01REC 
                                                        ASR5K-00-00000000 / ASR5K-00-GN01REC 
                                                        ASR5K-00-SN01REC / ASR5K-00-IS10PXY 
                                                        ASR5K-00-IS01PXY / ASR5K-00-HWXXSREC 
                                                        ASR5K-00-PW01REC / ASR5K-00-SY01R-K9 
                                                        ASR5K-00-IG01REC / ASR5K-00-PC10SR 
                                                        ASR5K-00-EG01SR / ASR5K-00-FY01SR 
                                                        ASR5K-00-CS01LASR / ASR5K-00-FY01USR 
                                                        ASR5K-00-EW01SR / ASR5K-00-SM01SR 
                                                        ASR5K-00-S301SR ]
   + Enhanced Lawful Intercept                        [ ASR5K-00-CS01ELI / ASR5K-00-CS10ELI ]
  NAT/PAT with DPI                                    [ ASR5K-00-CS01NAT ]
  GRE Interface Tunneling                             [ ASR5K-00-CS10GRET / ASR5K-00-CS01GRET ]
  Optimized Paging                                    [ ASR5K-00-CSXXOPTP ]
  MME Resiliency Bundle                               [ ASR5K-00-MEXXRES ]
  Local Policy Decision Engine                        [ ASR5K-00-PWXXDEC ]
  EPDG                                                [ ASR5K-00-EG01S-K9 / ASR5K-00-EG10S-K9 ]
  HTTP Header Enrichment and Encryption               [ ASR5K-00-CS01E-K9 ]
  DNS Snooping                                        [ ASR5K-00-CS01DNSS ]
  SAE GW Bundle                                       [ ASR5K-00-SG01 / ASR5K-00-SG10 ]
  Flow Aware Packet Acceleration Per ASR5500-U Syste  [ ASR55-00-CSXFAPU ]
  MTC Feature Set                                     [ ASR5K-00-ME01CNG ]
  EPC-GW Support for Wi-Fi Integration, 1K Sessions   [ ASR5K-00-EP01WIFI ]
  ADC Trigger Over Gx, 1K Sessions                    [ ASR5K-00-CS01ADGX ]
  EPC-GW Non-Standard QCI Support, 1K Sessions        [ ASR5K-00-EP01QCNS ]
  Per Subscriber Traffic Shaping APN-AMBR, 1K Sessio  [ ASR5K-00-PW01TSPS ]
  SGSN Direct Tunnel                                  [ ASR5K-00-SN01DIRT ]
  SGSN Iu/Gb Flex and Pooling                         [ ASR5K-00-SN01FLEX ]
  5G NSA Enablement Fee, Network Wide                 [ ASR5K-00-EP51NSE / LIF5K-00-EP51NSE 
                                                        QVPCA-00-EP51NSE / QVPCF-00-EP51NSE ]
  5G NSA Feature Set 100K Sess VPCSW Active           [ ASR5K-00-EP51NSLP / LIF5K-00-EP51NSLP 
                                                        QVPCA-00-EP51NSLP / QVPCF-00-EP51NSLP ]
Session Limits:
                 Sessions  Session Type
               ----------  -----------------------
                  7000000  GGSN
                 10000000  ECS
                  7000000  Application Detection and Control
                  7000000  Per Subscriber Stateful Firewall
                  9100000  PGW
                  9100000  SGW
                  7000000  MME license
                  7000000  EPDG
                  2100000  SAE GW Bundle
                  7000000  SGSN Direct Tunnel
                  7000000  SGSN Iu/Gb Flex and Pooling
                  7000000  5G NSA Feature Set 100K Sess VPCSW Active
CARD License Counts:
  [none]
NOTICE: The above features and limits have been reduced because this
        license includes capabilities beyond what the scale supports.
Status:
  Chassis Type           qvpc-di (Any Hardware)
  License Status         Good (Any Hardware) 
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        license_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'Comment\s+(?P<comment>.+$)')
        p1= re.compile(r'Chassis\sSN\s+(?P<chassis>.+$)')
        p2 = re.compile(r'Issued\s+\w+\s(?P<month_issued>\w+)\s(?P<day_issued>\d+)\s\d+:\d+:\d+\s\w+\s(?P<year_issued>\d+$)')
        p3 = re.compile(r'Expires\s+\w+\s(?P<month_exp>\w+)\s(?P<day_exp>\d+)\s\d+:\d+:\d+\s\w+\s(?P<year_exp>\d+$)')
        p4 = re.compile(r'Key\sNumber\s+(?P<key_number>\d+$)')
        p5 = re.compile(r'^\s*(?P<sessions>(\d+))\s+(?P<type>(.+$))')
        p6 = re.compile(r'(Chassis MEC SN\s+(?P<chassis_mec>.+)|Chassis Type\s+(?P<chassis_type>.+)$)')
        p7 = re.compile(r'License\sStatus\s+(?P<status>.*$)')

        for line in out.splitlines():
            line = line.strip()
            
            m = p0.match(line)
            if m:
                if 'license_info' not in license_dict:
                    result_dict = license_dict.setdefault('license_info',{})
                comment = m.groupdict()['comment']
                result_dict['information']={}
                result_dict['information']['Comment'] = comment
                continue

            m = p1.match(line)
            if m:
                if 'license_info' not in license_dict:
                    result_dict = license_dict.setdefault('license_info',{})
                chassis = m.groupdict()['chassis']
                result_dict['information']['Chassis SN'] = chassis
                continue

            m = p2.match(line)
            if m:
                if 'license_info' not in license_dict:
                    result_dict = license_dict.setdefault('license_info',{})
                month_issued = m.groupdict()['month_issued']
                year_issued = m.groupdict()['year_issued']
                day_issued = m.groupdict()['day_issued']
                result_dict['information']['Issued'] = {}
                result_dict['information']['Issued']['Month'] = month_issued
                result_dict['information']['Issued']['Year'] = year_issued
                result_dict['information']['Issued']['Day'] = day_issued
                continue
                
            m = p3.match(line)
            if m:
                if 'license_info' not in license_dict:
                    result_dict = license_dict.setdefault('license_info',{})
                month_exp = m.groupdict()['month_exp']
                year_exp = m.groupdict()['year_exp']
                day_exp = m.groupdict()['day_exp']
                result_dict['information']['Expires'] = {}
                result_dict['information']['Expires']['Month'] = month_exp
                result_dict['information']['Expires']['Year'] = year_exp
                result_dict['information']['Expires']['Day'] = day_exp
                continue

            m = p4.match(line)
            if m:
                if 'license_info' not in license_dict:
                    result_dict = license_dict.setdefault('license_info',{})
                key_number = m.groupdict()['key_number']
                result_dict['information']['Key Number'] = key_number
                continue

            m = p5.match(line)
            if m:
                if 'license_info' not in license_dict:
                    result_dict = license_dict.setdefault('license_info',{})
                if 'Session Limits' not in license_dict['license_info']['information']:
                    result_dict['information'].setdefault('Session Limits',{})
                sessions = m.groupdict()['sessions']
                type = m.groupdict()['type']
                result_dict['information']['Session Limits'][type] = {}
                result_dict['information']['Session Limits'][type]['Sessions'] = sessions
                continue

            m = p6.match(line)
            if m:
                if 'license_info' not in license_dict:
                    result_dict = license_dict.setdefault('license_info',{})
                ch_type = m.groupdict()['chassis_type']
                chassis_mec = m.groupdict()['chassis_mec']
                #result_dict['information']['Status'] = {}
                #result_dict['information']['Status']['Chassis MEC'] = chassis_mec
                #ch_type = str(m.groupdict()['chassis_type'])
                if 'Status' not in result_dict['information']:
                    result_dict['information']['Status'] = {'Chassis': []}
                if ch_type: 
                    #result_dict['information']['Status'] = {}
                    result_dict['information']['Status']['Chassis'].append(ch_type)
                #result_dict['information']['Status'] = {}
                if chassis_mec:
                    result_dict['information']['Status']['Chassis'].append(chassis_mec)
                continue

            m = p7.match(line)
            if m:
                if 'license_info' not in license_dict:
                    result_dict = license_dict.setdefault('license_info',{})
                status = m.groupdict()['status']
                result_dict['information']['Status']['Status'] = status
                continue

        return license_dict
