''' show_ospf_database.py

IOSXE parsers for the following show commands:

    * show ip ospf database
    * show ip ospf database router
    * show ip ospf database network
    * show ip ospf database summary
    * show ip ospf database external
    * show ip ospf database opaque-area
    * show ip ospf database opaque-area self-originate
    * show ip ospf database opaque-area adv-router {address}
'''

# Python
import re
import xmltodict
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common

# ===========================
# Schema for:
#   * 'show ip ospf database'
# ===========================
class ShowIpOspfDatabaseSchema(MetaParser):
    
    ''' Schema for:
        * 'show ip ospf database'
    '''

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {'instance':
                            {Any():
                                {Optional('areas'):
                                    {Any():
                                        {'database':
                                            {'lsa_types':
                                                {Any():
                                                    {'lsa_type': int,
                                                    'lsas':
                                                        {Any():
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2':
                                                                {'header':
                                                                    {'lsa_id': str,
                                                                    'adv_router': str,
                                                                    'age': int,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    Optional('link_count'): int,
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
                            },
                        },
                    },
                },
            },
        }


# ==========================
# Parser for:
#    'show ip ospf database'
# ==========================
class ShowIpOspfDatabase(ShowIpOspfDatabaseSchema):

    ''' Parser for:
        * 'show ip ospf database'
    '''

    cli_command = 'show ip ospf database'
    exclude = ['age']

    def cli(self, output=None):

        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        address_family = 'ipv4'
        default_mt_id = 0

        # 1: Router
        # 2: Network Link
        # 3: Summary
        # 3: Summary Network
        # 3: Summary Net
        # 4: Summary ASB
        # 5: Type-5 AS External
        # 10: Opaque Area
        lsa_type_mapping = {
            'router': 1,
            'net': 2,
            'summary': 3,
            'summary net': 3,
            'summary asb': 4,
            'external': 5,
            'opaque': 10,
            }

        # OSPF Router with ID (172.16.1.214) (Process ID 65109)
        # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
        p1 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)'
                         ' +\(Process +ID +(?P<instance>(\d+))'
                         '(?:, +VRF +(?P<vrf>(\S+)))?\)$')

        # Router Link States (Area 0)
        # Net Link States (Area 0)
        # Summary Net Link States (Area 8)
        # Summary ASB Link States (Area 8)
        p2 = re.compile(r'^(?P<lsa_type>([a-zA-Z\s]+)) +Link +States +\(Area'
                         ' +(?P<area>(\S+))\)$')

        # Link ID         ADV Router      Age         Seq#       Checksum Link count
        # 10.13.202.64    10.120.202.64   2794        0x80000043 0x002254 3
        # 10.1.1.2        10.169.197.253  70          0x8000003F 0x0015EF
        p3 = re.compile(r'^(?P<link_id>(\S+)) +(?P<adv_router>(\S+))'
                         ' +(?P<age>(\d+)) +(?P<seq>(\S+)) +(?P<checksum>(\S+))'
                         '(?: *(?P<link_count>(\d+)))?$')

        for line in out.splitlines():
            line = line.strip()

            # Load for five secs: 71%/0%; one minute: 11%; five minutes: 9%
            # Time source is NTP, 20:29:26.348 EST Fri Nov 11 2016

            # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                router_id = str(group['router_id'])
                instance = str(group['instance'])
                if group['vrf']:
                    vrf = str(group['vrf'])
                else:
                    vrf = 'default'
                # Create dict
                ospf_dict = ret_dict.setdefault('vrf', {}).\
                                     setdefault(vrf, {}).\
                                     setdefault('address_family', {}).\
                                     setdefault(address_family, {}).\
                                     setdefault('instance', {}).\
                                     setdefault(instance, {})
                continue

            # Router Link States (Area 0)
            # Net Link States (Area 0)
            # Summary Net Link States (Area 8)
            # Summary ASB Link States (Area 8)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lsa_type_key = group['lsa_type'].lower()
                if lsa_type_key in lsa_type_mapping:
                    lsa_type = lsa_type_mapping[lsa_type_key]
                else:
                    continue

                # Set area
                if group['area']:
                    try:
                        int(group['area'])
                        area = str(IPAddress(str(group['area'])))
                    except Exception:
                        area = str(group['area'])
                else:
                    area = '0.0.0.0'

                # Create dict structure
                lsa_type_dict = ospf_dict.setdefault('areas', {}).\
                                          setdefault(area, {}).\
                                          setdefault('database', {}).\
                                          setdefault('lsa_types', {}).\
                                          setdefault(lsa_type, {})
                # Set lsa_type
                lsa_type_dict['lsa_type'] = lsa_type
                continue

            # Link ID         ADV Router      Age         Seq#       Checksum Link count
            # 10.13.202.64    10.120.202.64   2794        0x80000043 0x002254 3
            # 10.1.1.2        10.169.197.253  70          0x8000003F 0x0015EF
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lsa_id = group['link_id']

                # Create dict
                lsas_dict = lsa_type_dict.setdefault('lsas', {}).\
                                          setdefault(lsa_id, {})
                lsas_dict['lsa_id'] = lsa_id
                lsas_dict['adv_router'] = group['adv_router']

                # osfpv2 dict
                ospfv2_dict = lsas_dict.setdefault('ospfv2', {}).\
                                        setdefault('header', {})
                ospfv2_dict['lsa_id'] = lsa_id
                ospfv2_dict['adv_router'] = group['adv_router']
                ospfv2_dict['age'] = int(group['age'])
                ospfv2_dict['seq_num'] = group['seq']
                ospfv2_dict['checksum'] = group['checksum']
                if group['link_count']:
                    ospfv2_dict['link_count'] = int(group['link_count'])
                continue

        return ret_dict


# =====================================
# Super parser for:
#   * 'show ip ospf database external'
#   * 'show ip ospf database network'
#   * 'show ip ospf database summary'
#   * 'show ip ospf database router'
#   * 'show ip ospf database opaque'
#   * 'show ip ospf database opaque-area self-originate'
# =====================================
class ShowIpOspfDatabaseTypeParser(MetaParser):

    ''' Parser for:
        * 'show ip ospf database external'
        * 'show ip ospf database network'
        * 'show ip ospf database summary'
        * 'show ip ospf database router'
        * 'show ip ospf database opaque
        * 'show ip ospf database opaque-area self-originate''
    '''

    def cli(self, db_type, out=None):

        assert db_type in ['external', 'network', 'summary', 'router',
                           'opaque']

        # Init vars
        ret_dict = {}
        address_family = 'ipv4'
        default_mt_id = 0
        capabilities_flag = False
        tlv_type_flag = False
        sub_tlv_type_flag = False
        sub_tlv_temp = []

        # Router
        # Network Link
        # Summary Network
        # Opaque Area
        # Type-5 AS External
        lsa_type_mapping = {
            'router': 1,
            'network': 2,
            'summary': 3,
            'external': 5,
            'opaque': 10,
            }

        p1 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)'
                            ' +\(Process +ID +(?P<instance>(\d+))'
                            '(?:, +VRF +(?P<vrf>(\S+)))?\)$')
       
        p2 = re.compile(r'^(?P<lsa_type_name>(.*)) +Link +States'
                            '(?: +\(Area +(?P<area>(\S+))\))?$')
       
        p3_1 = re.compile(r'^Routing +Bit +Set +on +this +LSA$')
       
        p3_2 = re.compile(r'^LS +age: +(?P<age>(\d+))$')
       
        p3_2_1 = re.compile(r'^LS +age: +\w+\((?P<age>(\d+))\)$')
       
        p4 = re.compile(r'^Options:(?: +(?P<option>([a-zA-Z0-9]+)))?'
                        '(?: *\((?P<option_desc>(.*))\))?$')
       
        p5_1 = re.compile(r'^LS +Type: +(?P<lsa_type>(.*))$')
       
        p5_2 = re.compile(r'^Link +State +ID: +(?P<lsa_id>(\S+))'
                            '(?: +\(.*\))?$')
       
        p6 = re.compile(r'^Advertising +Router: +(?P<adv_router>(\S+))$')
       
        p7 = re.compile(r'^LS +Seq +Number: +(?P<ls_seq_num>(\S+))$')
       
        p8 = re.compile(r'^Checksum: +(?P<checksum>(\S+))$')
       
        p9 = re.compile(r'^Length *: +(?P<length>(\d+))$')
       
        p10 = re.compile(r'^Network +Mask: +\/(?P<net_mask>(\S+))$')
       
        p11_1 = re.compile(r'^Metric +Type: +2 +\(.*\)$')
       
        p11_2 = re.compile(r'^Metric +Type: +1 +\(.*\)$')
       
        p12 = re.compile(r'^TOS:? +(?P<tos>(\d+))(?:(\s+|\t+)Metric(?:s)?:'
                            ' +(?P<metric>(\d+)))?$')
       
        p13 = re.compile(r'^Metric: +(?P<metric>(\d+))$')
       
        p14 = re.compile(r'^Forward +Address: +(?P<addr>(\S+))$')
       
        p15 = re.compile(r'^External +Route +Tag: +(?P<tag>(\d+))$')
       
        p16 = re.compile(r'^Attached +Router: +(?P<att_router>(\S+))$')
       
        p17 = re.compile(r'^Number +of +(l|L)inks *: +(?P<num>(\d+))$')
       
        p18 = re.compile(r'^Link +connected +to: +a +(?P<type>(.*))$')
       
        p18_1 = re.compile(r'^Link\s+connected +to\s*: +(?P<type>(.*))$')
       
        p19_1 = re.compile(r'^\(Link +ID\) +Network\/(s|S)ubnet +(n|N)umber:'
                            ' +(?P<link_id>(\S+))$')
       
        p19_2 = re.compile(r'^\(Link +ID\) +(D|d)esignated +(R|r)outer'
                            ' +(a|A)ddress: +(?P<link_id>(\S+))$')
       
        p19_3 = re.compile(r'^\(Link +ID\) +(N|n)eighboring +(R|r)outer'
                            ' +(I|d)D: +(?P<link_id>(\S+))$')
       
        p20_1 = re.compile(r'^\(Link +Data\) +Network +Mask:'
                            ' +(?P<link_data>(\S+))$')
       
        p20_2 = re.compile(r'^\(Link +Data\) +Router +Interface +address:'
                            ' +(?P<link_data>(\S+))$')
       
        # MTID 32 Metrics: 1
        # MTID   : 0
        p21 = re.compile(r'MTID\s*:*\s*(?P<mtid>\d+)\s*(?:(Metrics*\s*:*\s*(?P<metric>\d+)))?')
       
        p21_1 = re.compile(r'^Number +of +MTID +metrics: +(?P<num>(\d+))$')
       
        p22 = re.compile(r'^Opaque +Type: +(?P<type>(\d+))(?: +\((Traffic Engineering)\))?$')
       
        p23 = re.compile(r'^Opaque +ID: +(?P<id>(\d+))$')
       
        p24 = re.compile(r'^Fragment +number *: +(?P<num>(\d+))$')
       
        p25 = re.compile(r'^MPLS +TE +router +ID *: +(?P<mpls>(\S+))$')
       
        p26_1 = re.compile(r'^AS +Boundary +Router$')
       
        p26_2 = re.compile(r'^Area +Border +Router$')
       
        p27 = re.compile(r'^Link +connected +to\s*\:*\s+(?P<link>(.*))$')
       
        p28 = re.compile(r'^Link +ID *: +(?P<id>(\S+))$')
       
        p29 = re.compile(r'^Interface +Address *: +(?P<addr>(\S+))$')
       
        p30 = re.compile(r'^Admin +Metric *: +(?P<te_metric>(\d+))$')
       
        p31 = re.compile(r'^Maximum +(B|b)andwidth *:'
                            ' +(?P<max_band>(\d+))$')
       
        p32 = re.compile(r'^Maximum +(R|r)eservable +(B|b)andwidth'
                            '(?: +global)? *: +(?P<max_res_band>(\d+))$')
       
        p33 = re.compile(r'^Affinity +Bit *: +(?P<admin_group>(\S+))$')
       
        p33_1 = re.compile(r'^IGP +Metric *: +(?P<igp_metric>(\d+))$')
       
        p33_2 = re.compile(r'^Number +of +Priority *: +(?P<num>(\d+))$')
       
        p34 = re.compile(r'^Priority +(?P<num1>(\d+)) *:'
                            ' +(?P<band1>(\d+))(?: +Priority +(?P<num2>(\d+))'
                            ' *: +(?P<band2>(\d+)))?$')
       
        p35 = re.compile(r'^Unknown +Sub-TLV *: +Type += +(?P<type>(\d+)),'
                            ' +Length += +(?P<length>(\d+))'
                            ' +Value += +(?P<value>(.*))$')
       
        p36 = re.compile(r'^Extended +Administrative +Group *: +Length *:'
                            ' +(?P<eag_length>(\d+))$')
       
        p37 = re.compile(r'^EAG\[(?P<group_num>(\d+))\]: +(?P<val>(\d+))$')

        # Neighbor Address : 192.168.220.2
        p38 = re.compile(r'Neighbor\s+Address\s*:\s*(?P<neighbor_address>\S+)')

        # TLV Type: Router Information
        # TLV Type: Segment Routing Algorithm
        p39 = re.compile(r'TLV\s+Type\s*:\s*(?P<tlv_type>.+)')

        # Router Information
        p39_1 = re.compile(r'(R|r)outer\s+(I|i)nformation')

        # Segment Routing Algorithm
        p39_2 = re.compile(r'(S|s)egment\s+(R|r)outing\s+(A|a)lgorithm')

        # Segment Routing Range
        p39_3 = re.compile(r'(S|s)egment\s+(R|r)outing\s+(R|r)ange')

        # Segment Routing Node MSD
        p39_4 = re.compile(r'(S|s)egment\s+(R|r)outing\s+(N|n)ode\s+MSD')

        # Segment Routing Local Block
        p39_5 = re.compile(r'(S|s)egment\s+(R|r)outing\s+(L|l)ocal\s+(B|b)lock')

        # Extended Prefix
        p39_6 = re.compile(r'(E|e)xtended\s+(P|p)refix')

        # Extended Link
        p39_7 = re.compile(r'(E|e)xtended\s+(L|l)ink')

        # Algorithm: SPF
        # Algorithm: Strict SPF
        p40 = re.compile(r'Algo(?:(rithm))?\s*:\s*(?P<algorithm>.+)')

        # Range Size: 1000
        p41 = re.compile(r'Range\s+Size\s*:\s*(?P<range_size>\d+)')

        # Flags  : L-Bit, V-bit
        p42 = re.compile(r'Flags\s*\:\s*(?P<flags>.+)')        

        # Weight : 0
        p44 = re.compile(r'Weight\s*:\s*(?P<weight>\d+)')

        # Label  : 19
        p45 = re.compile(r'Label\s*:\s*(?P<label>\d+)')       
        
        # (Link Data) Interface IP address: 192.168.220.1
        p46 = re.compile(r'\(Link\s+Data\)\s+Interface\s+IP\s+address\s*:\s*(?P<link_data>\S+)')

        # Prefix    : 10.4.1.1/32
        p47 = re.compile(r'Prefix\s*:\s*(?P<prefix>\S+)')

        # AF        : 0
        p48 = re.compile(r'AF\s*:\s*(?P<af>\S+)')

        # Route-type: Intra
        p49 = re.compile(r'Route\-type\s*:\s*(?P<route_type>.+)')

        # Sub-TLV Type: Remote Intf Addr
        # Sub-TLV Type: Local / Remote Intf ID
        p50 = re.compile(r'Sub\-TLV\s+Type\s*:\s*(?P<sub_tlv_type>.+)')

        # Remote Interface Address   : 192.168.0.1
        p51 = re.compile(r'Remote\s+Interface\s+Address\s*:\s*(?P<remote_interface_address>\S+)')

        # Local Interface ID   : 20
        p52 = re.compile(r'Local\s+Interface\s+ID\s*:\s*(?P<local_interface_id>\S+)')

        # Remote Interface ID   : 20
        p53 = re.compile(r'Remote\s+Interface\s+ID\s*:\s*(?P<remote_interface_id>\S+)')

        # SID   : 1
        p54 = re.compile(r'SID\s*:\s*(?P<sid>\S+)')

        # Graceful Restart Helper                
        p55 = re.compile(r'(G|g)raceful\s+(R|r)estart\s+(H|h)elper')

        # Stub Router Support
        p56 = re.compile(r'(S|s)tub\s+(R|r)outer\s+(S|s)upport')

        # SPF
        p57 = re.compile(r'SPF')

        # Strict SPF
        p58 = re.compile(r'Strict\s+SPF')

        # Sub-type: Node Max Sid Depth, Value: 13
        p59 = re.compile(r'Sub\-type\s*:\s*Node\s+Max\s+Sid\s+Depth\,\s+Value:\s*(?P<value>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # OSPF Router with ID (10.36.3.3) (Process ID 1)
            # OSPF Router with ID (10.36.3.3) (Process ID 1, VRF VRF1)
            m = p1.match(line)
            if m:
                router_id = str(m.groupdict()['router_id'])
                instance = str(m.groupdict()['instance'])
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if address_family not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][address_family] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][address_family]:
                    ret_dict['vrf'][vrf]['address_family'][address_family]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][address_family]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][address_family]['instance']\
                        [instance] = {}
                continue

            # Router Link States (Area 0)
            # Net Link States (Area 1)
            # Summary Net Link States (Area 0.0.0.0)
            # Type-5 AS External Link States
            # Type-10 Opaque Link Area Link States (Area 0)
            m = p2.match(line)
            if m:
                lsa_type = lsa_type_mapping[db_type]
                
                # Set area
                if m.groupdict()['area']:
                    try:
                        int(m.groupdict()['area'])
                        area = str(IPAddress(str(m.groupdict()['area'])))
                    except Exception:
                        area = str(m.groupdict()['area'])
                else:
                    area = '0.0.0.0'

                # Create dict structure
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][address_family]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][address_family]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][address_family]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][address_family]['instance']\
                        [instance]['areas'][area] = {}
                if 'database' not in ret_dict['vrf'][vrf]['address_family'][address_family]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][address_family]['instance']\
                        [instance]['areas'][area]['database'] = {}
                if 'lsa_types' not in ret_dict['vrf'][vrf]['address_family']\
                        [address_family]['instance'][instance]['areas'][area]['database']:
                    ret_dict['vrf'][vrf]['address_family'][address_family]['instance']\
                        [instance]['areas'][area]['database']['lsa_types'] = {}
                if lsa_type not in ret_dict['vrf'][vrf]['address_family'][address_family]\
                        ['instance'][instance]['areas'][area]['database']\
                        ['lsa_types']:
                    ret_dict['vrf'][vrf]['address_family'][address_family]['instance']\
                        [instance]['areas'][area]['database']['lsa_types']\
                        [lsa_type] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][address_family]\
                            ['instance'][instance]['areas'][area]['database']\
                            ['lsa_types'][lsa_type]

                # Set lsa_type
                sub_dict['lsa_type'] = lsa_type
                continue

            # Routing Bit Set on this LSA
            m = p3_1.match(line)
            if m:
                routing_bit_enable = True
                continue

            # LS age: 1565
            m = p3_2.match(line)
            if m:
                tlv_type_flag = False
                sub_tlv_type_flag = False
                age = int(m.groupdict()['age'])
                continue

            # LS age: MAXAGE(3601)
            m = p3_2_1.match(line)
            if m:
                tlv_type_flag = False
                sub_tlv_type_flag = False
                age = int(m.groupdict()['age'])
                continue

            # Options: 0x20 (No TOS-capability, DC)
            # Options: (No TOS-capability, DC)
            m = p4.match(line)
            if m:
                option = str(m.groupdict()['option'])
                option_desc = str(m.groupdict()['option_desc'])
                continue

            # LS Type: Type-5 AS-External
            m = p5_1.match(line)
            if m:
                lsa_type = lsa_type_mapping[db_type]
                continue

            # Link State ID: 10.4.1.1
            # Link State ID: 10.94.44.44 (Network address)
            # Link State ID: 10.1.2.1 (Designated Router address)
            # Link State ID: 10.1.2.1 (address of Designated Router)
            m = p5_2.match(line)
            if m:
                lsa_id = str(m.groupdict()['lsa_id'])
                continue

            # Advertising Router: 10.64.4.4
            m = p6.match(line)
            if m:
                adv_router = str(m.groupdict()['adv_router'])
                lsa = '{} {}'.format(lsa_id, adv_router)
                
                # Reset counters for this lsa
                link_tlv_counter = 0
                unknown_tlvs_counter = 0

                # Create schema structure
                if 'lsas' not in sub_dict:
                    sub_dict['lsas'] = {}
                if lsa not in sub_dict['lsas']:
                    sub_dict['lsas'][lsa] = {}
                
                # Set keys under 'lsa'
                sub_dict['lsas'][lsa]['adv_router'] = adv_router
                try:
                    sub_dict['lsas'][lsa]['lsa_id'] = lsa_id
                except Exception:
                    pass

                # Set db_dict
                if 'ospfv2' not in sub_dict['lsas'][lsa]:
                    sub_dict['lsas'][lsa]['ospfv2'] = {}
                if 'body' not in sub_dict['lsas'][lsa]['ospfv2']:
                    sub_dict['lsas'][lsa]['ospfv2']['body'] = {}
                if db_type not in sub_dict['lsas'][lsa]['ospfv2']['body']:
                    sub_dict['lsas'][lsa]['ospfv2']['body'][db_type] = {}
                db_dict = sub_dict['lsas'][lsa]['ospfv2']['body'][db_type]

                # Create 'topologies' sub_dict if 'summary' or 'database'
                if db_type in ['summary', 'external']:
                    if 'topologies' not in db_dict:
                        db_dict['topologies'] = {}
                    if default_mt_id not in db_dict['topologies']:
                        db_dict['topologies'][default_mt_id] = {}
                    db_topo_dict = db_dict['topologies'][default_mt_id]
                    db_topo_dict['mt_id'] = default_mt_id

                # Set header dict
                if 'header' not in sub_dict['lsas'][lsa]['ospfv2']:
                    sub_dict['lsas'][lsa]['ospfv2']['header'] = {}
                header_dict = sub_dict['lsas'][lsa]['ospfv2']['header']

                # Set previously parsed values
                try:
                    header_dict['routing_bit_enable'] = routing_bit_enable
                    del routing_bit_enable
                except Exception:
                    pass
                try:
                    header_dict['age'] = age
                    del age
                except Exception:
                    pass
                try:
                    header_dict['option'] = option
                    del option
                except Exception:
                    pass
                try:
                    header_dict['option_desc'] = option_desc
                    del option_desc
                except Exception:
                    pass
                try:
                    header_dict['type'] = lsa_type
                    del lsa_type
                except Exception:
                    pass
                try:
                    header_dict['lsa_id'] = lsa_id
                    del lsa_id
                except Exception:
                    pass
                try:
                    header_dict['adv_router'] = adv_router
                    del adv_router
                except Exception:
                    pass
                try:
                    header_dict['opaque_type'] = opaque_type
                    del opaque_type
                except Exception:
                    pass
                try:
                    header_dict['opaque_id'] = opaque_id
                    del opaque_id
                except Exception:
                    pass

            # LS Seq Number: 0x80000002
            m = p7.match(line)
            if m:
                header_dict['seq_num'] = str(m.groupdict()['ls_seq_num'])
                continue

            # Checksum: 0x7d61
            m = p8.match(line)
            if m:
                header_dict['checksum'] = str(m.groupdict()['checksum'])
                continue

            # Length: 36
            # Length : 36
            m = p9.match(line)
            if m:
                length = int(m.groupdict()['length'])
                if sub_tlv_type_flag:
                    sub_tlv_types_dict['length'] = length
                elif tlv_type_flag:
                    tlv_type_dict['length'] = length
                else:
                    header_dict['length'] = length
                continue

            # Network Mask: /32
            m = p10.match(line)
            if m:
                dummy = '{}/{}'.format('0.0.0.0', m.groupdict()['net_mask'])
                db_dict['network_mask'] = str(IPNetwork(dummy).netmask)
                continue

            # Metric Type: 2 (Larger than any link state path)
            # Metric Type: 2 (Larger than any link state path)
            m = p11_1.match(line)
            if m:
                db_topo_dict['flags'] = "E"
                db_topo_dict['metric_type'] = 2
                continue

            # Metric Type: 1 (Comparable directly to link state metric)
            m = p11_2.match(line)
            if m:
                db_topo_dict['metric_type'] = 1
                continue

            # TOS: 0
            # TOS: 0 Metric: 1
            m = p12.match(line)
            if m:
                if db_type == 'router':
                    if m.groupdict()['tos']:
                        db_dict['links'][link_id]['topologies'][default_mt_id]\
                                ['tos'] = int(m.groupdict()['tos'])
                    if m.groupdict()['metric']:
                        db_dict['links'][link_id]['topologies'][default_mt_id]\
                                ['metric'] = int(m.groupdict()['metric'])
                        continue
                else:
                    db_topo_dict['tos'] = int(m.groupdict()['tos'])
                    if m.groupdict()['metric']:
                        db_topo_dict['metric'] = int(m.groupdict()['metric'])
                        continue

            # Metric: 20
            m = p13.match(line)
            if m:
                db_topo_dict['metric'] = int(m.groupdict()['metric'])
                continue

            # Forward Address: 0.0.0.0
            m = p14.match(line)
            if m:
                db_topo_dict['forwarding_address'] = str(m.groupdict()['addr'])
                continue

            # External Route Tag: 0
            m = p15.match(line)
            if m:
                db_topo_dict['external_route_tag'] = int(m.groupdict()['tag'])
                continue

            # Attached Router: 10.84.66.66
            m = p16.match(line)
            if m:
                attached_router = str(m.groupdict()['att_router'])
                if 'attached_routers' not in db_dict:
                    db_dict['attached_routers'] = {}
                if attached_router not in db_dict['attached_routers']:
                    db_dict['attached_routers'][attached_router] = {}
                continue

            # Number of links: 3
            # Number of Links: 3
            m = p17.match(line)
            if m:
                db_dict['num_of_links'] = int(m.groupdict()['num'])
                continue

            # Link connected to: a Stub Network
            m = p18.match(line)
            if m:
                link_type = str(m.groupdict()['type']).lower()
                continue

            # Link connected to: another Router (point-to-point)
            m = p18_1.match(line)
            if m:
                if tlv_type_flag:                    
                    sub_link_type = str(m.groupdict()['type']).lower()
                    if 'another router' in sub_link_type:
                        opaque_link_type = 1
                    tlv_type_dict['link_name'] = sub_link_type
                    tlv_type_dict['link_type'] = opaque_link_type
                    continue

                link_type = str(m.groupdict()['type']).lower()
                continue

            # (Link ID) Network/subnet number: 10.4.1.1
            m = p19_1.match(line)
            if m:
                link_id = str(m.groupdict()['link_id'])

                # Create dict structures
                if 'links' not in db_dict:
                    db_dict['links'] = {}
                if link_id not in db_dict['links']:
                    db_dict['links'][link_id] = {}
                db_dict['links'][link_id]['link_id'] = link_id

                # Set previously parsed values
                try:
                    db_dict['links'][link_id]['type'] = link_type
                except Exception:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if default_mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][default_mt_id] = {}
                db_dict['links'][link_id]['topologies'][default_mt_id]['mt_id'] = default_mt_id
                continue

            # (Link ID) Designated Router address: 10.166.7.6
            m = p19_2.match(line)
            if m:
                link_id = str(m.groupdict()['link_id'])

                # If 'TLV Type' found in output this flag is set to true
                if tlv_type_flag:
                    tlv_type_dict['link_id'] = link_id
                    continue

                # Create dict structures
                if 'links' not in db_dict:
                    db_dict['links'] = {}
                if link_id not in db_dict['links']:
                    db_dict['links'][link_id] = {}
                db_dict['links'][link_id]['link_id'] = link_id

                # Set previously parsed values
                try:
                    db_dict['links'][link_id]['type'] = link_type
                except Exception:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if default_mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][default_mt_id] = {}
                db_dict['links'][link_id]['topologies'][default_mt_id]['mt_id'] = default_mt_id
                continue

            # (Link ID) Neighboring Router ID: 10.151.22.22
            m = p19_3.match(line)
            if m:
                link_id = str(m.groupdict()['link_id'])

                if tlv_type_flag:
                    tlv_type_dict['link_id'] = link_id
                    continue

                # Create dict structures
                if 'links' not in db_dict:
                    db_dict['links'] = {}
                if link_id not in db_dict['links']:
                    db_dict['links'][link_id] = {}
                db_dict['links'][link_id]['link_id'] = link_id

                # Set previously parsed values
                try:
                    db_dict['links'][link_id]['type'] = link_type
                except Exception:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if default_mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][default_mt_id] = {}
                db_dict['links'][link_id]['topologies'][default_mt_id]['mt_id'] = default_mt_id
                continue

            # (Link Data) Network Mask: 255.255.255.255
            m = p20_1.match(line)
            if m:
                db_dict['links'][link_id]['link_data'] = \
                    str(m.groupdict()['link_data'])
                continue

            # (Link Data) Router Interface address: 10.166.7.6
            m = p20_2.match(line)
            if m:
                db_dict['links'][link_id]['link_data'] = \
                    str(m.groupdict()['link_data'])
                continue

            # MTID 32 Metrics: 1
            # MTID   : 0
            m = p21.match(line)
            if m:
                mtid = int(m.groupdict()['mtid'])

                if sub_tlv_type_flag:
                    sub_tlv_types_dict['mt_id'] = int(mtid)
                    continue

                if db_type == 'router':
                    if mtid not in db_dict['links'][link_id]['topologies']:
                        db_dict['links'][link_id]['topologies'][mtid] = {}
                    db_dict['links'][link_id]['topologies'][mtid]['mt_id'] = mtid
                    db_dict['links'][link_id]['topologies'][mtid]['metric'] = \
                        int(m.groupdict()['metric'])
                elif db_type == 'summary':
                    if 'topologies' not in db_dict:
                        db_dict['topologies'] = {}
                    if mtid not in db_dict['topologies']:
                        db_dict['topologies'][mtid] = {}
                    db_topo_dict = db_dict['topologies'][mtid]
                    db_topo_dict['mt_id'] = mtid
                    db_topo_dict['metric'] = int(m.groupdict()['metric'])
                continue

            # Number of MTID metrics: 0
            m = p21_1.match(line)
            if m:
                db_dict['links'][link_id]['num_mtid_metrics'] = \
                    int(m.groupdict()['num'])
                continue
                
            # Number of TOS metrics: 0
            p21_2 = re.compile(r'^Number +of +TOS +metrics: +(?P<num>(\d+))$')
            m = p21_2.match(line)
            if m:
                db_dict['links'][link_id]['num_tos_metrics'] = \
                    int(m.groupdict()['num'])
                continue

            # Opaque Type: 1
            m = p22.match(line)
            if m:
                opaque_type = int(m.groupdict()['type'])
                continue
            
            # Opaque ID: 38
            m = p23.match(line)
            if m:
                opaque_id = int(m.groupdict()['id'])
                continue

            # Fragment number: 0
            m = p24.match(line)
            if m:
                header_dict['fragment_number'] = int(m.groupdict()['num'])
                continue

            # MPLS TE router ID : 10.4.1.1
            m = p25.match(line)
            if m:
                db_dict['mpls_te_router_id'] = str(m.groupdict()['mpls'])
                continue

            # AS Boundary Router
            m = p26_1.match(line)
            if m:
                header_dict['as_boundary_router'] = True
                continue

            # Area Border Router
            m = p26_2.match(line)
            if m:
                header_dict['area_border_router'] = True
                continue

            # Link connected to Broadcast network
            m = p27.match(line)
            if m:
                link_tlv_counter += 1
                if 'link_tlvs' not in db_dict:
                    db_dict['link_tlvs'] = {}
                if link_tlv_counter not in db_dict['link_tlvs']:
                    db_dict['link_tlvs'][link_tlv_counter] = {}

                # Set link type
                opaque_link = str(m.groupdict()['link']).lower()
                if opaque_link == 'broadcast network':
                    opaque_link_type = 2
                else:
                    opaque_link_type = 1
                db_dict['link_tlvs'][link_tlv_counter]\
                    ['link_type'] = opaque_link_type
                db_dict['link_tlvs'][link_tlv_counter]\
                    ['link_name'] = opaque_link
                
                # Set remote_if_ipv4_addrs (if needed)
                if opaque_link_type == 2:
                    if 'remote_if_ipv4_addrs' not in db_dict['link_tlvs']\
                            [link_tlv_counter]:
                        db_dict['link_tlvs'][link_tlv_counter]\
                            ['remote_if_ipv4_addrs'] = {}
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['remote_if_ipv4_addrs']['0.0.0.0'] = {}
                continue

            # Link ID : 10.1.4.4
            m = p28.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['link_id'] = \
                    str(m.groupdict()['id'])
                continue

            # Interface Address : 10.1.4.1
            m = p29.match(line)
            if m:
                addr = str(m.groupdict()['addr'])
                if 'local_if_ipv4_addrs' not in db_dict['link_tlvs']\
                        [link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['local_if_ipv4_addrs'] = {}
                if addr not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['local_if_ipv4_addrs']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['local_if_ipv4_addrs'][addr] = {}
                    continue

            # Admin Metric : 1
            m = p30.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['te_metric'] = \
                    int(m.groupdict()['te_metric'])
                continue

            # Maximum Bandwidth : 125000000
            # Maximum bandwidth : 125000000
            m = p31.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['max_bandwidth'] = \
                    int(m.groupdict()['max_band'])
                continue

            # Maximum reservable bandwidth : 93750000
            # Maximum reservable bandwidth global: 93750000
            m = p32.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]\
                    ['max_reservable_bandwidth'] = \
                    int(m.groupdict()['max_res_band'])
                continue

            # Affinity Bit : 0x0
            m = p33.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['admin_group'] = \
                    str(m.groupdict()['admin_group'])
                continue

            # IGP Metric : 1
            m = p33_1.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['igp_metric'] = \
                    int(m.groupdict()['igp_metric'])
                continue

            # Number of Priority : 8
            m = p33_2.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['total_priority'] = \
                    int(m.groupdict()['num'])
                continue
            
            # Priority 0 : 93750000    Priority 1 : 93750000
            m = p34.match(line)
            if m:
                value1 = '{} {}'.format(str(m.groupdict()['num1']), str(m.groupdict()['band1']))
                value2 = '{} {}'.format(str(m.groupdict()['num2']), str(m.groupdict()['band2']))
                if 'unreserved_bandwidths' not in db_dict['link_tlvs']\
                        [link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'] = {}
                if value1 not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value1] = {}
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value1]['priority'] = \
                        int(m.groupdict()['num1'])
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value1]\
                        ['unreserved_bandwidth'] = int(m.groupdict()['band1'])
                if value2 not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value2] = {}
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value2]['priority'] = \
                            int(m.groupdict()['num2'])
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value2]\
                        ['unreserved_bandwidth'] = int(m.groupdict()['band2'])
                    continue

            # Unknown Sub-TLV   :  Type = 32770, Length = 4 Value = 00 00 00 01
            m = p35.match(line)
            if m:
                unknown_tlvs_counter += 1
                if 'unknown_tlvs' not in db_dict['link_tlvs'][link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs'] = {}
                if unknown_tlvs_counter not in db_dict['link_tlvs']\
                        [link_tlv_counter]['unknown_tlvs']:
                    db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                        [unknown_tlvs_counter] = {}
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['type'] = int(m.groupdict()['type'])
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['length'] = int(m.groupdict()['length'])
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['value'] = str(m.groupdict()['value'])
                continue

            # Extended Administrative Group : Length: 8
            m = p36.match(line)
            if m:
                if 'extended_admin_group' not in db_dict['link_tlvs']\
                        [link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['extended_admin_group'] = {}
                db_dict['link_tlvs'][link_tlv_counter]['extended_admin_group']\
                    ['length'] = int(m.groupdict()['eag_length'])
                continue

            # EAG[0]: 0
            m = p37.match(line)
            if m:
                group_num = int(m.groupdict()['group_num'])
                if 'groups' not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['extended_admin_group']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['extended_admin_group']['groups'] = {}
                if group_num not in db_dict['link_tlvs'][link_tlv_counter]\
                    ['extended_admin_group']['groups']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['extended_admin_group']['groups'][group_num] = {}
                db_dict['link_tlvs'][link_tlv_counter]['extended_admin_group']\
                    ['groups'][group_num]['value'] = int(m.groupdict()['val'])
                continue

            # Neighbor Address : 192.168.220.2
            m = p38.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['remote_if_ipv4_addrs'] = {m.groupdict()['neighbor_address']: {}}
                
                continue

            # TLV Type: Extended Link
            # TLV Type: Segment Routing Node MSD
            m = p39.match(line)
            if m:
                tlv_type_flag = True
                sub_tlv_type_flag = False

                group = m.groupdict()
                tlv_type = group['tlv_type']
                
                # Router Information
                if p39_1.match(tlv_type):
                    tlv_type_field = 'router_capabilities_tlv'

                # Segment Routing Algorithm
                elif p39_2.match(tlv_type):
                    tlv_type_field = 'sr_algorithm_tlv'

                # Segment Routing Range
                elif p39_3.match(tlv_type):
                    tlv_type_field = 'sid_range_tlvs'

                # Segment Routing Node MSD
                elif p39_4.match(tlv_type):
                    tlv_type_field = 'node_msd_tlvs'

                # Segment Routing Local Block
                elif p39_5.match(tlv_type):
                    tlv_type_field = 'local_block_tlvs'

                # Extended Prefix
                elif p39_6.match(tlv_type):
                    tlv_type_field = 'extended_prefix_tlvs'

                # Extended Link
                elif p39_7.match(tlv_type):
                    tlv_type_field = 'extended_link_tlvs'
                
                tlv_types_index = db_dict.get(tlv_type_field, {}).keys()

                if tlv_types_index:
                    index = max(tlv_types_index) + 1
                else:
                    index = 1
                
                tlv_type_dict = db_dict\
                    .setdefault(tlv_type_field, {})\
                    .setdefault(index, {})

                tlv_type_dict['tlv_type'] = tlv_type

                continue

            if 'Capabilities' in line:                
                capabilities_flag = True
                continue

            if capabilities_flag:

                if not line:
                    capabilities_flag = False
                    continue
                capability_field = None

                # Graceful Restart Helper
                if p55.match(line):
                    capability_field = 'graceful_restart_helper'

                # Stub Router Support
                elif p56.match(line):
                    capability_field = 'stub_router'

                if not capability_field:
                    continue

                capabilities_dict = tlv_type_dict\
                    .setdefault('information_capabilities', {})                    

                capabilities_dict[capability_field] = True

                continue

            # Algorithm: SPF
            # Algorithm: Strict SPF
            m = p40.match(line)
            if m:
                group = m.groupdict()
                algorithm = group['algorithm']
                algorithm = algorithm.strip()

                if sub_tlv_type_flag:
                    sub_tlv_types_dict['algo'] = algorithm
                    continue

                algo_field = None

                # SPF
                if p57.match(algorithm):
                    algo_field = 'spf'

                # Strict SPF
                if p58.match(algorithm):
                    algo_field = 'strict_spf'

                if not algo_field:
                    continue

                algorithm_dict = tlv_type_dict.setdefault('algorithm', {})
                algorithm_dict[algo_field] = True

                continue

            # Range Size: 1000
            m = p41.match(line)
            if m:
                group = m.groupdict()
                range_size = group['range_size']
                tlv_type_dict['range_size'] = int(range_size)

                continue

            # Flags  : L-Bit, V-bit
            m = p42.match(line)
            if m:
                group = m.groupdict()
                flags = group['flags']

                if sub_tlv_type_flag:
                    sub_tlv_types_dict['flags'] = flags
                    continue 

                tlv_type_dict['flags'] = flags

                continue

            # Weight : 0
            m = p44.match(line)
            if m:                
                group = m.groupdict()
                weight = int(group['weight'])

                if sub_tlv_type_flag:
                    sub_tlv_types_dict['weight'] = weight
                    continue

                tlv_type_dict['weight'] = weight

                continue

            # Label  : 19
            m = p45.match(line)
            if m:
                group = m.groupdict()
                label = group['label']

                sub_tlv_types_dict['label'] = int(label)                                

                continue

            # (Link Data) Interface IP address: 192.168.220.1
            m = p46.match(line)
            if m:
                group = m.groupdict()
                tlv_type_dict['link_data'] = group['link_data']

                continue

            # Prefix    : 10.4.1.1/32
            m = p47.match(line)
            if m:
                group = m.groupdict()
                prefix = group['prefix']

                tlv_type_dict['prefix'] = prefix

                continue

            # AF        : 0
            m = p48.match(line)
            if m:
                group = m.groupdict()
                af = int(group['af'])

                tlv_type_dict['af'] = af

                continue

            # Route-type: Intra
            m = p49.match(line)
            if m:
                group = m.groupdict()
                route_type = group['route_type']            

                tlv_type_dict['route_type'] = route_type

                continue

            # Sub-TLV Type: Remote Intf Addr
            # Sub-TLV Type: Local / Remote Intf ID
            m = p50.match(line)
            if m:
                tlv_type_flag = False
                sub_tlv_type_flag = True
                group = m.groupdict()
                sub_tlv_type = group['sub_tlv_type']

                sub_tlv_types_index = tlv_type_dict.get('sub_tlvs', {}).keys()
                if sub_tlv_types_index:
                    index = max(sub_tlv_types_index) + 1
                else:
                    index = 1

                sub_tlv_types_dict = tlv_type_dict.setdefault('sub_tlvs', {}).setdefault(index, {})
                sub_tlv_types_dict['type'] = sub_tlv_type
                if sub_tlv_temp:
                    for i in sub_tlv_temp:
                        sub_tlv_types_dict.update(i)
                    sub_tlv_temp.clear()
                continue

            # Remote Interface Address   : 192.168.0.1
            m = p51.match(line)
            if m:
                group = m.groupdict()
                remote_interface_address = group['remote_interface_address']
                sub_tlv_types_dict['remote_interface_address'] = remote_interface_address
                continue

            # Local Interface ID   : 20
            m = p52.match(line)
            if m:
                group = m.groupdict()
                local_interface_id = int(group['local_interface_id'])
                try:
                    sub_tlv_types_dict['local_interface_id'] = local_interface_id
                except UnboundLocalError:
                    sub_tlv_temp.append({'local_interface_id': local_interface_id})

                continue            

            # Remote Interface ID   : 20
            m = p53.match(line)
            if m:
                group = m.groupdict()
                remote_interface_id = int(group['remote_interface_id'])
                try:
                    sub_tlv_types_dict['remote_interface_id'] = remote_interface_id
                except UnboundLocalError:
                    sub_tlv_temp.append({'remote_interface_id': remote_interface_id})

                continue

            # SID   : 1
            m = p54.match(line)                        
            if m:
                group = m.groupdict()
                sid = int(group['sid'])

                sub_tlv_types_dict['sid'] = sid
                continue

            # Sub-type: Node Max Sid Depth, Value: 13
            m = p59.match(line)
            if m:
                group = m.groupdict()
                sub_type_value = int(group['value'])

                sub_type_dict = tlv_type_dict.setdefault('sub_type', {})
                sub_type_dict['node_max_sid_depth_value'] = sub_type_value

                continue

        return ret_dict


# ==================================
# Schema for:
#   * 'show ip ospf database router'
# ==================================
class ShowIpOspfDatabaseRouterSchema(MetaParser):

    ''' Schema for:
        * show ip ospf database router'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {Optional('areas'): 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    Optional('routing_bit_enable'): bool,
                                                                    Optional('as_boundary_router'): bool,
                                                                    Optional('area_border_router'): bool,
                                                                    },
                                                                'body': 
                                                                    {'router': 
                                                                        {Optional('flags'): str,
                                                                        'num_of_links': int,
                                                                        Optional('links'):
                                                                            {Any(): 
                                                                                {'link_id': str,
                                                                                'link_data': str,
                                                                                'type': str,
                                                                                Optional('num_mtid_metrics'): int,
                                                                                Optional('num_tos_metrics'): int,
                                                                                'topologies': 
                                                                                    {Any(): 
                                                                                        {'mt_id': int,
                                                                                        Optional('metric'): int,
                                                                                        Optional('tos'): int,
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


# ==================================
# Parser for:
#   * 'show ip ospf database router'
# ==================================
class ShowIpOspfDatabaseRouter(ShowIpOspfDatabaseRouterSchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database router'
    '''

    cli_command = 'show ip ospf database router'
    exclude = ['age', 'seq_num', 'checksum', 'links']


    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(db_type='router', out=output)


# ====================================
# Schema for:
#   * 'show ip ospf database external'
# ====================================
class ShowIpOspfDatabaseExternalSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf database external'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {Optional('areas'): 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    Optional('routing_bit_enable'): bool,
                                                                    },
                                                                'body': 
                                                                    {'external': 
                                                                        {'network_mask': str,
                                                                        'topologies': 
                                                                            {Any(): 
                                                                                {'mt_id': int,
                                                                                Optional('flags'): str,
                                                                                Optional('metric_type'): int,
                                                                                'metric': int,
                                                                                'forwarding_address': str,
                                                                                'external_route_tag': int},
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
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ====================================
# Parser for:
#   * 'show ip ospf database external'
# ====================================
class ShowIpOspfDatabaseExternal(ShowIpOspfDatabaseExternalSchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database external'
    '''

    cli_command = 'show ip ospf database external'

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(db_type='external', out=output)


# ===================================
# Schema for:
#   * 'show ip ospf database network'
# ===================================
class ShowIpOspfDatabaseNetworkSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf database network'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {Optional('areas'): 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    Optional('routing_bit_enable'): bool,
                                                                    },
                                                                'body': 
                                                                    {'network': 
                                                                        {'network_mask': str,
                                                                        'attached_routers': 
                                                                            {Any(): {},
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
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ===================================
# Parser for:
#   * 'show ip ospf database network'
# ===================================
class ShowIpOspfDatabaseNetwork(ShowIpOspfDatabaseNetworkSchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database network'
    '''

    cli_command = 'show ip ospf database network'
    exclude = ['age', 'seq_num', 'checksum', 'lsas']

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(db_type='network', out=output)


# ===================================
# Schema for:
#   * 'show ip ospf database summary'
# ===================================
class ShowIpOspfDatabaseSummarySchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf database summary'
    '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {Optional('areas'): 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    Optional('routing_bit_enable'): bool,
                                                                    },
                                                                'body': 
                                                                    {'summary': 
                                                                        {'network_mask': str,
                                                                        'topologies': 
                                                                            {Any(): 
                                                                                {'mt_id': int,
                                                                                'metric': int},
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
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ===================================
# Parser for:
#   * 'show ip ospf database summary'
# ===================================
class ShowIpOspfDatabaseSummary(ShowIpOspfDatabaseSummarySchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database summary'
    '''

    cli_command = 'show ip ospf database summary'
    exclude = ['age', 'seq_num', 'checksum']


    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(db_type='summary', out=output)


# =======================================
# Schema for:
#   * 'show ip ospf database opaque-area'
# =======================================
class ShowIpOspfDatabaseOpaqueAreaSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf database opaque-area'
        * 'show ip ospf database opaque-area self-originate'
    '''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                Optional('areas'): {
                                    Any(): {
                                        'database': {
                                            'lsa_types': {
                                                Any(): {
                                                    'lsa_type': int,
                                                    'lsas': {
                                                        Any(): {
                                                            'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': {
                                                                'header': {
                                                                    'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    Optional('opaque_type'): int,
                                                                    'opaque_id': int,
                                                                    Optional('fragment_number'): int,
                                                                },
                                                                'body': {
                                                                    'opaque': {
                                                                        Optional('mpls_te_router_id'): str,
                                                                        Optional('links'): {
                                                                            Any(): {
                                                                                'link_id': str,
                                                                                'topologies': {
                                                                                    Any(): {
                                                                                        'mt_id': int
                                                                                    }
                                                                                },
                                                                            }
                                                                        },
                                                                        Optional('num_of_links'): int,                                                                        
                                                                        Optional('router_capabilities_tlv'): {
                                                                            Any(): {
                                                                                'length': int,
                                                                                'tlv_type': str,
                                                                                Optional('information_capabilities'): {
                                                                                    Optional('graceful_restart'): bool,       
                                                                                    Optional('graceful_restart_helper'): bool,
                                                                                    Optional('stub_router'): bool,            
                                                                                    Optional('traffic_enginnering'): bool,    
                                                                                    Optional('p2p_over_lan'): bool,           
                                                                                    Optional('experimental_te'): bool,
                                                                                }
                                                                            }
                                                                        },
                                                                        Optional('sr_algorithm_tlv'): {
                                                                            Any(): {
                                                                                'tlv_type': str,
                                                                                'length': int,
                                                                                Optional('algorithm'): {
                                                                                    Optional('spf'): bool,
                                                                                    Optional('strict_spf'): bool,
                                                                                }
                                                                            }
                                                                        },
                                                                        Optional('sid_range_tlvs'): {
                                                                            Any(): {
                                                                                'tlv_type': str,
                                                                                'length': int,
                                                                                'range_size': int,
                                                                                'sub_tlvs': {
                                                                                    Any(): { 
                                                                                        'type': str,
                                                                                        'length': int,
                                                                                        'label': int,
                                                                                        Optional('local_interface_id'): int,
                                                                                        Optional('remote_interface_id'): int,
                                                                                    }
                                                                                }
                                                                            }
                                                                        },
                                                                        Optional('node_msd_tlvs'): {
                                                                            Any(): {
                                                                                'tlv_type': str,
                                                                                'length': int,
                                                                                'sub_type': {
                                                                                    'node_max_sid_depth_value': int
                                                                                }
                                                                            }
                                                                        },
                                                                        Optional('local_block_tlvs'): {
                                                                            Any(): {
                                                                                'tlv_type': str,
                                                                                'range_size': int,
                                                                                'length': int,
                                                                                'sub_tlvs': {
                                                                                    Any(): {
                                                                                        'type': str,
                                                                                        'length': int,
                                                                                        'label': int
                                                                                    }
                                                                                }
                                                                            }
                                                                        },
                                                                        Optional('extended_prefix_tlvs'): {
                                                                            Any(): {
                                                                                'tlv_type': str,
                                                                                'route_type': str,
                                                                                'length': int,
                                                                                'flags': str,
                                                                                'prefix': str,
                                                                                'af': int,
                                                                                Optional('sub_tlvs'): {
                                                                                    Any(): {
                                                                                        'type': str,
                                                                                        'length': int,
                                                                                        'flags': str,
                                                                                        Optional('mt_id'): int,
                                                                                        'algo': str,
                                                                                        'sid': int,
                                                                                    }
                                                                                }

                                                                            }
                                                                        },
                                                                        Optional('extended_link_tlvs'): {
                                                                            Any(): {
                                                                                'link_id': str,
                                                                                'link_data': str,
                                                                                'length': int,
                                                                                Optional('link_name'): str,
                                                                                'link_type': int,
                                                                                'tlv_type': str,
                                                                                'sub_tlvs': {
                                                                                    Any(): {
                                                                                        'type': str,
                                                                                        Optional('length'): int,
                                                                                        Optional('flags'): str,
                                                                                        Optional('mt_id'): int,
                                                                                        Optional('weight'): int,
                                                                                        Optional('label'): int,
                                                                                        Optional('remote_interface_address'): str,
                                                                                        Optional('local_interface_id'): int,
                                                                                        Optional('remote_interface_id'): int,
                                                                                    }
                                                                                }
                                                                            }
                                                                        },
                                                                        Optional('link_tlvs'): {
                                                                            Any(): {
                                                                                Optional('link_type'): int,
                                                                                Optional('link_name'): str,
                                                                                Optional('link_id'): str,
                                                                                Optional('te_metric'): int,
                                                                                Optional('max_bandwidth'): int,
                                                                                Optional('max_reservable_bandwidth'): int,
                                                                                Optional('admin_group'): str,
                                                                                Optional('igp_metric'): int,
                                                                                Optional('total_priority'): int,
                                                                                Optional('local_if_ipv4_addrs'): {
                                                                                    Any(): {}
                                                                                },
                                                                                Optional('remote_if_ipv4_addrs'): {
                                                                                    Any(): {}
                                                                                },
                                                                                Optional('unreserved_bandwidths'): {
                                                                                    Any(): {
                                                                                        'priority': int,
                                                                                        'unreserved_bandwidth': int,
                                                                                    }
                                                                                },
                                                                                Optional('unknown_tlvs'): {
                                                                                    Any(): {
                                                                                        'type': int,
                                                                                        'length': int,
                                                                                        'value': str,
                                                                                    }
                                                                                },
                                                                                Optional('extended_admin_group'): {
                                                                                    'length': int,
                                                                                    Optional('groups'): {
                                                                                        Any(): {
                                                                                            'value': int
                                                                                        }
                                                                                    },
                                                                                },
                                                                            }
                                                                        },
                                                                    }
                                                                },
                                                            },
                                                        }
                                                    },
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



# =======================================
# Parser for:
#   * 'show ip ospf database opaque-area'
# =======================================
class ShowIpOspfDatabaseOpaqueArea(ShowIpOspfDatabaseOpaqueAreaSchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database opaque-area'
    '''

    cli_command = 'show ip ospf database opaque-area'

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(db_type='opaque', out=output)



# =================================================
# Parser for:
#   * 'show ip ospf database router self-originate'
# =================================================
class ShowIpOspfDatabaseRouterSelfOriginate(ShowIpOspfDatabaseRouterSchema, ShowIpOspfDatabaseTypeParser):

    ''' Parser for:
        * 'show ip ospf database router self-originate'
    '''

    cli_command = 'show ip ospf database router self-originate'
    exclude = ['age' , 'checksum', 'seq_num', 'dead_time']

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(db_type='router', out=output)




class ShowIpOspfDatabaseOpaqueAreaSelfOriginate(ShowIpOspfDatabaseOpaqueAreaSchema, ShowIpOspfDatabaseTypeParser):
    ''' Parser for:
        * 'show ip ospf database opaque-area self-originate'
    '''

    cli_command = ['show ip ospf database opaque-area {lsa_id} self-originate', 
                   'show ip ospf database opaque-area self-originate']

    def cli(self, lsa_id=None, output=None):
        if output is None:
            if lsa_id:
                output = self.device.execute(self.cli_command[0].format(lsa_id=lsa_id))
            else:
                output = self.device.execute(self.cli_command[1])

        return super().cli(db_type='opaque', out=output)

class ShowIpOspfDatabaseOpaqueAreaAdvRouter(ShowIpOspfDatabaseOpaqueAreaSchema, ShowIpOspfDatabaseTypeParser):
    ''' Parser for:
        * 'show ip ospf database opaque-area adv-router {address}'
    '''

    cli_command = 'show ip ospf database opaque-area adv-router {address}'

    def cli(self, address, output=None):
        if not output:
            output = self.device.execute(self.cli_command.format(address=address))

        return super().cli(db_type='opaque', out=output)

class ShowIpOspfDatabaseOpaqueAreaTypeExtLink(ShowIpOspfDatabaseOpaqueAreaSchema, ShowIpOspfDatabaseTypeParser):
    """ Parser for:
            * show ip ospf database opaque-area type ext-link
    """
    cli_command = 'show ip ospf database opaque-area type ext-link'

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(db_type='opaque', out=output)

class ShowIpOspfDatabaseOpaqueAreaTypeExtLinkSelfOriginate(ShowIpOspfDatabaseOpaqueAreaSchema, ShowIpOspfDatabaseTypeParser):
    """ Parser for:
            * show ip ospf database opaque-area type ext-link self-originate
    """
    cli_command = 'show ip ospf database opaque-area type ext-link self-originate'

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(db_type='opaque', out=output)

class ShowIpOspfDatabaseOpaqueAreaTypeExtLinkAdvRouter(ShowIpOspfDatabaseOpaqueAreaSchema, ShowIpOspfDatabaseTypeParser):
    """ Parser for:
            * show ip ospf database opaque-area type ext-link adv-router {address}
    """
    cli_command = 'show ip ospf database opaque-area type ext-link adv-router {address}'

    def cli(self, address, output=None):
        if not output:
            output = self.device.execute(self.cli_command.format(address=address))

        return super().cli(db_type='opaque', out=output)

class ShowIpOspfDatabaseOpaqueAreaTypeTrafficEngineeringSelfOriginate(ShowIpOspfDatabaseOpaqueAreaSchema, ShowIpOspfDatabaseTypeParser):
    """ Parser for:
            * show ip ospf database opaque-area type traffic-engineering self-originate
    """
    cli_command = 'show ip ospf database opaque-area type traffic-engineering self-originate'

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command)

        return super().cli(db_type='opaque', out=output)


# =================================================================
# Schema for:
#   * 'show ip ospf database database-summary detail'
#   * 'show ip ospf {process_id }database database-summary detail'
# =================================================================

class ShowIpOspfDatabaseSummaryDetailSchema(MetaParser):

    ''' Schema for:
        * 'show ip ospf database database-summary detail'
        * 'show ip ospf {process_id} database database-summary detail'
    '''

    schema = {
        'vrf':{
            Any():{
                'instance':{
                    Any():{
                        Any():{
                            'router':{
                                'count': int,
                                'delete': int,
                                'maxage': int,
                            },
                            'network':{
                                'count': int,
                                'delete': int,
                                'maxage': int,
                            },
                            'summary_net':{
                                'count': int,
                                'delete': int,
                                'maxage': int,
                            },
                            'summary_asbr':{
                                'count': int,
                                'delete': int,
                                'maxage': int,
                            },
                            'type_5_ext':{
                                'count': int,
                                'delete': int,
                                'maxage': int,
                            },
                            'type_7_ext':{
                                'count': int,
                                'delete': int,
                                'maxage': int,
                            },
                            'opaque_link':{
                                'count': int,
                                'delete': int,
                                'maxage': int,
                            },
                            'opaque_area':{
                                'count': int,
                                'delete': int,
                                'maxage': int,
                            },
                            'opaque_as':{
                                'count': int,
                                'delete': int,
                                'maxage': int,
                            },
                            'total':{
                                'count': int,
                                'delete': int,
                                'maxage': int,
                            },
                        },
                    },            
                },
            },
        },
    }        

# ================================================================
# Parser for:
#   * 'show ip ospf database database-summary detail'
#   * 'show ip ospf {process_id} database database-summary detail'
# ================================================================
class ShowIpOspfDatabaseSummaryDetail(ShowIpOspfDatabaseSummaryDetailSchema):

    ''' Parser for:
        * 'show ip ospf database database-summary detail'
        * "show ip ospf {process_id} database database-summary detail"
    '''

    cli_command = ['show ip ospf database database-summary detail', 'show ip ospf {process_id} database database-summary detail']

    def cli(self, process_id=None, output=None):

        if not output:
            if process_id:
                output = self.device.execute(self.cli_command[1].format(process_id=process_id))
            else:
                output = self.device.execute(self.cli_command[0])

        # Init variables
        ret_dict = {}
        vrf = 'default'

        # OSPF Router with ID (10.36.3.3) (Process ID 1)
        # OSPF Router with ID (20.3.5.6) (Process ID 2, VRF VRF1)
        p0 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\) +\(Process +ID +(?P<instance>(\d+))'
                        r'(?:, +VRF +(?P<vrf>(\S+)))?\)$')

        # Router 22.22.22.22 LSA summary
        p1 = re.compile('^Router +(?P<router_ip>(\S+)) +LSA +summary$')

        #LSA Type      Count    Delete   Maxage
        #Router        2        0        0
        #Network       2        0        0
        #Summary Net   2        0        0
        #Summary ASBR  2        0        0
        #Type-5 Ext    0        0        0
        #Type-7 Ext    0        0        0
        #Opaque Link   0        0        0
        #Opaque Area   0        0        0
        #Opaque AS     0        0        0
        #Total         8        0        0
        
        p2 = re.compile(r'^(?P<lsa_type>(Router|Network|Summary Net|Summary ASBR|'
                r'Type-5 Ext|Type-7 Ext|Opaque Link|Opaque Area|Opaque AS|Total))'
                r' +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+))')

        for line in output.splitlines():
            line = line.strip()
            m = p0.match(line)
            if m:
                group = m.groupdict()
                instance = str(group['instance'])
                if group['vrf']:
                    vrf = str(group['vrf'])
                else:
                    vrf = 'default'

                ospf_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('instance', {}).setdefault(instance, {})
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                item = group['router_ip']
                lsa_dict = ospf_dict.setdefault(item, {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                lsa_type = group['lsa_type'].strip().lower().replace(" ", "_").replace("-", "_")
                tmp_dict = lsa_dict.setdefault(lsa_type, {})
                tmp_dict['count'] = int(group['count'])
                tmp_dict['delete'] = int(group['delete'])
                tmp_dict['maxage'] = int(group['maxage'])
        
        return ret_dict

# ====================
# Schema for:
#  * 'show ip ospf database database-summary'
# ====================
class ShowIpOspfDatabaseDatabaseSummarySchema(MetaParser):
    ''' Schema for "show ip ospf database database-summary" '''

    schema = {
        Optional('instance'): {
            Any(): {    # OSPF PID
                'router_id': str,
                'area_summary': {
                    Any(): {     # Area Num
                        'router': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'network': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'summary_net': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'summary_asbr': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'type_7_ext': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'prefixes_redist_type_7': int,
                        'opaque_link': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'opaque_area': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'subtotal': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                    }   
                },
                'process_summary': {
                    Any(): {         # OSPF PID
                        'router': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'network': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'summary_net': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'summary_asbr': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'type_7_ext': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'opaque_link': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'opaque_area': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'type_5_ext': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'prefixes_redist_type_5': int,
                        'opaque_as': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'total': {
                            'count': int,
                            'delete': int,
                            'maxage': int
                        },
                        'non_self': int
                    }   
                }
            }
        }
    }



# ====================
# Parser for:
#  * 'show ip ospf database database-summary'
# ====================
class ShowIpOspfDatabaseDatabaseSummary(ShowIpOspfDatabaseDatabaseSummarySchema):
    ''' Parser for "show ip ospf database database-summary" '''

    #                 OSPF Router with ID (192.168.0.1) (Process ID 1)

    # Area 0 database summary
    #   LSA Type      Count    Delete   Maxage
    #   Router        0        0        0       
    #   Network       0        0        0       
    #   Summary Net   0        0        0       
    #   Summary ASBR  0        0        0       
    #   Type-7 Ext    0        0        0       
    #     Prefixes redistributed in Type-7  0
    #   Opaque Link   0        0        0       
    #   Opaque Area   0        0        0       
    #   Subtotal      0        0        0       

    # Area 1 database summary
    #   LSA Type      Count    Delete   Maxage
    #   Router        0        0        0       
    #   Network       0        0        0       
    #   Summary Net   0        0        0       
    #   Summary ASBR  0        0        0       
    #   Type-7 Ext    0        0        0       
    #     Prefixes redistributed in Type-7  0
    #   Opaque Link   0        0        0       
    #   Opaque Area   0        0        0       
    #   Subtotal      0        0        0       

    # Process 1 database summary
    #   LSA Type      Count    Delete   Maxage
    #   Router        0        0        0       
    #   Network       0        0        0       
    #   Summary Net   0        0        0       
    #   Summary ASBR  0        0        0       
    #   Type-7 Ext    0        0        0       
    #   Opaque Link   0        0        0       
    #   Opaque Area   0        0        0       
    #   Type-5 Ext    0        0        0       
    #       Prefixes redistributed in Type-5  0
    #   Opaque AS     0        0        0       
    #   Total         0        0        0       
    #   Non-self      0       

    #             OSPF Router with ID (102.102.102.102) (Process ID 202)

    # Area 0 database summary
    #   LSA Type      Count    Delete   Maxage
    #   Router        2        0        0       
    #   Network       1        0        0       
    #   Summary Net   2        0        0       
    #   Summary ASBR  0        0        0       
    #   Type-7 Ext    0        0        0       
    #     Prefixes redistributed in Type-7  0
    #   Opaque Link   0        0        0       
    #   Opaque Area   0        0        0       
    #   Subtotal      5        0        0       

    # Area 1 database summary
    #   LSA Type      Count    Delete   Maxage
    #   Router        2        0        0       
    #   Network       1        0        0       
    #   Summary Net   2        0        0       
    #   Summary ASBR  0        0        0       
    #   Type-7 Ext    0        0        0       
    #     Prefixes redistributed in Type-7  0
    #   Opaque Link   0        0        0       
    #   Opaque Area   0        0        0       
    #   Subtotal      5        0        0       

    # Process 202 database summary
    #   LSA Type      Count    Delete   Maxage
    #   Router        4        0        0       
    #   Network       2        0        0       
    #   Summary Net   4        0        0       
    #   Summary ASBR  0        0        0       
    #   Type-7 Ext    0        0        0       
    #   Opaque Link   0        0        0       
    #   Opaque Area   0        0        0       
    #   Type-5 Ext    0        0        0       
    #       Prefixes redistributed in Type-5  0
    #   Opaque AS     0        0        0       
    #   Total         10       0        0       
    #   Non-self      3       

    cli_command = 'show ip ospf database database-summary'

    # Define a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # Define RegExes for each possible kind of line

        #                 OSPF Router with ID (192.168.0.1) (Process ID 1)
        p1 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\) +\(Process +ID +(?P<ospf_pid>(\d+))\)$')

        # Area 0 database summary
        p2 = re.compile(r'^Area +(?P<area_no>(\d+)) +database +summary$')

        #   Router        0        0        0 
        p3 = re.compile(r'^Router +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        #   Network       0        0        0       
        p4 = re.compile(r'^Network +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        #   Summary Net   0        0        0       
        p5 = re.compile(r'^Summary +Net +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        #   Summary ASBR  0        0        0       
        p6 = re.compile(r'^Summary +ASBR +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        #   Type-7 Ext    0        0        0       
        p7 = re.compile(r'^Type-7 +Ext +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        #     Prefixes redistributed in Type-7  0
        p8 = re.compile(r'^Prefixes +redistributed +in +Type-7 +(?P<prefixes_redist_type_7>(\d+))$')

        #   Opaque Link   0        0        0       
        p9 = re.compile(r'^Opaque +Link +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        #   Opaque Area   0        0        0       
        p10 = re.compile(r'^Opaque +Area +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        #   Subtotal      0        0        0       
        p11 = re.compile(r'^Subtotal +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        # Process 1 database summary
        p12 = re.compile(r'^Process +(?P<ospf_pid>(\d+)) +database +summary$')
  
        #   Type-5 Ext    0        0        0      
        p13 = re.compile(r'^Type-5 +Ext +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        #       Prefixes redistributed in Type-5  0
        p14 = re.compile(r'^Prefixes +redistributed +in +Type-5 +(?P<prefixes_redist_type_5>(\d+))$')

        #   Opaque AS     0        0        0       
        p15 = re.compile(r'^Opaque +AS +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        #   Total         0        0        0       
        p16 = re.compile(r'^Total +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+)) *$')

        #   Non-self      0   
        p17 = re.compile(r'^Non-self +(?P<non_self_count>(\d+)) *$')


        area_summary_update = False
        process_summary_update = False

        ospf_instance_dict = None
        ospf_area_summary_dict = None
        ospf_process_summary_dict = None


        # Iterate over output lines to check which pattern is matched

        for line in output.splitlines():
            line = line.strip()

            # Try matching pattern 1
            #                 OSPF Router with ID (192.168.0.1) (Process ID 1)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf_instance_dict = parsed_dict.setdefault("instance",{}).setdefault(group["ospf_pid"],{})
                ospf_instance_dict.update({
                    'router_id': group["router_id"],
                    'area_summary': {},
                    'process_summary': {}
                })
                continue

            # Try matching pattern 2
            # Area 0 database summary
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_area_summary_dict = ospf_instance_dict['area_summary'].setdefault(group["area_no"],{})
                area_summary_update = True
                process_summary_update = False
                ospf_area_summary_dict.update({
                    'router': None,
                    'network': None,
                    'summary_net': None,
                    'summary_asbr': None,
                    'type_7_ext': None,
                    'prefixes_redist_type_7': None,
                    'opaque_link': None,
                    'opaque_area': None,
                    'subtotal': None
                })
                continue

            # Try matching pattern 3
            #   Router        0        0        0 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if area_summary_update==True:
                    ospf_area_summary_dict.update({
                        'router': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })
                elif process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'router': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })

                continue

            # Try matching pattern 4
            #   Network       0        0        0       
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if area_summary_update==True:
                    ospf_area_summary_dict.update({
                        'network': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })
                elif process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'network': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })

                continue

            # Try matching pattern 5
            #   Summary Net   0        0        0       
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if area_summary_update==True:
                    ospf_area_summary_dict.update({
                        'summary_net': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })
                elif process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'summary_net': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })

                continue

            # Try matching pattern 6
            #   Summary ASBR  0        0        0       
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if area_summary_update==True:
                    ospf_area_summary_dict.update({
                        'summary_asbr': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })
                elif process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'summary_asbr': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })

                continue

            # Try matching pattern 7
            #   Type-7 Ext    0        0        0       
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if area_summary_update==True:
                    ospf_area_summary_dict.update({
                        'type_7_ext': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })
                elif process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'type_7_ext': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })

                continue

            # Try matching pattern 8
            #     Prefixes redistributed in Type-7  0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if area_summary_update==True:
                    ospf_area_summary_dict.update({
                        'prefixes_redist_type_7': int(group["prefixes_redist_type_7"])
                    })

                continue

            # Try matching pattern 9
            #   Opaque Link   0        0        0       
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if area_summary_update==True:
                    ospf_area_summary_dict.update({
                        'opaque_link': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })
                elif process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'opaque_link': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })

                continue

            # Try matching pattern 10
            #   Opaque Area   0        0        0       
            m = p10.match(line)
            if m:
                group = m.groupdict()
                if area_summary_update==True:
                    ospf_area_summary_dict.update({
                        'opaque_area': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })
                elif process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'opaque_area': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })

                continue

            # Try matching pattern 11
            #   Subtotal      0        0        0       
            m = p11.match(line)
            if m:
                group = m.groupdict()
                if area_summary_update==True:
                    ospf_area_summary_dict.update({
                        'subtotal': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })

                continue

            # Try matching pattern 12
            # Process 1 database summary
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ospf_process_summary_dict = ospf_instance_dict['process_summary'].setdefault(group["ospf_pid"],{})
                process_summary_update = True
                area_summary_update = False
                ospf_process_summary_dict.update({
                    'router': None,
                    'network': None,
                    'summary_net': None,
                    'summary_asbr': None,
                    'type_7_ext': None,
                    'opaque_link': None,
                    'opaque_area': None,
                    'type_5_ext': None,
                    'prefixes_redist_type_5': None,
                    'opaque_as': None,
                    'total': None,
                    'non_self': None
                })
                continue

            # Try matching pattern 13
            #   Type-5 Ext    0        0        0      
            m = p13.match(line)
            if m:
                group = m.groupdict()
                if process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'type_5_ext': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })
                continue

            # Try matching pattern 14
            #       Prefixes redistributed in Type-5  0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                if process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'prefixes_redist_type_5': int(group["prefixes_redist_type_5"])
                    })
                continue

            # Try matching pattern 15
            #   Opaque AS     0        0        0       
            m = p15.match(line)
            if m:
                group = m.groupdict()
                if process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'opaque_as': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })
                continue

            # Try matching pattern 16
            #   Total         0        0        0       
            m = p16.match(line)
            if m:
                group = m.groupdict()
                if process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'total': {
                            'count': int(group["count"]),
                            'delete': int(group["delete"]),
                            'maxage': int(group["maxage"])
                        }
                    })
                continue

            # Try matching pattern 17
            #   Non-self      0   
            m = p17.match(line)
            if m:
                group = m.groupdict()
                if process_summary_update==True:
                    ospf_process_summary_dict.update({
                        'non_self': int(group["non_self_count"])
                    })
                continue
        
            
        return parsed_dict
    



