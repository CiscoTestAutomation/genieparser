"""show_l2vpn.py

show l2vpn bridge-domain
"""
# Python
import re
from ipaddress import ip_address

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.libs.parser.utils.common import Common

# ====================================
# Schema for 'show l2vpn bridge-domain'
# ====================================

class ShowL2vpnBridgeDomainSchema(MetaParser):
    """Schema for show l2vpn bridge-domain
    """
    schema = {
        'bridge_group': {
            Any(): {
                'bridge_domain': {
                    Any(): {
                        'id': int,
                        'state': str,
                        Optional('shg_id'): int,
                        Optional('mst_i'): int,
                        Optional('mac_aging_time'): int,
                        Optional('mac_limit'): int,
                        Optional('mac_limit_action'): str,
                        Optional('mac_limit_notification'): str,
                        Optional('filter_mac_address'): int,
                        'ac': {
                            'num_ac': int,
                            'num_ac_up': int,
                            Optional('interfaces'): {
                                Any(): {
                                    'state': str,
                                    Optional('static_mac_address'): int,
                                    Optional('bvi_mac_address'): int,
                                    Optional('mst_i'): int,
                                    Optional('mst_i_state'): str
                                }
                            }
                        },
                        Optional('vfi'): {
                            'num_vfi': int,
                            Any(): {
                                Optional('state'): str,
                                Optional('neighbor'): {
                                    Any(): {
                                        'pw_id': {
                                            Any(): {
                                                'state': str,
                                                'static_mac_address': int
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        'pw': {
                            'num_pw': int,
                            'num_pw_up': int,
                            Optional("neighbor"): {
                                Any(): {
                                    "pw_id": {
                                        Any(): {
                                            "state": str, 
                                            "static_mac_address": int
                                        }
                                    }
                                }
                            }
                        },
                        Optional('pbb'): {
                            'num_pbb': int,
                            'num_pbb_up': int,
                        },
                        Optional('vni'): {
                            'num_vni': int,
                            'num_vni_up': int,
                        },
                        Optional('evpn'): {
                            Any(): {
                                'state': str,
                            }
                        }
                    },
                }
            }
        }
    }


class ShowL2vpnBridgeDomain(ShowL2vpnBridgeDomainSchema):
    """Parser for show l2vpn bridge-domain"""

    cli_command = 'show l2vpn bridge-domain'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        ret_dict = {}
        section_name = ""

        # Bridge group: g1, bridge-domain: bd1, id: 0, state: up, ShgId: 0, MSTi: 0
        # Bridge group: ev-Multicast, bridge-domain: ev-Multicast-TV, id: 1, state: up, ShgId: 0, MSTi: 0
        # Bridge group: a_b, bridge-domain: CD, id: 2, state: admin down (Shutdown), ShgId: 0, MSTi: 0
        p1 = re.compile(r'^Bridge +group: +(?P<bridge_group>\S+), +bridge\-domain: +'
            '(?P<bridge_domain>\S+), +id: +(?P<id>\d+), +state: +(?P<state>[\w\s\(\)]+), +'
            'ShgId: +(?P<shg_id>\d+), +MSTi: +(?P<mst_i>\d+)$')

        # Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
        # Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        p2 = re.compile(r'^Aging: +(?P<mac_aging_time>\d+) s, +MAC +limit: +(?P<mac_limit>\d+), +'
                r'Action: +(?P<mac_limit_action>[\S ]+), +Notification: +'
                r'(?P<mac_limit_notification>[\S ]+)$')

        # Filter MAC addresses: 0
        p3 = re.compile(r'^Filter +MAC +addresses: +(?P<filter_mac_address>\d+)$')

        # ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
        p4 = re.compile(r'^ACs: +(?P<ac>\d+) +\((?P<ac_up>\d+) +up\), +VFIs: +(?P<vfi>\d+), +'
            'PWs: +(?P<pw>\d+) +\((?P<pw_up>\d+) +\w+\)(, +PBBs: +(?P<pbb>\d+)'
            ' +\((?P<pbb_up>\d+) +up\))?(, +VNIs: +(?P<vni>\d+) +\((?P<vni_up>\d+) +up\))?$')

        # Gi0/1/0/0, state: up, Static MAC addresses: 2, MSTi: 0 (unprotected)
        p5 = re.compile(r'^(?P<interface>\S+), +state: +(?P<state>\w+), +Static +'
            'MAC +addresses: +(?P<static_mac_address>\d+)(, +MSTi: +(?P<mst_i>\d+)'
            '( +\((?P<mst_i_state>\w+)\))?)?$')
        
        # BV100, state: up, BVI MAC addresses: 1
        p5_1 = re.compile(r'^(?P<interface>\S+), +state: +(?P<state>\w+), +BVI +'
            'MAC +addresses: +(?P<bvi_mac_address>\S+)$')

        # VFI 1
        # VFI vfi60 (up)
        # VFI string_LABEL_01 (up)
        p6 = re.compile(r'^VFI\s+(?P<vfi>\S+)(\s*(\((?P<state>[\w\s]+)\))?\s*)$')

        # Neighbor 10.1.1.1 pw-id 1, state: up, Static MAC addresses: 0
        # Neighbor 172.16.152.13 pw-id 20161:10090, state: up, Static MAC addresses: 0
        p7 = re.compile(r'Neighbor +(?P<neighbor>\S+) +pw-id +(?P<pw_id>[\d\:]+), +state: +'
            '(?P<state>\w+), +Static +MAC +addresses: +(?P<static_mac_address>\d+)$')

        # g1/bd1                           0     up         1/1            1/1 
        p8 = re.compile(r'^(?P<bridge_group>\S+)\/(?P<bridge_domain_name>\S+) +(?P<id>\d+) +'
            '(?P<state>\w+) +(?P<ac>\d+)\/(?P<ac_up>\d+) +(?P<pw>\d+)\/(?P<pw_up>\d+)$')
        
        # EVPN, state: up
        p9 = re.compile(r'^(?P<evpn>\S+), +state: +(?P<state>\w+)$')

        # List of Access PWs:
        p10 = re.compile(r'^List +of +Access +PWs:$')

        # List of VFIs:
        p11 = re.compile(r'^List +of +VFIs:$')
        
        for line in out.splitlines():
            line = line.strip()
            
            # Bridge group: g1, bridge-domain: bd1, id: 0, state: up, ShgId: 0, MSTi: 0
            # Bridge group: EVPN-Multicast, bridge-domain: EVPN-Multicast-BTV, id: 0, state: up, ShgId: 0, MSTi: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                bridge_group = group['bridge_group']
                bridge_domain = group['bridge_domain']
                id = int(group['id'])
                state = group['state']
                shg_id = int(group['shg_id'])
                mst_i = int(group['mst_i'])

                bridge_domain_dict = ret_dict.setdefault('bridge_group', {}). \
                    setdefault(bridge_group, {}). \
                    setdefault('bridge_domain', {}). \
                    setdefault(bridge_domain, {})

                bridge_domain_dict.update({'id': id})  
                bridge_domain_dict.update({'state': state}) 
                bridge_domain_dict.update({'shg_id': shg_id}) 
                bridge_domain_dict.update({'mst_i': mst_i}) 
                continue
            
            # Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for k,v in group.items():
                    bridge_domain_dict.update({k: int(v) if v.isdigit() else v})
                continue
            
            # Filter MAC addresses: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                filter_mac_address = int(group['filter_mac_address'])
                bridge_domain_dict.update({'filter_mac_address': filter_mac_address})
                continue
                
            # ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ac = int(group['ac'])
                ac_up = int(group['ac_up'])
                vfi = int(group['vfi'])
                pw = int(group['pw'])
                pw_up = int(group['pw_up'])
                
                ac_dict = bridge_domain_dict.setdefault('ac', {})
                ac_dict.update({'num_ac': ac})
                ac_dict.update({'num_ac_up': ac_up})

                vfi_dict = bridge_domain_dict.setdefault('vfi', {})
                vfi_dict.update({'num_vfi': vfi})

                pw_dict = bridge_domain_dict.setdefault('pw', {})
                pw_dict.update({'num_pw': pw})
                pw_dict.update({'num_pw_up': pw_up})

                pbb = group['pbb']
                pbb_up = group['pbb_up']
                if pbb:
                    pbb_dict = bridge_domain_dict.setdefault('pbb', {})
                    pbb_dict.update({'num_pbb': int(pbb)})
                    pbb_dict.update({'num_pbb_up': int(pbb_up)})

                vni = group['vni']
                vni_up = group['vni_up']
                if vni:
                    vni_dict = bridge_domain_dict.setdefault('vni', {})
                    vni_dict.update({'num_vni': int(vni)})
                    vni_dict.update({'num_vni_up': int(vni_up)})

                continue
            
            # Gi0/1/0/0, state: up, Static MAC addresses: 2, MSTi: 0 (unprotected)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                state = group['state']
                static_mac_address = int(group['static_mac_address'])
                interface_dict = ac_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                interface_dict.update({'state': state})
                interface_dict.update({'static_mac_address': static_mac_address})
                if group['mst_i']:
                    mst_i = int(group['mst_i'])
                    interface_dict.update({'mst_i': mst_i})
                mst_i_state = group['mst_i_state']
                if mst_i_state:
                    interface_dict.update({'mst_i_state': mst_i_state})
                continue

            # BV100, state: up, BVI MAC addresses: 1
            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                state = group['state']
                bvi_mac_address = int(group['bvi_mac_address'])

                interface_dict = ac_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                interface_dict.update({'state': state})
                interface_dict.update({'bvi_mac_address': bvi_mac_address})
                continue

            # VFI 1
            # VFI vfi60 (up)
            m = p6.match(line)
            if m:
                # clear state from earlier
                state = ''
                group = m.groupdict()
                vfi = group['vfi']
                vfi_dict = bridge_domain_dict.setdefault('vfi', {}). \
                    setdefault(vfi, {})
                if group['state']:   
                    state = group['state']
                if state:
                    vfi_dict.update({'state': state})
                continue

            # Neighbor 10.1.1.1 pw-id 1, state: up, Static MAC addresses: 0
            # Neighbor 172.16.152.13 pw-id 20161:10090, state: up, Static MAC addresses: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                neighbor = group['neighbor']
                pw_id = group['pw_id']
                state = group['state']
                static_mac_address = int(group['static_mac_address'])

                if section_name == "vfi":
                    neighbor_dict = vfi_dict.setdefault('neighbor', {}). \
                        setdefault(neighbor, {}). \
                        setdefault('pw_id', {}). \
                        setdefault(pw_id, {})
                elif section_name == "access_pw":
                    neighbor_dict = pw_dict.setdefault('neighbor', {}). \
                        setdefault(neighbor, {}). \
                        setdefault('pw_id', {}). \
                        setdefault(pw_id, {})    

                neighbor_dict.update({'state': state})
                neighbor_dict.update({'static_mac_address': static_mac_address})
                continue

            # g1/bd1                           0     up         1/1            1/1 
            m = p8.match(line)
            if m:
                group = m.groupdict()
                bridge_group = group['bridge_group']
                bridge_domain = group['bridge_domain_name']
                bridge_domain_id = int(group['id'])
                state = group['state']
                ac = int(group['ac'])
                ac_up = int(group['ac_up'])
                pw = int(group['pw'])
                pw_up = int(group['pw_up'])

                bridge_domain_dict = ret_dict.setdefault('bridge_group', {}). \
                    setdefault(bridge_group, {}). \
                    setdefault('bridge_domain', {}). \
                    setdefault(bridge_domain, {})

                bridge_domain_dict.update({'id': bridge_domain_id})  
                bridge_domain_dict.update({'state': state})

                ac_dict = bridge_domain_dict.setdefault('ac', {})
                ac_dict.update({'num_ac': ac})
                ac_dict.update({'num_ac_up': ac_up})

                pw_dict = bridge_domain_dict.setdefault('pw', {})
                pw_dict.update({'num_pw': pw})
                pw_dict.update({'num_pw_up': pw_up})

                continue
            
            # EVPN, state: up
            m = p9.match(line)
            if m:
                group = m.groupdict()
                evpn = group['evpn']
                evpn_state = group['state']
                evpn_dict = bridge_domain_dict.setdefault('evpn', {}). \
                                setdefault(evpn, {})
                evpn_dict.update({'state': state})
                continue

            # List of Access PWs:
            m = p10.match(line)
            if m:
                section_name = "access_pw"
                continue

            # List of VFIs:
            m = p11.match(line)
            if m:
                section_name = "vfi"
                continue

        return ret_dict
