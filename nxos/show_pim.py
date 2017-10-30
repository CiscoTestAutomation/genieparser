import re
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional

# ====================================================
# schema Parser for 'show ip pim interface'
# ====================================================
class ShowIpPimInterfaceSchema(MetaParser):

    '''Schema for show ip pim interface'''

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
    '''Parser for show ip pim interface'''

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
            p2 = re.compile(r'^\s*(?P<interface_name>[\w\/]+),?'
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
            p13 = re.compile(r'^\s*PIM +Neighbor +policy: +(?P<nbr_policy>[\w\-\s]+)$')
            m = p13.match(line)
            if m:
                neighbor_filter = m.groupdict()['nbr_policy']

            # PIM Join-Prune inbound policy: v4jp-policy
            p14 = re.compile(r'^\s*PIM +Join-Prune +inbound +policy: +(?P<jp_inbound_policy>[\w\-\s]+)$')
            m = p14.match(line)
            if m:
                jp_inbound_policy = m.groupdict()['jp_inbound_policy']

            # PIM Join-Prune outbound policy: v4jp-policy
            p15 = re.compile(r'^\s*PIM +Join-Prune +outbound +policy: +(?P<jp_outbound_policy>[\w\-\s]+)$')
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

    '''Schema for show ipv6 pim vrf all detail'''

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
    '''Parser for show ipv6 pim vrf all detail'''

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
            p2 = re.compile(r'^\s*State +Limit: +(?P<state_limit>\w+)$')
            m = p2.match(line)
            if m:
                state_limit = m.groupdict()['state_limit'].lower()
                parsed_dict['vrf'][vrf_name]['address_family'] \
                [af_name]['state_limit'] = state_limit
                continue


            # Register Rate Limit: none
            p3 = re.compile(r'^\s*Register +Rate +Limit: +(?P<register_rate_limit>\w+)$')
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
            p6 = re.compile(r'^\s*Shared +tree +ranges: +(?P<shared_tree_ranges>\w+)$')
            m = p6.match(line)
            if m:
                shared_tree_ranges = m.groupdict()['shared_tree_ranges']
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['shared_tree_ranges'] = shared_tree_ranges

                continue

        return parsed_dict