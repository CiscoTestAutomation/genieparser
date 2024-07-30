"""show_ip_bgp.py

    * 'show ip bgp all'
    * 'show ip bgp {address_family} all'
    * 'show ip bgp'
    * 'show ip bgp {address_family}'
    * 'show ip bgp {address_family} rd {rd}'
    * 'show ip bgp {address_family} vrf {vrf}'
    * 'show ip bgp all detail'
    * 'show ip bgp {address_family} vrf {vrf} detail'
    * 'show ip bgp {address_family} rd {rd} detail'
    * 'show ip bgp summary'
    * 'show ip bgp {address_family} summary'
    * 'show ip bgp {address_family} vrf {vrf} summary'
    * 'show ip bgp {address_family} rd {rd} summary'
    * 'show ip bgp all summary'
    * 'show ip bgp {address_family} all summary'
    * 'show ip bgp regexp ^$'
    * 'show ip bgp all neighbors',
    * 'show ip bgp all neighbors {neighbor}'
    * 'show ip bgp {address_family} all neighbors'
    * 'show ip bgp {address_family} all neighbors {neighbor}'
    * 'show ip bgp neighbors'
    * 'show ip bgp neighbors {neighbor}'
    * 'show ip bgp {address_family} neighbors'
    * 'show ip bgp {address_family} neighbors {neighbor}'
    * 'show ip bgp {address_family} vrf {vrf} neighbors'
    * 'show ip bgp {address_family} vrf {vrf} neighbors {neighbor}'
    * 'show ip bgp all neighbors {neighbor} advertised-routes'
    * 'show ip bgp {address_family} all neighbors {neighbor} advertised-routes'
    * 'show ip bgp neighbors {neighbor} advertised-routes'
    * 'show ip bgp {address_family} neighbors {neighbor} advertised-routes'
    * 'show ip bgp all neighbors {neighbor} received-routes'
    * 'show ip bgp {address_family} all neighbors {neighbor} received-routes'
    * 'show ip bgp neighbors {neighbor} received-routes'
    * 'show ip bgp {address_family} neighbors {neighbor} received-routes'
    * 'show ip bgp all neighbors {neighbor} routes'
    * 'show ip bgp {address_family} all neighbors {neighbor} routes'
    * 'show ip bgp neighbors {neighbor} routes'
    * 'show ip bgp {address_family} neighbors {neighbor} routes'
    * 'show ip bgp {address_family} vrf {vrf} neighbors {neighbor} routes'
    * show ip bgp template peer-session
    * show ip bgp template peer-session {template_name}
    * show ip bgp template peer-policy
    * show ip bgp template peer-policy {template_name}
    * show ip bgp all dampening parameters
    * show ip bgp {address_family} rd {rd} neighbors {neighbor} advertised-routes
    * show ip bgp {address_family} vrf {vrf} {route}
    * show ip bgp {address_family} rd {rd} {route}
    * show ip bgp {address_family} vrf {vrf} neighbors {neighbor} advertised-routes
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# Parser
from genie.libs.parser.iosxe.show_vrf import ShowVrf
from genie.libs.parser.iosxe.show_bgp import *


# ======================================
# Parser for:
#   * 'show ip bgp all'
#   * 'show ip bgp {address_family} all'
# ======================================
class ShowIpBgpAll(ShowBgpSuperParser, ShowBgpSchema):

    ''' Parser for:
        * 'show ip bgp all'
        * 'show ip bgp {address_family} all'
    '''

    cli_command = ['show ip bgp {address_family} all',
                   'show ip bgp all',
                   ]

    def cli(self, address_family='', output=None):

        if output is None:
            # Build command
            if address_family:
                cmd = self.cli_command[0].format(address_family=address_family)
            else:
                cmd = self.cli_command[1]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, address_family=address_family)


# =============================================
# Parser for:
#   * 'show ip bgp {route}'
#   * 'show ip bgp {address_family}'
# =============================================
class ShowIpBgpRouteDistributer(MetaParser):
    ''' Parser for:
        * 'show ip bgp {route}'
        * 'show ip bgp {address_family}'
    '''
    cli_command = ['show ip bgp {route}', 
        'show ip bgp {address_family}']

    def cli(self, route=None, address_family=None, output=None):
        if route:
            cmd = self.cli_command[0].format(route=route)
        else:
            cmd = self.cli_command[1].format(address_family=address_family)
        
        if not output:
            output = self.device.execute(cmd)

        # show ip bgp 192.168.1.1
        if route or '.' in address_family:
            parser = ShowIpBgpAllDetail(self.device)
        # show ip bgp ipv4
        else:
            parser = ShowIpBgp(self.device)
        self.schema = parser.schema
        return parser.parse(output=output)

# =============================================
# Parser for:
#   * 'show ip bgp'
#   * 'show ip bgp {address_family}'
#   * 'show ip bgp {address_family} rd {rd}'
#   * 'show ip bgp {address_family} vrf {vrf}'
#   * 'show ip bgp regexp ^$'
# =============================================
class ShowIpBgp(ShowBgpSuperParser, ShowBgpSchema):

    ''' Parser for:
        * 'show ip bgp'
        * 'show ip bgp {address_family}'
        * 'show ip bgp {address_family} rd {rd}'
        * 'show ip bgp {address_family} vrf {vrf}'
        * 'show ip bgp regexp ^$'
    '''

    cli_command = ['show ip bgp {address_family} vrf {vrf}',
                   'show ip bgp {address_family} rd {rd}',
                   'show ip bgp',
                   'show ip bgp regexp {regexp}'
                   ]

    def cli(self, address_family='', rd='', vrf='', regexp='', output=None):

        if output is None:
            # Build command
            if address_family and vrf:
                cmd = self.cli_command[0].format(address_family=address_family,
                                                 vrf=vrf)
            elif address_family and rd:
                cmd = self.cli_command[1].format(address_family=address_family,
                                                 rd=rd)
            elif regexp:
                cmd = self.cli_command[3].format(regexp=regexp)
            else:
                cmd = self.cli_command[2]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, vrf=vrf,
                           address_family=address_family)

# =============================================
# Parser for:
#   * 'show ip bgp regexp {regexp}'
# =============================================
class ShowIpBgpRegexp(ShowBgpSuperParser, ShowBgpSchema):

    ''' Parser for:
        * 'show ip bgp regexp {regexp}'
    '''

    cli_command = 'show ip bgp regexp {regexp}'

    def cli(self, regexp, output=None):

        if output is None:
            cmd = self.cli_command.format(regexp=regexp)
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output)

# ====================================================
# Parser for:
#   * 'show ip bgp all detail'
#   * 'show ip bgp {address_family} vrf {vrf} {route}'
# ====================================================
class ShowIpBgpAllDetail(ShowBgpDetailSuperParser):

    ''' Parser for:
        * 'show ip bgp all detail'
        * 'show ip bgp {address_family} vrf {vrf} {route}'
    '''

    cli_command = ['show ip bgp all detail',
        'show ip bgp {address_family} vrf {vrf} {route}']

    def cli(self, address_family='', vrf='', route='',output=None):

        if output is None:
            if address_family and vrf and route:
                cmd = self.cli_command[1].format(address_family=address_family,
                    vrf=vrf, route=route)
            else:
                cmd = self.cli_command[0]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, address_family=address_family, vrf=vrf)

# ====================================================
# Parser for:
#   * 'show ip bgp {address_family} vrf {vrf} detail'
#   * 'show ip bgp {address_family} rd {rd} detail'
#   * 'show ip bgp {address_family} rd {rd} {route}'
# ====================================================
class ShowIpBgpDetail(ShowBgpDetailSuperParser, ShowBgpAllDetailSchema):

    ''' Parser for:
        * 'show ip bgp {address_family} vrf {vrf} detail'
        * 'show ip bgp {address_family} rd {rd} detail'
        * 'show ip bgp {address_family} rd {rd} {route}'
        * 'show ip bgp {address_family} all detail'
    '''

    cli_command = ['show ip bgp {address_family} vrf {vrf} detail',    
                   'show ip bgp {address_family} rd {rd} detail',
                   'show ip bgp {address_family} rd {rd} {route}',
                   'show ip bgp {address_family} all detail'
                   ]

    def cli(self, address_family='', vrf='', rd='', route='', output=None):

        # Init dict
        ret_dict = {}

        if output is None:
            if vrf:
                if address_family:
                    cmd = self.cli_command[0].format(address_family=address_family,
                                                 vrf=vrf)
                else:
                    return ret_dict
            elif rd:
                if address_family:
                    if route:
                        cmd = self.cli_command[2].format(address_family=address_family,
                                                     rd=rd, route=route)
                    else:
                        cmd = self.cli_command[1].format(address_family=address_family,
                                                 rd=rd)
                else:
                    return ret_dict   
            else:
                if address_family:
                    cmd = self.cli_command[3].format(address_family=address_family)
                else:
                    return ret_dict
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, vrf=vrf, rd=rd,
                           address_family=address_family)


# ====================================================
# Parser for:
#   * 'show ip bgp {address_family} detail'
#   * 'show ip bgp {address_family} evi {evi}'
#   * 'show ip bgp {address_family} route-type {rt}'
#   * 'show ip bgp {address_family} evi {evi} route-type {rt}'
# ====================================================
class ShowIpBgpL2VPNEVPN(ShowBgpDetailSuperParser, ShowBgpAllDetailSchema):
    ''' Parser for:
          * 'show ip bgp {address_family} detail'
          * 'show ip bgp {address_family} {evi} detail'
          * 'show ip bgp {address_family} route-type {rt}'
          * 'show ip bgp {address_family} evi {evi} route-type {rt}'
          * 'show ip bgp {address_family} route-type {rt} {esi} {eti} {mpls_label}'
          * 'show ip bgp {address_family} route-type {rt} {esi} {eti}'
          * 'show ip bgp {address_family} route-type {rt} {esi}'
          * 'show ip bgp {address_family} route-type {rt} {eti} {mac} {ip}'
          * 'show ip bgp {address_family} route-type {rt} {eti} {ip}'
          * 'show ip bgp {address_family} route-type {rt} {esi} {ip}'
          * 'show ip bgp {address_family} route-type {rt} {eti} {ip} {ip_len}'
          * 'show ip bgp {address_family} route-type {rt} {eti} {src_ip} {group_ip} {orig_ip}'
          * 'show ip bgp {address_family} route-type {rt} {esi} {eti} {src_ip} {group_ip} {orig_ip}'
          * 'show ip bgp {address_family} route-type {rt} {esi} {eti} {src_ip} {group_ip} {orig_ip} {lg_sync}'
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {eti} {mpls_label}', # RT1
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {eti}', # RT1
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {esi}', # RT1
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {eti} {mac} {ip}', # RT2
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {eti} {ip}', # RT3
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {ip}', # RT4 
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {eti} {ip} {ip_len}', # RT5 
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {eti} {src_ip} {group_ip} {orig_ip}', # RT6
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {eti} {src_ip} {group_ip} {orig_ip}', # RT7
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {eti} {src_ip} {group_ip} {orig_ip} {lg_sync}', # RT8
          * 'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {eti} {mac} {ip}'
    '''
    cli_command = ['show ip bgp {address_family} detail',
                    'show ip bgp {address_family} evi {evi} detail',
                    'show ip bgp {address_family} route-type {rt}',
                    'show ip bgp {address_family} evi {evi} route-type {rt}',
                    'show ip bgp {address_family} route-type {rt} {esi} {eti} {mpls_label}', # RT1
                    'show ip bgp {address_family} route-type {rt} {esi} {eti}', # RT1
                    'show ip bgp {address_family} route-type {rt} {esi}', # RT1
                    'show ip bgp {address_family} route-type {rt} {eti} {mac} {ip}', # RT2
                    'show ip bgp {address_family} route-type {rt} {eti} {ip}', # RT3
                    'show ip bgp {address_family} route-type {rt} {esi} {ip}', # RT4 
                    'show ip bgp {address_family} route-type {rt} {eti} {ip} {ip_len}', # RT5 
                    'show ip bgp {address_family} route-type {rt} {eti} {src_ip} {group_ip} {orig_ip}', # RT6
                    'show ip bgp {address_family} route-type {rt} {esi} {eti} {src_ip} {group_ip} {orig_ip}', # RT7
                    'show ip bgp {address_family} route-type {rt} {esi} {eti} {src_ip} {group_ip} {orig_ip} {lg_sync}', # RT8
                    'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {eti} {mpls_label}', # RT1
                    'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {eti}', # RT1
                    'show ip bgp {address_family} evi {evi} route-type {rt} {esi}', # RT1
                    'show ip bgp {address_family} evi {evi} route-type {rt} {eti} {mac} {ip}', # RT2
                    'show ip bgp {address_family} evi {evi} route-type {rt} {eti} {ip}', # RT3
                    'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {ip}', # RT4 
                    'show ip bgp {address_family} evi {evi} route-type {rt} {eti} {ip} {ip_len}', # RT5 
                    'show ip bgp {address_family} evi {evi} route-type {rt} {eti} {src_ip} {group_ip} {orig_ip}', # RT6
                    'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {eti} {src_ip} {group_ip} {orig_ip}', # RT7
                    'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {eti} {src_ip} {group_ip} {orig_ip} {lg_sync}', # RT8
                    'show ip bgp {address_family} evi {evi} route-type {rt} {esi} {eti} {mac} {ip}']

    def cli(self, address_family='', evi='', rt='', output=None, **kwargs):
        if output is None:
            if evi and rt:
                cmd = self.cli_command[3].format(address_family='l2vpn evpn', evi=evi, rt=rt)
            elif rt and not evi:
                cmd = self.cli_command[2].format(address_family='l2vpn evpn', rt=rt)
            elif not rt and evi:
                cmd = self.cli_command[1].format(address_family='l2vpn evpn', evi=evi)
            else:
                cmd = self.cli_command[0].format(address_family='l2vpn evpn')

            for arg in ['esi', 'eti', 'mac', 'mpls_label', 'ip', 'ip_len', 'src_ip', 'group_ip', 'orig_ip', 'lg_sync']:
                    if arg in kwargs and kwargs[arg]:
                        cmd += ' {}'.format(kwargs[arg])

            output = self.device.execute(cmd)

        show_output = output
        if evi and rt:
            return super().cli(address_family='l2vpn evpn', evi=evi, rt=rt, output=show_output)
        elif rt and not evi:
            return super().cli(address_family='l2vpn evpn', rt=rt, output=show_output)
        elif not rt and evi:
            return super().cli(address_family='l2vpn evpn', evi=evi, output=show_output)
        else:
            return super().cli(address_family='l2vpn evpn', output=show_output)

#-------------------------------------------------------------------------------

# =====================================================
# Parser for:
#   * 'show ip bgp summary'
#   * 'show ip bgp {address_family} summary'
#   * 'show ip bgp {address_family} vrf {vrf} summary'
#   * 'show ip bgp {address_family} rd {rd} summary'
# =====================================================
class ShowIpBgpSummary(ShowBgpSummarySuperParser, ShowBgpSummarySchema):

    ''' Parser for:
        * 'show ip bgp summary'
        * 'show ip bgp {address_family} summary'
        * 'show ip bgp {address_family} vrf {vrf} summary'
        * 'show ip bgp {address_family} rd {rd} summary'
    '''

    cli_command = ['show ip bgp {address_family} rd {rd} summary',
                   'show ip bgp {address_family} vrf {vrf} summary',
                   'show ip bgp {address_family} summary',
                   'show ip bgp summary',
                   ]

    exclude = ['msg_rcvd', 'msg_sent', 'up_down']
    
    def cli(self, address_family='', vrf='', rd='', output=None):

        cmd = ''
        if output is None:
            # Build command
            if address_family and rd:
                cmd = self.cli_command[0].format(address_family=address_family,
                                                 rd=rd)
            elif address_family and vrf:
                cmd = self.cli_command[1].format(address_family=address_family,
                                                 vrf=vrf)
            elif address_family:
                cmd = self.cli_command[2].format(address_family=address_family)
            else:   
                cmd = self.cli_command[3]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, vrf=vrf, rd=rd,
                           address_family=address_family, cmd=cmd)


# ===============================================
# Parser for:
#   * 'show ip bgp all summary'
#   * 'show ip bgp {address_family} all summary'
# ===============================================
class ShowIpBgpAllSummary(ShowBgpSummarySuperParser, ShowBgpSummarySchema):

    ''' Parser for:
        * 'show ip bgp all summary'
        * 'show ip bgp {address_family} all summary'
    '''

    cli_command = ['show ip bgp {address_family} all summary',
                   'show ip bgp all summary',
                   ]

    exclude = ['msg_rcvd', 'msg_sent', 'up_down']
    def cli(self, address_family='', output=None):

        cmd = ''
        if output is None:
            # Build command
            if address_family:
                cmd = self.cli_command[0].format(address_family=address_family)
            else:
                cmd = self.cli_command[1]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, address_family=address_family,
                          cmd=cmd)


# ==================================================================
# Parser for:
#   * 'show ip bgp all neighbors',
#   * 'show ip bgp all neighbors {neighbor}'
#   * 'show ip bgp {address_family} all neighbors'
#   * 'show ip bgp {address_family} all neighbors {neighbor}'
# ==================================================================
class ShowIpBgpAllNeighbors(ShowBgpNeighborSuperParser, ShowBgpAllNeighborsSchema):

    ''' Parser for:
        * 'show ip bgp all neighbors',
        * 'show ip bgp all neighbors {neighbor}'
        * 'show ip bgp {address_family} all neighbors'
        * 'show ip bgp {address_family} all neighbors {neighbor}'
    '''

    cli_command = ['show ip bgp all neighbors',
                   'show ip bgp all neighbors {neighbor}',
                   'show ip bgp {address_family} all neighbors',
                   'show ip bgp {address_family} all neighbors {neighbor}',
                   ]

    exclude = ['current_time', 'last_read', 'last_write', 'up_time', 'ackhold' , 'retrans', 'keepalives', 'total', 'total_data', 
                    'value', 'with_data', 'delrcvwnd', 'rcvnxt', 'rcvwnd', 'receive_idletime' , 'sent_idletime', 'sndnxt', 'snduna',
                    'uptime']

    def cli(self, neighbor='', address_family='', output=None):

        # Restricted address families
        restricted_list = ['ipv4 unicast', 'ipv6 unicast']

        # Init vars
        ret_dict = {}

        if output is None:
            # Select the command
            if address_family and neighbor:
                if address_family not in restricted_list:
                    cmd = self.cli_command[3].format(address_family=address_family, neighbor=neighbor)
                else:
                    return ret_dict
            elif address_family:
                if address_family not in restricted_list:
                    cmd = self.cli_command[2].format(address_family=address_family)
                else:
                    return ret_dict
            elif neighbor:
                cmd = self.cli_command[1].format(neighbor=neighbor)
            else:
                cmd = self.cli_command[0]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, neighbor=neighbor,
                           address_family=address_family)

# ===================================================================
# Parser for:
#   * 'show ip bgp neighbors'
#   * 'show ip bgp neighbors {neighbor}'
#   * 'show ip bgp {address_family} neighbors'
#   * 'show ip bgp {address_family} neighbors {neighbor}'
#   * 'show ip bgp {address_family} vrf {vrf} neighbors'
#   * 'show ip bgp {address_family} vrf {vrf} neighbors {neighbor}'
# ===================================================================
class ShowIpBgpNeighbors(ShowBgpNeighborSuperParser, ShowBgpAllNeighborsSchema):

    ''' Parser for:
        * 'show ip bgp neighbors'
        * 'show ip bgp neighbors {neighbor}'
        * 'show ip bgp {address_family} neighbors'
        * 'show ip bgp {address_family} neighbors {neighbor}'
        * 'show ip bgp {address_family} vrf {vrf} neighbors'
        * 'show ip bgp {address_family} vrf {vrf} neighbors {neighbor}'
    '''

    cli_command = ['show ip bgp {address_family} vrf {vrf} neighbors {neighbor}',
                   'show ip bgp {address_family} vrf {vrf} neighbors',
                   'show ip bgp {address_family} neighbors {neighbor}',
                   'show ip bgp {address_family} neighbors',
                   'show ip bgp neighbors {neighbor}',
                   'show ip bgp neighbors',
                   ]
    excude = ['current_time' , 'last_read' , 'last_write', 'up_time', 'ackhold', 'retrans', 'keepalives', 
                'total', 'total_data' , 'value', 'with_data', 'delrcvwnd', 'rcvnxt', 'rcvwnd'
                'receive_idletime', 'sent_idletime', 'sndnxt', 'snduna', 'uptime']

    def cli(self, neighbor='', address_family='', vrf='', output=None):

        # Restricted address families
        restricted_list = ['ipv4 unicast', 'ipv6 unicast', 'link-state link-state','l2vpn evpn']

        # Init vars
        ret_dict = {}

        if output is None:
            # Select the command
            if address_family and vrf and neighbor:
                if address_family not in restricted_list:
                    cmd = self.cli_command[0].\
                                        format(address_family=address_family,
                                               vrf=vrf, neighbor=neighbor)
                else:
                    return ret_dict
            elif address_family and vrf:
                if address_family not in restricted_list:
                    cmd = self.cli_command[1].\
                                        format(address_family=address_family,
                                               vrf=vrf)
                else:
                    return ret_dict
            elif address_family and neighbor:
                if address_family in restricted_list:
                    cmd = self.cli_command[2].format(address_family=address_family,
                                                     neighbor=neighbor)
                else:
                    return ret_dict
            elif address_family:
                if address_family in restricted_list:
                    cmd = self.cli_command[3].format(address_family=address_family)
                else:
                    return ret_dict
            elif neighbor:
                cmd = self.cli_command[4].format(neighbor=neighbor)
            else:
                cmd = self.cli_command[5]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, neighbor=neighbor, vrf=vrf,
                           address_family=address_family)


#-------------------------------------------------------------------------------


# =============================================================================
# Parser for:
#   * 'show ip bgp all neighbors {neighbor} advertised-routes'
#   * 'show ip bgp {address_family} all neighbors {neighbor} advertised-routes'
# =============================================================================
class ShowIpBgpAllNeighborsAdvertisedRoutes(ShowBgpNeighborsAdvertisedRoutesSuperParser, ShowBgpNeighborsAdvertisedRoutesSchema):

    ''' Parser for:
        * 'show ip bgp all neighbors {neighbor} advertised-routes'
        * 'show ip bgp {address_family} all neighbors {neighbor} advertised-routes'
    '''

    cli_command = ['show ip bgp {address_family} all neighbors {neighbor} advertised-routes',
                   'show ip bgp all neighbors {neighbor} advertised-routes',
                   ]

    def cli(self, neighbor, address_family='', output=None):

        if output is None:
            # Build command
            if address_family and neighbor:
                cmd = self.cli_command[0].format(address_family=address_family,
                                                 neighbor=neighbor)
            else:
                cmd = self.cli_command[1].format(neighbor=neighbor)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            if self.check_number_of_prefixes(output) == 0:
                return {}
            show_output = output

        # Call super
        return super().cli(output=show_output, neighbor=neighbor,
                           address_family=address_family)

    def check_number_of_prefixes(self, output):
        number_of_prefixes = re.compile(r'Total\s+number\s+of\s+prefixes\s+(?P<number_of_prefixes>\d+)\s*')
        m = number_of_prefixes.search(output)
        if not m:
            return 0
        return int(m["number_of_prefixes"])


# =================================================================================
# Parser for:
#   * 'show ip bgp neighbors {neighbor} advertised-routes'
#   * 'show ip bgp {address_family} neighbors {neighbor} advertised-routes'
#   * 'show ip bgp {address_family} rd {rd} neighbors {neighbor} advertised-routes'
#   * 'show ip bgp {address_family} vrf {vrf} neighbors {neighbor} advertised-routes'
# =================================================================================
class ShowIpBgpNeighborsAdvertisedRoutes(ShowBgpNeighborsAdvertisedRoutesSuperParser, ShowBgpNeighborsAdvertisedRoutesSchema):

    ''' Parser for:
        * 'show ip bgp neighbors {neighbor} advertised-routes'
        * 'show ip bgp {address_family} neighbors {neighbor} advertised-routes'
        * 'show ip bgp {address_family} rd {rd} neighbors {neighbor} advertised-routes'
        * 'show ip bgp {address_family} vrf {vrf} neighbors {neighbor} advertised-routes'
    '''

    cli_command = ['show ip bgp {address_family} neighbors {neighbor} advertised-routes',
                   'show ip bgp neighbors {neighbor} advertised-routes',
                   'show ip bgp {address_family} rd {rd} neighbors {neighbor} advertised-routes',
                   'show ip bgp {address_family} vrf {vrf} neighbors {neighbor} advertised-routes'
                   ]

    def cli(self, neighbor='', rd='', vrf='', address_family='', output=None):

        if output is None:
            # Build command
            if address_family and neighbor and rd:
                cmd = self.cli_command[2].format(address_family=address_family,
                    rd=rd, neighbor=neighbor)
            elif address_family and neighbor and vrf:
                cmd = self.cli_command[3].format(address_family=address_family,
                    vrf=vrf, neighbor=neighbor)
            elif address_family and neighbor:
                cmd = self.cli_command[0].format(address_family=address_family,
                                                 neighbor=neighbor)
            elif neighbor:
                cmd = self.cli_command[1].format(neighbor=neighbor)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, neighbor=neighbor,
                           address_family=address_family)




#-------------------------------------------------------------------------------


# ===========================================================================
# Parser for:
#   * 'show ip bgp all neighbors {neighbor} received-routes'
#   * 'show ip bgp {address_family} all neighbors {neighbor} received-routes'
# ===========================================================================
class ShowIpBgpAllNeighborsReceivedRoutes(ShowBgpNeighborsReceivedRoutesSuperParser, ShowBgpNeighborsReceivedRoutesSchema):

    ''' Parser for:
        * 'show ip bgp all neighbors {neighbor} received-routes'
        * 'show ip bgp {address_family} all neighbors {neighbor} received-routes'
    '''

    cli_command = ['show ip bgp {address_family} all neighbors {neighbor} received-routes',
                   'show ip bgp all neighbors {neighbor} received-routes',
                   ]

    def cli(self, neighbor, address_family='', output=None):

        if output is None:
            # Build command
            if address_family and neighbor:
                cmd = self.cli_command[0].format(address_family=address_family,
                                                 neighbor=neighbor)
            else:
                cmd = self.cli_command[1].format(neighbor=neighbor)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, neighbor=neighbor,
                           address_family=address_family)


# =======================================================================
# Parser for:
#   * 'show ip bgp neighbors {neighbor} received-routes'
#   * 'show ip bgp {address_family} neighbors {neighbor} received-routes'
# =======================================================================
class ShowIpBgpNeighborsReceivedRoutes(ShowBgpNeighborsReceivedRoutesSuperParser, ShowBgpNeighborsReceivedRoutesSchema):

    ''' Parser for:
        * 'show ip bgp neighbors {neighbor} received-routes'
        * 'show ip bgp {address_family} neighbors {neighbor} received-routes'
    '''

    cli_command = ['show ip bgp {address_family} neighbors {neighbor} received-routes',
                   'show ip bgp neighbors {neighbor} received-routes',
                   ]

    def cli(self, neighbor, address_family='', output=None):

        if output is None:
            # Build command
            if address_family and neighbor:
                cmd = self.cli_command[0].format(address_family=address_family,
                                                 neighbor=neighbor)
            elif neighbor:
                cmd = self.cli_command[1].format(neighbor=neighbor)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, neighbor=neighbor,
                           address_family=address_family)


#-------------------------------------------------------------------------------


# ==================================================================
# Parser for:
#   * 'show ip bgp all neighbors {neighbor} routes'
#   * 'show ip bgp {address_family} all neighbors {neighbor} routes'
# ==================================================================
class ShowIpBgpAllNeighborsRoutes(ShowBgpAllNeighborsRoutesSuperParser, ShowBgpAllNeighborsRoutesSchema):

    ''' Parser for:
        * 'show ip bgp all neighbors {neighbor} routes'
        * 'show ip bgp {address_family} all neighbors {neighbor} routes'
    '''

    cli_command = ['show ip bgp {address_family} all neighbors {neighbor} routes',
                   'show ip bgp all neighbors {neighbor} routes',
                   ]

    def cli(self, neighbor, address_family='', output=None):

        if output is None:
            # Build command
            if address_family and neighbor:
                cmd = self.cli_command[0].format(address_family=address_family,
                                                 neighbor=neighbor)
            else:
                cmd = self.cli_command[1].format(neighbor=neighbor)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, neighbor=neighbor,
                           address_family=address_family)


# ==============================================================
# Parser for:
#   * 'show ip bgp neighbors {neighbor} routes'
#   * 'show ip bgp {address_family} neighbors {neighbor} routes'
#   * 'show ip bgp {address_family} vrf {vrf} neighbors {neighbor} routes'
# ==============================================================
class ShowIpBgpNeighborsRoutes(ShowBgpAllNeighborsRoutesSuperParser, ShowBgpAllNeighborsRoutesSchema):

    ''' Parser for:
        * 'show ip bgp neighbors {neighbor} routes'
        * 'show ip bgp {address_family} neighbors {neighbor} routes'
        * 'show ip bgp {address_family} vrf {vrf} neighbors {neighbor} routes'
    '''

    cli_command = ['show ip bgp {address_family} vrf {vrf} neighbors {neighbor} routes',
                   'show ip bgp {address_family} neighbors {neighbor} routes',
                   'show ip bgp neighbors {neighbor} routes',
                   ]

    def cli(self, neighbor, address_family='', vrf='', output=None):

        if output is None:
            # Build command

            if address_family and vrf:
                cmd = self.cli_command[0].format(neighbor=neighbor, 
                                                 address_family=address_family, 
                                                 vrf=vrf)
            elif address_family:
                cmd = self.cli_command[1].format(neighbor=neighbor, 
                                                 address_family=address_family)
            else:
                cmd = self.cli_command[2].format(neighbor=neighbor)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, neighbor=neighbor,
                           address_family=address_family, vrf=vrf)


#-------------------------------------------------------------------------------


# =======================================================
# Schema for:
#   * 'show ip bgp template peer-session {template_name}'
# =======================================================
class ShowIpBgpTemplatePeerSessionSchema(MetaParser):

    ''' Schema "show ip bgp template peer-session {template_name}" '''

    schema = {
        'peer_session':
            {Any():
                {Optional('local_policies'): str ,
                Optional('inherited_polices'): str ,
                Optional('fall_over_bfd'): bool ,
                Optional('suppress_four_byte_as_capability'): bool,
                Optional('description'): str,
                Optional('disable_connected_check'): bool,
                Optional('ebgp_multihop_enable'): bool,
                Optional('ebgp_multihop_max_hop'): int,
                Optional('local_as_as_no'): int,
                Optional('password_text'): str,
                Optional('remote_as'): int,
                Optional('shutdown'): bool,
                Optional('keepalive_interval'): int,
                Optional('holdtime'): int,
                Optional('transport_connection_mode'): str,
                Optional('update_source'): str,
                Optional('index'): int,
                Optional('inherited_session_commands'):
                    {Optional('fall_over_bfd'): bool,
                    Optional('suppress_four_byte_as_capability'): bool,
                    Optional('description'): str,
                    Optional('disable_connected_check'): bool,
                    Optional('ebgp_multihop_enable'): bool,
                    Optional('ebgp_multihop_max_hop'): int,
                    Optional('local_as_as_no'): int,
                    Optional('password_text'): str,
                    Optional('remote_as'): int,
                    Optional('shutdown'): bool,
                    Optional('keepalive_interval'): int,
                    Optional('holdtime'): int,
                    Optional('transport_connection_mode'): str,
                    Optional('update_source'): str,
                    },
                },
            },
        }


# =======================================================
# Parser for:
#   * 'show ip bgp template peer-session {template_name}'
# =======================================================
class ShowIpBgpTemplatePeerSession(ShowIpBgpTemplatePeerSessionSchema):

    ''' Parser for "show ip bgp template peer-session {template_name}" '''

    cli_command = ['show ip bgp template peer-session {template_name}', 'show ip bgp template peer-session']

    def cli(self, template_name="", output=None):
        # show ip bgp template peer-session <WORD>
        if output is None:
            if template_name:
                cmd = self.cli_command[0].format(template_name=template_name)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        p1 = re.compile(r'^\s*Template:+(?P<template_id>[0-9\s\S\w]+),'
                        ' +index:(?P<index>[0-9]+)$')
        p2 = re.compile(r'^\s*Local +policies:+(?P<local_policies>0x[0-9A-F]+),'
                        ' +Inherited +polices:+(?P<inherited_polices>0x[0-9A-F]+)$')
        p3 = re.compile(r'^\s*Locally +configured +session +commands:$')
        p4 = re.compile(r'^\s*remote-as +(?P<remote_as>[0-9]+)$')
        p5 = re.compile(r'^\s*password +(?P<password_text>[\w\s]+)$')
        p6 = re.compile(r'^\s*shutdown$')
        p7 = re.compile(r'^\s*ebgp-multihop +(?P<ebgp_multihop_max_no>[0-9]+)$')
        p8 = re.compile(r'^\s*update-source +(?P<update_source>[\d\w]+)$')
        p9 = re.compile(r'^\s*transport +connection-mode +(?P<transport_connection_mode>[\s\w]+)$')
        p10 = re.compile(r'^\s*description +(?P<desc>[\d\S\s\w]+)$')
        p11 = re.compile(r'^\s*dont-capability-negotiate +four-octets-as$')
        p12 = re.compile(r'^\s*timers +(?P<keepalive_interval>[\d]+)'
                            ' +(?P<holdtime>[\d]+)$')
        p13 = re.compile(r'^\s*local-as +(?P<local_as_as_no>[\d]+)$')
        p14 = re.compile(r'^\s*disable-connected-check$')
        p15 = re.compile(r'^\s*fall-over +bfd$')
        p16 = re.compile(r'^\s*Inherited +session +commands:$')

        # Init vars
        parsed_dict = {}
        for line in out.splitlines():
            if line.strip():
                line = line.rstrip()
            else:
                continue
            # Template:PEER-SESSION, index:1
            m = p1.match(line)
            if m:
                template_id = m.groupdict()['template_id']
                index = int(m.groupdict()['index'])

                if 'peer_session' not in parsed_dict:
                    parsed_dict['peer_session'] = {}

                if template_id not in parsed_dict['peer_session']:
                    parsed_dict['peer_session'][template_id] = {}

                parsed_dict['peer_session'][template_id]['index'] = index
                continue

            # Local policies:0x5025FD, Inherited polices:0x0
            m = p2.match(line)
            if m:
                local_policy = m.groupdict()['local_policies']
                inherited_policy = m.groupdict()['inherited_polices']
                parsed_dict['peer_session'][template_id]['local_policies'] = local_policy
                parsed_dict['peer_session'][template_id]['inherited_polices'] = inherited_policy
                continue

            # Locally configured session commands:
            m = p3.match(line)
            if m:
                flag = False
                continue

            # remote-as 321
            m = p4.match(line)
            if m:
                remote_as = int(m.groupdict()['remote_as'])
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']['remote_as'] = remote_as
                else:
                    parsed_dict['peer_session'][template_id]['remote_as'] = remote_as
                continue

            # password is configured
            m = p5.match(line)
            if m:
                password_text = m.groupdict()['password_text']
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['password_text'] = password_text
                else:
                    parsed_dict['peer_session'][template_id]['password_text'] = password_text
                continue

            # shutdown
            m = p6.match(line)
            if m:
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] \
                        ['shutdown'] = True
                else:
                    parsed_dict['peer_session'][template_id]['shutdown'] = True
                continue

            # ebgp-multihop 254
            m = p7.match(line)
            if m:
                ebgp_multihop_max_no = int(m.groupdict()['ebgp_multihop_max_no'])
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] \
                        ['ebgp_multihop_max_hop'] = ebgp_multihop_max_no
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] \
                            ['ebgp_multihop_enable'] = True
                else:
                    parsed_dict['peer_session'][template_id]['ebgp_multihop_max_hop'] = ebgp_multihop_max_no
                    parsed_dict['peer_session'][template_id]['ebgp_multihop_enable'] = True
                continue

            # update-source Loopback0
            m = p8.match(line)
            if m:
                update_source = m.groupdict()['update_source']
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['update_source'] = update_source
                else:
                    parsed_dict['peer_session'][template_id]['update_source'] = update_source
                continue
            # transport connection-mode passive
            m = p9.match(line)
            if m:
                transport_connection_mode = m.groupdict()['transport_connection_mode']
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] \
                        ['transport_connection_mode'] = transport_connection_mode
                else:
                    parsed_dict['peer_session'][template_id]['transport_connection_mode'] \
                        = transport_connection_mode
                continue

            # description desc1!
            m = p10.match(line)
            if m:
                description = m.groupdict()['desc']
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] \
                        ['description'] = description
                else:
                    parsed_dict['peer_session'][template_id]['description'] \
                        = description
                continue

            # dont-capability-negotiate four-octets-as
            m = p11.match(line)
            if m:
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['suppress_four_byte_as_capability'] = True
                else:
                    parsed_dict['peer_session'][template_id]['suppress_four_byte_as_capability'] \
                        = True
                continue
            # timers 10 30
            m = p12.match(line)
            if m:
                keepalive_interval = int(m.groupdict()['keepalive_interval'])
                holdtime = int(m.groupdict()['holdtime'])
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['keepalive_interval'] = keepalive_interval
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']['holdtime'] \
                        = holdtime
                else:
                    parsed_dict['peer_session'][template_id]['keepalive_interval'] \
                        = keepalive_interval
                    parsed_dict['peer_session'][template_id]['holdtime'] \
                        = holdtime
                continue

            # local-as 255
            m = p13.match(line)
            if m:
                local_as_as_no = int(m.groupdict()['local_as_as_no'])
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['local_as_as_no'] = local_as_as_no
                else:
                    parsed_dict['peer_session'][template_id]['local_as_as_no'] = local_as_as_no

                continue

            # disable-connected-check
            m = p14.match(line)
            if m:
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['disable_connected_check'] = True
                else:
                    parsed_dict['peer_session'][template_id]['disable_connected_check'] = True
                continue

            # fall-over bfd
            m = p15.match(line)
            if m:
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['fall_over_bfd'] = True
                else:
                    parsed_dict['peer_session'][template_id]['fall_over_bfd'] = True
                continue

            # Inherited session commands:
            m = p16.match(line)
            if m:
                if 'inherited_session_commands' not in parsed_dict['peer_session'][template_id]:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] = {}
                    flag = True
                continue

        if parsed_dict:
            for key, value in  parsed_dict['peer_session'].items():
                if 'inherited_session_commands' in parsed_dict['peer_session'][key]:
                    if not len(parsed_dict['peer_session'][key]['inherited_session_commands']):
                        del parsed_dict['peer_session'][key]['inherited_session_commands']
        return parsed_dict


#-------------------------------------------------------------------------------


# ======================================================
# Schema for:
#   * 'show ip bgp template peer-policy {template_name}'
# ======================================================
class ShowIpBgpTemplatePeerPolicySchema(MetaParser):

    ''' Schema for "show ip bgp template peer-policy {template_name}" '''

    schema = {
        'peer_policy':
            {Any():
                {Optional('local_policies'): str,
                Optional('inherited_polices'): str,
                Optional('local_disable_policies'): str,
                Optional('inherited_disable_polices'): str,
                Optional('allowas_in'): bool ,
                Optional('allowas_in_as_number'): int,
                Optional('as_override'): bool,
                Optional('default_originate'): bool,
                Optional('default_originate_route_map'): str,
                Optional('route_map_name_in'): str,
                Optional('route_map_name_out'): str,
                Optional('maximum_prefix_max_prefix_no'): int,
                Optional('maximum_prefix_threshold'): int,
                Optional('maximum_prefix_restart'): int,
                Optional('maximum_prefix_warning_only'): bool,
                Optional('next_hop_self'): bool,
                Optional('route_reflector_client'): bool,
                Optional('send_community'): str,
                Optional('soft_reconfiguration'): bool,
                Optional('soo'): str,
                Optional('index'): int,
                Optional('inherited_policies'):
                    {Optional('allowas_in'): bool,
                    Optional('allowas_in_as_number'): int,
                    Optional('as_override'): bool,
                    Optional('default_originate'): bool,
                    Optional('default_originate_route_map'): str,
                    Optional('route_map_name_in'): str,
                    Optional('route_map_name_out'): str,
                    Optional('maximum_prefix_max_prefix_no'): int,
                    Optional('maximum_prefix_threshold'): int,
                    Optional('maximum_prefix_restart'): int,
                    Optional('maximum_prefix_warning_only'): bool,
                    Optional('next_hop_self'): bool,
                    Optional('route_reflector_client'): bool,
                    Optional('send_community'): str,
                    Optional('soft_reconfiguration'): bool,
                    Optional('soo'): str,
                    },
                },
            },
        }


# ======================================================
# Parser for:
#   * 'show ip bgp template peer-policy {template_name}'
# ======================================================
class ShowIpBgpTemplatePeerPolicy(ShowIpBgpTemplatePeerPolicySchema):

    ''' Parser for "show ip bgp template peer-policy {template_name}" '''

    cli_command = ['show ip bgp template peer-policy {template_name}', 'show ip bgp template peer-policy']

    def cli(self, template_name="", output=None):
        # show ip bgp template peer-policy <WORD>
        if output is None:
            if template_name:
                cmd = self.cli_command[0].format(template_name=template_name)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        p1 = re.compile(r'^\s*Template:+(?P<template_id>[0-9\s\S\w]+),'
                        ' +index:(?P<index>[0-9]+).$')
    
        p2 = re.compile(r'^\s*Local +policies:+(?P<local_policies>0x[0-9A-F]+),'
                        ' +Inherited +polices:+(?P<inherited_polices>0x[0-9A-F]+)$')
    
        p3 = re.compile(r'^\s*Local +disable +policies:+(?P<local_disable_policies>0x[0-9A-F]+),'
                        ' +Inherited +disable +policies:+(?P<inherited_disable_polices>0x[0-9A-F]+)$')
    
        p4 = re.compile(r'^\s*Locally +configured +policies:$')
    
        p5 = re.compile(r'^\s*route-map +(?P<remote_map_in>[0-9a-zA-Z]+) +in$')
    
        p6 = re.compile(r'^\s*route-map +(?P<route_map_out>[0-9a-zA-Z]+) +out$')
    
        p7 = re.compile(r'^\s*default-originate +route-map'
                        ' +(?P<default_originate_route_map>[0-9a-zA-Z]+)$')
    
        p8 = re.compile(r'^\s*soft-reconfiguration'
                        ' +(?P<soft_reconfiguration>[a-zA-Z]+)$')
    
        p9 = re.compile(r'^\s*maximum-prefix'
                        ' +(?P<maximum_prefix_max_prefix_no>[0-9]+)'
                        ' ?(?P<maximum_prefix_threshold>[0-9]+)?'
                        ' +restart +(?P<maximum_prefix_restart>[0-9]+)$')
    
        p10 = re.compile(r'^\s*as-override$')
    
        p11 = re.compile(r'^\s*allowas-in +(?P<allowas_in_as_number>[0-9]+)$')
    
        p12 = re.compile(r'^\s*route-reflector-client$')
    
        p13 = re.compile(r'^\s*next-hop-self$')
    
        p14 = re.compile(r'^\s*send-community +(?P<send_community>[\w]+)$')
    
        p15 = re.compile(r'^\s*soo +(?P<soo>[\w\:\d]+)$')
    
        p16 = re.compile(r'^\s*Inherited policies:$')

        # Init vars
        parsed_dict = {}

        for line in out.splitlines():
            if line.strip():
                line = line.rstrip()
            else:
                continue
            # Template:PEER-POLICY, index:1.
            m = p1.match(line)
            if m:
                template_id = m.groupdict()['template_id']
                index = int(m.groupdict()['index'])

                if 'peer_policy' not in parsed_dict:
                    parsed_dict['peer_policy'] = {}

                if template_id not in parsed_dict['peer_policy']:
                    parsed_dict['peer_policy'][template_id] = {}

                parsed_dict['peer_policy'][template_id]['index'] = index
                continue

            # Local policies:0x8002069C603, Inherited polices:0x0
            m = p2.match(line)
            if m:
                local_policy = m.groupdict()['local_policies']
                inherited_policy = m.groupdict()['inherited_polices']

                parsed_dict['peer_policy'][template_id]['local_policies'] = local_policy
                parsed_dict['peer_policy'][template_id]['inherited_polices'] = inherited_policy
                continue

            # Local disable policies:0x0, Inherited disable policies:0x0
            m = p3.match(line)
            if m:
                local_policy = m.groupdict()['local_disable_policies']
                inherited_policy = m.groupdict()['inherited_disable_polices']
                parsed_dict['peer_policy'][template_id]['local_disable_policies'] = local_policy
                parsed_dict['peer_policy'][template_id]['inherited_disable_polices'] = inherited_policy
                continue

            #Locally configured policies:
            m = p4.match(line)
            if m:
                flag = False
                continue

            # route-map test in
            m = p5.match(line)
            if m:
                route_map_in = m.groupdict()['remote_map_in']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies'] \
                        ['route_map_name_in'] = route_map_in
                else:
                    parsed_dict['peer_policy'][template_id]['route_map_name_in'] = route_map_in
                continue

            # route-map test2 out
            m = p6.match(line)
            if m:
                route_map_out = m.groupdict()['route_map_out']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']\
                        ['route_map_name_out'] = route_map_out
                else:
                    parsed_dict['peer_policy'][template_id]['route_map_name_out'] = route_map_out
                continue

            # default-originate route-map test
            m = p7.match(line)
            if m:
                default_originate_route_map = m.groupdict()['default_originate_route_map']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']\
                        ['default_originate'] = True
                    parsed_dict['peer_policy'][template_id]['inherited_policies']\
                        ['default_originate_route_map'] = default_originate_route_map
                else:
                    parsed_dict['peer_policy'][template_id]['default_originate'] = True
                    parsed_dict['peer_policy'][template_id]['default_originate_route_map'] = \
                        default_originate_route_map
                continue

            # soft-reconfiguration inbound
            m = p8.match(line)
            if m:
                default_originate = m.groupdict()['soft_reconfiguration']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['soft_reconfiguration'] \
                        = True
                else:
                    parsed_dict['peer_policy'][template_id]['soft_reconfiguration'] \
                    = True
                continue

            # maximum-prefix 5555 70 restart 300
            m = p9.match(line)
            if m:
                maximum_prefix_max_prefix_no = int(m.groupdict()['maximum_prefix_max_prefix_no'])
                maximum_prefix_restart = int(m.groupdict()['maximum_prefix_restart'])
                maximum_prefix_threshold = m.groupdict()['maximum_prefix_threshold']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['maximum_prefix_max_prefix_no'] \
                        = maximum_prefix_max_prefix_no
                    if maximum_prefix_threshold:
                        parsed_dict['peer_policy'][template_id]['inherited_policies']['maximum_prefix_threshold'] \
                            = int(maximum_prefix_threshold)

                    parsed_dict['peer_policy'][template_id]['inherited_policies']['maximum_prefix_restart'] \
                        = maximum_prefix_restart
                else:
                    parsed_dict['peer_policy'][template_id]['maximum_prefix_max_prefix_no'] \
                        = maximum_prefix_max_prefix_no
                    if maximum_prefix_threshold:
                        parsed_dict['peer_policy'][template_id]['maximum_prefix_threshold'] \
                            = int(maximum_prefix_threshold)

                    parsed_dict['peer_policy'][template_id]['maximum_prefix_restart'] \
                        = maximum_prefix_restart
                continue

            # as-override
            m = p10.match(line)
            if m:
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['as_override'] = True
                else:
                    parsed_dict['peer_policy'][template_id]['as_override'] = True
                continue

            # allowas-in 9
            m = p11.match(line)
            if m:
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['allowas_in'] = True
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['allowas_in_as_number'] = \
                         int(m.groupdict()['allowas_in_as_number'])
                else:
                    parsed_dict['peer_policy'][template_id]['allowas_in'] = True
                    parsed_dict['peer_policy'][template_id]['allowas_in_as_number'] = \
                        int(m.groupdict()['allowas_in_as_number'])
                continue

            # route-reflector-client
            m = p12.match(line)
            if m:
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']\
                        ['route_reflector_client'] = True
                else:
                    parsed_dict['peer_policy'][template_id]['route_reflector_client'] = True
                continue

            # next-hop-self
            m = p13.match(line)
            if m:
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['next_hop_self'] = True
                else:
                    parsed_dict['peer_policy'][template_id]['next_hop_self'] = True
                continue

            # send-community both
            m = p14.match(line)
            if m:
                send_community = m.groupdict()['send_community']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']\
                        ['send_community'] = send_community
                else:
                    parsed_dict['peer_policy'][template_id]['send_community'] = send_community
                continue

            # soo SoO:100:100
            m = p15.match(line)
            if m:
                soo = m.groupdict()['soo']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['soo'] = soo
                else:
                    parsed_dict['peer_policy'][template_id]['soo'] = soo
                continue
            # Inherited policies:
            m = p16.match(line)
            if m:
                if 'inherited_policies' not in parsed_dict['peer_policy'][template_id]:
                    parsed_dict['peer_policy'][template_id]['inherited_policies'] = {}
                    flag = True

                continue

        if parsed_dict:
            for key, value in parsed_dict['peer_policy'].items():
                if 'inherited_policies' in parsed_dict['peer_policy'][key]:
                    if not len(parsed_dict['peer_policy'][key]['inherited_policies']):
                        del parsed_dict['peer_policy'][key]['inherited_policies']

        return parsed_dict


#-------------------------------------------------------------------------------


# ==========================================
# Schema for:
#   * 'show ip bgp all dampening parameters'
# ==========================================
class ShowIpBgpAllDampeningParametersSchema(MetaParser):

    ''' Schema for "show ip bgp all dampening parameters" '''

    schema = {
        'vrf':
            {Any():
                 {Optional('address_family'):
                    {Any():
                        {Optional('dampening'): bool,
                        Optional('dampening_decay_time'): int,
                        Optional('dampening_half_life_time'): int,
                        Optional('dampening_reuse_time'): int,
                        Optional('dampening_max_suppress_penalty'): int,
                        Optional('dampening_suppress_time'): int,
                        Optional('dampening_max_suppress_time'): int,
                        },
                    },
                },
            },
        }


# ==========================================
# Parser for:
#   * 'show ip bgp all dampening parameters'
# ==========================================
class ShowIpBgpAllDampeningParameters(ShowIpBgpAllDampeningParametersSchema):

    ''' Parser for "show ip bgp all dampening parameters" '''

    cli_command = 'show ip bgp all dampening parameters'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        p1 = re.compile(r'^\s*For +address +family:'
                        ' +(?P<address_family>[a-zA-Z0-9\-\s]+)$')

        p2 = re.compile(r'^\s*dampening'
                        ' +(?P<dampening_val>[\d\s\S]+)$')

        p3 = re.compile(r'^\s*Half-life +time\s*:'
                        ' +(?P<half_life_time>[\d]+)'
                        ' mins +Decay +Time +: +(?P<decay_time>[\d]+) +secs$')

        p4 = re.compile(r'^\s*Max +suppress +penalty:'
                        '\s+(?P<max_suppress_penalty>[0-9]+)'
                        '\s+Max +suppress +time:\s+(?P<max_suppress_time>[\d]+) +mins$')

        p5 = re.compile(r'^\s*Suppress +penalty +:'
                        ' +(?P<suppress_penalty>[\d]+)'
                        ' +Reuse +penalty +: +(?P<reuse_penalty>[\d]+)$')

        p6 = re.compile(r'^\s*% +dampening +not +enabled +for +base$')

        p7 = re.compile(r'^\s*For +vrf: +(?P<vrf_name>[\w\d]+)$')

        p8 = re.compile(r'^\s*% +dampening +not +enabled +for +vrf +(?P<vrf_name>[\d\w]+)$')
            
        # Init vars
        parsed_dict = {}
        vrf_name = 'default'

        for line in out.splitlines():
            if line.strip():
                line = line.rstrip()
            else:
                continue

            # For address family: IPv4 Unicast
            m = p1.match(line)
            if m:
                af_name = m.groupdict()['address_family'].lower()
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}
                continue

            # dampening 35 200 200 70
            m = p2.match(line)
            if m:
                dampening_val = m.groupdict()['dampening_val']
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}

                parsed_dict['vrf'][vrf_name]['address_family'][af_name]['dampening'] = True
                continue

            # Half-life time      : 35 mins       Decay Time       : 4200 secs
            m = p3.match(line)
            if m:
                half_life_time = int(m.groupdict()['half_life_time'])*60
                decay_time = int(m.groupdict()['decay_time'])
                parsed_dict['vrf'][vrf_name]['address_family'][af_name]\
                    ['dampening_half_life_time'] = half_life_time
                parsed_dict['vrf'][vrf_name]['address_family'][af_name] \
                    ['dampening_decay_time'] = decay_time
                continue

            # Max suppress penalty:   800         Max suppress time: 70 mins
            m = p4.match(line)
            if m:
                max_suppress_penalty = int(m.groupdict()['max_suppress_penalty'])
                max_suppress_time = int(m.groupdict()['max_suppress_time'])*60
                parsed_dict['vrf'][vrf_name]['address_family'][af_name] \
                    ['dampening_max_suppress_penalty'] = max_suppress_penalty
                parsed_dict['vrf'][vrf_name]['address_family'][af_name] \
                    ['dampening_max_suppress_time'] = max_suppress_time
                continue

            # Suppress penalty :   200         Reuse penalty : 200
            m = p5.match(line)
            if m:
                suppress_penalty = int(m.groupdict()['suppress_penalty'])
                reuse_time = int(m.groupdict()['reuse_penalty'])
                parsed_dict['vrf'][vrf_name]['address_family'][af_name] \
                    ['dampening_suppress_time'] = suppress_penalty
                parsed_dict['vrf'][vrf_name]['address_family'][af_name]\
                    ['dampening_reuse_time'] = reuse_time
                continue

            # % dampening not enabled for base
            m = p6.match(line)
            if m:
                continue

            # For vrf: VRF1
            m = p7.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                continue

            # % dampening not enabled for vrf VRF1
            m = p8.match(line)
            if m:
                continue

        if parsed_dict:
            for vrf_name in parsed_dict['vrf'].keys():
                if 'address_family' in parsed_dict['vrf'][vrf_name]:
                    for i in parsed_dict['vrf'][vrf_name]['address_family'].copy():
                        if not parsed_dict['vrf'][vrf_name]['address_family'][i]:
                            parsed_dict['vrf'][vrf_name]['address_family'].pop(i)

            for vrf_name in parsed_dict['vrf'].keys():
                for i in parsed_dict['vrf'][vrf_name].copy():
                    if not parsed_dict['vrf'][vrf_name][i]:
                        parsed_dict['vrf'][vrf_name].pop(i)

            for i in parsed_dict['vrf'].copy():
                if not parsed_dict['vrf'][i]:
                    parsed_dict['vrf'].pop(i)

            for i in parsed_dict.copy():
                if not parsed_dict[i]:
                    parsed_dict.pop(i)

        return parsed_dict


#-------------------------------------------------------------------------------

# ===============================================
# Parser for:
#   * 'show ip bgp {address_family} mdt vrf {vrf}'
# ===============================================

class ShowIpBgpMdtVrf(ShowBgpSuperParser, ShowBgpSchema):
    ''' Parser for
        show ip bgp {address_family} mdt vrf {vrf}
    '''

    cli_command = 'show ip bgp {address_family} mdt vrf {vrf}'

    def cli(self, output=None, address_family='', vrf=''):
        if output is None:
            output = self.device.execute(self.cli_command.format(address_family=address_family, vrf=vrf))

        # Call Super
        return super().cli(output=output, address_family=address_family, vrf=vrf)

