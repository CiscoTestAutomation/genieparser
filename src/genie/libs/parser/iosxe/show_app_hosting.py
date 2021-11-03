''' show_app_hosting.py

IOSXE parsers for the following show commands:
    * show app-hosting list
    * show app-hosting infra
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

