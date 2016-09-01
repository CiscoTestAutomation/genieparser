''' show_evpn.py

show evpn parser class

'''

from netaddr import EUI
from ipaddress import ip_address

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
re_ipv6 = r'(?[A-Fa-f0-9:]+(?::' + re_ipv4 + ')?)'
re_ip = r'(?:' + r'|'.join([re_ipv4, re_ipv6]) + ')'
re_label_str = r'(' + r'|'.join([
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
        cmd = 'show evpn evi mac'.format()
        if self.mac:
            cmd += ' {mac}'.format(self.mac)

        out = self.device.execute(cmd)

        result = {
            'entries': []
        }


        for line in out.splitlines():
            line = line.rstrip()

            # MAC address    Nexthop                                 Label    vpn-id  
            # -------------- --------------------------------------- -------- --------

            # 7777.7777.0002 N/A                                     24005    7       
            m = re.match(r'^(<?P<mac>' + re_mac + ')'
                         r' +(?:N/A|(?P<next_hop>' + re_ip + '))'
                         r' +(?P<label>' + re_label_str + ')'
                         r' +(?P<evi>[0-9]+)$', line)
            if m:
                entry = {
                    'mac': EUI(m.group('mac')),
                    'next_hop': m.group('next_hop') and ip_address(m.group('next_hop')),
                    'label': m.group('label'),
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
