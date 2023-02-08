'''
show_product_analytics.py
IOSXE C9300 parsers for the following show commands: 
    * show product-analytics report summary
    * show product-analytics kpi summary
    * show product-analytics kpi report <id>
'''
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or, ListOf

from genie.libs.parser.utils.common import Common
from genie import parsergen

class ShowProductAnalyticsReportSummarySchema(MetaParser):
    """Schema for ShowProductAnalyticsReportSummary"""
    schema = {
        'paReports': {
            Any(): {
                'policy_version': str
            }
        }
    }

class ShowProductAnalyticsReportSummary(ShowProductAnalyticsReportSummarySchema):
    """Parser for show product analytics report summary"""

    cli_command = 'show product-analytics report summary'    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Report ID                   Policy Version   
        # --------------------------- ---------------- 
        # 1664338829                    17.11.1
        p1 = re.compile(r'^(?P<paReport_id>\d+)\s+(?P<policy_version>\S+)$')
        
        for line in out.splitlines():
           line = line.strip()
           m = p1.match(line)
           if m:
                groups = m.groupdict()
                paReport_id = int(groups['paReport_id'])
                paReport_id_dict = ret_dict.setdefault('paReports', {}).setdefault(paReport_id, {})
                paReport_id_dict['policy_version'] = groups['policy_version']
                continue
        return ret_dict

class ShowProductAnalyticsKpiSummarySchema(MetaParser):
    """Schema for ShowProductAnalyticsKpiSummary"""

    schema = {
        'report_id': {
            Any(): {
                'kpi_name': {
                    Any(): {             
                        'time_stamp': str,
                    }
                }
            }
        }
    }

class ShowProductAnalyticsKpiSummary(ShowProductAnalyticsKpiSummarySchema):
    """Parser for show product analytics kpi summary"""

    cli_command = 'show product-analytics kpi summary'
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Time                          Report ID                     KPI Name                   
        # ----------------------------- ----------------------------- ---------------------------
        # 10/05/2022 00:00:00            1664953200                      hardware_inventory 
        p1 = re.compile(r"^(?P<time_stamp>[\d\/]+ [\d\:]+)\s+(?P<report_id>\d+)\s+(?P<kpi_name>\S+)$")

        for line in out.splitlines():
           line = line.strip()
           m = p1.match(line)
           if m:
                groups = m.groupdict()
                report_id = int (groups['report_id'].strip())
                kpi_name = groups['kpi_name'].strip()
                report_dict = ret_dict.setdefault('report_id',{}).setdefault(report_id,{})
                kpi_dict = report_dict.setdefault('kpi_name',{}).setdefault(kpi_name,{})
                kpi_dict['time_stamp'] = groups['time_stamp'].strip()
                continue
        return ret_dict

class ShowProductAnalyticsKpiReportIdSchema(MetaParser):
    """Schema for ShowProductAnalyticsKpiReportId"""

    schema = {
        'report_id': {
            Any(): {
                'kpi_name': {
                    Any(): {             
                        'time_stamp': str,
                        'kpi_value': str,
                    }
                }
            }
        }
    }

class ShowProductAnalyticsKpiReportId(ShowProductAnalyticsKpiReportIdSchema):
    """Parser for: show product analytics kpi report <report>"""

    cli_command = 'show product-analytics kpi report {report}'

    def cli(self, report = "",  output=None):
        if output is None:
            cmd = self.cli_command.format(report=report)
            out = self.device.execute(cmd)    
        else:
            out = output

        ret_dict = {}

        # Report ID     : 1665964800
        p1 = re.compile(r'^Report +ID +: +(?P<report_id>\d+)$')

        # Computed at   : 10/16/2022 17:00:00
        p2 = re.compile(r'^Computed +at +: +(?P<time_stamp>([\d\/]+ [\d\:]+))$')

        # KPI Name      : hardware_inventory
        p3 = re.compile(r'^KPI +Name +: +(?P<kpi_name>\S+)$')

        # KPI Value     : [{"cname":"Switch2","serial_no":"FCW2137L0E2","part_no":"C9300-48U"},{"cname":"Switch8","serial_no":"FOC2624Y70Z","part_no":"C9300-48U"},{"cname":"c93xx Stack","serial_no":"FCW2137L0E2","part_no":"C9300-48U"},{"cname":"StackPort2/1","serial_no":"MOC2117A9QX","part_no":"STACK-T1-1M"},{"cname":"StackPort2/2","serial_no":"LCC2109G0LM","part_no":"STACK-T1-1M"},{"cname":"StackPort8/1","serial_no":"LCC2109G0LM","part_no":"STACK-T1-1M"},{"cname":"StackPort8/2","serial_no":"MOC2117A9QX","part_no":"STACK-T1-1M"},{"cname":"PowerSupply2/B","serial_no":"DCA2210G3R5","part_no":"PWR-C1-715WAC"},{"cname":"PowerSupply8/A","serial_no":"DTN2106V0HE","part_no":"PWR-C1-1100WAC"},{"cname":"FRUUplinkModule2/1","serial_no":"FOC19110PQ6","part_no":"C3850-NM-8-10G"},{"cname":"FRUUplinkModule8/1","serial_no":"FOC17167MHJ","part_no":"C3850-NM-4-1G"}]

        p4 = re.compile(r'^KPI +Value +: +(?P<kpi_value>.*)$')
        
        for line in out.splitlines():
            line = line.strip()
            # Report ID     : 1665964800
            m = p1.match(line)
            if m:
                group1 = m.groupdict()
                report_id= int(group1['report_id'])
                if 'report_id' not in ret_dict:
                    ret_dict['report_id'] = {}
                if report_id not in ret_dict:
                    report_dict=ret_dict['report_id'].setdefault(report_id,{})
                continue

            # Computed at   : 10/16/2022 17:00:00
            m = p2.match(line)
            if m:
                group2 = m.groupdict()
                continue

            # KPI Name      : hardware_inventory
            m = p3.match(line)
            if m:
                group3 = m.groupdict()
                kpi_name = group3['kpi_name']
                if 'kpi_name' not in report_dict:
                    kpi_dict1 = report_dict.setdefault('kpi_name',{}).setdefault(kpi_name,{})
                    kpi_dict1.update({'time_stamp':group2['time_stamp']})
                if kpi_name not in kpi_dict1:
                    kpi_dict2 = report_dict.setdefault('kpi_name',{}).setdefault(kpi_name,{})
                    kpi_dict2.update({'time_stamp':group2['time_stamp']})
                continue

            m = p4.match(line)
            if m:
                group4 = m.groupdict()
                if kpi_dict2:
                    kpi_dict2.update({'kpi_value':group4['kpi_value']})
                elif kpi_dict1:
                   kpi_dict1.update({'kpi_value':group4['kpi_value']}) 
                continue

        return ret_dict
