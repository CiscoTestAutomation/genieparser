from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# =======================================
# Schema for 'show cloudexpress application'
# =======================================

class ShowCloudexpressApplicationSchema(MetaParser):

    """ schema for 'show cloudexpress applications' """

    schema = {
        "index": {
            Any(): {
                "vpn": int,
                "application": str,
                "exit_type": str,
                "gw_sys_ip": str,
                "interface": str,
                "latency": int,
                "local_color": str,
                "loss": int,
                "remote_color": str,
                }
            }
        }

class ShowCloudexpressApplication(ShowCloudexpressApplicationSchema):
    """Parser for 'show cloudexpress application' on Viptela vEdge
    appliances - CLI"""
    cli_command = 'show cloudexpress applications'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        index = 0
        #1    salesforce               gateway  172.16.255.14  -          103      1     lte    lte
        #1    google_apps              gateway  172.16.255.14  -          47       0     lte    lte
        p1 = re.compile(r'^(?P<vpn>\S+)\s\s+(?P<application>\S+)\s\s+(?P<exit_type>\S+)\s\s+(?P<gw_sys_ip>\S+)'
                        '\s\s+(?P<interface>\S+)\s\s+(?P<latency>\S+)\s\s+(?P<loss>\S+)\s\s+(?P<local_color>\S+)'
                        '\s\s+(?P<remote_color>\S+)')

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# =======================================
# Schema for 'show cloudexpress application'
# =======================================

class ShowCloudexpressApplicationSchema(MetaParser):

    """ schema for 'show cloudexpress applications' """

    schema = {
        "index": {
            Any(): {
                "vpn": int,
                "application": str,
                "exit_type": str,
                "gw_sys_ip": str,
                "interface": str,
                "latency": int,
                "local_color": str,
                "loss": int,
                "remote_color": str,
                }
            }
        }

class ShowCloudexpressApplication(ShowCloudexpressApplicationSchema):
    """Parser for 'show cloudexpress application' on Viptela vEdge
    appliances - CLI"""
    cli_command = 'show cloudexpress applications'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        index = 0
        #1    salesforce               gateway  172.16.255.14  -          103      1     lte    lte
        #1    google_apps              gateway  172.16.255.14  -          47       0     lte    lte
        p1 = re.compile(r'^(?P<vpn>\S+)\s\s+(?P<application>\S+)\s\s+(?P<exit_type>\S+)\s\s+(?P<gw_sys_ip>\S+)'
                        '\s\s+(?P<interface>\S+)\s\s+(?P<latency>\S+)\s\s+(?P<loss>\S+)\s\s+(?P<local_color>\S+)'
                        '\s\s+(?P<remote_color>\S+)')

        for line in out.splitlines():
            line = line.strip()
            
            #1    salesforce               gateway  172.16.255.14  -          103      1     lte    lte
            #1    google_apps              gateway  172.16.255.14  -          47       0     lte    lte
            m = p1.match(line)
            if m:
                group = m.groupdict()
                #vpn = group['vpn']
                vpn_dict = result_dict.setdefault('index', {}).setdefault(index, {})
                vpn_dict.update({'vpn': int(group['vpn'])})
                vpn_dict.update({'application': group['application']})
                vpn_dict.update({'exit_type': group['exit_type']})
                vpn_dict.update({'gw_sys_ip': group['gw_sys_ip']})
                vpn_dict.update({'interface': group['interface']})
                vpn_dict.update({'latency': int(group['latency'])})
                vpn_dict.update({'loss': int(group['loss'])})
                vpn_dict.update({'local_color': group['local_color']})
                vpn_dict.update({'remote_color': group['remote_color']})
                index += 1
                continue

        return result_dict