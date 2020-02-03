
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.nxos.show_ospf import ShowIpOspf,\
                                  ShowIpOspfMplsLdpInterface,\
                                  ShowIpOspfVirtualLinks,\
                                  ShowIpOspfShamLinks,\
                                  ShowIpOspfInterface,\
                                  ShowIpOspfNeighborDetail,\
                                  ShowIpOspfDatabaseExternalDetail,\
                                  ShowIpOspfDatabaseNetworkDetail,\
                                  ShowIpOspfDatabaseSummaryDetail,\
                                  ShowIpOspfDatabaseRouterDetail,\
                                  ShowIpOspfDatabaseOpaqueAreaDetail


# =====================================
#  Unit test for 'show ip ospf'
#  Unit test for 'show ip ospf vrf all'
# =====================================
class TestShowIpOspf(unittest.TestCase):

    '''Unit test for 'show ip ospf'
       Unit test for 'show ip ospf vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '1': {
                                'areas': {
                                    '0.0.0.1': {
                                        'area_id': '0.0.0.1',
                                        'area_type': 'stub',
                                        'authentication': 'none',
                                        'default_cost': 1,
                                        'existed': '08:30:42',
                                        'numbers': {
                                            'active_interfaces': 3,
                                            'interfaces': 3,
                                            'loopback_interfaces': 0,
                                            'passive_interfaces': 0
                                        },
                                        'ranges': {
                                            '10.4.0.0/16': {
                                                'advertise': False,
                                                'cost': 31,
                                                'net': 1,
                                                'prefix': '10.4.0.0/16'
                                            }
                                        },
                                        'statistics': {
                                            'area_scope_lsa_cksum_sum': '11',
                                            'area_scope_lsa_count': 11,
                                            'spf_last_run_time': 0.000464,
                                            'spf_runs_count': 33
                                        }
                                    }
                                },
                                'auto_cost': {
                                    'bandwidth_unit': 'mbps',
                                    'enable': False,
                                    'reference_bandwidth': 40000
                                },
                                'enable': True,
                                'discard_route_external': True,
                                'discard_route_internal': True,
                                'graceful_restart': {
                                    'ietf': {
                                        'enable': True,
                                        'exist_status': 'none',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'
                                    }
                                },
                                'instance': 1,
                                'nsr': {
                                    'enable': True
                                },
                                'numbers': {
                                    'active_areas': {
                                        'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1
                                    },
                                    'areas': {
                                        'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1
                                    }
                                },
                                'opaque_lsa_enable': True,
                                'this_router_is': 'an area border and '
                                'autonomous system boundary',
                                'preference': {
                                    'single_value': {
                                        'all': 110
                                    }
                                },
                                'router_id': '10.151.22.22',
                                'single_tos_routes_enable': True,
                                'redistribution': {
                                    'bgp': {
                                        'bgp_id': 100
                                    }
                                },
                                'spf_control': {
                                    'paths': 8,
                                    'throttle': {
                                        'lsa': {
                                            'group_pacing': 10,
                                            'hold': 5000,
                                            'maximum': 5000,
                                            'minimum': 1000,
                                            'numbers': {
                                                'external_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                },
                                                'opaque_as_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                }
                                            },
                                            'start': 0
                                        },
                                        'spf': {
                                            'hold': 1000,
                                            'maximum': 5000,
                                            'start': 200
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '1': {
                                'areas': {
                                    '0.0.0.0': {
                                        'area_id': '0.0.0.0',
                                        'area_type': 'normal',
                                        'authentication': 'none',
                                        'existed': '08:30:42',
                                        'numbers': {
                                            'active_interfaces': 4,
                                            'interfaces': 4,
                                            'loopback_interfaces': 1,
                                            'passive_interfaces': 0
                                        },
                                        'ranges': {
                                            '10.4.1.0/24': {
                                                'advertise': True,
                                                'cost': 33,
                                                'net': 0,
                                                'prefix': '10.4.1.0/24'
                                            }
                                        },
                                        'statistics': {
                                            'area_scope_lsa_cksum_sum': '19',
                                            'area_scope_lsa_count': 19,
                                            'spf_last_run_time': 0.001386,
                                            'spf_runs_count': 8
                                        }
                                    }
                                },
                                'auto_cost': {
                                    'bandwidth_unit': 'mbps',
                                    'enable': False,
                                    'reference_bandwidth': 40000
                                },
                                'bfd': {
                                    'enable': True
                                },
                                'database_control': {
                                    'max_lsa': 123
                                },
                                'enable': True,
                                'discard_route_external': True,
                                'discard_route_internal': True,
                                'graceful_restart': {
                                    'ietf': {
                                        'enable': True,
                                        'exist_status': 'none',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'
                                    }
                                },
                                'instance': 1,
                                'nsr': {
                                    'enable': True
                                },
                                'numbers': {
                                    'active_areas': {
                                        'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1
                                    },
                                    'areas': {
                                        'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1
                                    }
                                },
                                'opaque_lsa_enable': True,
                                'preference': {
                                    'single_value': {
                                        'all': 110
                                    }
                                },
                                'router_id': '10.100.2.2',
                                'single_tos_routes_enable': True,
                                'spf_control': {
                                    'paths': 8,
                                    'throttle': {
                                        'lsa': {
                                            'group_pacing': 10,
                                            'hold': 5000,
                                            'maximum': 5000,
                                            'minimum': 1000,
                                            'numbers': {
                                                'external_lsas': {
                                                    'checksum': '0x7d61',
                                                    'total': 1
                                                },
                                                'opaque_as_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                }
                                            },
                                            'start': 0
                                        },
                                        'spf': {
                                            'hold': 1000,
                                            'maximum': 5000,
                                            'start': 200
                                        }
                                    }
                                },
                                'stub_router': {
                                    'always': {
                                        'always': True
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        Routing Process 1 with ID 10.100.2.2 VRF default
        Routing Process Instance Number 1
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive
        BFD is enabled
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        Administrative distance 110
        Originating router LSA with maximum metric
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs,
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs,
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum number of non self-generated LSA allowed 123
        Maximum paths to destination 8
        Number of external LSAs 1, checksum sum 0x7d61
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area BACKBONE(0.0.0.0)
            Area has existed for 08:30:42
            Interfaces in this area: 4 Active interfaces: 4
            Passive interfaces: 0  Loopback interfaces: 1
            No authentication available
            SPF calculation has run 8 times
             Last SPF ran for 0.001386s
            Area ranges are
            10.4.1.0/24 Passive (Num nets: 0) Advertise Cost configured 33
            Number of LSAs: 19, checksum sum 0x7a137

        Routing Process 1 with ID 10.151.22.22 VRF VRF1
        Routing Process Instance Number 1
        Domain ID type 0x0005, Value 0.0.0.0
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        This router is an area border and autonomous system boundary.
        Redistributing External Routes from
        bgp-100
        Administrative distance 110
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs,
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs,
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 0, checksum sum 0
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area (0.0.0.1)
            This area is a STUB area
            Generates stub default route with cost 1
            Area has existed for 08:30:42
            Interfaces in this area: 3 Active interfaces: 3
            Passive interfaces: 0  Loopback interfaces: 0
            No authentication available
            SPF calculation has run 33 times
             Last SPF ran for 0.000464s
            Area ranges are
            10.4.0.0/16 Active (Num nets: 1) DoNotAdvertise Cost configured 31
            Number of LSAs: 11, checksum sum 0x527f9
        '''}

    golden_parsed_output_1 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.0':
                                        {'area_id': '0.0.0.0',
                                        'area_type': 'normal',
                                        'authentication': 'none',
                                        'existed': '1w5d',
                                        'numbers':
                                            {'active_interfaces': 4,
                                            'interfaces': 6,
                                            'loopback_interfaces': 4,
                                            'passive_interfaces': 0},
                                        'statistics':
                                            {'area_scope_lsa_cksum_sum': '1',
                                            'area_scope_lsa_count': 1,
                                            'spf_last_run_time': 0.000447,
                                            'spf_runs_count': 2}}},
                                'auto_cost':
                                    {'bandwidth_unit': 'mbps',
                                    'enable': False,
                                    'reference_bandwidth': 40000},
                                'enable': False,
                                'discard_route_external': True,
                                'discard_route_internal': True,
                                'graceful_restart':
                                    {'ietf':
                                        {'enable': True,
                                        'exist_status': 'none',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'}},
                                'instance': 1,
                                'nsr':
                                    {'enable': True},
                                'numbers':
                                    {'active_areas':
                                        {'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1},
                                    'areas':
                                        {'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1}},
                                'opaque_lsa_enable': True,
                                'preference':
                                    {'single_value':
                                        {'all': 110}},
                                'router_id': '10.100.2.2',
                                'single_tos_routes_enable': True,
                                'spf_control':
                                    {'paths': 8,
                                    'throttle':
                                        {'lsa':
                                            {'group_pacing': 10,
                                            'hold': 5000,
                                            'maximum': 5000,
                                            'minimum': 1000,
                                            'numbers':
                                                {'external_lsas':
                                                    {'checksum': '0',
                                                    'total': 0},
                                                'opaque_as_lsas':
                                                    {'checksum': '0',
                                                 'total': 0}},
                                            'start': 0.0},
                                            'spf':
                                                {'hold': 1000,
                                            'maximum': 5000,
                                            'start': 200}}}}}}}}}}

    golden_output_1 = {'execute.return_value': '''
        Routing Process 1 with ID 10.100.2.2 VRF default
        Routing Process Instance Number 1
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        Administrative distance 110
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs,
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs,
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 0, checksum sum 0
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area BACKBONE(0.0.0.0) (Inactive)
            Area has existed for 1w5d
            Interfaces in this area: 6 Active interfaces: 4
            Passive interfaces: 0  Loopback interfaces: 4
            No authentication available
            SPF calculation has run 2 times
             Last SPF ran for 0.000447s
            Area ranges are
            Number of LSAs: 1, checksum sum 0x9ccb
        '''}

    golden_parsed_output_2 = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '1': {
                                'areas': {
                                    '0.0.0.0': {
                                        'area_id': '0.0.0.0',
                                        'area_type': 'normal',
                                        'existed': '2d05h',
                                        'authentication': 'Message-digest',
                                        'numbers': {
                                            'active_interfaces': 3,
                                            'interfaces': 4,
                                            'loopback_interfaces': 1,
                                            'passive_interfaces': 0
                                        },
                                        'statistics': {
                                            'area_scope_lsa_cksum_sum': '35',
                                            'area_scope_lsa_count': 35,
                                            'spf_last_run_time': 0.002091,
                                            'spf_runs_count': 64
                                        }
                                    }
                                },
                                'auto_cost': {
                                    'bandwidth_unit': 'mbps',
                                    'enable': False,
                                    'reference_bandwidth': 40000
                                },
                                'discard_route_external': True,
                                'discard_route_internal': True,
                                'enable': True,
                                'graceful_restart': {
                                    'ietf': {
                                        'enable': True,
                                        'exist_status': 'none',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'
                                    }
                                },
                                'instance': 1,
                                'nsr': {
                                    'enable': True
                                },
                                'numbers': {
                                    'active_areas': {
                                        'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1
                                    },
                                    'areas': {
                                        'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1
                                    }
                                },
                                'opaque_lsa_enable': True,
                                'preference': {
                                    'single_value': {
                                        'all': 110
                                    }
                                },
                                'router_id': '10.1.0.105',
                                'single_tos_routes_enable': True,
                                'spf_control': {
                                    'paths': 8,
                                    'throttle': {
                                        'lsa': {
                                            'group_pacing': 10,
                                            'hold': 50,
                                            'maximum': 500,
                                            'minimum': 50,
                                            'numbers': {
                                                'external_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                },
                                                'opaque_as_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                }
                                            },
                                            'start': 20
                                        },
                                        'spf': {
                                            'hold': 50,
                                            'maximum': 500,
                                            'start': 20
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

    golden_output_2 = {'execute.return_value': '''
        show ip ospf vrf all
        Routing Process 1 with ID 10.1.0.105 VRF default
        Routing Process Instance Number 1
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        Administrative distance 110
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 20.000 msecs,
        SPF throttling hold time of 50.000 msecs,
        SPF throttling maximum wait time of 500.000 msecs
        LSA throttling start time of 20.000 msecs,
        LSA throttling hold interval of 50.000 msecs,
        LSA throttling maximum wait time of 500.000 msecs
        Minimum LSA arrival 50.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 0, checksum sum 0
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area BACKBONE(0.0.0.0)
            Area has existed for 2d05h
            Interfaces in this area: 4 Active interfaces: 3
            Passive interfaces: 0  Loopback interfaces: 1
            Message-digest authentication
            SPF calculation has run 64 times
             Last SPF ran for 0.002091s
            Area ranges are
            Number of LSAs: 35, checksum sum 0x13a425
        '''}

    golden_parsed_output_3 = {
        'vrf':{
            'default':{
                'address_family': {
                    'ipv4':{
                        'instance': {
                            '10': {
                                'areas': {
                                    '10.4.2.255': {
                                        'generate_nssa_default_route': True,
                                        'area_id': '10.4.2.255',
                                        'area_type': 'nssa',
                                        'authentication': 'none',
                                        'existed': '1y16w',
                                        'summary': False,
                                        'perform_translation': 'type-7/type-5',
                                        'numbers': {
                                            'active_interfaces': 16,
                                            'interfaces': 20,
                                            'loopback_interfaces': 1,
                                            'passive_interfaces': 17
                                        },
                                        'statistics': {
                                            'area_scope_lsa_cksum_sum': '85',
                                            'area_scope_lsa_count': 85,
                                            'spf_last_run_time': 0.004560,
                                            'spf_runs_count': 123
                                        }
                                    }
                                },
                                'auto_cost': {
                                    'bandwidth_unit': 'mbps',
                                    'enable': True,
                                    'reference_bandwidth': 100000
                                },
                                'redistribution': {
                                    'static': {
                                        'enabled': True
                                    }
                                },
                                'enable': True,
                                'graceful_restart': {
                                    'ietf': {
                                        'enable': True,
                                        'exist_status': 'none',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'
                                    }
                                },
                                'instance': 10,
                                'nsr': {
                                    'enable': True
                                },
                                'numbers': {
                                    'active_areas': {
                                        'normal': 0,
                                        'nssa': 1,
                                        'stub': 0,
                                        'total': 1
                                    },
                                    'areas': {
                                        'normal': 0,
                                        'nssa': 1,
                                        'stub': 0,
                                        'total': 1
                                    }
                                },
                                'opaque_lsa_enable': True,
                                'this_router_is': 'an autonomous system boundary',
                                'preference': {
                                    'single_value': {
                                        'all': 110
                                    }
                                },
                                'router_id': '10.219.255.1',
                                'single_tos_routes_enable': True,
                                'spf_control': {
                                    'paths': 8,
                                    'throttle': {
                                        'lsa': {
                                            'group_pacing': 10,
                                            'hold': 5000,
                                            'maximum': 5000,
                                            'minimum': 1000,
                                            'numbers': {
                                                'external_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                },
                                                'opaque_as_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                }
                                            },
                                            'start': 0
                                        },
                                        'spf': {
                                            'hold': 1000,
                                            'maximum': 5000,
                                            'start': 200
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

    golden_output_3 = {'execute.return_value': '''
        Routing Process 10 with ID 10.219.255.1 VRF default
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive
        Last graceful restart exit status: None
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        This router is an autonomous system boundary
        Redistributing External Routes from
        static
        Administrative distance 110
        Reference Bandwidth is 100000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs,
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs,
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 0, checksum sum 0
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 0 normal, 0 stub, 1 nssa
        Number of active areas is 1, 0 normal, 0 stub, 1 nssa
       Area (10.4.2.255)
            Area has existed for 1y16w
            Interfaces in this area: 20 Active interfaces: 16
            Passive interfaces: 17  Loopback interfaces: 1
            This area is a NSSA area
            Perform type-7/type-5 LSA translation
            Generates NSSA default route
            Summarization is disabled
            No authentication available
            SPF calculation has run 123 times
            Last SPF ran for 0.004560s
            Area ranges are
            Number of LSAs: 85, checksum sum 0x2a0ebf
        '''}

    golden_output_customer = {'execute.return_value': '''
        show ip ospf vrf all


        Routing Process 2000 with ID 10.100.0.11 VRF default
        Routing Process Instance Number 2
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive 
        Last graceful restart exit status: Failed (grace period timeout)
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        This router is an autonomous system boundary
        Redistributing External Routes from
        static
        Administrative distance 110
        Reference Bandwidth is 1000000 Mbps
        SPF throttling delay time of 1.000 msecs,
        SPF throttling hold time of 50.000 msecs, 
        SPF throttling maximum wait time of 50.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs, 
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 10.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 1473, checksum sum 0x2e1b151
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Name Lookup is enabled
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area (0.0.0.1) 
                Area has existed for 5w2d
                Interfaces in this area: 153 Active interfaces: 152
                Passive interfaces: 147  Loopback interfaces: 1
                No authentication available
                SPF calculation has run 6 times
                Last SPF ran for 0.004728s
                Area ranges are
                Number of LSAs: 2702, checksum sum 0x54707bc

        Routing Process 1000 with ID 10.100.0.13 VRF default
        Routing Process Instance Number 1
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive 
        Last graceful restart exit status: Successful
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        This router is an area border
        Administrative distance 110
        Reference Bandwidth is 40000 Mbps
        SPF throttling delay time of 200.000 msecs,
        SPF throttling hold time of 1000.000 msecs, 
        SPF throttling maximum wait time of 5000.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs, 
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 1000.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 0, checksum sum 0
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 0, 0 normal, 0 stub, 0 nssa
        Number of active areas is 0, 0 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.

        Routing Process 1000 with ID 10.100.0.13 VRF LAN-GENIE
        Routing Process Instance Number 1
        Stateful High Availability enabled
        Graceful-restart is configured
        Grace period: 60 state: Inactive 
        Last graceful restart exit status: Successful
        Supports only single TOS(TOS0) routes
        Supports opaque LSA
        Administrative distance 110
        Reference Bandwidth is 1000000 Mbps
        SPF throttling delay time of 1.000 msecs,
        SPF throttling hold time of 50.000 msecs, 
        SPF throttling maximum wait time of 50.000 msecs
        LSA throttling start time of 0.000 msecs,
        LSA throttling hold interval of 5000.000 msecs, 
        LSA throttling maximum wait time of 5000.000 msecs
        Minimum LSA arrival 10.000 msec
        LSA group pacing timer 10 secs
        Maximum paths to destination 8
        Number of external LSAs 1243, checksum sum 0x268032f
        Number of opaque AS LSAs 0, checksum sum 0
        Number of areas is 1, 1 normal, 0 stub, 0 nssa
        Number of active areas is 1, 1 normal, 0 stub, 0 nssa
        Install discard route for summarized external routes.
        Install discard route for summarized internal routes.
        Area (0.0.0.1) 
                Area has existed for 5w2d
                Interfaces in this area: 5 Active interfaces: 5
                Passive interfaces: 0  Loopback interfaces: 1
                No authentication available
                SPF calculation has run 11 times
                Last SPF ran for 0.004147s
                Area ranges are
                Number of LSAs: 2661, checksum sum 0x5317cd7 
    '''
    }

    golden_parsed_output_customer = {
        'vrf': {
            'LAN-GENIE': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '1000': {
                                'areas': {
                                    '0.0.0.1': {
                                        'area_id': '0.0.0.1',
                                        'area_type': 'normal',
                                        'authentication': 'none',
                                        'existed': '5w2d',
                                        'numbers': {
                                            'active_interfaces': 5,
                                            'interfaces': 5,
                                            'loopback_interfaces': 1,
                                            'passive_interfaces': 0
                                        },
                                        'statistics': {
                                            'area_scope_lsa_cksum_sum': '2661',
                                            'area_scope_lsa_count': 2661,
                                            'spf_last_run_time': 0.004147,
                                            'spf_runs_count': 11
                                        }
                                    }
                                },
                                'auto_cost': {
                                    'bandwidth_unit': 'mbps',
                                    'enable': True,
                                    'reference_bandwidth': 1000000
                                },
                                'discard_route_external': True,
                                'discard_route_internal': True,
                                'enable': True,
                                'graceful_restart': {
                                    'ietf': {
                                        'enable': True,
                                        'exist_status': 'successful',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'
                                    }
                                },
                                'instance': 1,
                                'nsr': {
                                    'enable': True
                                },
                                'numbers': {
                                    'active_areas': {
                                        'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1
                                    },
                                    'areas': {
                                        'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1
                                    }
                                },
                                'opaque_lsa_enable': True,
                                'preference': {
                                    'single_value': {
                                        'all': 110
                                    }
                                },
                                'router_id': '10.100.0.13',
                                'single_tos_routes_enable': True,
                                'spf_control': {
                                    'paths': 8,
                                    'throttle': {
                                        'lsa': {
                                            'group_pacing': 10,
                                            'hold': 5000,
                                            'maximum': 5000,
                                            'minimum': 10,
                                            'numbers': {
                                                'external_lsas': {
                                                    'checksum': '0x268032f',
                                                    'total': 1243
                                                },
                                                'opaque_as_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                }
                                            },
                                            'start': 0
                                        },
                                        'spf': {
                                            'hold': 50,
                                            'maximum': 50,
                                            'start': 1
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '1000': {
                                'auto_cost': {
                                    'bandwidth_unit': 'mbps',
                                    'enable': False,
                                    'reference_bandwidth': 40000
                                },
                                'discard_route_external': True,
                                'discard_route_internal': True,
                                'graceful_restart': {
                                    'ietf': {
                                        'enable': True,
                                        'exist_status': 'successful',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'
                                    }
                                },
                                'instance': 1,
                                'nsr': {
                                    'enable': True
                                },
                                'numbers': {
                                    'active_areas': {
                                        'normal': 0,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 0
                                    },
                                    'areas': {
                                        'normal': 0,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 0
                                    }
                                },
                                'opaque_lsa_enable': True,
                                'this_router_is': 'an area border',
                                'preference': {
                                    'single_value': {
                                        'all': 110
                                    }
                                },
                                'router_id': '10.100.0.13',
                                'single_tos_routes_enable': True,
                                'spf_control': {
                                    'paths': 8,
                                    'throttle': {
                                        'lsa': {
                                            'group_pacing': 10,
                                            'hold': 5000,
                                            'maximum': 5000,
                                            'minimum': 1000,
                                            'numbers': {
                                                'external_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                },
                                                'opaque_as_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                }
                                            },
                                            'start': 0
                                        },
                                        'spf': {
                                            'hold': 1000,
                                            'maximum': 5000,
                                            'start': 200
                                        }
                                    }
                                }
                            },
                            '2000': {
                                'areas': {
                                    '0.0.0.1': {
                                        'area_id': '0.0.0.1',
                                        'area_type': 'normal',
                                        'authentication': 'none',
                                        'existed': '5w2d',
                                        'numbers': {
                                            'active_interfaces': 152,
                                            'interfaces': 153,
                                            'loopback_interfaces': 1,
                                            'passive_interfaces': 147
                                        },
                                        'statistics': {
                                            'area_scope_lsa_cksum_sum': '2702',
                                            'area_scope_lsa_count': 2702,
                                            'spf_last_run_time': 0.004728,
                                            'spf_runs_count': 6
                                        }
                                    }
                                },
                                'auto_cost': {
                                    'bandwidth_unit': 'mbps',
                                    'enable': True,
                                    'reference_bandwidth': 1000000
                                },
                                'discard_route_external': True,
                                'discard_route_internal': True,
                                'enable': True,
                                'graceful_restart': {
                                    'ietf': {
                                        'enable': True,
                                        'exist_status': 'failed',
                                        'restart_interval': 60,
                                        'state': 'Inactive',
                                        'type': 'ietf'
                                    }
                                },
                                'instance': 2,
                                'name_lookup': True,
                                'nsr': {
                                    'enable': True
                                },
                                'numbers': {
                                    'active_areas': {
                                        'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1
                                    },
                                    'areas': {
                                        'normal': 1,
                                        'nssa': 0,
                                        'stub': 0,
                                        'total': 1
                                    }
                                },
                                'opaque_lsa_enable': True,
                                'this_router_is': 'an autonomous system boundary',
                                'preference': {
                                    'single_value': {
                                        'all': 110
                                    }
                                },
                                'redistribution': {
                                    'static': {
                                        'enabled': True
                                    }
                                },
                                'router_id': '10.100.0.11',
                                'single_tos_routes_enable': True,
                                'spf_control': {
                                    'paths': 8,
                                    'throttle': {
                                        'lsa': {
                                            'group_pacing': 10,
                                            'hold': 5000,
                                            'maximum': 5000,
                                            'minimum': 10,
                                            'numbers': {
                                                'external_lsas': {
                                                    'checksum': '0x2e1b151',
                                                    'total': 1473
                                                },
                                                'opaque_as_lsas': {
                                                    'checksum': '0',
                                                    'total': 0
                                                }
                                            },
                                            'start': 0
                                        },
                                        'spf': {
                                            'hold': 50,
                                            'maximum': 50,
                                            'start': 1
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

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_default_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_default_vrf2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_default_vrf3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)
    
    def test_vrf_all_customer(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_customer)
        obj = ShowIpOspf(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_customer)

# ========================================================
#  Unit test for 'show ip ospf mpls ldp interface'
#  Unit test for 'show ip ospf mpls ldp interface vrf all'
# ========================================================
class TestShowIpOspfMplsLdpInterface(unittest.TestCase):

    '''Unit test for 'show ip ospf mpls ldp interface'
       Unit test for 'show ip ospf mpls ldp interface vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output1 = {'execute.return_value': '''
        loopback0 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        Ethernet2/2 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        Ethernet2/3 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        Ethernet2/4 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        Ethernet2/1 - Process ID 1 VRF VRF1, area 0.0.0.1
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State BDR, Network type BROADCAST
        SL1-0.0.0.0-10.151.22.22-10.229.11.11 - Process ID 1 VRF VRF1, area 0.0.0.1
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State P2P, Network type P2P
        SL2-0.0.0.0-10.151.22.22-10.21.33.33 - Process ID 1 VRF VRF1, area 0.0.0.1
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State P2P, Network type P2P
        port-channel4001 - Process ID 1 VRF VRF2, area 0.0.1.1
            LDP Autoconfig is enabled
            LDP Sync not enabled, not required
            State P2P, Network type P2P
        port-channel4002 - Process ID 1 VRF VRF2, area 0.0.1.1
            LDP Autoconfig is enabled
            LDP Sync not enabled, not required
            State P2P, Network type P2P
        '''}

    golden_parsed_output1 = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.1':
                                        {'mpls':
                                            {'ldp':
                                                {'autoconfig': False,
                                                'autoconfig_area_id': '0.0.0.1',
                                                'igp_sync': False,
                                                'required': False}},
                                        'interfaces':
                                            {'Ethernet2/1':
                                                {'area': '0.0.0.1',
                                                'interface_type': 'broadcast',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.1',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'Ethernet2/1',
                                                'state': 'bdr'}},
                                        'sham_links':
                                            {'10.151.22.22 10.229.11.11':
                                                {'area': '0.0.0.1',
                                                'interface_type': 'point_to_point',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.1',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': '10.151.22.22 10.229.11.11',
                                                'state': 'point_to_point'},
                                            '10.151.22.22 10.21.33.33':
                                                {'area': '0.0.0.1',
                                                'interface_type': 'point_to_point',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.1',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': '10.151.22.22 '
                                                '10.21.33.33',
                                                'state': 'point_to_point'}}}}}}}}},
            'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.0':
                                        {'mpls':
                                            {'ldp':
                                                {'autoconfig': False,
                                                'autoconfig_area_id': '0.0.0.0',
                                                'igp_sync': False,
                                                'required': False}},
                                        'interfaces':
                                            {'Ethernet2/2':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'broadcast',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'Ethernet2/2',
                                                'state': 'bdr'},
                                            'Ethernet2/3':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'broadcast',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'Ethernet2/3',
                                                'state': 'bdr'},
                                            'Ethernet2/4':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'broadcast',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'Ethernet2/4',
                                                'state': 'bdr'},
                                            'loopback0':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'loopback0',
                                                'state': 'loopback'}}}}}}}}},
             'VRF2':
                 {'address_family':
                      {'ipv4':
                           {'instance':
                                {'1':
                                     {'areas':
                                          {'0.0.1.1':
                                               {'mpls':
                                                    {'ldp':
                                                         {'autoconfig': True,
                                                          'autoconfig_area_id': '0.0.1.1',
                                                          'igp_sync': False,
                                                          'required': False}},
                                               'interfaces':
                                                    {'port-channel4001':
                                                         {'area': '0.0.1.1',
                                                          'interface_type': 'point_to_point',
                                                          'mpls':
                                                              {'ldp':
                                                                   {'autoconfig': True,
                                                                    'autoconfig_area_id': '0.0.1.1',
                                                                    'igp_sync': False,
                                                                    'required': False}},
                                                          'name': 'port-channel4001',
                                                          'state': 'point_to_point'},
                                                    'port-channel4002':
                                                         {'area': '0.0.1.1',
                                                          'interface_type': 'point_to_point',
                                                          'mpls':
                                                              {'ldp':
                                                                   {'autoconfig': True,
                                                                    'autoconfig_area_id': '0.0.1.1',
                                                                    'igp_sync': False,
                                                                    'required': False}},
                                                          'name': 'port-channel4002',
                                                          'state': 'point_to_point'}}
                                                }}}}}}}
             }}

    golden_output2 = {'execute.return_value': '''
        Ethernet4/1 - Process ID UNDERLAY VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State DOWN, Network type BROADCAST
        Ethernet4/10 - Process ID UNDERLAY VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State DOWN, Network type BROADCAST
        loopback1 - Process ID UNDERLAY VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        loopback2 - Process ID UNDERLAY VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        loopback3 - Process ID UNDERLAY VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        loopback4 - Process ID UNDERLAY VRF default, area 0.0.0.0
            LDP Autoconfig not enabled
            LDP Sync not enabled, not required
            State LOOPBACK, Network type LOOPBACK
        '''}

    golden_parsed_output2 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'UNDERLAY':
                                {'areas':
                                    {'0.0.0.0':
                                        {'mpls':
                                            {'ldp':
                                                {'autoconfig': False,
                                                'autoconfig_area_id': '0.0.0.0',
                                                'igp_sync': False,
                                                'required': False}},
                                        'interfaces':
                                            {'Ethernet4/1':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'broadcast',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'Ethernet4/1',
                                                'state': 'down'},
                                            'Ethernet4/10':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'broadcast',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'Ethernet4/10',
                                                'state': 'down'},
                                            'loopback1':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'loopback1',
                                                'state': 'loopback'},
                                            'loopback2':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'loopback2',
                                                'state': 'loopback'},
                                            'loopback3':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'loopback3',
                                                'state': 'loopback'},
                                            'loopback4':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': False,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': False,
                                                        'required': False}},
                                                'name': 'loopback4',
                                                'state': 'loopback'}}}}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        port-channel4001 - Process ID 1 VRF VRF2, area 0.0.1.1
            LDP Autoconfig is enabled
            LDP Sync is enabled, is required and is achieved
            State P2P, Network type P2P
        port-channel4002 - Process ID 1 VRF VRF2, area 0.0.1.1
            LDP Autoconfig is enabled
            LDP Sync is enabled, is required and is achieved
            State P2P, Network type P2P
        '''}

    golden_parsed_output3 = {
        'vrf':{
            'VRF2':
                {'address_family':
                     {'ipv4':
                          {'instance':
                               {'1':
                                    {'areas':
                                         {'0.0.1.1':
                                              {'mpls':
                                                   {'ldp':
                                                        {'autoconfig': True,
                                                         'autoconfig_area_id': '0.0.1.1',
                                                         'igp_sync': True,
                                                         'required': True,
                                                         'achieved': True}},
                                              'interfaces':
                                                   {'port-channel4001':
                                                        {'area': '0.0.1.1',
                                                         'interface_type': 'point_to_point',
                                                         'mpls':
                                                             {'ldp':
                                                                  {'autoconfig': True,
                                                                   'autoconfig_area_id': '0.0.1.1',
                                                                   'igp_sync': True,
                                                                   'required': True,
                                                                   'achieved': True}},
                                                         'name': 'port-channel4001',
                                                         'state': 'point_to_point'},
                                                   'port-channel4002':
                                                        {'area': '0.0.1.1',
                                                         'interface_type': 'point_to_point',
                                                         'mpls':
                                                             {'ldp':
                                                                  {'autoconfig': True,
                                                                   'autoconfig_area_id': '0.0.1.1',
                                                                   'igp_sync': True,
                                                                   'required': True,
                                                                   'achieved': True}},
                                                         'name': 'port-channel4002',
                                                         'state': 'point_to_point'}}
                                               }}}}}}}}}

    golden_output4 = {'execute.return_value': '''
        port-channel4001 - Process ID 1 VRF VRF1, area 0.0.1.1
            LDP Autoconfig is enabled
            LDP Sync is enabled, is required and not achieved
            State P2P, Network type P2P
        port-channel4002 - Process ID 1 VRF VRF1, area 0.0.1.1
            LDP Autoconfig is enabled
            LDP Sync is enabled, is required and not achieved
            State P2P, Network type P2P
        '''}

    golden_parsed_output4 = {
        'vrf': {
            'VRF1':
                {'address_family':
                     {'ipv4':
                          {'instance':
                               {'1':
                                    {'areas':
                                         {'0.0.1.1':
                                              {'mpls':
                                                   {'ldp':
                                                        {'autoconfig': True,
                                                         'autoconfig_area_id': '0.0.1.1',
                                                         'igp_sync': True,
                                                         'required': True,
                                                         'achieved': False}},
                                               'interfaces':
                                                   {'port-channel4001':
                                                        {'area': '0.0.1.1',
                                                         'interface_type': 'point_to_point',
                                                         'mpls':
                                                             {'ldp':
                                                                  {'autoconfig': True,
                                                                   'autoconfig_area_id': '0.0.1.1',
                                                                   'igp_sync': True,
                                                                   'required': True,
                                                                   'achieved': False}},
                                                         'name': 'port-channel4001',
                                                         'state': 'point_to_point'},
                                                    'port-channel4002':
                                                        {'area': '0.0.1.1',
                                                         'interface_type': 'point_to_point',
                                                         'mpls':
                                                             {'ldp':
                                                                  {'autoconfig': True,
                                                                   'autoconfig_area_id': '0.0.1.1',
                                                                   'igp_sync': True,
                                                                   'required': True,
                                                                   'achieved': False}},
                                                         'name': 'port-channel4002',
                                                         'state': 'point_to_point'}}
                                               }}}}}}}
        }}

    golden_output5 = {'execute.return_value': '''
        show ip ospf mpls ldp interface vrf all
        loopback0 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig is enabled
            LDP Sync is enabled, not required
            State LOOPBACK, Network type LOOPBACK
        port-channel1 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig is enabled
            LDP Sync is enabled, is required and not achieved
            State DOWN, Network type P2P
        port-channel5 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig is enabled
            LDP Sync is enabled, is required and is achieved
            State P2P, Network type P2P
        port-channel4001 - Process ID 1 VRF default, area 0.0.0.0
            LDP Autoconfig is enabled
            LDP Sync is enabled, is required and is achieved
            State P2P, Network type P2P
        '''}

    golden_parsed_output5 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.0':
                                        {'interfaces':
                                            {'loopback0':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'loopback',
                                                'mpls':
                                                    {'ldp':
                                                        {'autoconfig': True,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': True,
                                                        'required': False}},
                                                'name': 'loopback0',
                                                'state': 'loopback'},
                                            'port-channel1':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'point_to_point',
                                                'mpls':
                                                    {'ldp':
                                                        {'achieved': False,
                                                        'autoconfig': True,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': True,
                                                        'required': True}},
                                                'name': 'port-channel1',
                                                'state': 'down'},
                                            'port-channel4001':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'point_to_point',
                                                'mpls':
                                                    {'ldp':
                                                        {'achieved': True,
                                                        'autoconfig': True,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': True,
                                                        'required': True}},
                                                  'name': 'port-channel4001',
                                                  'state': 'point_to_point'},
                                            'port-channel5':
                                                {'area': '0.0.0.0',
                                                'interface_type': 'point_to_point',
                                                'mpls':
                                                    {'ldp':
                                                        {'achieved': True,
                                                        'autoconfig': True,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': True,
                                                        'required': True}},
                                                'name': 'port-channel5',
                                                'state': 'point_to_point'}},
                                                'mpls':
                                                    {'ldp':
                                                        {'achieved': True,
                                                        'autoconfig': True,
                                                        'autoconfig_area_id': '0.0.0.0',
                                                        'igp_sync': True,
                                                        'required': True}}}}}}}}}}}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ip_ospf_mpls_ldp_interface_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_ospf_mpls_ldp_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_ospf_mpls_ldp_interface_vrf_vrf2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse(vrf="VRF2")
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_ip_ospf_mpls_ldp_interface_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_ip_ospf_mpls_ldp_interface_vrf_all2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowIpOspfMplsLdpInterface(device=self.device)
        parsed_output = obj.parse(vrf="all")
        self.assertEqual(parsed_output, self.golden_parsed_output5)


# ===================================================
#  Unit test for 'show ip ospf virtual-links vrf all'
# ===================================================
class TestShowIpOspfVirtualLinks(unittest.TestCase):

    '''Unit test for 'show ip ospf virtual-links vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.1':
                                        {'virtual_links':
                                            {'0.0.0.1 10.64.4.4':
                                                {'backbone_area_id': '0.0.0.0',
                                                'cost': 40,
                                                'dead_interval': 40,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:05',
                                                'index': 7,
                                                'interface': 'Ethernet1/5',
                                                'interface_type': 'point_to_point',
                                                'link_state': 'up',
                                                'name': 'VL1',
                                                'nbr_adjs': 1,
                                                'nbr_flood': 1,
                                                'nbr_total': 1,
                                                'neighbors':
                                                    {'10.64.4.4':
                                                        {'address': '10.19.4.4',
                                                        'dbd_option': '0x72',
                                                        'dead_timer': '00:00:33',
                                                        'hello_option': '0x32',
                                                        'last_change': '00:07:51',
                                                        'last_non_hello_received': '00:07:49',
                                                        'neighbor_router_id': '10.64.4.4',
                                                        'state': 'full',
                                                        'statistics':
                                                            {'nbr_event_count': 5}}},
                                                'remote_addr': '10.19.4.4',
                                                'retransmit_interval': 5,
                                                'router_id': '10.64.4.4',
                                                'state': 'point_to_point',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0},
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 1,
                                                'unnumbered_interface': 'Ethernet1/5',
                                                'unnumbered_ip_address': '10.19.4.3',
                                                'wait_interval': 40}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        Virtual link VL1 to router 10.64.4.4 is up
            Transit area 0.0.0.1, via interface Eth1/5, remote addr 10.19.4.4
            Unnumbered interface using IP address of Ethernet1/5 (10.19.4.3)
            Process ID 1 VRF default, area 0.0.0.0
            State P2P, Network type P2P, cost 40
            Index 7, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:05
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
            Adjacency Information
            State is FULL, 5 state changes, last change 00:07:51
            Hello options 0x32, dbd options 0x72
            Last non-hello packet received 00:07:49
              Dead timer due in 00:00:33
        '''}

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfVirtualLinks(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfVirtualLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ================================================
#  Unit test for 'show ip ospf sham-links vrf all'
# ================================================
class TestShowIpOspfShamLinks(unittest.TestCase):

    '''Unit test for 'show ip ospf sham-links vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.1':
                                        {'sham_links':
                                            {'10.151.22.22 10.229.11.11':
                                                {'backbone_area_id': '0.0.0.0',
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'destination': '10.229.11.11',
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:02',
                                                'index': 6,
                                                'interface_type': 'point_to_point',
                                                'link_state': 'up',
                                                'local_id': '10.151.22.22',
                                                'name': 'SL1',
                                                'nbr_adjs': 1,
                                                'nbr_flood': 1,
                                                'nbr_total': 1,
                                                'neighbors':
                                                    {'10.229.11.11':
                                                        {'address': '10.229.11.11',
                                                        'area': '0.0.0.1',
                                                        'backbone_area_id': '0.0.0.0',
                                                        'dbd_option': '0x72',
                                                        'dead_timer': '00:00:38',
                                                        'hello_option': '0x32',
                                                        'instance': '1',
                                                        'last_change': '08:10:01',
                                                        'last_non_hello_received': 'never',
                                                        'local': '10.151.22.22',
                                                        'neighbor_router_id': '10.229.11.11',
                                                        'remote': '10.229.11.11',
                                                        'state': 'full',
                                                        'statistics': {'nbr_event_count': 8}}},
                                                'remote_id': '10.229.11.11',
                                                'retransmit_interval': 5,
                                                'state': 'point_to_point',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0},
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 1,
                                                'unnumbered_interface': 'loopback1',
                                                'unnumbered_ip_address': '10.151.22.22',
                                                'wait_interval': 40},
                                            '10.151.22.22 10.21.33.33':
                                                {'authentication':
                                                    {'auth_trailer_key':
                                                        {'crypto_algorithm': 'simple'},
                                                    'auth_trailer_key_chain':
                                                        {'key_chain': 'test',
                                                        'status': 'ready'}},
                                                'backbone_area_id': '0.0.0.0',
                                                'cost': 111,
                                                'dead_interval': 13,
                                                'destination': '10.21.33.33',
                                                'hello_interval': 3,
                                                'hello_timer': '00:00:01',
                                                'index': 7,
                                                'nbr_adjs': 0,
                                                'nbr_flood': 0,
                                                'nbr_total': 0,
                                                'interface_type': 'point_to_point',
                                                'link_state': 'up',
                                                'local_id': '10.151.22.22',
                                                'name': 'SL2',
                                                'remote_id': '10.21.33.33',
                                                'retransmit_interval': 5,
                                                'state': 'point_to_point',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0},
                                                'transit_area_id': '0.0.0.1',
                                                'transmit_delay': 7,
                                                'unnumbered_interface': 'loopback1',
                                                'unnumbered_ip_address': '10.151.22.22',
                                                'wait_interval': 13}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        SL1-0.0.0.0-10.151.22.22-10.229.11.11 line protocol is up
            Unnumbered interface using IP address of loopback1 (10.151.22.22)
            Process ID 1 VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 1
            Index 6, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:02
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
            Adjacency Information :
            Destination IP address: 10.229.11.11
         Neighbor 10.229.11.11, interface address 10.229.11.11
            Process ID 1 VRF VRF1, in area 0.0.0.1 via interface SL1-0.0.0.0-10.151.22.22
        -10.229.11.11
            State is FULL, 8 state changes, last change 08:10:01
            Hello options 0x32, dbd options 0x72
            Last non-hello packet received never
              Dead timer due in 00:00:38

         SL2-0.0.0.0-10.151.22.22-10.21.33.33 line protocol is up
            Unnumbered interface using IP address of loopback1 (10.151.22.22)
            Process ID 1 VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 111
            Index 7, Transmit delay 7 sec
            0 Neighbors, flooding to 0, adjacent with 0
            Timer intervals: Hello 3, Dead 13, Wait 13, Retransmit 5
              Hello timer due in 00:00:01
            Simple authentication, using keychain test (ready)
            Number of opaque link LSAs: 0, checksum sum 0
            Adjacency Information :
            Destination IP address: 10.21.33.33
        '''}

    def test_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpOspfShamLinks(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfShamLinks(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ===============================================
#  Unit test for 'show ip ospf interface vrf all'
# ===============================================
class TestShowIpOspfInterfaceVrfAll(unittest.TestCase):

    '''Unit test for 'show ip ospf interface vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'UNDERLAY':
                                {'areas':
                                    {'0.0.0.1':
                                        {'interfaces':
                                            {'Ethernet2/1':
                                                {'bdr_ip_addr': '10.229.6.2',
                                                'bdr_router_id': '10.151.22.22',
                                                'bfd':
                                                    {'enable': False},
                                                'cost': 40,
                                                'dead_interval': 40,
                                                'dr_ip_addr': '10.229.6.6',
                                                'dr_router_id': '10.84.66.66',
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:07',
                                                'if_cfg': True,
                                                'index': 2,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.229.6.2/24',
                                                'line_protocol': 'up',
                                                'name': 'Ethernet2/1',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'state': 'bdr',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40}},
                                        'sham_links':
                                            {'10.151.22.22 10.229.11.11':
                                                {'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:07',
                                                'if_cfg': False,
                                                'index': 6,
                                                'interface_type': 'p2p',
                                                'ip_address': '10.151.22.22',
                                                'line_protocol': 'up',
                                                'name': 'SL1-0.0.0.0-10.151.22.22-10.229.11.11',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'p2p',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            '10.151.22.22 10.21.33.33':
                                                {'authentication':
                                                    {'auth_trailer_key':
                                                        {'crypto_algorithm': 'Simple'},
                                                        'auth_trailer_key_chain':
                                                            {'key_chain': 'test'}},
                                                    'bfd':
                                                        {'enable': False},
                                                    'cost': 111,
                                                    'dead_interval': 13,
                                                    'enable': True,
                                                    'hello_interval': 3,
                                                    'hello_timer': '00:00:00',
                                                    'if_cfg': False,
                                                    'index': 7,
                                                    'interface_type': 'p2p',
                                                    'ip_address': '10.151.22.22',
                                                    'line_protocol': 'up',
                                                    'name': 'SL2-0.0.0.0-10.151.22.22-10.21.33.33',
                                                    'passive': False,
                                                    'retransmit_interval': 5,
                                                    'state': 'p2p',
                                                    'statistics':
                                                        {'link_scope_lsa_cksum_sum': 0,
                                                        'link_scope_lsa_count': 0,
                                                        'num_nbrs_adjacent': 0,
                                                        'num_nbrs_flooding': 0,
                                                        'total_neighbors': 0},
                                                    'transmit_delay': 7,
                                                    'wait_interval': 13}},
                                        'virtual_links':
                                            {'0.0.0.1 10.1.8.8':
                                                {'backbone_area_id': '0.0.0.0',
                                                'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:07',
                                                'if_cfg': False,
                                                'index': 6,
                                                'interface_type': 'p2p',
                                                'ip_address': '10.151.22.22',
                                                'line_protocol': 'up',
                                                'name': 'VL1-0.0.0.0-10.1.8.8-10.66.12.12',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'p2p',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}}}}}}}},
            'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'UNDERLAY':
                                {'areas':
                                    {'0.0.0.0':
                                        {'interfaces':
                                            {'Ethernet2/2':
                                                {'bdr_ip_addr': '10.2.3.2',
                                                'bdr_router_id': '10.100.2.2',
                                                'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'dr_ip_addr': '10.2.3.3',
                                                'dr_router_id': '10.36.3.3',
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:02',
                                                'if_cfg': True,
                                                'index': 3,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.2.3.2/24',
                                                'line_protocol': 'up',
                                                'name': 'Ethernet2/2',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'state': 'bdr',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'Ethernet2/3':
                                                {'bdr_ip_addr': '10.2.4.2',
                                                'bdr_router_id': '10.100.2.2',
                                                'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'dr_ip_addr': '10.2.4.4',
                                                'dr_router_id': '10.64.4.4',
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:00',
                                                'if_cfg': True,
                                                'index': 4,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.2.4.2/24',
                                                'line_protocol': 'up',
                                                'name': 'Ethernet2/3',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'state': 'bdr',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'Ethernet2/4':
                                                {'bdr_ip_addr': '10.1.2.2',
                                                'bdr_router_id': '10.100.2.2',
                                                'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'dr_ip_addr': '10.1.2.1',
                                                'dr_router_id': '10.4.1.1',
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:00',
                                                'if_cfg': True,
                                                'index': 5,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.1.2.2/24',
                                                'line_protocol': 'up',
                                                'name': 'Ethernet2/4',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'state': 'bdr',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40},
                                            'loopback0':
                                                {'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'enable': True,
                                                'if_cfg': True,
                                                'index': 1,
                                                'interface_type': 'loopback',
                                                'ip_address': '10.100.2.2/32',
                                                'line_protocol': 'up',
                                                'name': 'loopback0',
                                                'state': 'loopback'}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf interface vrf all
         Ethernet2/2 is up, line protocol is up
            IP address 10.2.3.2/24
            Process ID UNDERLAY VRF default, area 0.0.0.0
            Enabled by interface configuration
            State BDR, Network type BROADCAST, cost 1
            Index 3, Transmit delay 1 sec, Router Priority 1
            Designated Router ID: 10.36.3.3, address: 10.2.3.3
            Backup Designated Router ID: 10.100.2.2, address: 10.2.3.2
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:02
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         Ethernet2/3 is up, line protocol is up
            IP address 10.2.4.2/24
            Process ID UNDERLAY VRF default, area 0.0.0.0
            Enabled by interface configuration
            State BDR, Network type BROADCAST, cost 1
            Index 4, Transmit delay 1 sec, Router Priority 1
            Designated Router ID: 10.64.4.4, address: 10.2.4.4
            Backup Designated Router ID: 10.100.2.2, address: 10.2.4.2
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:00
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         Ethernet2/4 is up, line protocol is up
            IP address 10.1.2.2/24
            Process ID UNDERLAY VRF default, area 0.0.0.0
            Enabled by interface configuration
            State BDR, Network type BROADCAST, cost 1
            Index 5, Transmit delay 1 sec, Router Priority 1
            Designated Router ID: 10.4.1.1, address: 10.1.2.1
            Backup Designated Router ID: 10.100.2.2, address: 10.1.2.2
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:00
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         loopback0 is up, line protocol is up
            IP address 10.100.2.2/32
            Process ID UNDERLAY VRF default, area 0.0.0.0
            Enabled by interface configuration
            State LOOPBACK, Network type LOOPBACK, cost 1
            Index 1
         SL1-0.0.0.0-10.151.22.22-10.229.11.11 is up, line protocol is up
            Unnumbered interface using IP address of loopback1 (10.151.22.22)
            Process ID UNDERLAY VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 1
            Index 6, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:07
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         SL2-0.0.0.0-10.151.22.22-10.21.33.33 is up, line protocol is up
            Unnumbered interface using IP address of loopback1 (10.151.22.22)
            Process ID UNDERLAY VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 111
            Index 7, Transmit delay 7 sec
            0 Neighbors, flooding to 0, adjacent with 0
            Timer intervals: Hello 3, Dead 13, Wait 13, Retransmit 5
              Hello timer due in 00:00:00
            Simple authentication, using keychain test (ready)
            Number of opaque link LSAs: 0, checksum sum 0
         VL1-0.0.0.0-10.1.8.8-10.66.12.12 is up, line protocol is up
            Unnumbered interface using IP address of loopback1 (10.151.22.22)
            Process ID UNDERLAY VRF VRF1, area 0.0.0.1
            State P2P, Network type P2P, cost 1
            Index 6, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:07
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         Ethernet2/1 is up, line protocol is up
            IP address 10.229.6.2/24
            Process ID UNDERLAY VRF VRF1, area 0.0.0.1
            Enabled by interface configuration
            State BDR, Network type BROADCAST, cost 40
            Index 2, Transmit delay 1 sec, Router Priority 1
            Designated Router ID: 10.84.66.66, address: 10.229.6.6
            Backup Designated Router ID: 10.151.22.22, address: 10.229.6.2
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:07
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
        '''}

    golden_parsed_output2 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'100':
                                {'areas':
                                    {'0.0.0.1':
                                        {'interfaces':
                                            {'loopback0':
                                                {'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'enable': True,
                                                'if_cfg': True,
                                                'index': 3,
                                                'interface_type': 'loopback',
                                                'ip_address': '192.168.111.1/32',
                                                'line_protocol': 'up',
                                                'name': 'loopback0',
                                                'state': 'loopback'},
                                            'loopback21':
                                                {'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'enable': True,
                                                'if_cfg': True,
                                                'index': 2,
                                                'interface_type': 'loopback',
                                                'ip_address': '192.168.136.1/32',
                                                'line_protocol': 'up',
                                                'name': 'loopback21',
                                                'state': 'loopback'},
                                            'port-channel1.100':
                                                {'bdr_ip_addr': '192.168.234.1',
                                                'bdr_router_id': '192.168.111.1',
                                                'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'dr_ip_addr': '192.168.234.2',
                                                'dr_router_id': '192.168.246.1',
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:04',
                                                'if_cfg': True,
                                                'index': 1,
                                                'interface_type': 'broadcast',
                                                'ip_address': '192.168.234.1/24',
                                                'line_protocol': 'up',
                                                'name': 'port-channel1.100',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'state': 'bdr',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}}}},
                            '2':
                                {'areas':
                                    {'0.0.0.1':
                                        {'interfaces':
                                            {'loopback3':
                                                {'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'enable': True,
                                                'if_cfg': True,
                                                'index': 2,
                                                'interface_type': 'loopback',
                                                'ip_address': '192.168.51.1/32',
                                                'line_protocol': 'up',
                                                'name': 'loopback3',
                                                'state': 'loopback'},
                                            'port-channel1.103':
                                                {'bdr_ip_addr': '192.168.246.1',
                                                'bdr_router_id': '192.168.111.1',
                                                'bfd':
                                                    {'enable': False},
                                                'cost': 1,
                                                'dead_interval': 40,
                                                'dr_ip_addr': '192.168.246.2',
                                                'dr_router_id': '192.168.4.1',
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:05',
                                                'if_cfg': True,
                                                'index': 1,
                                                'interface_type': 'broadcast',
                                                'ip_address': '192.168.246.1/24',
                                                'line_protocol': 'up',
                                                'name': 'port-channel1.103',
                                                'passive': False,
                                                'priority': 1,
                                                'retransmit_interval': 5,
                                                'state': 'bdr',
                                                'statistics':
                                                    {'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1},
                                                'transmit_delay': 1,
                                                'wait_interval': 40}}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        +++ CE1: executing command 'show ip ospf interface vrf all' +++
        show ip ospf interface vrf all

         port-channel1.103 is up, line protocol is up
            IP address 192.168.246.1/24, Process ID 2 VRF default, area 0.0.0.1
            Enabled by interface configuration
            State BDR, Network type BROADCAST, cost 1
            Index 1, Transmit delay 1 sec, Router Priority 1
            Designated Router ID: 192.168.4.1, address: 192.168.246.2
            Backup Designated Router ID: 192.168.111.1, address: 192.168.246.1
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:05
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         loopback3 is up, line protocol is up
            IP address 192.168.51.1/32, Process ID 2 VRF default, area 0.0.0.1
            Enabled by interface configuration
            State LOOPBACK, Network type LOOPBACK, cost 1
            Index 2
         port-channel1.100 is up, line protocol is up
            IP address 192.168.234.1/24, Process ID 100 VRF default, area 0.0.0.1
            Enabled by interface configuration
            State BDR, Network type BROADCAST, cost 1
            Index 1, Transmit delay 1 sec, Router Priority 1
            Designated Router ID: 192.168.246.1, address: 192.168.234.2
            Backup Designated Router ID: 192.168.111.1, address: 192.168.234.1
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
              Hello timer due in 00:00:04
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
         loopback0 is up, line protocol is up
            IP address 192.168.111.1/32, Process ID 100 VRF default, area 0.0.0.1
            Enabled by interface configuration
            State LOOPBACK, Network type LOOPBACK, cost 1
            Index 3
         loopback21 is up, line protocol is up
            IP address 192.168.136.1/32, Process ID 100 VRF default, area 0.0.0.1
            Enabled by interface configuration
            State LOOPBACK, Network type LOOPBACK, cost 1
            Index 2
        '''}

    golden_output_customer = {'execute.return_value': '''
        show ip ospf interface vrf all

        Vlan3030 is up, line protocol is up
            IP address 10.115.128.4/24
            Process ID 2000 VRF default, area 0.0.0.1
            Enabled by interface configuration
            State DR, Network type BROADCAST, cost 1000
            Index 118, Passive interface
        Vlan997 is up, line protocol is up
            IP address 10.100.17.81/30
            Process ID 2000 VRF default, area 0.0.0.1
            Enabled by interface configuration
            State P2P, Network type P2P, cost 10
            Index 137, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
            Hello timer due in 00:00:04
            No authentication
            Number of opaque link LSAs: 1, checksum sum 0xe038
        Vlan986 is up, line protocol is up
            IP address 10.100.17.51/29
            Process ID 2000 VRF default, area 0.0.0.1
            Enabled by interface configuration
            State DR, Network type BROADCAST, cost 1000
            Index 122, Passive interface
        loopback100 is up, line protocol is up
            IP address 10.100.0.11/32
            Process ID 2000 VRF default, area 0.0.0.1
            Enabled by interface configuration
            State LOOPBACK, Network type LOOPBACK, cost 1
            Index 50
        Ethernet1/31 is up, line protocol is up
            IP address 10.100.31.252/31
            Process ID 2000 VRF default, area 0.0.0.1
            Enabled by interface configuration
            State P2P, Network type P2P, cost 100
            Index 3, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 2, Dead 6, Wait 6, Retransmit 5
            Hello timer due in 00:00:01
            Message-digest authentication, using key id 1
            Number of opaque link LSAs: 1, checksum sum 0xafaf
        Ethernet1/45 is up, line protocol is down
            IP address 10.111.3.2/30
            Process ID 2000 VRF default, area 0.0.0.1
            State DOWN, Network type P2P, cost 100
            Index 1, Transmit delay 1 sec
            0 Neighbors, flooding to 0, adjacent with 0
            Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0

        Vlan959 is up, line protocol is up
            IP address 10.100.31.217/30
            Process ID 1000 VRF GENIE-CORE, area 0.0.0.1
            Enabled by interface configuration
            State P2P, Network type P2P, cost 10
            Index 4, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 2, Dead 6, Wait 6, Retransmit 5
            Hello timer due in 00:00:00
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
        port-channel1001 is up, line protocol is up
            IP address 10.100.31.197/30
            Process ID 1000 VRF GENIE-CORE, area 0.0.0.1
            Enabled by interface configuration
            State P2P, Network type P2P, cost 10
            BFD is enabled
            Index 5, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 2, Dead 6, Wait 6, Retransmit 5
            Hello timer due in 00:00:01
            No authentication
            Number of opaque link LSAs: 0, checksum sum 0
        loopback110 is up, line protocol is up
            IP address 10.100.0.13/32
            Process ID 1000 VRF GENIE-CORE, area 0.0.0.1
            Enabled by interface configuration
            State LOOPBACK, Network type LOOPBACK, cost 1
            Index 3
        Ethernet1/2 is up, line protocol is up
            IP address 10.100.31.27/31
            Process ID 1000 VRF GENIE-CORE, area 0.0.0.1
            Enabled by interface configuration
            State P2P, Network type P2P, cost 20
            Index 1, Transmit delay 1 sec
            1 Neighbors, flooding to 1, adjacent with 1
            Timer intervals: Hello 2, Dead 6, Wait 6, Retransmit 5
            Hello timer due in 00:00:01
            Message-digest authentication, using key id 1
            Number of opaque link LSAs: 0, checksum sum 0
    '''}

    golden_parsed_output_customer = {
        'vrf': {
            'GENIE-CORE': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '1000': {
                                'areas': {
                                    '0.0.0.1': {
                                        'interfaces': {
                                            'Ethernet1/2': {
                                                'bfd': {
                                                    'enable': False
                                                },
                                                'cost': 20,
                                                'dead_interval': 6,
                                                'enable': True,
                                                'hello_interval': 2,
                                                'hello_timer': '00:00:01',
                                                'if_cfg': True,
                                                'index': 1,
                                                'interface_type': 'p2p',
                                                'ip_address': '10.100.31.27/31',
                                                'line_protocol': 'up',
                                                'name': 'Ethernet1/2',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'p2p',
                                                'statistics': {
                                                    'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1
                                                },
                                                'transmit_delay': 1,
                                                'wait_interval': 6
                                            },
                                            'Vlan959': {
                                                'bfd': {
                                                    'enable': False
                                                },
                                                'cost': 10,
                                                'dead_interval': 6,
                                                'enable': True,
                                                'hello_interval': 2,
                                                'hello_timer': '00:00:00',
                                                'if_cfg': True,
                                                'index': 4,
                                                'interface_type': 'p2p',
                                                'ip_address': '10.100.31.217/30',
                                                'line_protocol': 'up',
                                                'name': 'Vlan959',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'p2p',
                                                'statistics': {
                                                    'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1
                                                },
                                                'transmit_delay': 1,
                                                'wait_interval': 6
                                            },
                                            'loopback110': {
                                                'bfd': {
                                                    'enable': False
                                                },
                                                'cost': 1,
                                                'enable': True,
                                                'if_cfg': True,
                                                'index': 3,
                                                'interface_type': 'loopback',
                                                'ip_address': '10.100.0.13/32',
                                                'line_protocol': 'up',
                                                'name': 'loopback110',
                                                'state': 'loopback'
                                            },
                                            'port-channel1001': {
                                                'bfd': {
                                                    'enable': True
                                                },
                                                'cost': 10,
                                                'dead_interval': 6,
                                                'enable': True,
                                                'hello_interval': 2,
                                                'hello_timer': '00:00:01',
                                                'if_cfg': True,
                                                'index': 5,
                                                'interface_type': 'p2p',
                                                'ip_address': '10.100.31.197/30',
                                                'line_protocol': 'up',
                                                'name': 'port-channel1001',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'p2p',
                                                'statistics': {
                                                    'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1
                                                },
                                                'transmit_delay': 1,
                                                'wait_interval': 6
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '2000': {
                                'areas': {
                                    '0.0.0.1': {
                                        'interfaces': {
                                            'Ethernet1/31': {
                                                'bfd': {
                                                    'enable': False
                                                },
                                                'cost': 100,
                                                'dead_interval': 6,
                                                'enable': True,
                                                'hello_interval': 2,
                                                'hello_timer': '00:00:01',
                                                'if_cfg': True,
                                                'index': 3,
                                                'interface_type': 'p2p',
                                                'ip_address': '10.100.31.252/31',
                                                'line_protocol': 'up',
                                                'name': 'Ethernet1/31',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'p2p',
                                                'statistics': {
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1
                                                },
                                                'transmit_delay': 1,
                                                'wait_interval': 6
                                            },
                                            'Ethernet1/45': {
                                                'bfd': {
                                                    'enable': False
                                                },
                                                'cost': 100,
                                                'dead_interval': 40,
                                                'enable': True,
                                                'hello_interval': 10,
                                                'if_cfg': False,
                                                'index': 1,
                                                'interface_type': 'p2p',
                                                'ip_address': '10.111.3.2/30',
                                                'line_protocol': 'down',
                                                'name': 'Ethernet1/45',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'down',
                                                'statistics': {
                                                    'link_scope_lsa_cksum_sum': 0,
                                                    'link_scope_lsa_count': 0,
                                                    'num_nbrs_adjacent': 0,
                                                    'num_nbrs_flooding': 0,
                                                    'total_neighbors': 0
                                                },
                                                'transmit_delay': 1,
                                                'wait_interval': 40
                                            },
                                            'Vlan3030': {
                                                'bfd': {
                                                    'enable': False
                                                },
                                                'cost': 1000,
                                                'enable': True,
                                                'if_cfg': True,
                                                'index': 118,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.115.128.4/24',
                                                'line_protocol': 'up',
                                                'name': 'Vlan3030',
                                                'passive': True,
                                                'state': 'dr'
                                            },
                                            'Vlan986': {
                                                'bfd': {
                                                    'enable': False
                                                },
                                                'cost': 1000,
                                                'enable': True,
                                                'if_cfg': True,
                                                'index': 122,
                                                'interface_type': 'broadcast',
                                                'ip_address': '10.100.17.51/29',
                                                'line_protocol': 'up',
                                                'name': 'Vlan986',
                                                'passive': True,
                                                'state': 'dr'
                                            },
                                            'Vlan997': {
                                                'bfd': {
                                                    'enable': False
                                                },
                                                'cost': 10,
                                                'dead_interval': 40,
                                                'enable': True,
                                                'hello_interval': 10,
                                                'hello_timer': '00:00:04',
                                                'if_cfg': True,
                                                'index': 137,
                                                'interface_type': 'p2p',
                                                'ip_address': '10.100.17.81/30',
                                                'line_protocol': 'up',
                                                'name': 'Vlan997',
                                                'passive': False,
                                                'retransmit_interval': 5,
                                                'state': 'p2p',
                                                'statistics': {
                                                    'num_nbrs_adjacent': 1,
                                                    'num_nbrs_flooding': 1,
                                                    'total_neighbors': 1
                                                },
                                                'transmit_delay': 1,
                                                'wait_interval': 40
                                            },
                                            'loopback100': {
                                                'bfd': {
                                                    'enable': False
                                                },
                                                'cost': 1,
                                                'enable': True,
                                                'if_cfg': True,
                                                'index': 50,
                                                'interface_type': 'loopback',
                                                'ip_address': '10.100.0.11/32',
                                                'line_protocol': 'up',
                                                'name': 'loopback100',
                                                'state': 'loopback'
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

    def test_full_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_full_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_customer(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_customer)
        obj = ShowIpOspfInterface(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_customer)

# ======================================================
#  Unit test for 'show ip ospf neighbors detail vrf all'
# ======================================================
class TestShowIpOspfNeighborsDetailVrfAll(unittest.TestCase):

    '''Unit test for 'show ip ospf neighbors detail vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.1':
                                        {'interfaces':
                                            {'Ethernet2/1':
                                                {'neighbors':
                                                    {'10.84.66.66':
                                                        {'address': '10.229.6.6',
                                                        'bdr_ip_addr': '10.229.6.2',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:38',
                                                        'dr_ip_addr': '10.229.6.6',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': 'never',
                                                        'last_state_change': '08:38:39',
                                                        'priority': 1,
                                                        'neighbor_router_id': '10.84.66.66',
                                                        'state': 'full',
                                                        'statistics':
                                                            {'nbr_event_count': 6}}}}},
                                        'sham_links':
                                            {'10.151.22.22 10.229.11.11':
                                                {'neighbors':
                                                    {'10.229.11.11':
                                                        {'address': '10.229.11.11',
                                                        'dbd_options': '0x72',
                                                        'dead_timer': '00:00:41',
                                                        'hello_options': '0x32',
                                                        'last_non_hello_packet_received': 'never',
                                                        'last_state_change': '08:16:20',
                                                        'neighbor_router_id': '10.229.11.11',
                                                        'state': 'full',
                                                        'statistics':
                                                            {'nbr_event_count': 8}}}}}}}}}}}},
            'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.0':
                                        {'interfaces':
                                            {'Ethernet1/2':
                                                {'neighbors':
                                                    {'10.4.1.1':
                                                        {'address': '10.1.3.1',
                                                        'bdr_ip_addr': '10.1.3.3',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:36',
                                                        'dr_ip_addr': '10.1.3.1',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': '00:00:15',
                                                        'last_state_change': '11:04:28',
                                                        'priority': 1,
                                                        'neighbor_router_id': '10.4.1.1',
                                                        'state': 'full',
                                                        'statistics':
                                                            {'nbr_event_count': 5}}}},
                                            'Ethernet2/2':
                                                {'neighbors':
                                                    {'10.36.3.3':
                                                        {'address': '10.2.3.3',
                                                        'bdr_ip_addr': '10.2.3.2',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:39',
                                                        'dr_ip_addr': '10.2.3.3',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': 'never',
                                                        'last_state_change': '08:38:40',
                                                        'priority': 1,
                                                        'neighbor_router_id': '10.36.3.3',
                                                        'state': 'full',
                                                        'statistics':
                                                            {'nbr_event_count': 5}}}},
                                            'Ethernet2/3':
                                                {'neighbors':
                                                    {'10.64.4.4':
                                                        {'address': '10.2.4.4',
                                                        'bdr_ip_addr': '10.2.4.2',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:33',
                                                        'dr_ip_addr': '10.2.4.4',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': 'never',
                                                        'last_state_change': '08:38:42',
                                                        'priority': 1,
                                                        'neighbor_router_id': '10.64.4.4',
                                                        'state': 'full',
                                                        'statistics':
                                                            {'nbr_event_count': 6}}}},
                                            'Ethernet2/4':
                                                {'neighbors':
                                                    {'10.4.1.1':
                                                        {'address': '10.1.2.1',
                                                        'bdr_ip_addr': '10.1.2.2',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:35',
                                                        'dr_ip_addr': '10.1.2.1',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': 'never',
                                                        'last_state_change': '08:38:41',
                                                        'priority': 1,
                                                        'neighbor_router_id': '10.4.1.1',
                                                        'state': 'full',
                                                        'statistics':
                                                            {'nbr_event_count': 5}}}}},
                                        'virtual_links':
                                            {'0.0.0.1 10.64.4.4':
                                                {'neighbors':
                                                    {'10.64.4.4':
                                                        {'address': '10.19.4.4',
                                                        'dbd_options': '0x72',
                                                        'dead_timer': '00:00:43',
                                                        'hello_options': '0x32',
                                                        'last_non_hello_packet_received': '00:00:18',
                                                        'last_state_change': '00:00:23',
                                                        'neighbor_router_id': '10.64.4.4',
                                                        'state': 'full',
                                                        'statistics':
                                                            {'nbr_event_count': 5}}}}}},
                                    '0.0.0.1':
                                        {'interfaces':
                                            {'Ethernet1/3':
                                                {'neighbors':
                                                    {'10.100.2.2':
                                                        {'address': '10.229.3.2',
                                                        'bdr_ip_addr': '10.229.3.3',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:36',
                                                        'dr_ip_addr': '10.229.3.2',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': '00:00:18',
                                                        'last_state_change': '11:04:25',
                                                        'priority': 1,
                                                        'neighbor_router_id': '10.100.2.2',
                                                        'state': 'full',
                                                        'statistics':
                                                            {'nbr_event_count': 5}}}},
                                            'Ethernet1/5':
                                                {'neighbors':
                                                    {'10.64.4.4':
                                                        {'address': '10.19.4.4',
                                                        'bdr_ip_addr': '10.19.4.3',
                                                        'dbd_options': '0x52',
                                                        'dead_timer': '00:00:36',
                                                        'dr_ip_addr': '10.19.4.4',
                                                        'hello_options': '0x12',
                                                        'last_non_hello_packet_received': '00:00:18',
                                                        'last_state_change': '11:04:28',
                                                        'priority': 1,
                                                        'neighbor_router_id': '10.64.4.4',
                                                        'state': 'full',
                                                        'statistics':
                                                            {'nbr_event_count': 6}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf neighbors detail vrf all
          Neighbor 10.36.3.3, interface address 10.2.3.3
            Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet2/2
            State is FULL, 5 state changes, last change 08:38:40
            Neighbor priority is 1
            DR is 10.2.3.3 BDR is 10.2.3.2
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received never
            Dead timer due in 00:00:39
          Neighbor 10.64.4.4, interface address 10.2.4.4
            Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet2/3
            State is FULL, 6 state changes, last change 08:38:42
            Neighbor priority is 1
            DR is 10.2.4.4 BDR is 10.2.4.2
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received never
            Dead timer due in 00:00:33
          Neighbor 10.4.1.1, interface address 10.1.2.1
            Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet2/4
            State is FULL, 5 state changes, last change 08:38:41
            Neighbor priority is 1
            DR is 10.1.2.1 BDR is 10.1.2.2
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received never
            Dead timer due in 00:00:35
          Neighbor 10.229.11.11, interface address 10.229.11.11
            Process ID 1 VRF VRF1, in area 0.0.0.1 via interface SL1-0.0.0.0-10.151.22.22-10.229.11.11
            State is FULL, 8 state changes, last change 08:16:20
            Hello options 0x32, dbd options 0x72
            Last non-hello packet received never
            Dead timer due in 00:00:41
          Neighbor 10.84.66.66, interface address 10.229.6.6
            Process ID 1 VRF VRF1, in area 0.0.0.1 via interface Ethernet2/1
            State is FULL, 6 state changes, last change 08:38:39
            Neighbor priority is 1
            DR is 10.229.6.6 BDR is 10.229.6.2
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received never
            Dead timer due in 00:00:38
          Neighbor 10.64.4.4, interface address 10.19.4.4
            Process ID 1 VRF default, in area 0.0.0.0 via interface VL1-0.0.0.1-10.64.4.4
            State is FULL, 5 state changes, last change 00:00:23
            We are slave in DBD exchange, seqnr 0x26aa , all DBDs sent and acked
            Hello options 0x32, dbd options 0x72
            Last non-hello packet received 00:00:18
              Dead timer due in 00:00:43
              DBD rxmit timer due in 00:00:22
          Neighbor 10.4.1.1, interface address 10.1.3.1
            Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet1/2
            State is FULL, 5 state changes, last change 11:04:28
            Neighbor priority is 1
            DR is 10.1.3.1 BDR is 10.1.3.3
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received 00:00:15
              Dead timer due in 00:00:36
          Neighbor 10.100.2.2, interface address 10.229.3.2
            Process ID 1 VRF default, in area 0.0.0.1 via interface Ethernet1/3
            State is FULL, 5 state changes, last change 11:04:25
            Neighbor priority is 1
            DR is 10.229.3.2 BDR is 10.229.3.3
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received 00:00:18
              Dead timer due in 00:00:36
          Neighbor 10.64.4.4, interface address 10.19.4.4
            Process ID 1 VRF default, in area 0.0.0.1 via interface Ethernet1/5
            State is FULL, 6 state changes, last change 11:04:28
            Neighbor priority is 1
            DR is 10.19.4.4 BDR is 10.19.4.3
            Hello options 0x12, dbd options 0x52
            Last non-hello packet received 00:00:18
              Dead timer due in 00:00:36
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfNeighborDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================================
#  Unit test for 'show ip ospf database external detail vrf all'
# ==============================================================
class TestShowIpOspfDatabaseExternalDetailVrfAll(unittest.TestCase):

    '''Unit test for 'show ip ospf database external detail vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'UNDERLAY':
                                {'areas':
                                    {'0.0.0.0':
                                        {'database':
                                            {'lsa_types':
                                                {5:
                                                    {'lsa_type': 5,
                                                    'lsas':
                                                        {'10.94.44.44 10.64.4.4':
                                                            {'lsa_id': '10.94.44.44',
                                                            'adv_router': '10.64.4.4',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'external':
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies':
                                                                            {0:
                                                                                {'external_route_tag': 0,
                                                                                'flags': 'E',
                                                                                'forwarding_address': '0.0.0.0',
                                                                                'metric': 20,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.64.4.4',
                                                                    'age': 1565,
                                                                    'checksum': '0x7d61',
                                                                    'length': 36,
                                                                    'lsa_id': '10.94.44.44',
                                                                    'option': '0x20',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 5}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf database external detail vrf all
        OSPF Router with ID (10.100.2.2) (Process ID UNDERLAY VRF default)

                Type-5 AS External Link States

        LS age: 1565
        Options: 0x20 (No TOS-capability, DC)
        LS Type: Type-5 AS-External
        Link State ID: 10.94.44.44 (Network address)
        Advertising Router: 10.64.4.4
        LS Seq Number: 0x80000002
        Checksum: 0x7d61
        Length: 36
        Network Mask: /32
             Metric Type: 2 (Larger than any link state path)
             TOS: 0
             Metric: 20
             Forward Address: 0.0.0.0
             External Route Tag: 0
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseExternalDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseExternalDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================================
#  Unit test for 'show ip ospf database network detail vrf all'
# ==============================================================
class TestShowIpOspfDatabaseNetworkDetailVrfAll(unittest.TestCase):

    '''Unit test for 'show ip ospf database network detail vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.1':
                                        {'database':
                                            {'lsa_types':
                                                {2:
                                                    {'lsa_type': 2,
                                                    'lsas':
                                                        {'10.186.5.1 10.229.11.11':
                                                            {'lsa_id': '10.186.5.1',
                                                            'adv_router': '10.229.11.11',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'network':
                                                                        {'attached_routers':
                                                                            {'10.229.11.11': {},
                                                                            '10.115.55.55': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header':
                                                                    {'adv_router': '10.229.11.11',
                                                                    'age': 1454,
                                                                    'checksum': '0xddd9',
                                                                    'length': 32,
                                                                    'lsa_id': '10.186.5.1',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000033',
                                                                    'type': 2}}},
                                                        '10.229.6.6 10.84.66.66':
                                                            {'lsa_id': '10.229.6.6',
                                                            'adv_router': '10.84.66.66',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'network':
                                                                        {'attached_routers':
                                                                            {'10.151.22.22': {},
                                                                            '10.84.66.66': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header':
                                                                    {'adv_router': '10.84.66.66',
                                                                    'age': 1080,
                                                                    'checksum': '0x3f5f',
                                                                    'length': 32,
                                                                    'lsa_id': '10.229.6.6',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000010',
                                                                    'type': 2}}},
                                                        '10.19.7.7 10.1.77.77':
                                                            {'adv_router': '10.1.77.77',
                                                            'lsa_id': '10.19.7.7',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'network':
                                                                        {'attached_routers':
                                                                            {'10.36.3.3': {},
                                                                            '10.1.77.77': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header':
                                                                    {'adv_router': '10.1.77.77',
                                                                    'age': 812,
                                                                    'checksum': '0x5a1a',
                                                                    'length': 32,
                                                                    'lsa_id': '10.19.7.7',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x8000002b',
                                                                    'type': 2}}},
                                                        '10.115.6.6 10.84.66.66':
                                                            {'lsa_id': '10.115.6.6',
                                                            'adv_router': '10.84.66.66',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'network':
                                                                        {'attached_routers':
                                                                            {'10.115.55.55': {},
                                                                            '10.84.66.66': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header':
                                                                    {'adv_router': '10.84.66.66',
                                                                    'age': 573,
                                                                    'checksum': '0x5f9d',
                                                                    'length': 32,
                                                                    'lsa_id': '10.115.6.6',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x8000002a',
                                                                    'type': 2}}},
                                                        '10.166.7.6 10.84.66.66':
                                                            {'lsa_id': '10.166.7.6',
                                                            'adv_router': '10.84.66.66',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'network':
                                                                        {'attached_routers':
                                                                            {'10.84.66.66': {},
                                                                            '10.1.77.77': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header':
                                                                    {'adv_router': '10.84.66.66',
                                                                    'age': 1819,
                                                                    'checksum': '0x960b',
                                                                    'length': 32,
                                                                    'lsa_id': '10.166.7.6',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x8000002b',
                                                                    'type': 2}}}}}}}}}}}}}},
            'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.0':
                                        {'database':
                                            {'lsa_types':
                                                {2:
                                                    {'lsa_type': 2,
                                                    'lsas':
                                                        {'10.1.2.1 10.4.1.1':
                                                            {'lsa_id': '10.1.2.1',
                                                            'adv_router': '10.4.1.1',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'network':
                                                                        {'attached_routers':
                                                                            {'10.4.1.1': {},
                                                                            '10.100.2.2': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header':
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 772,
                                                                    'checksum': '0x3bd1',
                                                                    'length': 32,
                                                                    'lsa_id': '10.1.2.1',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000010',
                                                                    'type': 2}}},
                                                        '10.1.4.4 10.64.4.4':
                                                            {'lsa_id': '10.1.4.4',
                                                            'adv_router': '10.64.4.4',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'network':
                                                                        {'attached_routers':
                                                                            {'10.4.1.1': {},
                                                                            '10.64.4.4': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header':
                                                                    {'adv_router': '10.64.4.4',
                                                                    'age': 1482,
                                                                    'checksum': '0xa232',
                                                                    'length': 32,
                                                                    'lsa_id': '10.1.4.4',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x8000002f',
                                                                    'type': 2}}},
                                                        '10.2.3.3 10.36.3.3':
                                                            {'lsa_id': '10.2.3.3',
                                                            'adv_router': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'network':
                                                                        {'attached_routers':
                                                                            {'10.100.2.2': {},
                                                                            '10.36.3.3': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 788,
                                                                    'checksum': '0x28d0',
                                                                    'length': 32,
                                                                    'lsa_id': '10.2.3.3',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000010',
                                                                    'type': 2}}},
                                                        '10.2.4.4 10.64.4.4':
                                                            {'lsa_id': '10.2.4.4',
                                                            'adv_router': '10.64.4.4',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'network':
                                                                        {'attached_routers':
                                                                            {'10.100.2.2': {},
                                                                            '10.64.4.4': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header':
                                                                    {'adv_router': '10.64.4.4',
                                                                    'age': 724,
                                                                    'checksum': '0x07e7',
                                                                    'length': 32,
                                                                    'lsa_id': '10.2.4.4',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000010',
                                                                    'type': 2}}},
                                                        '10.3.4.4 10.64.4.4':
                                                            {'lsa_id': '10.3.4.4',
                                                            'adv_router': '10.64.4.4',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'network':
                                                                        {'attached_routers':
                                                                            {'10.36.3.3': {},
                                                                            '10.64.4.4': {}},
                                                                        'network_mask': '255.255.255.0'}},
                                                                'header':
                                                                    {'adv_router': '10.64.4.4',
                                                                    'age': 987,
                                                                    'checksum': '0xeedb',
                                                                    'length': 32,
                                                                    'lsa_id': '10.3.4.4',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x8000002f',
                                                                    'type': 2}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf database network detail vrf all
        OSPF Router with ID (10.100.2.2) (Process ID 1 VRF default)

                Network Link States (Area 0.0.0.0)

        LS age: 772
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.1.2.1 (Designated Router address)
        Advertising Router: 10.4.1.1
        LS Seq Number: 0x80000010
        Checksum: 0x3bd1
        Length: 32
        Network Mask: /24
             Attached Router: 10.4.1.1
             Attached Router: 10.100.2.2

        LS age: 1482
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.1.4.4 (Designated Router address)
        Advertising Router: 10.64.4.4
        LS Seq Number: 0x8000002f
        Checksum: 0xa232
        Length: 32
        Network Mask: /24
             Attached Router: 10.64.4.4
             Attached Router: 10.4.1.1

        LS age: 788
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.2.3.3 (Designated Router address)
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000010
        Checksum: 0x28d0
        Length: 32
        Network Mask: /24
             Attached Router: 10.100.2.2
             Attached Router: 10.36.3.3

        LS age: 724
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.2.4.4 (Designated Router address)
        Advertising Router: 10.64.4.4
        LS Seq Number: 0x80000010
        Checksum: 0x07e7
        Length: 32
        Network Mask: /24
             Attached Router: 10.64.4.4
             Attached Router: 10.100.2.2

        LS age: 987
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.3.4.4 (Designated Router address)
        Advertising Router: 10.64.4.4
        LS Seq Number: 0x8000002f
        Checksum: 0xeedb
        Length: 32
        Network Mask: /24
             Attached Router: 10.64.4.4
             Attached Router: 10.36.3.3


            OSPF Router with ID (10.151.22.22) (Process ID 1 VRF VRF1)

                    Network Link States (Area 0.0.0.1)

        LS age: 1454
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.186.5.1 (Designated Router address)
        Advertising Router: 10.229.11.11
        LS Seq Number: 0x80000033
        Checksum: 0xddd9
        Length: 32
        Network Mask: /24
             Attached Router: 10.229.11.11
             Attached Router: 10.115.55.55

        LS age: 1080
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.229.6.6 (Designated Router address)
        Advertising Router: 10.84.66.66
        LS Seq Number: 0x80000010
        Checksum: 0x3f5f
        Length: 32
        Network Mask: /24
             Attached Router: 10.84.66.66
             Attached Router: 10.151.22.22

        LS age: 812
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.19.7.7 (Designated Router address)
        Advertising Router: 10.1.77.77
        LS Seq Number: 0x8000002b
        Checksum: 0x5a1a
        Length: 32
        Network Mask: /24
             Attached Router: 10.1.77.77
             Attached Router: 10.36.3.3

        LS age: 573
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.115.6.6 (Designated Router address)
        Advertising Router: 10.84.66.66
        LS Seq Number: 0x8000002a
        Checksum: 0x5f9d
        Length: 32
        Network Mask: /24
             Attached Router: 10.84.66.66
             Attached Router: 10.115.55.55

        LS age: 1819
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Links
        Link State ID: 10.166.7.6 (Designated Router address)
        Advertising Router: 10.84.66.66
        LS Seq Number: 0x8000002b
        Checksum: 0x960b
        Length: 32
        Network Mask: /24
             Attached Router: 10.84.66.66
             Attached Router: 10.1.77.77
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseNetworkDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseNetworkDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================================
#  Unit test for 'show ip ospf database summary detail vrf all'
# ==============================================================
class TestShowIpOspfDatabaseSummaryDetailVrfAll(unittest.TestCase):

    '''Unit test for 'show ip ospf database summary detail vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.1':
                                        {'database':
                                            {'lsa_types':
                                                {3:
                                                    {'lsa_type': 3,
                                                    'lsas':
                                                        {'10.1.2.0 10.100.2.2':
                                                            {'lsa_id': '10.1.2.0',
                                                            'adv_router': '10.100.2.2',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 4294,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.100.2.2',
                                                                    'age': 788,
                                                                    'checksum': '0xfc54',
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.2.0',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000001',
                                                                    'type': 3}}},
                                                        '10.1.2.0 10.36.3.3':
                                                            {'lsa_id': '10.1.2.0',
                                                            'adv_router': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 151,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 632,
                                                                    'checksum': '0x5655',
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.2.0',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                   'seq_num': '0x80000002',
                                                                   'type': 3}}},
                                                        '10.1.3.0 10.36.3.3':
                                                            {'lsa_id': '10.1.3.0',
                                                            'adv_router': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 40,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 642,
                                                                    'checksum': '0xf029',
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.3.0',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                   'seq_num': '0x80000002',
                                                                   'type': 3}}},
                                                        '10.2.3.0 10.100.2.2':
                                                            {'lsa_id': '10.2.3.0',
                                                            'adv_router': '10.100.2.2',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 222,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.100.2.2',
                                                                    'age': 788,
                                                                    'checksum': '0x4601',
                                                                    'length': 28,
                                                                    'lsa_id': '10.2.3.0',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                   'seq_num': '0x80000001',
                                                                   'type': 3}}},
                                                        '10.2.3.0 10.36.3.3':
                                                            {'lsa_id': '10.2.3.0',
                                                            'adv_router': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 262,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 397,
                                                                    'checksum': '0x96a2',
                                                                    'length': 28,
                                                                    'lsa_id': '10.2.3.0',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000003',
                                                                    'type': 3}}},
                                                        '10.100.2.2 10.100.2.2':
                                                            {'lsa_id': '10.100.2.2',
                                                            'adv_router': '10.100.2.2',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 1,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.100.2.2',
                                                                    'age': 789,
                                                                    'checksum': '0xfa31',
                                                                    'length': 28,
                                                                    'lsa_id': '10.100.2.2',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000001',
                                                                    'type': 3}}},
                                                        '10.36.3.3 10.36.3.3':
                                                            {'lsa_id': '10.36.3.3',
                                                            'adv_router': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 1,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 642,
                                                                    'checksum': '0x8eb4',
                                                                    'length': 28,
                                                                    'lsa_id': '10.36.3.3',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                  'seq_num': '0x80000002',
                                                                  'type': 3}}},
                                                        '10.94.44.44 10.64.4.4':
                                                            {'lsa_id': '10.94.44.44',
                                                            'adv_router': '10.64.4.4',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 1,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.64.4.4',
                                                                    'age': 403,
                                                                    'checksum': '0x2b50',
                                                                    'length': 28,
                                                                    'lsa_id': '10.94.44.44',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000001',
                                                                    'type': 3}}}}}}}},
                                    '0.0.0.0':
                                        {'database':
                                            {'lsa_types':
                                                {3:
                                                    {'lsa_type': 3,
                                                    'lsas':
                                                        {'10.186.3.0 10.4.1.1':
                                                            {'lsa_id': '10.186.3.0',
                                                            'adv_router': '10.4.1.1',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 1,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 694,
                                                                    'checksum': '0x43dc',
                                                                    'length': 28,
                                                                    'lsa_id': '10.186.3.0',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000001',
                                                                    'type': 3}}},
                                                        '10.186.3.0 10.36.3.3':
                                                            {'lsa_id': '10.186.3.0',
                                                            'adv_router': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 40,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 642,
                                                                    'checksum': '0x6ea1',
                                                                    'length': 28,
                                                                    'lsa_id': '10.186.3.0',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 3}}},
                                                        '10.229.3.0 10.36.3.3':
                                                            {'lsa_id': '10.229.3.0',
                                                            'adv_router': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 40,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 642,
                                                                    'checksum': '0x62ac',
                                                                    'length': 28,
                                                                    'lsa_id': '10.229.3.0',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 3}}},
                                                        '10.229.4.0 10.36.3.3':
                                                            {'lsa_id': '10.229.4.0',
                                                            'adv_router': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 41,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 401,
                                                                    'checksum': '0x5dad',
                                                                    'length': 28,
                                                                    'lsa_id': '10.229.4.0',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000004',
                                                                    'type': 3}}},
                                                        '10.19.4.0 10.36.3.3':
                                                            {'lsa_id': '10.19.4.0',
                                                            'adv_router': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.0',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 40,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 642,
                                                                    'checksum': '0x4bc1',
                                                                    'length': 28,
                                                                    'lsa_id': '10.19.4.0',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 3}}},
                                                        '10.64.4.4 10.36.3.3':
                                                            {'lsa_id': '10.64.4.4',
                                                            'adv_router': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'summary':
                                                                        {'network_mask': '255.255.255.255',
                                                                        'topologies':
                                                                            {0:
                                                                                {'metric': 41,
                                                                                'mt_id': 0,
                                                                                'tos': 0}}}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 401,
                                                                    'checksum': '0xef26',
                                                                    'length': 28,
                                                                    'lsa_id': '10.64.4.4',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000003',
                                                                    'type': 3}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R3_ospf_nx# show ip ospf database summary detail vrf all
        OSPF Router with ID (10.36.3.3) (Process ID 1 VRF default)

                Summary Network Link States (Area 0.0.0.0)

        LS age: 401
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.64.4.4 (Network address)
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000003
        Checksum: 0xef26
        Length: 28
        Network Mask: /32
          TOS:   0 Metric: 41

        LS age: 694
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Summary
        Link State ID: 10.186.3.0 (Network address)
        Advertising Router: 10.4.1.1
        LS Seq Number: 0x80000001
        Checksum: 0x43dc
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 1

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.186.3.0 (Network address)
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000002
        Checksum: 0x6ea1
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 40

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.229.3.0 (Network address)
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000002
        Checksum: 0x62ac
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 40

        LS age: 401
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.229.4.0 (Network address)
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000004
        Checksum: 0x5dad
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 41

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.19.4.0 (Network address)
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000002
        Checksum: 0x4bc1
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 40


                    Summary Network Link States (Area 0.0.0.1)

        LS age: 789
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Summary
        Link State ID: 10.100.2.2 (Network address)
        Advertising Router: 10.100.2.2
        LS Seq Number: 0x80000001
        Checksum: 0xfa31
        Length: 28
        Network Mask: /32
          TOS:   0 Metric: 1

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.36.3.3 (Network address)
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000002
        Checksum: 0x8eb4
        Length: 28
        Network Mask: /32
          TOS:   0 Metric: 1

        LS age: 788
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Summary
        Link State ID: 10.1.2.0 (Network address)
        Advertising Router: 10.100.2.2
        LS Seq Number: 0x80000001
        Checksum: 0xfc54
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 4294

        LS age: 632
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.1.2.0 (Network address)
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000002
        Checksum: 0x5655
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 151

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.1.3.0 (Network address)
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000002
        Checksum: 0xf029
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 40

        LS age: 788
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Summary
        Link State ID: 10.2.3.0 (Network address)
        Advertising Router: 10.100.2.2
        LS Seq Number: 0x80000001
        Checksum: 0x4601
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 222

        LS age: 397
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Network Summary
        Link State ID: 10.2.3.0 (Network address)
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000003
        Checksum: 0x96a2
        Length: 28
        Network Mask: /24
          TOS:   0 Metric: 262

        LS age: 403
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Network Summary
        Link State ID: 10.94.44.44 (Network address)
        Advertising Router: 10.64.4.4
        LS Seq Number: 0x80000001
        Checksum: 0x2b50
        Length: 28
        Network Mask: /32
          TOS:   0 Metric: 1
        '''}

    def test_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseSummaryDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseSummaryDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ============================================================
#  Unit test for 'show ip ospf database router detail vrf all'
# ============================================================
class TestShowIpOspfDatabaseRouterDetailVrfAll(unittest.TestCase):

    '''Unit test for 'show ip ospf database router detail vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'VRF1':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.1':
                                        {'database':
                                            {'lsa_types':
                                                {1:
                                                    {'lsa_type': 1,
                                                        'lsas':
                                                            {'10.229.11.11 10.229.11.11':
                                                                {'adv_router': '10.229.11.11',
                                                                    'lsa_id': '10.229.11.11',
                                                                    'ospfv2':
                                                                        {'body':
                                                                            {'router':
                                                                                {'links':
                                                                                    {'10.186.5.1':
                                                                                        {'link_data': '10.186.5.1',
                                                                                        'link_id': '10.186.5.1',
                                                                                        'num_tos_metrics': 0,
                                                                                        'topologies':
                                                                                            {0:
                                                                                                {'metric': 1,
                                                                                                'mt_id': 0,
                                                                                                'tos': 0}},
                                                                                        'type': 'transit network'},
                                                                                    '10.151.22.22':
                                                                                        {'link_data': '0.0.0.14',
                                                                                        'link_id': '10.151.22.22',
                                                                                        'num_tos_metrics': 0,
                                                                                        'topologies':
                                                                                            {0:
                                                                                                {'metric': 111,
                                                                                                'mt_id': 0,
                                                                                                'tos': 0}},
                                                                                        'type': 'router (point-to-point)'}},
                                                                                'num_of_links': 2}},
                                                                    'header':
                                                                        {'adv_router': '10.229.11.11',
                                                                        'age': 646,
                                                                        'checksum': '0x9ae4',
                                                                        'length': 48,
                                                                        'lsa_id': '10.229.11.11',
                                                                        'option': '0x22',
                                                                        'option_desc': 'No TOS-capability, DC',
                                                                        'seq_num': '0x8000003f',
                                                                        'type': 1}}},
                                                            '10.151.22.22 10.151.22.22':
                                                                {'adv_router': '10.151.22.22',
                                                                'lsa_id': '10.151.22.22',
                                                                'ospfv2':
                                                                    {'body':
                                                                        {'router':
                                                                            {'links':
                                                                                {'10.229.11.11':
                                                                                    {'link_data': '0.0.0.6',
                                                                                    'link_id': '10.229.11.11',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 1,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'router (point-to-point)'},
                                                                                '10.229.6.6':
                                                                                    {'link_data': '10.229.6.2',
                                                                                    'link_id': '10.229.6.6',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 40,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'transit network'}},
                                                                            'num_of_links': 2}},
                                                                'header':
                                                                    {'adv_router': '10.151.22.22',
                                                                    'age': 642,
                                                                    'checksum': '0xc21b',
                                                                    'length': 48,
                                                                    'lsa_id': '10.151.22.22',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x8000001a',
                                                                    'type': 1}}},
                                                            '10.36.3.3 10.36.3.3':
                                                                {'adv_router': '10.36.3.3',
                                                                'lsa_id': '10.36.3.3',
                                                                'ospfv2':
                                                                    {'body':
                                                                        {'router':
                                                                            {'links':
                                                                                {'10.19.7.7':
                                                                                    {'link_data': '10.19.7.3',
                                                                                    'link_id': '10.19.7.7',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 1,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'transit network'}},
                                                                            'num_of_links': 1}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 1148,
                                                                    'checksum': '0x5646',
                                                                    'length': 36,
                                                                    'lsa_id': '10.36.3.3',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000036',
                                                                    'type': 1}}},
                                                            '10.115.55.55 10.115.55.55':
                                                                {'adv_router': '10.115.55.55',
                                                                'lsa_id': '10.115.55.55',
                                                                'ospfv2':
                                                                    {'body':
                                                                        {'router':
                                                                            {'links':
                                                                                {'10.186.5.1':
                                                                                    {'link_data': '10.186.5.5',
                                                                                    'link_id': '10.186.5.1',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 1,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                            'type': 'transit network'},
                                                                                '10.115.6.6':
                                                                                    {'link_data': '10.115.6.5',
                                                                                    'link_id': '10.115.6.6',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 30,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'transit network'},
                                                                                '10.115.55.55':
                                                                                    {'link_data': '255.255.255.255',
                                                                                    'link_id': '10.115.55.55',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 1,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'stub network'}},
                                                                            'num_of_links': 3}},
                                                                    'header':
                                                                        {'adv_router': '10.115.55.55',
                                                                        'age': 304,
                                                                        'checksum': '0xe5bd',
                                                                        'length': 60,
                                                                        'lsa_id': '10.115.55.55',
                                                                        'option': '0x22',
                                                                        'option_desc': 'No TOS-capability, DC',
                                                                        'seq_num': '0x80000038',
                                                                        'type': 1}}},
                                                            '10.84.66.66 10.84.66.66':
                                                                {'adv_router': '10.84.66.66',
                                                                'lsa_id': '10.84.66.66',
                                                                'ospfv2':
                                                                    {'body':
                                                                        {'router':
                                                                            {'links':
                                                                                {'10.229.6.6':
                                                                                    {'link_data': '10.229.6.6',
                                                                                    'link_id': '10.229.6.6',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 1,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                            'type': 'transit network'},
                                                                                '10.115.6.6':
                                                                                    {'link_data': '10.115.6.6',
                                                                                    'link_id': '10.115.6.6',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 30,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'transit network'},
                                                                                '10.166.7.6':
                                                                                    {'link_data': '10.166.7.6',
                                                                                    'link_id': '10.166.7.6',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 30,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'transit network'},
                                                                                '10.84.66.66':
                                                                                    {'link_data': '255.255.255.255',
                                                                                    'link_id': '10.84.66.66',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 1,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'stub network'}},
                                                                            'num_of_links': 4}},
                                                                    'header':
                                                                        {'adv_router': '10.84.66.66',
                                                                        'age': 524,
                                                                        'checksum': '0x1083',
                                                                        'length': 72,
                                                                        'lsa_id': '10.84.66.66',
                                                                        'option': '0x22',
                                                                        'option_desc': 'No TOS-capability, DC',
                                                                        'seq_num': '0x8000003d',
                                                                        'type': 1}}},
                                                            '10.1.77.77 10.1.77.77':
                                                                {'adv_router': '10.1.77.77',
                                                                'lsa_id': '10.1.77.77',
                                                                'ospfv2':
                                                                    {'body':
                                                                        {'router':
                                                                            {'links':
                                                                                {'10.19.7.7':
                                                                                    {'link_data': '10.19.7.7',
                                                                                    'link_id': '10.19.7.7',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 1,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'transit network'},
                                                                                '10.166.7.6':
                                                                                    {'link_data': '10.166.7.7',
                                                                                    'link_id': '10.166.7.6',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 30,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'transit network'},
                                                                                '10.1.77.77':
                                                                                    {'link_data': '255.255.255.255',
                                                                                    'link_id': '10.1.77.77',
                                                                                    'num_tos_metrics': 0,
                                                                                    'topologies':
                                                                                        {0:
                                                                                            {'metric': 1,
                                                                                            'mt_id': 0,
                                                                                            'tos': 0}},
                                                                                    'type': 'stub network'}},
                                                                            'num_of_links': 3}},
                                                                    'header':
                                                                        {'adv_router': '10.1.77.77',
                                                                        'age': 237,
                                                                        'checksum': '0x117a',
                                                                        'length': 60,
                                                                        'lsa_id': '10.1.77.77',
                                                                        'option': '0x22',
                                                                        'option_desc': 'No TOS-capability, DC',
                                                                        'seq_num': '0x80000031',
                                                                        'type': 1}}}}}}}}}}}}}},
            'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.0':
                                        {'database':
                                            {'lsa_types':
                                                {1:
                                                    {'lsa_type': 1,
                                                    'lsas':
                                                        {'10.4.1.1 10.4.1.1':
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.4.1.1',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'router':
                                                                        {'links':
                                                                            {'10.4.1.1':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.4.1.1',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'},
                                                                            '10.1.2.1':
                                                                                {'link_data': '10.1.2.1',
                                                                                'link_id': '10.1.2.1',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'},
                                                                            '10.1.4.4':
                                                                                {'link_data': '10.1.4.1',
                                                                                'link_id': '10.1.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'transit network'}},
                                                                        'num_of_links': 3}},
                                                                'header':
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 723,
                                                                    'checksum': '0x6029',
                                                                    'length': 60,
                                                                    'lsa_id': '10.4.1.1',
                                                                    'option': '0x22',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x8000003e',
                                                                    'type': 1}}},
                                                        '10.100.2.2 10.100.2.2':
                                                            {'adv_router': '10.100.2.2',
                                                            'lsa_id': '10.100.2.2',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'router':
                                                                        {'links':
                                                                            {'10.1.2.1':
                                                                                {'link_data': '10.1.2.2',
                                                                                'link_id': '10.1.2.1',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                        'type': 'transit network'},
                                                                            '10.2.3.3':
                                                                                {'link_data': '10.2.3.2',
                                                                                'link_id': '10.2.3.3',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                        'type': 'transit network'},
                                                                            '10.2.4.4':
                                                                                {'link_data': '10.2.4.2',
                                                                                'link_id': '10.2.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                        'type': 'transit network'},
                                                                            '10.100.2.2':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.100.2.2',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                    'type': 'stub network'}},
                                                                        'num_of_links': 4}},
                                                            'header':
                                                                {'adv_router': '10.100.2.2',
                                                                'age': 1683,
                                                                'checksum': '0x652b',
                                                                'length': 72,
                                                                'lsa_id': '10.100.2.2',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000014',
                                                                'type': 1}}},
                                                        '10.36.3.3 10.36.3.3':
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.36.3.3',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'router':
                                                                        {'links':
                                                                            {'10.2.3.3':
                                                                                {'link_data': '10.2.3.3',
                                                                                'link_id': '10.2.3.3',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                        'type': 'transit network'},
                                                                            '10.3.4.4':
                                                                                {'link_data': '10.3.4.3',
                                                                                'link_id': '10.3.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                        'type': 'transit network'},
                                                                            '10.36.3.3':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.36.3.3',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                        'type': 'stub network'}},
                                                                        'num_of_links': 3}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 217,
                                                                'checksum': '0x73f9',
                                                                'length': 60,
                                                                'lsa_id': '10.36.3.3',
                                                                'option': '0x22',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000034',
                                                                'type': 1}}},
                                                        '10.64.4.4 10.64.4.4':
                                                            {'adv_router': '10.64.4.4',
                                                            'lsa_id': '10.64.4.4',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'router':
                                                                        {'links':
                                                                            {'10.1.4.4':
                                                                                {'link_data': '10.1.4.4',
                                                                                'link_id': '10.1.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                        'type': 'transit '
                                                                                        'network'},
                                                                            '10.2.4.4':
                                                                                {'link_data': '10.2.4.4',
                                                                                'link_id': '10.2.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                        'type': 'transit '
                                                                                        'network'},
                                                                            '10.3.4.4':
                                                                                {'link_data': '10.3.4.4',
                                                                                'link_id': '10.3.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                        'type': 'transit '
                                                                                        'network'},
                                                                            '10.64.4.4':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.64.4.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                        'type': 'stub '
                                                                                        'network'}},
                                                                        'num_of_links': 4}},
                                                            'header':
                                                                {'adv_router': '10.64.4.4',
                                                                'age': 1433,
                                                                'checksum': '0xa37d',
                                                                'length': 72,
                                                                'lsa_id': '10.64.4.4',
                                                                'option': '0x22',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000037',
                                                                'type': 1}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf database router detail vrf all
        OSPF Router with ID (10.100.2.2) (Process ID 1 VRF default)

                Router Link States (Area 0.0.0.0)

        LS age: 723
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 10.4.1.1
        Advertising Router: 10.4.1.1
        LS Seq Number: 0x8000003e
        Checksum: 0x6029
        Length: 60
        Number of links: 3

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.4.1.1
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.1.2.1
          (Link Data) Router Interface address: 10.1.2.1
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.1.4.4
          (Link Data) Router Interface address: 10.1.4.1
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 1683
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Router Links
        Link State ID: 10.100.2.2
        Advertising Router: 10.100.2.2
        LS Seq Number: 0x80000014
        Checksum: 0x652b
        Length: 72
        Number of links: 4

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.100.2.2
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.2.3.3
          (Link Data) Router Interface address: 10.2.3.2
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.2.4.4
          (Link Data) Router Interface address: 10.2.4.2
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.1.2.1
          (Link Data) Router Interface address: 10.1.2.2
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 217
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 10.36.3.3
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000034
        Checksum: 0x73f9
        Length: 60
        Number of links: 3

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.36.3.3
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.3.4.4
          (Link Data) Router Interface address: 10.3.4.3
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.2.3.3
          (Link Data) Router Interface address: 10.2.3.3
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 1433
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 10.64.4.4
        Advertising Router: 10.64.4.4
        LS Seq Number: 0x80000037
        Checksum: 0xa37d
        Length: 72
        AS border router
        Number of links: 4

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.64.4.4
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.2.4.4
          (Link Data) Router Interface address: 10.2.4.4
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.3.4.4
          (Link Data) Router Interface address: 10.3.4.4
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.1.4.4
          (Link Data) Router Interface address: 10.1.4.4
           Number of TOS metrics: 0
             TOS   0 Metric: 1


            OSPF Router with ID (10.151.22.22) (Process ID 1 VRF VRF1)

                    Router Link States (Area 0.0.0.1)

        LS age: 1148
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 10.36.3.3
        Advertising Router: 10.36.3.3
        LS Seq Number: 0x80000036
        Checksum: 0x5646
        Length: 36
        Area border router
        AS border router
        Number of links: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.19.7.7
          (Link Data) Router Interface address: 10.19.7.3
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 646
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 10.229.11.11
        Advertising Router: 10.229.11.11
        LS Seq Number: 0x8000003f
        Checksum: 0x9ae4
        Length: 48
        Area border router
        AS border router
        Number of links: 2

         Link connected to: a Router (point-to-point)
         (Link ID) Neighboring Router ID: 10.151.22.22
         (Link Data) Router Interface address: 0.0.0.14
           Number of TOS metrics: 0
             TOS   0 Metric: 111

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.186.5.1
          (Link Data) Router Interface address: 10.186.5.1
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 642
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Router Links
        Link State ID: 10.151.22.22
        Advertising Router: 10.151.22.22
        LS Seq Number: 0x8000001a
        Checksum: 0xc21b
        Length: 48
        Area border router
        AS border router
        Number of links: 2

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.229.6.6
          (Link Data) Router Interface address: 10.229.6.2
           Number of TOS metrics: 0
             TOS   0 Metric: 40

         Link connected to: a Router (point-to-point)
         (Link ID) Neighboring Router ID: 10.229.11.11
         (Link Data) Router Interface address: 0.0.0.6
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 304
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 10.115.55.55
        Advertising Router: 10.115.55.55
        LS Seq Number: 0x80000038
        Checksum: 0xe5bd
        Length: 60
        Number of links: 3

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.115.55.55
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.115.6.6
          (Link Data) Router Interface address: 10.115.6.5
           Number of TOS metrics: 0
             TOS   0 Metric: 30

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.186.5.1
          (Link Data) Router Interface address: 10.186.5.5
           Number of TOS metrics: 0
             TOS   0 Metric: 1

        LS age: 524
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 10.84.66.66
        Advertising Router: 10.84.66.66
        LS Seq Number: 0x8000003d
        Checksum: 0x1083
        Length: 72
        Number of links: 4

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.84.66.66
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.166.7.6
          (Link Data) Router Interface address: 10.166.7.6
           Number of TOS metrics: 0
             TOS   0 Metric: 30

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.229.6.6
          (Link Data) Router Interface address: 10.229.6.6
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.115.6.6
          (Link Data) Router Interface address: 10.115.6.6
           Number of TOS metrics: 0
             TOS   0 Metric: 30

        LS age: 237
        Options: 0x22 (No TOS-capability, DC)
        LS Type: Router Links
        Link State ID: 10.1.77.77
        Advertising Router: 10.1.77.77
        LS Seq Number: 0x80000031
        Checksum: 0x117a
        Length: 60
        Number of links: 3

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.1.77.77
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.166.7.6
          (Link Data) Router Interface address: 10.166.7.7
           Number of TOS metrics: 0
             TOS   0 Metric: 30

         Link connected to: a Transit Network
          (Link ID) Designated Router address: 10.19.7.7
          (Link Data) Router Interface address: 10.19.7.7
           Number of TOS metrics: 0
             TOS   0 Metric: 1
        '''}

    golden_parsed_output2 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'UNDERLAY':
                                {'areas':
                                    {'0.0.0.0':
                                        {'database':
                                            {'lsa_types':
                                                {1:
                                                    {'lsa_type': 1,
                                                    'lsas':
                                                        {'10.186.0.1 10.186.0.1':
                                                            {'adv_router': '10.186.0.1',
                                                            'lsa_id': '10.186.0.1',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'router':
                                                                        {'links':
                                                                            {'10.55.1.1':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.55.1.1',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'},
                                                                            '10.51.0.1':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.51.0.1',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'},
                                                                            '10.186.0.1':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.186.0.1',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'},
                                                                            '10.186.0.2':
                                                                                {'link_data': '10.186.1.1',
                                                                                'link_id': '10.186.0.2',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 40,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'router (point-to-point)'},
                                                                            '10.186.0.3':
                                                                                {'link_data': '0.0.0.5',
                                                                                'link_id': '10.186.0.3',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 4,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'router (point-to-point)'},
                                                                            '10.186.0.4':
                                                                                {'link_data': '0.0.0.4',
                                                                                'link_id': '10.186.0.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 4,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'router (point-to-point)'},
                                                                            '10.186.1.0':
                                                                                {'link_data': '255.255.255.0',
                                                                                'link_id': '10.186.1.0',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 40,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 7}},
                                                                'header':
                                                                    {'adv_router': '10.186.0.1',
                                                                    'age': 29,
                                                                    'checksum': '0x5cf6',
                                                                    'length': 108,
                                                                    'lsa_id': '10.186.0.1',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000905',
                                                                    'type': 1}}}}}}}}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        show ip ospf database router detail vrf all
            OSPF Router with ID (10.186.0.1) (Process ID UNDERLAY VRF default)

                    Router Link States (Area 0.0.0.0)

        LS age: 29
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Router Links
        Link State ID: 10.186.0.1
        Advertising Router: 10.186.0.1
        LS Seq Number: 0x80000905
        Checksum: 0x5cf6
        Length: 108
        Number of links: 7

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.186.0.1
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.51.0.1
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.55.1.1
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Router (point-to-point)
         (Link ID) Neighboring Router ID: 10.186.0.2
         (Link Data) Router Interface address: 10.186.1.1
           Number of TOS metrics: 0
             TOS   0 Metric: 40

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.186.1.0
          (Link Data) Network Mask: 255.255.255.0
           Number of TOS metrics: 0
             TOS   0 Metric: 40

         Link connected to: a Router (point-to-point)
         (Link ID) Neighboring Router ID: 10.186.0.4
         (Link Data) Router Interface address: 0.0.0.4
           Number of TOS metrics: 0
             TOS   0 Metric: 4

         Link connected to: a Router (point-to-point)
         (Link ID) Neighboring Router ID: 10.186.0.3
         (Link Data) Router Interface address: 0.0.0.5
           Number of TOS metrics: 0
             TOS   0 Metric: 4
        '''}

    golden_parsed_output3 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'UNDERLAY':
                                {'areas':
                                    {'0.0.0.0':
                                        {'database':
                                            {'lsa_types':
                                                {1:
                                                    {'lsa_type': 1,
                                                    'lsas':
                                                        {'10.186.0.1 10.186.0.1':
                                                            {'adv_router': '10.186.0.1',
                                                            'lsa_id': '10.186.0.1',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'router':
                                                                        {'links':
                                                                            {'10.55.1.1':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.55.1.1',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'},
                                                                            '10.51.0.1':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.51.0.1',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'},
                                                                            '10.186.0.1':
                                                                                {'link_data': '255.255.255.255',
                                                                                'link_id': '10.186.0.1',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 1,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'},
                                                                            '10.186.0.2':
                                                                                {'link_data': '10.186.1.1',
                                                                                'link_id': '10.186.0.2',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 40,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'router (point-to-point)'},
                                                                            '10.186.0.3':
                                                                                {'link_data': '0.0.0.2',
                                                                                'link_id': '10.186.0.3',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 4,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'router (point-to-point)'},
                                                                            '10.186.0.4':
                                                                                {'link_data': '0.0.0.3',
                                                                                'link_id': '10.186.0.4',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 4,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'router (point-to-point)'},
                                                                            '10.186.1.0':
                                                                                {'link_data': '255.255.255.0',
                                                                                'link_id': '10.186.1.0',
                                                                                'num_tos_metrics': 0,
                                                                                'topologies':
                                                                                    {0:
                                                                                        {'metric': 40,
                                                                                        'mt_id': 0,
                                                                                        'tos': 0}},
                                                                                'type': 'stub network'}},
                                                                        'num_of_links': 7}},
                                                                'header':
                                                                    {'adv_router': '10.186.0.1',
                                                                    'age': 587,
                                                                    'checksum': '0x0155',
                                                                    'length': 108,
                                                                    'lsa_id': '10.186.0.1',
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000906',
                                                                    'type': 1}}}}}}}}}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        show ip ospf database router detail vrf all
            OSPF Router with ID (10.186.0.1) (Process ID UNDERLAY VRF default)

                    Router Link States (Area 0.0.0.0)

        LS age: 587
        Options: 0x2 (No TOS-capability, No DC)
        LS Type: Router Links
        Link State ID: 10.186.0.1
        Advertising Router: 10.186.0.1
        LS Seq Number: 0x80000906
        Checksum: 0x0155
        Length: 108
        Number of links: 7

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.186.0.1
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Router (point-to-point)
         (Link ID) Neighboring Router ID: 10.186.0.3
         (Link Data) Router Interface address: 0.0.0.2
           Number of TOS metrics: 0
             TOS   0 Metric: 4

         Link connected to: a Router (point-to-point)
         (Link ID) Neighboring Router ID: 10.186.0.4
         (Link Data) Router Interface address: 0.0.0.3
           Number of TOS metrics: 0
             TOS   0 Metric: 4

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.51.0.1
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.55.1.1
          (Link Data) Network Mask: 255.255.255.255
           Number of TOS metrics: 0
             TOS   0 Metric: 1

         Link connected to: a Router (point-to-point)
         (Link ID) Neighboring Router ID: 10.186.0.2
         (Link Data) Router Interface address: 10.186.1.1
           Number of TOS metrics: 0
             TOS   0 Metric: 40

         Link connected to: a Stub Network
          (Link ID) Network/Subnet Number: 10.186.1.0
          (Link Data) Network Mask: 255.255.255.0
           Number of TOS metrics: 0
             TOS   0 Metric: 40
        '''}

    def test_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseRouterDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfDatabaseRouterDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowIpOspfDatabaseRouterDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseRouterDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# =================================================================
#  Unit test for 'show ip ospf database opaque-area detail vrf all'
# =================================================================
class TestShowIpOspfDatabaseOpaqueAreaDetailVrfAll(unittest.TestCase):

    '''Unit test for 'show ip ospf database opaque-area detail vrf all' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.0':
                                        {'database':
                                            {'lsa_types':
                                                {10:
                                                    {'lsa_type': 10,
                                                    'lsas':
                                                        {'10.1.0.0 10.4.1.1':
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque': {}},
                                                                'header':
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 385,
                                                                    'checksum': '0x54d3',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.0.0',
                                                                    'mpls_te_router_id': '10.4.1.1',
                                                                    'num_links': 0,
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': '0x20',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000003',
                                                                    'type': 10}}},
                                                        '10.1.0.0 10.100.2.2':
                                                            {'adv_router': '10.100.2.2',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque': {}},
                                                            'header':
                                                                {'adv_router': '10.100.2.2',
                                                                'age': 1612,
                                                                'checksum': '0x1c22',
                                                                'fragment_number': 0,
                                                                'length': 28,
                                                                'lsa_id': '10.1.0.0',
                                                                'mpls_te_router_id': '10.100.2.2',
                                                                'num_links': 0,
                                                                'opaque_id': 0,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000003',
                                                                'type': 10}}},
                                                        '10.1.0.0 10.36.3.3':
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque': {}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 113,
                                                                'checksum': '0x5cbb',
                                                                'fragment_number': 0,
                                                                'length': 28,
                                                                'lsa_id': '10.1.0.0',
                                                                'mpls_te_router_id': '10.36.3.3',
                                                                'num_links': 0,
                                                                'opaque_id': 0,
                                                                'opaque_type': 1,
                                                                'option': '0x20',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000003',
                                                                'type': 10}}},
                                                        '10.1.0.1 10.4.1.1':
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.0.1',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '10.1.4.4',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'10.1.4.1': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unknown_tlvs':
                                                                                    {1:
                                                                                        {'length': 4,
                                                                                        'type': 32770,
                                                                                        'value': '00 00 00 01'}},
                                                                                'unreserved_bandwidths':
                                                                                    {'0 93750000':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}}}},
                                                                'header':
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 385,
                                                                    'checksum': '0x6387',
                                                                    'fragment_number': 1,
                                                                    'length': 124,
                                                                    'lsa_id': '10.1.0.1',
                                                                    'num_links': 1,
                                                                    'opaque_id': 1,
                                                                    'opaque_type': 1,
                                                                    'option': '0x20',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000003',
                                                                    'type': 10}}},
                                                        '10.1.0.2 10.4.1.1':
                                                            {'adv_router': '10.4.1.1',
                                                            'lsa_id': '10.1.0.2',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '10.1.2.1',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs': {'10.1.2.1': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unknown_tlvs':
                                                                                    {1:
                                                                                        {'length': 4,
                                                                                        'type': 32770,
                                                                                        'value': '00 00 00 01'}},
                                                                                'unreserved_bandwidths':
                                                                                    {'0 93750000':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}}}},
                                                                'header':
                                                                    {'adv_router': '10.4.1.1',
                                                                    'age': 385,
                                                                    'checksum': '0xb23e',
                                                                    'fragment_number': 2,
                                                                    'length': 124,
                                                                    'lsa_id': '10.1.0.2',
                                                                    'num_links': 1,
                                                                    'opaque_id': 2,
                                                                    'opaque_type': 1,
                                                                    'option': '0x20',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000003',
                                                                    'type': 10}}},
                                                        '10.1.0.37 10.100.2.2':
                                                            {'adv_router': '10.100.2.2',
                                                            'lsa_id': '10.1.0.37',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '10.2.3.3',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'10.2.3.2': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unreserved_bandwidths':
                                                                                    {'0 93750000':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}}}},
                                                                'header':
                                                                    {'adv_router': '10.100.2.2',
                                                                    'age': 1202,
                                                                    'checksum': '0xe492',
                                                                    'fragment_number': 37,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.37',
                                                                    'num_links': 1,
                                                                    'opaque_id': 37,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000004',
                                                                    'type': 10}}},
                                                        '10.1.0.38 10.100.2.2':
                                                            {'adv_router': '10.100.2.2',
                                                            'lsa_id': '10.1.0.38',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '10.2.4.4',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'10.2.4.2': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unreserved_bandwidths':
                                                                                    {'0 93750000':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}}}},
                                                                'header':
                                                                    {'adv_router': '10.100.2.2',
                                                                    'age': 1191,
                                                                    'checksum': '0x2350',
                                                                    'fragment_number': 38,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.38',
                                                                    'num_links': 1,
                                                                    'opaque_id': 38,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000004',
                                                                    'type': 10}}},
                                                        '10.1.0.39 10.100.2.2':
                                                            {'adv_router': '10.100.2.2',
                                                            'lsa_id': '10.1.0.39',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '10.1.2.1',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'10.1.2.2': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unreserved_bandwidths':
                                                                                    {'0 93750000':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}}}},
                                                                'header':
                                                                    {'adv_router': '10.100.2.2',
                                                                    'age': 1191,
                                                                    'checksum': '0x4239',
                                                                    'fragment_number': 39,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.39',
                                                                    'num_links': 1,
                                                                    'opaque_id': 39,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000004',
                                                                    'type': 10}}},
                                                        '10.1.0.4 10.36.3.3':
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.1.0.4',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '10.3.4.4',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'10.3.4.3': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unknown_tlvs':
                                                                                    {1:
                                                                                        {'length': 4,
                                                                                        'type': 32770,
                                                                                        'value': '00 00 00 01'},
                                                                                    2: {'length': 32,
                                                                                        'type': 32771,
                                                                                        'value': '00 00 00 00 00 0 0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'}},
                                                                                'unreserved_bandwidths':
                                                                                    {'0 93750000':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}}}},
                                                                'header':
                                                                    {'adv_router': '10.36.3.3',
                                                                    'age': 113,
                                                                    'checksum': '0x8f5e',
                                                                    'fragment_number': 4,
                                                                    'length': 160,
                                                                    'lsa_id': '10.1.0.4',
                                                                    'num_links': 1,
                                                                    'opaque_id': 4,
                                                                    'opaque_type': 1,
                                                                    'option': '0x20',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'seq_num': '0x80000003',
                                                                    'type': 10}}},
                                                        '10.1.0.6 10.36.3.3':
                                                            {'adv_router': '10.36.3.3',
                                                            'lsa_id': '10.1.0.6',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '10.2.3.3',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'10.2.3.3': {}},
                                                                                'max_bandwidth': 125000000,
                                                                                'max_reservable_bandwidth': 93750000,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unknown_tlvs':
                                                                                    {1:
                                                                                        {'length': 4,
                                                                                        'type': 32770,
                                                                                        'value': '00 00 00 01'},
                                                                                    2: {'length': 32,
                                                                                        'type': 32771,
                                                                                        'value': '00 00 00 00 00 0 0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'}},
                                                                                'unreserved_bandwidths':
                                                                                    {'0 93750000':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '1 93750000':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '2 93750000':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '3 93750000':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '4 93750000':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '5 93750000':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '6 93750000':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 93750000},
                                                                                    '7 93750000':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 93750000}}}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 113,
                                                                'checksum': '0x03ed',
                                                                'fragment_number': 6,
                                                                'length': 160,
                                                                'lsa_id': '10.1.0.6',
                                                                'num_links': 1,
                                                                'opaque_id': 6,
                                                                'opaque_type': 1,
                                                                'option': '0x20',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000003',
                                                                'type': 10}}}}}}}}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R2_ospf_nx# show ip ospf database opaque-area detail vrf all
        OSPF Router with ID (10.100.2.2) (Process ID 1 VRF default)

                Opaque Area Link States (Area 0.0.0.0)

       LS age: 385
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 10.1.0.0
       Opaque Type: 1
       Opaque ID: 0
       Advertising Router: 10.4.1.1
       LS Seq Number: 0x80000003
       Checksum: 0x54d3
       Length: 28
       Fragment number: 0

         MPLS TE router ID : 10.4.1.1

         Number of Links : 0

       LS age: 1612
       Options: 0x2 (No TOS-capability, No DC)
       LS Type: Opaque Area Link
       Link State ID: 10.1.0.0
       Opaque Type: 1
       Opaque ID: 0
       Advertising Router: 10.100.2.2
       LS Seq Number: 0x80000003
       Checksum: 0x1c22
       Length: 28
       Fragment number: 0

         MPLS TE router ID : 10.100.2.2

         Number of Links : 0

       LS age: 113
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 10.1.0.0
       Opaque Type: 1
       Opaque ID: 0
       Advertising Router: 10.36.3.3
       LS Seq Number: 0x80000003
       Checksum: 0x5cbb
       Length: 28
       Fragment number: 0

         MPLS TE router ID : 10.36.3.3

         Number of Links : 0

       LS age: 385
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 10.1.0.1
       Opaque Type: 1
       Opaque ID: 1
       Advertising Router: 10.4.1.1
       LS Seq Number: 0x80000003
       Checksum: 0x6387
       Length: 124
       Fragment number: 1

         Link connected to Broadcast network
         Link ID : 10.1.4.4
         Interface Address : 10.1.4.1
         Admin Metric : 1
         Maximum Bandwidth : 125000000
         Maximum reservable bandwidth : 93750000
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000
           Priority 2 : 93750000    Priority 3 : 93750000
           Priority 4 : 93750000    Priority 5 : 93750000
           Priority 6 : 93750000    Priority 7 : 93750000
         Affinity Bit : 0x0
          Unknown Sub-TLV      :  Type = 32770, Length = 4 Value = 00 00 00 01

         Number of Links : 1

       LS age: 385
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 10.1.0.2
       Opaque Type: 1
       Opaque ID: 2
       Advertising Router: 10.4.1.1
       LS Seq Number: 0x80000003
       Checksum: 0xb23e
       Length: 124
       Fragment number: 2

         Link connected to Broadcast network
         Link ID : 10.1.2.1
         Interface Address : 10.1.2.1
         Admin Metric : 1
         Maximum Bandwidth : 125000000
         Maximum reservable bandwidth : 93750000
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000
           Priority 2 : 93750000    Priority 3 : 93750000
           Priority 4 : 93750000    Priority 5 : 93750000
           Priority 6 : 93750000    Priority 7 : 93750000
         Affinity Bit : 0x0
          Unknown Sub-TLV      :  Type = 32770, Length = 4 Value = 00 00 00 01

         Number of Links : 1

       LS age: 113
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 10.1.0.4
       Opaque Type: 1
       Opaque ID: 4
       Advertising Router: 10.36.3.3
       LS Seq Number: 0x80000003
       Checksum: 0x8f5e
       Length: 160
       Fragment number: 4

         Link connected to Broadcast network
         Link ID : 10.3.4.4
         Interface Address : 10.3.4.3
         Admin Metric : 1
         Maximum Bandwidth : 125000000
         Maximum reservable bandwidth : 93750000
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000
           Priority 2 : 93750000    Priority 3 : 93750000
           Priority 4 : 93750000    Priority 5 : 93750000
           Priority 6 : 93750000    Priority 7 : 93750000
         Affinity Bit : 0x0
          Unknown Sub-TLV      :  Type = 32770, Length = 4 Value = 00 00 00 01
          Unknown Sub-TLV      :  Type = 32771, Length = 32 Value = 00 00 00 00 00 0
           0 00 00 00 00 00 00 00 00 00 00 00 00 00 00
           00 00 00 00 00 00 00 00 00 00 00 00

         Number of Links : 1

       LS age: 113
       Options: 0x20 (No TOS-capability, DC)
       LS Type: Opaque Area Link
       Link State ID: 10.1.0.6
       Opaque Type: 1
       Opaque ID: 6
       Advertising Router: 10.36.3.3
       LS Seq Number: 0x80000003
       Checksum: 0x03ed
       Length: 160
       Fragment number: 6

         Link connected to Broadcast network
         Link ID : 10.2.3.3
         Interface Address : 10.2.3.3
         Admin Metric : 1
         Maximum Bandwidth : 125000000
         Maximum reservable bandwidth : 93750000
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000
           Priority 2 : 93750000    Priority 3 : 93750000
           Priority 4 : 93750000    Priority 5 : 93750000
           Priority 6 : 93750000    Priority 7 : 93750000
         Affinity Bit : 0x0
          Unknown Sub-TLV      :  Type = 32770, Length = 4 Value = 00 00 00 01
          Unknown Sub-TLV      :  Type = 32771, Length = 32 Value = 00 00 00 00 00 0
           0 00 00 00 00 00 00 00 00 00 00 00 00 00 00
           00 00 00 00 00 00 00 00 00 00 00 00

         Number of Links : 1

       LS age: 1202
       Options: 0x2 (No TOS-capability, No DC)
       LS Type: Opaque Area Link
       Link State ID: 10.1.0.37
       Opaque Type: 1
       Opaque ID: 37
       Advertising Router: 10.100.2.2
       LS Seq Number: 0x80000004
       Checksum: 0xe492
       Length: 116
       Fragment number: 37

         Link connected to Broadcast network
         Link ID : 10.2.3.3
         Interface Address : 10.2.3.2
         Admin Metric : 1
         Maximum Bandwidth : 125000000
         Maximum reservable bandwidth : 93750000
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000
           Priority 2 : 93750000    Priority 3 : 93750000
           Priority 4 : 93750000    Priority 5 : 93750000
           Priority 6 : 93750000    Priority 7 : 93750000
         Affinity Bit : 0x0

         Number of Links : 1

       LS age: 1191
       Options: 0x2 (No TOS-capability, No DC)
       LS Type: Opaque Area Link
       Link State ID: 10.1.0.38
       Opaque Type: 1
       Opaque ID: 38
       Advertising Router: 10.100.2.2
       LS Seq Number: 0x80000004
       Checksum: 0x2350
       Length: 116
       Fragment number: 38

         Link connected to Broadcast network
         Link ID : 10.2.4.4
         Interface Address : 10.2.4.2
         Admin Metric : 1
         Maximum Bandwidth : 125000000
         Maximum reservable bandwidth : 93750000
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000
           Priority 2 : 93750000    Priority 3 : 93750000
           Priority 4 : 93750000    Priority 5 : 93750000
           Priority 6 : 93750000    Priority 7 : 93750000
         Affinity Bit : 0x0

         Number of Links : 1

       LS age: 1191
       Options: 0x2 (No TOS-capability, No DC)
       LS Type: Opaque Area Link
       Link State ID: 10.1.0.39
       Opaque Type: 1
       Opaque ID: 39
       Advertising Router: 10.100.2.2
       LS Seq Number: 0x80000004
       Checksum: 0x4239
       Length: 116
       Fragment number: 39

         Link connected to Broadcast network
         Link ID : 10.1.2.1
         Interface Address : 10.1.2.2
         Admin Metric : 1
         Maximum Bandwidth : 125000000
         Maximum reservable bandwidth : 93750000
         Number of Priority : 8
           Priority 0 : 93750000    Priority 1 : 93750000
           Priority 2 : 93750000    Priority 3 : 93750000
           Priority 4 : 93750000    Priority 5 : 93750000
           Priority 6 : 93750000    Priority 7 : 93750000
         Affinity Bit : 0x0

         Number of Links : 1
        '''}

    golden_parsed_output2 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'instance':
                            {'1':
                                {'areas':
                                    {'0.0.0.0':
                                        {'database':
                                            {'lsa_types':
                                                {10:
                                                    {'lsa_type': 10,
                                                    'lsas':
                                                        {'10.1.0.0 192.168.4.1':
                                                            {'adv_router': '192.168.4.1',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque': {}},
                                                                'header':
                                                                    {'adv_router': '192.168.4.1',
                                                                    'age': 720,
                                                                    'checksum': '0x8c2b',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.0.0',
                                                                    'mpls_te_router_id': '192.168.4.1',
                                                                    'num_links': 0,
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.0 192.168.154.1':
                                                            {'adv_router': '192.168.154.1',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque': {}},
                                                                'header':
                                                                    {'adv_router': '192.168.154.1',
                                                                    'age': 720,
                                                                    'checksum': '0x8e27',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.0.0',
                                                                    'mpls_te_router_id': '192.168.154.1',
                                                                    'num_links': 0,
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.0 192.168.51.1':
                                                            {'adv_router': '192.168.51.1',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque': {}},
                                                                'header':
                                                                    {'adv_router': '192.168.51.1',
                                                                    'age': 515,
                                                                    'checksum': '0x9023',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.0.0',
                                                                    'mpls_te_router_id': '192.168.51.1',
                                                                    'num_links': 0,
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.0 192.168.205.1':
                                                            {'adv_router': '192.168.205.1',
                                                            'lsa_id': '10.1.0.0',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque': {}},
                                                                'header':
                                                                    {'adv_router': '192.168.205.1',
                                                                    'age': 497,
                                                                    'checksum': '0x921f',
                                                                    'fragment_number': 0,
                                                                    'length': 28,
                                                                    'lsa_id': '10.1.0.0',
                                                                    'mpls_te_router_id': '192.168.205.1',
                                                                    'num_links': 0,
                                                                    'opaque_id': 0,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.233 192.168.51.1':
                                                            {'adv_router': '192.168.51.1',
                                                            'lsa_id': '10.1.0.233',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '192.168.145.2',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'192.168.145.2': {}},
                                                                                'max_bandwidth': 5000000000,
                                                                                'max_reservable_bandwidth': 3749999872,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unreserved_bandwidths':
                                                                                    {'0 3749999872':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '1 3749999872':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '2 3749999872':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '3 3749999872':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '4 3749999872':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '5 3749999872':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '6 3749999872':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '7 3749999872':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 3749999872}}}}}},
                                                                'header':
                                                                    {'adv_router': '192.168.51.1',
                                                                    'age': 475,
                                                                    'checksum': '0x9a3b',
                                                                    'fragment_number': 233,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.233',
                                                                    'num_links': 1,
                                                                    'opaque_id': 233,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.237 192.168.51.1':
                                                            {'adv_router': '192.168.51.1',
                                                            'lsa_id': '10.1.0.237',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '192.168.81.2',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'192.168.81.1': {}},
                                                                                'max_bandwidth': 5000000000,
                                                                                'max_reservable_bandwidth': 3749999872,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unreserved_bandwidths':
                                                                                    {'0 3749999872':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '1 3749999872':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '2 3749999872':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '3 3749999872':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '4 3749999872':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '5 3749999872':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '6 3749999872':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '7 3749999872':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 3749999872}}}}}},
                                                                'header':
                                                                    {'adv_router': '192.168.51.1',
                                                                    'age': 455,
                                                                    'checksum': '0x7c40',
                                                                    'fragment_number': 237,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.237',
                                                                    'num_links': 1,
                                                                    'opaque_id': 237,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.42 192.168.154.1':
                                                            {'adv_router': '192.168.154.1',
                                                            'lsa_id': '10.1.0.42',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '192.168.196.2',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'192.168.196.2': {}},
                                                                                'max_bandwidth': 2500000000,
                                                                                'max_reservable_bandwidth': 1874999936,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 2,
                                                                                'unreserved_bandwidths':
                                                                                    {'0 1874999936':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '1 1874999936':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '2 1874999936':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '3 1874999936':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '4 1874999936':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '5 1874999936':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '6 1874999936':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '7 1874999936':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 1874999936}}}}}},
                                                                'header':
                                                                    {'adv_router': '192.168.154.1',
                                                                    'age': 510,
                                                                    'checksum': '0xcce3',
                                                                    'fragment_number': 42,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.42',
                                                                    'num_links': 1,
                                                                    'opaque_id': 42,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.47 192.168.154.1':
                                                            {'adv_router': '192.168.154.1',
                                                            'lsa_id': '10.1.0.47',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '192.168.145.2',
                                                                                'link_name': 'broadcast '
                                                                                'network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'192.168.145.1': {}},
                                                                                'max_bandwidth': 5000000000,
                                                                                'max_reservable_bandwidth': 3749999872,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unreserved_bandwidths':
                                                                                    {'0 3749999872':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '1 3749999872':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '2 3749999872':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '3 3749999872':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '4 3749999872':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '5 3749999872':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '6 3749999872':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '7 3749999872':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 3749999872}}}}}},
                                                                'header':
                                                                    {'adv_router': '192.168.154.1',
                                                                    'age': 470,
                                                                    'checksum': '0xcec3',
                                                                    'fragment_number': 47,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.47',
                                                                    'num_links': 1,
                                                                    'opaque_id': 47,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.51 192.168.154.1':
                                                            {'adv_router': '192.168.154.1',
                                                            'lsa_id': '10.1.0.51',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '192.168.106.2',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'192.168.106.1': {}},
                                                                                'max_bandwidth': 5000000000,
                                                                                'max_reservable_bandwidth': 3749999872,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unreserved_bandwidths':
                                                                                    {'0 3749999872':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '1 3749999872':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '2 3749999872':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '3 3749999872':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '4 3749999872':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '5 3749999872':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '6 3749999872':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '7 3749999872':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 3749999872}}}}}},
                                                                'header':
                                                                    {'adv_router': '192.168.154.1',
                                                                    'age': 450,
                                                                    'checksum': '0xd8b3',
                                                                    'fragment_number': 51,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.0.51',
                                                                    'num_links': 1,
                                                                    'opaque_id': 51,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}},
                                                        '10.1.0.55 192.168.4.1':
                                                            {'adv_router': '192.168.4.1',
                                                            'lsa_id': '10.1.0.55',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '192.168.196.2',
                                                                                'link_name': 'broadcast network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'192.168.196.1': {}},
                                                                                'max_bandwidth': 2500000000,
                                                                                'max_reservable_bandwidth': 1874999936,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 2,
                                                                                'unreserved_bandwidths':
                                                                                    {'0 1874999936':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '1 1874999936':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '2 1874999936':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '3 1874999936':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '4 1874999936':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '5 1874999936':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '6 1874999936':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 1874999936},
                                                                                    '7 1874999936':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 1874999936}}}}}},
                                                            'header':
                                                                {'adv_router': '192.168.4.1',
                                                                'age': 510,
                                                                'checksum': '0x3372',
                                                                'fragment_number': 55,
                                                                'length': 116,
                                                                'lsa_id': '10.1.0.55',
                                                                'num_links': 1,
                                                                'opaque_id': 55,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                        '10.1.1.11 192.168.205.1':
                                                            {'adv_router': '192.168.205.1',
                                                            'lsa_id': '10.1.1.11',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1:
                                                                                {'admin_group': '0x0',
                                                                                'link_id': '192.168.81.2',
                                                                                'link_name': 'broadcast '
                                                                                'network',
                                                                                'link_type': 2,
                                                                                'local_if_ipv4_addrs':
                                                                                    {'192.168.81.2': {}},
                                                                                'max_bandwidth': 5000000000,
                                                                                'max_reservable_bandwidth': 3749999872,
                                                                                'remote_if_ipv4_addrs':
                                                                                    {'0.0.0.0': {}},
                                                                                'te_metric': 1,
                                                                                'unreserved_bandwidths':
                                                                                    {'0 3749999872':
                                                                                        {'priority': 0,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '1 3749999872':
                                                                                        {'priority': 1,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '2 3749999872':
                                                                                        {'priority': 2,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '3 3749999872':
                                                                                        {'priority': 3,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '4 3749999872':
                                                                                        {'priority': 4,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '5 3749999872':
                                                                                        {'priority': 5,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '6 3749999872':
                                                                                        {'priority': 6,
                                                                                        'unreserved_bandwidth': 3749999872},
                                                                                    '7 3749999872':
                                                                                        {'priority': 7,
                                                                                        'unreserved_bandwidth': 3749999872}}}}}},
                                                                'header':
                                                                    {'adv_router': '192.168.205.1',
                                                                    'age': 447,
                                                                    'checksum': '0x6537',
                                                                    'fragment_number': 267,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.1.11',
                                                                    'num_links': 1,
                                                                    'opaque_id': 267,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}},
                                                        '10.1.1.15 192.168.205.1':
                                                            {'adv_router': '192.168.205.1',
                                                            'lsa_id': '10.1.1.15',
                                                            'ospfv2':
                                                                {'body':
                                                                    {'opaque':
                                                                        {'link_tlvs':
                                                                            {1: {'admin_group': '0x0',
                                                                            'link_id': '192.168.106.2',
                                                                            'link_name': 'broadcast '
                                                                            'network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'192.168.106.2': {}},
                                                                            'max_bandwidth': 5000000000,
                                                                            'max_reservable_bandwidth': 3749999872,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unreserved_bandwidths':
                                                                                {'0 3749999872':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '1 3749999872':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '2 3749999872':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '3 3749999872':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '4 3749999872':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '5 3749999872':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '6 3749999872':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '7 3749999872':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 3749999872}}}}}},
                                                                'header':
                                                                    {'adv_router': '192.168.205.1',
                                                                    'age': 457,
                                                                    'checksum': '0x4765',
                                                                    'fragment_number': 271,
                                                                    'length': 116,
                                                                    'lsa_id': '10.1.1.15',
                                                                    'num_links': 1,
                                                                    'opaque_id': 271,
                                                                    'opaque_type': 1,
                                                                    'option': '0x2',
                                                                    'option_desc': 'No TOS-capability, No DC',
                                                                    'seq_num': '0x80000002',
                                                                    'type': 10}}}}}}}}}},
                            '2': {}}}}}}}

    golden_output2 = {'execute.return_value': '''
        +++ P1: executing command 'show ip ospf database opaque-area detail vrf all' +++
        show ip ospf database opaque-area detail vrf all

                OSPF Router with ID (192.168.154.1) (Process ID 2 VRF default)

                OSPF Router with ID (192.168.154.1) (Process ID 1 VRF default)

                        Opaque Area Link States (Area 0.0.0.0)

           LS age: 720
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.0.0
           Opaque Type: 1
           Opaque ID: 0
           Advertising Router: 192.168.4.1
           LS Seq Number: 0x80000002
           Checksum: 0x8c2b
           Length: 28
           Fragment number: 0

             MPLS TE router ID : 192.168.4.1

             Number of Links : 0

           LS age: 720
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.0.0
           Opaque Type: 1
           Opaque ID: 0
           Advertising Router: 192.168.154.1
           LS Seq Number: 0x80000002
           Checksum: 0x8e27
           Length: 28
           Fragment number: 0

             MPLS TE router ID : 192.168.154.1

             Number of Links : 0

           LS age: 515
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.0.0
           Opaque Type: 1
           Opaque ID: 0
           Advertising Router: 192.168.51.1
           LS Seq Number: 0x80000002
           Checksum: 0x9023
           Length: 28
           Fragment number: 0

             MPLS TE router ID : 192.168.51.1

             Number of Links : 0

           LS age: 497
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.0.0
           Opaque Type: 1
           Opaque ID: 0
           Advertising Router: 192.168.205.1
           LS Seq Number: 0x80000002
           Checksum: 0x921f
           Length: 28
           Fragment number: 0

             MPLS TE router ID : 192.168.205.1

             Number of Links : 0

           LS age: 510
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.0.42
           Opaque Type: 1
           Opaque ID: 42
           Advertising Router: 192.168.154.1
           LS Seq Number: 0x80000002
           Checksum: 0xcce3
           Length: 116
           Fragment number: 42

             Link connected to Broadcast network
             Link-ID :   Link ID : 192.168.196.2
             Interface Address :   Interface Address : 192.168.196.2
             Admin Metric : 2
             Maximum Bandwidth : 2500000000
             Maximum reservable bandwidth : 1874999936
             Number of Priority : 8
               Priority 0 : 1874999936  Priority 1 : 1874999936
               Priority 2 : 1874999936  Priority 3 : 1874999936
               Priority 4 : 1874999936  Priority 5 : 1874999936
               Priority 6 : 1874999936  Priority 7 : 1874999936
             Affinity Bit : 0x0

             Number of Links : 1

           LS age: 470
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.0.47
           Opaque Type: 1
           Opaque ID: 47
           Advertising Router: 192.168.154.1
           LS Seq Number: 0x80000002
           Checksum: 0xcec3
           Length: 116
           Fragment number: 47

             Link connected to Broadcast network
             Link-ID :   Link ID : 192.168.145.2
             Interface Address :   Interface Address : 192.168.145.1
             Admin Metric : 1
             Maximum Bandwidth : 5000000000
             Maximum reservable bandwidth : 3749999872
             Number of Priority : 8
               Priority 0 : 3749999872  Priority 1 : 3749999872
               Priority 2 : 3749999872  Priority 3 : 3749999872
               Priority 4 : 3749999872  Priority 5 : 3749999872
               Priority 6 : 3749999872  Priority 7 : 3749999872
             Affinity Bit : 0x0

             Number of Links : 1

           LS age: 450
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.0.51
           Opaque Type: 1
           Opaque ID: 51
           Advertising Router: 192.168.154.1
           LS Seq Number: 0x80000002
           Checksum: 0xd8b3
           Length: 116
           Fragment number: 51

             Link connected to Broadcast network
             Link-ID :   Link ID : 192.168.106.2
             Interface Address :   Interface Address : 192.168.106.1
             Admin Metric : 1
             Maximum Bandwidth : 5000000000
             Maximum reservable bandwidth : 3749999872
             Number of Priority : 8
               Priority 0 : 3749999872  Priority 1 : 3749999872
               Priority 2 : 3749999872  Priority 3 : 3749999872
               Priority 4 : 3749999872  Priority 5 : 3749999872
               Priority 6 : 3749999872  Priority 7 : 3749999872
             Affinity Bit : 0x0

             Number of Links : 1

           LS age: 510
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.0.55
           Opaque Type: 1
           Opaque ID: 55
           Advertising Router: 192.168.4.1
           LS Seq Number: 0x80000002
           Checksum: 0x3372
           Length: 116
           Fragment number: 55

             Link connected to Broadcast network
             Link-ID :   Link ID : 192.168.196.2
             Interface Address :   Interface Address : 192.168.196.1
             Admin Metric : 2
             Maximum Bandwidth : 2500000000
             Maximum reservable bandwidth : 1874999936
             Number of Priority : 8
               Priority 0 : 1874999936  Priority 1 : 1874999936
               Priority 2 : 1874999936  Priority 3 : 1874999936
               Priority 4 : 1874999936  Priority 5 : 1874999936
               Priority 6 : 1874999936  Priority 7 : 1874999936
             Affinity Bit : 0x0

             Number of Links : 1

           LS age: 475
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.0.233
           Opaque Type: 1
           Opaque ID: 233
           Advertising Router: 192.168.51.1
           LS Seq Number: 0x80000002
           Checksum: 0x9a3b
           Length: 116
           Fragment number: 233

             Link connected to Broadcast network
             Link-ID :   Link ID : 192.168.145.2
             Interface Address :   Interface Address : 192.168.145.2
             Admin Metric : 1
             Maximum Bandwidth : 5000000000
             Maximum reservable bandwidth : 3749999872
             Number of Priority : 8
               Priority 0 : 3749999872  Priority 1 : 3749999872
               Priority 2 : 3749999872  Priority 3 : 3749999872
               Priority 4 : 3749999872  Priority 5 : 3749999872
               Priority 6 : 3749999872  Priority 7 : 3749999872
             Affinity Bit : 0x0

             Number of Links : 1

           LS age: 455
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.0.237
           Opaque Type: 1
           Opaque ID: 237
           Advertising Router: 192.168.51.1
           LS Seq Number: 0x80000002
           Checksum: 0x7c40
           Length: 116
           Fragment number: 237

             Link connected to Broadcast network
             Link-ID :   Link ID : 192.168.81.2
             Interface Address :   Interface Address : 192.168.81.1
             Admin Metric : 1
             Maximum Bandwidth : 5000000000
             Maximum reservable bandwidth : 3749999872
             Number of Priority : 8
               Priority 0 : 3749999872  Priority 1 : 3749999872
               Priority 2 : 3749999872  Priority 3 : 3749999872
               Priority 4 : 3749999872  Priority 5 : 3749999872
               Priority 6 : 3749999872  Priority 7 : 3749999872
             Affinity Bit : 0x0

             Number of Links : 1

           LS age: 447
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.1.11
           Opaque Type: 1
           Opaque ID: 267
           Advertising Router: 192.168.205.1
           LS Seq Number: 0x80000002
           Checksum: 0x6537
           Length: 116
           Fragment number: 267

             Link connected to Broadcast network
             Link-ID :   Link ID : 192.168.81.2
             Interface Address :   Interface Address : 192.168.81.2
             Admin Metric : 1
             Maximum Bandwidth : 5000000000
             Maximum reservable bandwidth : 3749999872
             Number of Priority : 8
               Priority 0 : 3749999872  Priority 1 : 3749999872
               Priority 2 : 3749999872  Priority 3 : 3749999872
               Priority 4 : 3749999872  Priority 5 : 3749999872
               Priority 6 : 3749999872  Priority 7 : 3749999872
             Affinity Bit : 0x0

             Number of Links : 1

           LS age: 457
           Options: 0x2 (No TOS-capability, No DC)
           LS Type: Opaque Area Link
           Link State ID: 10.1.1.15
           Opaque Type: 1
           Opaque ID: 271
           Advertising Router: 192.168.205.1
           LS Seq Number: 0x80000002
           Checksum: 0x4765
           Length: 116
           Fragment number: 271

             Link connected to Broadcast network
             Link-ID :   Link ID : 192.168.106.2
             Interface Address :   Interface Address : 192.168.106.2
             Admin Metric : 1
             Maximum Bandwidth : 5000000000
             Maximum reservable bandwidth : 3749999872
             Number of Priority : 8
               Priority 0 : 3749999872  Priority 1 : 3749999872
               Priority 2 : 3749999872  Priority 3 : 3749999872
               Priority 4 : 3749999872  Priority 5 : 3749999872
               Priority 6 : 3749999872  Priority 7 : 3749999872
             Affinity Bit : 0x0

             Number of Links : 1

        '''}

    def test_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpOspfDatabaseOpaqueAreaDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpOspfDatabaseOpaqueAreaDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpOspfDatabaseOpaqueAreaDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
