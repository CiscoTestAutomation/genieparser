"""show_l2route.py

NXOS parsers for the following show commands:
    * show l2route evpn mac all
    * show l2route evpn mac evi <evi>
    * show l2route evpn mac evi <WORD> mac <WORD>
"""

import re


from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# ====================================================
#  schema for 'show l2route evpn mac all'
# ====================================================
class ShowL2routeEvpnMacSchema(MetaParser):
    """Schema for show l2route evpn mac all"""

    schema = {
        'topology':
            {Any():
                {'mac_address':
                    {Any():
                        {'prod': str,
                         'flags': str,
                         'seq_no': str,
                         'next_hops': str,
                         Optional('label'): str}
                    },
                }
            },
        }

# ====================================================
#  parser for 'show l2route evpn mac all'
#  parser for 'show l2route evpn mac evi <evi>'
# ====================================================
class ShowL2routeEvpnMac(ShowL2routeEvpnMacSchema):
    """Parser for the following show commands:
        show l2route evpn mac all
        show l2route evpn mac evi <evi>
    """

    cli_command = ['show l2route evpn mac all',
        'show l2route evpn mac evi {evi}']

    def cli(self, evi='', output=None):
        if output is None:
            if evi:
                out = self.device.execute(self.cli_command[1].format(evi=evi))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 100         fa16.3eff.2a0c BGP    SplRcv        0          10.166.1.1
            p1 = re.compile(r'^\s*(?P<topology>[0-9]+) +(?P<mac_address>[a-z0-9\.]+) '
                '+(?P<prod>[a-zA-Z]+) +(?P<flags>[a-zA-Z\,]+) +(?P<seq_no>[0-9]+) '
                '+(?P<next_hops>[a-zA-Z0-9\/\.]+) *(\(Label: +)?(?P<label>[0-9]*)\)?$')
            m = p1.match(line)
            if m:

                topology = str(m.groupdict()['topology'])
                mac_address = str(m.groupdict()['mac_address'])
                label = str(m.groupdict()['label'])

                if 'topology' not in ret_dict:
                    ret_dict['topology'] = {}
                if topology not in ret_dict['topology']:
                    ret_dict['topology'][topology] = {}
                if 'mac_address' not in ret_dict['topology'][topology]:
                    ret_dict['topology'][topology]['mac_address'] = {}
                if mac_address not in ret_dict['topology'][topology]['mac_address']:
                    ret_dict['topology'][topology]['mac_address'][mac_address] = {}

                ret_dict['topology'][topology]['mac_address'][mac_address]['prod'] = \
                    str(m.groupdict()['prod'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['flags'] = \
                    str(m.groupdict()['flags'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['seq_no'] = \
                    str(m.groupdict()['seq_no'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['next_hops'] = \
                    str(m.groupdict()['next_hops'])
                if label:
                    ret_dict['topology'][topology]['mac_address'][mac_address]['label'] = \
                    label


                continue

        return ret_dict

# =========================================================
#  schema for 'show l2route evpn mac evi <WORD> mac <WORD>'
# =========================================================
class ShowL2routeEvpnMacEviSchema(MetaParser):
    """Schema for show l2route evpn mac evi <WORD> mac <WORD>"""

    schema = {
        'topology':
            {Any():
                {'mac_address':
                    {Any():
                        {'prod': str,
                         'flags': str,
                         'seq_no': str,
                         'next_hops': str}
                    },
                }
            },
        }

# =========================================================
#  parser for 'show l2route evpn mac evi <WORD> mac <WORD>'
# =========================================================
class ShowL2routeEvpnMacEvi(ShowL2routeEvpnMacEviSchema):
    """Parser for show l2route evpn mac evi <WORD> mac <WORD>"""

    cli_command = 'show l2route evpn mac evi {evi} mac {mac}'

    def cli(self, evi, mac, output=None):
        cmd = ""
        if evi and mac:
            cmd = self.cli_command.format(evi=evi, mac=mac)

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # 100         fa16.3eff.2a0c BGP    SplRcv        0          10.166.1.1
        p1 = re.compile(r'^\s*(?P<topology>[0-9]+) +(?P<mac_address>[a-z0-9\.]+) '
            '+(?P<prod>[a-zA-Z]+) +(?P<flags>[a-zA-Z\,]+) +(?P<seq_no>[0-9]+) '
            '+(?P<next_hops>[a-zA-Z0-9\/\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:

                topology = str(m.groupdict()['topology'])
                mac_address = str(m.groupdict()['mac_address'])

                if 'topology' not in ret_dict:
                    ret_dict['topology'] = {}
                if topology not in ret_dict['topology']:
                    ret_dict['topology'][topology] = {}
                if 'mac_address' not in ret_dict['topology'][topology]:
                    ret_dict['topology'][topology]['mac_address'] = {}
                if mac_address not in ret_dict['topology'][topology]['mac_address']:
                    ret_dict['topology'][topology]['mac_address'][mac_address] = {}

                ret_dict['topology'][topology]['mac_address'][mac_address]['prod'] = \
                    str(m.groupdict()['prod'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['flags'] = \
                    str(m.groupdict()['flags'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['seq_no'] = \
                    str(m.groupdict()['seq_no'])
                ret_dict['topology'][topology]['mac_address'][mac_address]['next_hops'] = \
                    str(m.groupdict()['next_hops'])

                continue

        return ret_dict

# vim: ft=python ts=8 sw=4 et