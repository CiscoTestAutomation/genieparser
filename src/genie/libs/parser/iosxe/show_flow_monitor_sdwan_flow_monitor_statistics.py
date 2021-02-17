# Python
import re
# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


class ShowFlowMonitorSdwanFlowMonitorStatisticsSchema(MetaParser):
    ''' Schema for show flow monitor sdwan_flow_monitor statistics'''
    schema = {
        "cache_type": str,
        "cache_size": int,
        "current_entries": int,
        "high_watermark": int,
        "flows_added": int,
        "flows_aged":{
                    "total_flows_aged" : int,
                    Optional("active_timeout_secs"): int,
                    Optional("active_time"): int,
                    Optional("inactive_timeout_secs"):int,
                    Optional("inactive_time"):int
                }
            }


class ShowFlowMonitorSdwanFlowMonitorStatistics(ShowFlowMonitorSdwanFlowMonitorStatisticsSchema):

    """ Parser for "show flow monitor sdwan_flow_monitor statistics" """
    
    cli_command = "show flow monitor {flow_monitor_name} statistics"

    def cli(self,flow_monitor_name='',output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(flow_monitor_name=flow_monitor_name))
        else:
            out = output

        #Cache type: Normal (Platform cache)
        p1=re.compile(r'Cache+\s+type+\:+\s+(?P<cache_type>[\w\W\s()]+)')

        #Cache size: 200000
        p2=re.compile(r'Cache+\s+size+\:+\s+(?P<cache_size>\d+)')

        #Current entries: 12534
        p3=re.compile(r'Current+\s+entries+\:+\s+(?P<current_entries>\d+)')

        #High Watermark: 16030
        p4=re.compile(r'High+\s+Watermark+\:+\s+(?P<high_watermark>\d+)')

        #Flows added: 197808242
        p5=re.compile(r'Flows+\s+added+\:+\s+(?P<flows_added>\d+)')

        #Flows aged: 197795708
        p6=re.compile(r'Flows+\s+aged+\:+\s+(?P<flows_aged>\d+)')

        #- Active timeout ( 60 secs) 11897289
        p7=re.compile(r'\-+\s+Active+\s+timeout+\s+\(+\s+(?P<active_time_secs>\d+)+\s+secs+\)+\s+(?P<active_time>\d+)')

        #- Inactive timeout ( 10 secs) 185898419
        p8=re.compile(r'\-+\s+Inactive+\s+timeout+\s+\(+\s+(?P<inactive_time_secs>\d+)+\s+secs+\)+\s+(?P<inactive_time>\d+)')


        parsed_dict={}
        check_flag=0

        for line in out.splitlines():
            m1= p1.match(line)
            if m1:
                #{'cache_type':'Normal (Platform cache)'}
                groups=m1.groupdict()
                parsed_dict['cache_type']=groups['cache_type']

            m2= p2.match(line)
            if m2:
                #{'cache_size':'200000'}
                groups=m2.groupdict()
                parsed_dict['cache_size']=int(groups['cache_size'])

            m3= p3.match(line)
            if m3:
                #{'current_entries':'12534'}
                groups=m3.groupdict()
                parsed_dict['current_entries']=int(groups['current_entries'])

            m4= p4.match(line)
            if m4:
                #{'high_watermark':'16030}
                groups=m4.groupdict()
                parsed_dict['high_watermark']=int(groups['high_watermark'])

            m5= p5.match(line)
            if m5:
                #{'flows_added':'197808242'}
                groups=m5.groupdict()
                parsed_dict['flows_added']=int(groups['flows_added'])

            m6= p6.match(line)
            if m6:
                #{'flows_aged':'1997795708'}
                parsed_dict['flows_aged']={}
                cur_dict=parsed_dict['flows_aged']
                groups=m6.groupdict()
                cur_dict['total_flows_aged']=int(groups['flows_aged'])

            m7=p7.match(line)
            if m7:
                #{'active_time_secs':'60','active_time':'11897289'}
                groups=m7.groupdict()
                cur_dict['active_timeout_secs']= int(groups['active_time_secs'])
                cur_dict['active_time']= int(groups['active_time'])

            m8=p8.match(line)
            if m8:
                #{'inactive_time_secs':'10','inactive_time':'185898419'}
                groups=m8.groupdict()
                cur_dict['inactive_timeout_secs']= int(groups['inactive_time_secs'])
                cur_dict['inactive_time']= int(groups['inactive_time'])

        return parsed_dict
