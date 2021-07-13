''' show_nve.py

IOSXE parsers for the following show commands:

    * 'show nve peers'
    * 'show nve peers interface nve {nve}'
    * 'show nve peers peer-ip {peer_ip}'
    * 'show nve peers vni {vni}'

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ====================================================
#  schema for show nve peers
# ====================================================
class ShowNvePeersSchema(MetaParser):
    '''Schema for:

       * 'show nve peers'
       * 'show nve peers interface nve {nve}'
       * 'show nve peers peer-ip {peer_ip}'
       * 'show nve peers vni {vni}'
    '''

    schema = {
        'interface': {
            Any(): {
                Optional('vni'): {
                    Any(): {
                        Optional('peer_ip'): {
                            Any (): {
                                'type': str,
                                'rmac_num_rt': str,
                                'evni': str,
                                'state': str,
                                'flags': str,
                                'uptime': str
                            }
                        }
                    }
                },
            },
        },
    }

# ============================================
# Super Parser for:
#   * 'show nve peers '
#   * 'show nve peers interface nve {nve}'
#   * 'show nve peers peer-ip {peer_ip}'
#   * 'show nve peers vni {vni}'
# ============================================
class ShowNvePeers(ShowNvePeersSchema):
    ''' Parser for the following show commands:

        * 'show nve peers'
        * 'show nve peers interface nve {nve}'
        * 'show nve peers peer-ip {peer_ip}'
        * 'show nve peers vni {vni}'
    '''

    cli_command = ['show nve peers',
                   'show nve peers interface nve {nve}',
                   'show nve peers peer-ip {peer_ip}',
                   'show nve peers vni {vni}']

    def cli(self, nve='', peer_ip='', vni='', output=None):

        if output is None:
            if nve:
                cmd = self.cli_command[1].format(nve=nve)
            elif peer_ip:
                cmd = self.cli_command[2].format(peer_ip=peer_ip)
            elif vni:
                cmd = self.cli_command[3].format(vni=vni)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        res_dict = {}
        # Interface  VNI      Type Peer-IP          RMAC/Num_RTs   eVNI     state flags UP time
        # nve1       3000101  L3CP 20.0.101.2       5c71.0dfe.fb60 3000101    UP  A/M/4 4d21h
        # nve1       3000101  L3CP 30.0.107.78      ac3a.6767.049f 3000101    UP  A/M/4 4d21h
        # nve1       200051   L2CP 20.0.101.2       3              200051     UP   N/A  4d17h
        # nve1       200051   L2CP 20.0.101.3       3              200051     UP   N/A  4d17h
        # nve1       200051   L2CP 30.0.107.78      6              200051     UP   N/A  4d17h
        # nve1       200052   L2CP 20.0.101.2       3              200052     UP   N/A  4d17h
        # nve1       200052   L2CP 20.0.101.3       3              200052     UP   N/A  4d17h
        # nve1       200052   L2CP 30.0.107.78      6              200052     UP   N/A  4d17h

        p1 = re.compile(r'^\s*(?P<nve_interface>[\w\/]+)\s+(?P<vni>[\d]+)\s+'
                            r'(?P<type>(L3CP|L2CP))\s+(?P<peer_ip>[\w\.\:]+)\s+(?P<rmac_num_rt>[\S]+)\s+'
                            r'(?P<evni>[\d]+)\s+(?P<state>(UP|DOWN))\s+(?P<flags>[\S]+)\s+(?P<uptime>[\S]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                nve_interface = group['nve_interface']
                vni = group['vni']
                cp_type = group['type']
                peer_ip = group['peer_ip']
                rmac_num_rt = group['rmac_num_rt']
                evni = group['evni']
                state = group['state']
                flags = group['flags']
                uptime = group['uptime']
                intf_dict = res_dict.setdefault('interface', {}).setdefault(nve_interface, {})
                vni_dict = intf_dict.setdefault('vni', {}).setdefault(vni, {})
                peer_dict = vni_dict.setdefault('peer_ip', {}).setdefault(peer_ip, {})
                peer_dict.update({'type': cp_type})
                peer_dict.update({'rmac_num_rt': rmac_num_rt})
                peer_dict.update({'evni': evni})
                peer_dict.update({'state': state})
                peer_dict.update({'flags': flags})
                peer_dict.update({'uptime': uptime})

                continue

        return res_dict

#-------------------------------------------------------------------------------
