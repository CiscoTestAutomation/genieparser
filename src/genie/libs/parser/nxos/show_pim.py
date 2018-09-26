import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.libs.parser.utils.common import Common


# ====================================================
# schema Parser for 'show ipv6 pim interface'
# ====================================================
class ShowIpv6PimInterfaceSchema(MetaParser):
    """Schema for show ipv6 pim interface"""

    schema = {
        'vrf':{
            Any():{
                'interfaces':{
                    Any():{
                        'address_family': {
                            Any(): {
                                Optional('oper_status'): str,
                                Optional('link_status'): str,
                                Optional('admin_status'): str,
                                Optional('address'): list,
                                Optional('dr_address'): str,
                                Optional('dr_priority'): int,
                                Optional('configured_dr_priority'): int,
                                Optional('neighbor_count'): int,
                                Optional('hello_interval'): int,
                                Optional('hello_expiration'): str,
                                Optional('neighbor_holdtime'): int,
                                Optional('dr_delay'): int,
                                Optional('bsr_border'): bool,
                                Optional('genid'): str,
                                Optional('hello_md5_ah_authentication'): str,
                                Optional('neighbor_filter'): str,
                                Optional('jp_inbound_policy'): str,
                                Optional('jp_outbound_policy'): str,
                                Optional('jp_interval'): int,
                                Optional('jp_next_sending'): int,
                                Optional('bfd'):{
                                    Optional('enable'): bool,
                                    },
                                Optional('sm'):{
                                    Optional('passive'): bool,
                                },
                                Optional('vpc_svi'): bool,
                                Optional('auto_enabled'): bool,
                                Optional('statistics'):{
                                    Optional('last_reset'): str,
                                    Optional('general'):{
                                        Optional('hellos'): str,
                                        Optional('jps'): str,
                                        Optional('asserts'): str,
                                        Optional('grafts'): str,
                                        Optional('graft_acks'): str,
                                        Optional('df_offers'): str,
                                        Optional('df_winners'): str,
                                        Optional('df_backoffs'): str,
                                        Optional('df_passes'): str,
                                    },
                                    Optional('errors'):{
                                        Optional('checksum'): int,
                                        Optional('invalid_packet_types'): int,
                                        Optional('invalid_df_subtypes'): int,
                                        Optional('authentication_failed'): int,
                                        Optional('packet_length_errors'): int,
                                        Optional('bad_version_packets'): int,
                                        Optional('packets_from_self'): int,
                                        Optional('packets_from_non_neighbors'): int,
                                        Optional('packets_received_on_passiveinterface'): int,
                                        Optional('jps_received_on_rpf_interface'): int,
                                        Optional('joins_received_with_no_rp'): int,
                                        Optional('joins_received_with_wrong_rp'): int,
                                        Optional('joins_received_with_ssm_groups'): int,
                                        Optional('joins_received_with_bidir_groups'): int,
                                        Optional('jps_filtered_by_inbound_policy'): int,
                                        Optional('jps_filtered_by_outbound_policy'): int,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

# ==========================================================
#  parser for show ipv6 pim interface vrf <word>
#  parser for show ipv6 pim interface
#  parser for show ipv6 pim interface <word>
#  parser for show ipv6 pim interface <word1> vrf <word2>
#
# ==========================================================
class ShowIpv6PimInterface(ShowIpv6PimInterfaceSchema):
    """Parser for:
        show ipv6 pim interface vrf <vrf>
        show ipv6 pim interface
        show ipv6 pim interface <interface>
        show ipv6 pim interface <interface> vrf <vrf>"""

    def cli(self , interface ="", vrf=""):

        if not vrf and not interface:
            cmd = 'show ipv6 pim interface'
        if not vrf and interface:
            cmd = 'show ipv6 pim interface {}'.format(interface)
        if vrf and not interface:
            cmd = 'show ipv6 pim interface vrf {}'.format(vrf)
        if vrf and interface:
            cmd = 'show ipv6 pim interface {0} vrf {1}'.format(interface, vrf)

        out = self.device.execute(cmd)
        af_name = 'ipv6'

        # Init dictionary
        parsed_dict = dict()
        address_list = []
        checksum = invalid_packet_types = invalid_df_subtypes = authentication_failed \
          = packet_length_errors = bad_version_packets = packets_from_self =\
          packets_from_non_neighbors = packets_received_on_passiveinterface = \
          jps_received_on_rpf_interface = joins_received_with_bidir_groups = \
          joins_received_with_no_rp = joins_received_with_ssm_groups = joins_received_with_wrong_rp = \
          jps_filtered_by_inbound_policy = jps_filtered_by_outbound_policy = hellos = jps = asserts = grafts\
          = graft_acks = df_backoffs = df_passes = df_winners = df_offers = ""

        oper_status = link_status = admin_status = interface_name = dr_address = bsr_border \
            = hello_md5_ah_authentication = \
            hello_interval = hello_expiration = dr_priority = configured_dr_delay = jp_next_sending = bfd\
            = jp_interval = passive = auto_enabled = genid = jp_outbound_policy = jp_inbound_policy = \
            nbr_count = neighbor_holdtime = neighbor_filter = vpc_svi =last_rest = ""

        for line in out.splitlines():
            line = line.rstrip()

            #PIM6 Interface Status for VRF "VRF1"
            p1 = re.compile(r'^\s*PIM6 +Interface +Status +for +VRF+ \"(?P<vrf>[\w]+)\"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                checksum = invalid_packet_types = invalid_df_subtypes = authentication_failed \
                = packet_length_errors = bad_version_packets = packets_from_self = \
                packets_from_non_neighbors = packets_received_on_passiveinterface = \
                jps_received_on_rpf_interface = joins_received_with_bidir_groups = \
                joins_received_with_no_rp = joins_received_with_ssm_groups = joins_received_with_wrong_rp = \
                jps_filtered_by_inbound_policy = jps_filtered_by_outbound_policy = hellos = jps = asserts = grafts \
                = graft_acks = df_backoffs = df_passes = df_winners = df_offers = ""

                oper_status = link_status = admin_status = interface_name = dr_address = bsr_border \
                    = hello_md5_ah_authentication = \
                hello_interval = hello_expiration = dr_priority = configured_dr_delay = jp_next_sending = bfd \
                = jp_interval = passive = auto_enabled = genid = jp_outbound_policy = jp_inbound_policy = \
                nbr_count = configured_dr_priority = neighbor_holdtime = neighbor_filter = vpc_svi =last_rest = ""

            # Ethernet2/2, Interface status: protocol-up/link-up/admin-up
            p2 = re.compile(r'^\s*(?P<interface_name>[\w\/\.\-]+),'
                            ' +Interface +status: +protocol\-(?P<oper_status>[\w]+)/'
                            'link\-(?P<link_status>[\w]+)/'
                            'admin\-(?P<admin_status>[\w]+)$')
            m = p2.match(line)
            if m:
                interface_name = m.groupdict()['interface_name']
                oper_status = m.groupdict()['oper_status']
                link_status = m.groupdict()['link_status']
                admin_status = m.groupdict()['admin_status']
                address_list = []

            # IPv6 address:
            #   10.11.33.11, IP subnet: 10.11.33.0/24
            p3 = re.compile(r'^\s*(?P<space>\s{4})'
                            '(?P<address>[^Error:][\w\/\:]+)( +\[VALID\])?$')
            m = p3.match(line)
            if m:
                address_list.append(m.groupdict()['address'])

            # PIM6 DR: fe80::5054:ff:fe89:740c, DR's priority: 1
            p4 = re.compile(r'^\s*PIM6 +DR: +(?P<dr_address>[\w\:]+),'
                            ' +DR\'s +priority: +(?P<dr_priority>[\d]+)$')
            m = p4.match(line)
            if m:
                dr_address = m.groupdict()['dr_address']
                dr_priority = m.groupdict()['dr_priority']

            # PIM6 neighbor count: 1
            p5 = re.compile(r'^\s*PIM6 +neighbor +count: +(?P<nbr_count>[\d]+)$')

            m = p5.match(line)
            if m:
                nbr_count = m.groupdict()['nbr_count']

            # PIM6 hello interval: 45 secs (configured 44444 ms), next hello sent in: 00:00:05
            p6 = re.compile(r'^\s*PIM6 +hello +interval: +(?P<hello_interval>[\d]+) +secs'
                            '( +\(configured +(?P<configured_interval_ms>\d+) +ms\))?,'
                            ' +next +hello +sent +in: +(?P<hello_expiration>[\w\:]+)$')
            m = p6.match(line)
            if m:
                hello_interval = m.groupdict()['hello_interval']
                hello_expiration = m.groupdict()['hello_expiration']

            # PIM6 neighbor holdtime: 159 secs
            p7 = re.compile(r'^\s*PIM6 +neighbor +holdtime: +(?P<holdtime>[\d]+) +secs$')
            m = p7.match(line)
            if m:
                neighbor_holdtime = m.groupdict()['holdtime']

            # PIM6 configured DR priority: 144
            p8 = re.compile(r'^\s*PIM6 +configured +DR +priority: +(?P<configured_dr_priority>[\d]+)$')
            m = p8.match(line)
            if m:
                configured_dr_priority = m.groupdict()['configured_dr_priority']

            # PIM6 configured DR delay: 3 secs
            p9 = re.compile(r'^\s*PIM6 +configured +DR +delay: +(?P<configured_dr_delay>[\d]+) +secs$')
            m = p9.match(line)
            if m:
                configured_dr_delay = m.groupdict()['configured_dr_delay']

            # PIM6 border interface: yes
            p10 = re.compile(r'^\s*PIM6 +border +interface: +(?P<border_interface>[\w]+)$')
            m = p10.match(line)
            if m:
                bsr_border = m.groupdict()['border_interface']

            # PIM6 GenID sent in Hellos: 0x26fae674
            p11 = re.compile(r'^\s*PIM6 +GenID +sent +in +Hellos: +(?P<genid>[\S]+)$')
            m = p11.match(line)
            if m:
                genid = m.groupdict()['genid']

            # PIM6 Hello MD5-AH Authentication: disabled
            p12 = re.compile(r'^\s*PIM6 +Hello +MD5-AH +Authentication: +(?P<md5_authentication>[\w]+)$')
            m = p12.match(line)
            if m:
                hello_md5_ah_authentication = m.groupdict()['md5_authentication']

            # PIM6 Neighbor policy: v4neighbor-policy
            p13 = re.compile(r'^\s*PIM6 +Neighbor +policy: +(?P<nbr_policy>(?!none +configured)[\w\-\s]+)$')
            m = p13.match(line)
            if m:
                neighbor_filter = m.groupdict()['nbr_policy']

            # PIM6 Join-Prune inbound policy: v4jp-policy
            p14 = re.compile(r'^\s*PIM6 +Join-Prune +inbound +policy: +(?P<jp_inbound_policy>(?!none)[\w\-\s]+)$')
            m = p14.match(line)
            if m:
                jp_inbound_policy = m.groupdict()['jp_inbound_policy']

            # PIM6 Join-Prune outbound policy: v4jp-policy
            p15 = re.compile(r'^\s*PIM6 +Join-Prune +outbound +policy: +(?P<jp_outbound_policy>(?!none)[\w\-\s]+)$')
            m = p15.match(line)
            if m:
                jp_outbound_policy = m.groupdict()['jp_outbound_policy']

            # PIM6 Join-Prune interval: 1 minutes
            p16 = re.compile(r'^\s*PIM6 +Join-Prune +interval: +(?P<jp_interval>[\d]+) +minutes$')
            m = p16.match(line)
            if m:
                jp_interval = m.groupdict()['jp_interval']

            # PIM6 Join-Prune next sending: 1 minutes
            p17 = re.compile(r'^\s*PIM6 +Join-Prune +next +sending: +(?P<jp_next_sending>[\d]+) +minutes$')
            m = p17.match(line)
            if m:
                jp_next_sending = m.groupdict()['jp_next_sending']

            # PIM6 BFD enabled: no
            p18 = re.compile(r'^\s*PIM6 +BFD +enabled: +(?P<bfd_enabled>[\w]+)$')
            m = p18.match(line)
            if m:
                bfd = m.groupdict()['bfd_enabled']

            # PIM6 passive interface: no
            p19 = re.compile(r'^\s*PIM(6)? +passive +interface: +(?P<passive>[\w]+)$')
            m = p19.match(line)
            if m:
                passive = m.groupdict()['passive']

            # PIM6 VPC SVI: no
            p20 = re.compile(r'^\s*PIM6 +VPC +SVI: +(?P<vpc_svi>[\w]+)$')
            m = p20.match(line)
            if m:
                vpc_svi = m.groupdict()['vpc_svi']

            # PIM6 Auto Enabled: no
            p21 = re.compile(r'^\s*PIM(6)? +Auto +Enabled: +(?P<auto_enabled>[\w]+)$')
            m = p21.match(line)
            if m:
                auto_enabled = m.groupdict()['auto_enabled']

            # PIM6 Interface Statistics, last reset: never
            # PIM6 Interface Statistics
            p22 = re.compile(r'^\s*PIM6 +Interface +Statistics+(, +last +reset: +(?P<last_reset>[\w\:]+))?$')
            m = p22.match(line)
            if m:
                statistic = True
                if m.groupdict()['last_reset']:
                    last_rest = m.groupdict()['last_reset']

            # Hellos: 360/474 (early: 0), JPs: 0/0, Asserts: 0/0
            p23 = re.compile(r'^\s*Hellos: +(?P<hellos>[\d\/]+)'
                             '( +\(early: +(?P<early>\d+)\))?,'
                             ' +JPs: +(?P<jps>[\d\/]+),'
                             ' +Asserts: +(?P<asserts>[\d\/]+)$')
            m = p23.match(line)
            if m:
                hellos = m.groupdict()['hellos']
                jps = m.groupdict()['jps']
                asserts = m.groupdict()['asserts']

            # Grafts: 0/0, Graft-Acks: 0/0
            p24 = re.compile(r'^\s*Grafts: +(?P<grafts>[\d\/]+),'
                             ' +Graft-Acks: +(?P<graft_acks>[\d\/]+)$')
            m = p24.match(line)
            if m:
                grafts = m.groupdict()['grafts']
                graft_acks = m.groupdict()['graft_acks']

            # DF-Offers: 0/0, DF-Winners: 0/0, DF-Backoffs: 0/0, DF-Passes: 0/0
            p25 = re.compile(r'^\s*DF-Offers: +(?P<df_offers>[\d\/]+),'
                             ' +DF-Winners: +(?P<df_winners>[\d\/]+),'
                             ' +DF-Backoffs: +(?P<df_backoffs>[\d\/]+),'
                             ' +DF-Passes: +(?P<df_passes>[\d\/]+)$')
            m = p25.match(line)
            if m:
                df_offers = m.groupdict()['df_offers']
                df_winners = m.groupdict()['df_winners']
                df_backoffs = m.groupdict()['df_backoffs']
                df_passes = m.groupdict()['df_passes']

            #    Checksum errors: 0, Invalid packet types/DF subtypes: 0/0
            p26 = re.compile(r'^\s*Checksum errors: +(?P<checksum>[\d]+),'
                             ' +Invalid +packet +types\/DF +subtypes:'
                             ' +(?P<invalid_packet_types>[\d]+)/(?P<invalid_df_subtypes>[\d]+)$')
            m = p26.match(line)
            if m:
                checksum = m.groupdict()['checksum']
                invalid_packet_types = m.groupdict()['invalid_packet_types']
                invalid_df_subtypes = m.groupdict()['invalid_df_subtypes']

            #    Authentication failed: 0
            p27 = re.compile(r'^\s*Authentication +failed: +(?P<authentication_failed>[\d]+)$')
            m = p27.match(line)
            if m:
                authentication_failed = m.groupdict()['authentication_failed']

            #    Packet length errors: 0, Bad version packets: 0, Packets from self: 0
            p28 = re.compile(r'^\s*Packet +length +errors: +(?P<packet_length_errors>[\d]+),'
                             ' +Bad +version +packets: +(?P<bad_version_packets>[\d]+),'
                             ' +Packets +from +self: +(?P<packets_from_self>[\d]+)$')
            m = p28.match(line)
            if m:
                packet_length_errors = m.groupdict()['packet_length_errors']
                bad_version_packets = m.groupdict()['bad_version_packets']
                packets_from_self = m.groupdict()['packets_from_self']

            #    Packets from non-neighbors: 0
            p29 = re.compile(r'^\s*Packets +from +non\-neighbors: +(?P<packets_from_non_neighbors>[\d]+)$')
            m = p29.match(line)
            if m:
                packets_from_non_neighbors = m.groupdict()['packets_from_non_neighbors']

            #    Packets received on passiveinterface: 0
            p30 = re.compile(r'^\s*Packets +received +on +passiveinterface:'
                             ' +(?P<packets_received_on_passiveinterface>[\d]+)$')
            m = p30.match(line)
            if m:
                packets_received_on_passiveinterface = m.groupdict()['packets_received_on_passiveinterface']

            #    JPs received on RPF-interface: 0
            p31 = re.compile(r'^\s*JPs +received +on +RPF\-interface:'
                             ' +(?P<jp_received_on_rpf_interface>[\d]+)$')
            m = p31.match(line)
            if m:
                jps_received_on_rpf_interface = m.groupdict()['jp_received_on_rpf_interface']

            #    (*,G) Joins received with no/wrong RP: 0/0
            p32 = re.compile(r'^\s*(?P<s_g>[\w\(\)\,\*]+) +Joins +received +with +no\/+wrong RP:'
                             ' +(?P<joins_received_with_no_rp>\d+)/(?P<joins_received_with_wrong_rp>\d+)$')
            m = p32.match(line)
            if m:
                joins_received_with_no_rp = m.groupdict()['joins_received_with_no_rp']
                joins_received_with_wrong_rp = m.groupdict()['joins_received_with_wrong_rp']

            #  (*,G)/(S,G) JPs received for SSM/Bidir groups: 0/0
            p33 = re.compile(r'^\s*(?P<s_g>[\w\(\)\,\*\/]+) +JPs +received +for +SSM\/Bidir +groups:'
                             ' +(?P<joins_received_with_ssm_groups>\d+)/(?P<joins_received_with_bidir_groups>\d+)$')
            m = p33.match(line)
            if m:
                joins_received_with_ssm_groups = m.groupdict()['joins_received_with_ssm_groups']
                joins_received_with_bidir_groups = m.groupdict()['joins_received_with_bidir_groups']

            # JPs filtered by inbound policy: 0
            p34 = re.compile(r'^\s*JPs +filtered +by +inbound +policy:'
                             ' +(?P<jps_filtered_by_inbound_policy>\d+)$')
            m = p34.match(line)
            if m:
                jps_filtered_by_inbound_policy = m.groupdict()['jps_filtered_by_inbound_policy']

            # JPs filtered by outbound policy: 0
            p35 = re.compile(r'^\s*JPs +filtered +by +outbound +policy:'
                             ' +(?P<jps_filtered_by_outbound_policy>\d+)$')
            m = p35.match(line)
            if m:
                jps_filtered_by_outbound_policy = m.groupdict()['jps_filtered_by_outbound_policy']


            if vrf and interface_name:
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}
                if 'interfaces' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['interfaces'] = {}

                if interface_name not in parsed_dict['vrf'][vrf]['interfaces']:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name] = {}

                if 'address_family' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'] = {}

                if af_name not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family']:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] = {}

                if oper_status:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name]\
                        ['oper_status'] = oper_status
                if link_status:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name]\
                        ['link_status'] = link_status
                if admin_status:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name]\
                        ['admin_status'] = admin_status
                if address_list:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['address'] = address_list

                if dr_address:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['dr_address'] = dr_address
                if dr_priority:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['dr_priority'] = int(dr_priority)
                if configured_dr_priority:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['configured_dr_priority'] = int(configured_dr_priority)

                if configured_dr_delay:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['dr_delay'] = int(configured_dr_delay)
                if nbr_count:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['neighbor_count'] = int(nbr_count)
                if hello_interval:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['hello_interval'] = int(hello_interval)
                if hello_expiration:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['hello_expiration'] = hello_expiration
                if neighbor_holdtime:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['neighbor_holdtime'] = int(neighbor_holdtime)
                if dr_priority:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['dr_priority'] = int(dr_priority)
                if bsr_border:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['bsr_border'] = True if bsr_border.lower() == 'yes' else False
                if genid:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['genid'] = genid

                if hello_md5_ah_authentication:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['hello_md5_ah_authentication'] = hello_md5_ah_authentication

                if neighbor_filter:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['neighbor_filter'] = neighbor_filter

                if jp_inbound_policy:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['jp_inbound_policy'] = jp_inbound_policy

                if jp_outbound_policy:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['jp_outbound_policy'] = jp_outbound_policy

                if jp_interval:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['jp_interval'] = int(jp_interval)
                if jp_next_sending:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['jp_next_sending'] = int(jp_next_sending)


                if bfd:
                    if 'bfd' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]\
                            ['address_family'][af_name]:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family']\
                            [af_name]['bfd'] = {}
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['bfd']['enable'] = True if bfd.lower() == 'yes' else False


                if passive:
                    if 'sm' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]\
                            ['address_family'][af_name]:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family']\
                            [af_name]['sm'] = {}
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['sm']['passive'] = True if passive.lower() == 'yes' else False

                if vpc_svi:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['vpc_svi'] = True if vpc_svi.lower() == 'yes' else False


                if auto_enabled:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['auto_enabled'] = True if auto_enabled.lower() == 'yes' else False

                if hellos or jps or asserts or grafts or graft_acks or df_backoffs or df_passes\
                        or df_winners or df_offers:
                    if 'statistics' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]\
                            ['address_family'][af_name]:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics'] = {}
                    if 'general' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']['general'] = {}
                    if last_rest:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']['last_reset'] = last_rest

                    if hellos:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name]\
                        ['statistics']['general']['hellos'] = hellos
                    if jps:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['jps'] = jps
                    if asserts:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['asserts'] = asserts
                    if df_offers:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['df_offers'] = df_offers
                    if graft_acks:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['graft_acks'] = graft_acks
                    if grafts:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['grafts'] = grafts
                    if df_backoffs:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['df_backoffs'] = df_backoffs
                    if df_passes:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['df_passes'] = df_passes
                    if df_winners:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['df_winners'] = df_winners

                if checksum or invalid_packet_types or invalid_df_subtypes or authentication_failed\
                        or packet_length_errors or bad_version_packets or packets_from_self or \
                        packets_from_non_neighbors or packets_received_on_passiveinterface or \
                        jps_received_on_rpf_interface or joins_received_with_bidir_groups or \
                        joins_received_with_no_rp or joins_received_with_ssm_groups or joins_received_with_wrong_rp or\
                        jps_filtered_by_inbound_policy or jps_filtered_by_outbound_policy:
                    if 'statistics' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]\
                            ['address_family'][af_name]:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics'] = {}
                    if 'errors' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']['errors'] = {}
                    if checksum:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']['errors']['checksum'] = int(checksum)

                    if invalid_df_subtypes:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name]\
                            ['statistics']['errors']['invalid_df_subtypes'] = int(invalid_df_subtypes)
                    if invalid_packet_types:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['invalid_packet_types'] = int(invalid_packet_types)

                    if authentication_failed:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['authentication_failed'] = int(authentication_failed)
                    if packet_length_errors:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['packet_length_errors'] = int(packet_length_errors)
                    if bad_version_packets:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['bad_version_packets'] = int(bad_version_packets)

                    if packets_from_self:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['packets_from_self'] = int(packets_from_self)
                    if packets_from_non_neighbors:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['packets_from_non_neighbors'] = int(packets_from_non_neighbors)

                    if packets_received_on_passiveinterface:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['packets_received_on_passiveinterface']\
                            = int(packets_received_on_passiveinterface)

                    if jps_received_on_rpf_interface:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['jps_received_on_rpf_interface'] = int(jps_received_on_rpf_interface)
                    if joins_received_with_bidir_groups:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['joins_received_with_bidir_groups'] = int(joins_received_with_bidir_groups)

                    if joins_received_with_no_rp:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['joins_received_with_no_rp'] = int(joins_received_with_no_rp)

                    if joins_received_with_ssm_groups:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['joins_received_with_ssm_groups'] = int(joins_received_with_ssm_groups)

                    if joins_received_with_wrong_rp:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['joins_received_with_wrong_rp'] = int(joins_received_with_wrong_rp)
                    if jps_filtered_by_inbound_policy:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['jps_filtered_by_inbound_policy'] = int(jps_filtered_by_inbound_policy)
                    if jps_filtered_by_outbound_policy:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['jps_filtered_by_outbound_policy'] = int(jps_filtered_by_outbound_policy)
                continue

        return parsed_dict



# =====================================================
# schema for 'show ip/ipv6 pim rp [vrf <WORD>]'
# =====================================================
class ShowPimRpSchema(MetaParser):
    """Schema for:
        show ip pim rp
        show ip pim rp vrf <vrf>
        show ipv6 pim rp
        show ipv6 pim rp vrf <vrf>"""

    schema = {
        'vrf':{
            Any():{
                'address_family':{
                    Any():{
                        Optional('rp'):{
                            Optional('static_rp'):{
                                Any(): {
                                    Optional('sm'): {
                                        'policy_name': str,
                                        Optional('route_map'): str,
                                    },
                                    Optional('bidir'): {
                                        'policy_name': str,
                                        Optional('route_map'): str,
                                    },
                                },
                            },
                            Optional('bsr'):{
                                Optional('bsr_candidate'):{
                                    'priority': int,
                                    'hash_mask_length': int,
                                    'address': str,
                                },
                                Optional('bsr'):{
                                    'priority': int,
                                    'hash_mask_length': int,
                                    'address': str,
                                    Optional('up_time'): str,
                                    Optional('expires'): str,
                                },
                                Optional('rp'):{
                                    'up_time': str,
                                    'group_policy': str,
                                    Optional('rp_address'): str,
                                },
                                Optional('bsr_address'): {
                                    Any():{
                                        'priority': int,
                                        'mode': str,
                                        'address': str,
                                        'policy': str,
                                    },
                                },
                                Optional('bsr_next_bootstrap'): str,
                                Optional('rp_candidate_policy'): str,
                                Optional('rp_policy'): str,
                                Optional('rp_candidate_next_advertisement'): str,
                            },
                            Optional('autorp'): {
                                Optional('announce_policy'): str,
                                Optional('discovery_policy'): str,
                                Optional('address'): str,
                                Optional('bsr_next_discovery'): str,
                                Optional('send_rp_announce'): {                                    
                                    Optional('group'): str,
                                    Optional('scope'): int,
                                    Optional('group_list'): str,
                                    Optional('bidir'): bool,
                                    Optional('rp_source'): str,
                                },
                            },
                            Optional('rp_list'): {
                                Any(): {
                                    Optional('address'): str,
                                    Optional('info_source_address'): str,
                                    Optional('info_source_type'): str,
                                    Optional('up_time'): str,
                                    Optional('expiration'): str,
                                    Optional('df_ordinal'): int,
                                    Optional('priority'): int,
                                    Optional('mode'): str,
                                    Optional('group_ranges'): str,
                                },
                            },
                            Optional('rp_mappings'): {
                                Any(): {
                                    'group': str,
                                    'rp_address': str,
                                    'protocol': str,
                                    'up_time': str, 
                                    Optional('expiration'): str, 
                                },
                            }
                        },
                        Optional('sm'): {
                            Optional('asm'): {
                                Optional('anycast_rp'): {
                                    Any(): {
                                       Optional('anycast_address'): str,
                                    }
                                },
                            },
                        },
                    },
                },
            },
        },
    }

# ==========================================================
#  parser for 'show ip/ipv6 pim rp [vrf <vrf>]'
# ==========================================================
class ShowPimRp(ShowPimRpSchema):
    """Parser for:
        show <address_family> pim rp
        show <address_family> pim rp vrf <vrf>"""

    def cli(self, af='ip', vrf=''):

        cmd = 'show {af} pim rp vrf {vrf}'.format(af=af, vrf=vrf) if vrf else \
              'show {af} pim rp'.format(af=af)
        output = self.device.execute(cmd)
        af_name = 'ipv4' if af == 'ip' else af

        # Init dictionary
        parsed_output = dict()
        vrf_name = bsr = None
        anycast_rp_members_list = []
        flag = False
        connection_flag = False

        for line in output.splitlines():
            line = line.rstrip()

            # PIM6 RP Status Information for VRF "VRF1"
            # PIM RP Status Information for VRF "VRF1"
            p1 = re.compile(r'^\s*(PIM6|PIM) +RP +Status +Information +for +VRF +\"(?P<vrf_name>[\w\S]+)\"$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                anycast_rp_members_list = []
                flag = False
                connection_flag = False
                bsr = None
                auto_rp_address = None
                continue

            # BSR: Not Operational
            # BSR: 10.1.5.1*, next Bootstrap message in: 00:00:01,
            p2 = re.compile(r'^\s*BSR: +(?P<bsr>[\w\S]+)'
                            '(, +next +Bootstrap +message +in: +(?P<next_bsr_message>[\w\S]+),)?$')
            m = p2.match(line)
            if m:
                bsr = m.groupdict()['bsr'].replace('*','')
                if 'not' in bsr.lower() or 'none' in bsr.lower():
                    bsr = None
                    continue

                if 'vrf' not in parsed_output:
                    parsed_output['vrf'] = {}
                if vrf_name not in parsed_output['vrf']:
                    parsed_output['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_output['vrf'][vrf_name]:
                    parsed_output['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_output['vrf'][vrf_name]['address_family']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name] = {}

                if 'rp' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] = {}
                if 'bsr' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']['bsr'] = {}

                if m.groupdict()['next_bsr_message']:
                     parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                        ['bsr']['bsr_next_bootstrap'] = m.groupdict()['next_bsr_message']

                if 'bsr_candidate' not in parsed_output['vrf'][vrf_name]['address_family']\
                        [af_name]['rp']['bsr']:
                    parsed_output['vrf'][vrf_name]['address_family'] \
                        [af_name]['rp']['bsr']['bsr_candidate'] = {}

                if 'bsr' not in parsed_output['vrf'][vrf_name]['address_family']\
                        [af_name]['rp']['bsr']:
                    parsed_output['vrf'][vrf_name]['address_family'] \
                        [af_name]['rp']['bsr']['bsr'] = {}

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                    ['bsr']['bsr']['address'] = bsr

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                    ['bsr']['bsr_candidate']['address'] = bsr
                continue


            # BSR: 10.1.5.5, uptime: 18:04:20, expires: 00:01:50,
            p2_1 = re.compile(r'^\s*BSR(\:)? +(?P<bsr_candidate>[\w\s\.\*\:]+)'
                            ', +uptime: +(?P<bsr_uptime>[\w\.\:]+)'
                            ', +expires: +(?P<bsr_expires>[\w\.\:]+),$')
            m = p2_1.match(line)
            if m:
                bsr_candidate = m.groupdict()['bsr_candidate'].replace('*', '')
                bsr_candidate_uptime = m.groupdict()['bsr_uptime']
                bsr_candidate_expires = m.groupdict()['bsr_expires']

                if 'vrf' not in parsed_output:
                    parsed_output['vrf'] = {}
                if vrf_name not in parsed_output['vrf']:
                    parsed_output['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_output['vrf'][vrf_name]:
                    parsed_output['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_output['vrf'][vrf_name]['address_family']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name] = {}

                if 'rp' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] = {}
                if 'bsr' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']['bsr'] = {}

                if 'bsr_candidate' not in parsed_output['vrf'][vrf_name]['address_family']\
                        [af_name]['rp']['bsr']:
                    parsed_output['vrf'][vrf_name]['address_family'] \
                        [af_name]['rp']['bsr']['bsr_candidate'] = {}

                if 'bsr' not in parsed_output['vrf'][vrf_name]['address_family']\
                        [af_name]['rp']['bsr']:
                    parsed_output['vrf'][vrf_name]['address_family'] \
                        [af_name]['rp']['bsr']['bsr'] = {}

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                    ['bsr']['bsr']['address'] = bsr_candidate

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                    ['bsr']['bsr_candidate']['address'] = bsr_candidate

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                    ['bsr']['bsr']['up_time'] = bsr_candidate_uptime

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                    ['bsr']['bsr']['expires'] = bsr_candidate_expires

                continue


            # Auto-RP disabled
            p3 = re.compile(r'^\s*Auto-RP +disabled$')
            m = p3.match(line)
            if m:
                continue

            # Auto-RP RPA: 11.11.11.11*, next Discovery message in: 00:00:15
            p3 = re.compile(r'^\s*Auto-RP RPA: +(?P<auto_rp_address>[\w\S]+),'
                            ' +next +[d|D]iscovery +message +in: +(?P<next_discory_message>[\w\S]+)$')
            m = p3.match(line)
            if m:
                auto_rp_address = m.groupdict()['auto_rp_address'].replace('*','')

                if 'vrf' not in parsed_output:
                    parsed_output['vrf'] = {}
                if vrf_name not in parsed_output['vrf']:
                    parsed_output['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_output['vrf'][vrf_name]:
                    parsed_output['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_output['vrf'][vrf_name]['address_family']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name] = {}

                if 'rp' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] = {}
                if 'autorp' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']['autorp'] = {}

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                    ['autorp']['address'] = auto_rp_address

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']\
                    ['autorp']['bsr_next_discovery'] = m.groupdict()['next_discory_message']
                continue

            # BSR RP Candidate policy: None
            p4 = re.compile(r'^\s*BSR +RP +Candidate +policy: +(?P<bsr_rp_candidate_policy>[\w\S]+)$')
            m = p4.match(line)
            if m and bsr:
                rp_candidate_policy = None if m.groupdict()['bsr_rp_candidate_policy'].lower() == 'none' \
                    else m.groupdict()['bsr_rp_candidate_policy']

                if rp_candidate_policy:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                                ['bsr']['rp_candidate_policy'] = rp_candidate_policy
                continue

            # BSR RP policy: None
            p5 = re.compile(r'^\s*BSR +RP +policy: +(?P<bsr_rp_policy>[\w\S]+)$')
            m = p5.match(line)
            if m and bsr:
                rp_policy = "" if m.groupdict()['bsr_rp_policy'].lower() == 'none' \
                    else m.groupdict()['bsr_rp_policy']
                if rp_policy:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                        ['bsr']['rp_policy'] = rp_policy
                continue


            # Auto-RP Announce policy: None
            p6 = re.compile(r'^\s*Auto\-RP +Announce +policy: +(?P<auto_rp_announce_policy>[\w\S]+)$')
            m = p6.match(line)
            if m and auto_rp_address:
                announce_policy = "" if m.groupdict()['auto_rp_announce_policy'].lower() \
                                        == 'none' else m.groupdict()['auto_rp_announce_policy']
                if 'autorp' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']['autorp'] = {}

                if announce_policy:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']\
                        ['autorp']['announce_policy'] = announce_policy
                continue

            # Auto-RP Discovery policy: None
            p7 = re.compile(r'^\s*Auto\-RP +Discovery +policy: +(?P<auto_rp_discovery_policy>[\w\S]+)$')
            m = p7.match(line)
            if m and auto_rp_address:
                discovery_policy = "" if m.groupdict()['auto_rp_discovery_policy'].lower() == 'none' else \
                    m.groupdict()['auto_rp_discovery_policy']
                if discovery_policy:
                    if 'autorp' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']['autorp'] = {}
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']\
                        ['autorp']['discovery_policy'] = discovery_policy
                continue

            # Anycast-RP 10.111.111.111 members:
            p11 = re.compile(r'^\s*Anycast\-RP +(?P<anycast_rp>[\w\d\S]+) +members:$')
            m = p11.match(line)
            if m:
                anycast_rp = m.groupdict()['anycast_rp']
                flag = True
                
                if 'vrf' not in parsed_output:
                    parsed_output['vrf'] = {}
                if vrf_name not in parsed_output['vrf']:
                    parsed_output['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_output['vrf'][vrf_name]:
                    parsed_output['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_output['vrf'][vrf_name]['address_family']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name] = {}
                continue

            # 10.1.2.1*  10.1.5.1
            p11_1 = re.compile(r'^(?P<anycast_rp_members>[\w\.\:\*\s]+)$')
            m = p11_1.match(line)
            if m and flag:
                anycast_rp_members_list = m.groupdict()['anycast_rp_members'].split()
                for member in anycast_rp_members_list:
                    anycast_member = anycast_rp +" "+ member.replace('*','')
                    if 'sm' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'] = {}

                    if 'asm' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm']['asm'] = {}

                    if 'anycast_rp' not in parsed_output['vrf'][vrf_name]['address_family']\
                            [af_name]['sm']['asm']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm']\
                            ['asm']['anycast_rp'] = {}

                    if anycast_member not in parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm']\
                            ['asm']['anycast_rp']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm']\
                            ['asm']['anycast_rp'][anycast_member] = {}

                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm']\
                        ['asm']['anycast_rp'][anycast_member]['anycast_address'] = anycast_rp
                flag = False
                continue

            # RP: 33.33.33.33, (0), uptime: 03:52:52, expires: never,
            p8 = re.compile(r'^\s*RP: +(?P<rp>[\w\d\S]+), +\(+(?P<df_ordinal>[\d\S]+)+\),'
                            ' +uptime: +(?P<uptime>[\w\.\:]+),'
                            ' +expires: +(?P<expires>[\w\d\S][^,]+)(?P<comma>[\,]+)?$')
            m = p8.match(line)
            if m:
                rp_dict = parsed_output.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(af_name, {}).setdefault('rp', {})

                rp_address = m.groupdict()['rp'].replace('*','')
                df_ordinal = m.groupdict()['df_ordinal']
                uptime = m.groupdict()['uptime']
                expires = m.groupdict()['expires']
                connection_flag = False
                code = None
                continue

            # RP: 55.55.55.51, (0), 
            p8_1 = re.compile(r'^\s*RP: +(?P<rp>[\w\d\S]+), +\(+(?P<df_ordinal>[\d\S]+)+\),$')
            m = p8_1.match(line)
            if m:
                rp_dict = parsed_output.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(af_name, {}).setdefault('rp', {})

                rp_address = m.groupdict()['rp'].replace('*','')
                df_ordinal = m.groupdict()['df_ordinal']
                connection_flag = False
                code = None
                continue

            # uptime: 1d13h   priority: 255, 
            # uptime: 2d21h, (A) (B),  priority: 192
            p8_2 = re.compile(r'^\s*uptime: +(?P<uptime>[\w\.\:]+),?'
                               '( +(?P<modes>( *\(\w\)){0,3}),)? '
                               '+priority: +(?P<priority>\d+),?$')
            m = p8_2.match(line)
            if m:
                uptime = m.groupdict()['uptime']
                priority = int(m.groupdict()['priority'])
                continue

            # RP-source: (local), 
            # RP-source: (local), group-map: BIDIR_SPARSE1, 
            p8_3 = re.compile(r'^\s*RP\-source:( +(?P<rp_source>\S+))? +\(+(?P<info_source_type>\w+)+\),'
                               ' *(group-map: +(?P<route_map>[\w\-]+),)?$')
            m = p8_3.match(line)
            if m:
                code = None
                rp_sources = [m.groupdict()['rp_source']]
                route_map = m.groupdict()['route_map']
                info_source_type = m.groupdict()['info_source_type']
                if info_source_type.lower() == 'local':
                    info_source_type_conversions = ['static']
                if info_source_type.lower() == 'b':
                    info_source_type_conversions = ['bootstrap']
                if info_source_type.lower() == 'a':
                    info_source_type_conversions = ['autorp']
                continue 

            # RP-source: 2.2.2.2 (A), 2.2.2.2 (B),
            # RP-source: 6.6.6.6 (A), 2.2.2.2 (B), (local), 
            p8_4 = re.compile(r'^\s*RP\-source: +(?P<rp_source>\S+) +\(+(?P<info_source_type>\w+)+\),')
            m = p8_4.match(line)
            if m:
                p = re.compile(r'(?P<rp_source>\S+) +(?P<info_source_type>[\w\(\)\,\s]+),')
                m = p.findall(line)
                info_source_type_conversions = []
                rp_sources = []
                for rp_source, info_source_type in m:
                    conversions = []
                    if 'local' in info_source_type.lower():
                        conversions.append('static')
                    if '(b)' in info_source_type.lower():
                        conversions.append('bootstrap')
                    if '(a)' in info_source_type.lower():
                        conversions.append('autorp')

                    rp_sources.extend([rp_source] * len(conversions))
                    info_source_type_conversions.extend(conversions)
                code = None
                continue 

            # group ranges:
            line = line.strip()
            p8_4 = re.compile(r'^group +ranges:$')
            m = p8_4.match(line)
            if m:
                route_map = None
                connection_flag = True
                continue 

            #  priority: 0, RP-source: (local), group ranges:
            #  priority: 92, RP-source: 10.1.5.1 (B), group ranges:
            #  priority: 0, RP-source: (local), group-map: PIM6-STATIC-RP, group ranges:
            p9 = re.compile(r'^\s*priority: +(?P<priority>\d+),'
                            ' +RP\-source:( +(?P<rp_source>[\w\S]+))? +\(+(?P<info_source_type>\w+)+\),'
                            '( *group-map: +(?P<route_map>\S+),)?'
                            ' +group +ranges:$')
            m = p9.match(line)
            if m:
                connection_flag = True
                priority = int(m.groupdict()['priority'])
                rp_sources = [m.groupdict()['rp_source']]
                route_map = m.groupdict()['route_map']
                info_source_type = m.groupdict()['info_source_type']

                if info_source_type.lower() == 'local':
                    info_source_type_conversions = ['static']
                    code = 'static'
                if info_source_type.lower() == 'b':
                    info_source_type_conversions = ['bootstrap']
                    code = 'bootstrap'
                if info_source_type.lower() == 'a':
                    info_source_type_conversions = ['autorp']
                    code = 'autorp'
                continue

            #      224.0.0.0/4
            #      233.0.0.0/24  (bidir)
            #      ff1e::3002/128 ff1e::3001/128
            # 226.0.0.0/8   (bidir)  ,  expires: 00:02:24 (A)
            p10 = re.compile(r'^\s*(?P<group_ranges>[\w\/\.\:\s]+)'
                             '( +\((?P<bidir>\w+)\))?'
                             '( *, *expires: (?P<expires>[\w\.\:]+)( *\((?P<code>\w+)\))?)?$')
            m = p10.match(line)
            if m and connection_flag:
                expire_dict = {}
                group_ranges = m.groupdict()['group_ranges'].strip()
                if  m.groupdict()['bidir'] and 'bidir' in m.groupdict()['bidir'].lower():
                    mode = 'BIDIR'
                else:
                    mode = 'SM'

                try:
                    expires = m.groupdict()['expires'] or expires
                except Exception:
                    expires = None

                try:
                    code = m.groupdict()['code'] or code
                    if not code:
                        code = 'static'
                except Exception:
                    code = None

                if code and 'b' == code.lower():
                    code = 'bootstrap'
                elif code and 'a' == code.lower():
                    code = 'autorp'

                # rp_list dict
                rp_list_d = rp_dict.setdefault('rp_list', {})
                for info_source_type_conversion, rp_source in zip(info_source_type_conversions, rp_sources):

                    rp_address_source_type = rp_address + " " + mode + ' ' + info_source_type_conversion

                    rp_list_dict = rp_list_d.setdefault(rp_address_source_type, {})

                    rp_list_dict['address'] = rp_address

                    rp_list_dict['info_source_type'] = info_source_type_conversion

                    if rp_source:
                        rp_list_dict['info_source_address'] = rp_source

                    rp_list_dict['up_time'] = uptime

                    if expires:
                        rp_list_dict['expiration'] = expires

                    if df_ordinal:
                        rp_list_dict['df_ordinal'] = int(df_ordinal)

                    if priority:
                        rp_list_dict['priority'] = priority

                    rp_list_dict['mode'] = mode

                    # append to the list if group-ranges have many entries
                    group_range = rp_list_dict.get('group_ranges', '')
                    group_range = set(group_range.split())
                    group_range.add(group_ranges)
                    rp_list_dict['group_ranges'] = ' '.join(sorted(group_range))

                    # static
                    if info_source_type_conversion == 'static':
                        s_mode = mode.lower()
                        static_rp_dict = rp_dict.setdefault('static_rp', {})\
                            .setdefault(rp_address, {}).setdefault(s_mode, {})

                        static_rp_dict['policy_name'] = group_ranges
                        if route_map:                                
                            static_rp_dict['route_map'] = route_map

                    # autorp
                    if info_source_type_conversion == 'autorp':
                        autorp_dict = rp_dict.setdefault('autorp', {}).setdefault('send_rp_announce', {})
                        if rp_source:
                            autorp_dict['rp_source'] = rp_source
                        
                        autorp_dict['scope'] = int(df_ordinal)

                        autorp_dict['bidir'] = True if mode == 'BIDIR' else False

                        autorp_dict['group_list'] = group_ranges

                        autorp_dict['group'] = group_ranges.split('/')[0]

                    # rp_mappings
                    key = group_ranges + ' ' + rp_address + ' ' + info_source_type_conversion

                    rp_mappings_dict = rp_dict.setdefault('rp_mappings', {}).setdefault(key, {})

                    rp_mappings_dict['rp_address'] = rp_address

                    rp_mappings_dict['protocol'] = info_source_type_conversion

                    rp_mappings_dict['group'] = group_ranges

                    rp_mappings_dict['up_time'] = uptime

                    if expires and code and code in info_source_type_conversion:
                        rp_mappings_dict['expiration'] = expires

                    # rp  bsr  bsr_rp_candidate_address
                    if info_source_type_conversion == 'bootstrap' and rp_source:
                        bsr_dict = rp_dict.setdefault('bsr', {}).setdefault('bsr_address', {}).setdefault(rp_source, {})

                        bsr_dict['address'] = rp_source

                        # append to the list if group-ranges have many entries
                        group_range = bsr_dict.get('policy', '')
                        group_range = set(group_range.split())
                        group_range.add(group_ranges)
                        bsr_dict['policy'] = ' '.join(sorted(group_range))

                        bsr_dict['mode'] = mode

                        bsr_dict['priority'] = priority

                        if expires:
                            rp_dict.setdefault('bsr', {}).setdefault('rp_candidate_next_advertisement', expires)


                    # rp  bsr  rp
                    if info_source_type_conversion == 'bootstrap':
                        bsr_rp_dict = rp_dict.setdefault('bsr', {}).setdefault('rp', {})

                        if rp_source:
                            bsr_rp_dict['rp_address'] = rp_source

                        # append to the list if group-ranges have many entries
                        group_range = bsr_rp_dict.get('group_policy', '')
                        group_range = set(group_range.split())
                        group_range.add(group_ranges)
                        bsr_rp_dict['group_policy'] = ' '.join(sorted(group_range))

                        bsr_rp_dict['up_time'] = uptime
                continue

            #    priority: 111, hash-length: 30
            p13 = re.compile(r'^\s*priority: +(?P<priority>\d+),'
                             ' +hash-length: +(?P<hash_length>\d+)$')
            m = p13.match(line)
            if m:
                bsr_prioprity = int(m.groupdict()['priority'])
                bsr_hash_length = int(m.groupdict()['hash_length'])

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']\
                    ['bsr']['bsr']['priority'] = bsr_prioprity

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp']\
                    ['bsr']['bsr']['hash_mask_length'] = bsr_hash_length

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                    ['bsr']['bsr_candidate']['priority'] = bsr_prioprity

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['rp'] \
                    ['bsr']['bsr_candidate']['hash_mask_length'] = bsr_hash_length
                continue

        return parsed_output


# ==========================================================
#  parser for 'show ipv6 pim rp [vrf <vrf>]'
# ==========================================================
class ShowIpv6PimRp(ShowPimRp):
    """Parser for:
        show ipv6 pim rp
        show ipv6 pim rp vrf <vrf>"""

    def cli(self, vrf=''):
        return super().cli(af='ipv6', vrf=vrf)

# ==========================================================
#  parser for 'show ip pim rp [vrf <vrf>]'
# ==========================================================
class ShowIpPimRp(ShowPimRp):
    """Parser for:
        show ip pim rp
        show ip pim rp vrf <vrf>"""

    def cli(self, vrf=''):
        return super().cli(af='ip', vrf=vrf)


# ==============================================
# schema Parser for 'show ipv6 pim df vrf all'
# ==============================================
class ShowIpv6PimDfSchema(MetaParser):
    """Schema for:
        show ipv6 pim df
        show ipv6 pim df vrf <vrf>"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        Optional('rp'): {
                            Optional('bidir'): {
                                Optional('interface_df_election'): {
                                    Optional(Any()): {
                                        Optional('address'): str,
                                        Optional('df_ordinal'): int,
                                        Optional('metric_pref'): int,
                                        Optional('metric'): int,
                                        Optional('group_range'): str,
                                        Optional('interface_name'): str,
                                        Optional('df_address'): str,
                                        Optional('df_uptime'): str,
                                        Optional('interface_state'): str,
                                        Optional('winner_metric_pref'): int,
                                        Optional('winner_metric'): int,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ==========================================================
#  parser for show ipv6 pim df vrf all
#
# ==========================================================
class ShowIpv6PimDf(ShowIpv6PimDfSchema):
    """Parser for:
        show ipv6 pim df
        show ipv6 pim df vrf <vrf>"""

    def cli(self, vrf=""):

        if vrf:
            cmd = 'show ipv6 pim df vrf {}'.format(vrf)
        else:
            cmd = 'show ipv6 pim df'

        out = self.device.execute(cmd)
        af_name = 'ipv6'
        # Init dictionary
        parsed_dict = dict()
        vrf = ordinal = df_uptime = df_address = interface = rp_address = ""

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Bidir-PIM6 Designated Forwarder Information for VRF "default"
            p1 = re.compile(r'^\s*Bidir-PIM6 +Designated +Forwarder'
                            ' +Information +for +VRF \"(?P<vrf>[\w]+)\"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                ordinal = df_uptime = df_address = interface = rp_address = ""

            # RP Address (ordinal)   RP Metric       Group Range
            # 2001:db8:1:1::1 (8)
            p2 = re.compile(r'^\s*(?P<rp_address>[\w\:\.]+) +\((?P<ordinal>\d+)\)$')
            m = p2.match(line)
            if m:
                metrics_pref = metrics = group_range = interface = df_address = interface_state \
                    = winner_metrics_pref = winner_metrics = df_uptime = ""
                rp_address = m.groupdict()['rp_address']
                ordinal = m.groupdict()['ordinal']

            #           [0/0]           ff09::/16
            p3 = re.compile(r'^\s*(?P<space>\s{23})'
                            '\[(?P<metrics_pref>[\d\-]+)/(?P<metrics>[\d\-]+)\] +(?P<group_range>[\w\.\:\/]+)$')
            m = p3.match(line)
            if m:

                metrics_pref = m.groupdict()['metrics_pref']
                metrics = m.groupdict()['metrics']
                group_range = m.groupdict()['group_range']

            # Interface     DF Address                 DF State DF Metric  DF Uptime
            # Eth2/1        fe80::5054:ff:fe89:740c    Winner   [0/0]      00:00:48
            p4 = re.compile(r'^\s*(?P<interface>[\w\-\/]+) +(?P<df_address>[\S]+)'
                            ' +(?P<df_state>\w+)'
                            ' +\[(?P<winner_metrics_pref>[\d\-]+)/(?P<winner_metrics>[\d\-]+)\]'
                            ' +(?P<df_uptime>\S+)$')
            m = p4.match(line)
            if m:
                interface = Common.convert_intf_name(m.groupdict()['interface'])
                df_address = m.groupdict()['df_address']
                interface_state = m.groupdict()['df_state'].lower()
                if interface_state == 'winner':
                    interface_state = 'win'
                winner_metrics_pref = m.groupdict()['winner_metrics_pref']
                winner_metrics = m.groupdict()['winner_metrics']
                df_uptime = m.groupdict()['df_uptime']

            if vrf and rp_address:
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}

                if 'address_family' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['address_family'] = {}
                if af_name not in parsed_dict['vrf'][vrf]['address_family']:
                    parsed_dict['vrf'][vrf]['address_family'][af_name] = {}

                if 'rp' not in parsed_dict['vrf'][vrf]['address_family'][af_name]:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['rp'] = {}
                if 'bidir' not in parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] = {}
                if 'interface_df_election' not in parsed_dict['vrf'][vrf]['address_family'] \
                        [af_name]['rp']['bidir']:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['bidir']['interface_df_election'] = {}

                if rp_address and interface:
                    interface_df_election = rp_address + " " + interface
                    if interface_df_election not in parsed_dict['vrf'][vrf]['address_family'][af_name] \
                            ['rp']['bidir']['interface_df_election']:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election] = {}
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                        ['interface_df_election'][interface_df_election]['interface_name'] = interface
                    if rp_address:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['address'] = rp_address
                    if df_address:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['df_address'] = df_address

                    if interface_state:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['interface_state'] = interface_state

                    if ordinal:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['df_ordinal'] = int(ordinal)

                    if metrics_pref:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['metric_pref'] = int(metrics_pref)

                    if metrics:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['metric'] = int(metrics)

                    if group_range:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['group_range'] = group_range

                    if winner_metrics_pref:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election] \
                            ['winner_metric_pref'] = int(winner_metrics_pref)

                    if winner_metrics:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election] \
                            ['winner_metric'] = int(winner_metrics)

                    if df_uptime:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['df_uptime'] = df_uptime

        return parsed_dict



# ==============================================
# schema Parser for 'show ip pim df [vrf <vrf>]'
# ==============================================
class ShowIpPimDfSchema(MetaParser):
    """Schema for:
        show ip pim df
        show ip pim df vrf <vrf>"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        Optional('rp'): {
                            Optional('bidir'): {
                                Optional('interface_df_election'): {
                                    Optional(Any()): {
                                        Optional('address'): str,
                                        Optional('df_ordinal'): int,
                                        Optional('df_bits'): str,
                                        Optional('metric_pref'): int,
                                        Optional('metric'): int,
                                        Optional('group_range'): str,
                                        Optional('interface_name'): str,
                                        Optional('df_address'): str,
                                        Optional('df_uptime'): str,
                                        Optional('interface_state'): str,
                                        Optional('winner_metric_pref'): int,
                                        Optional('winner_metric'): int,
                                        Optional('is_rpf'): bool,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ==========================================================
#  parser for show ip pim df [vrf <vrf>]
#
# ==========================================================
class ShowIpPimDf(ShowIpPimDfSchema):
    """Parser for:
        show ip pim df
        show ip pim df vrf <vrf>"""

    def cli(self, vrf=""):

        if vrf:
            cmd = 'show ip pim df vrf {}'.format(vrf)
        else:
            cmd = 'show ip pim df'

        out = self.device.execute(cmd)
        af_name = 'ipv4'
        # Init dictionary
        parsed_dict = dict()
        vrf = ordinal = df_uptime = df_bits = df_address = interface = rp_address = is_rpf = ""

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Bidir-PIM Designated Forwarder Information for VRF "default"
            p1 = re.compile(r'^\s*Bidir-PIM +Designated +Forwarder'
                            ' +Information +for +VRF \"(?P<vrf>[\w]+)\"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                ordinal = df_uptime = df_bits = df_address = interface = rp_address = is_rpf = ""

            # RP Address (ordinal)   DF-bits          RP Metric  Group Range
            # 2.2.2.2 (2)            00000002 (1)     [0/0]      224.128.0.0/9
            p2 = re.compile(r'^\s*(?P<rp_address>[\d\.]+) +\((?P<ordinal>\d+)\)'
                            ' +(?P<df_bits>[\w\s\(\)]+)'
                            ' +\[(?P<metrics_pref>\d+)/(?P<metrics>\d+)\] +(?P<group_range>[\d\.\/]+)$')
            m = p2.match(line)
            if m:
                rp_address = m.groupdict()['rp_address']
                ordinal = m.groupdict()['ordinal']
                df_bits = m.groupdict()['df_bits'].rstrip()
                metrics_pref = m.groupdict()['metrics_pref']
                metrics = m.groupdict()['metrics']
                group_range = m.groupdict()['group_range']

            # Interface            DF Address       DF State   DF Metric    DF Uptime
            #  Loopback0            1.1.1.1          Winner     [0/0]        00:28:14   (RPF)
            #  Ethernet2/2                 10.2.0.2         Lose       [0/0]        00:28:14

            p3 = re.compile(r'^\s*(?P<interface>\S+) +(?P<df_address>\S+)'
                            ' +(?P<df_state>\w+)'
                            ' +\[(?P<winner_metrics_pref>\d+)/(?P<winner_metrics>\d+)\]'
                            ' +(?P<df_uptime>\S+)'
                            '( +\((?P<is_rpf>\S+)\))?$')
            m = p3.match(line)
            if m:
                interface = Common.convert_intf_name(m.groupdict()['interface'])
                df_address = m.groupdict()['df_address']
                interface_state = m.groupdict()['df_state'].lower()
                if interface_state == 'winner':
                    interface_state = 'win'
                winner_metrics_pref = m.groupdict()['winner_metrics_pref']
                winner_metrics = m.groupdict()['winner_metrics']
                df_uptime = m.groupdict()['df_uptime']
                if m.groupdict()['is_rpf'] and 'rpf' in m.groupdict()['is_rpf'].lower():
                    is_rpf = True

            if vrf and rp_address:
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}

                if 'address_family' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['address_family'] = {}
                if af_name not in parsed_dict['vrf'][vrf]['address_family']:
                    parsed_dict['vrf'][vrf]['address_family'][af_name] = {}

                if 'rp' not in parsed_dict['vrf'][vrf]['address_family'][af_name]:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['rp'] = {}
                if 'bidir' not in parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] = {}
                if 'interface_df_election' not in parsed_dict['vrf'][vrf]['address_family'] \
                        [af_name]['rp']['bidir']:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['bidir']['interface_df_election'] = {}

                if rp_address and interface:
                    interface_df_election = rp_address + " " + interface
                    if interface_df_election not in parsed_dict['vrf'][vrf]['address_family'][af_name] \
                            ['rp']['bidir']['interface_df_election']:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election] = {}
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                        ['interface_df_election'][interface_df_election]['interface_name'] = interface
                    if rp_address:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['address'] = rp_address
                    if df_address:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['df_address'] = df_address

                    if interface_state:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['interface_state'] = interface_state

                    if is_rpf:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['is_rpf'] = is_rpf

                    if ordinal:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['df_ordinal'] = int(ordinal)

                    if df_bits:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['df_bits'] = df_bits

                    if metrics_pref:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['metric_pref'] = int(metrics_pref)

                    if metrics:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['metric'] = int(metrics)

                    if group_range:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['group_range'] = group_range

                    if winner_metrics_pref:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election] \
                            ['winner_metric_pref'] = int(winner_metrics_pref)

                    if winner_metrics:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election] \
                            ['winner_metric'] = int(winner_metrics)

                    if df_uptime:
                        parsed_dict['vrf'][vrf]['address_family'][af_name]['rp']['bidir'] \
                            ['interface_df_election'][interface_df_election]['df_uptime'] = df_uptime

        return parsed_dict


# ============================================
# schema Parser for 'show ipv6 pim route'
# schema Parser for 'show ipv6 pim route vrf <vrf>'
# ============================================
class ShowIpv6PimRouteSchema(MetaParser):
    """Schema for:
        show ipv6 pim route
        show ipv6 pim route vrf <vrf>"""
    schema = {
        'vrf':{
            Any():{
                'address_family':{
                    Any():{
                        Optional('topology_tree_info'): {
                            Any():{
                                Optional('group'): str,
                                Optional('source_address'): str,
                                Optional('is_rpt'): bool,
                                Optional('rp_bit'): bool,
                                Optional('expiration'): str,
                                Optional('incoming_interface'): str,
                                Optional('mode'): str,
                                Optional('rp_address'): str,
                                Optional('rpf_neighbor'): str,
                                Optional('jp_holdtime_roundup'): int,
                                Optional('oif'):str,
                                Optional('oif_count'):int,
                                Optional('oif_timeout_count'):int,
                                Optional('oif_timeout'):str,
                                Optional('immediate'): str,
                                Optional('immediate_count'): int,
                                Optional('immediate_timeout_count'):int,
                                Optional('immediate_timeout'): str,
                                Optional('timeout_interval'): int,
                                Optional('sgr_prune_count'): int,
                                Optional('sgr_prune'): str,
                                Optional('route_fabric_owned'): bool,
                            },
                        },
                    },
                },
            },
        },
    }

# ==========================================================
#  parser for show ipv6 pim route
#  Parser for show ipv6 pim route vrf <vrf>
# ==========================================================
class ShowIpv6PimRoute(ShowIpv6PimRouteSchema):
    """Parser for:
        show ipv6 pim route
        show ipv6 pim route vrf <vrf>"""

    def cli(self, vrf=""):

        if vrf:
            cmd = 'show ipv6 pim route vrf {}'.format(vrf)
        else:
            cmd = 'show ipv6 pim route'
        output = self.device.execute(cmd)
        af_name = 'ipv6'
        rp_bit = False
        is_rpt = False
        mode = vrf_name = group = incoming_interface = imm_timeout_bf_str= imm_count = imm_timeout_count=\
            immf_bf_str = oif_bf_str = oif_timeout_bf_str = oif_count = oif_timeout_count = rp_address =\
            timeout_interval = sgr_count = sgr_prune_str = jp_round_up = rpf_nbr = expires = ""


        # Init dictionary
        parsed_output = dict()

        for line in output.splitlines():
            line = line.rstrip()

            # PIM6 Routing Table for VRF "VRF1" - 1 entries
            p1 = re.compile(r'^\s*PIM6 +Routing +Table +for +VRF +\"(?P<vrf_name>[\S]+)\" +\-'
                            ' +(?P<counter>\d+) +entries$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                group = ""

            # (*, ff08::/16), RP 2001:db8:12:12::12, bidir, expires 00:02:31 Route Fabric owned : FALSE, RP-bit
            # (*, ff30::/12), expires 00:02:31 Route Fabric owned : FALSE
            # (*, ff30::/12), expires 0.000000 Route Fabric owned : FALSE (00:00:02)
            p2 = re.compile(r'^\s*\((?P<source_address>[\S]+)'
                            ', +(?P<group>[\S]+)\),'
                            '( +RP +(?P<rp>[\S\-]+),)?( +(?P<mode>\w+),)?'
                            ' +expires +(?P<expires>[\w\.\:\(\)\s]+)'
                            ' +Route +Fabric +owned +: ((?P<fabric_owned>[\w]+)( *(?P<dummy>\S+))?)'
                            '(, +(?P<rp_bit>[\S]+))?$')
            m = p2.match(line)
            if m:
                rp_bit = False
                mode = incoming_interface = imm_timeout_bf_str = \
                    imm_count = imm_timeout_count = \
                    immf_bf_str = oif_bf_str = oif_timeout_bf_str = oif_count \
                    = oif_timeout_count = rp_address = \
                    timeout_interval = sgr_count = sgr_prune_str = jp_round_up = rpf_nbr = expires = ""

                group = m.groupdict()['group']
                source_address = m.groupdict()['source_address']
                if source_address == '*':
                    is_rpt = True
                else:
                    is_rpt = False

                route_fabric_owned = m.groupdict()['fabric_owned'].lower()

                expire_value = m.groupdict()['expires']
                if '(' in expire_value:
                    p2_1 = re.compile('^\s*(?P<expires_1>[\d\S]+) +\((?P<expires_2>[\S]+)\)$')
                    match_1 = p2_1.match(expire_value)
                    if match_1:
                        expires = match_1.groupdict()['expires_2']
                else:
                    expires = expire_value

                if m.groupdict()['mode']:
                    mode = m.groupdict()['mode']
                if m.groupdict()['rp_bit']:
                    rp_bit = True
                if m.groupdict()['rp']:
                    rp_address = m.groupdict()['rp'].replace('*','')


            # Incoming interface: Null, RPF nbr 0.0.0.0
            p3 = re.compile(r'^\s*Incoming +interface: (?P<incoming_interface>[\S]+),'
                           ' +RPF +nbr +(?P<rpf_nbr>[\S]+)$')
            m = p3.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']
                rpf_nbr = m.groupdict()['rpf_nbr']

            # Oif-list: (0) 00000000, timeout-list: (0) 00000000
            p4 = re.compile(r'^\s*Oif-list: +\((?P<oif_count>[\d]+)\)'
                            ' +(?P<oif_bf_str>[\S]+), +timeout\-list: +\((?P<timeout_count>[\d]+)\)'
                            ' +(?P<timeout_bf_str>[\S]+)$')
            m = p4.match(line)
            if m:
                oif_count = m.groupdict()['oif_count']
                oif_bf_str = m.groupdict()['oif_bf_str']
                oif_timeout_count = m.groupdict()['timeout_count']
                oif_timeout_bf_str = m.groupdict()['timeout_bf_str']

            # Immediate-list: (0) 00000000, timeout-list: (0) 00000000
            p5 = re.compile(r'^\s*Immediate-list: +\((?P<imm_count>[\d]+)\)'
                            ' +(?P<imm_bf_str>[\S]+), +timeout\-list: +\((?P<timeout_count>[\d]+)\)'
                            ' +(?P<timeout_bf_str>[\S]+)$')
            m = p5.match(line)
            if m:
                imm_count = m.groupdict()['imm_count']
                immf_bf_str = m.groupdict()['imm_bf_str']
                imm_timeout_count = m.groupdict()['timeout_count']
                imm_timeout_bf_str = m.groupdict()['timeout_bf_str']

            # Sgr-prune-list: (0) 00000000
            p5 = re.compile(r'^\s*Sgr-prune-list: +\((?P<sgr_count>[\d]+)\)'
                            ' +(?P<sgr_prune_str>[\S]+)$')
            m = p5.match(line)
            if m:
                sgr_count = m.groupdict()['sgr_count']
                sgr_prune_str = m.groupdict()['sgr_prune_str']

            # Timeout-interval: 3, JP-holdtime round-up: 3
            p6 = re.compile(r'^\s*Timeout-interval: +(?P<timeout_interval>\d+)'
                            ', +JP-holdtime +round-up: +(?P<jp_round_up>\d+)$')
            m = p6.match(line)
            if m:
                timeout_interval = m.groupdict()['timeout_interval']
                jp_round_up = m.groupdict()['jp_round_up']

            if vrf_name and group:
                if 'vrf' not in parsed_output:
                    parsed_output['vrf'] = {}
                if vrf_name not in parsed_output['vrf']:
                    parsed_output['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_output['vrf'][vrf_name]:
                    parsed_output['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_output['vrf'][vrf_name]['address_family']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name] = {}

                if 'topology_tree_info' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] = {}

                topology = group + " " + source_address + " " + str(is_rpt)

                if topology not in parsed_output['vrf'][vrf_name]['address_family']\
                        [af_name]['topology_tree_info']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology] = {}

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info']\
                    [topology]['group'] = group
                parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info']\
                    [topology]['source_address'] = source_address
                parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info']\
                    [topology]['expiration'] = expires
                parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                    [topology]['is_rpt'] = is_rpt
                if mode:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['mode'] = mode
                if rp_bit:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['rp_bit'] = rp_bit

                if incoming_interface:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['incoming_interface'] = incoming_interface
                if rp_address:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['rp_address'] = rp_address
                if rpf_nbr:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['rpf_neighbor'] = rpf_nbr
                if oif_count:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['oif_count'] = int(oif_count)
                if oif_bf_str:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['oif'] = oif_bf_str
                if oif_timeout_count:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['oif_timeout_count'] = int(oif_timeout_count)
                if oif_timeout_bf_str:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['oif_timeout'] = oif_timeout_bf_str
                if imm_count:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['immediate_count'] = int(imm_count)
                if immf_bf_str:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['immediate'] = immf_bf_str
                if imm_timeout_count:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['immediate_timeout_count'] = int(imm_timeout_count)
                if imm_timeout_bf_str:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['immediate_timeout'] = imm_timeout_bf_str
                if sgr_count:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['sgr_prune_count'] = int(sgr_count)
                if sgr_prune_str:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['sgr_prune'] = sgr_prune_str

                if timeout_interval:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['timeout_interval'] = int(timeout_interval)
                if jp_round_up:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['jp_holdtime_roundup'] = int(jp_round_up)
                if route_fabric_owned:
                    if route_fabric_owned.lower() == 'false':
                        route_val = False
                    else:
                        route_val = True
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['route_fabric_owned'] = route_val
                continue

        return parsed_output


# ===========================================
# schema Parser for 'show ipv6 pim neighbor'
# ===========================================
class ShowIpv6PimNeighborSchema(MetaParser):
    """Schema for show ipv6 pim neighbor"""
    schema = {
        'vrf':{
            Any():{
                'interfaces':{
                    Any():{
                        'address_family':{
                            Any():{
                                'neighbors':{
                                    Any():{
                                        Optional('bfd_status'): bool,
                                        Optional('expiration'): str,
                                        Optional('dr_priority'): int,
                                        Optional('up_time'): str,
                                        Optional('interface'): str,
                                        Optional('bidir_capable'): bool,
                                    },
                                    Optional('secondary_address'): list,
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ==========================================================
#  parser for show ipv6 pim neighbor
#  parser for show ipv6 pim neighbor vrf <word>
# ==========================================================
class ShowIpv6PimNeighbor(ShowIpv6PimNeighborSchema):
    """Parser for:
        show ipv6 pim neighbor
        show ipv6 pim neighbor vrf <vrf>"""

    def cli(self, vrf=""):

        if not vrf:
            cmd = 'show ipv6 pim neighbor'
        else:
            cmd = 'show ipv6 pim neighbor vrf {}'.format(vrf)

        output = self.device.execute(cmd)
        af_name = 'ipv6'

        # Init dictionary
        parsed_output = dict()
        second_address_flag = False
        secondary_address = []

        for line in output.splitlines():
            line = line.rstrip()

            # PIM Neighbor Status for VRF "VRF1"
            p1 = re.compile(r'^\s*PIM6 +Neighbor +Status +for +VRF +\"(?P<vrf_name>[\S]+)\"$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                neighbor = ""
                secondary_address = []
                continue

            #  Secondary addresses:
            p3 = re.compile(r'^\s*Secondary +addresses:$')
            m = p3.match(line)
            if m:
                second_address_flag = True
                continue

            #    2001:db8:11:33::33
            p4 = re.compile(r'^\s*(?P<space>\s{4})(?P<secondary_address>[\S]+)$')
            m = p4.match(line)
            if m:
                secondary_address.append(m.groupdict()['secondary_address'])
                if intf_name and vrf_name:
                    if 'vrf' not in parsed_output:
                        parsed_output['vrf'] = {}
                    if vrf_name not in parsed_output['vrf']:
                        parsed_output['vrf'][vrf_name] = {}

                    if 'interfaces' not in parsed_output['vrf'][vrf_name]:
                        parsed_output['vrf'][vrf_name]['interfaces'] = {}
                    if intf_name not in parsed_output['vrf'][vrf_name]['interfaces']:
                        parsed_output['vrf'][vrf_name]['interfaces'][intf_name] = {}

                    if 'address_family' not in parsed_output['vrf'][vrf_name]['interfaces'][intf_name]:
                        parsed_output['vrf'][vrf_name]['interfaces'][intf_name]['address_family'] = {}
                    if af_name not in parsed_output['vrf'][vrf_name]['interfaces']\
                            [intf_name]['address_family']:
                        parsed_output['vrf'][vrf_name]['interfaces'][intf_name]\
                            ['address_family'][af_name] = {}

                    if 'neighbors' not in parsed_output['vrf'][vrf_name]['interfaces']\
                            [intf_name]['address_family'][af_name]:
                        parsed_output['vrf'][vrf_name]['interfaces'] \
                            [intf_name]['address_family'][af_name]['neighbors'] = {}

                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'] \
                        ['secondary_address'] = secondary_address

                continue

            # Neighbor Address              Interface   Uptime    Expires   DR   Bidir-  BFD
            #                                                               Pri  Capable State
            # fe80::5054:ff:fe5b:aa80       Eth2/2      07:31:36  00:01:28  1    yes     n/a
            p2 = re.compile(r'^\s*(?P<neighbor>[\S]+)'
                            ' +(?P<intf_name>[\S]+)'
                            ' +(?P<up_time>[\S]+)'
                            ' +(?P<expires>[\S]+)'
                            ' +(?P<dr_priority>\d+)'
                            ' +(?P<bidir_capable>\w+)'
                            ' +(?P<bfd_state>[\S]+)$')
            m = p2.match(line)
            if m:
                neighbor = m.groupdict()['neighbor']
                intf_name = Common.convert_intf_name(m.groupdict()['intf_name'])
                up_time = m.groupdict()['up_time']
                expires = m.groupdict()['expires']
                dr_priority = int(m.groupdict()['dr_priority'])
                bidir_capable = True if m.groupdict()['bidir_capable'].lower() == 'yes' else False
                bfd_state = m.groupdict()['bfd_state']


                if intf_name and vrf_name:
                    if 'vrf' not in parsed_output:
                        parsed_output['vrf'] = {}
                    if vrf_name not in parsed_output['vrf']:
                        parsed_output['vrf'][vrf_name] = {}

                    if 'interfaces' not in parsed_output['vrf'][vrf_name]:
                        parsed_output['vrf'][vrf_name]['interfaces'] = {}
                    if intf_name not in parsed_output['vrf'][vrf_name]['interfaces']:
                        parsed_output['vrf'][vrf_name]['interfaces'][intf_name] = {}

                    if 'address_family' not in parsed_output['vrf'][vrf_name]['interfaces'][intf_name]:
                        parsed_output['vrf'][vrf_name]['interfaces'][intf_name]['address_family'] = {}
                    if af_name not in parsed_output['vrf'][vrf_name]['interfaces']\
                            [intf_name]['address_family']:
                        parsed_output['vrf'][vrf_name]['interfaces'][intf_name]\
                            ['address_family'][af_name] = {}

                    if 'neighbors' not in parsed_output['vrf'][vrf_name]['interfaces']\
                            [intf_name]['address_family'][af_name]:
                        parsed_output['vrf'][vrf_name]['interfaces'] \
                            [intf_name]['address_family'][af_name]['neighbors'] = {}

                    if neighbor not in  parsed_output['vrf'][vrf_name]['interfaces'] \
                            [intf_name]['address_family'][af_name]['neighbors']:
                        parsed_output['vrf'][vrf_name]['interfaces'] \
                            [intf_name]['address_family'][af_name]['neighbors'][neighbor] = {}

                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]\
                            ['neighbors'][neighbor]['bfd_status'] = False if 'n/a' in bfd_state else True

                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'][neighbor]['expiration'] = expires
                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'][neighbor]['dr_priority'] = dr_priority
                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'][neighbor]['up_time'] = up_time
                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'][neighbor]['interface'] =intf_name
                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'][neighbor]\
                        ['bidir_capable'] = bidir_capable

                continue

        return parsed_output


# ============================================
# schema Parser for 'show ip pim route'
# ============================================
class ShowIpPimRouteSchema(MetaParser):
    """Schema for:
        show ip pim route
        show ip pim route vrf <vrf>"""

    schema = {
        'vrf':{
            Any():{
                'address_family':{
                    Any():{
                        Optional('topology_tree_info'): {  # Ops From cmds [show ip mroute vrf all|show ipv6 mroute vrf all]
                            Any():{#[group source_address is_rpt]: {  # Ops '232.0.0.0/8 * True'
                                Optional('group'): str,  # Ops '232.0.0.0/8'
                                Optional('source_address'): str,  # Ops '*'|'192.168.1.1'
                                Optional('is_rpt'): bool,  # Ops True|False (True if source-address is '*')
                                Optional('rp_bit'): bool,
                                Optional('expiration'): str,  # Ops '00:01:58' from show ip|ipv6 pim route vrf all
                                Optional('incoming_interface'): str,  # Ops 'Ethernet1/34'
                                Optional('mode'): str,  # Ops 'none'|'ssm'|'asm'|'bidir'|'dm'|'other'
                                Optional('rp_address'): str,  # Ops '2.2.2.2'
                                Optional('rpf_neighbor'): str,  # Ops '11.1.0.1'
                                Optional('jp_holdtime_roundup'): int,
                                Optional('oif'):str,
                                Optional('oif_count'):int,
                                Optional('oif_timeout_count'):int,
                                Optional('oif_timeout'):str,
                                Optional('immediate'): str,
                                Optional('immediate_count'): int,
                                Optional('immediate_timeout_count'):int,
                                Optional('immediate_timeout'): str,
                                Optional('timeout_interval'): int,
                                Optional('sgr_prune_count'): int,
                                Optional('sgr_prune'): str,
                            },
                        },
                    },
                },
            },
        },
    }

# ==========================================================
#  parser for show ip pim route
#  parser for show ip pim route vrf <word>
# ==========================================================
class ShowIpPimRoute(ShowIpPimRouteSchema):
    """Parser for:
        show ip pim route
        show ip pim route vrf <vrf>"""

    def cli(self, vrf=""):

        if not vrf:
            cmd = 'show ip pim route'
        else:
            cmd = 'show ip pim route vrf {}'.format(vrf)

        output = self.device.execute(cmd)
        af_name = 'ipv4'
        rp_bit = False
        is_rpt = False
        mode = vrf_name = group = incoming_interface = imm_timeout_bf_str= imm_count = imm_timeout_count=\
            immf_bf_str = oif_bf_str = oif_timeout_bf_str = oif_count = oif_timeout_count = rp_address =\
            timeout_interval = sgr_count = sgr_prune_str = jp_round_up = rpf_nbr = expires = ""


        # Init dictionary
        parsed_output = dict()

        for line in output.splitlines():
            line = line.rstrip()

            # PIM Routing Table for VRF "VRF1" - 1 entries
            p1 = re.compile(r'^\s*PIM +Routing +Table +for +VRF +\"(?P<vrf_name>[\S]+)\" +\-'
                            ' +(?P<counter>\d+) +entries$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                group = ""

            # (*, 232.0.0.0/8), expires 0.000000 (00:00:01)
            # (*, 233.0.0.0/24), RP 12.12.12.12, bidir, expires 00:01:58, RP-bit
            p2 = re.compile(r'^\s*\((?P<source_address>[\S]+)'
                            ', +(?P<group>[\S]+)\),'
                            '( +RP +(?P<rp>[\S\-]+),)?( +(?P<mode>\w+),)?'
                            ' +expires +(?P<expires>[\w\.\:\(\)\s]+)'
                            '(, +(?P<rp_bit>[\S]+))?$')
            m = p2.match(line)
            if m:
                rp_bit = False
                mode = incoming_interface = imm_timeout_bf_str = \
                    imm_count = imm_timeout_count = \
                    immf_bf_str = oif_bf_str = oif_timeout_bf_str = oif_count \
                    = oif_timeout_count = rp_address = \
                    timeout_interval = sgr_count = sgr_prune_str = jp_round_up = rpf_nbr = expires = ""

                group = m.groupdict()['group']
                source_address = m.groupdict()['source_address']
                if source_address == '*':
                    is_rpt = True
                else:
                    is_rpt = False
                expire_value = m.groupdict()['expires']
                if '(' in expire_value:
                    p2_1 = re.compile('^\s*(?P<expires_1>[\d\S]+) +\((?P<expires_2>[\S]+)\)$')
                    match_1 = p2_1.match(expire_value)
                    if match_1:
                        expires = match_1.groupdict()['expires_2']
                else:
                    expires = expire_value

                if m.groupdict()['mode']:
                    mode = m.groupdict()['mode']
                if m.groupdict()['rp_bit']:
                    rp_bit = True
                if m.groupdict()['rp']:
                    rp_address = m.groupdict()['rp'].replace('*','')


            # Incoming interface: Null, RPF nbr 0.0.0.0
            p3 = re.compile(r'^\s*Incoming +interface: (?P<incoming_interface>[\S]+),'
                           ' +RPF +nbr +(?P<rpf_nbr>[\S]+)$')
            m = p3.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']
                rpf_nbr = m.groupdict()['rpf_nbr']

            # Oif-list: (0) 00000000, timeout-list: (0) 00000000
            p4 = re.compile(r'^\s*Oif-list: +\((?P<oif_count>[\d]+)\)'
                            ' +(?P<oif_bf_str>[\S]+), +timeout\-list: +\((?P<timeout_count>[\d]+)\)'
                            ' +(?P<timeout_bf_str>[\S]+)$')
            m = p4.match(line)
            if m:
                oif_count = m.groupdict()['oif_count']
                oif_bf_str = m.groupdict()['oif_bf_str']
                oif_timeout_count = m.groupdict()['timeout_count']
                oif_timeout_bf_str = m.groupdict()['timeout_bf_str']

            # Immediate-list: (0) 00000000, timeout-list: (0) 00000000
            p5 = re.compile(r'^\s*Immediate-list: +\((?P<imm_count>[\d]+)\)'
                            ' +(?P<imm_bf_str>[\S]+), +timeout\-list: +\((?P<timeout_count>[\d]+)\)'
                            ' +(?P<timeout_bf_str>[\S]+)$')
            m = p5.match(line)
            if m:
                imm_count = m.groupdict()['imm_count']
                immf_bf_str = m.groupdict()['imm_bf_str']
                imm_timeout_count = m.groupdict()['timeout_count']
                imm_timeout_bf_str = m.groupdict()['timeout_bf_str']

            # Sgr-prune-list: (0) 00000000
            p5 = re.compile(r'^\s*Sgr-prune-list: +\((?P<sgr_count>[\d]+)\)'
                            ' +(?P<sgr_prune_str>[\S]+)$')
            m = p5.match(line)
            if m:
                sgr_count = m.groupdict()['sgr_count']
                sgr_prune_str = m.groupdict()['sgr_prune_str']

            # Timeout-interval: 3, JP-holdtime round-up: 3
            p6 = re.compile(r'^\s*Timeout-interval: +(?P<timeout_interval>\d+)'
                            ', +JP-holdtime +round-up: +(?P<jp_round_up>\d+)$')
            m = p6.match(line)
            if m:
                timeout_interval = m.groupdict()['timeout_interval']
                jp_round_up = m.groupdict()['jp_round_up']

            if vrf_name and group:
                if 'vrf' not in parsed_output:
                    parsed_output['vrf'] = {}
                if vrf_name not in parsed_output['vrf']:
                    parsed_output['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_output['vrf'][vrf_name]:
                    parsed_output['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_output['vrf'][vrf_name]['address_family']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name] = {}

                if 'topology_tree_info' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] = {}

                topology = group + " " + source_address + " " + str(is_rpt)

                if topology not in parsed_output['vrf'][vrf_name]['address_family']\
                        [af_name]['topology_tree_info']:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology] = {}

                parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info']\
                    [topology]['group'] = group
                parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info']\
                    [topology]['source_address'] = source_address
                parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info']\
                    [topology]['expiration'] = expires
                parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                    [topology]['is_rpt'] = is_rpt
                if mode:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['mode'] = mode
                if rp_bit:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['rp_bit'] = rp_bit

                if incoming_interface:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['incoming_interface'] = incoming_interface
                if rp_address:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['rp_address'] = rp_address
                if rpf_nbr:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['rpf_neighbor'] = rpf_nbr
                if oif_count:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['oif_count'] = int(oif_count)
                if oif_bf_str:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['oif'] = oif_bf_str
                if oif_timeout_count:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['oif_timeout_count'] = int(oif_timeout_count)
                if oif_timeout_bf_str:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['oif_timeout'] = oif_timeout_bf_str
                if imm_count:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['immediate_count'] = int(imm_count)
                if immf_bf_str:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['immediate'] = immf_bf_str
                if imm_timeout_count:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['immediate_timeout_count'] = int(imm_timeout_count)
                if imm_timeout_bf_str:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['immediate_timeout'] = imm_timeout_bf_str
                if sgr_count:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['sgr_prune_count'] = int(sgr_count)
                if sgr_prune_str:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['sgr_prune'] = sgr_prune_str

                if timeout_interval:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['timeout_interval'] = int(timeout_interval)
                if jp_round_up:
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['topology_tree_info'] \
                        [topology]['jp_holdtime_roundup'] = int(jp_round_up)
                continue

        return parsed_output


# ==================================================
# schema Parser for 'show ipv6 pim group-range'
# ==================================================
class ShowIpv6PimGroupRangeSchema(MetaParser):
    """Schema for show ipv6 pim group-range"""

    schema = {
        'vrf':{
            Any():{
                'address_family':{
                    Any():{
                        'sm':{
                            Any():{
                                Any():{
                                    Optional('mode'): str,
                                    Optional('rp_address'): str,
                                    Optional('shared_tree_only'): str,
                                    Optional('range'): str,
                                },
                            },

                        },
                    },
                },
            },
        },
    }


# ==========================================================
#  parser for show ipv6 pim group-range
#  parser for show ipv6 pim group-range vrf <vrf>
# ==========================================================
class ShowIpv6PimGroupRange(ShowIpv6PimGroupRangeSchema):
    """Parser for:
        show ipv6 pim group-range
        show ipv6 pim group-range vrf <vrf>"""

    def cli(self, vrf=""):

        if not vrf:
            cmd = 'show ipv6 pim group-range'
        else:
            cmd = 'show ipv6 pim group-range vrf {}'.format(vrf)


        output = self.device.execute(cmd)
        af_name = 'ipv6'

        # Init dictionary
        parsed_output = dict()

        if vrf:
            vrf_name = vrf

        for line in output.splitlines():
            line = line.rstrip()

            # PIM6 Group-Range Configuration for VRF "VRF1"
            p1 = re.compile(r'^\s*PIM6 +Group\-Range +Configuration +for +VRF +\"(?P<vrf_name>[\S]+)\"$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                mode = ""
                continue

            # Group-range               Mode      RP-address          Shared-tree-only range
            # ff3x::/32                 SSM       -                   -
            p2 = re.compile(r'^\s*(?P<group_range>[^\s*Group-range][\S]+)'
                            ' +(?P<mode>[\S]+)'
                            ' +(?P<rp_address>[\S]+)'
                            '( +(?P<shared_tree_only>[\S]+))?'
                            '( +(?P<range>[\S]+))?$')
            m = p2.match(line)
            if m:
                group_range = m.groupdict()['group_range']
                mode = m.groupdict()['mode'].lower()
                rp_address = m.groupdict()['rp_address']
                if m.groupdict()['shared_tree_only']:
                    shared_tree_only = m.groupdict()['shared_tree_only']
                if m.groupdict()['range']:
                    range = m.groupdict()['range']

                if group_range and vrf_name and mode:
                    if 'vrf' not in parsed_output:
                        parsed_output['vrf'] = {}
                    if vrf_name not in parsed_output['vrf']:
                        parsed_output['vrf'][vrf_name] = {}

                    if 'address_family' not in parsed_output['vrf'][vrf_name]:
                        parsed_output['vrf'][vrf_name]['address_family'] = {}
                    if af_name not in parsed_output['vrf'][vrf_name]['address_family']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name] = {}

                    if 'sm' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'] = {}

                    if mode not in parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode] = {}

                    if group_range not in parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode]:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range] = {}

                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range]\
                        ['mode'] = mode
                    if '-' not in rp_address:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range]\
                            ['rp_address'] = rp_address
                    if m.groupdict()['shared_tree_only'] and '-' not in m.groupdict()['shared_tree_only']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range] \
                            ['shared_tree_only'] = shared_tree_only
                    if m.groupdict()['range']  and '-' not in m.groupdict()['range']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range] \
                            ['range'] = range.lower()

                continue


        return parsed_output


# ==================================================
# schema Parser for 'show ip pim neighbor'
# ==================================================
class ShowIpPimNeighborSchema(MetaParser):
    """Schema for show ip pim neighbor"""
    schema = {
        'vrf':{
            Any():{
                'interfaces':{
                    Any():{
                        'address_family':{
                            Any():{
                                'neighbors':{
                                    Any():{
                                        'bfd_status': bool,
                                        'expiration': str,
                                        'dr_priority': int,
                                        'up_time': str,
                                        'interface': str,
                                        'bidir_capable': bool,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

# ==========================================================
#  parser for show ip pim neighbor vrf all
#  parser for show ip pim neighbor vrf <vrf>
# ==========================================================
class ShowIpPimNeighbor(ShowIpPimNeighborSchema):
    """Parser for:
        show ip pim neighbor
        show ip pim neighbor vrf <vrf>"""

    def cli(self, vrf=""):

        if not vrf:
            cmd = 'show ip pim neighbor'
        else:
            cmd = 'show ip pim neighbor vrf {}'.format(vrf)

        output = self.device.execute(cmd)
        af_name = 'ipv4'

        # Init dictionary
        parsed_output = dict()


        for line in output.splitlines():
            line = line.rstrip()

            # PIM Neighbor Status for VRF "VRF1"
            p1 = re.compile(r'^\s*PIM +Neighbor +Status +for +VRF +\"(?P<vrf_name>[\S]+)\"$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                continue

            # Neighbor        Interface            Uptime    Expires   DR       Bidir-  BFD
            #                                              Priority Capable State
            # 10.11.33.33     Ethernet2/2          07:31:30  00:01:25  1        yes     n/a
            
            # Neighbor        Interface            Uptime    Expires   DR       Bidir-  BFD    ECMP Redirect
            #                                                          Priority Capable State     Capable
            # 10.2.3.3        Ethernet1/3.11       00:31:08  00:01:39  1        yes     n/a     no
            p2 = re.compile(r'^\s*(?P<neighbor>[\S]+)'
                            ' +(?P<intf_name>[\S]+)'
                            ' +(?P<up_time>[\S]+)'
                            ' +(?P<expires>[\S]+)'
                            ' +(?P<dr_priority>\d+)'
                            ' +(?P<bidir_capable>\w+)'
                            ' +(?P<bfd_state>[\S]+)'
                            '( +(?P<redict_capable>[\S]+))?$')
            m = p2.match(line)
            if m:
                neighbor = m.groupdict()['neighbor']
                intf_name = m.groupdict()['intf_name']
                up_time = m.groupdict()['up_time']
                expires = m.groupdict()['expires']
                dr_priority = int(m.groupdict()['dr_priority'])
                bidir_capable = True if m.groupdict()['bidir_capable'].lower() == 'yes' else False
                bfd_state = m.groupdict()['bfd_state']


                if intf_name and vrf_name:
                    if 'vrf' not in parsed_output:
                        parsed_output['vrf'] = {}
                    if vrf_name not in parsed_output['vrf']:
                        parsed_output['vrf'][vrf_name] = {}

                    if 'interfaces' not in parsed_output['vrf'][vrf_name]:
                        parsed_output['vrf'][vrf_name]['interfaces'] = {}
                    if intf_name not in parsed_output['vrf'][vrf_name]['interfaces']:
                        parsed_output['vrf'][vrf_name]['interfaces'][intf_name] = {}

                    if 'address_family' not in parsed_output['vrf'][vrf_name]['interfaces'][intf_name]:
                        parsed_output['vrf'][vrf_name]['interfaces'][intf_name]['address_family'] = {}
                    if af_name not in parsed_output['vrf'][vrf_name]['interfaces']\
                            [intf_name]['address_family']:
                        parsed_output['vrf'][vrf_name]['interfaces'][intf_name]\
                            ['address_family'][af_name] = {}

                    if 'neighbors' not in parsed_output['vrf'][vrf_name]['interfaces']\
                            [intf_name]['address_family'][af_name]:
                        parsed_output['vrf'][vrf_name]['interfaces'] \
                            [intf_name]['address_family'][af_name]['neighbors'] = {}

                    if neighbor not in  parsed_output['vrf'][vrf_name]['interfaces'] \
                            [intf_name]['address_family'][af_name]['neighbors']:
                        parsed_output['vrf'][vrf_name]['interfaces'] \
                            [intf_name]['address_family'][af_name]['neighbors'][neighbor] = {}

                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]\
                            ['neighbors'][neighbor]['bfd_status'] = False if 'n/a' in bfd_state else True

                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'][neighbor]['expiration'] = expires
                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'][neighbor]['dr_priority'] = dr_priority
                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'][neighbor]['up_time'] = up_time
                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'][neighbor]['interface'] =intf_name
                    parsed_output['vrf'][vrf_name]['interfaces'] \
                        [intf_name]['address_family'][af_name]['neighbors'][neighbor]['bidir_capable'] = bidir_capable
                continue



        return parsed_output


# =============================================
# schema Parser for 'show ip pim vrf all detail'
# ==============================================
class ShowIpPimVrfDetailSchema(MetaParser):
    """Schema for show ip pim vrf all detail"""
    schema = {
            'vrf':{
                Any():{
                    'address_family':{
                        Any():{
                            Optional('sm'):{
                                Optional('asm'):{
                                    Optional('register_source'): str,
                                    Optional('register_source_address'): str,
                                    Optional('sg_expiry_timer'):{
                                        Optional('sg_list'): str,
                                        Optional('infinity'): bool,
                                        Optional('sg_expiry_timer_configured'): bool,
                                        Optional('sg_expiry_timer'): int,
                                        Optional('config_version'): int,
                                        Optional('active_version'): int,

                                        },
                                    },
                                },
                            Optional('vrf_id'): int,
                            Optional('table_id'): str,
                            Optional('interface_count'): int,
                            Optional('bfd'): {
                                Optional('enable'): bool,
                            },
                            Optional('mvpn'): {
                                Optional('enable'): bool,
                            },
                            Optional('state_limit'): str,
                            Optional('register_rate_limit'): str,
                            Optional('cli_vrf_done'): bool,
                            Optional('cibtype_auto_enabled'): bool,
                            Optional('vxlan_vni_id'): int,
                            Optional('shared_tree_ranges'): str,
                            Optional('pre_build_spt'): str,
                        },
                    },
                },
            },
        }

# ==========================================================
#  parser for show ip pim vrf all detail
#
# ==========================================================
class ShowIpPimVrfDetail(ShowIpPimVrfDetailSchema):
    """Parser for:
        show ip pim vrf detail
        show ip pim vrf <vrf> detail"""

    def cli(self, vrf=""):

        if vrf:
            cmd = 'show ip pim vrf {} detail'.format(vrf)
        else:
            cmd = 'show ip pim vrf detail'

        out = self.device.execute(cmd)
        af_name = 'ipv4'

        # Init dictionary
        parsed_dict = dict()
        intf_name = ""
        expiry_timer_configured = sg_expiry_timer_infinity = False
        sg_expiry_timer = ""

        for line in out.splitlines():
            line = line.rstrip()

            #VRF Name              VRF      Table       Interface  BFD        MVPN
            #          ID       ID          Count      Enabled    Enabled
            # default               1        0x00000001  3          no          no
            p1 = re.compile(r'^\s*(?P<vrf>[\w\d]+) +(?P<vrf_id>\d+)'
                            ' +(?P<table_id>0x[a_f0-9]+) +(?P<interface_count>\d+)'
                            ' +(?P<bfd>\w+)? +(?P<mvpn>\w+)?$')
            m = p1.match(line)
            if m:
                expiry_timer_configured = sg_expiry_timer_infinity = False
                sg_expiry_timer = ""
                vrf_name = m.groupdict()['vrf']
                vrf_id = int(m.groupdict()['vrf_id'])
                table_id = m.groupdict()['table_id']
                interface_count = int(m.groupdict()['interface_count'])
                bfd_enabled = True if m.groupdict()['bfd'].lower() == 'yes' else False
                mvpn_enabled = True if m.groupdict()['mvpn'].lower() == 'yes' else False

                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}

                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}

                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}


                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['vrf_id'] = vrf_id

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['table_id'] = table_id
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['interface_count'] = interface_count

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['bfd'] = {}
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['bfd']['enable'] = bfd_enabled

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['mvpn'] = {}
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['mvpn']['enable'] = mvpn_enabled

                continue

            # State Limit: None
            p2 = re.compile(r'^\s*State +Limit: +(?P<state_limit>(?!None)\w+)$')
            m = p2.match(line)
            if m:
                state_limit = m.groupdict()['state_limit'].lower()
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}

                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['state_limit'] = state_limit


            # Register Rate Limit: none
            p3 = re.compile(r'^\s*Register +Rate +Limit: +(?P<register_rate_limit>(?!none)\w+)$')
            m = p3.match(line)
            if m:
                register_rate_limit = m.groupdict()['register_rate_limit'].lower()
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}

                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['register_rate_limit'] = register_rate_limit

            # Register source  interface : loopback0 address : 1.1.1.1
            p4 = re.compile(r'^\s*Register +source +interface +: +(?P<intf_name>[\w\d\S]+)'
                            ' +address +: +(?P<address>[\w\d\S]+)$')
            m = p4.match(line)
            if m:
                register_source = m.groupdict()['intf_name']
                register_source_address = m.groupdict()['address']

                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}

                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}


                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['vrf_id'] = vrf_id

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['table_id'] = table_id


                if register_source:
                    if 'sm' not in parsed_dict['vrf'][vrf_name]['address_family'][af_name]:
                        parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm'] = {}
                    if 'asm' not in parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']:
                        parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm'] = {}

                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm']\
                        ['register_source'] = register_source

                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm'] \
                        ['register_source_address'] = register_source_address

                continue

            # Shared tree ranges: none
            p5 = re.compile(r'^\s*Shared +tree +ranges: +(?P<shared_tree_ranges>(?!none)\w+)$')
            m = p5.match(line)
            if m:
                shared_tree_ranges = m.groupdict()['shared_tree_ranges']

                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['shared_tree_ranges'] = shared_tree_ranges
                #continue

            # (S,G)-expiry timer: configured, infinity
            # (S,G)-expiry timer: configured, 1200 secs
            p7 = re.compile(r'^\s*\(S\,G\)\-expiry +timer: +(?P<expiry_timer_configured>\w+)'
                            '(, +(?P<sg_expiry_timer_infinity>[\w]+))?'
                            '(, +(?P<sg_expiry_timer>[\d]+) +secs)?$')
            m = p7.match(line)
            if m:
                if m.groupdict()['expiry_timer_configured']:
                    expiry_timer_configured = True if m.groupdict()['expiry_timer_configured']\
                        == 'configured' else False

                if m.groupdict()['sg_expiry_timer_infinity']:
                    sg_expiry_timer_infinity = True if m.groupdict()['sg_expiry_timer_infinity']\
                                                       .lower() == 'infinity' else False

                if m.groupdict()['sg_expiry_timer']:
                    sg_expiry_timer = m.groupdict()['sg_expiry_timer']


                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}

                if 'sm' not in parsed_dict['vrf'][vrf_name]['address_family'][af_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm'] = {}
                if 'asm' not in parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm'] = {}
                if 'sg_expiry_timer' not in parsed_dict['vrf'][vrf_name]['address_family']\
                        [af_name]['sm']['asm']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm']['sg_expiry_timer'] = {}
                if sg_expiry_timer_infinity:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm']\
                    ['sg_expiry_timer']['infinity'] = sg_expiry_timer_infinity
                if expiry_timer_configured:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm'] \
                    ['sg_expiry_timer']['sg_expiry_timer_configured'] = expiry_timer_configured

                if sg_expiry_timer:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm'] \
                    ['sg_expiry_timer']['sg_expiry_timer'] = int(sg_expiry_timer)

                continue

            #  (S,G)-list policy: sg-expiry-timer-sg-list
            p8 = re.compile(r'^\s*\(S\,G\)\-list +policy: +(?P<sg_list_policy>(?!none)[\w\S]+)$')
            m = p8.match(line)
            if m:
                sg_list_policy = m.groupdict()['sg_list_policy']

                if 'sm' not in parsed_dict['vrf'][vrf_name]['address_family'][af_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm'] = {}
                if 'asm' not in parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm'] = {}
                if 'sg_expiry_timer' not in parsed_dict['vrf'][vrf_name]['address_family']\
                        [af_name]['sm']['asm']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm']['sg_expiry_timer'] = {}
                parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm']\
                    ['sg_expiry_timer']['sg_list'] = sg_list_policy
                continue

            #  (S,G)-expiry timer config version 1, active version 1
            p9 = re.compile(r'^\s*\(S\,G\)\-expiry +timer +config +version +(?P<expiry_timer_config_version>\d+)'
                            '+, +active +version +(?P<expiry_timer_active_version>\d+)$')
            m = p9.match(line)
            if m:
                expiry_timer_config_version = int(m.groupdict()['expiry_timer_config_version'])
                expiry_timer_active_version = int(m.groupdict()['expiry_timer_active_version'])

                if 'sm' not in parsed_dict['vrf'][vrf_name]['address_family'][af_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm'] = {}
                if 'asm' not in parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm'] = {}
                if 'sg_expiry_timer' not in parsed_dict['vrf'][vrf_name]['address_family']\
                        [af_name]['sm']['asm']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm']['sg_expiry_timer'] = {}

                parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm']\
                    ['sg_expiry_timer']['active_version'] = expiry_timer_active_version
                parsed_dict['vrf'][vrf_name]['address_family'][af_name]['sm']['asm'] \
                    ['sg_expiry_timer']['config_version'] = expiry_timer_config_version

                continue

            # Pre-build SPT for all (S,G)s in VRF: disabled
            p10 = re.compile(r'^\s*Pre\-build +SPT +for +all +\(S\,G\)s +in +VRF: +(?P<pre_build_spt>\w+)$')
            m = p10.match(line)
            if m:
                pre_build_spt = m.groupdict()['pre_build_spt']
                parsed_dict['vrf'][vrf_name]['address_family'] \
                [af_name]['pre_build_spt'] = pre_build_spt
                continue

            # CLI vrf done: TRUE
            p11 = re.compile(r'^\s*CLI +vrf +done: +(?P<cli_vrf_done>\w+)$')
            m= p11.match(line)
            if m:
                cli_vrf_done = True if m.groupdict()['cli_vrf_done'].lower() == 'true' else False

                parsed_dict['vrf'][vrf_name]['address_family']\
                [af_name]['cli_vrf_done'] = cli_vrf_done
                continue

            # PIM cibtype Auto Enabled: yes
            p12 = re.compile(r'^\s*PIM +cibtype +[a|A]uto +[e|E]nabled: +(?P<cibtype_auto_enabled>\w+)$')
            m = p12.match(line)
            if m:
                cibtype_auto_enabled = True if m.groupdict()['cibtype_auto_enabled'].lower() == 'yes' else False

                parsed_dict['vrf'][vrf_name]['address_family'] \
                [af_name]['cibtype_auto_enabled'] = cibtype_auto_enabled
                continue

            # PIM VxLAN VNI ID: 0
            p13 = re.compile(r'^\s*PIM +VxLAN +VNI +ID: +(?P<vxvlan_vni_id>\d+)$')
            m = p13.match(line)
            if m:
                vxlan_vni_id = int(m.groupdict()['vxvlan_vni_id'])
                parsed_dict['vrf'][vrf_name]['address_family'][af_name]['vxlan_vni_id'] = vxlan_vni_id
                continue

        return parsed_dict


# ==================================================
# schema Parser for 'show ip pim group-range'
# ==================================================
class ShowIpPimGroupRangeSchema(MetaParser):
    '''Schema for show ip pim group-range'''

    schema = {
        'vrf':{
            Any():{
                'address_family':{
                    Any():{
                        'sm':{
                            Any():{
                                Any():{
                                    Optional('action'): str,
                                    Optional('mode'): str,
                                    Optional('rp_address'): str,
                                    Optional('shared_tree_only'): str,
                                    Optional('range'): str,
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ==========================================================
#  parser for show ip pim group-range
#  parser for show ip pim group-range vrf <vrf>
# ==========================================================
class ShowIpPimGroupRange(ShowIpPimGroupRangeSchema):
    """parser for:
        show ip pim group-range
        show ip pim group-range vrf <vrf>"""

    def cli(self,vrf = ""):

        if not vrf:
            cmd = 'show ip pim group-range'
        else:
            cmd = 'show ip pim group-range vrf {}'.format(vrf)
        output = self.device.execute(cmd)
        af_name = 'ipv4'

        # Init dictionary
        parsed_output = dict()
        vrf_name = ""
        for line in output.splitlines():
            line = line.rstrip()

            # PIM Group-Range Configuration for VRF "VRF1"
            p1 = re.compile(r'^\s*PIM +Group\-Range +Configuration +for +VRF +\"(?P<vrf_name>[\S]+)\"$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                continue

            # Group-range        Action    Mode      RP-address       Shared-tree-only range
            # 232.0.0.0/8        Accept    SSM       -                -         Local
            p2 = re.compile(r'^\s*(?P<group_range>[^\s*Group-range][\S]+)'
                            ' +(?P<action>[\S]+)'
                            ' +(?P<mode>[\S]+)'
                            ' +(?P<rp_address>[\S]+)'
                            ' +(?P<shared_tree_only>[\S]+)'
                            '( +(?P<range>[\S]+))?$')
            m = p2.match(line)
            if m:
                group_range = m.groupdict()['group_range']
                action = m.groupdict()['action']
                mode = m.groupdict()['mode'].lower()
                rp_address = m.groupdict()['rp_address']
                shared_tree_only = m.groupdict()['shared_tree_only']
                if m.groupdict()['range']:
                    range = m.groupdict()['range']


                if group_range and vrf_name and mode:
                    if 'vrf' not in parsed_output:
                        parsed_output['vrf'] = {}
                    if vrf_name not in parsed_output['vrf']:
                        parsed_output['vrf'][vrf_name] = {}

                    if 'address_family' not in parsed_output['vrf'][vrf_name]:
                        parsed_output['vrf'][vrf_name]['address_family'] = {}
                    if af_name not in parsed_output['vrf'][vrf_name]['address_family']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name] = {}

                    if 'sm' not in parsed_output['vrf'][vrf_name]['address_family'][af_name]:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'] = {}

                    if mode not in  parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode] = {}

                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range] = {}
                    if '-' not in action:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range]\
                      ['action'] = action.lower()
                    parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range]\
                        ['mode'] = mode
                    if '-' not in rp_address:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range]\
                            ['rp_address'] = rp_address
                    if '-' not in shared_tree_only:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range] \
                            ['shared_tree_only'] = shared_tree_only
                    if m.groupdict()['range']  and '-' not in m.groupdict()['range']:
                        parsed_output['vrf'][vrf_name]['address_family'][af_name]['sm'][mode][group_range] \
                            ['range'] = range.lower()

                continue


        return parsed_output


# =========================================================================
# schema for 'show ip pim policy statictics register_policy'
# =========================================================================
class ShowIpPimPolicyStaticticsRegisterPolicySchema(MetaParser):
    """Schema show ip pim policy statictics register_policy"""

    schema = {
        'vrf':{
            Any():{
            'address_family':{
                Any():{
                    Optional('sm'):{
                        Optional('asm'):{
                            Optional('accept_register'): str,
                            Optional('register_policy'):{
                                Any():{
                                    Optional('total_accept_count'): int,
                                    Optional('total_reject_count'): int,
                                    Any():{
                                        Optional('compare_count'):int,
                                        Optional('match_count'):int,
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

# =======================================================================
#  parser for show ip pim policy statistics register-policy
#  parser for show ip pim policy statistics register-policy vrf <vrf>
#
# =======================================================================
class ShowIpPimPolicyStaticticsRegisterPolicy(ShowIpPimPolicyStaticticsRegisterPolicySchema):
    """Parser for:
        show ip pim policy statictics register_policy
        show ip pim policy statictics register_policy vrf <vrf>"""

    def cli(self, vrf=""):

        cmd_vrf = "sh run | egrep '^vrf|register-policy'"
        vrf_out = self.device.execute(cmd_vrf)
        parsed_data = {}
        vrf_name  = 'default'
        for each_line in vrf_out.splitlines():
            each_line = each_line.rstrip()

            # ip pim register-policy pim_register_p
            p1 = re.compile(r'^\s*ip +pim +register-policy( +prefix-list)? +(?P<rg_policy_name>[\S]+)$')
            m = p1.match(each_line)
            if m:
                parsed_data[vrf_name] = m.groupdict()['rg_policy_name']
                continue

            # vrf context VRF1
            p1 = re.compile(r'^\s*vrf +context +(?P<vrf_name>[\S]+)$')
            m = p1.match(each_line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                continue

        if not vrf:
            cmd = 'show ip pim policy statistics register-policy'
        else:
            cmd = 'show ip pim policy statistics register-policy vrf {}'.format(vrf)

        out = self.device.execute(cmd)
        af_name = 'ipv4'
        compare_count = match_count = accept_register = info =\
            reject_policy_count = accept_policy_count = ""
        # Init dictionary
        parsed_dict = dict()

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            p0 = re.compile(r'^\s*C: +No. +of +comparisions, +M: +No. +of matches$')
            m = p0.match(line)
            if m:
                compare_count = match_count = accept_register = info = \
                    reject_policy_count = accept_policy_count = ""

            # route-map pim_register_vrf permit 10
            p1 = re.compile(r'^\s*route-map +(?P<route_map>[\S]+)'
                            ' +permit +(?P<route_map_permit>[\S]+)$')
            m = p1.match(line)
            if m:
                accept_register = m.groupdict()['route_map']
                route_map_permit = m.groupdict()['route_map_permit']

                for key, value in parsed_data.items():
                    if accept_register == value:
                        vrf = key

            # match ip multicast group 239.2.2.2/32                      C: 0      M: 0
            p1_1 = re.compile(r'^\s*match +ip +multicast +group +(?P<group>[\w\.\/]+)'
                              '( +[c|C]: +(?P<c>\d+))?'
                              '( +[m|M]: +(?P<m>\d+))?$')
            m = p1_1.match(line)
            if m:
                group = m.groupdict()['group'].rstrip()
                if m.groupdict()['c']:
                    compare_count = m.groupdict()['c']
                else:
                    compare_count = ""
                match_count = m.groupdict()['m']
                info = "match ip multicast group " + group

            # ip prefix-list testprefixlist seq 5 permit 239.3.3.3/32      M: 0
            p2_1 = re.compile(r'^\s*ip +prefix-list +(?P<prefix_list>[\S]+)'
                              '( +seq +(?P<seq>\d+))?'
                              '( +permit +(?P<permit>[\S]+))?'
                              '( +[c|C]: +(?P<c>\d+))?'
                              '( +[m|M]: +(?P<m>\d+))?$')
            m = p2_1.match(line)
            if m:
                accept_register = m.groupdict()['prefix_list']

                for key, value in parsed_data.items():
                    if accept_register == value:
                        vrf = key
                seq = m.groupdict()['seq']
                permit = m.groupdict()['permit']
                if m.groupdict()['c']:
                    compare_count = m.groupdict()['c']
                else:
                    compare_count = ""
                match_count = m.groupdict()['m']
                info = 'ip prefix-list '+ accept_register +" seq "+ seq + " permit "+permit

            # Total accept count for policy: 0
            p3 = re.compile(r'^\s*Total +accept +count +for +policy: +(?P<accept_policy_count>\d+)$')
            m = p3.match(line)
            if m:
                accept_policy_count = m.groupdict()['accept_policy_count']

            # Total reject count for policy: 0
            p4 = re.compile(r'^\s*Total +reject +count +for +policy: +(?P<reject_policy_count>\d+)$')
            m = p4.match(line)
            if m:
                reject_policy_count = m.groupdict()['reject_policy_count']

            if vrf and accept_register:
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['address_family'] = {}

                if af_name not in parsed_dict['vrf'][vrf]['address_family']:
                    parsed_dict['vrf'][vrf]['address_family'][af_name] = {}
                if 'sm' not in parsed_dict['vrf'][vrf]['address_family'][af_name]:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['sm'] = {}
                if 'asm' not in parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm'] = {}

                parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm']['accept_register'] = accept_register

                if 'register_policy' not in parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm']:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm']['register_policy'] = {}

                if accept_register not in parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']\
                        ['asm']['register_policy']:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm']['register_policy']\
                        [accept_register] = {}


                if reject_policy_count:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm']['register_policy'][accept_register] \
                        ['total_reject_count'] = int(reject_policy_count)

                if accept_policy_count:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm']['register_policy'][accept_register] \
                        ['total_accept_count'] = int(accept_policy_count)


                if info and info not in parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm'] \
                        ['register_policy'][accept_register]:
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm']['register_policy'] \
                        [accept_register][info] = {}

                if info and compare_count :
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm']['register_policy'][accept_register] \
                    [info]['compare_count'] = int(compare_count)

                if info and match_count :
                    parsed_dict['vrf'][vrf]['address_family'][af_name]['sm']['asm']['register_policy'][accept_register] \
                        [info]['match_count'] = int(match_count)

        return parsed_dict


# ====================================================
# schema Parser for 'show ip pim interface'
# ====================================================
class ShowIpPimInterfaceSchema(MetaParser):
    """Schema for show ip pim interface"""

    schema = {
        'vrf':{
            Any():{
                'interfaces':{
                    Any():{
                        'address_family': {
                            Any(): {
                                Optional('oper_status'): str,
                                Optional('link_status'): str,
                                Optional('admin_status'): str,
                                Optional('address'): list,
                                Optional('ip_subnet'): str,
                                Optional('dr_address'): str,
                                Optional('dr_priority'): int,
                                Optional('configured_dr_priority'): int,
                                Optional('neighbor_count'): int,
                                Optional('hello_interval'): int,
                                Optional('hello_expiration'): str,
                                Optional('neighbor_holdtime'): int,
                                Optional('dr_delay'): int,
                                Optional('bsr_border'): bool,
                                Optional('genid'): str,
                                Optional('hello_md5_ah_authentication'): str,
                                Optional('neighbor_filter'): str,
                                Optional('jp_inbound_policy'): str,
                                Optional('jp_outbound_policy'): str,
                                Optional('jp_interval'): int,
                                Optional('jp_next_sending'): int,
                                Optional('bfd'):{
                                    Optional('enable'): bool,
                                    },
                                Optional('sm'):{
                                    Optional('passive'): bool,
                                },
                                Optional('vpc_svi'): bool,
                                Optional('auto_enabled'): bool,
                                Optional('statistics'):{
                                    Optional('general'):{
                                        Optional('hellos'): str,
                                        Optional('jps'): str,
                                        Optional('asserts'): str,
                                        Optional('grafts'): str,
                                        Optional('graft_acks'): str,
                                        Optional('df_offers'): str,
                                        Optional('df_winners'): str,
                                        Optional('df_backoffs'): str,
                                        Optional('df_passes'): str,
                                    },
                                    Optional('errors'):{
                                        Optional('checksum'): int,
                                        Optional('invalid_packet_types'): int,
                                        Optional('invalid_df_subtypes'): int,
                                        Optional('authentication_failed'): int,
                                        Optional('packet_length_errors'): int,
                                        Optional('bad_version_packets'): int,
                                        Optional('packets_from_self'): int,
                                        Optional('packets_from_non_neighbors'): int,
                                        Optional('packets_received_on_passiveinterface'): int,
                                        Optional('jps_received_on_rpf_interface'): int,
                                        Optional('joins_received_with_no_rp'): int,
                                        Optional('joins_received_with_wrong_rp'): int,
                                        Optional('joins_received_with_ssm_groups'): int,
                                        Optional('joins_received_with_bidir_groups'): int,
                                        Optional('jps_filtered_by_inbound_policy'): int,
                                        Optional('jps_filtered_by_outbound_policy'): int,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

# ==========================================================
#  parser for show ip pim interface vrf <word>
#  parser for show ip pim interface
#  parser for show ip pim interface <word>
#  parser for show ip pim interface <word1> vrf <word2>
#
# ==========================================================
class ShowIpPimInterface(ShowIpPimInterfaceSchema):
    """Parser for:
        show ip pim interface
        show ip pim interface vrf <vrf>
        show ip pim interface <interface>
        show ip pim interface <interface> vrf <vrf>"""

    def cli(self , interface ="", vrf=""):

        if not vrf and not interface:
            cmd = 'show ip pim interface'
        if not vrf and interface:
            cmd = 'show ip pim interface {}'.format(interface)
        if vrf and not interface:
            cmd = 'show ip pim interface vrf {}'.format(vrf)
        if vrf and interface:
            cmd = 'show ip pim interface {0} vrf {1}'.format(interface, vrf)

        out = self.device.execute(cmd)
        af_name = 'ipv4'

        # Init dictionary
        parsed_dict = dict()

        checksum = invalid_packet_types = invalid_df_subtypes = authentication_failed \
          = packet_length_errors = bad_version_packets = packets_from_self =\
          packets_from_non_neighbors = packets_received_on_passiveinterface = \
          jps_received_on_rpf_interface = joins_received_with_bidir_groups = \
          joins_received_with_no_rp = joins_received_with_ssm_groups = joins_received_with_wrong_rp = \
          jps_filtered_by_inbound_policy = jps_filtered_by_outbound_policy = hellos = jps = asserts = grafts\
          = graft_acks = df_backoffs = df_passes = df_winners = df_offers = ""

        interface_status = interface_name = address = dr_address = bsr_border = hello_md5_ah_authentication = \
            hello_interval = hello_expiration = dr_priority = configured_dr_delay = jp_next_sending = bfd\
            = jp_interval = passive = auto_enabled = genid = jp_outbound_policy = jp_inbound_policy = \
            nbr_count = ip_subnet = neighbor_holdtime = neighbor_filter = vpc_svi = bad_version_packets = ""

        for line in out.splitlines():
            line = line.rstrip()

            #PIM Interface Status for VRF "VRF1"
            p1 = re.compile(r'^\s*PIM +Interface +Status +for +VRF+ \"(?P<vrf>[\w]+)\"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                checksum = invalid_packet_types = invalid_df_subtypes = authentication_failed \
                = packet_length_errors = bad_version_packets = packets_from_self = \
                packets_from_non_neighbors = packets_received_on_passiveinterface = \
                jps_received_on_rpf_interface = joins_received_with_bidir_groups = \
                joins_received_with_no_rp = joins_received_with_ssm_groups = joins_received_with_wrong_rp = \
                jps_filtered_by_inbound_policy = jps_filtered_by_outbound_policy = hellos = jps = asserts = grafts \
                = graft_acks = df_backoffs = df_passes = df_winners = df_offers = ""

                interface_status = interface_name = address = dr_address = bsr_border = hello_md5_ah_authentication = \
                hello_interval = hello_expiration = dr_priority = configured_dr_delay = jp_next_sending = bfd \
                = jp_interval = passive = auto_enabled = genid = jp_outbound_policy = jp_inbound_policy = \
                nbr_count = configured_dr_priority = ip_subnet = neighbor_holdtime = neighbor_filter = vpc_svi = bad_version_packets = ""

            # Ethernet2/2, Interface status: protocol-up/link-up/admin-up
            p2 = re.compile(r'^\s*(?P<interface_name>[\w\/\.\-]+),?'
                            ' +Interface +status:'
                            ' +protocol-(?P<oper_status>[\w]+)(/)?'
                            'link\-(?P<link_status>[\w]+)(/)?'
                            'admin\-(?P<admin_status>[\w]+)$')
            m = p2.match(line)
            if m:
                interface_name = m.groupdict()['interface_name']
                oper_status = m.groupdict()['oper_status']
                link_status = m.groupdict()['link_status']
                admin_status = m.groupdict()['admin_status']
                jp_outbound_policy = jp_inbound_policy = neighbor_filter = ""

            # IP address: 10.11.33.11, IP subnet: 10.11.33.0/24
            p3 = re.compile(r'^\s*IP +address: +(?P<address>[\w\.]+),'
                            ' +IP +subnet: +(?P<ip_subnet>[\w\.\/]+)$')
            m = p3.match(line)
            if m:
                address = m.groupdict()['address']
                ip_subnet = m.groupdict()['ip_subnet']

            # PIM DR: 10.11.33.11, DR's priority: 144
            p4 = re.compile(r'^\s*PIM +DR: +(?P<dr_address>[\w\.]+),'
                            ' +DR\'s +priority: +(?P<dr_priority>[\d]+)$')
            m = p4.match(line)
            if m:
                dr_address = m.groupdict()['dr_address']
                dr_priority = m.groupdict()['dr_priority']

            # PIM neighbor count: 1
            p5 = re.compile(r'^\s*PIM +neighbor +count: +(?P<nbr_count>[\d]+)$')

            m = p5.match(line)
            if m:
                nbr_count = m.groupdict()['nbr_count']

            # PIM hello interval: 45 secs (configured 44444 ms), next hello sent in: 00:00:05
            p6 = re.compile(r'^\s*PIM +hello +interval: +(?P<hello_interval>[\d]+) +secs'
                            '( +\(configured +(?P<configured_interval_ms>\d+) +ms\))?,'
                            ' +next +hello +sent +in: +(?P<hello_expiration>[\w\:]+)$')
            m = p6.match(line)
            if m:
                hello_interval = m.groupdict()['hello_interval']
                hello_expiration = m.groupdict()['hello_expiration']

            # PIM neighbor holdtime: 159 secs
            p7 = re.compile(r'^\s*PIM +neighbor +holdtime: +(?P<holdtime>[\d]+) +secs$')
            m = p7.match(line)
            if m:
                neighbor_holdtime = m.groupdict()['holdtime']

            # PIM configured DR priority: 144
            p8 = re.compile(r'^\s*PIM +configured +DR +priority: +(?P<configured_dr_priority>[\d]+)$')
            m = p8.match(line)
            if m:
                configured_dr_priority = m.groupdict()['configured_dr_priority']

            # PIM configured DR delay: 3 secs
            p9 = re.compile(r'^\s*PIM +configured +DR +delay: +(?P<configured_dr_delay>[\d]+) +secs$')
            m = p9.match(line)
            if m:
                configured_dr_delay = m.groupdict()['configured_dr_delay']

            # PIM border interface: yes
            p10 = re.compile(r'^\s*PIM +border +interface: +(?P<border_interface>[\w]+)$')
            m = p10.match(line)
            if m:
                bsr_border = m.groupdict()['border_interface']

            # PIM GenID sent in Hellos: 0x26fae674
            p11 = re.compile(r'^\s*PIM +GenID +sent +in +Hellos: +(?P<genid>[\S]+)$')
            m = p11.match(line)
            if m:
                genid = m.groupdict()['genid']

            # PIM Hello MD5-AH Authentication: disabled
            p12 = re.compile(r'^\s*PIM +Hello +MD5-AH +Authentication: +(?P<md5_authentication>[\w]+)$')
            m = p12.match(line)
            if m:
                hello_md5_ah_authentication = m.groupdict()['md5_authentication']

            # PIM Neighbor policy: v4neighbor-policy
            p13 = re.compile(r'^\s*PIM +Neighbor +policy: +(?P<nbr_policy>(?!none)[\w\-\s]+)$')
            m = p13.match(line)
            if m:
                neighbor_filter = m.groupdict()['nbr_policy']

            # PIM Join-Prune inbound policy: v4jp-policy
            p14 = re.compile(r'^\s*PIM +Join-Prune +inbound +policy: +(?P<jp_inbound_policy>(?!none)[\w\-\s]+)$')
            m = p14.match(line)
            if m:
                jp_inbound_policy = m.groupdict()['jp_inbound_policy']

            # PIM Join-Prune outbound policy: v4jp-policy
            p15 = re.compile(r'^\s*PIM +Join-Prune +outbound +policy: +(?P<jp_outbound_policy>(?!none)[\w\-\s]+)$')
            m = p15.match(line)
            if m:
                jp_outbound_policy = m.groupdict()['jp_outbound_policy']

            # PIM Join-Prune interval: 1 minutes
            p16 = re.compile(r'^\s*PIM +Join-Prune +interval: +(?P<jp_interval>[\d]+) +minutes$')
            m = p16.match(line)
            if m:
                jp_interval = m.groupdict()['jp_interval']

            # PIM Join-Prune next sending: 1 minutes
            p17 = re.compile(r'^\s*PIM +Join-Prune +next +sending: +(?P<jp_next_sending>[\d]+) +minutes$')
            m = p17.match(line)
            if m:
                jp_next_sending = m.groupdict()['jp_next_sending']

            # PIM BFD enabled: no
            p18 = re.compile(r'^\s*PIM +BFD +enabled: +(?P<bfd_enabled>[\w]+)$')
            m = p18.match(line)
            if m:
                bfd = m.groupdict()['bfd_enabled']

            # PIM passive interface: no
            p19 = re.compile(r'^\s*PIM +passive +interface: +(?P<passive>[\w]+)$')
            m = p19.match(line)
            if m:
                passive = m.groupdict()['passive']

            # PIM VPC SVI: no
            p20 = re.compile(r'^\s*PIM +VPC +SVI: +(?P<vpc_svi>[\w]+)$')
            m = p20.match(line)
            if m:
                vpc_svi = m.groupdict()['vpc_svi']

            # PIM Auto Enabled: no
            p21 = re.compile(r'^\s*PIM +Auto +Enabled: +(?P<auto_enabled>[\w]+)$')
            m = p21.match(line)
            if m:
                auto_enabled = m.groupdict()['auto_enabled']

            # PIM Interface Statistics, last reset: never
            # PIM Interface Statistics
            p22 = re.compile(r'^\s*PIM +Interface +Statistics+(, +last +reset: +(?P<last_reset>[\w\:]+))?$')
            m = p22.match(line)
            if m:
                statistic = True
                if m.groupdict()['last_reset']:
                    last_rest = m.groupdict()['last_reset']

            # Hellos: 360/474 (early: 0), JPs: 0/0, Asserts: 0/0
            p23 = re.compile(r'^\s*Hellos: +(?P<hellos>[\d\/]+)'
                             ' +\(early: +(?P<early>\d+)\)?,'
                             ' +JPs: +(?P<jps>[\d\/]+),'
                             ' +Asserts: +(?P<asserts>[\d\/]+)$')
            m = p23.match(line)
            if m:
                hellos = m.groupdict()['hellos']
                jps = m.groupdict()['jps']
                asserts = m.groupdict()['asserts']

            # Grafts: 0/0, Graft-Acks: 0/0
            p24 = re.compile(r'^\s*Grafts: +(?P<grafts>[\d\/]+),'
                             ' +Graft-Acks: +(?P<graft_acks>[\d\/]+)$')
            m = p24.match(line)
            if m:
                grafts = m.groupdict()['grafts']
                graft_acks = m.groupdict()['graft_acks']

            # DF-Offers: 0/0, DF-Winners: 0/0, DF-Backoffs: 0/0, DF-Passes: 0/0
            p25 = re.compile(r'^\s*DF-Offers: +(?P<df_offers>[\d\/]+),'
                             ' +DF-Winners: +(?P<df_winners>[\d\/]+),'
                             ' +DF-Backoffs: +(?P<df_backoffs>[\d\/]+),'
                             ' +DF-Passes: +(?P<df_passes>[\d\/]+)$')
            m = p25.match(line)
            if m:
                df_offers = m.groupdict()['df_offers']
                df_winners = m.groupdict()['df_winners']
                df_backoffs = m.groupdict()['df_backoffs']
                df_passes = m.groupdict()['df_passes']

            #    Checksum errors: 0, Invalid packet types/DF subtypes: 0/0
            p26 = re.compile(r'^\s*Checksum errors: +(?P<checksum>[\d]+),'
                             ' +Invalid +packet +types\/DF +subtypes:'
                             ' +(?P<invalid_packet_types>[\d]+)/(?P<invalid_df_subtypes>[\d]+)$')
            m = p26.match(line)
            if m:
                checksum = m.groupdict()['checksum']
                invalid_packet_types = m.groupdict()['invalid_packet_types']
                invalid_df_subtypes = m.groupdict()['invalid_df_subtypes']

            #    Authentication failed: 0
            p27 = re.compile(r'^\s*Authentication +failed: +(?P<authentication_failed>[\d]+)$')
            m = p27.match(line)
            if m:
                authentication_failed = m.groupdict()['authentication_failed']

            #    Packet length errors: 0, Bad version packets: 0, Packets from self: 0
            p28 = re.compile(r'^\s*Packet +length +errors: +(?P<packet_length_errors>[\d]+),'
                             ' +Bad +version +packets: +(?P<bad_version_packets>[\d]+),'
                             ' +Packets +from +self: +(?P<packets_from_self>[\d]+)$')
            m = p28.match(line)
            if m:
                packet_length_errors = m.groupdict()['packet_length_errors']
                bad_version_packets = m.groupdict()['bad_version_packets']
                packets_from_self = m.groupdict()['packets_from_self']

            #    Packets from non-neighbors: 0
            p29 = re.compile(r'^\s*Packets +from +non\-neighbors: +(?P<packets_from_non_neighbors>[\d]+)$')
            m = p29.match(line)
            if m:
                packets_from_non_neighbors = m.groupdict()['packets_from_non_neighbors']

            #    Packets received on passiveinterface: 0
            p30 = re.compile(r'^\s*Packets +received +on +passiveinterface:'
                             ' +(?P<packets_received_on_passiveinterface>[\d]+)$')
            m = p30.match(line)
            if m:
                packets_received_on_passiveinterface = m.groupdict()['packets_received_on_passiveinterface']

            #    JPs received on RPF-interface: 0
            p31 = re.compile(r'^\s*JPs +received +on +RPF\-interface:'
                             ' +(?P<jp_received_on_rpf_interface>[\d]+)$')
            m = p31.match(line)
            if m:
                jps_received_on_rpf_interface = m.groupdict()['jp_received_on_rpf_interface']

            #    (*,G) Joins received with no/wrong RP: 0/0
            p32 = re.compile(r'^\s*(?P<s_g>[\w\(\)\,\*]+) +Joins +received +with +no\/+wrong RP:'
                             ' +(?P<joins_received_with_no_rp>\d+)/(?P<joins_received_with_wrong_rp>\d+)$')
            m = p32.match(line)
            if m:
                joins_received_with_no_rp = m.groupdict()['joins_received_with_no_rp']
                joins_received_with_wrong_rp = m.groupdict()['joins_received_with_wrong_rp']

            #  (*,G)/(S,G) JPs received for SSM/Bidir groups: 0/0
            p33 = re.compile(r'^\s*(?P<s_g>[\w\(\)\,\*\/]+) +JPs +received +for +SSM\/Bidir +groups:'
                             ' +(?P<joins_received_with_ssm_groups>\d+)/(?P<joins_received_with_bidir_groups>\d+)$')
            m = p33.match(line)
            if m:
                joins_received_with_ssm_groups = m.groupdict()['joins_received_with_ssm_groups']
                joins_received_with_bidir_groups = m.groupdict()['joins_received_with_bidir_groups']

            # JPs filtered by inbound policy: 0
            p34 = re.compile(r'^\s*JPs +filtered +by +inbound +policy:'
                             ' +(?P<jps_filtered_by_inbound_policy>\d+)$')
            m = p34.match(line)
            if m:
                jps_filtered_by_inbound_policy = m.groupdict()['jps_filtered_by_inbound_policy']

            # JPs filtered by outbound policy: 0
            p35 = re.compile(r'^\s*JPs +filtered +by +outbound +policy:'
                             ' +(?P<jps_filtered_by_outbound_policy>\d+)$')
            m = p35.match(line)
            if m:
                jps_filtered_by_outbound_policy = m.groupdict()['jps_filtered_by_outbound_policy']


            if vrf and interface_name:
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}
                if 'interfaces' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['interfaces'] = {}

                if interface_name not in parsed_dict['vrf'][vrf]['interfaces']:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name] = {}

                if 'address_family' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'] = {}

                if af_name not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family']:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] = {}

                if oper_status:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name]\
                        ['oper_status'] = oper_status
                if link_status:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name]\
                        ['link_status'] = link_status
                if admin_status:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name]\
                        ['admin_status'] = admin_status
                if address:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['address'] = address.split()
                if ip_subnet:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['ip_subnet'] = ip_subnet
                if dr_address:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['dr_address'] = dr_address
                if dr_priority:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['dr_priority'] = int(dr_priority)
                if configured_dr_priority:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['configured_dr_priority'] = int(configured_dr_priority)

                if configured_dr_delay:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['dr_delay'] = int(configured_dr_delay)
                if nbr_count:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['neighbor_count'] = int(nbr_count)
                if hello_interval:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['hello_interval'] = int(hello_interval)
                if hello_expiration:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['hello_expiration'] = hello_expiration
                if neighbor_holdtime:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['neighbor_holdtime'] = int(neighbor_holdtime)
                if dr_priority:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['dr_priority'] = int(dr_priority)
                if bsr_border:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['bsr_border'] = True if bsr_border.lower() == 'yes' else False
                if genid:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['genid'] = genid

                if hello_md5_ah_authentication:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['hello_md5_ah_authentication'] = hello_md5_ah_authentication

                if neighbor_filter:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['neighbor_filter'] = neighbor_filter

                if jp_inbound_policy:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['jp_inbound_policy'] = jp_inbound_policy

                if jp_outbound_policy:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['jp_outbound_policy'] = jp_outbound_policy

                if jp_interval:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['jp_interval'] = int(jp_interval)*60
                if jp_next_sending:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['jp_next_sending'] = int(jp_next_sending)*60


                if bfd:
                    if 'bfd' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]\
                            ['address_family'][af_name]:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family']\
                            [af_name]['bfd'] = {}
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['bfd']['enable'] = True if bfd.lower() == 'yes' else False


                if passive:
                    if 'sm' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]\
                            ['address_family'][af_name]:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family']\
                            [af_name]['sm'] = {}
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['sm']['passive'] = True if passive.lower() == 'yes' else False

                if vpc_svi:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['vpc_svi'] = True if vpc_svi.lower() == 'yes' else False


                if auto_enabled:
                    parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['auto_enabled'] = True if auto_enabled.lower() == 'yes' else False

                if hellos or jps or asserts or grafts or graft_acks or df_backoffs or df_passes\
                        or df_winners or df_offers:
                    if 'statistics' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]\
                            ['address_family'][af_name]:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics'] = {}
                    if 'general' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']['general'] = {}

                    if hellos:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name]\
                        ['statistics']['general']['hellos'] = hellos
                    if jps:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['jps'] = jps
                    if asserts:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['asserts'] = asserts
                    if df_offers:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['df_offers'] = df_offers
                    if graft_acks:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['graft_acks'] = graft_acks
                    if grafts:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['grafts'] = grafts
                    if df_backoffs:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['df_backoffs'] = df_backoffs
                    if df_passes:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['df_passes'] = df_passes
                    if df_winners:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                        ['statistics']['general']['df_winners'] = df_winners

                if checksum or invalid_packet_types or invalid_df_subtypes or authentication_failed\
                        or packet_length_errors or bad_version_packets or packets_from_self or \
                        packets_from_non_neighbors or packets_received_on_passiveinterface or \
                        jps_received_on_rpf_interface or joins_received_with_bidir_groups or \
                        joins_received_with_no_rp or joins_received_with_ssm_groups or joins_received_with_wrong_rp or\
                        jps_filtered_by_inbound_policy or jps_filtered_by_outbound_policy:
                    if 'statistics' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name]\
                            ['address_family'][af_name]:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics'] = {}
                    if 'errors' not in parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']['errors'] = {}
                    if checksum:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name] \
                            ['address_family'][af_name]['statistics']['errors']['checksum'] = int(checksum)

                    if invalid_df_subtypes:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name]\
                            ['statistics']['errors']['invalid_df_subtypes'] = int(invalid_df_subtypes)
                    if invalid_packet_types:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['invalid_packet_types'] = int(invalid_packet_types)

                    if authentication_failed:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['authentication_failed'] = int(authentication_failed)
                    if packet_length_errors:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['packet_length_errors'] = int(packet_length_errors)
                    if bad_version_packets:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['bad_version_packets'] = int(bad_version_packets)

                    if packets_from_self:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['packets_from_self'] = int(packets_from_self)
                    if packets_from_non_neighbors:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['packets_from_non_neighbors'] = int(packets_from_non_neighbors)

                    if packets_received_on_passiveinterface:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['packets_received_on_passiveinterface']\
                            = int(packets_received_on_passiveinterface)

                    if jps_received_on_rpf_interface:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['jps_received_on_rpf_interface'] = int(jps_received_on_rpf_interface)
                    if joins_received_with_bidir_groups:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['joins_received_with_bidir_groups'] = int(joins_received_with_bidir_groups)

                    if joins_received_with_no_rp:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['joins_received_with_no_rp'] = int(joins_received_with_no_rp)

                    if joins_received_with_ssm_groups:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['joins_received_with_ssm_groups'] = int(joins_received_with_ssm_groups)

                    if joins_received_with_wrong_rp:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['joins_received_with_wrong_rp'] = int(joins_received_with_wrong_rp)
                    if jps_filtered_by_inbound_policy:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['jps_filtered_by_inbound_policy'] = int(jps_filtered_by_inbound_policy)
                    if  jps_filtered_by_outbound_policy:
                        parsed_dict['vrf'][vrf]['interfaces'][interface_name]['address_family'][af_name] \
                            ['statistics']['errors']['jps_filtered_by_outbound_policy'] = int(jps_filtered_by_outbound_policy)
                continue

        return parsed_dict
# ================================
# schema Parser for 'show ipv6 pim vrf all detail'
# ================================
class ShowIpv6PimVrfAllDetailSchema(MetaParser):
    """Schema for show ipv6 pim vrf all detail"""

    schema = {
        'vrf':{
            Any():{
            'address_family':{
                Any():{
                   Optional('vrf_id'): int,
                   Optional('table_id'): str,
                   Optional('interface_count'): int,
                   Optional('bfd'):{
                       Optional('enable'): bool,
                   },
                   Optional('state_limit'): str,
                   Optional('register_rate_limit'): str,
                   Optional('shared_tree_route_map'): str,
                   Optional('shared_tree_route_ranges'): str,
                   Optional('shared_tree_ranges'): str,
                   },
                },
            },
        },
    }

# ==========================================================
#  parser for show ipv6 pim vrf all detail
#
# ==========================================================
class ShowIpv6PimVrfAllDetail(ShowIpv6PimVrfAllDetailSchema):
    """Parser for show ipv6 pim vrf all detail"""

    def cli(self):

        cmd = 'show ipv6 pim vrf all detail'
        out = self.device.execute(cmd)
        af_name = 'ipv6'
        # Init dictionary
        parsed_dict = dict()

        for line in out.splitlines():
            line = line.rstrip()

            #VRF Name              VRF      Table       Interface  BFD
            #          ID       ID          Count      Enabled
            # default               1        0x80000001  3          no
            p1 = re.compile(r'^\s*(?P<vrf>[\w\d]+) +(?P<vrf_id>\d+)'
                            ' +(?P<table_id>0x[a_f0-9]+) +(?P<interface_count>\d+)'
                            ' +(?P<bfd>\w+)$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf']
                vrf_id = int(m.groupdict()['vrf_id'])
                table_id = m.groupdict()['table_id']
                interface_count = int(m.groupdict()['interface_count'])
                bfd_enabled = True if m.groupdict()['bfd'].lower() == 'yes' else False

                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['vrf_id'] = vrf_id

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['table_id'] = table_id
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['interface_count'] = interface_count

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['bfd'] = {}
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['bfd']['enable'] = bfd_enabled

                continue

            # State Limit: None
            p2 = re.compile(r'^\s*State +Limit: +(?P<state_limit>(?!None)\w+)$')
            m = p2.match(line)
            if m:
                state_limit = m.groupdict()['state_limit'].lower()
                parsed_dict['vrf'][vrf_name]['address_family'] \
                [af_name]['state_limit'] = state_limit
                continue


            # Register Rate Limit: none
            p3 = re.compile(r'^\s*Register +Rate +Limit: +(?P<register_rate_limit>(?!none)\w+)$')
            m = p3.match(line)
            if m:
                register_rate_limit = m.groupdict()['register_rate_limit'].lower()
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['register_rate_limit'] = register_rate_limit
                continue

            # Shared tree route-map: v6spt-threshold-group-list
            p4 = re.compile(r'^\s*Shared +tree +route-map: +(?P<route_map>[\w\d\S]+)$')
            m = p4.match(line)
            if m:
                shared_tree_route_map = m.groupdict()['route_map']
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['shared_tree_route_map'] = shared_tree_route_map
                continue

            # route-ranges: xxxxx
            p4 = re.compile(r'^\s*route-ranges:( +(?P<route_range>[\w\d\S]+))?$')
            m = p4.match(line)
            if m:
                if m.groupdict()['route_range']:
                    shared_tree_route_range = m.groupdict()['route_range']

                    parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['shared_tree_route_ranges'] = shared_tree_route_range

                continue

            # Shared tree ranges: none
            p6 = re.compile(r'^\s*Shared +tree +ranges: +(?P<shared_tree_ranges>(?!none)\w+)$')
            m = p6.match(line)
            if m:
                shared_tree_ranges = m.groupdict()['shared_tree_ranges']
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['shared_tree_ranges'] = shared_tree_ranges

                continue

        return parsed_dict



# ====================================
# Schema for 'show running-config pim'
# TODO: Add left attributes in PIM
# ====================================
class ShowRunningConfigPimSchema(MetaParser):
    """Schema for show running-config pim"""

    schema = {
        Optional('feature_pim'): bool,
        Optional('feature_pim6'): bool,
        Optional('vrf'): {
            Any(): {
                Optional('address_family'): {
                    Any(): {
                        Optional('rp'): {
                            Optional('autorp'): {
                                Optional('send_rp_announce'): {
                                    Optional('interface'): str, #send_rp_announce_intf
                                    Optional('group'): str,  #send_rp_announce_rp_group
                                    Optional('scope'): int, #send_rp_announce_scope
                                    Optional('group_list'): str, #send_rp_announce_group_list
                                    Optional('route_map'): str, #send_rp_announce_route_map
                                    Optional('prefix_list'): str, #send_rp_announce_prefix_list
                                    Optional('interval'): int, #send_rp_announce_interval
                                    Optional('bidir'): bool, #send_rp_announce_bidir
                                },
                                Optional('send_rp_discovery'): {
                                    'interface': str, #send_rp_discovery_intf
                                    Optional('scope'): int, #send_rp_discovery_scope
                                },
                                Optional('listener'): bool, #autorp_listener
                            },
                            Optional('bsr'): {
                                Any(): { # bsr_rp_candidate_interface
                                    Optional('interface'): str, # bsr_rp_candidate_interface
                                    Optional('policy'): str, # bsr_rp_candidate_group_list
                                    Optional('mode'): str, # bsr_rp_candidate_bidir
                                    Optional('priority'): int, # bsr_rp_candidate_priority
                                    Optional('interval'): int, # bsr_rp_candidate_interval
                                    Optional('route_map'): str, # bsr_rp_candidate_route_map
                                    Optional('prefix_list'): str, # bsr_rp_candidate_prefix_list
                                },
                            },
                            Optional('static_rp'): {
                                Any(): { # static_rp_addressl
                                    Optional('policy_name'): str, # static_rp_group_list
                                    Optional('override'): bool, # static_rp_override
                                    Optional('policy'): int, # static_rp_policy
                                    Optional('bidir'): bool, # static_rp_bidir
                                    Optional('route_map'): str, # static_rp_route_map
                                    Optional('prefix_list'): str, # static_rp_prefix_list
                                },
                            }
                        }
                    }
                }
            }
        }
    }

# ====================================
# Parser for 'show running-config pim'
# TODO: Add left attributes in PIM
# ====================================
class ShowRunningConfigPim(ShowRunningConfigPimSchema):
    """Parser for show running-config pim"""

    def cli(self, address_family=None, pip_str=None, vrf=None):

        assert address_family in ['ipv4', 'ipv6', None]

        if address_family == 'ipv4':
            features = ['pim']
        elif address_family == 'ipv6':
            features = ['pim6']
        else:
            features = ['pim', 'pim6']
        cmd  = 'show running-config {feature}'
        if vrf:
            if vrf == 'default':
                # command start with ip pim, or interface without spaces
                cmd += " | sec '^i'"
            else:
                cmd += ' | sec %s' % vrf
        if pip_str:
            cmd += ' | inc %s' % pip_str

        # initial output
        out = ''

        for ft in features:
            out += '\n' + self.device.execute(cmd.format(feature=ft))

        # Init vars
        pim_dict = {}

        # initial regular express
        # vrf context VRF1
        p_vrf  = re.compile(r'^vrf +context +(?P<vrf>\S+)$')

        # feature pim
        p1 = re.compile(r'^feature +pim$')

        # feature pim6
        p1_1 = re.compile(r'^feature +pim6$')

        # ip pim bsr bsr-candidate loopback0 priority 128
        p2 = re.compile(r'^ip(v6)? +pim *(bsr)? +bsr\-candidate +(?P<bsr_candidate_interface>[\w\/\.\-]+)'
                         '( +hash\-len +(?P<bsr_candidate_hash_mask_length>\d+))?'
                         '( priority +(?P<bsr_candidate_priority>\d+))?')

        # ip pim rp-address 6.6.6.6 group-list 234.0.0.0/8
        # ip pim rp-address 6.6.6.6 group-list 239.1.1.0/24 bidir
        p3 = re.compile(r'^(?P<af>ip|ipv6) +pim +rp\-address +(?P<static_rp_address>[\w\.\:]+) +'
                         '((group\-list +(?P<static_rp_group_list>[\w\.]+\/\d+))|'
                         '(route\-map +(?P<static_rp_route_map>\w+))|'
                         '(prefix\-list +(?P<static_rp_prefix_list>\w+)))'
                         '( *(?P<dummy>.*))?$$')

        # ip pim bsr rp-candidate loopback0 group-list 235.0.0.0/8 priority 128
        # ip pim rp-candidate Ethernet1/1 group-list 239.0.0.0/24 priority 10 interval 60 bidir
        p4 = re.compile(r'^(?P<af>ip|ipv6) +pim( *bsr)? +rp\-candidate +(?P<bsr_rp_candidate_interface>[\w\/\.\-]+) +'
                         '((group\-list +(?P<bsr_rp_candidate_group_list>[\w\.]+\/\d+))|'
                         '(route\-map +(?P<bsr_rp_candidate_route_map>\w+))|'
                         '(prefix\-list +(?P<bsr_rp_candidate_prefix_list>\w+)))'
                         '( *(?P<dummy>.*))?$')

        # ip pim send-rp-announce loopback0 group-list 236.0.0.0/8
        # ----  ipv6 not supported -----
        p5 = re.compile(r'^ip +pim +(send\-rp\-announce|(auto\-rp +rp\-candidate)) +'
                         '((?P<send_rp_announce_intf>(lo|Lo|Eth|eth|Port|port)\w+)|'
                         '(?P<send_rp_announce_rp_group>(\d+\.){3}\d+)) +'
                         '((group\-list +(?P<send_rp_announce_group_list>[\w\.]+\/\d+))|'
                         '(route\-map +(?P<send_rp_announce_route_map>\w+))|'
                         '(prefix\-list +(?P<send_rp_announce_prefix_list>\w+)))'
                         '(?P<dummy>.*)?$')

        # ip pim send-rp-discovery loopback0
        # ip pim send-rp-discovery loopback0 scope 34
        # ----  ipv6 not supported -----
        p6 = re.compile(r'^ip +pim +send\-rp\-discovery +(?P<send_rp_discovery_intf>[\w\/\.\-]+)'
                         '( scope +(?P<send_rp_discovery_scope>\d+))?$')

        # ip pim ssm range 232.0.0.0/8
        p7 = re.compile(r'^$')

        # ip pim anycast-rp 126.126.126.126 2.2.2.2
        # ip pim anycast-rp 126.126.126.126 6.6.6.6
        p8 = re.compile(r'^$')

        # ip pim bsr forward listen
        p9 = re.compile(r'^$')

        # ip pim register-source loopback0
        p10 = re.compile(r'^$')

        # ip pim auto-rp forward listen
        # ----  ipv6 not supported -----
        p11 = re.compile(r'^ip +pim +auto\-rp +forward +listen$')

        for line in out.splitlines():
            if line and not line.startswith(' '):
                vrf_dict = pim_dict.setdefault('vrf', {}).setdefault('default', {})
            elif vrf:
                vrf_dict = pim_dict.setdefault('vrf', {}).setdefault(vrf, {})

            line = line.strip()

            # vrf context VRF1
            m = p_vrf.match(line)
            if m:
                vrf_dict = pim_dict.setdefault('vrf', {}).setdefault(m.groupdict()['vrf'], {})
                continue

            # feature pim
            m = p1.match(line)
            if m:
                pim_dict['feature_pim'] = True
                continue

            # feature pimv6
            m = p1_1.match(line)
            if m:
                pim_dict['feature_pim6'] = True
                continue
           
            # ip pim rp-address 6.6.6.6 group-list 234.0.0.0/8
            # ip pim rp-address 6.6.6.6 group-list 239.1.1.0/24 bidir
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                af = 'ipv4' if groups['af'] == 'ip' else 'ipv6'

                rp_dict = vrf_dict.setdefault('address_family', {}).setdefault(af, {})\
                          .setdefault('rp', {}).setdefault('static_rp', {})\
                            .setdefault(groups['static_rp_address'], {})

                rp_dict.setdefault('policy_name', groups['static_rp_group_list']) \
                    if groups['static_rp_group_list'] else None

                rp_dict.setdefault('route_map', groups['static_rp_route_map']) \
                    if groups['static_rp_route_map'] else None

                rp_dict.setdefault('prefix_list', groups['static_rp_prefix_list']) \
                    if groups['static_rp_prefix_list'] else None

                if 'bidir' in str(groups['dummy']):
                    rp_dict['bidir'] = True
                if 'override' in str(groups['dummy']):
                    rp_dict['override'] = True
                continue

            # ip pim bsr rp-candidate loopback0 group-list 235.0.0.0/8 priority 128
            # ip pim rp-candidate loopback10 route-map filtera bidir
            # ip pim rp-candidate loopback10 prefix-list pfxlista priority 10
            # ip pim rp-candidate Ethernet1/1 group-list 239.0.0.0/24 priority 10 interval 60 bidir
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                af = 'ipv4' if groups['af'] == 'ip' else 'ipv6'

                rp_dict = vrf_dict.setdefault('address_family', {}).setdefault(af, {})\
                          .setdefault('rp', {}).setdefault('bsr', {})\
                            .setdefault(groups['bsr_rp_candidate_interface'], {})

                rp_dict['interface'] = groups['bsr_rp_candidate_interface']

                rp_dict.setdefault('policy', groups['bsr_rp_candidate_group_list']) \
                    if groups['bsr_rp_candidate_group_list'] else None

                rp_dict.setdefault('route_map', groups['bsr_rp_candidate_route_map']) \
                    if groups['bsr_rp_candidate_route_map'] else None

                rp_dict.setdefault('prefix_list', groups['bsr_rp_candidate_prefix_list']) \
                    if groups['bsr_rp_candidate_prefix_list'] else None

                interval = re.search('interval +(\d+)', groups['dummy'])
                priority = re.search('priority +(\d+)', groups['dummy'])
                bidir = re.search('bidir', groups['dummy'])
                if interval:
                    rp_dict['interval'] = int(interval.groups()[0])
                if priority:
                    rp_dict['priority'] = int(priority.groups()[0])
                if bidir:
                    rp_dict['mode'] = 'bidir'
                continue

            # ip pim send-rp-announce loopback0 group-list 236.0.0.0/8 bidir interval 60 scope 43
            # ip pim send-rp-announce 2.2.2.2 prefix-list abc bidir
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                rp_dict = vrf_dict.setdefault('address_family', {}).setdefault('ipv4', {})\
                        .setdefault('rp', {}).setdefault('autorp', {}).setdefault('send_rp_announce', {})
                rp_dict.setdefault('interface', groups['send_rp_announce_intf']) \
                    if groups['send_rp_announce_intf'] else None
                rp_dict.setdefault('group', groups['send_rp_announce_rp_group']) \
                    if groups['send_rp_announce_rp_group'] else None
                rp_dict.setdefault('group_list', groups['send_rp_announce_group_list']) \
                    if groups['send_rp_announce_group_list'] else None
                rp_dict.setdefault('route_map', groups['send_rp_announce_route_map']) \
                    if groups['send_rp_announce_route_map'] else None
                rp_dict.setdefault('prefix_list', groups['send_rp_announce_prefix_list']) \
                    if groups['send_rp_announce_prefix_list'] else None
                interval = re.search('interval +(\d+)', groups['dummy'])
                scope = re.search('scope +(\d+)', groups['dummy'])
                bidir = re.search('bidir', groups['dummy'])
                if interval:
                    rp_dict['interval'] = int(interval.groups()[0])
                if scope:
                    rp_dict['scope'] = int(scope.groups()[0])
                if bidir:
                    rp_dict['bidir'] = True
                continue

            # ip pim send-rp-discovery loopback0
            # ip pim send-rp-discovery loopback0 scope 34
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                rp_dict = vrf_dict.setdefault('address_family', {}).setdefault('ipv4', {}).setdefault('rp', {})\
                    .setdefault('autorp', {}).setdefault('send_rp_discovery', {})
                rp_dict['interface'] = groups['send_rp_discovery_intf']
                rp_dict.setdefault('scope', int(groups['send_rp_discovery_scope'])) \
                    if groups['send_rp_discovery_scope'] else None         
                continue

            # ip pim auto-rp forward listen
            m = p11.match(line)
            if m:
                rp_dict = vrf_dict.setdefault('address_family', {})\
                    .setdefault('ipv4', {}).setdefault('rp', {}).setdefault('autorp', {})
                rp_dict['autorp_listener'] = True        
                continue

        return pim_dict
