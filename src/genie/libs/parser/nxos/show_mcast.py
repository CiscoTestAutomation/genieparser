"""show_mcast.py

NXOS parsers for the following show commands:

    * show ip mroute vrf all
    * Show ipv6 mroute vrf all
    * Show ip static-route multicast
    * Show ipv6 static-route multicast

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.libs.parser.nxos.show_vrf import  ShowVrf

# ===================================
# Parser for 'show ip mroute vrf all'
# ===================================

class ShowIpMrouteVrfAllSchema(MetaParser):
    """Schema for show ip mroute vrf all"""

    schema = {'vrf':         
                {Any():
                    {'address_family':
                        {Any(): 
                            {Optional('multicast_group'): 
                                {Any(): 
                                    {Optional('source_address'): 
                                        {Any(): 
                                            {Optional('uptime'): str,
                                             Optional('flags'): str,
                                             Optional('oil_count'): int,
                                             Optional('bidir'): bool,
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
                },
            }

class ShowIpMrouteVrfAll(ShowIpMrouteVrfAllSchema):
    """Parser for show ip mroute vrf all"""

    cli_command = 'show ip mroute vrf all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        mroute_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # IP Multicast Routing Table for VRF "default" 
            p1 = re.compile(r'^\s*(?P<address_family>[\w\W]+) [mM]ulticast'
                             ' +[rR]outing +[tT]able +for +VRF '
                            '+(?P<vrf>[a-zA-Z0-9\"]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"',"")
                address_family = m.groupdict()['address_family'].lower()
                address_family += 'v4'

                if 'vrf' not in mroute_dict:
                    mroute_dict['vrf'] = {}
                if vrf not in mroute_dict['vrf']:
                    mroute_dict['vrf'][vrf] = {}
                if 'address_family' not in mroute_dict['vrf'][vrf]:
                    mroute_dict['vrf'][vrf]['address_family'] = {}
                if address_family not in mroute_dict['vrf'][vrf]['address_family']:
                    mroute_dict['vrf'][vrf]['address_family'][address_family] = {}
                continue

            # (*, 232.0.0.0/8), uptime: 9w2d, pim ip 
            # (*, 228.0.0.0/8), bidir, uptime: 10w5d, pim ip 
            p2 = re.compile(r'^\s*\((?P<source_address>[0-9\.\*\/]+),'
                             ' +(?P<multicast_group>[0-9\.\/]+)\),'
                             ' *(?P<bidir>(\S+))? *uptime:'
                             ' +(?P<uptime>[0-9a-zA-Z\:\.]+)(,)?(?:'
                             ' *(?P<flag>[a-zA-Z\(\)\s]+))?$')
            m = p2.match(line)
            if m:
                source_address = m.groupdict()['source_address']
                multicast_group = m.groupdict()['multicast_group']
                uptime = m.groupdict()['uptime']
                flag = m.groupdict()['flag']
                bidir = m.groupdict()['bidir']
                if flag:
                    flag = ' '.join(sorted(flag.split()))

                if 'multicast_group' not in mroute_dict['vrf'][vrf]['address_family'][address_family]:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'] = {}
                if multicast_group not in mroute_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group']:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group] = {}
                if 'source_address' not in mroute_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group'][multicast_group]:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'] = {}
                if source_address not in mroute_dict['vrf'][vrf]['address_family'][address_family]\
                        ['multicast_group'][multicast_group]['source_address']:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                        ['source_address'][source_address] = {}
                mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]['uptime'] = uptime
                mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]['flags'] = ' '.join(sorted(flag.split()))
                if bidir:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                        ['source_address'][source_address]['bidir'] = True

                continue

            # Incoming interface: Null, RPF nbr: 0.0.0.0 
            p3 = re.compile(r'^\s*Incoming +interface:'
                             ' +(?P<incoming_interface>[a-zA-Z0-9\/\-\.]+),'
                             ' +RPF +nbr: +(?P<rpf_nbr>[0-9\.]+)$')
            m = p3.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']
                rpf_nbr = m.groupdict()['rpf_nbr']

                if 'incoming_interface_list' not in mroute_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group'][multicast_group]['source_address'][source_address]:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]['incoming_interface_list'] = {}
                if incoming_interface not in mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group']\
                [multicast_group]['source_address'][source_address]['incoming_interface_list']:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]\
                    ['incoming_interface_list'][incoming_interface] = {}
                mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]['source_address']\
                [source_address]['incoming_interface_list'][incoming_interface]['rpf_nbr'] = rpf_nbr
                continue

            # Outgoing interface list: (count: 0) 
            p4 =  re.compile(r'^\s*Outgoing +interface +list: +\(count:'
                              ' +(?P<oil_count>[0-9]+)\)$')
            m = p4.match(line)
            if m:
                oil_count = int(m.groupdict()['oil_count'])
                mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                ['source_address'][source_address]['oil_count'] = oil_count
                continue

            # loopback2, uptime: 3d11h, igmp 
            p5 = re.compile(r'^\s*(?:(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+),)?'
                             ' +uptime: +(?:(?P<oil_uptime>[a-zA-Z0-9\:]+),)?'
                             ' +(?:(?P<oil_flags>[a-zA-Z\(\)\s]+))?( *\((?P<rpf>\w+)\))?$')
            m = p5.match(line)
            if m:
                outgoing_interface = m.groupdict()['outgoing_interface']
                oil_uptime = m.groupdict()['oil_uptime']
                oil_flags = m.groupdict()['oil_flags']

                if 'outgoing_interface_list' not in mroute_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group'][multicast_group]['source_address'][source_address]:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]['outgoing_interface_list'] = {}
                if outgoing_interface not in mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group']\
                [multicast_group]['source_address'][source_address]['outgoing_interface_list']:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]['outgoing_interface_list']\
                    [outgoing_interface] = {}
                mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                ['source_address'][source_address]['outgoing_interface_list']\
                [outgoing_interface]['oil_uptime'] = oil_uptime
                mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                ['source_address'][source_address]['outgoing_interface_list']\
                [outgoing_interface]['oil_flags'] = ' '.join(sorted(oil_flags.split()))
                continue

        return mroute_dict


# =====================================
# Schema for 'show ipv6 mroute vrf all'
# =====================================

class ShowIpv6MrouteVrfAllSchema(MetaParser):
    """Schema for show ipv6 mroute vrf all"""
    schema = {'vrf': 
                {Any():
                    {'address_family':
                        {Any(): 
                            {Optional('multicast_group'): 
                                {Any(): 
                                    {Optional('source_address'): 
                                        {Any(): 
                                            {Optional('uptime'): str,
                                             Optional('flags'): str,
                                             Optional('oil_count'): str,
                                             Optional('bidir'): bool,
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
                    },
                },
            }

class ShowIpv6MrouteVrfAll(ShowIpv6MrouteVrfAllSchema):
    """Parser for show ipv6 mroute vrf all"""

    cli_command = 'show ipv6 mroute vrf all'

    def cli(self, output=None):
        # Parser for show ipv6 mroute vrf all
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ipv6_mroute_vrf_all_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # IPv6 Multicast Routing Table for VRF "default
            p1 = re.compile(r'^\s*(?P<address_family>[\w\W]+) [mM]ulticast'
                             ' +[rR]outing +[tT]able +for +VRF'
                             ' +(?P<vrf>[a-zA-Z0-9\"]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"',"")
                address_family = m.groupdict()['address_family'].lower()
                if 'vrf' not in ipv6_mroute_vrf_all_dict:
                    ipv6_mroute_vrf_all_dict['vrf'] = {}
                if vrf not in ipv6_mroute_vrf_all_dict['vrf']:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf] = {}
                if 'address_family' not in ipv6_mroute_vrf_all_dict['vrf'][vrf]:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'] = {}
                if address_family not in ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family']:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family] = {}
                continue

            # (*, ff30::/12), uptime: 3d11h, pim6 ipv6
            # (*, ff03:3::/64), bidir, uptime: 10w5d, pim6 
            p2 = re.compile(r'^\s*\((?P<source_address>(\S+)),'
                             ' +(?P<multicast_group>(\S+))\),'
                             ' *(?P<bidir>(\S+),)? *uptime:'
                             ' +(?P<uptime>[0-9a-zA-Z\:\.]+)(,)?(?:'
                             ' *(?P<flag>[a-zA-Z0-9\s]+))?$')
            m = p2.match(line)
            if m:
                source_address = m.groupdict()['source_address']
                multicast_group = m.groupdict()['multicast_group']
                uptime = m.groupdict()['uptime']
                flag = m.groupdict()['flag']
                bidir = m.groupdict()['bidir']
                if flag:
                    flag = ' '.join(sorted(flag.split()))

                if 'multicast_group' not in ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'] = {}
                if multicast_group not in ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group']:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group']\
                    [multicast_group] = {}
                if 'source_address' not in ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group'][multicast_group]:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group']\
                    [multicast_group]['source_address'] = {}
                if source_address not in ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]\
                    ['multicast_group'][multicast_group]['source_address']:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group']\
                        [multicast_group]['source_address'][source_address] = {}
                ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group']\
                    [multicast_group]['source_address'][source_address]['uptime'] = uptime
                ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group']\
                    [multicast_group]['source_address'][source_address]['flags'] = flag
                if bidir:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group']\
                    [multicast_group]['source_address'][source_address]['bidir'] = True
                continue

            # Incoming interface: Null, RPF nbr: 0::
            p3 =  re.compile(r'^\s*Incoming +interface: +(?P<incoming_interface>[a-zA-Z0-9\/\.]+),'
                              ' +RPF +nbr: +(?P<rpf_nbr>[a-zA-Z0-9\:\,\s]+)$')
            m = p3.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']
                rpf_nbr = m.groupdict()['rpf_nbr']
                
                if 'incoming_interface_list' not in ipv6_mroute_vrf_all_dict['vrf']\
                [vrf]['address_family'][address_family]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]['incoming_interface_list'] = {}
                if incoming_interface not in ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group'][multicast_group]['source_address']\
                [source_address]['incoming_interface_list']:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group']\
                    [multicast_group]['source_address'][source_address]\
                    ['incoming_interface_list'][incoming_interface] = {}
                ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group']\
                [multicast_group]['source_address'][source_address]\
                ['incoming_interface_list'][incoming_interface]['rpf_nbr'] = rpf_nbr
                continue

            # Outgoing interface list: (count: 0)
            p4 =  re.compile(r'^\s*Outgoing +interface +list: +\(count:'
                              ' +(?P<oil_count>[0-9]+)\)$')
            m = p4.match(line)
            if m:
                oil_count = str(m.groupdict()['oil_count'])
                ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                ['source_address'][source_address]['oil_count'] = oil_count
                continue

            # loopback2, uptime: 3d11h, igmp
            p5 = re.compile(r'^\s*(?:(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+),'
                             ')? +uptime: +(?:(?P<oil_uptime>[a-zA-Z0-9\:]+),)?'
                             ' +(?:(?P<oil_flags>[a-zA-Z0-9\s]+),)?$')
            m = p5.match(line)
            if m:
                outgoing_interface = m.groupdict()['outgoing_interface']
                oil_uptime = m.groupdict()['oil_uptime']
                oil_flags = m.groupdict()['oil_flags']

                if 'outgoing_interface_list' not in ipv6_mroute_vrf_all_dict['vrf']\
                [vrf]['address_family'][address_family]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]['outgoing_interface_list'] = {}
                if outgoing_interface not in ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group'][multicast_group]['source_address']\
                [source_address]['outgoing_interface_list']:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]['outgoing_interface_list'][outgoing_interface] = {}

                ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                ['source_address'][source_address]['outgoing_interface_list']\
                [outgoing_interface]['oil_uptime'] = oil_uptime
                ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                ['source_address'][source_address]['outgoing_interface_list']\
                [outgoing_interface]['oil_flags'] = oil_flags
                continue

            p5_1 = re.compile(r'^\s*(?:(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+)'
                               ',)? +uptime: +(?:(?P<oil_uptime>[a-zA-Z0-9\:]+),)?'
                               ' +(?:(?P<oil_flags>[a-zA-Z0-9\s]+),)?'
                               ' +(?P<oif_rpf>(\(RPF\))+)*$')
            m = p5_1.match(line)
            if m:
                outgoing_interface = m.groupdict()['outgoing_interface']
                oil_uptime = m.groupdict()['oil_uptime']
                oil_flags = m.groupdict()['oil_flags']
                oif_rpf = m.groupdict()['oif_rpf']

                if 'outgoing_interface_list' not in ipv6_mroute_vrf_all_dict['vrf']\
                [vrf]['address_family'][address_family]['multicast_group'][multicast_group]['source_address'][source_address]:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]['outgoing_interface_list'] = {}
                if outgoing_interface not in ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group'][multicast_group]['source_address'][source_address]['outgoing_interface_list']:
                    ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'][source_address]['outgoing_interface_list'][outgoing_interface] = {}

                ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                ['source_address'][source_address]['outgoing_interface_list']\
                [outgoing_interface]['oil_uptime'] = oil_uptime
                ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                ['source_address'][source_address]['outgoing_interface_list']\
                [outgoing_interface]['oil_flags'] = oil_flags
                ipv6_mroute_vrf_all_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                ['source_address'][source_address]['outgoing_interface_list']\
                [outgoing_interface]['oif_rpf'] = True

        return ipv6_mroute_vrf_all_dict


# ===========================================
# Schema for 'show ip static route multicast'
# ===========================================
class ShowIpStaticRouteMulticastSchema(MetaParser):
    """Schema for show ip static-route multicast vrf all"""

    schema = {'vrf': 
                {Any():
                    {'address_family':
                        {Any():
                            {'mroute':
                                {Any():
                                    {'path':
                                        {Any():
                                            {'neighbor_address': str,
                                             Optional('interface_name'): str,
                                             Optional('vrf_id'): str,
                                             Optional('urib'): bool
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
    """Parser for show ip static-route multicast vrf all"""

    cli_command = 'show ip static-route multicast vrf all'

    def cli(self, output=None):
        # cli implemetation of parsers

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        static_routemulticast_dict = {}

        for line in out.splitlines():
            line = line.rstrip()
            #Mstatic-route for VRF "default"(1) 
            p1 = re.compile(r'^\s*(Static-route|Mstatic-route) +for +VRF'
                             ' +(?P<vrf>[a-zA-Z0-9\"]+) *\((?P<vrf_id>[0-9]+)\)$')
                              
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
            p2 = re.compile(r'^\s*(?P<address_family>[a-zA-Z0-9]+)'
                             ' +(MStatic|Unicast Static) +Routes:$')
            m = p2.match(line)
            if m:
                address_family = str(m.groupdict()['address_family']).lower()
                
                if 'address_family' not in static_routemulticast_dict['vrf'][vrf]:
                    static_routemulticast_dict['vrf'][vrf]['address_family'] = {}
                if address_family not in static_routemulticast_dict['vrf'][vrf]['address_family']:
                    static_routemulticast_dict['vrf'][vrf]['address_family'][address_family] = {}
                continue

            #10.49.0.0/8, configured nh: 0.0.0.0/32 Null0 
            p3 =  re.compile(r'^\s*(?P<mroute>[0-9\.\/]+), +configured +nh:'
                              ' +(?P<neighbor_address>[a-zA-Z0-9\.\/]+)'
                              ' +(?P<interface_name>[a-zA-Z0-9\.]+)$')
            m = p3.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                interface_name = str(m.groupdict()['interface_name'])
                neighbor_address = str(m.groupdict()['neighbor_address'])


                if 'mroute' not in static_routemulticast_dict['vrf'][vrf]\
                ['address_family'][address_family]:
                    static_routemulticast_dict['vrf'][vrf]['address_family']\
                    [address_family]['mroute'] = {}
                if mroute not in static_routemulticast_dict['vrf'][vrf]\
                ['address_family'][address_family]['mroute']:
                    static_routemulticast_dict['vrf'][vrf]['address_family']\
                    [address_family]['mroute'][mroute] = {} 

                if 'path' not in static_routemulticast_dict['vrf'][vrf]\
                ['address_family'][address_family]['mroute'][mroute]:
                    static_routemulticast_dict['vrf'][vrf]['address_family']\
                    [address_family]['mroute'][mroute]['path'] = {}

                path = neighbor_address + ' ' + interface_name

                if path not in static_routemulticast_dict['vrf'][vrf]\
                ['address_family'][address_family]['mroute'][mroute]['path']:
                    static_routemulticast_dict['vrf'][vrf]['address_family']\
                    [address_family]['mroute'][mroute]['path'][path] = {}

                static_routemulticast_dict['vrf'][vrf]['address_family'][address_family]\
                ['mroute'][mroute]['path'][path]['interface_name'] = interface_name
                static_routemulticast_dict['vrf'][vrf]['address_family'][address_family]\
                ['mroute'][mroute]['path'][path]['neighbor_address'] = neighbor_address
                static_routemulticast_dict['vrf'][vrf]['address_family'][address_family]\
                ['mroute'][mroute]['path'][path]['vrf_id'] = vrf_id
                continue

            # 10.2.2.2/32, configured nh: 0.0.0.0/32%sanity1 Vlan2
            p3_1 = re.compile(r'^\s*(?P<mroute>[0-9\.\/]+), +configured +nh:'
                               ' +(?P<neighbor_address>[a-zA-Z0-9\.\/\%\s]+)$')
            m = p3_1.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                neighbor_address = str(m.groupdict()['neighbor_address'])

                if 'mroute' not in static_routemulticast_dict['vrf'][vrf]\
                ['address_family'][address_family]:
                    static_routemulticast_dict['vrf'][vrf]['address_family']\
                    [address_family]['mroute'] = {}
                if mroute not in static_routemulticast_dict['vrf'][vrf]\
                ['address_family'][address_family]['mroute']:
                    static_routemulticast_dict['vrf'][vrf]['address_family']\
                    [address_family]['mroute'][mroute] = {} 
                if 'path' not in static_routemulticast_dict['vrf'][vrf]\
                ['address_family'][address_family]['mroute'][mroute]:
                    static_routemulticast_dict['vrf'][vrf]['address_family']\
                    [address_family]['mroute'][mroute]['path'] = {}
                path = neighbor_address
                if path not in static_routemulticast_dict['vrf'][vrf]\
                ['address_family'][address_family]['mroute'][mroute]['path']:
                    static_routemulticast_dict['vrf'][vrf]['address_family']\
                    [address_family]['mroute'][mroute]['path'][path] = {}
                static_routemulticast_dict['vrf'][vrf]['address_family']\
                [address_family]['mroute'][mroute]['path'][path]\
                ['neighbor_address'] = neighbor_address
                static_routemulticast_dict['vrf'][vrf]['address_family']\
                [address_family]['mroute'][mroute]['path'][path]['vrf_id'] = vrf_id
                continue

            # (installed in urib) 
            p4 = re.compile(r'^\s*(?P<urib>(\(installed in urib\))+)$')
            m = p4.match(line)
            if m:
                urib = bool(m.groupdict()['urib'])
                static_routemulticast_dict['vrf'][vrf]['address_family']\
                [address_family]['mroute'][mroute]['path'][path]['urib'] = True
                continue

        return static_routemulticast_dict


# =============================================
# Parser for 'show ipv6 static route multicast'
# =============================================

class ShowIpv6StaticRouteMulticastSchema(MetaParser):
    """Schema for show ipv6 static-route multicast vrf all"""

    schema = {'vrf':
                {Any():
                    {'address_family':
                        {Any():
                            {Optional('mroute'):
                                {Any():
                                    {Optional('path'):
                                        {Any():
                                            {Optional('neighbor_address'): str,
                                             Optional('nh_vrf'): str,
                                             Optional('reslv_tid'): str,
                                             Optional('interface_name'): str,
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
                    },
                },
            }

class ShowIpv6StaticRouteMulticast(ShowIpv6StaticRouteMulticastSchema):
    """Parser for show ipv6 static-route multicast vrf all"""

    cli_command = 'show ipv6 static-route multicast vrf all'

    def cli(self, output=None):
        # cli implementation of parsers '''
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ipv6_multicast_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # IPv6 Configured Static Routes for VRF "default"(1) 
            p1 = re.compile(r'^\s*(?P<address_family>[\w\W]+) +Configured +Static +Routes +for +VRF'
                             ' +(?P<vrf>[a-zA-Z0-9\"]+) *\((?P<vrf_id>[0-9]+)\)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"',"")
                vrf_id = m.groupdict()['vrf_id']
                vrf_id = vrf_id.replace("(","")
                vrf_id = vrf_id.replace(")","")
                address_family = m.groupdict()['address_family'].lower()

                if 'vrf' not in ipv6_multicast_dict:
                    ipv6_multicast_dict['vrf'] = {}
                if vrf not in ipv6_multicast_dict['vrf']:
                    ipv6_multicast_dict['vrf'][vrf] = {}
                if 'address_family' not in ipv6_multicast_dict['vrf'][vrf]:
                    ipv6_multicast_dict['vrf'][vrf]['address_family'] = {}
                if address_family not in ipv6_multicast_dict['vrf'][vrf]['address_family']:
                    ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family] = {}
                continue

            # 126::/16 -> Null0, preference: 1
            p2 = re.compile(r'^\s*(?P<mroute>[a-zA-Z0-9\:\/]+) +->'
                             ' +(?P<mroute_int>[\w\W]+), preference:'
                             ' +(?P<preference>[0-9]+)$')
            m = p2.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                preference = m.groupdict()['preference']
                mroute_int = m.groupdict()['mroute_int']

                if 'mroute' not in ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]:
                    ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'] = {}
                if mroute not in ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute']:
                    ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute] = {}                
                continue

            # nh_vrf(default) reslv_tid 80000001 
            p3 = re.compile(r'^\s*nh_vrf *(?P<nh_vrf>[a-zA-Z0-9\(\)]+)'
                             ' +reslv_tid +(?P<reslv_tid>[0-9]+)$')
            m = p3.match(line)
            if m:
                nh_vrf = m.groupdict()['nh_vrf']
                nh_vrf = nh_vrf.replace("(","")
                nh_vrf = nh_vrf.replace(")","")
                reslv_tid = m.groupdict()['reslv_tid']
                continue

            # real-next-hop: 0::, interface: Null0 
            p4 =  re.compile(r'^\s*real-next-hop: +(?P<neighbor_address>[a-zA-Z0-9\:]+),'
                              ' +interface: +(?P<interface_name>[\w\W]+)$')
            m = p4.match(line)
            if m:
                neighbor_address = m.groupdict()['neighbor_address']
                interface_name = m.groupdict()['interface_name']

                if 'path' not in ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]\
                ['mroute'][mroute]:
                    ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute']\
                    [mroute]['path'] = {}

                path = neighbor_address + ' ' + interface_name

                if path not in ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]\
                ['mroute'][mroute]['path']:
                    ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute']\
                    [mroute]['path'][path] = {}

                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['neighbor_address'] = neighbor_address
                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['interface_name'] = interface_name
                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['preference'] = preference
                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['nh_vrf'] = nh_vrf
                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['reslv_tid'] = reslv_tid
                continue

            # rnh(not installed in u6rib) 
            p5 = re.compile(r'^\s*rnh(?P<rnh_status>[a-zA-Z0-9\(\)\s]+)$')
            m = p5.match(line)
            if m:
                rnh_status = str(m.groupdict()['rnh_status'])
                rnh_status = rnh_status.replace("(","")
                rnh_status = rnh_status.replace(")","")

                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['rnh_status'] = rnh_status
                continue

            # bfd_enabled no
            p6 = re.compile(r'^\s*bfd_enabled +(?P<bfd_enable>(no)+)$')
            m = p6.match(line)
            if m:
                bfd_enable = m.groupdict()['bfd_enable']

                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['bfd_enable'] = False
                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['vrf_id'] = vrf_id
                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['mroute_int'] = mroute_int
                continue

            # bfd_enabled yes
            p6 = re.compile(r'^\s*bfd_enabled +(?P<bfd_enable>(yes)+)$')
            m = p6.match(line)
            if m:
                bfd_enable = m.groupdict()['bfd_enable']

                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['bfd_enable'] = True
                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['vrf_id'] = vrf_id
                ipv6_multicast_dict['vrf'][vrf]['address_family'][address_family]['mroute'][mroute]\
                ['path'][path]['mroute_int'] = mroute_int
                continue
        
        return ipv6_multicast_dict

# =================================================================
#  schema for show forwarding distribution multicast route vrf all
# ================================================================
class ShowForwardingDistributionMulticastRouteSchema(MetaParser):
    """Schema for:
        show forwarding distribution multicast route
        show forwarding distribution multicast route vrf <vrf>
        show forwarding distribution multicast route vrf all"""

    schema = {
        "distribution": {
            "multicast": {
                "route": {
                    "vrf": {
                        Any(): {
                            "address_family": {
                                Any(): {
                                    "num_groups": int,
                                    "gaddr": {
                                        Any(): {
                                            "grp_len": int,
                                            "saddr": {
                                                Any(): {
                                                    "rpf_ifname": str,
                                                    Optional("src_len"): int,
                                                    Optional("flags"): str,
                                                    "rcv_packets": int,
                                                    "rcv_bytes": int,
                                                    "num_of_oifs": int,
                                                    Optional("oifs"): {
                                                        "oif_index": int,
                                                        Any(): {
                                                            Optional('oif'): str,
                                                            Optional("encap"): str,
                                                            Optional("mem_l2_ports"): str,
                                                            Optional("l2_oiflist_index"): int,
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# =================================================================
#  Parser for show forwarding distribution multicast route vrf all
# =================================================================
class ShowForwardingDistributionMulticastRoute(ShowForwardingDistributionMulticastRouteSchema):
    """parser for:
        show forwarding distribution multicast route
        show forwarding distribution multicast route vrf <vrf>
        show forwarding distribution multicast route vrf all"""
    cli_command = ['show forwarding distribution multicast route vrf {vrf}',
                   'show forwarding distribution multicast route']

    def cli(self, vrf="", output=None):
        # finding vrf names
        vrf_dict = {}

        if vrf:
            if vrf == 'all':
                showparser = ShowVrf(device=self.device)
                vrfs_list = showparser.parse()
                for vrf_name in vrfs_list['vrfs'].keys():
                    vrf_id = vrfs_list['vrfs'][vrf_name]['vrf_id']
                    vrf_dict.update({vrf_id: vrf_name})

            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            vrf = 'default'
            cmd = self.cli_command[1]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # IPv4 Multicast Routing Table for table-id: 1
        # IPv4 Multicast Routing Table for table-id: 0x3
        p1 = re.compile(r'^\s*IPv4 +Multicast +Routing +Table +for +table\-id: +(?P<vrf_id>(?!wildcard)[\S]+)$')

        # Total number of groups: 5
        p2 = re.compile(r'^\s*Total +number +of +groups: +(?P<total_number_group>[\d]+)$')

        #  (*, 224.0.0.0/4), RPF Interface: NULL, flags: D
        #  (*, 231.100.1.1/32), RPF Interface: Ethernet1/2, flags: GLd
        p3 = re.compile(r'^\s*\((?P<saddr>[\w\/\.\*]+), +(?P<gaddr>[\w\/\.]+)\), +RPF +Interface:'
               ' +(?P<rpf_ifname>[\w\/\-]+), flags:( +(?P<flags>[\w]+))?$')

        #   Received Packets: 0 Bytes: 0
        p4 = re.compile(r'^\s*Received +Packets: +(?P<rcv_packets>[\d]+) +Bytes: +(?P<rcv_bytes>[\d]+)$')

        #   Number of Outgoing Interfaces: 0
        p5 = re.compile(r'^\s*Number +of +Outgoing +Interfaces: +(?P<num_of_oifs>[\d]+)$')

        #   Null Outgoing Interface List
        p6 = re.compile(r'^\s*Null +Outgoing +Interface +List$')

        #   Outgoing Interface List Index: 30
        p7 = re.compile(r'^\s*Outgoing +Interface +List +Index: +(?P<oif_index>[\d]+)$')

        #    nve1
        #    Vlan100 (Vxlan Encap)
        p8 = re.compile(r'^(?P<space>\s{6})(?P<oif>[\w\-\/]+)( +\((?P<encap>[\w]+) +Encap\))?$')

        #     ( Mem L2 Ports: nve1 )
        #     ( Mem L2 Ports: port-channel1 nve1 )
        p9 = re.compile(r'\s*\( +Mem +L2 +Ports: +(?P<mem_l2_ports>[\w\s\-\/]+) +\)$')

        #     l2_oiflist_index: 19
        p10 = re.compile(r'\s*l2_oiflist_index: +(?P<l2_oiflist_index>[\d]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                try:
                    vrfId = int(group['vrf_id'])
                except:
                    vrfId = int(group['vrf_id'],16)

                if vrf_dict:
                    for vrf_id, vrf_name in vrf_dict.items():
                        if vrf_id == vrfId:
                            vrf = vrf_name

                address_family_dict = result_dict.setdefault('distribution', {}).\
                    setdefault('multicast', {}).\
                    setdefault('route', {}).setdefault('vrf', {}).\
                    setdefault(vrf, {}).setdefault('address_family', {}).setdefault('ipv4', {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                address_family_dict.update({'num_groups': int(group['total_number_group'])})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                gaddr = group['gaddr']
                gaddr_dict = address_family_dict.setdefault('gaddr', {}).setdefault(gaddr, {})
                splited_gaddr = ""
                if '/' in gaddr:
                    splited_gaddr = int(gaddr.split('/')[1])

                gaddr_dict.update({'grp_len': splited_gaddr})

                saddr =group['saddr']
                saddr_dict = gaddr_dict.setdefault('saddr', {}).setdefault(saddr, {})
                if '/' in saddr:
                    saddr_dict.update({'src_len': int(saddr.split('/')[1])})
                saddr_dict.update({'rpf_ifname': group['rpf_ifname']})
                if group['flags']:
                    saddr_dict.update({'flags': group['flags']})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                saddr_dict.update({k:int(v) for k,v in group.items()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                saddr_dict.update({'num_of_oifs': int(group['num_of_oifs'])})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                oif_dict = saddr_dict.setdefault('oifs', {})
                oif_dict.update({'oif_index': int(group['oif_index'])})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                sub_oif_dict = oif_dict.setdefault(group['oif'], {})
                sub_oif_dict.update({'oif': group['oif']})
                if group['encap']:
                    sub_oif_dict.update({'encap': group['encap'].lower()})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                sub_oif_dict.update({'mem_l2_ports': group['mem_l2_ports']})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                sub_oif_dict.update({'l2_oiflist_index': int(group['l2_oiflist_index'])})
                continue

        return result_dict
