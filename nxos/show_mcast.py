###############################################################################
#                         Show feature parser
###############################################################################

''' show feature '''

import re
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional


class ShowFeatureSchema(MetaParser):
    '''Schema for show feature'''

    schema = {
        'feature': 
            {Any(): 
                {'instance':
                    {Any():
                        {'state': str
                    }
                }
            }
        },
    }


class ShowFeature(ShowFeatureSchema):
    ''' class to parse '''
    def cli(self):
        ''' cli implementation of parsers '''

        out = self.device.execute('show feature')
        feature_dict = {}

        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*(?P<feature_name>\S+) +(?P<instance>[0-9]+) +(?P<state>[a-zA-Z\-\(\)]+)$')
            m = p1.match(line)
            if m:
                feature = m.groupdict()['feature_name']
                instance = m.groupdict()['instance']
                state = m.groupdict()['state']

                if 'feature' not in feature_dict:
                    feature_dict['feature'] = {}
                if feature not in feature_dict['feature']:
                    feature_dict['feature'][feature] = {}
                if 'instance' not in feature_dict['feature'][feature]:
                    feature_dict['feature'][feature]['instance'] = {}
                if instance not in feature_dict['feature'][feature]['instance']:
                    feature_dict['feature'][feature]['instance'][instance] = {}
                    
                feature_dict['feature'][feature]['instance'][instance]['state'] = state
                continue

        return feature_dict


# ###############################################################################
# #                            show ip mroute vrf all parser
# ###############################################################################


class ShowIpMrouteVrfAllSchema(MetaParser):
    # schema for show ip mroute vrf all 

    schema = {'ip_mroute_vrf_all':
        {'vrf_name': 
            {Any(): 
                {'multicast_group': 
                    {Any(): 
                        {'source_address': 
                            {Any(): 
                                {'uptime': str,
                                 'flag': str,
                                 'oil_count': int,
                                 'incoming_interface_list':
                                    {Any(): 
                                        {'rpf_nbr': str,
                                        },
                                    },
                                 Optional('outgoing_interface_list'): 
                                    {Any(): 
                                        {'oil_uptime': str,
                                         'oil_flags': str,
                                         
                                        },

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

                if 'ip_mroute_vrf_all' not in ip_mroute_vrf_all_dict:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all'] = {}
                if 'vrf_name' not in ip_mroute_vrf_all_dict['ip_mroute_vrf_all']:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'] = {}
                if vrf_name not in ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name']:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name] = {}
                continue

            # (*, 232.0.0.0/8), uptime: 9w2d, pim ip 
            p2 = re.compile(r'^\s*\((?P<source_address>[0-9\.\*\/]+), *(?P<multicast_group>[0-9\.\/]+)\), *uptime: *(?P<uptime>[0-9a-zA-Z\:]+), *(?P<flag>[a-zA-Z\s]+)$')
            m = p2.match(line)
            if m:
                source_address = m.groupdict()['source_address']
                multicast_group = m.groupdict()['multicast_group']
                uptime = m.groupdict()['uptime']
                flag = m.groupdict()['flag']

                if 'multicast_group' not in ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'] = {}
                if multicast_group not in ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group']:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group] = {}
                if 'source_address' not in ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'] = {}
                if source_address not in ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address']:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address] = {}
                ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['uptime'] = uptime
                ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['flag'] = flag
                continue

            # Incoming interface: Null, RPF nbr: 0.0.0.0 
            p3 = re.compile(r'^\s*Incoming +interface: +(?P<incoming_interface>[a-zA-Z0-9\/\-\.]+), +RPF +nbr: +(?P<rpf_nbr>[0-9\.]+)$')
            m = p3.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']
                rpf_nbr = m.groupdict()['rpf_nbr']

                if 'incoming_interface_list' not in ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'] = {}
                if incoming_interface not in ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list']:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'][incoming_interface] = {}
                ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'][incoming_interface]['rpf_nbr'] = rpf_nbr
                continue

            # Outgoing interface list: (count: 0) 
            p4 =  re.compile(r'^\s*Outgoing *interface *list: *\(count: *(?P<oil_count>[0-9]+)\)$')
            m = p4.match(line)
            if m:
                oil_count = int(m.groupdict()['oil_count'])
                ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['oil_count'] = oil_count
                continue

            # loopback2, uptime: 3d11h, igmp 
            p5 = re.compile(r'^\s*(?:(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+),)? *uptime: *(?:(?P<oil_uptime>[a-zA-Z0-9\:]+),)? *(?:(?P<oil_flags>[a-zA-Z\s]+))?$')
            m = p5.match(line)
            if m:
                outgoing_interface = m.groupdict()['outgoing_interface']
                oil_uptime = m.groupdict()['oil_uptime']
                oil_flags = m.groupdict()['oil_flags']

                if 'outgoing_interface_list' not in ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'] = {}
                if outgoing_interface not in ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list']:
                    ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface] = {}
                ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_uptime'] = oil_uptime
                ip_mroute_vrf_all_dict['ip_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_flags'] = oil_flags

        return ip_mroute_vrf_all_dict


# ###############################################################################
# #                         Show ipv6 mroute vrf all
# ###############################################################################


class ShowIpv6MrouteVrfAllSchema(MetaParser):
 
    schema = {'ipv6_mroute_vrf_all':
        {'vrf_name': 
            {Any(): 
                {'multicast_group': 
                    {Any(): 
                        {'source_address': 
                            {Any(): 
                                {'uptime': str,
                                 'flag': str,
                                 'oil_count': int,
                                 'incoming_interface_list':
                                    {Any(): 
                                        {'rpf_nbr': str,
                                        },
                                    },
                                 Optional('outgoing_interface_list'): 
                                    {Any(): 
                                        {'oil_uptime': str,
                                         'oil_flags': str,
                                         'oif_rpf': str,
                                         'oif_rpf': bool                                         
                                        },

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
                if 'ipv6_mroute_vrf_all' not in ipv6_mroute_vrf_all_dict:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all'] = {}
                if 'vrf_name' not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'] = {}
                if vrf_name not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name']:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name] = {}
                    continue

            ''' (*, ff30::/12), uptime: 3d11h, pim6 ipv6 ''' 
            p2 = re.compile(r'^\s*\((?P<source_address>[a-zA-Z0-9\.\*\/\:]+), *(?P<multicast_group>[a-zA-Z0-9\:\/]+)\), *uptime: *(?P<uptime>[a-zA-Z0-9\:]+), *(?P<flag>[a-zA-Z0-9\s]+)$')
            m = p2.match(line)
            if m:
                source_address = m.groupdict()['source_address']
                multicast_group = m.groupdict()['multicast_group']
                uptime = m.groupdict()['uptime']
                flag = m.groupdict()['flag']

                if 'multicast_group' not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'] = {}
                if multicast_group not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group']:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group] = {}
                if 'source_address' not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'] = {}
                if source_address not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address']:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address] = {}
                ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['uptime'] = uptime
                ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['flag'] = flag
                continue

            ''' Incoming interface: Null, RPF nbr: 0:: '''
            p3 =  re.compile(r'^\s*Incoming *interface: *(?P<incoming_interface>[a-zA-Z0-9\/\.]+), *RPF *nbr: *(?P<rpf_nbr>[a-zA-Z0-9\:\,\s]+)$')
            m = p3.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']
                rpf_nbr = m.groupdict()['rpf_nbr']
                
                if 'incoming_interface_list' not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'] = {}
                if incoming_interface not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list']:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'][incoming_interface] = {}
                ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['incoming_interface_list'][incoming_interface]['rpf_nbr'] = rpf_nbr
                continue

            ''' Outgoing interface list: (count: 0) '''
            p4 =  re.compile(r'^\s*Outgoing *interface *list: *\(count: *(?P<oil_count>[0-9]+)\)$')
            m = p4.match(line)
            if m:
                oil_count = int(m.groupdict()['oil_count'])
                ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['oil_count'] = oil_count
                continue

            ''' loopback2, uptime: 3d11h, igmp '''
            p5 = re.compile(r'^\s*(?:(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+),)? *uptime: *(?:(?P<oil_uptime>[a-zA-Z0-9\:]+),)? *(?:(?P<oil_flags>[a-zA-Z0-9\s]+),)?$')
            m = p5.match(line)
            if m:
                outgoing_interface = m.groupdict()['outgoing_interface']
                oil_uptime = m.groupdict()['oil_uptime']
                oil_flags = m.groupdict()['oil_flags']

                if 'outgoing_interface_list' not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'] = {}
                if outgoing_interface not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list']:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface] = {}

                ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_uptime'] = oil_uptime
                ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_flags'] = oil_flags
                continue

            p5_1 = re.compile(r'^\s*(?:(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+),)? *uptime: *(?:(?P<oil_uptime>[a-zA-Z0-9\:]+),)? *(?:(?P<oil_flags>[a-zA-Z0-9\s]+),)? *(?P<oif_rpf>(\(RPF\))+)*$')
            m = p5_1.match(line)
            if m:
                outgoing_interface = m.groupdict()['outgoing_interface']
                oil_uptime = m.groupdict()['oil_uptime']
                oil_flags = m.groupdict()['oil_flags']
                oif_rpf = m.groupdict()['oif_rpf']

                if 'outgoing_interface_list' not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'] = {}
                if outgoing_interface not in ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list']:
                    ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface] = {}

                ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_uptime'] = oil_uptime
                ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oil_flags'] = oil_flags
                ipv6_mroute_vrf_all_dict['ipv6_mroute_vrf_all']['vrf_name'][vrf_name]['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list'][outgoing_interface]['oif_rpf'] = True

        return ipv6_mroute_vrf_all_dict

# ###############################################################################
# #                         Show ip static-route multicast
# ###############################################################################


class ShowIpStaticRouteMulticastSchema(MetaParser):
    # schema for show ip static-route multicast 

    schema = {'static_routemulticast':
                {'vrf': 
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
                                                 'urib': bool
                                                }
                                            },
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
            p1 = re.compile(r'^\s*(Static-route|Mstatic-route) *for *VRF +(?P<vrf>[a-zA-Z0-9\(\)\"]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"',"")
                vrf = vrf.replace("(","_")
                vrf = vrf.replace(")","")
                
                if 'static_routemulticast' not in static_routemulticast_dict:
                    static_routemulticast_dict['static_routemulticast'] = {}
                if 'vrf' not in static_routemulticast_dict['static_routemulticast']:
                    static_routemulticast_dict['static_routemulticast']['vrf'] = {}
                if vrf not in static_routemulticast_dict['static_routemulticast']['vrf']:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf] = {}
                    continue

            #IPv4 MStatic Routes:
            p2 = re.compile(r'^\s*(?P<af_name>[a-zA-Z0-9]+) *(MStatic|Unicast Static) *Routes:$')
            m = p2.match(line)
            if m:
                af_name = str(m.groupdict()['af_name'])
                
                if 'af_name' not in static_routemulticast_dict['static_routemulticast']['vrf'][vrf]:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'] = {}
                if af_name not in static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name']:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name] = {}
                #import pdb ; pdb.set_trace()
                    continue

            #112.0.0.0/8, configured nh: 0.0.0.0/32 Null0 
            p3 =  re.compile(r'^\s*(?P<mroute>[0-9\.\/]+), +configured +nh: +(?P<mroute_neighbor_address>[a-zA-Z0-9\.\/]+) +(?P<mroute_interface_name>[a-zA-Z0-9\.]+)$')
            m = p3.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                mroute_interface_name = str(m.groupdict()['mroute_interface_name'])
                mroute_neighbor_address = str(m.groupdict()['mroute_neighbor_address'])
                #path = m.groupdict()['path']


                if 'mroute' not in static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'] = {}
                if mroute not in static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute']:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute] = {} 

                if 'path' not in static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'] = {}

                path = mroute_neighbor_address + ' ' + mroute_interface_name

                if path not in static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path']:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path] = {}

                static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path]['mroute_interface_name'] = mroute_interface_name
                static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path]['mroute_neighbor_address'] = mroute_neighbor_address
                continue

            # 10.2.2.2/32, configured nh: 0.0.0.0/32%sanity1 Vlan2
            # 10.2.2.2/32, configured nh: 0.0.0.0/32%sanity1 Vlan2
            p3_1 = re.compile(r'^\s*(?P<mroute>[0-9\.\/]+), +configured +nh: +(?P<mroute_neighbor_address>[a-zA-Z0-9\.\/\%\s]+)$')
            m = p3_1.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                mroute_neighbor_address = str(m.groupdict()['mroute_neighbor_address'])

                if 'mroute' not in static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'] = {}
                if mroute not in static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute']:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute] = {} 
                if 'path' not in static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'] = {}
                path = mroute_neighbor_address
                if path not in static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path']:
                    static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path] = {}
                static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path]['mroute_neighbor_address'] = mroute_neighbor_address
                continue

            # (installed in urib) 
            p4 = re.compile(r'^\s*(?P<urib>(\(installed in urib\))+)$')
            m = p4.match(line)
            if m:
                static_routemulticast_dict['static_routemulticast']['vrf'][vrf]['af_name'][af_name]['mroute'][mroute]['path'][path]['urib'] = True
                continue

        return static_routemulticast_dict


###############################################################################
#                         Show ipv6 static-route multicast
###############################################################################


class ShowIpv6StaticRouteMulticastSchema(MetaParser):
    # schema for show ipv6 static-route multicast 

    schema = {'ipv6_static_routemulticast':
                                    {'vrf':
                                        {Any():
                                            {'mroute':
                                                {Any():
                                                    {'path':
                                                        {Any():
                                                            {'mroute_neighbor_address': str,
                                                             'nh_vrf': str,
                                                             'reslv_tid': str,
                                                             'mroute_interface_name': str,
                                                             'rnh_status': str,
                                                             'bfd_enable': bool,
                                                             'preference': str
                                                            },
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
            p1 = re.compile(r'^\s*IPv6 +Configured +Static +Routes +for +VRF +(?P<vrf>[a-zA-Z0-9\(\)\"]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"',"")
                vrf = vrf.replace("(","_")
                vrf = vrf.replace(")","")

                if 'ipv6_static_routemulticast' not in ipv6_static_routemulticast_dict:
                    ipv6_static_routemulticast_dict['ipv6_static_routemulticast'] = {}
                if 'vrf' not in ipv6_static_routemulticast_dict['ipv6_static_routemulticast']:
                    ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'] = {}
                if vrf not in ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf']:
                    ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf] = {}
                    continue

            # 126::/16 -> Null0, preference: 1
            p2 = re.compile(r'^\s*(?P<mroute>[a-zA-Z0-9\:\/]+) +-> +Null0, preference: +(?P<preference>[0-9]+)$')
            m = p2.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                preference = m.groupdict()['preference']

                if 'mroute' not in ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]:
                    ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'] = {}
                if mroute not in ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute']:
                    ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute] = {}                
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
            p4 =  re.compile(r'^\s*real-next-hop: +(?P<mroute_neighbor_address>[a-zA-Z0-9\:]+), +interface: +(?P<mroute_interface_name>[a-zA-Z0-9\/]+)$')
            m = p4.match(line)
            if m:
                mroute_neighbor_address = m.groupdict()['mroute_neighbor_address']
                mroute_interface_name = m.groupdict()['mroute_interface_name']

                if 'path' not in ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]:
                    ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path'] = {}

                path = mroute_neighbor_address + ' ' + mroute_interface_name

                if path not in ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path']:
                    ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path'][path] = {}

                ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path'][path]['mroute_neighbor_address'] = mroute_neighbor_address
                ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path'][path]['mroute_interface_name'] = mroute_interface_name
                ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path'][path]['preference'] = preference
                ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path'][path]['nh_vrf'] = nh_vrf
                ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path'][path]['reslv_tid'] = reslv_tid
                continue

            # rnh(not installed in u6rib) 
            p5 = re.compile(r'^\s*rnh(?P<rnh_status>[a-zA-Z0-9\(\)\s]+)$')
            m = p5.match(line)
            if m:
                rnh_status = str(m.groupdict()['rnh_status'])
                rnh_status = rnh_status.replace("(","")
                rnh_status = rnh_status.replace(")","")

                ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path'][path]['rnh_status'] = rnh_status
                continue

            # bfd_enabled no
            p6 = re.compile(r'^\s*bfd_enabled +(?P<bfd_enable>(no)+)$')
            m = p6.match(line)
            if m:
                bfd_enable = m.groupdict()['bfd_enable']

                ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path'][path]['bfd_enable'] = False
                continue

            p6 = re.compile(r'^\s*bfd_enabled +(?P<bfd_enable>(yes)+)$')
            m = p6.match(line)
            if m:
                bfd_enable = m.groupdict()['bfd_enable']

                ipv6_static_routemulticast_dict['ipv6_static_routemulticast']['vrf'][vrf]['mroute'][mroute]['path'][path]['bfd_enable'] = True
                continue
        
        return ipv6_static_routemulticast_dict


