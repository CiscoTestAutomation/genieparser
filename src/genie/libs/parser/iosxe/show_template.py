'''show_template.py
IOSXE parsers for the following commands
    * show template
    * show template interface source built-in Original all
    * show template brief
'''

# python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie import parsergen
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, Default

# pyATS
# import parser utils
from genie.libs.parser.utils.common import Common


# ======================================================
# Parser for 'show template '
# ======================================================

class ShowTemplateSchema(MetaParser):
    """Schema for show template"""

    schema = {
        'templates': {
            Any(): {
                'template': str,
                'class': str,
                'type': str,
                Optional('bound'): list,
                Optional('nested_template'): str,
            },
        },
    }

class ShowTemplate(ShowTemplateSchema):
    """Parser for show template"""

    cli_command = 'show template'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # --------                                         -----      ----
        p1 = re.compile(r"-{3}")   

        # AP_INTERFACE_TEMPLATE                            owner      Built-in        
        p2 = re.compile(r"^(?P<template>\S+)\s+(?P<class>\w+)\s+(?P<type>\S+)$")

        #  BOUND: Twe1/0/1               Twe1/0/2               Twe1/0/3
        p3 = re.compile(r'^\sBOUND:\s+(?P<bound>(.|\n)*)$')

        # NESTED TEMPLATE:  Child
        p4 = re.compile(r'^\sNESTED TEMPLATE:\s+(?P<nested_template>\S+)$')

        ret_dict = {}
        temp_flag = False

        for line in output.splitlines():
            line = line.rstrip()
            
            match_obj = p1.match(line)
            if match_obj:
                temp_flag = True
                continue

            if temp_flag:
                m = p2.match(line)
                if m:
                    dict_val = m.groupdict()
                    templates = ret_dict.setdefault('templates', {})
                    template_dict = templates.setdefault(dict_val['template'], dict_val)
                    continue
                
                m = p3.match(line)
                if m:
                    template_dict.setdefault('bound', m.groupdict()['bound'].split())
                
                m = p4.match(line)
                if m:
                    template_dict.setdefault('nested_template', m.groupdict()['nested_template'])
        
        return ret_dict


class ShowTemplateInterfaceSourceBuiltInOriginalAllSchema(MetaParser):
    """Schema for show template interface source built-in Original all"""
    schema = {
        'template': {
            Any(): {
                'definition': list
            }
        }
    }


class ShowTemplateInterfaceSourceBuiltInOriginalAll(ShowTemplateInterfaceSourceBuiltInOriginalAllSchema):
    """Parser for show template interface source built-in Original all"""

    cli_command = 'show template interface source built-in Original all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Template Name:   IP_PHONE_INTERFACE_TEMPLATE  
        p1 = re.compile(r'^Template Name:\s+(?P<template>\w+)$')

        # Template Definition: 
        p2 = re.compile(r'^Template Definition:$')

        # switchport mode access 
        # switchport block unicast
        # spanning-tree portfast
        # switchport port-security
        # spanning-tree bpduguard enable 
        # service-policy input AutoConf-4.0-Trust-Dscp-Input-Policy
        # service-policy output AutoConf-4.0-Output-Policy
        p3 = re.compile(r'^(?P<definition>.+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            # Template Name:   IP_PHONE_INTERFACE_TEMPLATE
            match = p1.match(line)
            if match:
                tmp_dict = ret_dict.setdefault('template', {}).setdefault(match.groupdict()['template'], {})
                continue

            # Template Definition:
            match = p2.match(line)
            if match:
                def_list = tmp_dict.setdefault('definition', [])
                continue

            # switchport mode access 
            # switchport block unicast
            # spanning-tree portfast
            # switchport port-security
            # spanning-tree bpduguard enable 
            # service-policy input AutoConf-4.0-Trust-Dscp-Input-Policy
            # service-policy output AutoConf-4.0-Output-Policy
            # exit
            match = p3.match(line)
            if match and match.groupdict()['definition'] != 'exit':
                def_list.append(match.groupdict()['definition'])
                continue
        
        return ret_dict


class ShowTemplateBriefSchema(MetaParser):
    """Schema for show template brief"""

    schema = {
        'interface_template': {
            Any(): {
                'source': str,
                'bound_to_interface': str
            }
        },
        'service_template': {
            Any(): {
                'source': str,
                'bound_to_session': str
            }
        }
    }


class ShowTemplateBrief(ShowTemplateBriefSchema):
    """Parser for show template brief"""

    cli_command = 'show template brief'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Interface Templates
        # Service Templates
        p1 = re.compile(r'^(?P<template_type>(Interface|Service))\s+Templates$')

        ret_dict = dict()
        res = parsergen.oper_fill_tabular(device_output=output,
            device_os='iosxe',
            table_terminal_pattern=r"^\n",
            header_fields=
            [ "Template-Name",
                "Source",
                "Bound-to-Interface" ],
            label_fields=
            [ "interface_template",
                "source",
                "bound_to_interface" ],
            index=[0])

        # Building the schema out of the parsergen output
        if res.entries:
            for tmp, values in res.entries.items():
                del values['interface_template']
                if values["source"] and values["bound_to_interface"]:
                    ret_dict.setdefault('interface_template', {}).update({tmp: values})
        
        res = parsergen.oper_fill_tabular(device_output=output,
            device_os='iosxe',
            table_terminal_pattern=r"^\n",
            header_fields=
            [ "Template-Name",
                "Source",
                "Bound-To-Session" ],
            label_fields=
            [ "service_template",
                "source",
                "bound_to_session" ],
            index=[0])

        # Building the schema out of the parsergen output      
        if res.entries:
            for tmp, values in res.entries.items():
                del values['service_template']
                ret_dict.setdefault('service_template', {}).update({tmp: values})

        return ret_dict


class ShowTemplateTemplateSchema(MetaParser):
    """Schema for show template {template}"""

    schema = {
        'template': str,
        'class': str,
        'type': str,
        Optional('bound'): list,
    }

class ShowTemplateTemplate(ShowTemplateTemplateSchema):
    """Parser for show template {template}"""

    cli_command = 'show template {template}'

    def cli(self, template, output=None):
        if output is None:
            cmd = self.cli_command.format(template=template)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Template                                         Class      Type
        # --------                                         -----      ----
        # test                                             owner      User
        res = parsergen.oper_fill_tabular(device_output=output,
            device_os='iosxe',
            table_terminal_pattern=r"^\n",
            header_fields=
            [ "Template",
                "Class",
                "Type" ],
            label_fields=
            [ "template",
                "class",
                "type" ],
            index=[0])

        # Building the schema out of the parsergen output
        if res.entries and template in res.entries:
            for key, value in res.entries[template].items():
                ret_dict.setdefault(key, value)

        #  Regex everything before "BOUND:", then grab everything after
        #  BOUND: Twe1/0/1               Twe1/0/2               Twe1/0/3
        #         Twe1/0/4               Twe1/0/5
        p1 = re.compile(r'^(.|\n)*(?P<bound>BOUND:)\s+(?P<targets>(.|\n)*)$')

        match = p1.match(output)
        if match:
            ret_dict.setdefault('bound', [])
            groups = match.groupdict()
            targets = [target.strip() for target in groups['targets'].split()]
            ret_dict['bound'] = targets

        return ret_dict


class ShowTemplateInterfaceBindingTargetSchema(MetaParser):
    """Schema for show template brief"""

    schema = {
        'interface': {
            Any(): {
                Optional('method'): {
                    Any(): {
                        'source': str,
                        'template_name': str
                    }
                }
            }
        }
    }


class ShowTemplateInterfaceBindingTarget(ShowTemplateInterfaceBindingTargetSchema):
    """Parser for show template interface binding target {interface}"""

    cli_command = 'show template interface binding target {interface}'
    
    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))
        
        # Interface: Gi1/0/1
        p1 = re.compile(r'^Interface:\s+(?P<interface>\S+)$')

        ret_dict = dict()
        
        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                continue

        res = parsergen.oper_fill_tabular(device_output=output,
            device_os='iosxe',
            table_terminal_pattern=r"^\n",
            header_fields=
            [ "Method",
                "Source",
                "Template-Name" ],
            label_fields=
            [ "method",
                "source",
                "template_name" ],
            index=[0])

        # Building the schema out of the parsergen output
        if res.entries:
            for tmp, values in res.entries.items():
                del values['method']
                if values["source"] and values["template_name"]:
                    int_dict.setdefault('method', {}).update({tmp: values})

        return ret_dict
