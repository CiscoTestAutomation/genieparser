###############################################################################
#                           Unitest for Show feature
###############################################################################

import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from parser.nxos.show_mcast import ShowIpStaticRouteMulticast, ShowIpv6StaticRouteMulticast, ShowFeature, ShowIpMrouteVrfAll, ShowIpv6MrouteVrfAll

class test_show_feature(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'feature': 
    {'bash-shell': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'bfd': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'bgp': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'bulkstat': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'cable-management': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'catena': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'container-tracker': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'dhcp': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'dot1x': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'eigrp': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                },
             '10': 
                {'state': 'disabled'
                },
             '11': 
                {'state': 'disabled'
                },
             '12': 
                {'state': 'disabled'
                },
             '13': 
                {'state': 'disabled'
                },
             '14': 
                {'state': 'disabled'
                },
             '15': 
                {'state': 'disabled'
                },
             '16': 
                {'state': 'disabled'
                },
             '2': 
                {'state': 'disabled'
                },
             '3': 
                {'state': 'disabled'
                },
             '4': 
                {'state': 'disabled'
                },
             '5': 
                {'state': 'disabled'
                },
             '6': 
                {'state': 'disabled'
                },
             '7': 
                {'state': 'disabled'
                },
             '8': 
                {'state': 'disabled'
                },
             '9': 
                {'state': 'disabled'
                }
            }
        },
    'eth-port-sec': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'evb': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'evc': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'evmed': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'fabric-access': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'fabric_mcast': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'hmm': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'hsrp_engine': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'icam': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'imp': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'interface-vlan': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'isis': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                },
            '10': 
                {'state': 'enabled(not-running)'
                },
            '11': 
                {'state': 'enabled(not-running)'
                },
            '12': 
                {'state': 'enabled(not-running)'
                },
            '13': 
                {'state': 'enabled(not-running)'
                },
            '14': 
                {'state': 'enabled(not-running)'
                },
            '15': 
                {'state': 'enabled(not-running)'
                },
            '16': 
                {'state': 'enabled(not-running)'
                },
            '2': 
                {'state': 'enabled(not-running)'
                },
            '3': 
                {'state': 'enabled(not-running)'
                },
            '4': 
                {'state': 'enabled(not-running)'
                },
            '5': 
                {'state': 'enabled(not-running)'
                },
            '6': 
                {'state': 'enabled(not-running)'
                },
            '7': 
                {'state': 'enabled(not-running)'
                },
            '8':
                {'state': 'enabled(not-running)'
                },
            '9': 
                {'state': 'enabled(not-running)'
                }
            }
        },
    'itd': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'l2vpn': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'lacp': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'ldap': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'ldp': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'lldp': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'macsec': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'mpls-evpn': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'mpls_oam': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'mpls_static': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'msdp': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'mvrp': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nat': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nbm': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'netflow': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'ngmvpn': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'ngoam': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'npiv': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nve': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxapi': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'nxsdk_app1': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app10':
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app11': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app12': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app13': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app14': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app15': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app16': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app17': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app18': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app19': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app2': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app20': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app21': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app22': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app23': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app24': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app25': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app26': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app27': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app28': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app29': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app3': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app30': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app31': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app32': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app4': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app5': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app6':
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app7': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app8': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_app9': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'nxsdk_mgr': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'onep': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'openflow': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'ospf': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                },
            '10': 
                {'state': 'enabled(not-running)'
                },
            '11': 
                {'state': 'enabled(not-running)'
                },
            '12': 
                {'state': 'enabled(not-running)'
                },
            '13': 
                {'state': 'enabled(not-running)'
                },
            '14': 
                {'state': 'enabled(not-running)'
                },
            '15': 
                {'state': 'enabled(not-running)'
                },
            '16': 
                {'state': 'enabled(not-running)'
                },
            '2': 
                {'state': 'enabled(not-running)'
                },
            '3': 
                {'state': 'enabled(not-running)'
                },
            '4': 
                {'state': 'enabled(not-running)'
                },
            '5': 
                {'state': 'enabled(not-running)'
                },
            '6': 
                {'state': 'enabled(not-running)'
                },
            '7': 
                {'state': 'enabled(not-running)'
                },
            '8': 
                {'state': 'enabled(not-running)'
                },
            '9': 
                {'state': 'enabled(not-running)'
                }
            }
        },
    'ospfv3': 
        {'instance': 
            {'1': 
                {'state': 'enabled(not-running)'
                },
            '10': 
                {'state': 'enabled(not-running)'
                },
            '11': 
                {'state': 'enabled(not-running)'
                },
            '12': 
                {'state': 'enabled(not-running)'
                },
            '13': 
                {'state': 'enabled(not-running)'
                },
            '14': 
                {'state': 'enabled(not-running)'
                },
            '15': 
                {'state': 'enabled(not-running)'
                },
            '16':
                {'state': 'enabled(not-running)'
                },
            '2': 
                {'state': 'enabled(not-running)'
                },
            '3': 
                {'state': 'enabled(not-running)'
                },
            '4': 
                {'state': 'enabled(not-running)'
                },
            '5': 
                {'state': 'enabled(not-running)'
                },
            '6': 
                {'state': 'enabled(not-running)'
                },
            '7': 
                {'state': 'enabled(not-running)'
                },
            '8': 
                {'state': 'enabled(not-running)'
                },
            '9': 
                {'state': 'enabled(not-running)'
                }
            }
        },
    'pbr': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'pim': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'pim6': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'plb': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'poe': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'private-vlan': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'privilege': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'ptp': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'rip': 
        {'instance': 
            {'1': 
                {'state': 'enabled(not-running)'
                },
            '2': 
                {'state': 'enabled(not-running)'
                },
            '3': 
                {'state': 'enabled(not-running)'
                },
            '4': 
                {'state': 'enabled(not-running)'
                }
            }
        },
    'rise': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'scheduler': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'scpServer': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'segment-routing': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'sflow': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'sftpServer': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'sla_responder': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'sla_sender': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'smart-channel': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'sshServer': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'tacacs': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'telemetry': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'telnetServer': 
        {'instance': 
            {'1': 
                {'state': 'enabled'
                }
            }
        },
    'tunnel': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'udld': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'vmtracker': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'vni': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'vnseg_vlan': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'vpc': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'vrrp': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'vrrpv3': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        },
    'vtp': 
        {'instance': 
            {'1': 
                {'state': 'disabled'
                }
            }
        }
    }
}


    golden_output = {'execute.return_value': '''

          Feature Name          Instance  State   
        --------------------  --------  --------
        bash-shell             1          enabled 
        bfd                    1          enabled 
        bgp                    1          enabled 
        bulkstat               1          disabled
        cable-management       1          disabled
        catena                 1          disabled
        container-tracker      1          disabled
        macsec                 1          disabled
        dhcp                   1          disabled
        dot1x                  1          disabled
        eigrp                  1          disabled
        eigrp                  2          disabled
        eigrp                  3          disabled
        eigrp                  4          disabled
        eigrp                  5          disabled
        eigrp                  6          disabled
        eigrp                  7          disabled
        eigrp                  8          disabled
        eigrp                  9          disabled
        eigrp                  10         disabled
        eigrp                  11         disabled
        eigrp                  12         disabled
        eigrp                  13         disabled
        eigrp                  14         disabled
        eigrp                  15         disabled
        eigrp                  16         disabled
        eth-port-sec           1          disabled
        evb                    1          disabled
        evc                    1          disabled
        evmed                  1          disabled
        fabric-access          1          disabled
        fabric_mcast           1          disabled
        hmm                    1          disabled
        hsrp_engine            1          disabled
        icam                   1          disabled
        imp                    1          disabled
        interface-vlan         1          enabled 
        isis                   1          enabled 
        isis                   2          enabled(not-running)
        isis                   3          enabled(not-running)
        isis                   4          enabled(not-running)
        isis                   5          enabled(not-running)
        isis                   6          enabled(not-running)
        isis                   7          enabled(not-running)
        isis                   8          enabled(not-running)
        isis                   9          enabled(not-running)
        isis                   10         enabled(not-running)
        isis                   11         enabled(not-running)
        isis                   12         enabled(not-running)
        isis                   13         enabled(not-running)
        isis                   14         enabled(not-running)
        isis                   15         enabled(not-running)
        isis                   16         enabled(not-running)
        itd                    1          disabled
        l2vpn                  1          disabled
        lacp                   1          enabled 
        ldap                   1          disabled
        ldp                    1          disabled
        lldp                   1          disabled
        mpls-evpn              1          disabled
        mpls_oam               1          disabled
        mpls_static            1          disabled
        msdp                   1          enabled 
        mvrp                   1          disabled
        nat                    1          disabled
        nbm                    1          disabled
        netflow                1          disabled
        ngmvpn                 1          disabled
        ngoam                  1          disabled
        npiv                   1          disabled
        nve                    1          disabled
        nxapi                  1          enabled 
        nxsdk_app1             1          disabled
        nxsdk_app10            1          disabled
        nxsdk_app11            1          disabled
        nxsdk_app12            1          disabled
        nxsdk_app13            1          disabled
        nxsdk_app14            1          disabled
        nxsdk_app15            1          disabled
        nxsdk_app16            1          disabled
        nxsdk_app17            1          disabled
        nxsdk_app18            1          disabled
        nxsdk_app19            1          disabled
        nxsdk_app2             1          disabled
        nxsdk_app20            1          disabled
        nxsdk_app21            1          disabled
        nxsdk_app22            1          disabled
        nxsdk_app23            1          disabled
        nxsdk_app24            1          disabled
        nxsdk_app25            1          disabled
        nxsdk_app26            1          disabled
        nxsdk_app27            1          disabled
        nxsdk_app28            1          disabled
        nxsdk_app29            1          disabled
        nxsdk_app3             1          disabled
        nxsdk_app30            1          disabled
        nxsdk_app31            1          disabled
        nxsdk_app32            1          disabled
        nxsdk_app4             1          disabled
        nxsdk_app5             1          disabled
        nxsdk_app6             1          disabled
        nxsdk_app7             1          disabled
        nxsdk_app8             1          disabled
        nxsdk_app9             1          disabled
        nxsdk_mgr              1          disabled
        onep                   1          disabled
        openflow               1          disabled
        ospf                   1          enabled 
        ospf                   2          enabled(not-running)
        ospf                   3          enabled(not-running)
        ospf                   4          enabled(not-running)
        ospf                   5          enabled(not-running)
        ospf                   6          enabled(not-running)
        ospf                   7          enabled(not-running)
        ospf                   8          enabled(not-running)
        ospf                   9          enabled(not-running)
        ospf                   10         enabled(not-running)
        ospf                   11         enabled(not-running)
        ospf                   12         enabled(not-running)
        ospf                   13         enabled(not-running)
        ospf                   14         enabled(not-running)
        ospf                   15         enabled(not-running)
        ospf                   16         enabled(not-running)
        ospfv3                 1          enabled(not-running)
        ospfv3                 2          enabled(not-running)
        ospfv3                 3          enabled(not-running)
        ospfv3                 4          enabled(not-running)
        ospfv3                 5          enabled(not-running)
        ospfv3                 6          enabled(not-running)
        ospfv3                 7          enabled(not-running)
        ospfv3                 8          enabled(not-running)
        ospfv3                 9          enabled(not-running)
        ospfv3                 10         enabled(not-running)
        ospfv3                 11         enabled(not-running)
        ospfv3                 12         enabled(not-running)
        ospfv3                 13         enabled(not-running)
        ospfv3                 14         enabled(not-running)
        ospfv3                 15         enabled(not-running)
        ospfv3                 16         enabled(not-running)
        pbr                    1          enabled 
        pim                    1          enabled 
        pim6                   1          enabled 
        plb                    1          disabled
        poe                    1          disabled
        private-vlan           1          disabled
        privilege              1          disabled
        ptp                    1          disabled
        rip                    1          enabled(not-running)
        rip                    2          enabled(not-running)
        rip                    3          enabled(not-running)
        rip                    4          enabled(not-running)
        rise                   1          disabled
        scheduler              1          disabled
        scpServer              1          disabled
        segment-routing        1          enabled 
        sflow                  1          disabled
        sftpServer             1          disabled
        sla_responder          1          disabled
        sla_sender             1          disabled
        smart-channel          1          disabled
        sshServer              1          enabled 
        tacacs                 1          disabled
        telemetry              1          disabled
        telnetServer           1          enabled 
        tunnel                 1          disabled
        udld                   1          disabled
        vmtracker              1          disabled
        vni                    1          disabled
        vnseg_vlan             1          disabled
        vpc                    1          disabled
        vrrp                   1          disabled
        vrrpv3                 1          disabled
        vtp                    1          disabled
        '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        feature_obj = ShowFeature(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = feature_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        feature_obj = ShowFeature(device=self.device)
        parsed_output = feature_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


###############################################################################
#                   Unitest for Show ip mroute vrf all
###############################################################################


class test_show_ip_mroute_vrf_all(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output =  {'ip_mroute_vrf_all': 
        {'vrf_name': 
            {'VRF1': 
                {'multicast_group': 
                    {'232.0.0.0/8': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'pim '
                                         'ip',
                                 'incoming_interface_list': 
                                    {'Null': 
                                        {'rpf_nbr': '0.0.0.0'
                                 }
                            },
                                 'oil_count': 0,
                                 'uptime': '3d11h'
                                 }
                            }
                        },
                     '239.5.5.5/32': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'igmp '
                                          'ip '
                                          'pim',
                                'incoming_interface_list': 
                                    {'Null': 
                                        {'rpf_nbr': '0.0.0.0'
                                        }
                                    },
                                'oil_count': 1,
                                'outgoing_interface_list': 
                                    {'loopback1': 
                                        {'oil_flags': 'igmp',
                                         'oil_uptime': '3d11h'
                                         }
                                    },
                                 'uptime': '3d11h'
                                 }
                            }
                        }
                    }
                },
             'VRF2': 
                {'multicast_group': 
                    {'224.192.1.10/32': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'igmp '
                                         'ip '
                                         'pim',
                                'incoming_interface_list': 
                                    {'port-channel8': 
                                        {'rpf_nbr': '159.103.50.233'
                                        }
                                    },
                                'oil_count': 3,
                                'outgoing_interface_list': 
                                    {'Vlan803': 
                                        {'oil_flags': 'igmp',
                                         'oil_uptime': '09:15:11'
                                         },
                                     'Vlan812': 
                                        {'oil_flags': 'igmp',
                                         'oil_uptime': '09:14:42'
                                         },
                                     'Vlan864': 
                                        {'oil_flags': 'igmp',
                                         'oil_uptime': '09:11:22'
                                         }
                                    },
                                'uptime': '09:15:11'
                                },
                            '192.168.112.3/32': 
                                {'flag': 'pim '
                                          'ip',
                                 'incoming_interface_list': 
                                    {'Vlan807': 
                                        {'rpf_nbr': '159.103.211.228'
                                        }
                                    },
                                 'oil_count': 1,
                                 'outgoing_interface_list': 
                                    {'port-channel9': 
                                        {'oil_flags': 'pim',
                                         'oil_uptime': '09:31:16'
                                         }
                                    },
                                'uptime': '09:31:16'
                                },
                             '192.168.112.4/32': 
                                {'flag': 'pim '
                                          'ip',
                                 'incoming_interface_list': 
                                    {'Ethernet1/1.10':
                                         {'rpf_nbr': '159.103.211.228'
                                         }
                                    },
                                 'oil_count': 1,
                                 'outgoing_interface_list': 
                                    {'Ethernet1/2.20': 
                                        {'oil_flags': 'pim',
                                         'oil_uptime': '09:31:16'
                                         }
                                    },
                                 'uptime': '09:31:16'
                                 }
                            }
                        }
                    }
                },
             'default': 
                {'multicast_group': 
                    {'232.0.0.0/8': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'pim '
                                          'ip',
                                 'incoming_interface_list': 
                                    {'Null': 
                                        {'rpf_nbr': '0.0.0.0'
                                        }
                                    },
                                 'oil_count': 0,
                                 'uptime': '9w2d'
                                 }
                            }
                        },
                     '239.1.1.1/32': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'igmp '
                                         'pim '
                                          'ip',
                                'incoming_interface_list': 
                                    {'Ethernet9/13': 
                                        {'rpf_nbr': '10.2.3.2'
                                        }
                                    },
                                'oil_count': 1,
                                'outgoing_interface_list': 
                                    {'loopback2': 
                                        {'oil_flags': 'igmp',
                                         'oil_uptime': '3d11h'
                                        }
                                    },
                                'uptime': '3d11h'
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    
    golden_output = {'execute.return_value': '''
      IP Multicast Routing Table for VRF "default"

(*, 232.0.0.0/8), uptime: 9w2d, pim ip 
  Incoming interface: Null, RPF nbr: 0.0.0.0
  Outgoing interface list: (count: 0)

(*, 239.1.1.1/32), uptime: 3d11h, igmp pim ip 
  Incoming interface: Ethernet9/13, RPF nbr: 10.2.3.2
  Outgoing interface list: (count: 1)
    loopback2, uptime: 3d11h, igmp


IP Multicast Routing Table for VRF "VRF1"

(*, 232.0.0.0/8), uptime: 3d11h, pim ip 
  Incoming interface: Null, RPF nbr: 0.0.0.0
  Outgoing interface list: (count: 0)

(*, 239.5.5.5/32), uptime: 3d11h, igmp ip pim 
  Incoming interface: Null, RPF nbr: 0.0.0.0
  Outgoing interface list: (count: 1)
    loopback1, uptime: 3d11h, igmp 

IP Multicast Routing Table for VRF "VRF2"

(*, 224.192.1.10/32), uptime: 09:15:11, igmp ip pim
   Incoming interface: port-channel8, RPF nbr: 159.103.50.233
   Outgoing interface list: (count: 3)
     Vlan864, uptime: 09:11:22, igmp
     Vlan812, uptime: 09:14:42, igmp
     Vlan803, uptime: 09:15:11, igmp

(192.168.112.3/32, 224.192.1.10/32), uptime: 09:31:16, pim ip
   Incoming interface: Vlan807, RPF nbr: 159.103.211.228
   Outgoing interface list: (count: 1)
     port-channel9, uptime: 09:31:16, pim        

(192.168.112.4/32, 224.192.1.10/32), uptime: 09:31:16, pim ip
   Incoming interface: Ethernet1/1.10, RPF nbr: 159.103.211.228
   Outgoing interface list: (count: 1)
     Ethernet1/2.20, uptime: 09:31:16, pim       
      '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_mroute_vrf_all_obj = ShowIpMrouteVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ip_mroute_vrf_all_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_mroute_vrf_all_obj = ShowIpMrouteVrfAll(device=self.device)
        parsed_output = ip_mroute_vrf_all_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


###############################################################################
#               Unitest for Show ipv6 mroute vrf all
###############################################################################    


class test_show_ipv6_mroute_vrf_all(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {'ipv6_mroute_vrf_all':
        {'vrf_name': 
            {'VRF1': 
                {'multicast_group': 
                    {'ff1e:1111::1:0/128': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'mld '
                                         'pim6 '
                                         'ipv6',
                                'incoming_interface_list': 
                                    {'loopback10': 
                                        {'rpf_nbr': '2001:9999::1'
                                        }
                                    },
                                'oil_count': 3,
                                'uptime': '00:04:03'
                                },
                            '2001::222:1:1:1234/128': 
                                {'flag': 'ipv6 '
                                         'pim6 '
                                         'm6rib',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.10': 
                                        {'rpf_nbr': '2001::222:1:1:1234, '
                                                        'internal'
                                        }
                                    },
                                'oil_count': 3,
                                'uptime': '00:04:03'
                                },
                            '2001::222:1:2:1234/128': 
                                {'flag': 'ipv6 '
                                         'pim6 '
                                         'm6rib',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'rpf_nbr': '2001::222:1:2:1234, '
                                                    'internal'
                                        }
                                    },
                                 'oil_count': 3,
                                 'outgoing_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'oif_rpf': True,
                                         'oil_flags': 'm6rib',
                                         'oil_uptime': '00:04:03'
                                         }
                                    },
                                'uptime': '00:04:03'},
                            '2001::222:2:3:1234/128': 
                                {'flag': 'pim6 '
                                         'm6rib '
                                         'ipv6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10, '
                                                    'internal'
                                         }
                                     },
                                'oil_count': 1,
                                'uptime': '00:04:03'
                                },
                            '2001::222:2:44:1234/128': 
                                {'flag': 'pim6 '
                                         'm6rib '
                                         'ipv6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10, '
                                                    'internal'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:03'
                                }
                            }
                        },
                    'ff1e:1111:ffff::/128': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'mld '
                                         'pim6 '
                                         'ipv6',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.10': 
                                        {'rpf_nbr': '2001::222:1:1:1'
                                        }
                                    },
                                'oil_count': 2,
                                'uptime': '00:04:03'
                                },
                            '2001::222:1:1:1234/128': 
                                {'flag': 'ipv6 '
                                         'pim6 '
                                         'm6rib',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.10': 
                                        {'rpf_nbr': '2001::222:1:1:1234, '
                                                      'internal'
                                        }
                                    },
                                'oil_count': 3,
                                'uptime': '00:04:03'},
                            '2001::222:1:2:1234/128': 
                                {'flag': 'ipv6 '
                                         'pim6 '
                                         'm6rib',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'rpf_nbr': '2001::222:1:2:1234, '
                                                         'internal'
                                        }
                                    },
                                'oil_count': 2,
                                'outgoing_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'oif_rpf': True,
                                         'oil_flags': 'm6rib',
                                         'oil_uptime': '00:04:03'
                                        }
                                    },
                                'uptime': '00:04:03'},
                            '2001::222:2:3:1234/128': 
                                {'flag': 'pim6 '
                                         'm6rib '
                                         'ipv6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10, '
                                                    'internal'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:03'
                                },
                            '2001::222:2:44:1234/128': 
                                {'flag': 'pim6 '
                                         'm6rib '
                                         'ipv6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10, '
                                                    'internal'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:03'
                                }
                            }
                        },
                    'ff1e:2222:ffff::/128': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'mld '
                                         'pim6 '
                                         'ipv6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:03'
                                },
                            '2001::222:1:1:1234/128': 
                                {'flag': 'ipv6 '
                                         'm6rib '
                                         'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.10': 
                                        {'rpf_nbr': '2001::222:1:1:1234'
                                        }
                                    },
                                'oil_count': 2,
                                'uptime': '00:04:03'
                                },
                            '2001::222:1:2:1234/128': 
                                {'flag': 'ipv6 '
                                         'm6rib '
                                         'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'rpf_nbr': '2001::222:1:2:1234'
                                        }
                                    },
                                'oil_count': 2,
                                'outgoing_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'oif_rpf': True,
                                         'oil_flags': 'm6rib',
                                         'oil_uptime': '00:04:03'
                                         }
                                    },
                                'uptime': '00:04:03'
                                },
                            '2001::222:2:3:1234/128': 
                                {'flag': 'ipv6 '
                                         'm6rib '
                                         'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:02'
                                },
                            '2001::222:2:44:1234/128': 
                                {'flag': 'ipv6 '
                                         'm6rib '
                                         'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:02'
                                }
                            }
                        },
                    'ff1e:2222:ffff::1:0/128': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'mld '
                                         'pim6 '
                                         'ipv6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:03'
                                },
                            '2001::222:1:1:1234/128': 
                                {'flag': 'ipv6 '
                                         'm6rib '
                                         'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.10': 
                                        {'rpf_nbr': '2001::222:1:1:1234'
                                        }
                                    },
                                'oil_count': 3,
                                'uptime': '00:04:03'
                            },
                            '2001::222:1:2:1234/128': 
                                {'flag': 'ipv6 '
                                         'm6rib '
                                         'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'rpf_nbr': '2001::222:1:2:1234'
                                        }
                                    },
                                'oil_count': 2,
                                'outgoing_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'oif_rpf': True,
                                         'oil_flags': 'm6rib',
                                         'oil_uptime': '00:04:03'
                                         }
                                    },
                                'uptime': '00:04:03'
                                }
                            }
                        },
                    'ff1e:3333::1:0/128': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'mld '
                                        'pim6 '
                                        'ipv6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:03'
                                },
                            '2001::222:1:1:1234/128': 
                                {'flag': 'ipv6 '
                                         'm6rib '
                                         'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.10': 
                                        {'rpf_nbr': '2001::222:1:1:1234'
                                        }
                                    },
                                'oil_count': 2,
                                'uptime': '00:04:03'
                            },
                            '2001::222:1:2:1234/128': 
                                {'flag': 'ipv6 '
                                         'm6rib '
                                         'pim6',
                                 'incoming_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'rpf_nbr': '2001::222:1:2:1234'
                                        }
                                    },
                                 'oil_count': 3,
                                 'outgoing_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'oif_rpf': True,
                                         'oil_flags': 'm6rib',
                                         'oil_uptime': '00:04:03'
                                         }
                                    },
                                 'uptime': '00:04:03'
                                 }
                            }
                        },
                    'ff1e:3333:ffff::/128': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'mld '
                                        'pim6 '
                                        'ipv6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:03'
                                },
                            '2001::222:1:1:1234/128': 
                                {'flag': 'ipv6 '
                                        'm6rib '
                                        'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.10': 
                                        {'rpf_nbr': '2001::222:1:1:1234'
                                        }
                                    },
                                'oil_count': 3,
                                'uptime': '00:04:03'
                            },
                            '2001::222:1:2:1234/128': 
                                {'flag': 'ipv6 '
                                         'm6rib '
                                         'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'rpf_nbr': '2001::222:1:2:1234'
                                        }
                                    },
                                'oil_count': 2,
                                'outgoing_interface_list': 
                                    {'Ethernet1/33.11': 
                                        {'oif_rpf': True,
                                         'oil_flags': 'm6rib',
                                         'oil_uptime': '00:04:03'
                                         }
                                    },
                                'uptime': '00:04:03'
                            },
                            '2001::222:2:3:1234/128': 
                                {'flag': 'ipv6 '
                                        'm6rib '
                                        'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:01'
                                },
                            '2001::222:2:44:1234/128': 
                                {'flag': 'ipv6 '
                                         'm6rib '
                                         'pim6',
                                'incoming_interface_list': 
                                    {'Ethernet1/26': 
                                        {'rpf_nbr': 'fe80::10'
                                        }
                                    },
                                'oil_count': 1,
                                'uptime': '00:04:00'
                                }
                            }
                        },
                     'ff30::/12': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'pim6 '
                                          'ipv6',
                                'incoming_interface_list': 
                                    {'Null': 
                                        {'rpf_nbr': '0::'
                                        }
                                    },
                                'oil_count': 0,
                                'uptime': '19:55:47'
                                }
                            }
                        }
                    }
                },
            'default': 
                {'multicast_group': 
                    {'ff30::/12': 
                        {'source_address': 
                            {'*': 
                                {'flag': 'pim6 '
                                         'ipv6',
                                 'incoming_interface_list': 
                                    {'Null': 
                                        {'rpf_nbr': '0::'
                                        }
                                    },
                                'oil_count': 0,
                                'uptime': '3d11h'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
 

    
    golden_output = {'execute.return_value': '''
     IPv6 Multicast Routing Table for VRF "default"

(*, ff30::/12), uptime: 3d11h, pim6 ipv6 
  Incoming interface: Null, RPF nbr: 0::
  Outgoing interface list: (count: 0)


IPv6 Multicast Routing Table for VRF "VRF1"

(*, ff30::/12), uptime: 3d11h, pim6 ipv6 
  Incoming interface: Null, RPF nbr: 0::
  Outgoing interface list: (count: 0)
  
(*, ff1e:1111::1:0/128), uptime: 00:04:03, mld pim6 ipv6 
  Incoming interface: loopback10, RPF nbr: 2001:9999::1
  Outgoing interface list: (count: 3)
    Ethernet1/26, uptime: 00:02:58, pim6
    port-channel1001, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, mld

(2001::222:1:1:1234/128, ff1e:1111::1:0/128), uptime: 00:04:03, ipv6 pim6 m6rib 
  Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234, internal
  Outgoing interface list: (count: 3)
    Ethernet1/26, uptime: 00:02:58, pim6
    port-channel1001, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib

(2001::222:1:2:1234/128, ff1e:1111::1:0/128), uptime: 00:04:03, ipv6 pim6 m6rib 
  Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234, internal
  Outgoing interface list: (count: 3)
    Ethernet1/26, uptime: 00:02:58, pim6
    port-channel1001, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

(2001::222:2:3:1234/128, ff1e:1111::1:0/128), uptime: 00:04:03, pim6 m6rib ipv6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10, internal
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:03, m6rib

(2001::222:2:44:1234/128, ff1e:1111::1:0/128), uptime: 00:04:03, pim6 m6rib ipv6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10, internal
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:03, m6rib

(*, ff1e:1111:ffff::/128), uptime: 00:04:03, mld pim6 ipv6 
  Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1
  Outgoing interface list: (count: 2)
    Ethernet1/26, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, mld

(2001::222:1:1:1234/128, ff1e:1111:ffff::/128), uptime: 00:04:03, ipv6 pim6 m6rib 
  Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234, internal
  Outgoing interface list: (count: 3)
    Ethernet1/26, uptime: 00:02:58, pim6
    port-channel1001, uptime: 00:04:00, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib

(2001::222:1:2:1234/128, ff1e:1111:ffff::/128), uptime: 00:04:03, ipv6 pim6 m6rib 
  Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234, internal
  Outgoing interface list: (count: 2)
    Ethernet1/26, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

(2001::222:2:3:1234/128, ff1e:1111:ffff::/128), uptime: 00:04:03, pim6 m6rib ipv6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10, internal
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:03, m6rib

(2001::222:2:44:1234/128, ff1e:1111:ffff::/128), uptime: 00:04:03, pim6 m6rib ipv6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10, internal
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:03, m6rib

(*, ff1e:2222:ffff::/128), uptime: 00:04:03, mld pim6 ipv6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:03, mld

(2001::222:1:1:1234/128, ff1e:2222:ffff::/128), uptime: 00:04:03, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234
  Outgoing interface list: (count: 2)
    Ethernet1/26, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib

(2001::222:1:2:1234/128, ff1e:2222:ffff::/128), uptime: 00:04:03, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234
  Outgoing interface list: (count: 2)
    Ethernet1/26, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

(2001::222:2:3:1234/128, ff1e:2222:ffff::/128), uptime: 00:04:02, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:02, m6rib

(2001::222:2:44:1234/128, ff1e:2222:ffff::/128), uptime: 00:04:02, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:02, m6rib

(*, ff1e:2222:ffff::1:0/128), uptime: 00:04:03, mld pim6 ipv6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:03, mld

(2001::222:1:1:1234/128, ff1e:2222:ffff::1:0/128), uptime: 00:04:03, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234
  Outgoing interface list: (count: 3)
    Ethernet1/26, uptime: 00:02:58, pim6
    port-channel1001, uptime: 00:04:02, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib

(2001::222:1:2:1234/128, ff1e:2222:ffff::1:0/128), uptime: 00:04:03, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234
  Outgoing interface list: (count: 2)
    Ethernet1/26, uptime: 00:04:02, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

(*, ff1e:3333::1:0/128), uptime: 00:04:03, mld pim6 ipv6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:03, mld

(2001::222:1:1:1234/128, ff1e:3333::1:0/128), uptime: 00:04:03, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234
  Outgoing interface list: (count: 2)
    Ethernet1/26, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib

(2001::222:1:2:1234/128, ff1e:3333::1:0/128), uptime: 00:04:03, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234
  Outgoing interface list: (count: 3)
    Ethernet1/26, uptime: 00:02:58, pim6
    port-channel1001, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

(*, ff1e:3333:ffff::/128), uptime: 00:04:03, mld pim6 ipv6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:03, mld

(2001::222:1:1:1234/128, ff1e:3333:ffff::/128), uptime: 00:04:03, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/33.10, RPF nbr: 2001::222:1:1:1234
  Outgoing interface list: (count: 3)
    Ethernet1/26, uptime: 00:02:58, pim6
    port-channel1001, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib

(2001::222:1:2:1234/128, ff1e:3333:ffff::/128), uptime: 00:04:03, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/33.11, RPF nbr: 2001::222:1:2:1234
  Outgoing interface list: (count: 2)
    Ethernet1/26, uptime: 00:04:01, pim6
    Ethernet1/33.11, uptime: 00:04:03, m6rib, (RPF)

(2001::222:2:3:1234/128, ff1e:3333:ffff::/128), uptime: 00:04:01, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:01, m6rib

(2001::222:2:44:1234/128, ff1e:3333:ffff::/128), uptime: 00:04:00, ipv6 m6rib pim6 
  Incoming interface: Ethernet1/26, RPF nbr: fe80::10
  Outgoing interface list: (count: 1)
    Ethernet1/33.11, uptime: 00:04:00, m6rib

(*, ff30::/12), uptime: 19:55:47, pim6 ipv6 
  Incoming interface: Null, RPF nbr: 0::
  Outgoing interface list: (count: 0)
      
      '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ipv6_mroute_vrf_all_obj = ShowIpv6MrouteVrfAll(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ipv6_mroute_vrf_all_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ipv6_mroute_vrf_all_obj = ShowIpv6MrouteVrfAll(device=self.device)
        parsed_output = ipv6_mroute_vrf_all_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


##############################################################################
#                Unitest for Show ip static route multicast
##############################################################################


class test_show_ip_static_route_multicast(unittest.TestCase):
    
    device = Device(name='aDevice')
    device0 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'static_routemulticast': 
        {'vrf': 
            {'VRF1_2': 
                {'af_name': 
                    {'IPv4': 
                        {'mroute': 
                            {'10.2.2.2/32': 
                                {'path': 
                                    {'0.0.0.0/32%sanity1 Vlan2': 
                                        {'mroute_neighbor_address': '0.0.0.0/32%sanity1 '
                                                                    'Vlan2',
                                         'urib': True}}},
                            '10.2.2.3/32': 
                                {'path': 
                                    {'0.0.0.0/32%sanity1 Vlan2': 
                                        {'mroute_neighbor_address': '0.0.0.0/32%sanity1 '
                                                                    'Vlan2',
                                         'urib': True}}}}}}},
             'default_1': 
                {'af_name': 
                    {'IPv4': 
                        {'mroute': 
                            {'112.0.0.0/8': 
                                {'path': 
                                    {'0.0.0.0/32 Null0': 
                                        {'mroute_interface_name': 'Null0',
                                         'mroute_neighbor_address': '0.0.0.0/32',
                                         'urib': True}}},
                             '212.0.0.0/8': 
                                {'path': 
                                    {'0.0.0.0/32 Null0': 
                                        {'mroute_interface_name': 'Null0',
                                         'mroute_neighbor_address': '0.0.0.0/32',
                                         'urib': True}}}}}}},
             'management_3': 
                {'af_name': 
                    {'IPv4': 
                        {'mroute': 
                            {'0.0.0.0/0': 
                                {'path': 
                                    {'172.31.200.1/32': 
                                        {'mroute_neighbor_address': '172.31.200.1/32',
                                         'urib': True}}}}}}},
             'sanity1_4': 
                {'af_name': 
                    {'IPv4': 
                        {'mroute': 
                            {'10.2.2.2/32': 
                                {'path': 
                                    {'0.0.0.0/32 Vlan2': 
                                        {'mroute_interface_name': 'Vlan2',
                                         'mroute_neighbor_address': '0.0.0.0/32',
                                         'urib': True}}},
                             '10.2.2.3/32': 
                                {'path': 
                                    {'0.0.0.0/32 Vlan2': 
                                        {'mroute_interface_name': 'Vlan2',
                                         'mroute_neighbor_address': '0.0.0.0/32',
                                         'urib': True}}}}}}}}}}

    
    golden_output = {'execute.return_value': '''
      Mstatic-route for VRF "default"(1)
IPv4 MStatic Routes:
  112.0.0.0/8, configured nh: 0.0.0.0/32 Null0
    (installed in urib)
  212.0.0.0/8, configured nh: 0.0.0.0/32 Null0
    (installed in urib)

    Static-route for VRF "VRF1"(2)
IPv4 Unicast Static Routes:
  10.2.2.2/32, configured nh: 0.0.0.0/32%sanity1 Vlan2
    (installed in urib)
  10.2.2.3/32, configured nh: 0.0.0.0/32%sanity1 Vlan2
    (installed in urib)

Static-route for VRF "management"(3)
IPv4 Unicast Static Routes:
  0.0.0.0/0, configured nh: 172.31.200.1/32
    (installed in urib)
    rnh(installed in urib)

Static-route for VRF "sanity1"(4)
IPv4 Unicast Static Routes:
  10.2.2.2/32, configured nh: 0.0.0.0/32 Vlan2
    (installed in urib)
  10.2.2.3/32, configured nh: 0.0.0.0/32 Vlan2
    (installed in urib)
       
      '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        ip_static_route_multicast_obj = ShowIpStaticRouteMulticast(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = ip_static_route_multicast_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        ip_static_route_multicast_obj = ShowIpStaticRouteMulticast(device=self.device)
        parsed_output = ip_static_route_multicast_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


###############################################################################
#                      Unitest for Show ipv6 static route multicast
###############################################################################


class test_show_ipv6_static_route_multicast(unittest.TestCase):
    
  device = Device(name='aDevice')
  device0 = Device(name='bDevice')
  empty_output = {'execute.return_value': ''}
    
  golden_parsed_output = {'ipv6_static_routemulticast': 
    {'vrf': 
        {'default_1': 
            {'mroute': 
                {'126::/16': 
                    {'path': 
                        {'0:: Null0': 
                            {'bfd_enable': False,
                             'mroute_interface_name': 'Null0',
                             'mroute_neighbor_address': '0::',
                             'nh_vrf': 'default',
                             'preference': '1',
                             'reslv_tid': '80000001',
                             'rnh_status': 'not '
                                           'installed '
                                           'in '
                                           'u6rib'}}},
                 '226::/16': 
                    {'path': 
                        {'0:: Null0': 
                            {'bfd_enable': False,
                             'mroute_interface_name': 'Null0',
                             'mroute_neighbor_address': '0::',
                             'nh_vrf': 'default',
                             'preference': '1',
                             'reslv_tid': '80000001',
                             'rnh_status': 'not '
                                           'installed '
                                           'in '
                                           'u6rib'}}}}}}}}



   
  golden_output = {'execute.return_value': '''
      IPv6 Configured Static Routes for VRF "default"(1)

  126::/16 -> Null0, preference: 1
    nh_vrf(default) reslv_tid 80000001
    real-next-hop: 0::, interface: Null0
      rnh(not installed in u6rib)
      bfd_enabled no
  226::/16 -> Null0, preference: 1
    nh_vrf(default) reslv_tid 80000001
    real-next-hop: 0::, interface: Null0
      rnh(not installed in u6rib)
      bfd_enabled no
 127::/16 -> port-channel8, preference: 2
    nh_vrf(default) reslv_tid 80000001
    real-next-hop: 0::, interface: port-channel8
      rnh(not installed in u6rib)
      bfd_enabled no
 227::/16 -> Ethernet1/2.10, preference: 3
    nh_vrf(default) reslv_tid 80000001
    real-next-hop: 0::, interface: Ethernet1/2.10
      rnh(not installed in u6rib)
      bfd_enabled no       
      '''}

  def test_empty(self):
      self.device1 = Mock(**self.empty_output)
      ipv6_static_route_multicast_obj = ShowIpv6StaticRouteMulticast(device=self.device1)
      with self.assertRaises(SchemaEmptyParserError):
          parsed_output = ipv6_static_route_multicast_obj.parse()

  def test_golden(self):
      self.device = Mock(**self.golden_output)
      ipv6_static_route_multicast_obj = ShowIpv6StaticRouteMulticast(device=self.device)
      parsed_output = ipv6_static_route_multicast_obj.parse()
      self.maxDiff = None
      self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()