# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import genie.parsergen as pg
import re
import pprint


# ===========================================
# Schema for 'show system status'
# ===========================================


class ShowSystemStatusSchema(MetaParser):
    """ Schema for "show system status" """

    schema = {
                Optional('boot_loader_version'): str,
                Optional('build'): str,
                Optional('chassis_serial_number'): str,
                Optional('commit_pending'): str,
                Optional('configuration_template'): str,
                Optional('cpu_allocation'): {
                    Optional('control'): str, 
                    Optional('data'): str, 
                    Optional('total'): str
                    },
                Optional('cpu_reported_reboot'): str,
                Optional('cpu_states'): {
                    Optional('idle'): str, 
                    Optional('system'): str, 
                    Optional('user'): str
                    },
                Optional('current_time'): str,
                Optional('disk_usage'): {
                    Optional('avail'): str,
                    Optional('filesystem'): str,
                    Optional('mounted_on'): str,
                    Optional('size'): str,
                    Optional('use_pc'): str,
                    Optional('used'): str
                    },
                Optional('last_reboot'): str,
                Optional('load_average'): {
                    Optional('minute_1'): str, 
                    Optional('minute_15'): str, 
                    Optional('minute_5'): str
                    },
                Optional('memory_usage'): {
                    Optional('buffers'): str,
                    Optional('cache'): str,
                    Optional('free'): str,
                    Optional('total'): str,
                    Optional('used'): str
                    },
                Optional('model_name'): str,
                Optional('personality'): str,
                Optional('processes'): str,
                Optional('services'): str,
                Optional('system_fips_state'): str,
                Optional('system_logging_disk'): str,
                Optional('system_logging_host'): str,
                Optional('system_state'): str,
                Optional('system_uptime'): str,
                Optional('testbed_mode'): str,
                Optional('version'): str,
                Optional('vmanaged'): str
            }

# ===========================================
# Parser for 'show system status'
# ===========================================

class ShowSystemStatus(ShowSystemStatusSchema):
    """ Parser for "show system status" """

    cli_command = "show system status"

    def cli(self, output=None):
        parsed_dict = {}
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # Version: 99.99.999-4567
        # Build: 4567
        # Configuration template:  CLItemplate_srp_vedge
        # Chassis serial number:   None
        if out:
            linelist=[]
            for line in out.splitlines():
                line = line.strip()
                linelist.append(line)
                p1 = re.compile(r'^(?P<key>[\w/\.\s\-]+:) +(?P<value>[\d\w/\.\:\s\,\%\-]+)$')
                m1 = p1.match(line)
                if m1:
                    groups = m1.groupdict()
                    key = groups['key'].replace('-', '_').replace(' ','_').replace(':','').lower()
                    parsed_dict.update({key: (groups['value'])})
                p4 = re.compile(r'^System +logging +to +(?P<type>[\w/\s]+) +is +(?P<value>[\d\w/\s]+)$')
                m4 = p4.match(line)
                if m4:
                    groups = m4.groupdict()
                    parsed_dict.update({'system_logging_'+groups['type'].replace(' ',''): (groups['value'])})
                #CPU allocation:          4 total,   1 control,   3 data
                p5 = re.compile(r'^CPU +allocation: +(?P<total>[\d]+) +total, +(?P<control>[\d]+) +control, +(?P<data>[\d]+) +data$')
                m5 = p5.match(line)
                if m5:
                    groups = m5.groupdict()
                    parsed_dict.update({'cpu_allocation': (groups)})
                #CPU states:              1.25% user,   5.26% system,   93.48% idle
                p6 = re.compile(r'^CPU +states: +(?P<user>[\d\%\.]+) +user, +(?P<system>[\d\%\.]+) +system, +(?P<idle>[\d\%\.]+) +idle$')
                m6 = p6.match(line)
                if m6:
                    groups = m6.groupdict()
                    parsed_dict.update({'cpu_states': (groups)})
                #Load average:            1 minute: 3.20, 5 minutes: 3.13, 15 minutes: 3.10
                p7 = re.compile(r'^Load +average: +1 +minute: +(?P<minute_1>[\d\%\.]+), +5 +minutes: +(?P<minute_5>[\d\%\.]+), +15 +minutes: +(?P<minute_15>[\d\%\.]+)$')
                m7 = p7.match(line)
                if m7:
                    groups = m7.groupdict()
                    parsed_dict.update({'load_average': (groups)})
            #Memory usage:            1907024K total,    1462908K used,   444116K free
            #                          0K buffers,  0K cache
            for lines in range(len(linelist)):
                if 'Memory usage:' in linelist[lines]:
                    line = linelist[lines] + ' '+linelist[lines+1]
                    break   
            p2 = re.compile(r'Memory +usage: +(?P<total>[\d\w/\\]+) +total, +(?P<used>[\d\w/\\]+) +used, +(?P<free>[\d\w/\\]+) +free +(?P<buffers>[\d\w/\\]+) +buffers, +(?P<cache>[\d\w/\\]+) +cache$')
            m2 = p2.match(line)
            if m2:
                groups = m2.groupdict()
                parsed_dict.update({'memory_usage': (groups)})
            #Disk usage:              Filesystem      Size   Used  Avail   Use %  Mounted on
            #                         /dev/root       7615M  447M  6741M   6%   /
            for line in out.split('\n\n'):
                line = line.strip()
                p3 = re.compile(r'^Disk +usage: +Filesystem +Size +Used +Avail + Use +% +Mounted +on\n +(?P<filesystem>[\d\w/\%\.]+) +(?P<size>[\d\w]+) +(?P<used>[\d\w]+) +(?P<avail>[\d\w]+) +(?P<use_pc>[\d\w/\%\.]+) +(?P<mounted_on>[\d\w/\%\.]+)$')
                m3 = p3.match(line)
                if m3:
                    groups = m3.groupdict()
                    parsed_dict.update({'disk_usage': (groups)})
        return parsed_dict