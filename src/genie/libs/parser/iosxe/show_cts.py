import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ======================
# Schema for:
#  * 'show cts rbacl.py'
# ======================
class ShowCtsRbacl.PySchema(MetaParser):
    """Schema for show cts rbacl.py."""

    schema = {
        "cts_rbacl": {
            "ip_ver_support": str,
            str: {
                "ip_protocol_version": str,
                "refcnt": int,
                "flag": str,
                "stale": "FALSE",
                int: {
                    "action": str,
                    "protocol": str,
                    "direction": str,
                    "port": int
                }
            }
        }
    }


# ======================
# Parser for:
#  * 'show cts rbacl.py'
# ======================
class ShowCtsRbacl.Py(ShowCtsRbacl.PySchema):
    """Parser for show cts rbacl.py"""

    cli_command = ['show cts rbacl.py']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        cts_rbacl_dict = {}

        ip_ver_capture = re.compile(r"^RBACL\s+IP\s+Version\s+Supported:\s(?P<ip_ver_support>.*$)")
        rbacl_capture = re.compile(r"^(?P<rbacl_key>.*)(?==)=\s+(?P<rbacl_value>.*$)")
        rbacl_ace_capture = re.compile(
            r"^(?P<action>(permit|deny))\s+(?P<protocol>\S+)(\s+(?P<direction>dst|src)\s+((?P<port_condition>)\S+)\s+(?P<port>\d+)|)")

        remove_lines = ('CTS RBACL Policy', '================', 'RBACL ACEs:')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)
        rbacl_name = ''
        rbacl_ace_index = 1
        for line in out:
            ip_ver_match = ip_ver_capture.match(line)
            if ip_ver_match:
                groups = ip_ver_match.groupdict()
                ip_ver_support = groups['ip_ver_support']
                if not cts_rbacl_dict.get('cts_rbacl', {}):
                    cts_rbacl_dict['cts_rbacl'] = {}
                cts_rbacl_dict['cts_rbacl']['ip_ver_support'] = ip_ver_support
                continue
            rbacl_match = rbacl_capture.match(line)
            if rbacl_match:
                groups = rbacl_match.groupdict()
                rbacl_key = groups['rbacl_key'].strip().lower().replace(' ', '_')
                rbacl_value = groups['rbacl_value']
                if rbacl_value.isdigit():
                    rbacl_value = int(rbacl_value)
                if not cts_rbacl_dict.get('cts_rbacl', {}):
                    cts_rbacl_dict['cts_rbacl'] = {}
                if rbacl_key == 'name':
                    rbacl_name = rbacl_value
                    cts_rbacl_dict['cts_rbacl'][rbacl_name] = {}
                    rbacl_ace_index = 1
                else:
                    cts_rbacl_dict['cts_rbacl'][rbacl_name].update({rbacl_key: rbacl_value})
                continue
            rbacl_ace_match = rbacl_ace_capture.match(line)
            if rbacl_ace_match:
                groups = rbacl_ace_match.groupdict()
                ace_group_dict = {}
                if groups['action']:
                    ace_group_dict.update({'action': groups['action']})
                if groups['protocol']:
                    ace_group_dict.update({'protocol': groups['protocol']})
                if groups['direction']:
                    ace_group_dict.update({'direction': groups['direction']})
                if groups['port_condition']:
                    ace_group_dict.update({'port_condition': groups['port_condition']})
                if groups['port']:
                    ace_group_dict.update({'port': int(groups['port'])})
                if not cts_rbacl_dict['cts_rbacl'][rbacl_name].get(rbacl_ace_index, {}):
                    cts_rbacl_dict['cts_rbacl'][rbacl_name][rbacl_ace_index] = ace_group_dict
                rbacl_ace_index = rbacl_ace_index + 1
                continue
        return cts_rbacl_dict