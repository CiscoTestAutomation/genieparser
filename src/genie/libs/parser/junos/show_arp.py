"""show_arp.py

JunOS parsers for the following show commands:
    * show arp
    * show arp | no-more
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema, ListOf)


class ShowArpSchema(MetaParser):
    """ Schema for:
            * show arp
            * show arp | no-more
    """
    """schema = {
        "arp-table-information": {
            "arp-entry-count": str,
            "arp-table-entry": [
                {
                    "arp-table-entry-flags": str,
                    "hostname": str,
                    "interface-name": str,
                    "ip-address": str,
                    "mac-address": str
                }
            ]
        }
    }"""

    # Main Schema
    schema = {
        "arp-table-information": {
            "arp-entry-count": str,
            "arp-table-entry": ListOf({
                "arp-table-entry-flags": str,
                "hostname": str,
                "interface-name": str,
                "ip-address": str,
                "mac-address": str
            })
        }
    }

class ShowArp(ShowArpSchema):
    """ Parser for:
            * show arp
    """
    cli_command = 'show arp'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 00:50:56:ff:ba:6f 10.1.0.1         10.1.0.1                   fxp0.0                  none
        p1 = re.compile(r'^(?P<mac_address>[\w:]+) +(?P<ip_address>\S+) +(?P<hostname>\S+) +'
                r'(?P<interface_name>\S+) +(?P<arp_table_entry_flags>\S+)$')

        # Total entries: 7
        p2 = re.compile(r'^Total +entries: +(?P<total_entries>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # 00:50:56:ff:ba:6f 10.1.0.1         10.1.0.1                   fxp0.0                  none
            m = p1.match(line)
            if m:
                group = m.groupdict()
                arp_table_entry_list = ret_dict.setdefault('arp-table-information', {}). \
                    setdefault('arp-table-entry', [])
                arp_table_entry_dict = {}
                arp_table_entry_dict.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                arp_table_entry_list.append(arp_table_entry_dict)
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                total_entries = group['total_entries']
                ret_dict.setdefault('arp-table-information', {}).\
                    setdefault('arp-entry-count', total_entries)
                continue
        return ret_dict

class ShowArpNoMore(ShowArp):
    """ Parser for:
            * show arp | no-more
    """
    cli_command = 'show arp | no-more'
    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowArpNoResolveSchema(MetaParser):
    """ Schema for:
            * show arp no-resolve
    """
    """schema = {
        Optional("@xmlns:junos"): str,
        "arp-table-information": {
            Optional("@junos:style"): str,
            Optional("@xmlns"): str,
            "arp-entry-count": str,
            "arp-table-entry": [
                {
                    "arp-table-entry-flags": str,
                    "interface-name": str,
                    "ip-address": str,
                    "mac-address": str
                }
            ]
        }
    }"""

    # Main Schema
    schema = {
        "arp-table-information": {
            "arp-entry-count": str,
            "arp-table-entry": ListOf({
                "arp-table-entry-flags": str,
                "interface-name": str,
                "ip-address": str,
                "mac-address": str
            })
        }
    }

class ShowArpNoResolve(ShowArpNoResolveSchema):
    """ Parser for:
            * show arp no-resolve
    """
    cli_command = 'show arp no-resolve'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #00:50:56:ff:ba:6f 10.1.0.1         fxp0.0                   none
        p1 = re.compile(r'^(?P<mac_address>[\w:]+) +'
                        r'(?P<ip_address>\S+) +(?P<interface_name>\S+) '
                        r'+(?P<arp_table_entry_flags>\S+)$')

        # Total entries: 7
        p2 = re.compile(r'^Total +entries: +(?P<total_entries>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            #00:50:56:ff:ba:6f 10.1.0.1         fxp0.0                   none
            m = p1.match(line)
            if m:
                group = m.groupdict()
                arp_table_dict = ret_dict.setdefault('arp-table-information', {})
                arp_table_entry_list =  arp_table_dict.setdefault('arp-table-entry', [])
                arp_table_entry_dict = {}
                arp_table_entry_dict.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                arp_table_entry_list.append(arp_table_entry_dict)
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                arp_table_dict["arp-entry-count"] = group['total_entries']
                continue

        return ret_dict