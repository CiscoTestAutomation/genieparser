''' show_logging.py

NXOS parsers for the following show commands:
    * show logging logfile
    * show logging logfile | include {include}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ==============================================
# Schema for:
#   * 'show logging logfile'
#   * 'show logging logfile | include {include}'
# ==============================================
class ShowLoggingLogfileSchema(MetaParser):
    
    '''Schema for:
        * 'show logging logfile'
        * 'show logging logfile | include {include}'
    '''

    schema = {
        'logs': list,
        Optional('acl_names'): list,
        }


# ==============================================
# Parser for:
#   * 'show logging logfile'
#   * 'show logging logfile | include {include}'
# ==============================================
class ShowLoggingLogfile(ShowLoggingLogfileSchema):

    '''Schema for:
        * 'show logging logfile'
        * 'show logging logfile | include {include}'
    '''

    cli_command = ['show logging logfile | include {include}',
                   'show logging logfile',
                   ]

    def cli(self, include='', output=None):

        if output is None:
            # Build the command
            if include:
                cmd = self.cli_command[0].format(include=include)
            else:
                cmd = self.cli_command[1]
            # Execute the command
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        parsed_dict = {}
        log_lines = []
        acl_names = []

        # 2019 May 22 16:20:45 ha01-n7010-01 %ACLLOG-5-ACLLOG_FLOW_INTERVAL: Src IP: 172.30.10.100, Dst IP: 15.15.15.2, Src Port: 0, Dst Port: 0, Src Intf: Ethernet3/3, Protocol: "IP"(253), ACL Name: match-ef-acl, ACE Action: Permit, Appl Intf: Vlan10, Hit-count: 600
        # 2019 May 22 16:20:50 ha01-n7010-01 %ACLLOG-5-ACLLOG_FLOW_INTERVAL: Src IP: 172.30.10.100, Dst IP: 15.15.15.2, Src Port: 0, Dst Port: 0, Src Intf: Ethernet3/3, Protocol: "IP"(253), ACL Name: match-ef-acl, ACE Action: Permit, Appl Intf: Vlan10, Hit-count: 500
        p1 = re.compile(r'.*ACL +Name: +(?P<acl_name>(\S+)),.*')

        for line in out.splitlines():
            line = line.strip()

            # Add line to 'logs'
            if line and 'show logging logfile' not in line:
                log_lines.append(line)
                parsed_dict['logs'] = log_lines

            # ... ACL Name: match-ef-acl ...
            m = p1.match(line)
            if m:
                acl_name = m.groupdict()['acl_name']
                if acl_name not in acl_names:
                    acl_names.append(acl_name)
                    parsed_dict['acl_names'] = acl_names
                continue

        return parsed_dict

