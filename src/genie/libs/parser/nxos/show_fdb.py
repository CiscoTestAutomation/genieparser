"""show_fdb.py
   supported commands:
     *  show mac address-table vni <WORD> | grep <WORD>
     *  show mac address-table local vni <WORD>
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use


class ShowMacAddressTableVniSchema(MetaParser):
    """Schema for show mac address-table vni <WORD> | grep <WORD>"""
    """Schema for show mac address-table local vni <WORD>"""

    schema = {'mac_address':
                {Any():
                    {'evi': str,
                     'mac_type': str,
                     'mac_aging_time': str,
                     'entry': str,
                     'secure': str,
                     'ntfy': str,
                     'next_hop': str,
                     'ports': str,
                    }
                },
            }

class ShowMacAddressTableVni(ShowMacAddressTableVniSchema):
    """Parser for show mac address-table vni <WORD> | grep <WORD>"""
    """Parser for show mac address-table local vni <WORD>"""

    cli_command = ['show mac address-table vni {vni} | grep {intf}', 'show mac address-table local vni {vni}']

    def cli(self, vni, intf=None, output=None):

        cmd = ""
        if output is None:
            if vni and intf:
                cmd = self.cli_command[0].format(vni=vni, intf=intf)
            if vni and not intf:
                cmd = self.cli_command[1].format(vni=vni)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # C 1001     0000.04b1.0000   dynamic  0         F      F    nve1(3.0.0.101)
        # * 1001     0000.0191.0000   dynamic  0         F      F    Eth1/11
        p1 = re.compile(r'^\s*(?P<entry>[A-Z\*\(\+\)]+) +(?P<evi>[0-9]+) '
            '+(?P<mac_address>[0-9a-z\.]+) +(?P<mac_type>[a-z]+) '
            '+(?P<age>[0-9\-\:]+) +(?P<secure>[A-Z]+) +(?P<ntfy>[A-Z]+) '
            '+([a-z0-9]+\((?P<next_hop>[0-9\.]+)\))?(?P<ports>[a-zA-Z0-9\/\.]+)?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:

                mac_address = str(m.groupdict()['mac_address'])

                if 'mac_address' not in ret_dict:
                    ret_dict['mac_address'] = {}
                if mac_address not in ret_dict['mac_address']:
                    ret_dict['mac_address'][mac_address] = {}

                ret_dict['mac_address'][mac_address]['evi'] = \
                    str(m.groupdict()['evi'])
                ret_dict['mac_address'][mac_address]['mac_type'] = \
                    str(m.groupdict()['mac_type'])
                ret_dict['mac_address'][mac_address]['mac_aging_time'] = \
                    str(m.groupdict()['age'])
                ret_dict['mac_address'][mac_address]['entry'] = \
                    str(m.groupdict()['entry'])
                ret_dict['mac_address'][mac_address]['secure'] = \
                    str(m.groupdict()['secure'])
                ret_dict['mac_address'][mac_address]['ntfy'] = \
                    str(m.groupdict()['ntfy'])
                ret_dict['mac_address'][mac_address]['next_hop'] = \
                    str(m.groupdict()['next_hop'])
                ret_dict['mac_address'][mac_address]['ports'] = \
                    str(m.groupdict()['ports'])

                continue

        return ret_dict