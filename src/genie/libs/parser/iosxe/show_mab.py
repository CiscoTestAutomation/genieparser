''' show_mab.py

IOSXE parsers for the following show commands:
    * show mab all details
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or


# ====================================================
#  Schema for show mab all details
# ====================================================
class ShowMabAllDetailsSchema(MetaParser):
    schema = {
        'interfaces': {
            Any(): {
                'mac_auth_bypass': str,
                'client_mac':{
                    Any(): {
                        Optional('session_id'): str,
                        Optional('mab_sm_state'): str,
                        Optional('authen_status'): str,
                    },
                },
            },
        }
    }


# ====================================================
#  Parser for show mab all details
# ====================================================
class ShowMabAllDetails(ShowMabAllDetailsSchema):
    """
    Parser for show mab all details
    """
    cli_command = 'show mab all details'
    
    def cli(self, output = None):

        cmd = 'show mab all details'

        # MAB details for GigabitEthernet2/0/2
        p1 = re.compile(r'(^MAB\s+details\s+for)\s*(.*)')
        # Mac-Auth-Bypass = Enabled
        p2 = re.compile(r'(^Mac-Auth-Bypass)\s*=\s*(?P<mac_auth_bypass>.*)')
        # MAB Client List
        p3 = re.compile(r'(^MAB\s+Client\s+List)\s*')
        
        # My Client MAC = 0000.0001.0003
        # My Session ID = 000000000000000C82FA130E
        # My Authen Status = SUCCESS
        p4 = re.compile(r'(^My)\s+(\w+\s+\w+)\s*=\s*(.*)')
        # My MAB SM state = TERMINATE
        p5 = re.compile(r'(^My\s*MAB\s*SM\s*state)\s*=\s*(?P<mab_sm_state>.*)')

        ret_dict = {}
        interface_dict = {}
        mac_dict = {}
        client_dict = {}

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        for line in out.splitlines():
            line = line.strip()

            # MAB details for GigabitEthernet2/0/2
            res = p1.match(line)
            if res:
                interface_dict = ret_dict.setdefault('interfaces', {}).setdefault(res.group(2), {})
                continue
            
            # Mac-Auth-Bypass = Enabled
            res = p2.match(line)
            if res:
                interface_dict.update(res.groupdict())
                continue
            
            # MAB Client List
            res = p3.match(line)
            if res:
                mac_dict = interface_dict.setdefault('client_mac', {})

            # My Client MAC = 0000.0001.0003
            # My Session ID = 000000000000000C82FA130E
            # My Authen Status = SUCCESS
            res = p4.match(line)
            if res:
                key_string = (re.sub(r'\s+', '_', res.group(2))).lower()
                if key_string == 'client_mac':
                    client_dict = mac_dict.setdefault(res.group(3), {})
                else:
                    client_dict.update({key_string: res.group(3)})

            # My MAB SM state = TERMINATE
            res = p5.match(line)
            if res:
                client_dict.update(res.groupdict())

        return ret_dict

# ====================================================
#  Schema for show mab all summary
# ====================================================
class ShowMabAllSummarySchema(MetaParser):
    ''' Schema for:
        * 'show mab all summary'
    '''

    schema = {
        'interfaces': {
            Any(): {
                'mac': {
                    Any(): {                
                        'auth_status': str
                    },
                },
            },
        },
    }


# ===========================
# Parser for:
#   * 'show mab all summary'
# ===========================
class ShowMabAllSummary(ShowMabAllSummarySchema):
    ''' Parser for:
        * 'show mab all summary'
     '''

    cli_command = ['show mab all summary']

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Init vars
        ret_dict = {}

        # Gi1/0/5         0005.0000.0001  SUCCESS
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<mac>\S+) +(?P<auth_status>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Gi1/0/5         0005.0000.0001  SUCCESS
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                mac = m.groupdict()['mac']
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                mac_dict = intf_dict.setdefault('mac', {}).setdefault(mac, {})
                mac_dict['auth_status'] = str(m.groupdict()['auth_status'])
                continue

        return ret_dict
