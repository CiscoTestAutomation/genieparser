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
        'active_tenants_num': str,
        'max_tenants': str,
        'tenant_name': {
                Any(): {
                    'tenant_id': str,
                    'tenant_name': str,
                    'tenant_vpnid': str,
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
            localdict={}
            return_dict['tenant_name']={}
            #tenant-summary max-tenants 24
            p1=re.compile(r'^tenant-summary +max-tenants +(?P<max_tenants>[0-9]+)$')
            #tenant-summary num-active-tenants 20
            p2=re.compile(r'^tenant-summary +num-active-tenants +(?P<active_tenants_num>[0-9]+)$')
            # Tenanttest12      2       1004
            # Tenanttest13      3       1005
            # apple             4       1006
            # grapes            5       1007
            # orange            6       1008
            p3=re.compile(r'^(?P<tenant_name>[\w/\-\.]+) +(?P<tenant_id>[0-9]+) +(?P<tenant_vpnid>[0-9]+)$')
            outlist=out.splitlines()
            for lines in outlist:
                m1=p1.match(lines.rstrip())
                m2=p2.match(lines.rstrip())
                m3=p3.match(lines.rstrip())
                if m1:
                    groups=m1.groupdict()
                    return_dict.update(groups)
                if m2:
                    groups=m2.groupdict()
                    return_dict.update(groups)
                if m3:
                    groups=m3.groupdict()
                    localdict[groups['tenant_name'].strip()] = groups
                    return_dict['tenant_name'].update(localdict)    
        return return_dict        


class ShowTenantOmpSummarySchema(MetaParser):
    ''' Schema for 
        *'show tenant {tenant_name} omp summary'
    '''
    schema = {
        Any(): str,
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

        return_dict={}
        if out:
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
            p1=re.compile(r'^(?P<key>[\w/\-\.]+) +(?P<value>[0-9\w\:]+)$')
            outlist= out.splitlines()
            for lines in outlist:
                m1=p1.match(lines.rstrip())
                if m1:
                    groups=m1.groupdict()
                    return_dict[groups['key']] = groups['value']
        return return_dict


class ShowTenantOmpPeersSchema(MetaParser):
    ''' Schema for 
        *'show tenant {tenant_name} omp peers'
    '''
    schema = {'peer': {
        Any(): {
            'domain_id': str,
            'overlay_id': str,
            'peer': str,
            'routes_installed': str,
            'routes_received': str,
            'routes_sent': str,
            'site_id': str,
            'state': str,
            'type': str,
            'uptime': str,
            },
        }
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

        return_dict={}
        if out:
            return_dict['peer'] = {}
            #169.254.10.7     vsmart  1         1         26        up       0:21:24:40       114/0/114
            p1=re.compile(r'^(?P<peer>[\d\.]+) +(?P<type>[0-9\w/\.]+) +(?P<domain_id>[\d]+) +(?P<overlay_id>[\d]+) +(?P<site_id>[\d]+) +(?P<state>[\w]+) +(?P<uptime>[\d\:]+) +(?P<ris>[\d/\.]+)$')
            outlist= out.splitlines()
            for lines in outlist:
                m1=p1.match(lines.rstrip())
                if m1:
                    groups=m1.groupdict()
                    a=groups['ris'].split('/')
                    groups['routes_received']=a[0]
                    groups['routes_installed']=a[1]
                    groups['routes_sent'] =a[-1]
                    del groups['ris']
                    return_dict['peer'][groups['peer']] = groups
        return return_dict


class ShowTenantOmpRoutesAdvertisedSchema(MetaParser):
    ''' Schema for 
        *'show tenant {tenant_name} omp routes advertised'
        *'show tenant {tenant_name} omp routes vpn {vpnid} advertised'
    '''
    schema = {
        'prefix': {
            Any(): {
                'vpn': str
                },
            }
        }

class ShowTenantOmpRoutesAdvertised(ShowTenantOmpRoutesAdvertisedSchema):
    """ Parser for 
    "show tenant {tenant_name} omp routes advertised" 
    "show tenant {tenant_name} omp routes vpn {vpnid} advertised"
    """
    
    cli_command = ["show tenant {tenant_name} omp routes advertised",
                   "show tenant {tenant_name} omp routes vpn {vpnid} advertised"]
    def cli(self, tenant_name='', vpnid='',output=None):
        
        if output is None:
            # Build command
            if tenant_name and vpnid:
                cmd = self.cli_command[1].format(tenant_name=tenant_name, vpnid=vpnid)
            elif tenant_name:
                cmd = self.cli_command[0].format(tenant_name=tenant_name)
            out = self.device.execute(cmd)
        else:
            out = output
        return_dict ={}
        if out:
            return_dict['prefix'] ={}
            # VPN    PREFIX
            # ---------------------------
            # 2      100.2.0.0/16
            # 2      103.2.0.0/16
            # 3      1.1.1.1/32
            p1 = re.compile(r'^(?P<vpn>[\d]+) +(?P<prefix>[0-9\w/\.]+)$')
            outlist=out.splitlines()
            for lines in outlist:
                m1=p1.match(lines.rstrip())
                if m1:
                    groups=m1.groupdict()
                    localdict={}
                    localdict['vpn']=groups['vpn']
                    return_dict['prefix'][groups['prefix']] = localdict
        return return_dict