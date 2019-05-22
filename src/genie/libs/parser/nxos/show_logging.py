''' show_logging.py

NXOS parsers for the following show commands:
    * show logging logfile | inc ACL
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ===========================================
# Schema for 'show logging logfile | inc ACL'
# ===========================================
class ShowLoggingACLSchema(MetaParser):
    
    '''Schema for:
        * 'show logging logfile | inc ACL'
    '''

    schema = {
        'acl_names': list,
        }


# ===========================================
# Parser for 'show logging logfile | inc ACL'
# ===========================================
class ShowLoggingACL(ShowLoggingACLSchema):

    '''Parser for:
        * 'show logging logfile | inc ACL'
    '''

    cli_command = ['show logging logfile | inc ACL']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        parsed_dict = {}
        acl_names = []

        # 2019 May 22 16:20:45 ha01-n7010-01 %ACLLOG-5-ACLLOG_FLOW_INTERVAL: Src IP: 172.30.10.100, Dst IP: 15.15.15.2, Src Port: 0, Dst Port: 0, Src Intf: Ethernet3/3, Protocol: "IP"(253), ACL Name: match-ef-acl, ACE Action: Permit, Appl Intf: Vlan10, Hit-count: 600
        # 2019 May 22 16:20:50 ha01-n7010-01 %ACLLOG-5-ACLLOG_FLOW_INTERVAL: Src IP: 172.30.10.100, Dst IP: 15.15.15.2, Src Port: 0, Dst Port: 0, Src Intf: Ethernet3/3, Protocol: "IP"(253), ACL Name: match-ef-acl, ACE Action: Permit, Appl Intf: Vlan10, Hit-count: 500
        p1 = re.compile(r'.*ACL +Name: +(?P<acl_name>(\S+)),.*')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                acl_name = m.groupdict()['acl_name']
                if acl_name not in acl_names:
                    acl_names.append(acl_name)
                    parsed_dict['acl_names'] = acl_names
                continue

        return parsed_dict

