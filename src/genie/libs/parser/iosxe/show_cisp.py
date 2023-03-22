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

# ======================================================
# Parser for 'show cisp summary '
# ======================================================

class ShowCispSummarySchema(MetaParser):
    """Schema for show cisp summary"""

    schema = {
        'interface': {
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

        #    Gi1/0/4 (Authenticator)
        p1 = re.compile(r"^\s+(?P<interface>\S+)\s+\((?P<mode>\w+)\)$")

        ret_dict = {}

        for line in output.splitlines():

            #    Gi1/0/4 (Authenticator)
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
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
            'supp_state': str,
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

        ret_dict = {}

        for line in output.splitlines():

            # Version:  1
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'cisp' not in ret_dict:
                    cisp = ret_dict.setdefault('cisp', {})
                cisp['version'] = int(dict_val['version'])
                continue

            # Mode:  Supplicant
            match_obj = p1_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'cisp' not in ret_dict:
                    cisp = ret_dict.setdefault('cisp', {})
                cisp['mode'] = dict_val['mode']
                continue

            # Peer Mode:  Authenticator
            match_obj = p1_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'cisp' not in ret_dict:
                    cisp = ret_dict.setdefault('cisp', {})
                cisp['peer_mode'] = dict_val['peer_mode']
                continue

            # Supp State:   Idle
            match_obj = p1_3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'cisp' not in ret_dict:
                    cisp = ret_dict.setdefault('cisp', {})
                cisp['supp_state'] = dict_val['supp_state']
                continue

            # CISP Status for interface Gi1/6
            match_obj = p1_4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'cisp' not in ret_dict:
                    cisp = ret_dict.setdefault('cisp', {})
                cisp['intf'] = dict_val['intf']
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
