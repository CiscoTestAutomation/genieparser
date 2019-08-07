"""show_virtual_service.py

NX-OS parsers for the following show commands:
    * show virtual-service global
    * show virtual-service list
    * show virtual-service core
    * show virtual-service core name <name>
    * show virtual-service detail
    * show virtual-service detail name <name>
    * show guestshell
    * show virtual-service utilization name <name>
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ========================================
# Schema for "show virtual-service global"
# ========================================

class ShowVirtualServiceGlobalSchema(MetaParser):
    """Schema for "show virtual-service global"."""

    schema = {
        'version': str,
        'virtual_services': {
            'installed': int,
            'activated': int,
        },
        'machine_types': {
            'supported': list,
            'disabled': list,
        },
        'resource_limits': {
            'cpus_per_service': int,
            'cpu': {
                'quota': int,
                'committed': int,
                'available': int,
            },
            'memory': {
                'quota': int,
                'committed': int,
                'available': int,
            },
            'bootflash': {
                'quota': int,
                'committed': int,
                'available': int,
            },
        },
    }


# ========================================
# Parser for "show virtual-service global"
# ========================================
class ShowVirtualServiceGlobal(ShowVirtualServiceGlobalSchema):
    """Parser for "show virtual-service global"."""

    cli_command = "show virtual-service global"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        global_dict = {}

        # Virtual Service Global State and Virtualization Limits:
        #
        # Infrastructure version : 1.10
        p1 = re.compile(r'^Infrastructure +version +: +(?P<version>[0-9.]+)$')

        # Total virtual services installed : 1
        # Total virtual services activated : 1
        p2 = re.compile(r'^Total +virtual +services +'
                        r'(?P<state>\S+) +: +(?P<count>\d+)$')

        # Machine types supported   : LXC
        # Machine types disabled    : KVM, CHROOT
        p3 = re.compile(r'^Machine +types +'
                        r'(?P<state>\S+) +: +(?P<kinds>.+)$')

        # Maximum VCPUs per virtual service : 1
        p4 = re.compile(r'^Maximum +VCPUs +per +virtual +service +: +'
                        r'(?P<count>\d+)$')

        # Resource virtualization limits:
        # Name                        Quota    Committed    Available
        # -------------------------------------------------------------------
        # system CPU (%)                 20            1           19
        # memory (MB)                  3840          500         3340
        # bootflash (MB)               8192         1000         7192
        p5 = re.compile(
            r'^(?P<kind>system +CPU +\(%\)|memory +\(MB\)|bootflash +\(MB\)) +'
            r'(?P<quota>\d+) +(?P<committed>\d+) +(?P<available>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            match = p1.match(line)
            if match:
                group = match.groupdict()
                version = group['version']

                global_dict['version'] = version
                continue

            match = p2.match(line)
            if match:
                group = match.groupdict()
                state = group['state']
                count = int(group['count'])

                if 'virtual_services' not in global_dict:
                    global_dict['virtual_services'] = {}

                global_dict['virtual_services'][state] = count
                continue

            match = p3.match(line)
            if match:
                group = match.groupdict()
                state = group['state']
                kinds = group['kinds'].split(", ")

                if 'machine_types' not in global_dict:
                    global_dict['machine_types'] = {}

                global_dict['machine_types'][state] = kinds
                continue

            match = p4.match(line)
            if match:
                group = match.groupdict()
                count = int(group['count'])

                if 'resource_limits' not in global_dict:
                    global_dict['resource_limits'] = {}

                global_dict['resource_limits']['cpus_per_service'] = count
                continue

            match = p5.match(line)
            if match:
                group = match.groupdict()
                kind = group['kind'].lower()
                if 'cpu' in kind:
                    kind = 'cpu'
                elif 'memory' in kind:
                    kind = 'memory'
                elif 'bootflash' in kind:
                    kind = 'bootflash'
                quota = int(group['quota'])
                committed = int(group['committed'])
                available = int(group['available'])

                if 'resource_limits' not in global_dict:
                    global_dict['resource_limits'] = {}

                global_dict['resource_limits'][kind] = {
                    'quota': quota,
                    'committed': committed,
                    'available': available,
                }
                continue

        return global_dict


# ======================================
# Schema for "show virtual-service list"
# ======================================
class ShowVirtualServiceListSchema(MetaParser):
    """Schema for "show virtual-service list"."""

    schema = {
        'service': {
            Any(): {
                'status': str,
                Optional('package'): str,
            },
        },
    }


# ======================================
# Parser for "show virtual-service list"
# ======================================
class ShowVirtualServiceList(ShowVirtualServiceListSchema):
    """Parser for "show virtual-service list"."""

    cli_command = "show virtual-service list"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        services_dict = {}

        # Virtual Service List:
        #
        # Name                    Status             Package Name
        # ----------------------------------------------------------------------
        # guestshell+             Activated          guestshell.ova
        # lxc4                    Not Installed      Not Available
        # sc_sanity_03            Installed          ft_mv_no_onep.ova
        # lxc_upgrade             Activate Failed    c63lxc_no_onep.ova

        p1 = re.compile(r'^(?P<name>(\S+))\s+'
                        '(?P<status>(\S+(?: \S+)?))\s+'
                        '(?P<package>(\S+(?: \S+)?))$')

        for line in output.splitlines():
            line = line.strip()

            match = p1.match(line)
            if match:
                group = match.groupdict()
                name = group['name']
                status = group['status'].lower()
                package = group['package']

                # Avoid false positives matching the output headers:
                if name == "Virtual" and status == "service":
                    continue
                if name == "Name" and status == "status":
                    continue

                service_dict = (services_dict
                                .setdefault('service', {})
                                .setdefault(name, {}))
                service_dict['status'] = status
                if package != "Not Available":
                    service_dict['package'] = package
                continue

        return services_dict

# ====================================================
# Schema for "show virtual-service core [name <name>]"
# ====================================================
class ShowVirtualServiceCoreSchema(MetaParser):
    """Schema for:
      * show virtual-service core
      * show virtual-service core name <name>
    """

    schema = {
        'cores': {
            Any(): {
                'virtual_service': str,
                'process_name': str,
                'pid': int,
                'date': str,
            }
        }
    }


# ====================================================
# Parser for "show virtual-service core [name <name>]"
# ====================================================
class ShowVirtualServiceCore(ShowVirtualServiceCoreSchema):
    """Parser for:
      * show virtual-service core
      * show virtual-service core name <name>
    """

    cli_command = ["show virtual-service core",
                   "show virtual-service core name {name}"]

    def cli(self, name="", output=None):
        if output is None:
            if name:
                cmd = self.cli_command[1].format(name=name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        cores_dict = {}

        # Virtual-Service  Process-name  PID       Date(Year-Month-Day Time)
        # ---------------  ------------  --------  -------------------------
        # guestshell+      sleep         266       2019-05-30 19:53:28
        p1 = re.compile(
            r'^(?P<vs>\S+)\s+(?P<proc>\S+)\s+(?P<pid>\d+)\s+(?P<date>.+)$')

        for line in output.splitlines():
            line = line.strip()

            match = p1.match(line)
            if match:
                g = match.groupdict()
                cd = cores_dict.setdefault('cores', {})
                cd[len(cd) + 1] = {
                    'virtual_service': g['vs'],
                    'process_name': g['proc'],
                    'pid': int(g['pid']),
                    'date': g['date'].strip(),
                }
                continue

        return cores_dict


# ======================================================
# Schema for "show virtual-service detail [name <name>]"
# ======================================================
class ShowVirtualServiceDetailSchema(MetaParser):
    """Schema for:
      * show virtual-service detail
      * show virtual-service detail name <name>
    """

    schema = {
        'service': {
            Any(): {
                'state': str,
                'package_information': {
                    'name': str,
                    'path': str,
                    'application': {
                        'name': str,
                        'version': str,
                        'description': str,
                    },
                    'signing': {
                        'key_type': str,
                        'method': str,
                    },
                    'licensing': {
                        'name': str,
                        'version': str,
                    },
                },
                'resource_reservation': {
                    'disk_mb': int,
                    'memory_mb': int,
                    'cpu_percent': int,
                },
                Optional('attached_devices'): {
                    Any(): {
                        'type': str,
                        Optional('name'): str,
                        Optional('alias'): str,
                    },
                },
            }
        }
    }


# ============================================================================
# Parser for "show virtual-service detail [name <name>]" and "show guestshell"
# ============================================================================
class ShowVirtualServiceDetail(ShowVirtualServiceDetailSchema):
    """Parser for:
      * show virtual-service detail
      * show virtual-service detail name <name>
      * show guestshell (by way of subclass ShowGuestshell)
    """

    cli_command = ["show virtual-service detail",
                   "show virtual-service detail name {name}"]

    def cli(self, name="", output=None):
        if output is None:
            if name:
                cmd = self.cli_command[1].format(name=name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        services_dict = {}

        # Virtual service guestshell+ detail
        p1 = re.compile(r'^Virtual +service +(?P<name>\S+) +detail$')

        # State                 : Activated
        p2 = re.compile(r'^State +: +(?P<state>.+)$')

        # Package information
        #   Name                : guestshell.ova
        #   Path                : /isanboot/bin/guestshell.ova
        p3 = re.compile(r'^Package information$')
        p3_1 = re.compile(r'^Name +: +(?P<name>.+)$')
        p3_2 = re.compile(r'^Path +: +(?P<path>.+)$')

        # Application
        #   Name              : GuestShell
        #   Installed version : 2.4(0.0)
        #   Description       : Cisco Systems Guest Shell
        p4 = re.compile(r'^Application$')
        p4_1 = re.compile(r'^Name +: +(?P<name>.+)$')
        p4_2 = re.compile(r'^Installed +version +: +(?P<version>.+)$')
        p4_3 = re.compile(r'^Description +: +(?P<description>.+)$')

        # Signing
        #   Key type          : Cisco release key
        #   Method            : SHA-1
        p5 = re.compile(r'^Signing')
        p5_1 = re.compile(r'^Key +type +: +(?P<key_type>.+)$')
        p5_2 = re.compile(r'^Method +: +(?P<method>.+)$')

        # Licensing
        #   Name              : None
        #   Version           : None
        p6 = re.compile(r'^Licensing')
        p6_1 = re.compile(r'^Name +: +(?P<name>.+)$')
        p6_2 = re.compile(r'^Version +: +(?P<version>.+)$')

        # Resource reservation
        #   Disk                : 1000 MB
        #   Memory              : 500 MB
        #   CPU                 : 1% system CPU
        p7 = re.compile(r'^Resource reservation$')
        p7_1 = re.compile(r'^Disk +: +(?P<disk>\d+) +MB$')
        p7_2 = re.compile(r'^Memory +: +(?P<memory>\d+) +MB$')
        p7_3 = re.compile(r'^CPU +: +(?P<cpu>\d+)% system CPU')

        # Attached devices
        #   Type              Name        Alias
        #   ---------------------------------------------
        #   Disk              _rootfs
        #   Disk              /cisco/cor
        #   Serial/shell
        #   Serial/aux
        #   Serial/Syslog                 serial2
        #   Serial/Trace                  serial3
        p8 = re.compile(r'^Attached devices$')
        p8_1 = re.compile(r'^Type +Name +Alias$')
        # It appears that any given entry never has both name and alias
        p8_2 = re.compile(
            r'^(?P<type>.{1,17})(?: (?P<name>\S+)| {13}(?P<alias>\S+))?$')

        service_dict = None
        info_dict = None
        app_dict = None
        signing_dict = None
        licensing_dict = None
        res_dict = None
        device_dict = None

        for line in output.splitlines():
            line = line.strip()

            match = p1.match(line)
            if match:
                service_dict = services_dict.setdefault(
                    'service', {}).setdefault(match.groupdict()['name'], {})
                info_dict = None
                app_dict = None
                signing_dict = None
                licensing_dict = None
                res_dict = None
                device_list = None
                continue

            match = p2.match(line)
            if match:
                service_dict['state'] = match.groupdict()['state'].lower()
                continue

            match = p3.match(line)
            if match:
                info_dict = service_dict.setdefault('package_information', {})
                continue

            if info_dict is not None and app_dict is None:
                match = p3_1.match(line)
                if match:
                    info_dict['name'] = match.groupdict()['name']
                    continue

                match = p3_2.match(line)
                if match:
                    info_dict['path'] = match.groupdict()['path']
                    continue

            match = p4.match(line)
            if match:
                app_dict = info_dict.setdefault('application', {})
                continue

            if app_dict is not None and signing_dict is None:
                match = p4_1.match(line)
                if match:
                    app_dict['name'] = match.groupdict()['name']
                    continue

                match = p4_2.match(line)
                if match:
                    app_dict['version'] = match.groupdict()['version']
                    continue

                match = p4_3.match(line)
                if match:
                    app_dict['description'] = match.groupdict()['description']
                    continue

            match = p5.match(line)
            if match:
                signing_dict = info_dict.setdefault('signing', {})
                continue

            if signing_dict is not None and licensing_dict is None:
                match = p5_1.match(line)
                if match:
                    signing_dict['key_type'] = match.groupdict()['key_type']
                    continue

                match = p5_2.match(line)
                if match:
                    signing_dict['method'] = match.groupdict()['method']
                    continue

            match = p6.match(line)
            if match:
                licensing_dict = info_dict.setdefault('licensing', {})
                continue

            if licensing_dict is not None and res_dict is None:
                match = p6_1.match(line)
                if match:
                    licensing_dict['name'] = match.groupdict()['name']
                    continue

                match = p6_2.match(line)
                if match:
                    licensing_dict['version'] = match.groupdict()['version']
                    continue

            match = p7.match(line)
            if match:
                res_dict = service_dict.setdefault('resource_reservation', {})
                continue

            if res_dict is not None and device_dict is None:
                match = p7_1.match(line)
                if match:
                    res_dict['disk_mb'] = int(match.groupdict()['disk'])
                    continue

                match = p7_2.match(line)
                if match:
                    res_dict['memory_mb'] = int(match.groupdict()['memory'])
                    continue

                match = p7_3.match(line)
                if match:
                    res_dict['cpu_percent'] = int(match.groupdict()['cpu'])
                    continue

            match = p8.match(line)
            if match:
                device_dict = service_dict.setdefault('attached_devices', {})
                continue

            if device_dict is not None:
                match = p8_1.match(line)
                if match:
                    continue

                match = p8_2.match(line)
                if match:
                    gd = match.groupdict()
                    entry = {'type': gd['type'].strip()}
                    if gd.get('name') and gd['name'].strip():
                        entry['name'] = gd['name'].strip()
                    if gd.get('alias') and gd['alias'].strip():
                        entry['alias'] = gd['alias'].strip()
                    device_dict[len(device_dict) + 1] = entry
                    continue

        return services_dict


# ======================================================
# Schema for "show guestshell"
# ======================================================
class ShowGuestshellSchema(MetaParser):
    """Schema for "show guestshell".

    This is the same as ShowVirtualServiceDetailSchema, minus the redundant
    `["service"]["guestshell+"]` enclosing container.
    """

    schema = {
        'state': str,
        'package_information': {
            'name': str,
            'path': str,
            'application': {
                'name': str,
                'version': str,
                'description': str,
            },
            'signing': {
                'key_type': str,
                'method': str,
            },
            'licensing': {
                'name': str,
                'version': str,
            },
        },
        'resource_reservation': {
            'disk_mb': int,
            'memory_mb': int,
            'cpu_percent': int,
        },
        Optional('attached_devices'): {
            Any(): {
                'type': str,
                Optional('name'): str,
                Optional('alias'): str,
            },
        },
    }


# ============================================================================
# Parser for "show guestshell"
# ============================================================================
class ShowGuestshell(ShowGuestshellSchema, ShowVirtualServiceDetail):
    """Parser for "show guestshell"."""

    cli_command = "show guestshell"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        services_dict = super().cli(output=output)
        return services_dict.get('service', {}).get('guestshell+', {})


# =========================================================
# Schema for "show virtual-service utilization name <name>"
# =========================================================

class ShowVirtualServiceUtilizationSchema(MetaParser):
    """Schema for "show virtual-service utilization name <name>"."""

    schema = {
        'cpu': {
            'requested_percent': int,
            'actual_percent': int,
            'state_abbrev': str,
            'state': str,
        },
        'memory': {
            'allocation_kb': int,
            'used_kb': int,
        },
        'storage': {
            Any(): {
                'capacity_kb': int,
                'used_kb': int,
                'available_kb': int,
                'used_percent': int,
            },
        },
    }


# =========================================================
# Parser for "show virtual-service utilization name <name>"
# =========================================================

class ShowVirtualServiceUtilization(ShowVirtualServiceUtilizationSchema):
    """Parser for "show virtual-service utilization name <name>"."""

    cli_command = "show virtual-service utilization name {name}"

    def cli(self, name, output=None):
        if output is None:
            cmd = self.cli_command.format(name=name)
            output = self.device.execute(cmd)

        util_dict = {}

        # Virtual-Service Utilization:
        #
        # CPU Utilization:
        #   Requested Application Utilization:  1 %
        p1 = re.compile(
            r'^Requested\s+Application\s+Utilization:\s+(?P<pct>\d+)\s*%$')
        #   Actual Application Utilization:  0 % (30 second average)
        p2 = re.compile(
            r'^Actual\s+Application\s+Utilization:\s+(?P<pct>\d+)\s*%\s+'
            r'\(30\s+second\s+average\)$')
        #   CPU State: R : Running
        p3 = re.compile(
            r'^CPU\s+State:\s+(?P<abbrev>\S+)\s*:\s*(?P<state>\S+)$')
        #
        # Memory Utilization:
        #   Memory Allocation: 262144 KB
        p4 = re.compile(r'^Memory\s+Allocation:\s+(?P<kb>\d+)\s+KB$')
        #   Memory Used:       13400 KB
        p5 = re.compile(r'^Memory\s+Used:\s+(?P<kb>\d+)\s+KB$')
        #
        # Storage Utilization:
        #   Name: _rootfs, Alias:
        p6 = re.compile(r'^Name:\s+(?P<name>\S+), Alias:$')
        #     Capacity(1K blocks):  243823      Used(1K blocks): 161690
        p7 = re.compile(r'^Capacity\(1K\s+blocks\):\s+(?P<capacity>\d+)\s+'
                        r'Used\(1K\s+blocks\):\s+(?P<used>\d+)$')
        #     Available(1K blocks): 77537       Usage: 68 %
        p8 = re.compile(r'^Available\(1K\s+blocks\):\s+(?P<available>\d+)\s+'
                        r'Usage:\s+(?P<usage_pct>\d+)\s*%$')

        storage_name = None

        for line in output.splitlines():
            line = line.strip()

            #   Requested Application Utilization:  1 %
            match = p1.match(line)
            if match:
                util_dict.setdefault('cpu', {})['requested_percent'] = int(match.groupdict()['pct'])
                continue

            #   Actual Application Utilization:  0 % (30 second average)
            match = p2.match(line)
            if match:
                util_dict.setdefault('cpu', {})['actual_percent'] = int(match.groupdict()['pct'])
                continue

            #   CPU State: R : Running
            match = p3.match(line)
            if match:
                util_dict.setdefault('cpu', {})['state_abbrev'] = match.groupdict()['abbrev']
                util_dict['cpu']['state'] = match.groupdict()['state']
                continue

            #   Memory Allocation: 262144 KB
            match = p4.match(line)
            if match:
                util_dict.setdefault('memory', {})['allocation_kb'] = int(match.groupdict()['kb'])
                continue

            #   Memory Used:       13400 KB
            match = p5.match(line)
            if match:
                util_dict.setdefault('memory', {})['used_kb'] = int(match.groupdict()['kb'])
                continue

            #   Name: _rootfs, Alias:
            match = p6.match(line)
            if match:
                storage_name = match.groupdict()['name']
                util_dict.setdefault('storage', {})[storage_name] = {}
                continue

            if storage_name:
                #     Capacity(1K blocks):  243823      Used(1K blocks): 161690
                match = p7.match(line)
                if match:
                    util_dict['storage'][storage_name]['capacity_kb'] = int(match.groupdict()['capacity'])
                    util_dict['storage'][storage_name]['used_kb'] = int(match.groupdict()['used'])
                    continue

                #     Available(1K blocks): 77537       Usage: 68 %
                match = p8.match(line)
                if match:
                    util_dict['storage'][storage_name]['available_kb'] = int(match.groupdict()['available'])
                    util_dict['storage'][storage_name]['used_percent'] = int(match.groupdict()['usage_pct'])
                    continue

        return util_dict
