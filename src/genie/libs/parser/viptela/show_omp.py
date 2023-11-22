from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
import re
import genie.parsergen as pg


class ShowOmpSummarySchema(MetaParser):
# =====================================
# Parser for 'show omp summary'
# =====================================
 schema = {
        'admin_state': str,
        'alert_received': int,
        'alert_sent': int,
        'handshake_received': int,
        'handshake_sent': int,
        'hello_received': int,
        'hello_sent': int,
        'inform_received': int,
        'inform_sent': int,
        'mcast_routes_received': int,
        'mcast_routes_sent': int,
        'omp_uptime': str,
        'oper_state': str,
        'personality': str,
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
        'total_packets_sent': int,
        'update_received': int,
        'update_sent': int,
        'vsmart_peers': int,
 }

class ShowOmpSummary(ShowOmpSummarySchema):

    """ Parser for "show omp summary" """

    cli_command = "show omp summary"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        #show sdwan omp summary 
        #oper-state             UP
        # admin-state            UP
        # personality            vedge
        # omp-uptime             34:03:00:35
        # routes-received        5
        # routes-installed       3
        # routes-sent            2
        p1 = re.compile(r'^(?P<key>[\w0-9\-]+) + (?P<value>[\d\w\:]+)$')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').lower()
                
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']

                parsed_dict.update({key: value})
        
        return parsed_dict

# =====================================
# Schema for 'show omp tloc path'
# =====================================
class ShowOmpTlocPathSchema(MetaParser):
    schema = {
        'tloc_path': {
            Any(): {
                'tloc': {
                    Any(): {
                        'transport': str
                    }
                }
            }
        }
    }     

# =====================================
# Parser for 'show omp tloc path'
# =====================================
class ShowOmpTlocPath(ShowOmpTlocPathSchema):

    """ Parser for "show omp tloc-paths" """

    cli_command = "show omp tloc-paths"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # tloc-paths entries 10.220.100.10 default ipsec
        p1 = re.compile(r'^tloc-paths entries +(?P<ip_add>\S+) +(?P<tloc>\S+) +(?P<transport>\S+)$')
        
        for line in out.splitlines():
            line = line.strip()

            # tloc-paths entries 10.220.100.10 default ipsec
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                tloc_data = parsed_dict.setdefault('tloc_path', {}).\
                        setdefault(groups['ip_add'], {}).\
                        setdefault('tloc', {}).\
					    setdefault(groups['tloc'], {})
                tloc_data.update({'transport' : groups['transport']}) 

        return parsed_dict


# =====================================
# Schema for 'show omp peers'
# =====================================
class ShowOmpPeersSchema(MetaParser):
 schema = {
    'peer': {
        Any(): {
            'type': str,
            'domain_id': int,
            'overlay_id': int,
            'site_id': int,
            'state': str,
            'uptime': str,
            'route': {
                'recv': int,
                'install': int,
                'sent': int
            }
            }
    }     
}           

# =====================================
# Parser for 'show omp peers'
# =====================================
class ShowOmpPeers(ShowOmpPeersSchema):

    """ Parser for "show omp peers" """

    cli_command = "show omp peers"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        peer_dict = {}

        # 10.4.1.5          vsmart  1         1         4294945506up       27:03:26:37      4012/0/4012
        # 10.1.1.1         vedge   1         1         10001985  up       1:23:10:51       884/0/236
        p1 = re.compile(r'^(?P<ip_add>\d\S+)\s+(?P<type>\S+)\s+(?P<domain_id>\S+)\s+(?P<overlay_id>\S+)\s+(?P<site_id>\d+)\s*(?P<state>\S+)\s+(?P<uptime>\S+)\s+(?P<route>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                peer_info = peer_dict.setdefault('peer', {}).setdefault(groups['ip_add'], {})
                peer_info.update({'type': groups['type']})
                peer_info.update({'domain_id': int(groups['domain_id'])})
                peer_info.update({'overlay_id': int(groups['overlay_id'])})
                peer_info.update({'site_id': int(groups['site_id'])})
                peer_info.update({'state': groups['state']})
                peer_info.update({'uptime': groups['uptime']})
                
                route_dict = peer_info.setdefault('route', {})
                recv,install,sent = groups['route'].split('/')
                route_dict.update({'recv': int(recv)})
                route_dict.update({'install': int(install)})
                route_dict.update({'sent': int(sent)})

        return peer_dict


# =====================================
# Schema for 'show omp tlocs'
# =====================================
class ShowOmpTlocsSchema(MetaParser):

    schema = {
        'tloc_data':    {
                Any(): {
                    'tloc': {
                        Any(): {
                            'transport': str,
                            'received_from': {
                                'peer': str,
                                'status': list,
                                'loss_reason': str,
                                'lost_to_peer': str,
                                'lost_to_path_id': str,
                                'attributes': {
                                    'attribute_type': str,
                                    'encap_key': str,
                                    'encap_proto': int,
                                    'encap_spi': int,
                                    'encap_auth': list,
                                    'encap_encrypt': str,
                                    'public_ip': str,
                                    'public_port': int,
                                    'private_ip': str,
                                    'private_port': int,
                                    'bfd_status': str,
                                    Optional('domain_id'): int,
                                    Optional('site_id'): int,
                                    Optional('overlay_id'): int,
                                    'preference': int,
                                    'tag': str,
                                    'stale': str,
                                    'weight': int,
                                    'version': int,
                                    'gen_id': str,
                                    'carrier': str,
                                    'restrict': int,
                                    'on_demand': int,
                                    'groups': list,
                                    'bandwidth': int,
                                    'qos_group': str,
                                    'border': str,
                                    'unknown_attr_len': str
                                }
                            }
                        }
                    } 
                }
            }
    }

# =====================================
# Parser for 'show omp tlocs'
# =====================================
class ShowOmpTlocs(ShowOmpTlocsSchema):

    """ Parser for "show omp tlocs" """

    cli_command = "show omp tlocs"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        tloc_data= {}

        # -------------------------------                
        p0= re.compile(r'^[\-]+$')
        #tloc entries for 10.220.100.10
        p1 =  re.compile(r'^tloc entries for +(?P<ip_add>\S+)$')
        #RECEIVED FROM: 
        p2 = re.compile(r'^(?P<recv>RECEIVED FROM)\:$')
        #ipsec
        p3 = re.compile(r'^(?P<trans>ipsec|gre)$')
        #default
        p4 = re.compile(r'^(?P<tloc>[\w\-0-9]+)$')
        #Attributes: 
        p5 = re.compile(r'^(?P<attr>\w+)\:$')
        
        #peer            0.0.0.0
        #status          C,Red,R
        p6 = re.compile(r'^(?P<key>\S+) +(?P<value>[\S\s]+)$')


        tloc_data = {}
        for line in out.splitlines():
            line = line.strip()

            # ------------------------------- 
            ### match the line so that P4 expression does not match the line and fail
            m = p0.match(line)
            if m:
                groups = m.groupdict()
                continue

            #tloc entries for 10.220.100.10
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                tloc_d = tloc_data.setdefault('tloc_data', {}).setdefault(groups['ip_add'], {})
                last_dict_ptr = tloc_d
                continue

            #RECEIVED FROM:
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                recv_fr = groups['recv'].replace(' ','_').lower()
                tloc_data_recv = tloc_d_color.setdefault(recv_fr, {})
                last_dict_ptr = tloc_data_recv
                continue
            
            #ipsec
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                tloc_d_color.update({'transport': groups['trans']})
                continue

            #default
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                tloc = groups['tloc'].replace(' ','_').lower()
                tloc_d_color = tloc_d.setdefault('tloc', {}).setdefault(tloc, {})
                last_dict_ptr = tloc_d_color
                continue

            #Attributes: 
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                attrs = groups['attr'].replace(' ','_').lower()
                tloc_data_attr = tloc_data_recv.setdefault(attrs, {})
                last_dict_ptr = tloc_data_attr
                continue
                
            #peer            0.0.0.0
            #status          C,Red,R
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                keys = groups['key'].replace('-','_').replace(' ','_').lower()
                if keys in ['encap_auth', 'status']:
                    values = list(groups['value'].split(","))
                elif keys in ['groups']:
                    values = groups['value'].replace('[','').replace(']','').replace(' ','') 
                    values = [int(i) for i in values.split(",")]
                elif keys in ['overlay_id', 'site_id', 'domain_id']:
                    #set the domain_id/site_id/overlay_id only if its int else skip
                    if groups['value'].isdigit():
                         values = int(groups['value'])
                    else:
                        continue
                else:
                    values = groups['value'].replace('-','_').replace(' ','_').lower()
                    if values.isdigit():
                        values = int(values)
                    else:
                        values =str(values)

                last_dict_ptr.update({keys:values})
                continue


        return tloc_data

# =====================================
# Schema for 'show omp routes'
# =====================================
class ShowOmpRoutesSchema(MetaParser):

    """ Schema for show omp routes
        * show omp routes <prefix>
        * show omp routes vpn <vpn>
        * show omp routes <prefix> vpn <vpn>
        * show omp routes family <af> vpn <vpn> 
    """

    schema = {
        'vrf': {
            Any(): {
                'prefixes': {
                    Any(): {
                        'prefix': str,
                        'from_peer': {
                            Any(): {
                                'peer': str,
                                'path_list': {
                                    Any(): {  # index
                                        'index': int,
                                        'path_id': str,
                                        'label': str,
                                        'status': list,
                                        'attr_type': str,
                                        'tloc_ip': str,
                                        'color': str,
                                        'encap': str,
                                        'preference': str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# =====================================
# Parser for 'show omp routes'
# =====================================
class ShowOmpRoutes(ShowOmpRoutesSchema):

    """parser for show omp routes
                  show omp routes <prefix>
                  show omp routes vpn <vpn>
                  show omp routes <prefix> vpn <vpn>
                  show omp routes family <af> vpn <vpn>"""

    cli_command = ['show omp routes',
                  'show omp routes {prefix}',
                  'show omp routes vpn {vpn}',
                  'show omp routes {prefix} vpn {vpn}',
                  'show omp routes family {af} vpn {vpn}']

    def cli(self, prefix=None, vpn=None, af='ipv4', output=None):

        if output is None:
            if prefix and vpn:
                cmd = self.cli_command[3].format(prefix=prefix, vpn=vpn)
            elif af and vpn:
                cmd = self.cli_command[4].format(af=af, vpn=vpn)
            elif prefix:
                cmd = self.cli_command[1].format(prefix=prefix)
            elif vpn:
                cmd = self.cli_command[2].format(vpn=vpn)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        #                                             PATH                      ATTRIBUTE                                                       
        # VPN    PREFIX              FROM PEER        ID     LABEL    STATUS    TYPE       TLOC IP          COLOR            ENCAP  PREFERENCE
        # --------------------------------------------------------------------------------------------------------------------------------------
        # 4      10.0.0.0/8          1.1.1.3          936    1002     C,I,R     installed  100.1.1.1        green            ipsec  200
        p1 = re.compile(r'(?P<vrf>\d+)\s+(?P<prefix>[\d\.\/]+)\s+(?P<from_peer>[\d\.\/]+)\s+(?P<path_id>\d+)\s+(?P<label>\d+)\s+(?P<status>\S+)\s+(?P<attr_type>\S+)\s+(?P<tloc_ip>[\d\.\/]+)\s+(?P<color>\S+)\s+(?P<encap>\S+)\s+(?P<preference>\S+)')

        #                            1.1.1.3          937    1002     C,I,R     installed  100.1.1.1        blue             ipsec  200         
        #                            1.1.1.3          938    1002     C,I,R     installed  100.1.1.2        green            ipsec  200         
        #                            1.1.1.3          939    1002     C,I,R     installed  100.1.1.2        blue             ipsec  200 
        p2 = re.compile(r'(?P<from_peer>[\d\.\/]+)\s+(?P<path_id>\d+)\s+(?P<label>\d+)\s+(?P<status>\S+)\s+(?P<attr_type>\S+)\s+(?P<tloc_ip>[\d\.\/]+)\s+(?P<color>\S+)\s+(?P<encap>\S+)\s+(?P<preference>\S+)')

        index = 1
        peer = ""

        for line in out.splitlines():
            line = line.strip()

            # 4      10.0.0.0/8          1.1.1.3          936    1002     C,I,R     installed  100.1.1.1        green            ipsec  200
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['vrf']:
                    vrf = group['vrf']
                if prefix != group['prefix'] or peer != group['from_peer']:
                    prefix = group['prefix']
                    peer = group['from_peer']
                    index = 1

                route_info = parsed_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('prefixes', {}).setdefault(prefix, {})
                route_info['prefix'] = prefix
                route_info.setdefault('from_peer', {})

                from_peer_dict = route_info['from_peer'].setdefault(peer, {})
                from_peer_dict['peer'] = peer
                path_list_dict = from_peer_dict.setdefault('path_list', {})
                idx_dict = path_list_dict.setdefault(index, {})
                idx_dict['index'] = index
                idx_dict['path_id'] = group['path_id']
                idx_dict['label'] = group['label']
                idx_dict['status'] = group['status'].split(",")
                idx_dict['attr_type'] = group['attr_type']
                idx_dict['tloc_ip'] = group['tloc_ip']
                idx_dict['color'] = group['color']
                idx_dict['encap'] = group['encap']
                idx_dict['preference'] = group['preference']
                index += 1

            #                            1.1.1.3          937    1002     C,I,R     installed  100.1.1.1        blue             ipsec  200
            m = p2.match(line)
            if m:
                group = m.groupdict()

                if peer != group['from_peer']:
                    peer = group['from_peer']
                    index = 1

                if vpn is not None:
                    route_info = parsed_dict.setdefault('vrf', {}).setdefault(vpn, {}).setdefault('prefixes',{}).setdefault(prefix, {})
                else:
                    route_info = parsed_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('prefixes',{}).setdefault(prefix, {})

                route_info['prefix'] = prefix
                route_info.setdefault('from_peer', {})

                from_peer_dict = route_info['from_peer'].setdefault(peer, {})
                from_peer_dict['peer'] = peer
                path_list_dict = from_peer_dict.setdefault('path_list', {})
                idx_dict = path_list_dict.setdefault(index, {})
                idx_dict['index'] = index
                idx_dict['path_id'] = group['path_id']
                idx_dict['label'] = group['label']
                idx_dict['status'] = group['status'].split(",")
                idx_dict['attr_type'] = group['attr_type']
                idx_dict['tloc_ip'] = group['tloc_ip']
                idx_dict['color'] = group['color']
                idx_dict['encap'] = group['encap']
                idx_dict['preference'] = group['preference']
                index += 1

        return parsed_dict
