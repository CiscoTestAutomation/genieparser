''' show_evpn.py

show evpn parser class

'''

from netaddr import EUI
from ipaddress import ip_address
import re

from ats import tcl
from ats.tcl import tclobj, tclstr
from metaparser import MetaParser
from metaparser.util.schemaengine import Any
from xbu_shared.parser.iosxr import IosxrCaasMetaParser

re_8bit_u = r'(?:' + r'|'.join([
    r'[0-9]',
    r'[1-9][0-9]',
    r'1[0-9][0-9]',
    r'2[0-4][0-9]',
    r'25[0-5]',
]) + r')'
re_8bit_x = r'(?:[A-Fa-f0-9]{1,2})'
re_8bit_02x = r'(?:[A-Fa-f0-9]{2})'
re_16bit_x = r'(?:[A-Fa-f0-9]{1,4})'
re_16bit_04x = r'(?:[A-Fa-f0-9]{4})'
re_mac = r'(?:' + r'|'.join([
    r'\.'.join([re_16bit_x] * 3),
    r':'.join([re_8bit_x] * 6),
    r'-'.join([re_8bit_x] * 6),
    r'\.'.join([re_8bit_x] * 6),
]) + r')'
re_ipv4 = r'(?:' + r'\.'.join([re_8bit_u] * 4) + r')'
re_ipv6 = r'(?:[A-Fa-f0-9:]*:[A-Fa-f0-9:]*(?::' + re_ipv4 + ')?)'
re_ip = r'(?:' + r'|'.join([re_ipv4, re_ipv6]) + ')'
re_label_str = r'(?:' + r'|'.join([
    r'[0-9]+',
    r'[A-Za-z0-9-]+', # See mpls_label_strings @ mpls/base/include/mpls_label_defs_extra.h
]) + r')'

class ShowEvpnEvi(IosxrCaasMetaParser):
    '''Parser class for 'show evpn evi' CLI.'''
    # TODO schema

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show evpn evi')
        return tcl.cast_any(result[1])


class ShowEvpnEviDetail(IosxrCaasMetaParser):
    '''Parser class for 'show evpn evi detail' CLI.'''
    # TODO schema

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show evpn evi detail')
        return tcl.cast_any(result[1])


class ShowEvpnEviMac(MetaParser):
    '''Parser class for 'show evpn evi mac' CLI.'''

    # TODO schema

    def __init__(self, mac=None, **kwargs):
        self.mac = mac
        super().__init__(**kwargs)

    def cli(self):
        if True:
            cmd = 'show evpn evi mac'.format()
        else:
            #bpetrovi Sept. 20th, 2016 - hacking to exclude remote
            #trying to match enXR baseline for ATT suite in JST's absence
            #bpetrovi Sept 27th, 2016, further changing local to Gi due to 
            #latest image changes
            cmd = 'show evpn evi mac | exclude 192.0.0.'.format()
        if self.mac:
            cmd += ' {mac}'.format(self.mac)

        out = self.device.execute(cmd)

        result = {
            'entries': []
        }


        for line in out.splitlines():
            line = line.rstrip()

            # EVI        MAC address    IP address                               Nexthop                                 Label
            # ---------- -------------- ---------------------------------------- --------------------------------------- --------

            # 65535      02e5.7847.6000 ::                                       Local                                   0
            # 1          0000.0000.0001 ::                                       No remote pathlist
            m = re.match(r'^(?P<evi>[0-9]+)'
                         r' +(?P<mac>' + re_mac + ')'
                         r' +(?P<ip>' + re_ip + ')'
                         r'(?: +No remote pathlist|'
                         r' +(?P<next_hop>\S+)'
                         r' +(?:(?P<label_int>\d+)|(?P<label_str>' + re_label_str + '))'
                         r')'
                         r'$', line)
            if m:
                entry = {
                    'evi': int(m.group('evi')),
                    'mac': EUI(m.group('mac')),
                    'ip': ip_address(m.group('ip')),
                    'next_hop': m.group('next_hop'),
                    'label': m.group('label_str') \
                    or (m.group('label_int') and int(m.group('label_int'))),
                }
                try:
                    entry['next_hop'] = ip_address(entry['next_hop'])
                except (TypeError, ValueError):
                    pass
                result['entries'].append(entry)
                continue

            # OLD

            # MAC address    Nexthop                                 Label    vpn-id  
            # -------------- --------------------------------------- -------- --------

            # 7777.7777.0002 N/A                                     24005    7       
            m = re.match(r'^(?P<mac>' + re_mac + ')'
                         r' +(?:N/A|(?P<ip>' + re_ip + ')|(?P<next_hop>\S+))'
                         r' +(?:(?P<label_int>\d+)|(?P<label_str>' + re_label_str + '))'
                         r' +(?P<evi>[0-9]+)'
                         r'$', line)
            if m:
                entry = {
                    'mac': EUI(m.group('mac')),
                    'ip': m.group('ip') and ip_address(m.group('ip')),
                    'next_hop': m.group('next_hop'),
                    'label': m.group('label_str') or int(m.group('label_int')),
                    'evi': int(m.group('evi')),
                }
                try:
                    entry['label'] = int(entry['label'])
                except ValueError:
                    pass
                result['entries'].append(entry)
                continue

        return result

# vim: ft=python ts=8 sw=4 et
