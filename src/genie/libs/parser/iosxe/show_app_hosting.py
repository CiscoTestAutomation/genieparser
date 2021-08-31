''' show_app_hosting.py

IOSXE parsers for the following show commands:
    * show app-hosting list
    * show app-hosting infra
    * show app-hosting detail appid meraki
'''

# Metaparser
from genie.metaparser import MetaParser
import genie.parsergen as pg
import re
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
                
                m = p1.match(line)
                if m:
                    parsed_dict['iox_version'] = m.groupdict()['iox_version']

                m = p2.match(line)
                if m:
                    parsed_dict['app_signature_verification'] = m.groupdict()['app_signature_verification']

                m = p3.match(line)
                if m:
                    parsed_dict['internal_working_directory'] = m.groupdict()['internal_working_directory']
                    
                '''
                1               AppGigabitEthernet3/0/1        KR Port - Internal   10G
                2               AppGigabitEthernet3/0/2        KR Port - Internal   10G            
                '''
       
                m = p4.match(line)
                if m:                
                    appge_interface_dict = {}
                    appge_interface_dict['appge_interface_name'] = m.groupdict()['appge_interface_name']
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
            out = pg.oper_fill_tabular(device_output=out,
                                    header_fields=["App id", "State"],
                                    index=[0])
            return_dict = out.entries
            app_id ={}
            for keys in return_dict.keys() :
                app_dict={}
                app_dict['state'] = return_dict[keys]['State']
                app_id[keys] = app_dict
            parsed_dict['app_id'] = app_id
        return parsed_dict
   
# ===========================================
# schema for 'show app-hosting detail'
# ===========================================   
class ShowAppHostingDetailAppIdMerakiSchema(MetaParser):
    """Schema for 
        * show app-hosting detail appid meraki | i version
    """
    schema = {
        'app_id' : str ,
        'owner' : str,
        'state' : str,
        'application' : {
            'type' : str,
            'name' : str,
            'version' : str,
            Optional('description') : str, 
            Optional('author') : str,
            Optional('path'): str,
            Optional('url_path') : str, 
            'activated_profile_name' : str,
        },
        'resource_reservation' : {
            'memory' : str,
            'disk' : str,
            'cpu' : str,
            'cpu_percent' : str,
            'vcpu' : int,
        }, 
        Optional('platform_resource_profiles') : {
            Any():{
                'cpu_unit' : str,
                'memory_mb': str,
                'disk_mb': str,
            },
        },
        'attached_devices' : {
            Any() : {
                'name' : str,
                'alias': str,
            },     
        },
        'network_interfaces' : {
            Any() : {
            'mac_address' : str,
            'ipv6_address' : str,
            'network_name' : str, 
            },
        },
        'docker' : {
            'run_time_information': {
                Optional('command'): str,
                'entry_point' : str,
                Optional('run_options_in_use') : str, 
                Optional('package_run_options') : str,
            },
            'application_health_information':{
                'status' : int,
                Optional('last_probe_error'): str,
                'last_probe_output' : str,
            },
        },
    }
# ===========================================
# parser for 'show app-hosting detail'
# ===========================================   
class ShowAppHostingDetailAppIdMeraki(ShowAppHostingDetailAppIdMerakiSchema):
    """Parser for 
        * show app-hosting detail appid meraki
    """

    cli_command = ['show app-hosting detail appid meraki | i version']

    def cli(self,output=None):
       
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #App id : meraki
        p1 = re.compile(r"App +id +: +(?P<app_id>\w+)$")

        #Owner : iox
        p2 = re.compile(r"Owner +: +(?P<owner>\w+)$")

        #State : RUNNING
        p3 = re.compile(r"State +: +(?P<state>\w+)$")

        # Application
        p4 = re.compile(r"^Application")

        # Type : docker
        p5 = re.compile(r"Type +: +(?P<type>\w+)$")

        # Name : cat9k-app
        p6 = re.compile(r"Name +: +(?P<name>[\w\-]+)$")

        # Version : T-202106031655-G5c6da678-L0b29c1a9M-clouisa-creditor
        p7 = re.compile(r"Version +: +(?P<version>[\w\-]+)$")

        # Description :
        p8 = re.compile(r"Description +: +(?P<description>\w+)$")   

        # Author : 
        p9 = re.compile(r"Author +: +(?P<author>\w+)$")  

        # Path : 
        p10 = re.compile(r"Path +: +(?P<path>\w+)$")

        # URL Path : 
        p11 =  re.compile(r"URL_Path +: +(?P<url_path>\w+)$")       

        # Activated profile name : custom
        p12 = re.compile(r"Activated +profile +name +: +(?P<activated_profile_name>\w+)$")

        # Resource reservation
        p13 = re.compile(r"^Resource reservation")

        # Memory : 512 MB
        p14 =  re.compile(r"Memory +: +(?P<memory>[\w\s]+)$")

        # Disk : 2 MB
        p15 =  re.compile(r"Disk +: +(?P<disk>[\w\s]+)$")

        # CPU : 500 units
        p16 =  re.compile(r"CPU +: +(?P<cpu>[\w\s]+)$")

        # CPU-percent : 7 %
        p17 =  re.compile(r"CPU-percent +: +(?P<cpu_percent>[\d\s%]+)$")

        # VCPU : 1
        p18 =  re.compile(r"VCPU +: +(?P<vcpu>\d+)$")

        #Profile Name CPU(unit) Memory(MB) Disk(MB)
        p19 = re.compile(r'^(?P<profile_name>\w+) '
                    r'(?P<cpu_unit>\d+) '
                    r'(?P<memory_mb>\d+) '
                    r'(?P<disk_mb>\d+)$')

        #serial/shell iox_console_shell serial0 
        p20 = re.compile(r'^(?P<type>\w+\/\w+) '
                r'(?P<name>[\w\_]+) '
                r'(?P<alias>\w+)$')

        # eth2:
        p21 = re.compile(r"^eth\d") 

        # MAC address : 52:54:dd:0c:8e:82
        p22 = re.compile(r"MAC address +: +(?P<mac_address>(([a-fA-F\d]{2}:){5}[a-fA-F\d]{2}))$")

        # IPv6 address : ::
        p23=re.compile(r"IPv6 address +: +(?P<ipv6_address>[a-fA-F\d\:]+)$")

        # Network name : mgmt-bridge100
        p24 = re.compile(r"Network name +: +(?P<network_name>[\w/-]+)$")

        # Docker
        p25 = re.compile(r"^Docker$")

        # Run-time information
        p26 = re.compile(r"^Run-time information$")

        # Command : 
        p27 = re.compile(r"Command +: +(?P<command>\w+)$")

        # Entry-point : /sbin/init
        p28 = re.compile(r"Entry-point +: +(?P<entry_point>[\/\w]+)$")

        # Run options in use : 
        p29 = re.compile(r"Run +options +in +use +: +(?P<run_options_in_use>\w+)$")

        # Package run options :
        p30 = re.compile(r"package +run +options +: +(?P<package_run_options>\w+)$")

        # Application health information
        p31 = re.compile(r"^Application health information$")

        # Status : 0
        p32 = re.compile(r"Status +: +(?P<status>\d+)$")

        # Last probe error : 
        p33 = re.compile(r"Last +probe +error +: +(?P<last_probe_error>\w+)$")

        # Last probe output : []
        p34 = re.compile(r"Last +probe +output +: +(?P<last_probe_output>\[\])$")


        for line in out.splitlines():

            line = line.strip()

            #App id : meraki
            m = p1.match(line)
            if m:
                ret_dict['app_id'] = m.groupdict()['app_id']

            #Owner : iox
            m = p2.match(line)
            if m:
                ret_dict['owner'] = m.groupdict()['owner']

            #State : RUNNING
            m = p3.match(line)
            if m:
                ret_dict['state'] = m.groupdict()['state']

            # Application
            m = p4.match(line)
            if m:
                ret_dict.setdefault('application', {})

            # Type : docker
            m = p5.match(line)
            if m:
                ret_dict['application']['type'] = m.groupdict()['type']

            # Name : cat9k-app
            m = p6.match(line)
            if m:
                ret_dict['application']['name'] = m.groupdict()['name']

            # Version : T-202106031655-G5c6da678-L0b29c1a9M-clouisa-creditor
            m = p7.match(line)
            if m:
                ret_dict['application']['version'] = m.groupdict()['version']

            # Description :
            m = p8.match(line)
            if m:
                ret_dict['application']['description'] = m.groupdict()['description']

            # Author : 
            m = p9.match(line)
            if m:
                ret_dict['application']['author'] = m.groupdict()['author']

            # Path :
            m = p10.match(line)
            if m:
                ret_dict['application']['path'] = m.groupdict()['path']

            # URL Path :
            m = p11.match(line)
            if m:
                ret_dict['application']['url_path'] = m.groupdict()['url_path']

            # Activated profile name : custom
            m = p12.match(line)
            if m:
                ret_dict['application']['activated_profile_name'] = m.groupdict()['activated_profile_name']

            # Resource reservation
            m = p13.match(line)
            if m:
                ret_dict.setdefault('resource_reservation', {})

            # Memory : 512 MB
            m = p14.match(line)
            if m:
                ret_dict['resource_reservation']['memory'] = m.groupdict()['memory']

            # Disk : 2 MB
            m = p15.match(line)
            if m:
                ret_dict['resource_reservation']['disk'] = m.groupdict()['disk']

            # CPU : 500 units
            m = p16.match(line)
            if m:
                ret_dict['resource_reservation']['cpu'] = m.groupdict()['cpu']

            # CPU-percent : 7 %
            m = p17.match(line)
            if m:
                ret_dict['resource_reservation']['cpu_percent'] = m.groupdict()['cpu_percent']

            # VCPU : 1
            m = p18.match(line)
            if m:
                ret_dict['resource_reservation']['vcpu'] = int(m.groupdict()['vcpu'])

            #Profile Name CPU(unit) Memory(MB) Disk(MB)
            m = p19.match(line)
            if m:
                ret_dict.setdefault('platform_resource_profiles', {})
                group = m.groupdict()
                profile_name = group.pop('profile_name')
                stack_dict1 = ['platform_resource_profiles']
                stack_dict1.setdefault(profile_name, {})
                stack_dict2 = ret_dict['platform_resource_profiles'][profile_name]
                stack_dict2.update({k:int(v) for k, v in group.items()})

            #serial/shell iox_console_shell serial0
            m = p20.match(line)
            if m:
                ret_dict.setdefault('attached_devices', {})
                group = m.groupdict()
                type_name = group.pop('type')
                stack_dict3 = ret_dict['attached_devices']
                stack_dict3.setdefault(type_name, {})
                stack_dict4 = ret_dict['attached_devices'][type_name]
                stack_dict4.update({k:v for k, v in group.items()})

            # eth2:
            m = p21.match(line)
            if m:
                ret_dict.setdefault('network_interfaces', {})
                interface = m.group()
                stack_dict5 = ret_dict['network_interfaces']
                stack_dict5.setdefault(interface, {})

            # MAC address : 52:54:dd:0c:8e:82
            m = p22.match(line)
            if m:
                ret_dict['network_interfaces'][interface]['mac_address'] = m.groupdict()['mac_address']

            # IPv6 address : ::
            m = p23.match(line)
            if m:
                ret_dict['network_interfaces'][interface]['ipv6_address'] = m.groupdict()['ipv6_address']

            # Network name : mgmt-bridge100
            m = p24.match(line)
            if m:
                ret_dict['network_interfaces'][interface]['network_name'] = m.groupdict()['network_name']

            # Docker
            m = p25.match(line)
            if m:
                ret_dict.setdefault('docker', {})
                stack_dict5 = ret_dict['docker']

            # Run-time information
            m = p26.match(line)
            if m:
                stack_dict5.setdefault('run_time_information', {})

            # Command : 
            m = p27.match(line)
            if m:
                ret_dict['docker']['run_time_information']['command'] = m.groupdict()['command']

            # Entry-point : /sbin/init
            m = p28.match(line)
            if m:
                ret_dict['docker']['run_time_information']['entry_point'] = m.groupdict()['entry_point']

            # Run options in use : 
            m = p29.match(line)
            if m:
                ret_dict['docker']['run_time_information']['run_options_in_use'] = m.groupdict()['run_options_in_use']

            # Package run options :
            m = p30.match(line)
            if m:
                ret_dict['docker']['run_time_information']['package_run_options'] = m.groupdict()['package_run_options']

            # Application health information
            m = p31.match(line)
            if m:
                stack_dict5.setdefault('application_health_information', {})

            # Status : 0
            m = p32.match(line)
            if m:
                ret_dict['docker']['application_health_information']['status'] = int(m.groupdict()['status'])

            # Last probe error :
            m = p33.match(line)
            if m:
                ret_dict['docker']['application_health_information']['last_probe_error'] = m.groupdict()['last_probe_error']

            # Last probe output : []
            m = p34.match(line)
            if m:
                ret_dict['docker']['application_health_information']['last_probe_output'] = m.groupdict()['last_probe_output']

        return ret_dict
