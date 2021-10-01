'''show_template_binding.py
IOSXE parsers for the following commands

    * 'show template binding target {interface}'

'''
# python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any

# pyATS
# import parser utils
from genie.libs.parser.utils.common import Common

class ShowTemplateBindingSchema(MetaParser):
    """Schema for show template binding"""
    schema = {
        Any(): {
            Optional('interface_templates'): {
                Any(): {
                    'source': str,
                    'method': str,
                },
            },
            Optional('service_templates'): {
                Any(): {
                    'source': str,
                    'mac': str,
                },
            },
        }
    }

class ShowTemplateBindingTarget(ShowTemplateBindingSchema):
    """parser for:
        show template binding target"""

    cli_command = 'show template binding target {interface}'

    def cli(self, interface=None, output=None):
        '''Module that parsers the output'''

        if not output:
            # get output from device
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        #Interface: Gi1/0/12
        p1 = re.compile(r'^Interface:\s+(?P<Interface>[\w/\-.]+)')

                # Method              Source            Template-Name
        # ------              ------            -------------
        # dynamic             User              cts_dot1x
        # static              User              port-config
        p2 = re.compile(
            r"^(?P<method>(static|dynamic))\s+"
            r"(?P<source>\w+)\s+"
            r"(?P<interface_template_name>[\w_\-.]+)"
        )
        # Template-Name                                    Source            Bound-To-MAc
        # -------------                                    ------            ----------------
        # DefaultCriticalAuthVlan_SRV_TEMPLATE             User               68-3B-78-7A-2C-90
        # DefaultCriticalVoice_SRV_TEMPLATE                User               68-3B-78-7A-2C-90
        p3 = re.compile(
            r"^(?P<service_template_name>[\w_]+)\s+"
            r"(?P<source>[\w\-]+)\s+"
            r"(?P<mac>[A-F0-9\-]+)"
        )

        result_dict = {}
        for line in out.splitlines():
            line = line.strip()
            
            m = p1.match(line)

            if m:
                group_dict_1 = m.groupdict()
                Interface = group_dict_1.pop('Interface')
                converted_interface = Common.convert_intf_name(Interface)
                continue

            m = p2.match(line)

            if m:
                group_dict_2 = m.groupdict()
                method = group_dict_2.pop('interface_template_name')
                method_dict = result_dict.setdefault(converted_interface, {}).\
                setdefault('interface_templates', {}).setdefault(method, {})
                method_dict.update({k: v.lower() for k, v in group_dict_2.items()})
                continue

            m = p3.match(line)

            if m:
                group_dict_3 = m.groupdict()
                if (len(group_dict_3['mac'])) > 12:
                    mac_address = group_dict_3.pop('service_template_name')
                    mac_dict = result_dict.setdefault(converted_interface, {}).\
                    setdefault('service_templates', {}).setdefault(mac_address, {})
                    mac_dict.update({k: v.lower() for k, v in group_dict_3.items()})
                continue

        return result_dict
