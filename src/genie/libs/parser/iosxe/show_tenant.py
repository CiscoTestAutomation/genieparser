'''
*'show tenant-summary'
*'show tenant {tenant_name} omp peers'
*'show tenant {tenant_name} omp summary'
*'show tenant {tenant_name} omp routes advertised'
*'show tenant {tenant_name} omp routes vpn {vpnid} advertised'
'''

# Python
import re
# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional



class ShowTenantSummarySchema(MetaParser):
    ''' Schema for show tenant-summary'''
    schema = {
        'active_tenants_num': int,
        'max_tenants': int,
        'tenant_name': {
                Any(): {
                    'tenant_id': int,
                    'tenant_vpnid': int,
                    },
                }
            }

class ShowTenantSummary(ShowTenantSummarySchema):

    """ Parser for "show tenant-summary" """
    
    cli_command = "show tenant-summary"
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return_dict={}
        if out:
            localdict = {}
            return_dict['tenant_name'] = {}
            # tenant-summary max-tenants 24
            p1 = re.compile(r'^tenant-summary +max-tenants +(?P<max_tenants>[0-9]+)$')
            # tenant-summary num-active-tenants 20
            p2 = re.compile(r'^tenant-summary +num-active-tenants +(?P<active_tenants_num>[0-9]+)$')
            # Tenanttest12      2       1004
            # Tenanttest13      3       1005
            # apple             4       1006
            # grapes            5       1007
            # orange            6       1008
            p3 = re.compile(r'^(?P<tenant_name>[\w/\-\.]+) +(?P<tenant_id>[0-9]+) +(?P<tenant_vpnid>[0-9]+)$')
            outlist = out.splitlines()
            for lines in outlist:
                m1 = p1.match(lines.rstrip())
                m2 = p2.match(lines.rstrip())
                m3 = p3.match(lines.rstrip())
                if m1:
                    groups = m1.groupdict()
                    return_dict['max_tenants'] = int(groups['max_tenants'])
                if m2:
                    groups = m2.groupdict()
                    return_dict['active_tenants_num'] = int(groups['active_tenants_num'])
                if m3:
                    groups = m3.groupdict()
                    localdict['tenant_id'] = int(groups['tenant_id'])
                    localdict['tenant_vpnid'] = int(groups['tenant_vpnid'])
                    return_dict['tenant_name'][groups['tenant_name']] = {}
                    return_dict['tenant_name'][groups['tenant_name']] = localdict
        return return_dict


class ShowTenantOmpSummarySchema(MetaParser):
    ''' Schema for
        *'show tenant {tenant_name} omp summary'
    '''
    schema = {'tenant_name':
                  {Any(): {
                       'admin_state': str,
                       'alert_received': int,
                       'alert_sent': int,
                       'handshake_received': int,
                       'handshake_sent': int,
                       'hello_received': int,
                       'hello_sent': int,
                       'inform_received': int,
                       'inform_sent': int,
                       'mcast_routes_installed': int,
                       'mcast_routes_received': int,
                       'mcast_routes_sent': int,
                       'omp_uptime': str,
                       'oper_state': str,
                       'personality': str,
                       'policy_queue': int,
                       'policy_received': int,
                       'policy_sent': int,
                       'routes_installed': int,
                       'routes_received': int,
                       'routes_sent': int,
                       'services_installed': int,
                       'services_received': int,
                       'services_sent': int,
                       'tlocs_installed': int,
                       'tlocs_received': int,
                       'tlocs_sent': int,
                       'total_packets_received': int,
                       'total_packets_sent': int,
                       'update_received': int,
                       'update_sent': int,
                       'vedge_peers': int,
                       'vsmart_peers': int
                  }
             }
       }

class ShowTenantOmpSummary(ShowTenantOmpSummarySchema):

    """ Parser for "show tenant {tenant_name} omp summary" """

    cli_command = "show tenant {tenant_name} omp summary"
    def cli(self, tenant_name='',output=None):

        if output is None:
            # Build command
            if tenant_name:
                cmd = self.cli_command.format(tenant_name=tenant_name)
            out = self.device.execute(cmd)
        else:
            out = output

        return_dict = {}
        parsed_dict = {}
        if out:
            parsed_dict['tenant_name'] = {}
            parsed_dict['tenant_name'][tenant_name] = {}
            # oper-state             UP
            # admin-state            UP
            # personality            vsmart
            # omp-uptime             7:20:46:19
            # routes-received        130
            # routes-installed       0
            # routes-sent            166
            # tlocs-received         18
            # tlocs-installed        11
            # tlocs-sent             21
            # services-received      76
            # services-installed     44
            # services-sent          32
            # mcast-routes-received  0
            # mcast-routes-installed 0
            # mcast-routes-sent      0
            # hello-sent             181946
            # hello-received         182041
            # handshake-sent         51
            # handshake-received     51
            # alert-sent             40
            # alert-received         7
            # inform-sent            353
            # inform-received        353
            # update-sent            7693
            # update-received        3458
            # policy-sent            810
            # policy-received        0
            # total-packets-sent     190907
            # total-packets-received 185910
            # vsmart-peers           1
            # vedge-peers            3
            # policy-queue           0
            p1 = re.compile(r'^(?P<key>[\w/\-\.]+) +(?P<value>[0-9\w\:]+)$')
            outlist = out.splitlines()
            for lines in outlist:
                m1 = p1.match(lines)
                if m1:
                    groups = m1.groupdict()
                    if groups['key'] == 'admin-state':return_dict['admin_state'] = groups['value']
                    elif groups['key'] == 'omp-uptime':return_dict['omp_uptime'] = groups['value']
                    elif groups['key'] == 'oper-state':return_dict['oper_state'] = groups['value']
                    elif groups['key'] == 'personality':return_dict['personality'] = groups['value']
                    else:return_dict[groups['key'].replace('-', '_')] = int(groups['value'])
            parsed_dict['tenant_name'][tenant_name] = return_dict
        return parsed_dict


class ShowTenantOmpPeersSchema(MetaParser):
    ''' Schema for
        *'show tenant {tenant_name} omp peers'
    '''
    schema = {'tenant_name':
                  {Any():
                       {'peer':
                            {Any():
                                 {'domain_id': int,
                                  'overlay_id': int,
                                  'routes_installed': int,
                                  'routes_received': int,
                                  'routes_sent': int,
                                  'site_id': int,
                                  'state': str,
                                  'type': str,
                                  'uptime': str
                                  },
                            },
                       },
                  },
              }

class ShowTenantOmpPeers(ShowTenantOmpPeersSchema):

    """ Parser for "show tenant {tenant_name} omp peers" """

    cli_command = "show tenant {tenant_name} omp peers"
    def cli(self, tenant_name='',output=None):

        if output is None:
            # Build command
            if tenant_name:
                cmd = self.cli_command.format(tenant_name=tenant_name)
            out = self.device.execute(cmd)
        else:
            out = output

        return_dict = {}
        parsed_dict = {}
        if out:
            parsed_dict['tenant_name'] = {}
            parsed_dict['tenant_name'][tenant_name] = {}
            return_dict['peer'] = {}
            # 169.254.10.7     vsmart  1         1         26        up       0:21:24:40       114/0/114
            # 169.254.10.10    vedge   1         1         501       up       0:06:53:57       11/0/108
            # 169.254.10.11    vedge   1         1         503       up       0:21:39:37       84/0/33
            # 169.254.10.12    vedge   1         1         504       up       0:21:39:38       16/0/30
            # 169.254.10.26    vedge   1         1         506       up       0:21:39:37       8/0/70
            p1 = re.compile(r'^(?P<peer>[\d\.]+) +(?P<type>[0-9\w/\.]+) +(?P<domain_id>[\d]+) +(?P<overlay_id>[\d]+) +(?P<site_id>[\d]+) +(?P<state>[\w]+) +(?P<uptime>[\d\:]+) +(?P<ris>[\d/\.]+)$')
            outlist = out.splitlines()
            for lines in outlist:
                m1 = p1.match(lines)
                if m1:
                    groups = m1.groupdict()
                    new_dict = {}
                    a = groups['ris'].split('/')
                    new_dict['routes_received'] = int(a[0])
                    new_dict['routes_installed'] = int(a[1])
                    new_dict['routes_sent'] = int(a[-1])
                    new_dict['type'] = groups['type']
                    new_dict['domain_id'] = int(groups['domain_id'])
                    new_dict['site_id'] = int(groups['site_id'])
                    new_dict['overlay_id'] = int(groups['overlay_id'])
                    new_dict['state'] = groups['state']
                    new_dict['uptime'] = groups['uptime']
                    return_dict['peer'][groups['peer']] = new_dict
            parsed_dict['tenant_name'][tenant_name] = return_dict
        return parsed_dict


class ShowTenantOmpRoutesAdvertisedSchema(MetaParser):
    ''' Schema for
        *'show tenant {tenant_name} omp routes advertised'
        *'show tenant {tenant_name} omp routes vpn {vpnid} advertised'
    '''
    schema = {'vpn':
                  {Any():
                       {'prefix': list
                        }
                   }
              }

class ShowTenantOmpRoutesAdvertised(ShowTenantOmpRoutesAdvertisedSchema):
    """ Parser for
    "show tenant {tenant_name} omp routes advertised"
    """

    cli_command = "show tenant {tenant_name} omp routes advertised"
    def cli(self, tenant_name='',output=None):

        if output is None:
            # Build command
            if tenant_name:
                cmd = self.cli_command.format(tenant_name=tenant_name)
            out = self.device.execute(cmd)
        else:
            out = output
        return_dict ={}
        if out:
            return_dict['vpn'] = {}
            localdict = {}
            # 2      10.204.0.0/16
            # 2      10.60.0.0/16
            # 3      10.4.1.1/32
            # 3      10.4.1.2/32
            # 3      10.16.2.0/30
            # 3      10.16.3.2/32
            # 3      10.154.0.0/16
            # 3      10.204.3.0/24
            # 3      10.16.0.0/16
            # 3      10.94.0.0/16
            # 3      10.106.0.0/16
            # 3      10.120.0.0/16
            # 3      10.136.0.0/16
            # 4      10.204.4.0/24
            # 5      10.154.5.0/24
            # 1002   10.111.2.0/24
            # 1002   10.154.2.0/24
            # 1002   10.51.2.0/24
            p1 = re.compile(r'^(?P<vpn>[\d]+) +(?P<prefix>[0-9\w/\.]+)$')
            outlist = out.splitlines()
            for lines in outlist:
                m1 = p1.match(lines)
                if m1:
                    groups = m1.groupdict()
                    if groups['vpn'] not in localdict:
                        localdict[groups['vpn']] = {}
                        prefix_list = []
                        prefix_list.append(groups['prefix'])
                        localdict[groups['vpn']]['prefix'] = {}
                        localdict[groups['vpn']]['prefix'] = prefix_list
                    else:
                        prefix_list.append(groups['prefix'])
                        localdict[groups['vpn']]['prefix'] = prefix_list
                    return_dict['vpn'] = localdict
        return return_dict


class ShowTenantOmpRoutesVpnAdvertised(ShowTenantOmpRoutesAdvertisedSchema):
    """ Parser for
    "show tenant {tenant_name} omp routes vpn {vpnid} advertised"
    """

    cli_command = "show tenant {tenant_name} omp routes vpn {vpnid} advertised"

    def cli(self, tenant_name='', vpnid='', output=None):

        if output is None:
            # Build command
            if tenant_name and vpnid:
                cmd = self.cli_command.format(tenant_name=tenant_name, vpnid=vpnid)
            out = self.device.execute(cmd)
        else:
            out = output
        return_dict = {}
        if out:
            return_dict['vpn'] = {}
            localdict = {}
            # 1002   10.111.2.0/24
            # 1002   10.154.2.0/24
            # 1002   10.51.2.0/24
            p1 = re.compile(r'^(?P<vpn>[\d]+) +(?P<prefix>[0-9\w/\.]+)$')
            outlist = out.splitlines()
            for lines in outlist:
                m1 = p1.match(lines)
                if m1:
                    groups = m1.groupdict()
                    if groups['vpn'] not in localdict:
                        localdict[groups['vpn']] = {}
                        prefix_list = []
                        prefix_list.append(groups['prefix'])
                        localdict[groups['vpn']]['prefix'] = {}
                        localdict[groups['vpn']]['prefix'] = prefix_list
                    else:
                        prefix_list.append(groups['prefix'])
                        localdict[groups['vpn']]['prefix'] = prefix_list
                    return_dict['vpn'] = localdict
        return return_dict