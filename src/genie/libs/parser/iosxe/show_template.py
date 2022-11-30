'''show_template.py
IOSXE parsers for the following commands
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

        