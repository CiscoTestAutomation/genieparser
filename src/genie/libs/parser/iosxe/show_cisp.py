''' show_device_sensor.py

IOSXE parsers for the following show commands:
    * show cisp summary
    * show interface {intf}
'''

# Python

# parser utils
from genie.libs.parser.utils.common import Common
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (And, Any, Default, Optional,
                                                Or, Schema, Use)
# import parser utils
from genie.libs.parser.utils.common import Common

# ======================================================
# Parser for 'show cisp summary '
# ======================================================

class ShowCispSummarySchema(MetaParser):
    """Schema for show cisp summary"""

    schema = {
        'cisp': {
            'enabled': bool,
            'running': bool
        },
        Optional('interface'): {
            Any(): {
                'mode': str,
            },
        },
    }

class ShowCispSummary(ShowCispSummarySchema):
    """Parser for show cisp summary"""

    cli_command = 'show cisp summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # CISP not enabled
        p1 = re.compile(r"^CISP not enabled$")

        # CISP is not running on any interface
        # CISP is running on the following interface(s):
        p2 = re.compile(r"^CISP is (?P<running>not running|running) on.+$")

        #    Gi1/0/4 (Authenticator)
        p3 = re.compile(r"^(?P<interface>\S+)\s+\((?P<mode>\w+)\)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # CISP not enabled
            m = p1.match(line)
            if m:
                cisp_dict = ret_dict.setdefault('cisp', {})
                cisp_dict['enabled'] = False
                cisp_dict['running'] = False
                continue

            # CISP is not running on any interface
            # CISP is running on the following interface(s):
            m = p2.match(line)
            if m:
                cisp_dict = ret_dict.setdefault('cisp', {})
                cisp_dict['enabled'] = True
                cisp_dict['running'] = True if m.groupdict()['running'] == 'running' else False
                continue

            #    Gi1/0/4 (Authenticator)
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                intf_var = dict_val['interface']
                if 'interface' not in ret_dict:
                    interface = ret_dict.setdefault('interface', {})
                if intf_var not in ret_dict['interface']:
                    intf_dict = ret_dict['interface'].setdefault(intf_var, {})
                intf_dict['mode'] = dict_val['mode']
                continue


        return ret_dict


# ======================================================
# Parser for 'show cisp interface '
# ======================================================

class ShowCispInterfaceSchema(MetaParser):
    """Schema for show cisp interface"""

    schema = {
        'cisp': {
            'version': int,
            'mode': str,
            'peer_mode': str,
            Optional('supp_state'): str,
            Optional('auth_state'): str,
            'intf': str,
        },
    }

class ShowCispInterface(ShowCispInterfaceSchema):
    """Parser for show cisp interface <intf>"""

    cli_command = 'show cisp interface {intf}'

    def cli(self, intf=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(intf=intf))

        # Version:  1
        p1 = re.compile(r"^Version:\s+(?P<version>\d+)$")
        
        # Mode:  Supplicant
        p1_1 = re.compile(r"^Mode:\s+(?P<mode>\w+)$")
        
        # Peer Mode:  Authenticator
        p1_2 = re.compile(r"^Peer\s+Mode:\s+(?P<peer_mode>\w+)$")
        
        # Supp State:   Idle
        p1_3 = re.compile(r"^Supp\s+State:\s+(?P<supp_state>\w+)$")
        
        # CISP Status for interface Gi1/6
        p1_4 = re.compile(r"^CISP\s+Status\s+for\s+interface\s+(?P<intf>\S+)$")

        # Auth State:   Idle
        p1_5 = re.compile(r"^Auth\s+State:\s+(?P<auth_state>\w+)$")

        ret_dict = {}

        for line in output.splitlines():

            # Version:  1
            match_obj = p1.match(line)
            if match_obj:
                cisp_dict['version'] = int(match_obj.groupdict()['version'])
                continue

            # Mode:  Supplicant
            match_obj = p1_1.match(line)
            if match_obj:
                cisp_dict['mode'] = match_obj.groupdict()['mode']
                continue

            # Peer Mode:  Authenticator
            match_obj = p1_2.match(line)
            if match_obj:
                cisp_dict['peer_mode'] = match_obj.groupdict()['peer_mode']
                continue

            # Supp State:   Idle
            match_obj = p1_3.match(line)
            if match_obj:
                cisp_dict['supp_state'] = match_obj.groupdict()['supp_state']
                continue

            # CISP Status for interface Gi1/6
            match_obj = p1_4.match(line)
            if match_obj:
                cisp_dict = ret_dict.setdefault('cisp', {})
                cisp_dict['intf'] = match_obj.groupdict()['intf']
                continue

            # Auth State:   Idle
            match_obj = p1_5.match(line)
            if match_obj:
                cisp_dict['auth_state'] = match_obj.groupdict()['auth_state']
                continue

        return ret_dict


# ======================================================
# Parser for 'show cisp clients'
# ======================================================

class ShowCispClientsSchema(MetaParser):
    """Schema for show cisp clients"""

    schema = {
        'table_name': {
            'mode': str,
        },
        'mac_address': {
            Any(): {
                'vlan': int,
                'interface': str,
            },
        },
    }

class ShowCispClients(ShowCispClientsSchema):
    """Parser for show cisp clients"""

    cli_command = 'show cisp clients'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Supplicant Client Table:
        p1 = re.compile(r"^(?P<mode>\w+)\s+Client\s+Table:$")
        #    0c75.bdc7.e8c3   20          Gi1/6
        p2 = re.compile(r"^\s+(?P<mac_address>\S+)\s+(?P<vlan>\d+)\s+(?P<interface>\S+)$")

        ret_dict = {}

        for line in output.splitlines():

            # Supplicant Client Table:
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'table_name' not in ret_dict:
                    table_name = ret_dict.setdefault('table_name', {})
                table_name['mode'] = dict_val['mode']
                continue

            #    0c75.bdc7.e8c3   20          Gi1/6
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                mac_address_var = dict_val['mac_address']
                if 'mac_address' not in ret_dict:
                    mac_address = ret_dict.setdefault('mac_address', {})
                if mac_address_var not in ret_dict['mac_address']:
                    mac_address_dict = ret_dict['mac_address'].setdefault(mac_address_var, {})
                mac_address_dict['vlan'] = int(dict_val['vlan'])
                mac_address_dict['interface'] = dict_val['interface']
                continue

        return ret_dict


class ShowCispRegistrationsSchema(MetaParser):
    """
        Schema for show cisp registrations
    """

    schema = {
        'interface': {
            Any(): {
                Optional('auth_mgr'): str,
                Optional('dot1x'): str
            }
        }
    }


class ShowCispRegistrations(ShowCispRegistrationsSchema):
    """
        Parser for show cisp registrations
    """

    cli_command = 'show cisp registrations'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Interface(s) with CISP registered user(s):
        p1 = re.compile(r'^Interface\(s\) with CISP registered user\(s\):$')

        # Te1/0/12
        p2 = re.compile(r"^(?P<interface>\w+\/\w+\/[\w\.]+)$")
        
        # Auth Mgr (Authenticator)
        p3 = re.compile(r"^Auth Mgr \((?P<auth_mgr>\w+)\)$")

        # 802.1x Sup (Supplicant)
        p4 = re.compile(r"^802\.1x.+\((?P<dot1x>\w+)\)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Interface(s) with CISP registered user(s):
            m = p1.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {})
                continue

            # Te1/0/12
            m = p2.match(line)
            if m:
                interface_dict = int_dict.setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                continue

            # Auth Mgr (Authenticator)
            m = p3.match(line)
            if m:
                interface_dict['auth_mgr'] = m.groupdict()['auth_mgr']
                continue

            # 802.1x Sup (Supplicant)
            m = p4.match(line)
            if m:
                interface_dict['dot1x'] = m.groupdict()['dot1x']
                continue

        return ret_dict