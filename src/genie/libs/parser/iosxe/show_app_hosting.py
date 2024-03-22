''' show_app_hosting.py

IOSXE parsers for the following show commands:
    * show app-hosting list
    * show app-hosting infra
    * show app-hosting resource
    * show app-hosting detail appid {appid}
'''
import re

# Metaparser
from genie.metaparser import MetaParser
import genie.parsergen as pg
from genie.metaparser.util.schemaengine import Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common

# ===========================================
# Schema for 'show app-hosting infra'
# ===========================================


class ShowApphostingInfraSchema(MetaParser):
    """ Schema for show app-hosting infra """
    schema = {
        'iox_version': str,
        'app_signature_verification': str,
        'internal_working_directory': str,
        'appge_port_number': {
            str: {
                'appge_interface_name': str,
                }
            }
         }


# ===========================================
# Parser for 'show app-hosting infra'
# ===========================================

class ShowApphostingInfra(ShowApphostingInfraSchema):
    ''' Parser for "show app-hosting infra"

    IOX version: 10.49.0.0
    App signature verification: disabled
    Internal working directory: /vol/usb1/iox

    Application Interface Mapping
    AppGigabitEthernet Port #  Interface Name                 Port Type            Bandwidth
               1               AppGigabitEthernet1/0/1        KR Port - Internal   1G


    CPU:
      Quota: 25(Percentage)
      Available: 25(Percentage)
      Quota: 7400(Units)
      Available: 7400(Units)
    '''

    cli_command = "show app-hosting infra"

    def cli(self, output=None):
        parsed_dict = {}

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # IOX version: 10.49.0.0
        p1 = re.compile(r"IOX version: (?P<iox_version>.*)$")

        # App signature verification: enabled
        p2 = re.compile(r"App signature verification: (?P<app_signature_verification>\w+)$")

        # Internal working directory: /vol/usb1/iox
        p3 = re.compile(r"Internal working directory: (?P<internal_working_directory>.*)$")

        p4 = re.compile(r'^\s*(?P<appge_port_number>[0-9])'
                        r'\s*(?P<appge_interface_name>\w+\/[0-9]\/[0-9])')

        if out:
            appge_dict = {}
            for line in out.splitlines():
                line_strip = line.strip()

                m = p1.match(line_strip)
                if m:
                    parsed_dict['iox_version'] = m.groupdict()['iox_version']

                m = p2.match(line_strip)
                if m:
                    parsed_dict['app_signature_verification'] = \
                        m.groupdict()['app_signature_verification']

                m = p3.match(line_strip)
                if m:
                    parsed_dict['internal_working_directory'] = \
                        m.groupdict()['internal_working_directory']

                '''
                1               AppGigabitEthernet3/0/1        KR Port - Internal   10G
                2               AppGigabitEthernet3/0/2        KR Port - Internal   10G
                '''

                m = p4.match(line_strip)
                if m:
                    appge_interface_dict = {}
                    appge_interface_dict['appge_interface_name'] = \
                        m.groupdict()['appge_interface_name']
                    appge_dict[m.groupdict()['appge_port_number']] = appge_interface_dict
            parsed_dict['appge_port_number'] = appge_dict
        return parsed_dict


# ===========================================
# Schema for 'show app-hosting list'
# ===========================================

class ShowApphostingListSchema(MetaParser):
    """ Schema for show app-hosting list """
    schema = {
        'app_id': {
            str: {
                'state': str,
                }
            }
         }


# ===========================================
# Parser for 'show app-hosting list'
# ===========================================
class ShowApphostingList(ShowApphostingListSchema):
    """ Parser for "show app-hosting list" """

    cli_command = "show app-hosting list"

    def cli(self, output=None):
        parsed_dict = {}
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # App id                                   State
        # ---------------------------------------------------------
        # utd                                      RUNNING
        if out:
            out = pg.oper_fill_tabular(device_output=out, header_fields=["App id", "State"],
                                       index=[0])
            return_dict = out.entries
            app_id = {}
            for keys in return_dict.keys():
                app_dict = {}
                app_dict['state'] = return_dict[keys]['State']
                app_id[keys] = app_dict
            parsed_dict['app_id'] = app_id
        return parsed_dict


# ===========================================
# Schema for 'show app-hosting resource'
# ===========================================
class ShowAppHostingResourceSchema(MetaParser):
    """
        Schema for show app-hosting resource
    """
    schema = {
        'cpu': {
            'quota': int,
            'available': int,
            'metric': str
        },
        'vcpu': {
            'count': int
        },
        'memory': {
            'quota': int,
            'available': int,
            'metric': str
        },
        'storage_space': {
            'total': int,
            'available': int,
            'metric': str
        }
    }


# ===========================================
# Parser for 'show app-hosting resource'
# ===========================================
class ShowAppHostingResource(ShowAppHostingResourceSchema):
    """
        Parser for show app-hosting resource
    """
    cli_command = 'show app-hosting resource'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # CPU:
        # VCPU:
        # Memory:
        # Storage space:
        p1 = re.compile(r'^(?P<resource_name>CPU|VCPU|Memory|Storage space):$')

        # Quota: 25(Percentage)
        # Available: 25(Percentage)
        # Count: 2
        # Quota: 2048(MB)
        # Available: 2048(MB)
        # Total: 3904(MB)
        # Available: 3485(MB)
        p2 = re.compile(r'^(?P<resource_type>Quota|Available|Count|Total)'
                        r':\s+(?P<resouce_value>\d+)(\((?P<metric>\w+)\))?$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # CPU:
            # VCPU:
            # Memory:
            # Storage space:
            m = p1.match(line)
            if m:
                resource_name = m.groupdict()['resource_name'].lower().replace(' ', '_')
                resource_dict = ret_dict.setdefault(resource_name, {})
                continue

            # Quota: 25(Percentage)
            # Available: 25(Percentage)
            # Count: 2
            # Quota: 2048(MB)
            # Available: 2048(MB)
            # Total: 3904(MB)
            # Available: 3485(MB)
            m = p2.match(line)
            if m:
                resources = m.groupdict()
                resource_dict[resources['resource_type'].lower()] = int(resources['resouce_value'])
                if resources['metric']:
                    resource_dict['metric'] = resources['metric']
                continue

        return ret_dict


# ===========================================
# Schema for 'show app-hosting detail'
# ===========================================
class ShowAppHostingDetailSchema(MetaParser):
    """
        Schema for show app-hosting detail
    """
    schema = {
        'application': {
            'type': str,
            'name': str,
            'version': str,
            Optional('desc'): str,
            'author': str,
            Optional('path'): str,
            'p_name': 'custom'
        },
        'resource_reservation': {
            'memory': str,
            'disk': str,
            'cpu': str,
            'cpu_p': str,
            'vcpu': int
        },
        'app_id': str,
        'owner': str,
        'state': str
    }


# ===========================================
# Parser for 'show app-hosting detail'
# ===========================================
class ShowAppHostingDetail(ShowAppHostingDetailSchema):
    """Parser for show app-hosting detail"""

    cli_command = "show app-hosting detail"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}

        # Process not enabled
        p0_rgx = re.compile(r'.*process for the command is not responding.*')

        # State                  : RUNNING
        p1_rgx = re.compile(r'State\s+:\s+(?P<state>(\w+))$')

        # Owner                  : iox
        p2_rgx = re.compile(r'Owner\s+:\s+(?P<owner>(\w+))$')

        # App id                   : Wireshark
        p3_rgx = re.compile(r'App\sid\s+:\s+(?P<app_id>(\w+))$')

        # Author                    : Cisco Systems, Inc
        p4_rgx = re.compile(r'Author\s+:\s+(?P<author>([\w\s,-]+))$')

        # Type                     : vm
        p5_rgx = re.compile(r'Type\s+:\s+(?P<type>(\w+))$')

        # Name                     : Wireshark
        p6_rgx = re.compile(r'Name\s+:\s+(?P<name>(\w+))$')

        # Version                    : 3.4
        # Version                    : 3.3.0
        p7_rgx = re.compile(r'Version\s+:\s+(?P<version>([\d.]+))$')

        # Activated Profile Name   : custom
        # Activated profile name   : custom
        p8_rgx = re.compile(r'Activated\s[Pp]rofile\s[Nn]ame\s+:\s+(?P<p_name>(\w+))$')

        # Description          : Cisco Systems Guest Shell XE for x86_64
        # Description              : Ubuntu based Wireshark
        p9_rgx = re.compile(r'Description\s+:\s+(?P<desc>([\w ]*))$')

        # Path                 : /guestshell/:guestshell.tar
        p10_rgx = re.compile(r'Path\s+:\s+(?P<path>([\/\w:.]+))$')

        # Memory                   : 1900 MB
        # Memory               : 256 GB
        p11_rgx = re.compile(r'Memory\s+:\s+(?P<memory>(\d+ [KMG]B))$')
        # Disk                 : 1 MB
        # Disk                 : 10 MB
        p12_rgx = re.compile(r'Disk\s+:\s+(?P<disk>(\d+ [KMG]B))$')

        # CPU                  : 800 units
        p13_rgx = re.compile(r'CPU\s+:\s+(?P<cpu>(\d+\s+units))$')

        # CPU-percent          : 100 %
        p14_rgx = re.compile(r'CPU-percent\s+:\s+(?P<cpu_p>(\d+\s+%))$')

        # VCPU                  : 8
        p15_rgx = re.compile(r'VCPU\s+:\s+(?P<vcpu>(\d+))$')

        for line in output.splitlines():
            line = line.strip()

            # app-hosting process not enabled
            m = re.match(p0_rgx, line)
            if m:
                ret_dict = {}
                return

            # State
            m = re.match(p1_rgx, line)
            if m:
                ret_dict.update({'state': m.groupdict()['state']})
                continue

            # Owner
            m = re.match(p2_rgx, line)
            if m:
                ret_dict.update({'owner': m.groupdict()['owner']})
                continue

            # App id
            m = re.match(p3_rgx, line)
            if m:
                ret_dict.update({'app_id': m.groupdict()['app_id']})
                continue

            app_dict = ret_dict.setdefault('application', {})
            # Author
            m = re.match(p4_rgx, line)
            if m:
                app_dict.update({'author': m.groupdict()['author']})
                continue
            # Type
            m = re.match(p5_rgx, line)
            if m:
                app_dict.update({'type': m.groupdict()['type']})
                continue
            # Name
            m = re.match(p6_rgx, line)
            if m:
                app_dict.update({'name': m.groupdict()['name']})
                continue
            # Version
            m = re.match(p7_rgx, line)
            if m:
                app_dict.update({'version': m.groupdict()['version']})
                continue
            # Activated profile name
            m = re.match(p8_rgx, line)
            if m:
                app_dict.update({'p_name': m.groupdict()['p_name']})
                continue
            # Description
            m = re.match(p9_rgx, line)
            if m:
                app_dict.update({'desc': m.groupdict()['desc']})
                continue
            # Path
            m = re.match(p10_rgx, line)
            if m:
                app_dict.update({'path': m.groupdict()['path']})
                continue

            res_dict = ret_dict.setdefault('resource_reservation', {})
            # Memory
            m = re.match(p11_rgx, line)
            if m:
                res_dict.update({'memory': m.groupdict()['memory']})
                continue
            # Disk
            m = re.match(p12_rgx, line)
            if m:
                res_dict.update({'disk': m.groupdict()['disk']})
                continue
            # CPU
            m = re.match(p13_rgx, line)
            if m:
                res_dict.update({'cpu': m.groupdict()['cpu']})
                continue
            # CPU-percent
            m = re.match(p14_rgx, line)
            if m:
                res_dict.update({'cpu_p': m.groupdict()['cpu_p']})
                continue
            # VCPU
            m = re.match(p15_rgx, line)
            if m:
                res_dict.update({'vcpu': int(m.groupdict()['vcpu'])})
                continue
        return ret_dict


# ===========================================
# Schema for 'show app-hosting detail appid {appid}'
# ===========================================
class ShowAppHostingDetailAppidSchema(MetaParser):
    """Schema for show app-hosting detail appid {appid}"""
    schema = {
        'app_id': str,
        'owner': str,
        'state': str,
        'application': {
            Any(): {
                'type': str,
                'version': str,
                Optional('description'): str,
                'author': str,
                'path': str,
                Optional('url_path'): str
            }
        },
        'activated_profile_name': str,
        'resource_reservation': {
            'memory': str,
            'disk': str,
            'cpu': int,
            'vcpu': int
        },
        'attached_devices': {
            Any(): {
                'type': str,
                'alias': str
            }
        },
        'network_interfaces': {
            Any(): {
                'mac_address': str,
                'network_name': str
            }
        },
        'application_health': {
            'status': str,
            Optional('last_probe_error'): str,
            Optional('last_probe_output'): str
        }
    }


# ===========================================
# Parser for 'show app-hosting detail appid {appid}'
# ===========================================
class ShowAppHostingDetailAppid(ShowAppHostingDetailAppidSchema):
    """Parser for show app-hosting detail appid {appid}"""

    cli_command = "show app-hosting detail appid {appid}"

    def cli(self, appid, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(appid=appid))

        # App id                 : thousandeyes_enterprise_agent
        p1 = re.compile(r'^App id\s+: (?P<app_id>.+)$')

        # Owner                  : iox
        p2 = re.compile(r'^Owner\s+: (?P<owner>.+)$')

        # State                  : RUNNING
        p3 = re.compile(r'^State\s+: (?P<state>.+)$')

        # Application
        p4 = re.compile(r'^Application$')

        # Type                 : docker
        p4_1 = re.compile(r'^Type\s+: (?P<type>.+)$')

        # Name                 : ThousandEyes Enterprise Agent
        p4_2 = re.compile(r'^Name\s+: (?P<application>.+)$')

        # Version              : 4.3.0
        p4_3 = re.compile(r'^Version\s+: (?P<version>.+)$')

        # Description          :
        p4_4 = re.compile(r'^Description\s+: (?P<description>.+)$')

        # Author               : ThousandEyes <support@thousandeyes.com>
        p4_5 = re.compile(r'^Author\s+: (?P<author>.+)$')

        # Path                 : flash:thousandeyes-enterprise-agent-4.3.0.cisco.tar
        p4_6 = re.compile(r'^Path\s+: (?P<path>.+)$')

        # URL Path             :
        p4_7 = re.compile(r'^URL Path\s+: (?P<url_path>.+)$')

        # Activated profile name : custom
        p5 = re.compile(r'^Activated profile name : (?P<activated_profile_name>.+)$')

        # Resource reservation
        p6 = re.compile(r'^Resource reservation$')

        # Memory               : 500 MB
        p6_1 = re.compile(r'^Memory\s+: (?P<memory>.+)$')

        # Disk                 : 1 MB
        p6_2 = re.compile(r'^Disk\s+: (?P<disk>.+)$')

        # CPU                  : 1850 units
        p6_3 = re.compile(r'^CPU\s+: (?P<cpu>\d+) units$')

        # VCPU                 : 1
        p6_4 = re.compile(r'^VCPU\s+: (?P<vcpu>\d+)$')

        # Attached devices
        p7 = re.compile(r'^Attached devices$')

        # Type              Name               Alias
        # ---------------------------------------------
        # serial/shell     iox_console_shell   serial0
        p7_1 = re.compile(r'^(?P<type>\w+\/\w+)\s+(?P<name>\S+)\s+(?P<alias>\w+)$')

        # Network interfaces
        p8 = re.compile(r'^Network interfaces$')

        # ---------------------------------------
        # eth0:
        p8_1 = re.compile(r'^(?P<network_interface>[\w\.\/]+):$')

        # MAC address         : 52:54:dd:d:38:3d
        p8_2 = re.compile(r'^MAC address\s+: (?P<mac_address>[a-f0-9\:]+)$')

        # Network name        : mgmt-bridge-v21
        p8_3 = re.compile(r'^Network name\s+: (?P<network_name>.+)$')

        # Application health information
        p9 = re.compile(r'^Application health information$')

        # Status               : 0
        p9_1 = re.compile(r'^Status\s+: (?P<status>\w+)$')

        # Last probe error     :
        p9_2 = re.compile(r'^Last probe error\s+: (?P<last_probe_error>.+)$')

        # Last probe output    :
        p9_3 = re.compile(r'^Last probe output\s+: (?P<last_probe_output>.+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # App id                 : thousandeyes_enterprise_agent
            m = p1.match(line)
            if m:
                ret_dict['app_id'] = m.groupdict()['app_id']
                continue

            # Owner                  : iox
            m = p2.match(line)
            if m:
                ret_dict['owner'] = m.groupdict()['owner']
                continue

            # State                  : RUNNING
            m = p3.match(line)
            if m:
                ret_dict['state'] = m.groupdict()['state']
                continue

            # Application
            m = p4.match(line)
            if m:
                application_dict = ret_dict.setdefault('application', {})
                continue

            # Type                 : docker
            m = p4_1.match(line)
            if m:
                app_type = m.groupdict()['type']
                continue

            # Name                 : ThousandEyes Enterprise Agent
            m = p4_2.match(line)
            if m:
                app_name_dict = application_dict.setdefault(
                    m.groupdict()['application'].lower().replace(' ', '_'), {}
                    )
                app_name_dict['type'] = app_type
                continue

            # Version              : 4.3.0
            m = p4_3.match(line)
            if m:
                app_name_dict['version'] = m.groupdict()['version']
                continue

            # Description          :
            m = p4_4.match(line)
            if m:
                app_name_dict['description'] = m.groupdict()['description']
                continue

            # Author               : ThousandEyes <support@thousandeyes.com>
            m = p4_5.match(line)
            if m:
                app_name_dict['author'] = m.groupdict()['author']
                continue

            # Path                 : flash:thousandeyes-enterprise-agent-4.3.0.cisco.tar
            m = p4_6.match(line)
            if m:
                app_name_dict['path'] = m.groupdict()['path']
                continue

            # URL Path             :
            m = p4_7.match(line)
            if m:
                app_name_dict['url_path'] = m.groupdict()['url_path']
                continue

            # Activated profile name : custom
            m = p5.match(line)
            if m:
                ret_dict['activated_profile_name'] = m.groupdict()['activated_profile_name']
                continue

            # Resource reservation
            m = p6.match(line)
            if m:
                resource_reservation_dict = ret_dict.setdefault('resource_reservation', {})
                continue

            # Memory               : 500 MB
            m = p6_1.match(line)
            if m:
                resource_reservation_dict['memory'] = m.groupdict()['memory']
                continue

            # Disk                 : 1 MB
            m = p6_2.match(line)
            if m:
                resource_reservation_dict['disk'] = m.groupdict()['disk']
                continue

            # CPU                  : 1850 units
            m = p6_3.match(line)
            if m:
                resource_reservation_dict['cpu'] = int(m.groupdict()['cpu'])
                continue

            # VCPU                 : 1
            m = p6_4.match(line)
            if m:
                resource_reservation_dict['vcpu'] = int(m.groupdict()['vcpu'])
                continue

            # Attached devices
            m = p7.match(line)
            if m:
                attached_devices_dict = ret_dict.setdefault('attached_devices', {})
                continue

            # Type              Name               Alias
            # ---------------------------------------------
            # serial/shell     iox_console_shell   serial0
            m = p7_1.match(line)
            if m:
                device_name_dict = attached_devices_dict.setdefault(
                    m.groupdict()['name'].lower().replace(' ', '_'), {}
                    )
                device_name_dict['type'] = m.groupdict()['type']
                device_name_dict['alias'] = m.groupdict()['alias']
                continue

            # Network interfaces
            m = p8.match(line)
            if m:
                network_dict = ret_dict.setdefault('network_interfaces', {})
                continue

            # ---------------------------------------
            # eth0:
            m = p8_1.match(line)
            if m:
                interface_dict = network_dict.setdefault(
                    Common.convert_intf_name(m.groupdict()['network_interface']), {}
                    )
                continue

            # MAC address         : 52:54:dd:d:38:3d
            m = p8_2.match(line)
            if m:
                interface_dict['mac_address'] = m.groupdict()['mac_address']
                continue

            # Network name        : mgmt-bridge-v21
            m = p8_3.match(line)
            if m:
                interface_dict['network_name'] = m.groupdict()['network_name']
                continue

            # Application health information
            m = p9.match(line)
            if m:
                application_health_dict = ret_dict.setdefault('application_health', {})
                continue

            # Status               : 0
            m = p9_1.match(line)
            if m:
                application_health_dict['status'] = m.groupdict()['status']
                continue

            # Last probe error     :
            m = p9_2.match(line)
            if m:
                application_health_dict['last_probe_error'] = m.groupdict()['last_probe_error']
                continue

            # Last probe output    :
            m = p9_3.match(line)
            if m:
                application_health_dict['last_probe_output'] = m.groupdict()['last_probe_output']
                continue

        return ret_dict
