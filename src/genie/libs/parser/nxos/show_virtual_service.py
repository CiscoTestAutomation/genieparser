"""show_virtual_service.py

NX-OS parsers for the following show commands:
    * show virtual-service global
    * show virtual-service list
    * show virtual-service detail
    * show virtual-service detail name <name>
    * show guestshell
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
                'info': {
                    'package_location': str,
                    'version' : str,
                    'description' : str,
                    'signing_key_type': str,
                },
                'resource_reservation': {
                    'disk_mb': int,
                    'memory_mb': int,
                    'cpu_percent': int,
                }
            }
        }
    }


# ============================================================================
# Parser for "show virtual-service detail [name <name>]" and "show guestshell"
# ============================================================================
class ShowVirtualServiceDetail(ShowVirtualServiceDetailSchema):
    """Parser for:
      * show virtual-service detail name <name>
      * show guestshell
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
        p3 = re.compile(r'^Path +: +(?P<path>.+)$')

        # Application
        #   Name              : GuestShell
        #   Installed version : 2.4(0.0)
        #   Description       : Cisco Systems Guest Shell
        p4 = re.compile(r'^Installed +version +: +(?P<version>.+)$')
        p5 = re.compile(r'^Description +: +(?P<description>.+)$')

        # Signing
        #   Key type          : Cisco release key
        #   Method            : SHA-1
        p6 = re.compile(r'^Key +type +: +(?P<key_type>.+)$')

        # Licensing
        #   Name              : None
        #   Version           : None
        # Resource reservation
        #   Disk                : 1000 MB
        #   Memory              : 500 MB
        #   CPU                 : 1% system CPU
        p7 = re.compile(r'^Disk +: +(?P<disk>\d+) +MB$')
        p8 = re.compile(r'^Memory +: +(?P<memory>\d+) +MB$')
        p9 = re.compile(r'^CPU +: +(?P<cpu>\d+)% system CPU')

        for line in output.splitlines():
            line = line.strip()

            match = p1.match(line)
            if match:
                service_dict = services_dict.setdefault(
                    'service', {}).setdefault(match.groupdict()['name'], {})
                continue

            match = p2.match(line)
            if match:
                service_dict['state'] = match.groupdict()['state'].lower()
                continue

            match = p3.match(line)
            if match:
                path = match.groupdict()['path']
                service_dict.setdefault('info', {})['package_location'] = path
                continue

            match = p4.match(line)
            if match:
                version = match.groupdict()['version']
                service_dict.setdefault('info', {})['version'] = version
                continue

            match = p5.match(line)
            if match:
                description = match.groupdict()['description']
                service_dict.setdefault('info', {})['description'] = description
                continue

            match = p6.match(line)
            if match:
                key_type = match.groupdict()['key_type']
                service_dict.setdefault('info',
                                        {})['signing_key_type'] = key_type
                continue

            match = p7.match(line)
            if match:
                disk = int(match.groupdict()['disk'])
                service_dict.setdefault('resource_reservation',
                                        {})['disk_mb'] = disk
                continue

            match = p8.match(line)
            if match:
                memory = int(match.groupdict()['memory'])
                service_dict.setdefault('resource_reservation',
                                        {})['memory_mb'] = memory
                continue

            match = p9.match(line)
            if match:
                cpu = int(match.groupdict()['cpu'])
                service_dict.setdefault('resource_reservation',
                                        {})['cpu_percent'] = cpu
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
        'info': {
            'package_location': str,
            'version' : str,
            'description' : str,
            'signing_key_type': str,
        },
        'resource_reservation': {
            'disk_mb': int,
            'memory_mb': int,
            'cpu_percent': int,
        }
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
