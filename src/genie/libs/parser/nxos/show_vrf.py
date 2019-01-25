"""show_vrf.py

NXOS parsers for the following show commands:
    * 'show vrf'
    * 'show vrf <WORD> detail'
"""

# Python
import re
import xmltodict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common

# =====================
# Parser for 'show vrf'
# =====================

class ShowVrfSchema(MetaParser):
    """Schema for show vrf"""

    schema = {
        'vrfs':
            {Any():
                {'vrf_id': int,
                 'vrf_state': str,
                 'reason': str,},
            },
        }

class ShowVrf(ShowVrfSchema):
    """Parser for show vrf"""

    cli_command = 'show vrf'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        vrf_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # VRF2                                    4 Up      --
            # default                                 1 Up      --
            p1 = re.compile(r'^\s*(?P<vrf_name>(\S+)) +(?P<vrf_id>[0-9]+)'
                             ' +(?P<vrf_state>(Up|Down)) +(?P<reason>(\S+))$')
            m = p1.match(line)
            if m:
                if 'vrfs' not in vrf_dict:
                    vrf_dict['vrfs'] = {}
                vrf_name = str(m.groupdict()['vrf_name'])
                if vrf_name not in vrf_dict['vrfs']:
                    vrf_dict['vrfs'][vrf_name] = {}
                vrf_dict['vrfs'][vrf_name]['vrf_id'] = \
                    int(m.groupdict()['vrf_id'])
                vrf_dict['vrfs'][vrf_name]['vrf_state'] = \
                    str(m.groupdict()['vrf_state'])
                vrf_dict['vrfs'][vrf_name]['reason'] = \
                    str(m.groupdict()['reason'])
                continue

        return vrf_dict

class ShowVrfInterfaceSchema(MetaParser):
    """Schema for show vrf interface"""

    schema = {
            'vrf_interface':
                {Any():
                    {'vrf_name': str,
                     'vrf_id': str,
                     'site_of_origin': str},
                },
            }

class ShowVrfInterface(ShowVrfInterfaceSchema):
    """Parser for show vrf Interface"""

    cli_command = 'show vrf interface'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # Init vars
        vrf_interface_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            p1 = re.compile(r'^\s*Interface +VRF-Name +VRF-ID +Site-of-Origin$')
            m = p1.match(line)
            if m:
                continue

            p2 = re.compile(r'^\s*(?P<intf_name>[a-zA-Z0-9\/]+)'
                ' +(?P<vrf_name>[a-zA-Z0-9\-]+) +(?P<vrf_id>[0-9]+)'
                ' +(?P<site_of_origin>[a-zA-Z0-9\-]+)?$')
            m = p2.match(line)
            if m:
                interface = m.groupdict()['intf_name']
                if 'vrf_interface' not in vrf_interface_dict:
                    vrf_interface_dict['vrf_interface'] = {}
                if interface not in vrf_interface_dict['vrf_interface']:
                    vrf_interface_dict['vrf_interface'][interface] = {}
                vrf_interface_dict['vrf_interface'][interface]['vrf_name'] = \
                    m.groupdict()['vrf_name']
                vrf_interface_dict['vrf_interface'][interface]['vrf_id'] = \
                    m.groupdict()['vrf_id']
                vrf_interface_dict['vrf_interface'][interface]['site_of_origin'] = \
                    m.groupdict()['site_of_origin']
                continue

        return vrf_interface_dict


class ShowVrfDetailSchema(MetaParser):
    """Schema for show vrf <vrf> detail"""

    schema = {Any():
                {
                 'vrf_id':  int,
                 Optional('route_distinguisher'): str,
                 Optional('vpn_id'): str,
                 'max_routes':  int,
                 'mid_threshold':  int,
                 'state': str,
                 'address_family': {
                    Any(): {
                        'table_id': str,
                         'fwd_id':  str,
                         'state':  str,
                    },                        
                }
            },
        }

class ShowVrfDetail(ShowVrfDetailSchema):
    """Parser for show vrf <vrf> detail"""

    cli_command = 'show vrf {vrf} detail'

    def cli(self, vrf='all',output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            out = output
        
        # Init vars
        vrf_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # VRF-Name: VRF1, VRF-ID: 3, State: Up
            p1 = re.compile(r'^VRF\-Name: +(?P<vrf>[\w\-]+), +'
                             'VRF-ID: +(?P<vrf_id>\d+), +'
                             'State: +(?P<state>\w+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                if vrf not in vrf_dict:
                    vrf_dict[vrf] = {}
                vrf_dict[vrf]['vrf_id'] = int(m.groupdict()['vrf_id'])
                vrf_dict[vrf]['state'] = m.groupdict()['state'].lower()
                continue

            # VPNID: unknown
            p2 = re.compile(r'^VPNID: +(?P<vpn_id>\w+)$')
            m = p2.match(line)
            if m:
                vpn_id = m.groupdict()['vpn_id']
                if vpn_id != 'unknown':
                    vrf_dict[vrf]['vpn_id'] = vpn_id
                continue

            # RD: 300:1
            p3 = re.compile(r'^RD: +(?P<rd>[\w\:\.]+)$')
            m = p3.match(line)
            if m:
                vrf_dict[vrf]['route_distinguisher'] = m.groupdict()['rd']
                continue

            # Max Routes: 20000  Mid-Threshold: 17000
            p4 = re.compile(r'^Max +Routes: +(?P<max_routes>\d+) +'
                             'Mid\-Threshold: +(?P<mid_threshold>\d+)$')
            m = p4.match(line)
            if m:
                vrf_dict[vrf]['max_routes'] = int(m.groupdict()['max_routes'])
                vrf_dict[vrf]['mid_threshold'] = int(m.groupdict()['mid_threshold'])
                continue

            # Table-ID: 0x80000003, AF: IPv6, Fwd-ID: 0x80000003, State: Up
            p5 = re.compile(r'^Table\-ID: +(?P<table_id>\w+), +'
                             'AF: +(?P<af>\w+), +'
                             'Fwd\-ID: (?P<fwd_id>\w+), +'
                             'State: +(?P<state>\w+)$')
            m = p5.match(line)
            if m:
                af = m.groupdict()['af'].lower()
                if 'address_family' not in vrf_dict[vrf]:
                    vrf_dict[vrf]['address_family'] = {}
                if af not in vrf_dict[vrf]['address_family']:
                    vrf_dict[vrf]['address_family'][af] = {}

                vrf_dict[vrf]['address_family'][af]['table_id'] = m.groupdict()['table_id']
                vrf_dict[vrf]['address_family'][af]['fwd_id'] = m.groupdict()['fwd_id']
                vrf_dict[vrf]['address_family'][af]['state'] = m.groupdict()['state'].lower()
                continue

        return vrf_dict

# =====================================================================
#  Schema for "Parser for show running-config vrf <vrf> | sec '^vrf'"
# =====================================================================
class ShowRunningConfigVrfSchema(MetaParser):
    """Schema for show running-config vrf <vrf> | sec '^vrf'"""

    schema = {
        'vrf': {
            Any(): {
                Optional('vrf_name'): str,
                Optional('vni'): int,
                Optional('rd'): str,
                Optional('address_family'): {
                    Any(): {
                        Optional('route_target'): {
                            Any():{  # rt
                                Optional('rt_type'): str,
                                Optional('protocol'):{
                                    Any():{    # mvpn , evpn
                                    Optional('rt_evpn'): bool,
                                    Optional('rt_mvpn'): bool,
                                    }
                                }
                            }
                        }
                    }
                }
            },
        }
    }

# ========================================================================
#  Schema for "Parser for show running-config vrf <vrf> | sec '^vrf'"
# ========================================================================
class ShowRunningConfigVrf(ShowRunningConfigVrfSchema):
    """Parser for show running-config vrf <vrf> | sec '^vrf' """

    cli_command = "show running-config vrf {vrf} | sec '^vrf'"
    def cli(self):
        # Init vars
        vrf_list = []
        result_dict = {}

        # vrf context vni_10100
        p1 = re.compile(r'^vrf +context +(?P<vrf>\S+)$')

        #   vni 10100
        p2= re.compile(r'^\s*vni +(?P<vni>\d+)$')

        #   rd auto
        p3 = re.compile(r'^\s*rd +(?P<rd>\S+)$')

        #   address-family ipv4 unicast
        p4 = re.compile(r'^\s*address-family +(?P<af>[\S\s]+)$')

        #     route-target both auto
        #     route-target both auto mvpn
        #     route-target both auto evpn
        p5 = re.compile(r'^\s*route-target +(?P<rt_type>\w+) +(?P<rt>\w+)( +(?P<rt_evpn_mvpn>\w+))?$')

        # find all list of vrfs
        showVrf = ShowVrf(device=self.device)
        vrfs = showVrf.parse()
        for vrf in vrfs['vrfs'].keys():
            vrf_list.append(vrf)


        for vrf in vrf_list:
            out = self.device.execute(self.cli_command.format(vrf=vrf))

            for line in out.splitlines():
                line = line.strip()

                m = p1.match(line)
                if m:
                    vrf = m.groupdict()['vrf']
                    vrf_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {})
                    vrf_dict.update({'vrf_name': vrf})
                    continue

                m = p2.match(line)
                if m:
                    vni = m.groupdict()['vni']
                    vrf_dict.update({'vni': int(vni)})
                    continue

                m = p3.match(line)
                if m:
                    rd = m.groupdict()['rd']
                    vrf_dict.update({'rd': rd})
                    continue

                m = p4.match(line)
                if m:
                    af = m.groupdict()['af']
                    af_dict = vrf_dict.setdefault('address_family', {}).setdefault(af, {})
                    continue

                m = p5.match(line)
                if m:
                    rt = m.groupdict()['rt']
                    rt_type = m.groupdict()['rt_type']
                    route_target_dict = af_dict.setdefault('route_target', {}).setdefault(rt, {})
                    route_target_dict.update({'rt_type': m.groupdict()['rt_type']})

                    if m.groupdict()['rt_evpn_mvpn']:
                        if 'evpn' in m.groupdict()['rt_evpn_mvpn']:
                            rt_evpn_mvpn = 'evpn'
                        if 'mvpn' in m.groupdict()['rt_evpn_mvpn']:
                            rt_evpn_mvpn = 'mvpn'
                        protocol_dict = route_target_dict.setdefault('protocol', {}).setdefault(rt_evpn_mvpn, {})

                        if 'mvpn' in rt_evpn_mvpn:
                            protocol_dict.update({'rt_mvpn': True})

                        if 'evpn' in rt_evpn_mvpn:
                            protocol_dict.update({'rt_evpn': True})

                    continue

        for i in list(result_dict['vrf']):
            if len(result_dict['vrf'][i]) < 2:
                del result_dict['vrf'][i]

        return result_dict