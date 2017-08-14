###############################################################################
#                         Show feature parser
###############################################################################

''' show feature '''

import re
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional


# ###############################################################################
#                             show ip mroute vrf all parser
# ###############################################################################


class ShowIpMrouteVrfAllSchema(MetaParser):
    # schema for show ip mroute vrf all 

    schema = {'vrf_name':         
                {Any(): 
                    {Optional('multicast_group'): 
                        {Any(): 
                            {Optional('source_address'): 
                                {Any(): 
                                    {Optional('uptime'): str,
                                     Optional('flag'): str,
                                     Optional('oil_count'): int,
                                     Optional('incoming_interface_list'):
                                        {Any(): 
                                            {Optional('rpf_nbr'): str,
                                            },
                                        },
                                     Optional('outgoing_interface_list'): 
                                        {Any(): 
                                            {Optional('oil_uptime'): str,
                                             Optional('oil_flags'): str,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            }



class ShowIpMrouteVrfAll(ShowIpMrouteVrfAllSchema):
    # class to parse
    def cli(self):
        # cli implementation of parsers 

        out = self.device.execute('show ip mroute vrf all')
        ip_mroute_vrf_all_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # IP Multicast Routing Table for VRF "default 
            p1 = re.compile(r'^\s*IP +Multicast +Routing +Table +for +VRF +(?P<vrf_name>[a-zA-Z0-9\"]+)$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                vrf_name = vrf_name.replace('"',"")

                if 'vrf_name' not in ip_mroute_vrf_all_dict:
                    ip_mroute_vrf_all_dict['vrf_name'] = {}
                if vrf_name not in ip_mroute_vrf_all_dict['vrf_name']:
                    ip_mroute_vrf_all_dict['vrf_name'][vrf_name] = {}
                    continue

            # (*, 232.0.0.0/8), uptime: 9w2d, pim ip 
            p2 = re.compile(r'^\s*\((?P<source_address>[0-9\.\*\/]+), *(?P<multicast_group>[0-9\.\/]+)\), *uptime: *(?P<uptime>[0-9a-zA-Z\:]+), *(?P<flag>[a-zA-Z\s]+)$')
            m = p2.match(line)
            if m:
                source_address = m.groupdict()['source_address']
                multicast_group = m.groupdict()['multicast_group']
                uptime = m.groupdict()['uptime']
                flag = m.groupdict()['flag']

                if 'multicast_group' not in ip_mroute_vrf_all_dict['vrf_name'][vrf_name]:
                    ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'] = {}
                if multicast_group not in ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group']:
                    ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group] = {}
                if 'source_address' not in ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]:
                    ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'] = {}
                if source_address not in ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address']:
                    ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address] = {}
                ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['uptime'] = uptime
                ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['flag'] = flag
                continue

            # Incoming interface: Null, RPF nbr: 0.0.0.0 
            p3 = re.compile(r'^\s*Incoming +interface: +(?P<incoming_interface>[a-zA-Z0-9\/\-\.]+), +RPF +nbr: +(?P<rpf_nbr>[0-9\.]+)$')
            m = p3.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']
                rpf_nbr = m.groupdict()['rpf_nbr']

                if 'incoming_interface_list' not in ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'] = {}
                if incoming_interface not in ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list']:
                    ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'][incoming_interface] = {}
                ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'][incoming_interface]['rpf_nbr'] = rpf_nbr
                continue

            # Outgoing interface list: (count: 0) 
            p4 =  re.compile(r'^\s*Outgoing *interface *list: *\(count: *(?P<oil_count>[0-9]+)\)$')
            m = p4.match(line)
            if m:
                oil_count = int(m.groupdict()['oil_count'])
                ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['oil_count'] = oil_count
                continue

            # loopback2, uptime: 3d11h, igmp 
            p5 = re.compile(r'^\s*(?:(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+),)? *uptime: *(?:(?P<oil_uptime>[a-zA-Z0-9\:]+),)? *(?:(?P<oil_flags>[a-zA-Z\s]+))?$')
            m = p5.match(line)
            if m:
                outgoing_interface = m.groupdict()['outgoing_interface']
                oil_uptime = m.groupdict()['oil_uptime']
                oil_flags = m.groupdict()['oil_flags']

                if 'outgoing_interface_list' not in ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'] = {}
                if outgoing_interface not in ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list']:
                    ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface] = {}
                ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_uptime'] = oil_uptime
                ip_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_flags'] = oil_flags

        return ip_mroute_vrf_all_dict


# ###############################################################################
# #                         Show ipv6 mroute vrf all
# ###############################################################################


class ShowIpv6MrouteVrfAllSchema(MetaParser):
 
    schema = {'vrf_name': 
                {Any(): 
                    {Optional('multicast_group'): 
                        {Any(): 
                            {Optional('source_address'): 
                                {Any(): 
                                    {Optional('uptime'): str,
                                     Optional('flag'): str,
                                     Optional('oil_count'): int,
                                     Optional('incoming_interface_list'):
                                        {Any(): 
                                            {Optional('rpf_nbr'): str,
                                            },
                                        },
                                     Optional('outgoing_interface_list'): 
                                        {Any(): 
                                            {Optional('oil_uptime'): str,
                                             Optional('oil_flags'): str,
                                             Optional('oif_rpf'): bool          
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            }

        
    


class ShowIpv6MrouteVrfAll(ShowIpv6MrouteVrfAllSchema):
    ''' class to parse '''
    def cli(self):
        ''' cli implementation of parsers '''

        out = self.device.execute('show ipv6 mroute vrf all')
        ipv6_mroute_vrf_all_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            ''' IPv6 Multicast Routing Table for VRF "default '''
            p1 = re.compile(r'^\s*IPv6 +Multicast +Routing +Table +for +VRF +(?P<vrf_name>[a-zA-Z0-9\"]+)$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                vrf_name = vrf_name.replace('"',"")
                if 'vrf_name' not in ipv6_mroute_vrf_all_dict:
                    ipv6_mroute_vrf_all_dict['vrf_name'] = {}
                if vrf_name not in ipv6_mroute_vrf_all_dict['vrf_name']:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name] = {}
                    continue

            ''' (*, ff30::/12), uptime: 3d11h, pim6 ipv6 ''' 
            p2 = re.compile(r'^\s*\((?P<source_address>[a-zA-Z0-9\.\*\/\:]+), *(?P<multicast_group>[a-zA-Z0-9\:\/]+)\), *uptime: *(?P<uptime>[a-zA-Z0-9\:]+), *(?P<flag>[a-zA-Z0-9\s]+)$')
            m = p2.match(line)
            if m:
                source_address = m.groupdict()['source_address']
                multicast_group = m.groupdict()['multicast_group']
                uptime = m.groupdict()['uptime']
                flag = m.groupdict()['flag']

                if 'multicast_group' not in ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'] = {}
                if multicast_group not in ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group']:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group] = {}
                if 'source_address' not in ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'] = {}
                if source_address not in ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address']:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address] = {}
                ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['uptime'] = uptime
                ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['flag'] = flag
                continue

            ''' Incoming interface: Null, RPF nbr: 0:: '''
            p3 =  re.compile(r'^\s*Incoming *interface: *(?P<incoming_interface>[a-zA-Z0-9\/\.]+), *RPF *nbr: *(?P<rpf_nbr>[a-zA-Z0-9\:\,\s]+)$')
            m = p3.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']
                rpf_nbr = m.groupdict()['rpf_nbr']
                
                if 'incoming_interface_list' not in ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'] = {}
                if incoming_interface not in ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list']:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'][incoming_interface] = {}
                ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'][incoming_interface]['rpf_nbr'] = rpf_nbr
                continue

            ''' Outgoing interface list: (count: 0) '''
            p4 =  re.compile(r'^\s*Outgoing *interface *list: *\(count: *(?P<oil_count>[0-9]+)\)$')
            m = p4.match(line)
            if m:
                oil_count = int(m.groupdict()['oil_count'])
                ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['oil_count'] = oil_count
                continue

            ''' loopback2, uptime: 3d11h, igmp '''
            p5 = re.compile(r'^\s*(?:(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+),)? *uptime: *(?:(?P<oil_uptime>[a-zA-Z0-9\:]+),)? *(?:(?P<oil_flags>[a-zA-Z0-9\s]+),)?$')
            m = p5.match(line)
            if m:
                outgoing_interface = m.groupdict()['outgoing_interface']
                oil_uptime = m.groupdict()['oil_uptime']
                oil_flags = m.groupdict()['oil_flags']

                if 'outgoing_interface_list' not in ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'] = {}
                if outgoing_interface not in ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list']:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface] = {}

                ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_uptime'] = oil_uptime
                ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_flags'] = oil_flags
                continue

            p5_1 = re.compile(r'^\s*(?:(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+),)? *uptime: *(?:(?P<oil_uptime>[a-zA-Z0-9\:]+),)? *(?:(?P<oil_flags>[a-zA-Z0-9\s]+),)? *(?P<oif_rpf>(\(RPF\))+)*$')
            m = p5_1.match(line)
            if m:
                outgoing_interface = m.groupdict()['outgoing_interface']
                oil_uptime = m.groupdict()['oil_uptime']
                oil_flags = m.groupdict()['oil_flags']
                oif_rpf = m.groupdict()['oif_rpf']

                if 'outgoing_interface_list' not in ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'] = {}
                if outgoing_interface not in ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list']:
                    ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface] = {}

                ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_uptime'] = oil_uptime
                ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_flags'] = oil_flags
                ipv6_mroute_vrf_all_dict['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oif_rpf'] = True

        return ipv6_mroute_vrf_all_dict

# ###############################################################################
# #                         Show ip static-route multicast
# ###############################################################################


class ShowIpStaticRouteMulticastSchema(MetaParser):
    # schema for show ip static-route multicast 

    schema = {'vrf': 
                {Any():
                    {'af_name':
                        {Any():
                            {'mroute':
                                {Any():
                                    {'path':
                                        {Any():
                                            {'mroute_neighbor_address': str,
                                             Optional('mroute_interface_name'): str,
                                             Optional('urib'): str,
                                             Optional('vrf_id'): str,
                                             'urib': bool
                                            }
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            }
            
                

class ShowIpStaticRouteMulticast(ShowIpStaticRouteMulticastSchema):
    # class to parse
    def cli(self):
        # cli implemetation of parsers
        out = self.device.execute('show ip static-route multicast')
        static_routemulticast_dict = {}

        for line in out.splitlines():
            line = line.rstrip()
            #Mstatic-route for VRF "default"(1) 
            p1 = re.compile(r'^\s*(Static-route|Mstatic-route) *for *VRF *(?P<vrf>[a-zA-Z0-9\"]+) *\((?P<vrf_id>[0-9]+)\)$')
                              
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"',"")
                vrf_id = str(m.groupdict()['vrf_id'])
                vrf_id = vrf_id.replace("(","")
                vrf_id = vrf_id.replace(")","")
                
                
                if 'vrf' not in static_routemulticast_dict:
                    static_routemulticast_dict['vrf'] = {}
                if vrf not in static_routemulticast_dict['vrf']:
                    static_routemulticast_dict['vrf'][vrf] = {}
                    continue

            #IPv4 MStatic Routes:
            p2 = re.compile(r'^\s*(?P<af_name>[a-zA-Z0-9]+) *(MStatic|Unicast Static) *Routes:$')
            m = p2.match(line)
            if m:
                af_name = str(m.groupdict()['af_name'])
                
                if 'af_name' not in static_routemulticast_dict['vrf'][vrf]:
                    static_routemulticast_dict['vrf'][vrf]['af_name'] = {}
                if af_name not in static_routemulticast_dict['vrf'][vrf]['af_name']:
                    static_routemulticast_dict['vrf'][vrf]['af_name'][af_name] = {}
                    continue

            #112.0.0.0/8, configured nh: 0.0.0.0/32 Null0 
            p3 =  re.compile(r'^\s*(?P<mroute>[0-9\.\/]+), +configured +nh: +(?P<mroute_neighbor_address>[a-zA-Z0-9\.\/]+) +(?P<mroute_interface_name>[a-zA-Z0-9\.]+)$')
            m = p3.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                mroute_interface_name = str(m.groupdict()['mroute_interface_name'])
                mroute_neighbor_address = str(m.groupdict()['mroute_neighbor_address'])
                #path = m.groupdict()['path']


                if 'mroute' not in static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]:
                    static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'] = {}
                if mroute not in static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute']:
                    static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute] = {} 

                if 'path' not in static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]:
                    static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'] = {}

                path = mroute_neighbor_address + ' ' + mroute_interface_name

                if path not in static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path']:
                    static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path] = {}

                static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path]['mroute_interface_name'] = mroute_interface_name
                static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path]['mroute_neighbor_address'] = mroute_neighbor_address
                continue

            # 10.2.2.2/32, configured nh: 0.0.0.0/32%sanity1 Vlan2
            # 10.2.2.2/32, configured nh: 0.0.0.0/32%sanity1 Vlan2
            p3_1 = re.compile(r'^\s*(?P<mroute>[0-9\.\/]+), +configured +nh: +(?P<mroute_neighbor_address>[a-zA-Z0-9\.\/\%\s]+)$')
            m = p3_1.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                mroute_neighbor_address = str(m.groupdict()['mroute_neighbor_address'])

                if 'mroute' not in static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]:
                    static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'] = {}
                if mroute not in static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute']:
                    static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute] = {} 
                if 'path' not in static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]:
                    static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'] = {}
                path = mroute_neighbor_address
                if path not in static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path']:
                    static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path] = {}
                static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path]['mroute_neighbor_address'] = mroute_neighbor_address
                continue

            # (installed in urib) 
            p4 = re.compile(r'^\s*(?P<urib>(\(installed in urib\))+)$')
            m = p4.match(line)
            if m:
                static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path]['urib'] = True
                static_routemulticast_dict['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path]['vrf_id'] = vrf_id
                continue

        return static_routemulticast_dict


###############################################################################
#                         Show ipv6 static-route multicast
###############################################################################


class ShowIpv6StaticRouteMulticastSchema(MetaParser):
    # schema for show ipv6 static-route multicast 

    schema = {'vrf':
                {Any():
                    {Optional('mroute'):
                        {Any():
                            {Optional('path'):
                                {Any():
                                    {Optional('mroute_neighbor_address'): str,
                                     Optional('nh_vrf'): str,
                                     Optional('reslv_tid'): str,
                                     Optional('mroute_interface_name'): str,
                                     Optional('rnh_status'): str,
                                     Optional('bfd_enable'): bool,
                                     Optional('vrf_id'): str,
                                     Optional('preference'): str,
                                     Optional('mroute_int'): str
                                    },
                                },
                            },
                        },
                    },
                },
            }
        


class ShowIpv6StaticRouteMulticast(ShowIpv6StaticRouteMulticastSchema):
    # class to parse '''
    def cli(self):
        # cli implementation of parsers '''

        out = self.device.execute('show ipv6 static-route multicast')
        ipv6_static_routemulticast_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # IPv6 Configured Static Routes for VRF "default"(1) 
            p1 = re.compile(r'^\s*IPv6 +Configured +Static +Routes +for +VRF +(?P<vrf>[a-zA-Z0-9\"]+) *\((?P<vrf_id>[0-9]+)\)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"',"")
                vrf_id = m.groupdict()['vrf_id']
                vrf_id = vrf_id.replace("(","")
                vrf_id = vrf_id.replace(")","")

                if 'vrf' not in ipv6_static_routemulticast_dict:
                    ipv6_static_routemulticast_dict['vrf'] = {}
                if vrf not in ipv6_static_routemulticast_dict['vrf']:
                    ipv6_static_routemulticast_dict['vrf'][vrf] = {}
                    continue

            # 126::/16 -> Null0, preference: 1
            p2 = re.compile(r'^\s*(?P<mroute>[a-zA-Z0-9\:\/]+) +-> +(?P<mroute_int>[\w\W]+), preference: +(?P<preference>[0-9]+)$')
            m = p2.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                preference = m.groupdict()['preference']
                mroute_int = m.groupdict()['mroute_int']

                if 'mroute' not in ipv6_static_routemulticast_dict['vrf'][vrf]:
                    ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'] = {}
                if mroute not in ipv6_static_routemulticast_dict['vrf'][vrf]['mroute']:
                    ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute] = {}                
                    continue

            # nh_vrf(default) reslv_tid 80000001 
            p3 = re.compile(r'^\s*nh_vrf *(?P<nh_vrf>[a-zA-Z0-9\(\)]+) +reslv_tid +(?P<reslv_tid>[0-9]+)$')
            m = p3.match(line)
            if m:
                nh_vrf = m.groupdict()['nh_vrf']
                nh_vrf = nh_vrf.replace("(","")
                nh_vrf = nh_vrf.replace(")","")
                reslv_tid = m.groupdict()['reslv_tid']
                continue

            # real-next-hop: 0::, interface: Null0 
            p4 =  re.compile(r'^\s*real-next-hop: +(?P<mroute_neighbor_address>[a-zA-Z0-9\:]+), +interface: +(?P<mroute_interface_name>[\w\W]+)$')
            m = p4.match(line)
            if m:
                mroute_neighbor_address = m.groupdict()['mroute_neighbor_address']
                mroute_interface_name = m.groupdict()['mroute_interface_name']

                if 'path' not in ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]:
                    ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'] = {}

                path = mroute_neighbor_address + ' ' + mroute_interface_name

                if path not in ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path']:
                    ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path] = {}

                ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path]['mroute_neighbor_address'] = mroute_neighbor_address
                ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path]['mroute_interface_name'] = mroute_interface_name
                ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path]['preference'] = preference
                ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path]['nh_vrf'] = nh_vrf
                ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path]['reslv_tid'] = reslv_tid
                continue

            # rnh(not installed in u6rib) 
            p5 = re.compile(r'^\s*rnh(?P<rnh_status>[a-zA-Z0-9\(\)\s]+)$')
            m = p5.match(line)
            if m:
                rnh_status = str(m.groupdict()['rnh_status'])
                rnh_status = rnh_status.replace("(","")
                rnh_status = rnh_status.replace(")","")

                ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path]['rnh_status'] = rnh_status
                continue

            # bfd_enabled no
            p6 = re.compile(r'^\s*bfd_enabled +(?P<bfd_enable>(no)+)$')
            m = p6.match(line)
            if m:
                bfd_enable = m.groupdict()['bfd_enable']

                ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path]['bfd_enable'] = False
                continue

            p6 = re.compile(r'^\s*bfd_enabled +(?P<bfd_enable>(yes)+)$')
            m = p6.match(line)
            if m:
                bfd_enable = m.groupdict()['bfd_enable']

                ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path]['bfd_enable'] = True
                ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path]['vrf_id'] = vrf_id
                ipv6_static_routemulticast_dict['vrf'][vrf]['mroute'][mroute]['path'][path]['mroute_int'] = mroute_int
                continue
        
        return ipv6_static_routemulticast_dict


