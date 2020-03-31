#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.nxos.aci.show_service import ShowServiceRedirInfoGroup


class TestShowServiceRedirInfoGroup(unittest.TestCase):

    dev = Device(name='aci')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'group_id': {
            366: {
                'destination': {
                    'dest-[2001:172:16:32::10]-[vxlan-2424832': {
                        'hg_name': 'Not attached',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-366',
                'oper_st': 'enabled',
                'oper_st_qual': 'no-oper-grp',
                'th': 0,
                'tl': 0,
                'tracking': 'no',
            },
            367: {
                'destination': {
                    'dest-[172.16.32.10]-[vxlan-2424832]': {
                        'hg_name': 'shangl-PBR::LB1',
                    },
                    'dest-[172.16.32.20]-[vxlan-2424832]': {
                        'hg_name': 'shangl-PBR::LB2',
                    },
                    'dest-[172.16.32.30]-[vxlan-2424832]': {
                        'hg_name': 'shangl-PBR::LB3',
                    },
                    'dest-[172.16.32.40]-[vxlan-2424832]': {
                        'hg_name': 'shangl-PBR::LB4',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-367',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            368: {
                'destination': {
                    'dest-[172.16.32.1]-[vxlan-2424832]': {
                        'hg_name': 'Not attached',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-368',
                'oper_st': 'enabled',
                'oper_st_qual': 'no-oper-grp',
                'th': 0,
                'tl': 0,
                'tracking': 'no',
            },
            369: {
                'destination': {
                    'dest-[2001:172:16:33::10]-[vxlan-2424832': {
                        'hg_name': 'Not attached',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-369',
                'oper_st': 'enabled',
                'oper_st_qual': 'no-oper-grp',
                'th': 0,
                'tl': 0,
                'tracking': 'no',
            },
            370: {
                'destination': {
                    'dest-[172.16.33.10]-[vxlan-2424832]': {
                        'hg_name': 'shangl-PBR::LB1',
                    },
                    'dest-[172.16.33.20]-[vxlan-2424832]': {
                        'hg_name': 'shangl-PBR::LB2',
                    },
                    'dest-[172.16.33.30]-[vxlan-2424832]': {
                        'hg_name': 'shangl-PBR::LB3',
                    },
                    'dest-[172.16.33.40]-[vxlan-2424832]': {
                        'hg_name': 'shangl-PBR::LB4',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-370',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            371: {
                'destination': {
                    'dest-[172.16.33.1]-[vxlan-2424832]': {
                        'hg_name': 'Not attached',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-371',
                'oper_st': 'enabled',
                'oper_st_qual': 'no-oper-grp',
                'th': 0,
                'tl': 0,
                'tracking': 'no',
            },
            394: {
                'destination': {
                    'No valid destinations': {
                        'hg_name': 'Not attached',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-394',
                'oper_st': 'disabled',
                'oper_st_qual': 'no-oper-grp',
                'th': 0,
                'tl': 0,
                'tracking': 'no',
            },
            395: {
                'destination': {
                    'No valid destinations': {
                        'hg_name': 'Not attached',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-395',
                'oper_st': 'disabled',
                'oper_st_qual': 'no-oper-grp',
                'th': 0,
                'tl': 0,
                'tracking': 'no',
            },
            396: {
                'destination': {
                    'dest-[172.16.32.1]-[vxlan-3014660]': {
                        'hg_name': 'shangl-vPC-vrrp::LB1',
                    },
                    'dest-[172.16.32.3]-[vxlan-3014660]': {
                        'hg_name': 'shangl-vPC-vrrp::LB3',
                    },
                    'dest-[172.16.32.4]-[vxlan-3014660]': {
                        'hg_name': 'shangl-vPC-vrrp',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-396',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            397: {
                'destination': {
                    'dest-[172.16.33.1]-[vxlan-3014660]': {
                        'hg_name': 'shangl-vPC-vrrp',
                    },
                    'dest-[172.16.33.3]-[vxlan-3014660]': {
                        'hg_name': 'shangl-vPC-vrrp::LB3',
                    },
                    'dest-[172.16.33.4]-[vxlan-3014660]': {
                        'hg_name': 'shangl-vPC-vrrp::LB4',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-397',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            402: {
                'destination': {
                    'dest-[172.16.228.1]-[vxlan-2555904]': {
                        'hg_name': 'toka-GiLAN::NAT',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-402',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            403: {
                'destination': {
                    'dest-[172.16.227.1]-[vxlan-2555904]': {
                        'hg_name': 'toka-GiLAN::NAT',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-403',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            404: {
                'destination': {
                    'dest-[172.16.223.1]-[vxlan-2555904]': {
                        'hg_name': 'toka-GiLAN::GW-',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-404',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            405: {
                'destination': {
                    'dest-[172.16.225.1]-[vxlan-2555904]': {
                        'hg_name': 'toka-GiLAN::LB-',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-405',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            406: {
                'destination': {
                    'dest-[172.16.224.1]-[vxlan-2555904]': {
                        'hg_name': 'toka-GiLAN::GW-',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-406',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            407: {
                'destination': {
                    'dest-[172.16.226.1]-[vxlan-2555904]': {
                        'hg_name': 'toka-GiLAN::LB-',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-407',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            429: {
                'destination': {
                    'dest-[10.186.0.1]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO2001:DB8::FW1',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-429',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            430: {
                'destination': {
                    'dest-[10.186.0.3]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO2001:DB8::FW3',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-430',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            431: {
                'destination': {
                    'dest-[10.186.0.4]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO2001:DB8::FW4',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-431',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            439: {
                'destination': {
                    'dest-[10.186.0.2]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO2001:DB8::FW2',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-439',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            512: {
                'destination': {
                    'dest-[172.16.11.1]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW1',
                    },
                    'dest-[172.16.11.2]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW2',
                    },
                    'dest-[172.16.11.3]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW3',
                    },
                    'dest-[172.16.11.4]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW4',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-512',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            513: {
                'destination': {
                    'dest-[172.16.12.1]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW1',
                    },
                    'dest-[172.16.12.2]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW2',
                    },
                    'dest-[172.16.12.3]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW3',
                    },
                    'dest-[172.16.12.4]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW4',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-513',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            522: {
                'destination': {
                    'dest-[2001:16:11::1]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW1v6',
                    },
                    'dest-[2001:16:11::2]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW2',
                    },
                    'dest-[2001:16:11::3]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW3v6',
                    },
                    'dest-[2001:16:11::4]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW4v6',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-522',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            523: {
                'destination': {
                    'dest-[2001:16:12::1]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW1v6',
                    },
                    'dest-[2001:16:12::2]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW2v6',
                    },
                    'dest-[2001:16:12::3]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW3',
                    },
                    'dest-[2001:16:12::4]-[vxlan-2293760]': {
                        'hg_name': 'SP-A-CISCO::GW4v6',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-523',
                'oper_st': 'disabled',
                'oper_st_qual': 'tracked-as-down',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            548: {
                'destination': {
                    'dest-[172.16.2.1]-[vxlan-2818053]': {
                        'hg_name': 'shangl-testauto',
                    },
                    'dest-[172.16.2.2]-[vxlan-2818053]': {
                        'hg_name': 'shangl-testauto::vGW2',
                    },
                },
                'hp': 'srconly',
                'name': 'destgrp-548',
                'oper_st': 'enabled',
                'oper_st_qual': 'no-oper-grp',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
            549: {
                'destination': {
                    'dest-[172.16.3.1]-[vxlan-2818053]': {
                        'hg_name': 'shangl-testauto::vGW1',
                    },
                    'dest-[172.16.3.2]-[vxlan-2818053]': {
                        'hg_name': 'shangl-testauto',
                    },
                },
                'hp': 'dstonly',
                'name': 'destgrp-549',
                'oper_st': 'enabled',
                'oper_st_qual': 'no-oper-grp',
                'th': 0,
                'tl': 0,
                'tracking': 'yes',
            },
        },
    }

    golden_output = {'execute.return_value': '''\
        show service redir info group 
        ============================================================================================
        LEGEND
        TL: Threshold(Low)   |     TH: Threshold(High)   |   HP: HashProfile     |     HG: HealthGrp
        ============================================================================================
        GrpID Name            destination                              HG-name         operSt     operStQual      TL   TH    HP         Tracking
        ===== ====            ===========                              ==============  =======    ============    ===  ====  ========   ========
        366   destgrp-366     dest-[2001:172:16:32::10]-[vxlan-2424832 Not attached    enabled    no-oper-grp     0    0     srconly    no      
        367   destgrp-367     dest-[172.16.32.40]-[vxlan-2424832]      shangl-PBR::LB4 disabled   tracked-as-down 0    0     srconly    yes     
                            dest-[172.16.32.20]-[vxlan-2424832]      shangl-PBR::LB2
                            dest-[172.16.32.10]-[vxlan-2424832]      shangl-PBR::LB1
                            dest-[172.16.32.30]-[vxlan-2424832]      shangl-PBR::LB3
        368   destgrp-368     dest-[172.16.32.1]-[vxlan-2424832]       Not attached    enabled    no-oper-grp     0    0     srconly    no      
        369   destgrp-369     dest-[2001:172:16:33::10]-[vxlan-2424832 Not attached    enabled    no-oper-grp     0    0     dstonly    no      
        370   destgrp-370     dest-[172.16.33.30]-[vxlan-2424832]      shangl-PBR::LB3 disabled   tracked-as-down 0    0     dstonly    yes     
                            dest-[172.16.33.40]-[vxlan-2424832]      shangl-PBR::LB4
                            dest-[172.16.33.20]-[vxlan-2424832]      shangl-PBR::LB2
                            dest-[172.16.33.10]-[vxlan-2424832]      shangl-PBR::LB1
        371   destgrp-371     dest-[172.16.33.1]-[vxlan-2424832]       Not attached    enabled    no-oper-grp     0    0     dstonly    no      
        394   destgrp-394     No valid destinations                    Not attached    disabled   no-oper-grp     0    0     srconly    no      
        395   destgrp-395     No valid destinations                    Not attached    disabled   no-oper-grp     0    0     dstonly    no      
        396   destgrp-396     dest-[172.16.32.4]-[vxlan-3014660]       shangl-vPC-vrrp disabled   tracked-as-down 0    0     srconly    yes     
                            dest-[172.16.32.3]-[vxlan-3014660]       shangl-vPC-vrrp::LB3
                            dest-[172.16.32.1]-[vxlan-3014660]       shangl-vPC-vrrp::LB1
        397   destgrp-397     dest-[172.16.33.1]-[vxlan-3014660]       shangl-vPC-vrrp disabled   tracked-as-down 0    0     dstonly    yes     
                            dest-[172.16.33.3]-[vxlan-3014660]       shangl-vPC-vrrp::LB3
                            dest-[172.16.33.4]-[vxlan-3014660]       shangl-vPC-vrrp::LB4
        402   destgrp-402     dest-[172.16.228.1]-[vxlan-2555904]      toka-GiLAN::NAT disabled   tracked-as-down 0    0     srconly    yes     
        403   destgrp-403     dest-[172.16.227.1]-[vxlan-2555904]      toka-GiLAN::NAT disabled   tracked-as-down 0    0     srconly    yes     
        404   destgrp-404     dest-[172.16.223.1]-[vxlan-2555904]      toka-GiLAN::GW- disabled   tracked-as-down 0    0     srconly    yes     
        405   destgrp-405     dest-[172.16.225.1]-[vxlan-2555904]      toka-GiLAN::LB- disabled   tracked-as-down 0    0     srconly    yes     
        406   destgrp-406     dest-[172.16.224.1]-[vxlan-2555904]      toka-GiLAN::GW- disabled   tracked-as-down 0    0     srconly    yes     
        407   destgrp-407     dest-[172.16.226.1]-[vxlan-2555904]      toka-GiLAN::LB- disabled   tracked-as-down 0    0     srconly    yes     
        429   destgrp-429     dest-[10.186.0.1]-[vxlan-2293760]          SP-A-CISCO2001:DB8::FW1 disabled   tracked-as-down 0    0     dstonly    yes     
        430   destgrp-430     dest-[10.186.0.3]-[vxlan-2293760]          SP-A-CISCO2001:DB8::FW3 disabled   tracked-as-down 0    0     dstonly    yes     
        431   destgrp-431     dest-[10.186.0.4]-[vxlan-2293760]          SP-A-CISCO2001:DB8::FW4 disabled   tracked-as-down 0    0     dstonly    yes     
        439   destgrp-439     dest-[10.186.0.2]-[vxlan-2293760]          SP-A-CISCO2001:DB8::FW2 disabled   tracked-as-down 0    0     dstonly    yes     
        512   destgrp-512     dest-[172.16.11.4]-[vxlan-2293760]       SP-A-CISCO::GW4 disabled   tracked-as-down 0    0     srconly    yes     
                            dest-[172.16.11.1]-[vxlan-2293760]       SP-A-CISCO::GW1
                            dest-[172.16.11.2]-[vxlan-2293760]       SP-A-CISCO::GW2
                            dest-[172.16.11.3]-[vxlan-2293760]       SP-A-CISCO::GW3
        513   destgrp-513     dest-[172.16.12.2]-[vxlan-2293760]       SP-A-CISCO::GW2 disabled   tracked-as-down 0    0     dstonly    yes     
                            dest-[172.16.12.1]-[vxlan-2293760]       SP-A-CISCO::GW1
                            dest-[172.16.12.3]-[vxlan-2293760]       SP-A-CISCO::GW3
                            dest-[172.16.12.4]-[vxlan-2293760]       SP-A-CISCO::GW4
        522   destgrp-522     dest-[2001:16:11::2]-[vxlan-2293760]     SP-A-CISCO::GW2 disabled   tracked-as-down 0    0     srconly    yes     
                            dest-[2001:16:11::3]-[vxlan-2293760]     SP-A-CISCO::GW3v6
                            dest-[2001:16:11::4]-[vxlan-2293760]     SP-A-CISCO::GW4v6
                            dest-[2001:16:11::1]-[vxlan-2293760]     SP-A-CISCO::GW1v6
        523   destgrp-523     dest-[2001:16:12::3]-[vxlan-2293760]     SP-A-CISCO::GW3 disabled   tracked-as-down 0    0     dstonly    yes     
                            dest-[2001:16:12::2]-[vxlan-2293760]     SP-A-CISCO::GW2v6
                            dest-[2001:16:12::4]-[vxlan-2293760]     SP-A-CISCO::GW4v6
                            dest-[2001:16:12::1]-[vxlan-2293760]     SP-A-CISCO::GW1v6
        548   destgrp-548     dest-[172.16.2.1]-[vxlan-2818053]        shangl-testauto enabled    no-oper-grp     0    0     srconly    yes     
                            dest-[172.16.2.2]-[vxlan-2818053]        shangl-testauto::vGW2
        549   destgrp-549     dest-[172.16.3.2]-[vxlan-2818053]        shangl-testauto enabled    no-oper-grp     0    0     dstonly    yes     
                            dest-[172.16.3.1]-[vxlan-2818053]        shangl-testauto::vGW1                    
                                    
    '''
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowServiceRedirInfoGroup(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowServiceRedirInfoGroup(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
