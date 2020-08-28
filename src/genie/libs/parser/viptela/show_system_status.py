'''
* 'show system status'
'''
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import genie.parsergen as pg
import re


# ===========================================
# Schema for 'show system status'
# ===========================================


class ShowSystemStatusSchema(MetaParser):
    """ Schema for "show system status" """

    schema = {
                'boot_loader_version': str,
                'build': str,
                'chassis_serial_number': str,
                'commit_pending': str,
                'configuration_template': str,
                Optional('engineering_signed'): bool,
                Optional('controller_compatibility'): str,
                Optional('cpu_allocation'): {
                    Optional('control'): int, 
                    Optional('data'): int, 
                    Optional('total'): int
                    },
                'cpu_reported_reboot': str,
                'cpu_states': {
                    'idle': float, 
                    'system': float, 
                    'user': float
                    },
                'current_time': str,
                'disk_usage': {
                    'avail_mega': int,
                    'filesystem': str,
                    'mounted_on': str,
                    'size_mega': int,
                    'use_pc': int,
                    'used_mega': int
                    },
                'last_reboot': str,
                Optional('load_average'): {
                    Optional('minute_1'): float, 
                    Optional('minute_15'): float, 
                    Optional('minute_5'): float
                    },
                'memory_usage': {
                    'buffers_kilo': int,
                    'cache_kilo': int,
                    'free_kilo': int,
                    'total_kilo': int,
                    'used_kilo': int
                    },
                Optional('hypervisor_type'):str,
                Optional('cloud_hosted_instance'):str,
                'model_name': str,
                'personality': str,
                'processes': int,
                'services': str,
                'system_fips_state': str,
                'system_logging_disk': str,
                'system_logging_host': str,
                'system_state': str,
                'system_uptime': str,
                'testbed_mode': str,
                'version': str,
                'vmanaged': str
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
        if out:
            linelist=[]
            # Controller Compatibility: 20.3
            # Version: 99.99.999-4567
            # Build: 4567
            # System state:            GREEN. All daemons up
            # System FIPS state:       Enabled
            # Testbed mode:            Enabled
            # Hypervisor Type:         None
            # Cloud Hosted Instance:   false
            # Last reboot:             Initiated by user - activate 99.99.999-4567.
            # CPU-reported reboot:     Not Applicable
            # Boot loader version:     Not applicable
            # System uptime:           0 days 21 hrs 35 min 28 sec
            # Current time:            Thu Aug 06 02:49:25 PDT 2020
            # Processes:               250 total
            # Personality:             vedge
            # Model name:              vedge-cloud
            # Services:                None
            # vManaged:                true
            # Commit pending:          false
            # Configuration template:  CLItemplate_srp_vedge
            # Chassis serial number:   None
            p1 = re.compile(r'^(?P<key>[\w/\.\s\-]+:) +(?P<value>[\d\w/\.\:\s\,\%\-]+)$')
            
            # System logging to host  is disabled
            # System logging to disk is enabled
            p2 = re.compile(r'^System +logging +to +(?P<type>[\w/\s]+) +is +(?P<value>[\d\w/\s]+)$')
            
            #CPU allocation:          4 total,   1 control,   3 data
            p3 = re.compile(r'^CPU +allocation: +(?P<total>[\0-9]+) +total, +(?P<control>[\0-9]+) +control, +(?P<data>[\0-9]+) +data$')
            
            #CPU states:              1.25% user,   5.26% system,   93.48% idle
            p4 = re.compile(r'^CPU +states: +(?P<user>[\0-9\%\.]+) +user, +(?P<system>[\0-9\%\.]+) +system, +(?P<idle>[\0-9\%\.]+) +idle$')
            
            #Load average:            1 minute: 3.20, 5 minutes: 3.13, 15 minutes: 3.10
            p5 = re.compile(r'^Load +average: +1 +minute: +(?P<minute_1>[\0-9\%\.]+), +5 +minutes: +(?P<minute_5>[\0-9\%\.]+), +15 +minutes: +(?P<minute_15>[\0-9\%\.]+)$')

            #Engineering Signed       True
            p6 = re.compile(r'^Engineering +Signed +(?P<value>[\d\w/\.\:\s\,\%\-]+)$') 
            for line in out.splitlines():
                line = line.strip()
                linelist.append(line)
                m1 = p1.match(line)
                if m1:
                    groups = m1.groupdict()
                    key = groups['key'].replace('-', '_').replace(' ','_').replace(':','').lower()
                    if key =='processes':groups['value']=int(groups['value'].replace('total','')) 
                    parsed_dict.update({key: (groups['value'])})
                m2 = p2.match(line)
                if m2:
                    groups = m2.groupdict()
                    parsed_dict.update({'system_logging_'+groups['type'].replace(' ',''): (groups['value'])})
                m3 = p3.match(line)
                if m3:
                    groups = m3.groupdict()
                    for keys in groups:groups[keys] = int(groups[keys])
                    parsed_dict.update({'cpu_allocation': (groups)})
                m4 = p4.match(line)
                if m4:
                    groups = m4.groupdict()
                    for keys in groups:groups[keys] = float(groups[keys].replace('%',''))
                    parsed_dict.update({'cpu_states': (groups)})
                m5 = p5.match(line)
                if m5:
                    groups = m5.groupdict()
                    for keys in groups:groups[keys] = float(groups[keys])
                    parsed_dict.update({'load_average': (groups)})
                m6 = p6.match(line)
                if m6:
                    groups = m6.groupdict()
                    for keys in groups:groups[keys] = bool(groups[keys])
                    parsed_dict.update({'engineering_signed': (groups['value'])})
            for lines in range(len(linelist)):
                if 'Memory usage:' in linelist[lines]:
                    line = linelist[lines] + ' '+linelist[lines+1]
                    break   
            #Memory usage:            1907024K total,    1462908K used,   444116K free
            #                          0K buffers,  0K cache
            p7 = re.compile(r'Memory +usage: +(?P<total_kilo>[\0-9\w/\\]+) +total, +(?P<used_kilo>[\0-9\w/\\]+) +used, +(?P<free_kilo>[\0-9\w/\\]+) +free +(?P<buffers_kilo>[\0-9\w/\\]+) +buffers, +(?P<cache_kilo>[\0-9\w/\\]+) +cache$')
            m7 = p7.match(line)
            if m7:
                groups = m7.groupdict()
                for keys in groups:groups[keys] = int(groups[keys].replace('K',''))
                parsed_dict.update({'memory_usage': (groups)})
            for lines in range(len(linelist)):
                if 'Disk usage:' in linelist[lines]:
                    line = linelist[lines] + ' '+linelist[lines+1]
                    break
            #Disk usage:              Filesystem      Size   Used  Avail   Use %  Mounted on
            #                         /dev/root       7615M  447M  6741M   6%   /
            p8 = re.compile(r'^Disk +usage: +Filesystem +Size +Used +Avail + Use +% +Mounted +on +(?P<filesystem>[\d\w/\%\.]+) +(?P<size_mega>[\d\w]+) +(?P<used_mega>[\d\w]+) +(?P<avail_mega>[\d\w]+) +(?P<use_pc>[\d\w/\%\.]+) +(?P<mounted_on>[\d\w/\%\.]+)$')
            m8 = p8.match(line)
            if m8:
                  groups = m8.groupdict()
                  for keys in groups:
                        if keys == 'size_mega':groups[keys] = int(groups[keys].replace('M',''))
                        if keys == 'used_mega':groups[keys] = int(groups[keys].replace('M',''))
                        if keys =='avail_mega':groups[keys] = int(groups[keys].replace('M',''))
                        if keys =='use_pc':groups[keys] = int(groups[keys].replace('M','').replace('%',''))
                  parsed_dict.update({'disk_usage': (groups)})
        return parsed_dict