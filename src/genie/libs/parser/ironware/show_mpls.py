"""
Module:
    genie.libs.parser.ironware.show_mpls

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    MPLS parsers for IronWare devices

Parsers:
    * show mpls lsp
    * show mpls vll <vll>
    * show mpls vll-local <vll>
    * show mpls ldp neighbor
"""

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

__author__ = 'James Di Trapani <james@ditrapani.com.au>'


# ======================================================
# Schema for 'show mpls lsp wide'
# ======================================================
class ShowMPLSLSPSchema(MetaParser):
    """Schema for show mpls lsp"""
    schema = {
        'lsps': {
            Any(): {
                'destination': str,
                'admin': str,
                'operational': str,
                'flap_count': int,
                'retry_count': int,
                Optional('tunnel_interface'): str,
                Optional('path'): str
            }
        }
    }


# ====================================================
#  parser for 'show mpls lsp wide'
# ====================================================
class ShowMPLSLSP(ShowMPLSLSPSchema):
    """
    Parser for show mpls lsp wide on Devices running IronWare
    """
    cli_command = 'show mpls lsp'

    """
    Note: LSPs marked with * are taking a Secondary Path
                                  Admin Oper  Tunnel   Up/Dn Retry Active
    Name                          State State Intf     Times No.   Path
    mlx8.1_to_ces.2      10.4.1.1  UP    UP    tnl0     1     0     --
    mlx8.1_to_ces.1      10.16.2.2   UP    UP    tnl56    1     0     --
    mlx8.1_to_mlx8.2     10.36.3.3   UP    UP    tnl63    1     0     --
    mlx8.1_to_mlx8.3     10.64.4.4   DOWN  DOWN  --       0     0     --
    """

    def cli(self, output=None):
        if output is None:
            # auto expand to wide
            out = self.device.execute(self.cli_command + ' wide')
        else:
            out = output
        lsp_dict = {}

        result_dict = {}

        # mlx8.1_to_ces.2      10.4.1.1  UP    UP    tnl0     1     0     --
        p1 = re.compile(
            r'(^(?P<name>\S+)\s+'
            r'(?P<endpoint>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+'
            r'(?P<adminstate>UP|DOWN)\s+(?P<operationstate>UP|DOWN)\s+'
            r'(?P<tunnelint>tnl\d+|--)\s+(?P<flapcount>\d+)\s+'
            r'(?P<retrynum>\d+)\s+(?P<activepath>\S+))'
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                result_dict = lsp_dict.setdefault('lsps', {})

                lsp_name = m.groupdict()['name']
                result_dict[lsp_name] = {
                    'destination': m.groupdict()['endpoint'],
                    'admin': m.groupdict()['adminstate'],
                    'operational': m.groupdict()['operationstate'],
                    'flap_count': int(m.groupdict()['flapcount']),
                    'retry_count': int(m.groupdict()['retrynum'])
                }

                tunnel = m.groupdict()['tunnelint']
                if tunnel != '--':
                    num = int(tunnel.strip('tnl'))
                    tunnel = 'tunnel{0}'.format(num)
                    result_dict[lsp_name]['tunnel_interface'] = tunnel

                path = m.groupdict()['activepath']
                if path != '--':
                    result_dict[lsp_name]['path'] = path

                continue
        return lsp_dict


# ======================================================
# Schema for 'show mpls vll {vll}'
# ======================================================
class ShowMPLSVLLSchema(MetaParser):
    """Schema for show mpls vll {vll}"""
    schema = {
        'vll': {
            Any(): {
                'vcid': int,
                'vll_index': int,
                'local': {
                    'type': str,
                    'interface': str,
                    Optional('vlan_id'): int,
                    Optional('inner_vlan_id'): int,
                    Optional('outer_vlan_id'): int,
                    'state': str,
                    Optional('mct_state'): str,
                    Optional('ifl_id'): str,
                    'vc_type': str,
                    'mtu': int,
                    'cos': str,
                    Optional('extended_counters'): bool,
                    Optional('counters'): bool
                },
                'peer': {
                    'ip': str,
                    'state': str,
                    Optional('reason'): str,
                    'vc_type': str,
                    'mtu': int,
                    'local_label': Or(int, str),
                    'remote_label': Or(int, str),
                    'local_group_id': Or(int, str),
                    'remote_group_id': Or(int, str),
                    Optional('tunnel_lsp'): {
                        'name': str,
                        Optional('tunnel_interface'): str
                    },
                    'lsps_assigned': str
                }
            }
        }
    }


# ====================================================
#  parser for 'show mpls vll {vll}'
# ====================================================
class ShowMPLSVLL(ShowMPLSVLLSchema):
    """
    Parser for show mpls vll {vll} on Devices running IronWare

    Reference Documenation -
        * https://resources.ditrapani.com.au/#!index.md#Vendor_Documentation

    """
    cli_command = 'show mpls vll {vll}'

    """
    VLL VLL-TEST1, VC-ID 2456, VLL-INDEX 2

    End-point        : tagged  vlan 3043  e 2/5
    End-Point state  : Up
    MCT state        : None
    IFL-ID           : --
    Local VC type    : tag
    Local VC MTU     : 9190
    COS              : --
    Extended Counters: Enabled
    Counter          : disabled

    Vll-Peer         : 192.168.1.1
        State          : UP
        Remote VC type : tag               Remote VC MTU  : 9190
        Local label    : 852217            Remote label   : 852417
        Local group-id : 0                 Remote group-id: 0
        Tunnel LSP     : mlx8.1_to_ces.2 (tnl15)
        MCT Status TLV : --
        LSPs assigned  : No LSPs assigned
    """

    def cli(self, vll, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vll=vll))
        else:
            out = output

        result_dict = {}

        interface_def = {
            'e': 'ethernet',
            'ethernet': 'ethernet'
        }

        # VLL VLL-TEST1, VC-ID 2456, VLL-INDEX 2
        p1 = re.compile(r'(^(VLL|vll|Vll)\s+(?P<name>[^,]+),+\s+VC-ID\s+'
                        r'(?P<vcid>[^,]+),'
                        r'\s+VLL-INDEX\s+(?P<vllindex>\d+$))')

        # End-point: tagged vlan 2501 e 2/10
        # End-point: untagged e 2/2
        # End-point: tagged vlan 100 inner-vlan 45 e 2/1
        p2 = re.compile(r'(^End-point\s+:\s+'
                        r'(?P<type>tagged|untagged|undefined)'
                        r'(\s+vlan\s+(?P<vid>\d+)|)(\s+inner-vlan\s+'
                        r'(?P<innerid>\d+)|)\s+(?P<interface_name>\w+)\s+'
                        r'(?P<interface>\d+\/\d+$))')

        # End-Point state  : Up
        p3 = re.compile(r'(^End-Point state\s+:\s+(?P<state>Up|Down))')

        # MCT state        : None
        p4 = re.compile(r'(^MCT state\s+:\s+(?P<mctstate>\S+$))')

        # IFL-ID           : --
        # IFL-ID           : n/a
        # IFL-ID           : 1234
        p5 = re.compile(r'(^IFL-ID\s+:\s+(?P<iflid>n\/a$|\d+$|--$))')

        # Local VC type    : tag
        # Local VC type : raw-pass-through
        p6 = re.compile(r'(^Local VC type\s+:\s+'
                        r'(?P<vctype>tag$|raw-pass-through$|--$|raw-mode$))')

        # Local VC MTU     : 9190
        p7 = re.compile(r'(^Local VC MTU\s+:\s+(?P<mtu>\d+$|--$))')

        # COS              : --
        p8 = re.compile(r'(^COS\s+:\s+(?P<cos>\S+$))')

        # Extended Counters: Enabled
        p9 = re.compile(r'(^Extended Counters:\s+'
                        r'(?P<extcounters>[e|E]nabled|[d|D]isabled)$)')

        # Counter          : disabled
        p10 = re.compile(r'(^Counter\s+:\s+'
                         r'(?P<counter>[e|E]nabled|[d|D]isabled)$)')

        # Vll-Peer         : 192.168.1.1
        p11 = re.compile(r'(^Vll-Peer\s+:\s+'
                         r'(?P<ip>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$))')

        # State          : UP
        # State          : DOWN - PW is Down (Reason:Wait for peer label)
        # For all states see page 550 in reference material
        p12 = re.compile(r'(^State\s+:\s+(?P<state>UP|DOWN)(\s-\s'
                         r'(?P<reason>\w.+$)|$))')

        # Remote VC type : tag               Remote VC MTU  : 9190
        p13 = re.compile(r'(^Remote VC type\s+:\s+'
                         r'(?P<vctype>tag|raw-pass-through|--)\s+'
                         r'Remote VC MTU\s+:\s+(?P<mtu>\d+$|--$))')

        # Local label    : 852217            Remote label   : 852417
        # Local label    : --                Remote label   : --
        p14 = re.compile(r'(^Local label\s+:\s(?P<local>\d+|--)\s+'
                         r'Remote label\s+:\s+(?P<remote>\d+$|--$))')

        # Local group-id : 0                 Remote group-id: 0
        p15 = re.compile(r'(^Local group-id\s+:\s+(?P<localgid>\d+|--)\s+'
                         r'Remote group-id:\s+(?P<remotegid>\d+$|--$))')

        # Tunnel LSP     : mlx8.1_to_ces.2 (tnl15)
        p16 = re.compile(r'(^Tunnel LSP\s+:\s+'
                         r'(?P<lspname>[^+\s]+)\s+\((?P<tunnel>\w+)\)$)')

        # LSPs assigned  : No LSPs assigned
        p17 = re.compile(r'(^LSPs\s+assigned\s+:\s+(?P<lsps>\w+.*$))')

        for line in out.splitlines():
            line = line.strip()

            # VLL VLL-TEST1, VC-ID 2456, VLL-INDEX 2
            m = p1.match(line)
            if m:
                vll_dict = result_dict.setdefault('vll', {}).setdefault(vll, {
                    'vcid': int(m.groupdict()['vcid']),
                    'vll_index': int(m.groupdict()['vllindex'])
                })
                continue

            # End-point: tagged vlan 2501 e 2/10
            # End-point: untagged e 2/2
            # End-point: tagged vlan 100 inner-vlan 45 e 2/1
            m = p2.match(line)
            if m:
                tag_type = m.groupdict()['type']

                interface_num = m.groupdict()['interface']
                interface_name = m.groupdict()['interface_name']
                expand_interface = interface_def.get(interface_name)

                vll_dict['local'] = {
                    'type': tag_type,
                    'interface': expand_interface + interface_num
                }

                if tag_type.lower() == 'tagged':
                    vlan_id = int(m.groupdict()['vid'])
                    inner_vlan = m.groupdict().get('innerid')
                    if inner_vlan is not None:
                        vll_dict['local']['outer_vlan_id'] = vlan_id
                        vll_dict['local']['inner_vlan_id'] = int(inner_vlan)
                    else:
                        vll_dict['local']['vlan_id'] = vlan_id

                continue

            # End-Point state  : Up
            m = p3.match(line)
            if m:
                local_state = m.groupdict()['state']
                vll_dict['local']['state'] = local_state
                continue

            # MCT state        : None
            m = p4.match(line)
            if m:
                mct_state = m.groupdict()['mctstate']
                vll_dict['local']['mct_state'] = mct_state
                continue

            # IFL-ID           : --
            # IFL-ID           : n/a
            # IFL-ID           : 1234
            m = p5.match(line)
            if m:
                ifl_id = m.groupdict()['iflid']
                vll_dict['local']['ifl_id'] = ifl_id
                continue

            # Local VC type    : tag
            # Local VC type : raw-pass-through
            m = p6.match(line)
            if m:
                vc_type = m.groupdict()['vctype']
                vll_dict['local']['vc_type'] = vc_type
                continue

            # Local VC MTU     : 9190
            m = p7.match(line)
            if m:
                mtu = m.groupdict()['mtu']
                if mtu == '--':
                    mtu = 0

                vll_dict['local']['mtu'] = int(mtu)
                continue

            # COS              : --
            m = p8.match(line)
            if m:
                vll_dict['local']['cos'] = m.groupdict()['cos']
                continue

            # Extended Counters: Enabled
            m = p9.match(line)
            if m:
                if m.groupdict()['extcounters'].lower() == 'enabled':
                    extcounters = True
                else:
                    extcounters = False

                vll_dict['local']['extended_counters'] = extcounters
                continue

            # Counter          : disabled
            m = p10.match(line)
            if m:
                if m.groupdict()['counter'].lower() == 'enabled':
                    counters = True
                else:
                    counters = False

                vll_dict['local']['counters'] = counters
                continue

            # Vll-Peer         : 192.168.1.1
            m = p11.match(line)
            if m:
                vll_dict['peer'] = {
                    'ip': m.groupdict()['ip']
                }
                continue

            # State          : UP
            # State          : DOWN - PW is Down (Reason:Wait for peer label)
            # For all states see page 550 in reference material
            m = p12.match(line)
            if m:
                state = m.groupdict()['state']
                reason = m.groupdict().get('reason')
                vll_dict['peer']['state'] = state

                if state.lower() == 'down':
                    vll_dict['peer']['reason'] = reason if reason is not None \
                            else 'Unknown'
                continue

            # Remote VC type : tag               Remote VC MTU  : 9190
            m = p13.match(line)
            if m:
                vc_type = m.groupdict()['vctype']
                mtu = m.groupdict()['mtu']
                if mtu == '--':
                    mtu = 0

                vll_dict['peer']['vc_type'] = vc_type
                vll_dict['peer']['mtu'] = int(mtu)
                continue

            # Local label    : 852217            Remote label   : 852417
            # Local label    : --                Remote label   : --
            m = p14.match(line)
            if m:
                local = m.groupdict()['local']
                remote = m.groupdict()['remote']

                if local == '--':
                    vll_dict['peer']['local_label'] = local
                else:
                    vll_dict['peer']['local_label'] = int(local)

                if remote == '--':
                    vll_dict['peer']['remote_label'] = remote
                else:
                    vll_dict['peer']['remote_label'] = int(remote)
                continue

            # Local group-id : 0                 Remote group-id: 0
            m = p15.match(line)
            if m:
                local = m.groupdict()['localgid']
                remote = m.groupdict()['remotegid']

                if local == '--':
                    vll_dict['peer']['local_group_id'] = local
                else:
                    vll_dict['peer']['local_group_id'] = int(local)

                if remote == '--':
                    vll_dict['peer']['remote_group_id'] = remote
                else:
                    vll_dict['peer']['remote_group_id'] = int(remote)
                continue

            # Tunnel LSP     : mlx8.1_to_ces.2 (tnl15)
            m = p16.match(line)
            if m:
                lsp = m.groupdict()['lspname']
                tunnel = m.groupdict().get('tunnel')

                if tunnel is not None:
                    vll_dict['peer']['tunnel_lsp'] = {
                        'name': lsp,
                        'tunnel_interface': tunnel
                    }
                else:
                    vll_dict['peer']['tunnel_lsp'] = {
                        'name': lsp
                    }
                continue

            # LSPs assigned  : No LSPs assigned
            m = p17.match(line)
            if m:
                vll_dict['peer']['lsps_assigned'] = m.groupdict()['lsps']
                continue

        return result_dict


# ======================================================
# Schema for 'show mpls vll-local {vll}'
# ======================================================
class ShowMPLSVLLLocalSchema(MetaParser):
    """Schema for show mpls vll {vll}"""
    schema = {
        'vll': {
            Any(): {
                'vll_id': int,
                'ifl_id': str,
                'state': str,
                Optional('reason'): str,
                'endpoint': {
                    1: {
                        'type': str,
                        Optional('vlan_id'): int,
                        'interface': str,
                        Optional('outer_vlan_id'): int,
                        Optional('inner_vlan_id'): int,
                        'cos': Or(int, str)
                    },
                    2: {
                        'type': str,
                        Optional('vlan_id'): int,
                        'interface': str,
                        Optional('outer_vlan_id'): int,
                        Optional('inner_vlan_id'): int,
                        'cos': Or(int, str)
                    }
                },
                Optional('extended_counters'): bool,
                Optional('counters'): bool
            }
        }
    }


# ====================================================
#  parser for 'show mpls vll-local {vll}'
# ====================================================
class ShowMPLSVLLLocal(ShowMPLSVLLLocalSchema):
    """
    Parser for show mpls vll-local {vll} on Devices running IronWare

    Reference Documenation -
        * https://resources.ditrapani.com.au/#!index.md#Vendor_Documentation

    """
    cli_command = 'show mpls vll-local {vll}'

    """
    VLL test-1 VLL-ID 1 IFL-ID --
        State: UP
        End-point 1: untagged e 2/2
        COS: --
        End-point 2: untagged e 2/13
        COS: --
        Extended Counters: Enabled
    """

    def cli(self, vll, output=None):
        if output is None:
            command = self.cli_command.format(vll=vll)
            out = self.device.execute(command)
        else:
            out = output

        result_dict = {}

        interface_def = {
            'e': 'ethernet'
        }

        # Vll test-4 VLL-ID 4 IFL-ID 4096
        p1 = re.compile(r'(^(VLL|vll|Vll)\s+(?P<name>[^\s]+)\s+VLL-ID\s+'
                        r'(?P<vllid>\d+)\s+IFL-ID\s+(?P<iflid>--$|\d+$))')

        # State: UP
        p2 = re.compile(r'(^State:\s+(?P<state>UP|DOWN)(\s+-\s+'
                        r'(?P<reason>configuration incomplete|'
                        r'endpoint port is down)|$))')

        # End-point 1: tagged vlan 2501 e 2/10
        # End-point 1: untagged e 2/2
        # End-point 1: tagged vlan 100 inner-vlan 45 e 2/1
        p3 = re.compile(r'(^End-point (?P<endpoint>1|2):\s+'
                        r'(?P<type>tagged|untagged|undefined)'
                        r'(\s+vlan\s+(?P<vid>\d+)|)(\s+inner-vlan\s+'
                        r'(?P<innerid>\d+)|)\s+(?P<interface_name>\w+)\s+'
                        r'(?P<interface>\d+\/\d+$))')

        # COS: 6
        p4 = re.compile(r'(^COS:\s+(?P<cos>--$|\d+$))')

        # Extended Counters: Enabled
        p5 = re.compile(r'(^Extended Counters:\s+'
                        r'(?P<extcounters>[e|E]nabled|[d|D]isabled)$)')

        # Counter          : disabled
        p6 = re.compile(r'(^Counter\s+:\s+'
                        r'(?P<counter>[e|E]nabled|[d|D]isabled)$)')

        for line in out.splitlines():
            line = line.strip()

            # Vll test-4 VLL-ID 4 IFL-ID 4096
            m = p1.match(line)
            if m:
                vll_dict = result_dict.setdefault('vll', {}).setdefault(vll, {
                    'vll_id': int(m.groupdict()['vllid']),
                    'ifl_id': m.groupdict()['iflid'],
                    'endpoint': {}
                })
                continue

            # State: UP
            m = p2.match(line)
            if m:
                state = m.groupdict()['state']
                vll_dict['state'] = state

                if state.lower() == 'down':
                    vll_dict['reason'] = m.groupdict().get('reason') if \
                            m.groupdict()['state'] is not None else 'Unknown'
                continue

            # End-point 1: tagged vlan 2501 e 2/10
            # End-point 1: untagged e 2/2
            # End-point 1: tagged vlan 100 inner-vlan 45 e 2/1
            m = p3.match(line)
            if m:
                port_type = m.groupdict()['type']
                endpoint_num = int(m.groupdict()['endpoint'])

                endpoint = {
                    'type': port_type
                }

                if port_type.lower() == 'tagged':
                    inner_vlan = m.groupdict().get('innerid')
                    if inner_vlan is not None:
                        endpoint['outer_vlan_id'] = int(m.groupdict()['vid'])
                        endpoint['inner_vlan_id'] = int(inner_vlan)
                    else:
                        endpoint['vlan_id'] = int(m.groupdict()['vid'])

                interface_num = m.groupdict()['interface']
                interface_name = m.groupdict()['interface_name']
                expand_interface = interface_def.get(interface_name)

                endpoint['interface'] = expand_interface + interface_num

                vll_dict['endpoint'][endpoint_num] = endpoint
                continue

            # COS: 6
            m = p4.match(line)
            if m:
                cos = m.groupdict()['cos']
                cos = int(cos) if cos != '--' else cos

                # Check if COS exists in endpoint_1
                if vll_dict['endpoint'][1].get('cos') is not None:
                    vll_dict['endpoint'][2]['cos'] = cos
                else:
                    vll_dict['endpoint'][1]['cos'] = cos
                continue

            # Extended Counters: Enabled
            m = p5.match(line)
            if m:
                if m.groupdict()['extcounters'].lower() == 'enabled':
                    extcounters = True
                else:
                    extcounters = False

                vll_dict['extended_counters'] = extcounters
                continue

            # Counter          : disabled
            m = p6.match(line)
            if m:
                if m.groupdict()['counter'].lower() == 'enabled':
                    counters = True
                else:
                    counters = False

                vll_dict['counters'] = counters
                continue

        return result_dict


# ======================================================
# Schema for 'show mpls ldp neighbor'
# ======================================================
class ShowMPLSLDPNeighborSchema(MetaParser):
    """Schema for show mpls ldp neighbor"""
    schema = {
        'neighbors': {
            Any(): {
                'interface': str,
                'ldp_id': str,
                'max_hold': int,
                'time_left': int
            }
        }
    }


# ====================================================
#  parser for 'show mpls ldp neighbor'
# ====================================================
class ShowMPLSLDPNeighbor(ShowMPLSLDPNeighborSchema):
    """
    Parser for show mpls ldp neighbor on Devices running IronWare
    """
    cli_command = 'show mpls ldp neighbor'

    """
    Nbr Transport Interface  Nbr LDP ID  Max Hold Time Left
    10.1.1.1      p4/1       10.1.1.1:0  15       14
    10.5.5.5      p3/2       10.5.5.5:0  15       11
    10.4.4.4      (targeted) 10.4.4.4:0  15       13
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        # 10.1.1.1      p4/1       10.1.1.1:0  15       14
        # 10.4.4.4      (targeted) 10.4.4.4:0  15       13
        p1 = re.compile(r'(^(?P<neighbor>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+'
                        r'(?P<int>\S+)\s+'
                        r'(?P<ldpid>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+)\s+'
                        r'(?P<hold>\d+)\s+(?P<time>\d+)$)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                neighbors_dict = result_dict.setdefault('neighbors', {})

                group = m.groupdict()
                neighbors_dict.setdefault(group['neighbor'], {
                    'interface': group['int'],
                    'ldp_id': group['ldpid'],
                    'max_hold': int(group['hold']),
                    'time_left': int(group['time'])
                })
                continue
        return result_dict
