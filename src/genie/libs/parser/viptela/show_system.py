'''
* 'show system status'
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


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
            Optional('total'): int,
            Optional('control'): int,
            Optional('data'): int
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
        Optional('vmanage_storage_usage'): {
            Optional('filesystem'): str,
            Optional('size_mega'): int,
            Optional('used_mega'): int,
            Optional('avail_mega'): int,
            Optional('use_pc'): int,
            Optional('mounted_on'): str
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
        Optional('device_role'): str,
        Optional('testbed_mode'): str,
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
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # System logging to host  is disabled
        # System logging to disk is enabled
        p1 = re.compile(r'^System\s+logging\s+to\s+(?P<type>\w+)\s+is\s+(?P<value>enabled|disabled)$')

        # CPU allocation:          4 total,   1 control,   3 data
        # CPU allocation:          16 total
        p2 = re.compile(r'^CPU\s+allocation:\s+(?P<total>\d+)\s+total(,\s+(?P<control>\d+)\s+control)?(,\s+(?P<data>\d+)\s+data)?$')

        # CPU states:              1.25% user,   5.26% system,   93.48% idle
        p3 = re.compile(r'^CPU\s+states:\s+(?P<user>[\d\.]+)\%\s+user,\s+(?P<system>[\d\.]+)\%\s+system,\s+(?P<idle>[\d\.]+)\%\s+idle$')

        # Load average:            1 minute: 3.20, 5 minutes: 3.13, 15 minutes: 3.10
        p4 = re.compile(r'^Load\s+average:\s+1\s+minute:\s+(?P<minute_1>[\d\.]+),\s+5\s+minutes:\s+(?P<minute_5>[\d\.]+),\s+15\s+minutes:\s+(?P<minute_15>[\d\.]+)$')

        # Engineering Signed       True
        p5 = re.compile(r'^Engineering +Signed +(?P<value>True|False)$')

        # Memory usage:            1907024K total,    1462908K used,   444116K free
        p6 = re.compile(r'^Memory\s+usage:\s+(?P<total_kilo>\d+)K\s+total,\s+(?P<used_kilo>\d+)K\s+used,\s+(?P<free_kilo>\d+)K\s+free$')

        # 0K buffers,  0K cache
        p7 = re.compile(r'^(?P<buffers_kilo>\d+)K\s+buffers,\s+(?P<cache_kilo>\d+)K\s+cache$')

        # Disk usage:              Filesystem      Size   Used  Avail   Use %  Mounted on
        # vManage storage usage:   Filesystem      Size   Used  Avail   Use%   Mounted on
        p8 = re.compile(r'^(?P<usage_dict>.+usage):\s+Filesystem\s+Size\s+Used\s+Avail\s+Use\s*%\s+Mounted\s+on$')

        # /dev/root       7615M  447M  6741M   6%   /
        # /dev/disk/by-label/fs-bootflash       11039M  1240M  9219M   12%   /bootflash
        # /dev/bootflash1       28748M  2031M  25257M   7%   /bootflash
        p9 = re.compile(r'^(?P<filesystem>.+\S)\s+(?P<size_mega>\d+)M\s+(?P<used_mega>\d+)M\s+(?P<avail_mega>\d+)M\s+(?P<use_pc>\d+)\%\s+(?P<mounted_on>.+)$')

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
        p10 = re.compile(r'^(?P<key>.*):\s+(?P<value>.*)$')


        for line in output.splitlines():
            line = line.strip()

            # System logging to host is disabled
            # System logging to disk is enabled
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                parsed_dict['system_logging_' + group['type']] = group['value']
                continue

            # CPU allocation:          4 total,   1 control,   3 data
            # CPU allocation:          16 total
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                group = {key: int(group[key]) for key in group if group[key]}
                parsed_dict.update({'cpu_allocation': group})
                continue

            # CPU states:              1.25% user,   5.26% system,   93.48% idle
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                for keys in group:
                    group[keys] = float(group[keys])
                parsed_dict.update({'cpu_states': group})
                continue

            # Load average:            1 minute: 3.20, 5 minutes: 3.13, 15 minutes: 3.10
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                for keys in group:
                    group[keys] = float(group[keys])
                parsed_dict.update({'load_average': group})
                continue

            # Engineering Signed       True
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                group = bool(group['value'])
                parsed_dict.update({'engineering_signed': group})
                continue

            # Memory usage:            1907024K total,    1462908K used,   444116K free
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                parsed_dict.update({'memory_usage': {
                    key:int(group[key]) for key in group
                }})
                continue

            # 0K buffers,  0K cache
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                parsed_dict['memory_usage'].update({
                    key:int(group[key]) for key in group
                })
                continue

            # Disk usage:              Filesystem      Size   Used  Avail   Use %  Mounted on
            # vManage storage usage:   Filesystem      Size  Used  Avail  Use%  Mounted on
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                usage_dict_name = group['usage_dict'].replace(' ', '_').lower()
                usage_dict = parsed_dict.setdefault(usage_dict_name, {})
                continue

            # /dev/sda        503966M  6162M  472203M   1%   /opt/data
            # /dev/bootflash1       28748M  2031M  25257M   7%   /bootflash
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                usage_dict.update({'filesystem': group.pop('filesystem')})
                usage_dict.update({'mounted_on': group.pop('mounted_on')})
                usage_dict.update({
                    key: int(group[key]) for key in group
                })
                continue

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
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                key = group['key'].replace('-', '_').replace(' ','_').replace(':','').lower()
                if key == 'processes':
                    group['value'] = int(group['value'].replace('total',''))
                parsed_dict.update({key: (group['value'])})
                continue

        return parsed_dict
