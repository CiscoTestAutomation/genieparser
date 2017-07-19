#############################################################################
# Parser For Show Interface
#############################################################################


class ShowInterfaceSchema(MetaParser):

    schema = {'interface':
                {Any():
                    {Optional('interface_state'): str,
                     Optional('admin_state'): str,
                     Optional('hardware_int'): str,
                     Optional('parent_interface'): str,
                     Optional('hardware_address'): str,
                     Optional('description'): str,
                     Optional('internet_address'): str,
                     Optional('mtu'): str,
                     Optional('bw'): str,
                     Optional('dly'): str,
                     Optional('reliability'): str,
                     Optional('txload'): str,
                     Optional('rxload'): str,
                     Optional('encapsulation'): str,
                     Optional('vlan_id'): str,
                     Optional('medium'): str,
                     Optional('port_mode'): str,
                     Optional('duplex_mode'): str,
                     Optional('port_speed'): str,
                     Optional('auto_negotiation'): str,
                     Optional('beacon'): str,
                     Optional('input_flow_control'): str,
                     Optional('output_flow_control'): str,
                     Optional('auto_mdix'): str,
                     Optional('switchport_monitor'): str,
                     Optional('ethertype'): str,
                     Optional('input_rate_bit_sec'): str,
                     Optional('input_rate_packets_sec'): str,
                     Optional('output_rate_bit_sec'): str,
                     Optional('output_rate_packets_sec'): str,
                     Optional('efficient_ethernet'): str,
                     Optional('last_linked_flapped'): str,
                     Optional('last_clearing'): str,
                     Optional('interface_reset'): str,
                     Optional('load_interval'):
                         {Any():
                             {Optional('input_time'): str,
                             Optional('output_time'): str,
                             Optional('o_rate_amount_bits_sec'): str,
                             Optional('o_rate_amount_packets_sec'): str,
                             Optional('i_rate_amount_packets_sec'): str,
                             Optional('i_rate_amount_bits_sec'): str,
                             Optional('load_interval_time'): str,
                             Optional('input_rate'): str,
                             Optional('input_rate_amount'): str,
                             'output_rate': str,
                             Optional('output_rate_amount'): str,
                             Optional('input_rate_bps'): str,
                             Optional('input_rate_pps'): str,
                             Optional('output_rate_bps'): str,
                             Optional('output_rate_pps'): str,
                            },
                        },
                    Optional('rx'):
                            {Optional('input_packets'): str,
                             Optional('unicast_packets'): str,
                             Optional('multicast_packets'): str,
                             Optional('broadcast_packets'): str,
                             Optional('broadcast_packets_bytes'): str,
                             Optional('input_packets'): str,
                             Optional('input_packets_bytes'): str,
                             Optional('jumbo_packets'): str,
                             Optional('storm_suppression_packets'): str,
                             Optional('runts'): str,
                             Optional('giants'): str,
                             Optional('crc_fcs'): str,
                             Optional('no_buffer'): str,
                             Optional('input_error'): str,
                             Optional('short_frame'): str,
                             Optional('overrun'): str,
                             Optional('underrun'): str,
                             Optional('ignored'): str,
                             Optional('watchdog'): str,
                             Optional('bad_etype_drop'): str,
                             Optional('bad_proto_drop'): str,
                             Optional('if_down_drop'): str,
                             Optional('input_with_dribble'): str,
                             Optional('input_discard'): str,
                             Optional('rx_pause'): str,
                            },
                        },                    
                     Optional('tx_output_packets'): str,
                     Optional('tx_unicast_packets'): str,
                     Optional('tx_multicast_packets'): str,
                     Optional('tx_broadcast_packets'): str,
                     Optional('tx_output_packets_byte'): str,
                     Optional('tx_broadcast_packets_bytes'): str,
                     Optional('tx_jumbo_packets'): str,
                     Optional('tx_output_error'): str,
                     Optional('tx_collision'): str,
                     Optional('tx_deferred'): str,
                     Optional('tx_late_collision'): str,
                     Optional('tx_lost_carrier'): str,
                     Optional('tx_no_carrier'): str,
                     Optional('tx_babble'): str,
                     Optional('tx_output_discard'): str,
                     Optional('tx_pause'): int
                    },
                }
                    
                

class ShowInterface(ShowInterfaceSchema):

    def cli(self):
        out = self.device.execute('show interface')

        interface_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # Ethernet2/1.10 is down (Administratively down)
            p1 =  re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.]+) *is'  
                              ' *(?P<interface_state>[a-zA-Z\(\)\s]+)$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                interface_state = m.groupdict()['interface_state']

                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}
                if interface not in interface_dict['interface']:
                    interface_dict['interface'][interface] = {}
                interface_dict['interface'][interface]['interface_state'] = interface_state
                continue

            p2 = re.compile(r'^\s*admin *state *is (?P<admin_state>[a-z]+)$')
            m = p2.match(line)
            if m:
                admin_state = m.groupdict()['admin_state']
        
                interface_dict['interface'][interface]['admin_state'] = admin_state
                continue

            p2_1 = re.compile(r'^\s*admin *state *is (?P<admin_state>[a-z]+), *Dedicated *Interface$')
            m = p2_1.match(line)
            if m:
                admin_state = m.groupdict()['admin_state']

                interface_dict['interface'][interface]['admin_state'] = admin_state
                continue


            p2_2 = re.compile(r'^\s*admin *state *is (?P<admin_state>[a-z]+), *Dedicated *Interface, \[parent *interface *is *(?P<parent_interface>[a-zA-Z0-9\/]+)\]$')
            m = p2_2.match(line)
            if m:
                admin_state = m.groupdict()['admin_state']
                parent_interface = m.groupdict()['parent_interface']

                interface_dict['interface'][interface]['parent_interface'] = parent_interface
                interface_dict['interface'][interface]['admin_state'] = admin_state
                continue

            p3 = re.compile(r'^\s*Hardware: *(?P<hardware_int>[a-zA-Z0-9]+),'
                        ' *address: *(?P<hardware_address>[a-z0-9\.\(\)\s]+)')
            m = p3.match(line)
            if m:
                hardware_int = m.groupdict()['hardware_int']
                hardware_address = m.groupdict()['hardware_address']

                interface_dict['interface'][interface]['hardware_int'] = hardware_int
                interface_dict['interface'][interface]['hardware_address'] = hardware_address
                continue

            p4 = re.compile(r'^\s*Description: *(?P<description>[a-z]+)$')
            m = p4.match(line)
            if m:
                description = m.groupdict()['description']

                interface_dict['interface'][interface]['description'] = description
                continue

            p5 = re.compile(r'^\s*Internet *Address *is *(?P<internet_address>[0-9\.\/]+)$')
            m = p5.match(line)
            if m:
                internet_address = m.groupdict()['internet_address']

                interface_dict['interface'][interface]['internet_address'] = internet_address
                continue

            p6 = re.compile(r'^\s*MTU *(?P<mtu>[0-9]+) *bytes, *BW *(?P<bw>[0-9]+) *kbit, *DLY *(?P<dly>[0-9]+) *usec$')
            m = p6.match(line)
            if m:
                mtu = m.groupdict()['mtu']
                bw = m.groupdict()['bw']
                dly = m.groupdict()['dly']

                interface_dict['interface'][interface]['mtu'] = mtu
                interface_dict['interface'][interface]['bw'] = bw
                interface_dict['interface'][interface]['dly'] = dly
                continue

            p7 = re.compile(r'^\s*reliability *(?P<reliability>[0-9\/]+),'
                ' *txload *(?P<txload>[0-9\/]+), *rxload *(?P<rxload>[0-9\/]+)$')
            m = p7.match(line)
            if m:
                reliability = m.groupdict()['reliability']
                txload = m.groupdict()['txload']
                rxload = m.groupdict()['rxload']

                interface_dict['interface'][interface]['reliability'] = reliability
                interface_dict['interface'][interface]['txload'] = txload
                interface_dict['interface'][interface]['rxload'] = rxload
                continue

            p8 = re.compile(r'^\s*Encapsulation *(?P<encapsulation>[A-Z]+),'
                             ' *medium *is *(?P<medium>[a-zA-Z]+)$')
            m = p8.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation']
                medium = m.groupdict()['medium']

                interface_dict['interface'][interface]['encapsulation'] = encapsulation
                interface_dict['interface'][interface]['medium'] = medium
                continue

            p8_1 = re.compile(r'^\s*Encapsulation *(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                               ' *vlan *ID *(?P<vlan_id>[0-9]+), *medium *is *(?P<medium>[a-zA-Z0-9]+)$')
            m = p8_1.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation']
                vlan_id = m.groupdict()['vlan_id']
                medium = m.groupdict()['medium']

                interface_dict['interface'][interface]['encapsulation'] = encapsulation
                interface_dict['interface'][interface]['vlan_id'] = vlan_id
                interface_dict['interface'][interface]['medium'] = medium
                continue


            p9 = re.compile(r'^\s*Port *mode *is *(?P<port_mode>[a-z]+)$')
            m = p9.match(line)
            if m:
                port_mode = m.groupdict()['port_mode']

                interface_dict['interface'][interface]['port_mode'] = port_mode
                continue

            p10 = re.compile(r'^\s*full-duplex, *(?P<duplex_mode>[0-9]+) *Mb/s$')
            m = p10.match(line)
            if m:
                duplex_mode = m.groupdict()['duplex_mode']

                interface_dict['interface'][interface]['duplex_mode'] = duplex_mode
                continue

            p11 = re.compile(r'^\s*Beacon *is *turned *(?P<beacon>[a-z]+)$')
            m = p11.match(line)
            if m:
                beacon = m.groupdict()['beacon']

                interface_dict['interface'][interface]['beacon'] = beacon
                continue

            p12 = re.compile(r'^\s*Auto-Negotiation *is *turned *(?P<auto_negotiation>[a-z]+)$')
            m = p12.match(line)
            if m:
                auto_negotiation = m.groupdict()['auto_negotiation']

                interface_dict['interface'][interface]['auto_negotiation'] = auto_negotiation
                continue

            p13 = re.compile(r'^\s*Input *flow-control *is *(?P<input_flow_control>[a-z]+),'
                              ' *output *flow-control *is *(?P<output_flow_control>[a-z]+)$')
            m = p13.match(line)
            if m:
                input_flow_control = m.groupdict()['input_flow_control']
                output_flow_control = m.groupdict()['output_flow_control']

                interface_dict['interface'][interface]['input_flow_control'] = input_flow_control
                interface_dict['interface'][interface]['output_flow_control'] = output_flow_control
                continue

            p14 = re.compile(r'^\s*Auto-mdix *is *turned *(?P<auto_mdix>[a-z]+)$')
            m = p14.match(line)
            if m:
                auto_mdix = m.groupdict()['auto_mdix']

                interface_dict['interface'][interface]['auto_mdix'] = auto_mdix
                continue

            p15 = re.compile(r'^\s*Switchport *monitor *is *(?P<switchport_monitor>[a-z]+)$')
            m = p15.match(line)
            if m:
                switchport_monitor = m.groupdict()['switchport_monitor']

                interface_dict['interface'][interface]['switchport_monitor'] = switchport_monitor
                continue

            p16 = re.compile(r'^\s*Ethertype *is *(?P<ethertype>[a-z0-9]+)$')
            m = p16.match(line)
            if m:
                ethertype = m.groupdict()['ethertype']

                interface_dict['interface'][interface]['ethertype'] = ethertype
                continue

            p17 = re.compile(r'^\s*1 *minute *input *rate *(?P<input_rate_bit_sec>[0-9]+)'
                              ' *bits/sec, *(?P<input_rate_packets_sec>[0-9]+) *packets/sec$')
            m = p17.match(line)
            if m:
                input_rate_bit_sec = m.groupdict()['input_rate_bit_sec']
                input_rate_packets_sec = m.groupdict()['input_rate_packets_sec']

                interface_dict['interface'][interface]['input_rate_bit_sec'] = input_rate_bit_sec
                interface_dict['interface'][interface]['input_rate_packets_sec'] = input_rate_packets_sec
                continue

            p18 = re.compile(r'^\s*1 *minute *output *rate *(?P<output_rate_bit_sec>[0-9]+)'
                              ' *bits/sec, *(?P<output_rate_packets_sec>[0-9]+) *packets/sec$')
            m = p18.match(line)
            if m:
                output_rate_bit_sec = m.groupdict()['output_rate_bit_sec']
                output_rate_packets_sec = m.groupdict()['output_rate_packets_sec']

                interface_dict['interface'][interface]['output_rate_bit_sec'] = output_rate_bit_sec
                interface_dict['interface'][interface]['output_rate_packets_sec'] = output_rate_packets_sec
                continue

            p19 = re.compile(r'^\s*EEE *\(efficient-ethernet\) *: *(?P<efficient_ethernet>[A-Za-z\/]+)$')
            m = p19.match(line)
            if m:
                efficient_ethernet = m.groupdict()['efficient_ethernet']

                interface_dict['interface'][interface]['efficient_ethernet'] = efficient_ethernet
                continue

            p20 = re.compile(r'^\s*Last *link *flapped *(?P<last_linked_flapped>[0-9\:]+)$')
            m = p20.match(line)
            if m:
                last_linked_flapped = m.groupdict()['last_linked_flapped']

                interface_dict['interface'][interface]['last_linked_flapped'] = last_linked_flapped
                continue

            p21 = re.compile(r'^\s*Last *clearing *of *\"show *interface\" *counters *(?P<last_clearing>[a-z]+)$')
            m = p21.match(line)
            if m:
                last_clearing = m.groupdict()['last_clearing']

                interface_dict['interface'][interface]['last_clearing'] = last_clearing
                continue

            p22 = re.compile(r'^\s*(?P<interface_reset>[0-9]+) *interface *resets$')
            m = p22.match(line)
            if m:
                interface_reset = m.groupdict()['interface_reset']

                interface_dict['interface'][interface]['interface_reset'] = interface_reset
                continue

            p23 = re.compile(r'^\s*Load-Interval *#(?P<load_interval>[0-9]+): *(?P<load_interval_time>[0-9]+) *seconds$')
            m = p23.match(line)
            if m:
                load_interval = m.groupdict()['load_interval']
                load_interval_time = m.groupdict()['load_interval_time']

                if 'load_interval' not in interface_dict['interface'][interface]:
                    interface_dict['interface'][interface]['load_interval'] = {}
                if load_interval not in interface_dict['interface'][interface]['load_interval']:
                    interface_dict['interface'][interface]['load_interval'][load_interval] = {}
                interface_dict['interface'][interface]['load_interval'][load_interval]['load_interval_time'] = load_interval_time
                continue

            p24 = re.compile(r'^\s*(?P<input_time>[0-9]+) *seconds *input *rate'
                              ' *(?P<i_rate_amount_bits_sec>[0-9]+) *bits/sec,'
                              ' *(?P<i_rate_amount_packets_sec>[0-9]+) *packets/sec$')
            m = p24.match(line)
            if m:
                input_time = m.groupdict()['input_time']
                i_rate_amount_bits_sec = m.groupdict()['i_rate_amount_bits_sec']
                i_rate_amount_packets_sec = m.groupdict()['i_rate_amount_packets_sec']

                interface_dict['interface'][interface]['load_interval'][load_interval]['input_time'] = input_time
                interface_dict['interface'][interface]['load_interval'][load_interval]['i_rate_amount_bits_sec'] = i_rate_amount_bits_sec
                interface_dict['interface'][interface]['load_interval'][load_interval]['i_rate_amount_packets_sec'] = i_rate_amount_packets_sec
                continue

            p25 = re.compile(r'^\s*(?P<output_time>[0-9]+) *seconds *output *rate'
                              ' *(?P<o_rate_amount_bits_sec>[0-9]+) *bits/sec,'
                              ' *(?P<o_rate_amount_packets_sec>[0-9]+) *packsts/sec$')
            m = p25.match(line)
            if m:
                time = m.groupdict()['output_time']
                o_rate_amount_bits_sec()['o_rate_amount_bits_sec']
                o_rate_amount_packets_sec()['o_rate_amount_packets_sec']

                interface_dict['interface'][interface]['load_interval'][load_interval]['output_time'] = output_time
                interface_dict['interface'][interface]['load_interval'][load_interval]['o_rate_amount_bits_sec'] = o_rate_amount_bits_sec
                interface_dict['interface'][interface]['load_interval'][load_interval]['o_rate_amount_packets_sec'] = o_rate_amount_packets_sec
                continue

            p26 = re.compile(r'^\s*input *rate *(?P<input_rate>[0-9]+) *bps,'
                              ' *(?P<input_rate_pps>[0-9]+) *pps; *output *rate'
                              ' *(?P<output_rate>[0-9]+) *bps, *(?P<output_rate_pps>[0-9]+) *pps$')
            m = p26.match(line)
            if m:
                input_rate = m.groupdict()['input_rate']
                input_rate_pps = m.groupdict()['input_rate_pps']
                output_rate = m.groupdict()['output_rate']
                output_rate_pps = m.groupdict()['output_rate_pps']

                interface_dict['interface'][interface]['load_interval'][load_interval]['input_rate'] = input_rate
                interface_dict['interface'][interface]['load_interval'][load_interval]['input_rate_pps'] = input_rate_pps
                interface_dict['interface'][interface]['load_interval'][load_interval]['output_rate'] = output_rate
                interface_dict['interface'][interface]['load_interval'][load_interval]['output_rate_pps'] = output_rate_pps
                continue

        #RX
            p27 = re.compile(r'^\s*(?P<unicast_packets>[0-9]+) +unicast +packets'
                              ' +(?P<multicast_packets>[0-9]+) +multicast +packets'
                              ' +(?P<broadcast_packets>[0-9]+) +broadcast +packets$')
            m = p27.match(line)
            if m:
                unicast_packets = m.groupdict()['unicast_packets']
                multicast_packets = m.groupdict()['multicast_packets']
                broadcast_packets = m.groupdict()['broadcast_packets']

                if 'rx' not in interface_dict['interface'][interface]:
                    interface_dict['interface'][interface]['rx'] = {}
        
                interface_dict['interface'][interface]['rx']['unicast_packets'] = unicast_packets
                interface_dict['interface'][interface]['rx']['multicast_packets'] = multicast_packets
                interface_dict['interface'][interface]['rx']['broadcast_packets'] = broadcast_packets
                continue

            p28 = re.compile(r'^\s*(?P<input_packets>[0-9]+) +input +packets +(?P<input_packets_bytes>[0-9]+) +bytes$')
            m = p28.match(line)
            if m:
                input_packets = m.groupdict()['input_packets']
                input_packets_bytes = m.groupdict()['input_packets_bytes']

                interface_dict['interface'][interface]['rx']['input_packets'] = input_packets
                interface_dict['interface'][interface]['rx']['input_packets_bytes'] = input_packets_bytes
                continue

            p29 = re.compile(r'^\s*(?P<jumbo_packets>[0-9]+) +jumbo +packets *(?P<storm_suppression_packets>[0-9]+) +storm +suppression +packets$')
            m = p29.match(line)
            if m:
                jumbo_packets = m.groupdict()['jumbo_packets']
                storm_suppression_packets = m.groupdict()['storm_suppression_packets']

                interface_dict['interface'][interface]['rx']['jumbo_packets'] = jumbo_packets
                interface_dict['interface'][interface]['rx']['storm_suppression_packets'] = storm_suppression_packets
                continue

            p30 = re.compile(r'^\s*(?P<runts>[0-9]+) *runts *(?P<giants>[0-9]+) *giants *(?P<crc_fcs>[0-9]+) *CRC/FCS *(?P<no_buffer>[0-9]+) *no *buffer$')
            m = p30.match(line)
            if m:
                runts = m.groupdict()['runts']
                giants = m.groupdict()['giants']
                crc_fcs = m.groupdict()['crc_fcs']
                no_buffer = m.groupdict()['no_buffer']

                interface_dict['interface'][interface]['rx']['runts'] = runts
                interface_dict['interface'][interface]['rx']['giants'] = giants
                interface_dict['interface'][interface]['rx']['crc_fcs'] = crc_fcs
                interface_dict['interface'][interface]['rx']['no_buffer'] = no_buffer
                continue

            p31 = re.compile(r'^\s*(?P<input_error>[0-9]+) *input *error'
                              ' *(?P<short_frame>[0-9]+) *short *frame'
                              ' *(?P<overrun>[0-9]+) *overrun *(?P<underrun>[0-9]+)'
                              ' *underrun *(?P<ignored>[0-9]+) *ignored$')
            m = p31.match(line)
            if m:
                input_error = m.groupdict()['input_error']
                short_frame = m.groupdict()['short_frame']
                overrun = m.groupdict()['overrun']
                underrun = m.groupdict()['underrun']
                ignored = m.groupdict()['ignored']

                interface_dict['interface'][interface]['rx']['input_error'] = input_error
                interface_dict['interface'][interface]['rx']['short_frame'] = short_frame
                interface_dict['interface'][interface]['rx']['overrun'] = overrun
                interface_dict['interface'][interface]['rx']['underrun'] = underrun
                interface_dict['interface'][interface]['rx']['ignored'] = ignored
                continue

            p32 = re.compile(r'^\s*(?P<watchdog>[0-9]+) *watchdog *(?P<bad_etype_drop>[0-9]+)'
                              ' *bad *etype *drop *(?P<bad_proto_drop>[0-9]+) *bad *proto'
                              ' *drop *(?P<if_down_drop>[0-9]+) *if *down *drop$')
            m = p32.match(line)
            if m:
                watchdog = m.groupdict()['watchdog']
                bad_etype_drop = m.groupdict()['bad_etype_drop']
                bad_proto_drop = m.groupdict()['bad_proto_drop']
                if_down_drop = m.groupdict()['if_down_drop']

                interface_dict['interface'][interface]['rx']['watchdog'] = watchdog
                interface_dict['interface'][interface]['rx']['bad_etype_drop'] = bad_etype_drop
                interface_dict['interface'][interface]['rx']['bad_proto_drop'] = bad_proto_drop
                interface_dict['interface'][interface]['rx']['if_down_drop'] = if_down_drop
                continue

            p33 = re.compile(r'^\s*(?P<input_with_dribble>[0-9]+) *input *with *dribble *(?P<input_discard>[0-9]+) *input *discard$')
            m = p33.match(line)
            if m:
                input_with_dribble = m.groupdict()['input_with_dribble']
                input_discard = m.groupdict()['input_discard']

                interface_dict['interface'][interface]['rx']['input_with_dribble'] = input_with_dribble
                interface_dict['interface'][interface]['rx']['input_discard'] = input_discard
                continue

            p34 = re.compile(r'^\s*(?P<rx_pause>[0-9]+) *Rx *pause$')
            m = p34.match(line)
            if m:
                rx_pause = m.groupdict()['rx_pause']

                interface_dict['interface'][interface]['rx']['rx_pause'] = rx_pause
                continue
        #TX 
            p35 = re.compile(r'^\s*(?P<tx_unicast_packets>[0-9]+) *unicast *packets'
                              ' *(?P<tx_multicast_packets>[0-9]+) *multicast *packets'
                              ' *(?P<tx_broadcast_packets>[0-9]+) *broadcast *packets$')
            m = p35.match(line)
            if m:
                tx_unicast_packets = str(m.groupdict()['tx_unicast_packets'])
                tx_multicast_packets = str(m.groupdict()['tx_multicast_packets'])
                tx_broadcast_packets = str(m.groupdict()['tx_broadcast_packets'])

                interface_dict['interface'][interface]['tx_unicast_packets'] = tx_unicast_packets
                interface_dict['interface'][interface]['tx_multicast_packets'] = tx_multicast_packets
                interface_dict['interface'][interface]['tx_broadcast_packets'] = tx_broadcast_packets
                continue

            p36 = re.compile(r'^\s*(?P<tx_output_packets>[0-9]+) *output *packets *(?P<tx_output_packets_bytes>[0-9]+) *bytes$')
            m = p36.match(line)
            if m:
                tx_output_packets = str(m.groupdict()['tx_output_packets'])
                tx_output_packets_bytes = str(m.groupdict()['tx_output_packets_bytes'])

                interface_dict['interface'][interface]['tx_output_packets'] = tx_output_packets
                interface_dict['interface'][interface]['tx_output_packets_bytes'] = tx_output_packets_bytes
                continue

            p37 = re.compile(r'^\s*(?P<tx_jumbo_packets>[0-9]+) *jumbo *packets$')
            m = p37.match(line)
            if m:
                tx_jumbo_packets = str(m.groupdict()['tx_jumbo_packets'])

                interface_dict['interface'][interface]['tx_jumbo_packets'] = tx_jumbo_packets
                continue

            p38 = re.compile(r'^\s*(?P<tx_output_error>[0-9]+) *output *error *(?P<tx_collision>[0-9]+)'
                              ' *collision *(?P<tx_deferred>[0-9]+) *deferred *(?P<tx_late_collision>[0-9]+)'
                              ' *late *collision$')
            m = p38.match(line)
            if m:
                tx_output_error = str(m.groupdict()['tx_output_error'])
                tx_collision = str(m.groupdict()['tx_collision'])
                tx_deferred = str(m.groupdict()['tx_deferred'])
                tx_late_collision = str(m.groupdict()['tx_late_collision'])

                interface_dict['interface'][interface]['tx_output_error'] = tx_output_error
                interface_dict['interface'][interface]['tx_collision'] = tx_collision
                interface_dict['interface'][interface]['tx_deferred'] = tx_deferred
                interface_dict['interface'][interface]['tx_late_collision'] = tx_late_collision
                continue

            p39 = re.compile(r'^\s*(?P<tx_lost_carrier>[0-9]+) *lost *carrier'
                              ' *(?P<tx_no_carrier>[0-9]+) *no *carrier'
                              ' *(?P<tx_babble>[0-9]+) *babble *(?P<tx_output_discard>[0-9]+) *output *discard$')
            m = p39.match(line)
            if m:
                tx_lost_carrier = str(m.groupdict()['tx_lost_carrier'])
                tx_no_carrier = str(m.groupdict()['tx_no_carrier'])
                tx_babble = str(m.groupdict()['tx_babble'])
                tx_output_discard = str(m.groupdict()['tx_output_discard'])

                interface_dict['interface'][interface]['tx_lost_carrier'] = tx_lost_carrier
                interface_dict['interface'][interface]['tx_no_carrier'] = tx_no_carrier
                interface_dict['interface'][interface]['tx_babble'] = tx_babble
                interface_dict['interface'][interface]['tx_output_discard'] = tx_output_discard
                continue

            p40 = re.compile(r'^\s*(?P<tx_pause>[0-9]+) *Tx *pause$')
            m = p40.match(line)
            if m:
                tx_pause = str(m.groupdict()['tx_pause'])

                interface_dict['interface'][interface]['tx_pause'] = tx_pause
                continue

        return interface_dict

#############################################################################
# Parser For Show Interface switchport
#############################################################################


class ShowIpInterfaceSwitchportSchema(MetaParser):

    schema = {'interface':
                {Any():
                    {'enabled': bool,
                     'monitor': bool,
                     'switchport_mode': str,
                     'access_vlan': str,
                     'trunk_vlans': str,
                     'encapsulation':
                        {'native_vlan': str,
                        },
                     'admin_priv_vlan_primary_host_assoc': str,
                     'admin_priv_vlan_secondary_host_assoc': str,
                     'admin_priv_vlan_primary_mapping': str,
                     'admin_priv_vlan_secondary_mapping': str,
                     'admin_priv_vlan_trunk_native_vlan': str,
                     'admin_priv_vlan_trunk_encapsulation': str,
                     'admin_priv_vlan_trunk_normal_vlans': str,
                     'admin_priv_vlan_trunk_private_vlans': str,
                     'operational_private_vlan': str
                     },
                },
            }
                    

class ShowIpInterfaceSwitchport(ShowIpInterfaceSwitchportSchema):

    def cli(self):
        out = self.device.execute('show ip interface switchport')

        ip_interface_switchport_dict = {}

        for line in out.splitlines()
            line = line.rstrip()

            #Name: Ethernet2/2
            p1 = re.compile(r'^\s*Name: *(?P<interface>[a-zA-Z0-9\/]+)$')
            m = p1.match(line)
            if m:
                 interface = m.groupdict()['interface']

                if 'interface' not in ip_interface_switchport_dict:
                    ip_interface_switchport_dict['interface'] = {}
                if interface not in ip_interface_switchport_dict['interface']:
                    ip_interface_switchport_dict['interface'][interface] = {}
                    continue

            #Switchport: Enabled
            p2 = re.compile(r'^\s*Switchport: *(?P<enabled>(enabled))$')
            m = p2.match(line)
            if m:
                
                enabled = m.groupdict()['enabled']

                ip_interface_switchport_dict['interface'][interface]['enabled'] = True
                continue

            #Switchport Monitor: Not enabled
            p3 = re.compile(r'^\s*Switchport *Monitor: *(?P<monitor>(Not enabled))$')
            m = p3.match(line)
            if m:
                monitor = m.groupdict()['monitor']

                ip_interface_switchport_dict['interface'][interface]['monitor'] = False
                continue

            #Operational Mode: trunk
            p4 = re.compile(r'^\s*Operational *Mode: *(?P<switchport_mode>[a-z]+)$')
            m = p4.match(line)
            if m:
                switchport_mode = m.groupdict()['switchport_mode']

                ip_interface_switchport_dict['interface'][interface]['switchport_mode'] = False
                continue

            #Access Mode VLAN: 1 (default)
            p5 = re.compile(r'^\s*Access *Mode *VLAN: *(?P<access_vlan>[0-9]+) *\((?P<access_vlan_mode>[a-z]+)\)$')
            m = p5.match(line)
            if m:
                access_vlan = m.groupdict()['access_vlan']
                access_vlan_mode = m.groupdict()['access_vlan_mode']

                ip_interface_switchport_dict['interface'][interface]['access_vlan'] = access_vlan
                ip_interface_switchport_dict['interface'][interface]['access_vlan_mode'] = access_vlan_mode
                continue

            #Trunking Native Mode VLAN: 1 (default)
            p6 = re.compile(r'^\s*Trunking *Native *Mode *VLAN:'
                             ' *(?P<native_vlan>[0-9]+)'
                             ' *\((?P<native_vlan_mode>[a-z]+)\)$')
            m = p6.match(line)
            if m:
                native_vlan = m.groupdict()['native_vlan']
                native_vlan_mode = m.groupdict()['native_vlan_mode']

                if 'encapsulation' not in ip_interface_switchport_dict['interface'][interface]:
                    ip_interface_switchport_dict['interface'][interface]['encapsulation'] = {}

                ip_interface_switchport_dict['interface'][interface]['encapsulation']['native_vlan'] = native_vlan
                ip_interface_switchport_dict['interface'][interface]['encapsulation']['native_vlan_mode'] = native_vlan_mode
                continue

            #Trunking VLANs Allowed: 100,300
            p7 = re.compile(r'^\s*Trunking *VLANs *Allowed: *(?P<trunk_vlans>[0-9\,]+)$')
            m = p7.match(line)
            if m:
                trunk_vlans = m.groupdict()['trunk_vlans']

                ip_interface_switchport_dict['interface'][interface]['trunk_vlans'] = trunk_vlans
                continue

            #Administrative private-vlan primary host-association: none
            p8 = re.compile(r'^\s*Administrative *private-vlan *primary'
                             ' *host-association:'
                             ' *(?P<admin_priv_vlan_primary_host_assoc>)$')
            m = p8.match(line)
            if m:
                admin_priv_vlan_primary_host_assoc = m.groupdict()['admin_priv_vlan_primary_host_assoc']

                ip_interface_switchport_dict['interface'][interface]['admin_priv_vlan_primary_host_assoc'] = admin_priv_vlan_primary_host_assoc
                continue

            #Administrative private-vlan secondary host-association: none
            p9 = re.compile(r'^\s*Administrative *private-vlan *secondary'
                             ' *host-association:'
                             ' *(?P<admin_priv_vlan_secondary_host_assoc>)$')
            m = p9.match(line)
            if m:
                admin_priv_vlan_secondary_host_assoc = m.groupdict()['admin_priv_vlan_secondary_host_assoc']

                ip_interface_switchport_dict['interface'][interface]['admin_priv_vlan_secondary_host_assoc'] = admin_priv_vlan_secondary_host_assoc
                continue

            #Administrative private-vlan primary mapping: none
            p10 = re.compile(r'^\s*Administrative *private-vlan *primary'
                             ' *mapping:'
                             ' *(?P<admin_priv_vlan_primary_mapping>)$')
            m = p10.match(line)
            if m:
                admin_priv_vlan_primary_mapping = m.groupdict()['admin_priv_vlan_primary_mapping']

                ip_interface_switchport_dict['interface'][interface]['admin_priv_vlan_primary_mapping'] = admin_priv_vlan_primary_mapping
                continue

            #Administrative private-vlan secondary mapping: none
            p11 = re.compile(r'^\s*Administrative *private-vlan *secondary'
                             ' *mapping:'
                             ' *(?P<admin_priv_vlan_secondary_mapping>)$')
            m = p11.match(line)
            if m:
                admin_priv_vlan_secondary_mapping = m.groupdict()['admin_priv_vlan_secondary_mapping']

                ip_interface_switchport_dict['interface'][interface]['admin_priv_vlan_secondary_mapping'] = admin_priv_vlan_secondary_mapping
                continue

            #Administrative private-vlan trunk native VLAN: none
            p12 = re.compile(r'^\s*Administrative *private-vlan *native'
                             ' *VLAN:'
                             ' *(?P<admin_priv_vlan_trunk_native_vlan>)$')
            m = p12.match(line)
            if m:
                admin_priv_vlan_trunk_native_vlan = m.groupdict()['admin_priv_vlan_trunk_native_vlan']

                ip_interface_switchport_dict['interface'][interface]['admin_priv_vlan_trunk_native_vlan'] = admin_priv_vlan_trunk_native_vlan
                continue

            #Administrative private-vlan trunk encapsulation: dot1q
            p13 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *encapsulation:'
                             ' *(?P<admin_priv_vlan_trunk_encapsulation>)$')
            m = p13.match(line)
            if m:
                admin_priv_vlan_trunk_encapsulation = m.groupdict()['admin_priv_vlan_trunk_encapsulation']

                ip_interface_switchport_dict['interface'][interface]['admin_priv_vlan_trunk_encapsulation'] = admin_priv_vlan_trunk_encapsulation
                continue

            #Administrative private-vlan trunk normal VLANs: none
            p14 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *normal VLANs:'
                             ' *(?P<admin_priv_vlan_trunk_normal_vlans>)$')
            m = p14.match(line)
            if m:
                admin_priv_vlan_trunk_normal_vlans = m.groupdict()['admin_priv_vlan_trunk_normal_vlans']

                ip_interface_switchport_dict['interface'][interface]['admin_priv_vlan_trunk_normal_vlans'] = admin_priv_vlan_trunk_normal_vlans
                continue

            #Administrative private-vlan trunk private VLANs: none
            p15 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *private VLANs:'
                             ' *(?P<admin_priv_vlan_trunk_private_vlans>)$')
            m = p15.match(line)
            if m:
                admin_priv_vlan_trunk_private_vlans = m.groupdict()['admin_priv_vlan_trunk_private_vlans']

                ip_interface_switchport_dict['interface'][interface]['admin_priv_vlan_trunk_private_vlans'] = admin_priv_vlan_trunk_private_vlans
                continue

            #Operational private-vlan: none
            p16 = re.compile(r'^\s*Operational *private-vlan:'
                             ' *(?P<operational_private_vlan>)$')
            m = p15.match(line)
            if m:
                operational_private_vlan = m.groupdict()['operational_private_vlan']

                ip_interface_switchport_dict['interface'][interface]['operational_private_vlan'] = operational_private_vlan
                continue

        return ip_interface_switchport_dict


#############################################################################
# Parser For Show Ip Interface Vrf All
#############################################################################


class ShowIpInterfaceVrfAllSchema(MetaParser):

    schema = {'vrf':
                {Any():
                    {'interface':
                        {Any():
                            {Optional('iod'): str,
                             Optional('interface_status'): str,
                             Optional('ip_add'): str,
                             Optional('ip_subnet'): str,
                             Optional('ip_broadcast_add'): str,
                             'ip_multicast_groups': str,
                             'mtu': str,
                             'route_preference': str,
                             'tag': str,
                             'proxy_arp': str,
                             'local_proxy_arp': str,
                             'multicast_routing': str,
                             'icmp_redirects': str,
                             'directed_broadcast': str,
                             'ip_forwarding': str,
                             'icmp_unreachable': str,
                             'icmp_port_unreachable': str,
                             'unicast_reverse_path': str,
                             'load_sharing': str,
                             'int_statistics_last_reset': str,
                             'int_software_stats': str,
                             'unicast_packets': str,
                             'unicast_bytes': str,
                             'multicast_packets': str,
                             'multicast_bytes': str,
                             'broadcast_packets': str,
                             'broadcast_bytes': str
                             'labeled_packets': str,
                             'labeled_bytes': str,
                             'wccp_redirect_outbound': str,
                             'wccp_redirect_inbound': str,
                             'wccp_redirect_exclude': str
                             },
                        },
                    },
                },
            }    

class ShowIpInterfaceVrfAll(ShowIpInterfaceVrfAllSchema):

    def cli(self):
        out = self.device.execute('show ip interface vrf all')

        ip_interface_vrf_all_dict = {}

        for line in out.splitlines()
            line = line.rstrip()

            #IP Interface Status for VRF "VRF1"
            p1 = re.compile(r'^\s*IP *Interface *Status *for *VRF *(?P<vrf>[a-zA-Z0-9\"]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']

                if 'vrf' not in ip_interface_vrf_all_dict:
                    ip_interface_vrf_all_dict['vrf'] = {}
                if vrf not in ip_interface_vrf_all_dict['vrf']:
                    ip_interface_vrf_all_dict['vrf'][vrf] = {}
                    continue

            #Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 36,
            p2 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/]+), *Interface *status: *(?P<interface_status>[a-z\-\/\s]+), *iod: *(?P<iod>[0-9]+),$')
            m = p2.match(line)
            if m:
                interface = m.groupdict()['interface']
                interface_status = m.groupdict()['interface_status']
                iod = m.groupdict()['iod']

                if 'interface' not in ip_interface_vrf_all_dict['vrf'][vrf]:
                    ip_interface_vrf_all_dict['vrf'][vrf]['interface'] = {}
                if interface not in ip_interface_vrf_all_dict['vrf'][vrf]['interface']:
                    ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface] = {}

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['interface_status'] = interface_status
                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['iod'] = iod
                continue

            #IP address: 10.4.4.4, IP subnet: 10.4.4.0/24
            p3 = re.compile(r'^\s*IP *address: *(?P<ip_add>[0-9\.]+), *IP *subnet: *(?P<ip_subnet>[a-z0-9\.\/\s]+)$')
            m = p3.match(line)
            if m:
                ip_add = m.groupdict()['ip_add']
                ip_subnet = m.groupdict()['ip_subnet']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['ip_add'] = ip_add
                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['ip_subnet'] = ip_subnet
                continue

            #IP broadcast address: 255.255.255.255
            p4 = re.compile(r'\s*IP *broadcast *address: *(?P<ip_broadcast_add>[0-9\.]+)$')
            m = p4.match(line)
            if m:
                ip_broadcast_add = m.groupdict('ip_broadcast_add')

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['ip_broadcast_add'] = ip_broadcast_add
                continue
            
            #IP multicast groups locally joined: none
            p5 = re.compile(r'\s*IP *multicast *groups *locally *joined: *(?P<ip_multicast_groups>[a-z]+)$')
            m = p5.match(line)
            if m:
                ip_multicast_groups = m.groupdict('ip_multicast_groups')

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['ip_multicast_groups'] = ip_multicast_groups
                continue

            #IP MTU: 1600 bytes (using link MTU)
            p6 = re.compile(r'\s*IP *MTU: *(?P<mtu>[0-9]+) *bytes *\(using *link *MTU\)$')
            m = p6.match(line)
            if m:
                mtu = m.groupdict()['mtu']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['mtu'] = mtu
                continue

            #IP primary address route-preference: 0, tag: 0
            p7 = re.compile(r'\s*IP *primary *address *route-preference: (?P<route_preference>[0-9]+), tag: (?P<tag>[0-9]+)$')
            m = p7.match(line)
            if m:
                route_preference = m.groupdict()['route_preference']
                tag = m.groupdict()['tag']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['route_preference'] = route_preference
                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['tag'] = tag
                continue

            #IP proxy ARP : disabled
            p8 = re.compile(r'\s*IP *proxy *ARP *: *(?P<proxy_arp>[a-z]+)$')
            m = p8.match(line)
            if m:
                proxy_arp = m.groupdict()['proxy_arp']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['proxy_arp'] = proxy_arp
                continue

            #IP Local Proxy ARP : disabled
            p9 = re.compile(r'\s*IP *Local *Proxy *ARP *: *(?P<local_proxy_arp>[a-z]+)$')
            m = p9.match(line)
            if m:
                local_proxy_arp = m.groupdict()['local_proxy_arp']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['local_proxy_arp'] = local_proxy_arp
                continue

            #IP multicast routing: disabled
            p10 = re.compile(r'\s*IP *multicast *routing: *(?P<multicast_routing>[a-z]+)$')
            m = p10.match(line)
            if m:
                multicast_routing = m.groupdict()['multicast_routing']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['multicast_routing'] = multicast_routing
                continue

            #IP icmp redirects: disabled
            p11 = re.compile(r'\s*IP *icmp *redirects: *(?P<icmp_redirects>[a-z]+)$')
            m = p11.match(line)
            if m:
                icmp_redirects = m.groupdict()['icmp_redirects']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['icmp_redirects'] = icmp_redirects
                continue

            #IP directed-broadcast: disabled
            p12 = re.compile(r'\s*IP directed-broadcast: *(?P<directed_broadcast>[a-z]+)$')
            m = p12.match(line)
            if m:
                directed_broadcast = m.groupdict()['directed_broadcast']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['directed_broadcast'] = directed_broadcast
                continue

            #IP Forwarding: disabled
            p13 = re.compile(r'\s*IP *Forwarding: *(?P<ip_forwarding>[a-z]+)$') 
            m = p13.match(line)
            if m:
                ip_forwarding = m.groupdict()['ip_forwarding']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['ip_forwarding'] = ip_forwarding
                continue

            #IP icmp unreachables (except port): disabled
            p14 = re.compile(r'\s*IP *icmp *unreachables *\(except *port\): *(?P<icmp_unreachable>[a-z]+)$')
            m = p14.match(line)
            if m:
                icmp_unreachable = m.groupdict()['icmp_unreachable']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['icmp_unreachable'] = icmp_unreachable
                continue

            #IP icmp port-unreachable: enabled
            p15 = re.compile(r'\s*IP *icmp *port-unreachable: *(?P<icmp_port_unreachable>[a-z]+)$')
            m = p15.match(line)
            if m:
                icmp_port_unreachable = m.groupdict()['icmp_port_unreachable']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['icmp_port_unreachable'] = icmp_port_unreachable
                continue

            #IP unicast reverse path forwarding: none
            p16 = re.compile(r'^\s*IP *unicast *reverse *path *forwarding: *(?P<unicast_reverse_path>[a-z]+)$')
            m = p16.match(line)
            if m:
                unicast_reverse_path = m.groupdict()['unicast_reverse_path']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['unicast_reverse_path'] = unicast_reverse_path
                continue

            #IP load sharing: none 
            p17 = re.compile(r'\s*IP *load *sharing: *(?P<load_sharing>[a-z]+)$')
            m = p17.match(line)
            if m:
                load_sharing = m.groupdict()['load_sharing']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['load_sharing'] = load_sharing
                continue

            #IP interface statistics last reset: never
            p18 = re.compile(r'\s*IP *interface *statistics *last *reset: *(?P<int_statistics_last_reset>[a-z]+)')
            m = p18.match(line)
            if m:
                int_statistics_last_reset = m.groupdict()['int_statistics_last_reset']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['int_statistics_last_reset'] = int_statistics_last_reset
                continue

            #IP interface software stats: (sent/received/forwarded/originated/consumed)
            p19 = re.compile(r'\s*IP *interface *software *stats: *(?P<int_software_stats>[a-z\/\(\)\s]+)')
            m = p19.match(line)
            if m:
                int_software_stats = m.groupdict()['int_software_stats']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['int_software_stats'] = int_software_stats
                continue

            #Unicast packets    : 0/0/0/0/0
            p20 = re.compile(r'\s*Unicast *packets *: *(?P<unicast_packets>[0-9\/]+)$')
            m = p20.match(line)
            if m:
                unicast_packets = m.groupdict()['unicast_packets']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['unicast_packets'] = unicast_packets
                continue

            #Unicast bytes      : 0/0/0/0/0
            p21 = re.compile(r'\s*Unicast *bytes *: *(?P<unicast_bytes>[0-9\/]+)$')
            m = p21.match(line)
            if m:
                unicast_bytes = m.groupdict()['unicast_bytes']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['unicast_bytes'] = unicast_bytes
                continue

            #Multicast packets  : 0/0/0/0/0
            p22 = re.compile(r'\s*Multicast *packets *: *(?P<multicast_packets>[0-9\/]+)$')
            m = p22.match(line)
            if m:
                multicast_packets = m.groupdict()['multicast_packets']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['multicast_packets'] = multicast_packets
                continue

            #Multicast bytes    : 0/0/0/0/0
            p23 = re.compile(r'\s*Multicast *bytes *: *(?P<multicast_bytes>[0-9\/]+)$')
            m = p23.match(line)
            if m:
                multicast_bytes = m.groupdict()['multicast_bytes']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['multicast_bytes'] = multicast_bytes
                continue

            #Broadcast packets  : 0/0/0/0/0
            p24 = re.compile(r'\s*Broadcast *packets *: *(?P<broadcast_packets>[0-9\/]+)$')
            m = p24.match(line)
            if m:
                broadcast_packets = m.groupdict()['broadcast_packets']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['broadcast_packets'] = broadcast_packets
                continue

            #Broadcast bytes    : 0/0/0/0/0
            p25 = re.compile(r'\s*Broadcast *bytes *: *(?P<broadcast_bytes>[0-9\/]+)$')
            m = p25.match(line)
            if m:
                broadcast_bytes = m.groupdict()['broadcast_bytes']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['broadcast_bytes'] = broadcast_bytes
                continue

            #Labeled packets    : 0/0/0/0/0
            p26 = re.compile(r'\s*Labeled *packets *: *(?P<labeled_packets>[0-9\/]+)$')
            m = p26.match(line)
            if m:
                labeled_packets = m.groupdict()['labeled_packets']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['labeled_packets'] = labeled_packets
                continue

            #Labeled bytes      : 0/0/0/0/0
            p27 = re.compile(r'\s*Labeled *bytes *: *(?P<labeled_bytes>[0-9\/]+)$')
            m = p27.match(line)
            if m:
                labeled_bytes = m.groupdict()['labeled_bytes']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['labeled_bytes'] = labeled_bytes
                continue

            #WCCP Redirect outbound: disabled
            p28 = re.compile(r'\s*WCCP *Redirect *outbound: *(?P<wccp_redirect_outbound>[a-z]+)$')
            m = p28.match(line)
            if m:
                wccp_redirect_outbound = m.groupdict()['wccp_redirect_outbound']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['wccp_redirect_outbound'] = wccp_redirect_outbound
                continue

            #WCCP Redirect inbound: disabled
            p29 = re.compile(r'\s*WCCP *Redirect *inbound: *(?P<wccp_redirect_inbound>[a-z]+)$')
            m = p29.match(line)
            if m:
                wccp_redirect_inbound = m.groupdict()['wccp_redirect_inbound']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['wccp_redirect_inbound'] = wccp_redirect_inbound
                continue

            #WCCP Redirect exclude: disabled
            p30 = re.compile(r'\s*WCCP *Redirect *exclude: *(?P<wccp_redirect_exclude>[a-z]+)$')
            m = p29.match(line)
            if m:
                wccp_redirect_exclude = m.groupdict()['wccp_redirect_exclude']

                ip_interface_vrf_all_dict['vrf'][vrf]['interface'][interface]['wccp_redirect_exclude'] = wccp_redirect_exclude
                continue

        return ip_interface_vrf_all_dict


#############################################################################
# Parser For Show Ipv6 Interface Vrf All
#############################################################################


class ShowIpv6InterfaceSchema(MetaParser):

    schema = {'vrf':
                {Any():
                    {'interface':
                        {Any():
                            {'interface_status': str,
                             'iod': str,
                             'ipv6':
                                {'ipv6_address': str,
                                 'ipv6_prefix_length': str,
                                 'ipv6_status': str,
                                },
                            'ipv6_subnet': str,
                            'ipv6_anycast': str,
                            'ipv6_link_local': str,
                            'ipv6_virtual': str,
                            'ipv6_multicast_routing': str,
                            'ipv6_report_link_local': str,
                            'ipv6_forwarding_feature': str,
                            'ipv6_multicast_groups': str,
                            'ipv6_multicast_entries': str,
                            'ipv6_mtu': str,
                            'ipv6_unicast_rev_path_forwarding': str,
                            'ipv6_load_sharing': str,
                            'ipv6_last_reset': str,
                            'ipv6_rp_traffic_statistics': str,
                            'unicast_packets': str,
                            'unicast_bytes': str,
                            'multicast_packets': str,
                            'multicast_bytes': str
                            },                    
                        },
                    },
                },
            }


class ShowIpv6Interface(ShowIpv6InterfaceSchema):

    def cli(self):
        out = self.device.execute('show ipv6 interface')

        ipv6_interface_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            #IPv6 Interface Status for VRF "VRF1"
            p1 = re.compile(r'^\s*IPv6 *Interface *Status *for *VRF'
                             ' *(?P<vrf>[a-zA-Z0-9\"]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']

                if 'vrf' not in ipv6_interface_dict:
                    ipv6_interface_dict['vrf'] = {}
                if vrf not in ipv6_interface_dict['vrf']:
                    ipv6_interface_dict['vrf'][vrf] = {}
                    continue

            p2 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/]+), Interface'
                             ' *status: *(?P<interface_status>[a-z\-\/]+),'
                             ' *iod: *(?P<iod>[0-9]+)$')
            m = p2.match(line)
            if m:
                interface = m.groupdict()['interface']
                interface_status = m.groupdict()['interface_status']
                iod = m.groupdict()['iod']

                if 'interface' not in ipv6_interface_dict['vrf'][vrf]:
                    ipv6_interface_dict['vrf'][vrf]['interface'] = {}
                if interface not in ipv6_interface_dict['vrf'][vrf]['interface']:
                    ipv6_interface_dict['vrf'][vrf]['interface'][interface] = {}
                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['interface_status'] = interface_status  
                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['iod'] = iod
                continue

            p3 = re.compile(r'^\s*IPv6 *address:$')
            m = p3.match(line)
            if m:
                if 'ipv6' not in ipv6_interface_dict['vrf'][vrf]['interface'][interface]:
                    ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6'] = {}
                    continue

            p3_1 = re.compile(r'^\s*(?P<ipv6_address>[a-z0-9\:]+)'
                               '(?P<ipv6_prefix_length>[0-9\/]+)'
                               ' *\[(?P<ipv6_status>[A-Z]+)\]$')
            m = p3_1.match(line)
            if m:
                ipv6_address = m.groupdict()['ipv6_address']
                ipv6_prefix_length = m.groupdict()['ipv6_prefix_length']
                ipv6_status = m.groupdict()['ipv6_status']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6']['ipv6_address'] = ipv6_address
                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6']['ipv6_prefix_length'] = ipv6_prefix_length
                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6']['ipv6_status'] = ipv6_status
                continue

            p4 = re.compile(r'^\s*IPv6 *subnet: *(?P<ipv6_subnet>[a-z0-9\:\/]+)$')
            m = p4.match(line)
            if m:
                ipv6_subnet = m.groupdict()['ipv6_subnet']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_subnet'] = ipv6_subnet
                continue

            p5 = re.compile(r'^\s*Anycast *configured *addresses:$')
            m = p5.match(line)
            if m:
                continue

            p6 = re.compile(r'^\s*(?P<ipv6_anycast>[a-zA-Z0-9\:\/\[\]])$')
            m = p6.match(line)
            if m:
                ipv6_anycast = m.groupdict()['ipv6_anycast']
                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_anycast'] = ipv6_anycast
                continue

            p7 = re.compile(r'^\s*IPv6 *link-local *address: *(?P<ipv6_link_local>[a-zA-Z0-9\:\(\)\s]+)$')
            m = p7.match(line)
            if m:
                ipv6_link_local = m.groupdict()['ipv6_link_local']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_link_local'] = ipv6_link_local
                continue

            p8 = re.compile(r'^\s*IPv6 *virtual *addresses *configured: *(?P<ipv6_virtual>[a-z]+)$')
            m = p8.match(line)
            if m:
                ipv6_virtual = m.groupdict()['ipv6_virtual']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_virtual'] = ipv6_virtual
                continue

            p9 = re.compile(r'^\s*IPv6 *multicast *routing: *(?P<ipv6_multicast_routing>[a-z]+)$')
            m = p9.match(line)
            if m:
                ipv6_multicast_routing = m.groupdict()['ipv6_multicast_routing']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_multicast_routing'] = ipv6_multicast_routing
                continue

            p10 = re.compile(r'^\s*IPv6 *report *link *local: *(?P<ipv6_report_link_local>[a-z]+)$')
            m = p10.match(line)
            if m:
                ipv6_report_link_local = m.groupdict()['ipv6_report_link_local']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_report_link_local'] = ipv6_report_link_local
                continue

            p11 = re.compile(r'^\s*IPv6 *Forwarding *feature: *(?P<ipv6_forwarding_feature>[a-z]+)$')
            m = p11.match(line)
            if m:
                ipv6_forwarding_feature = m.groupdict()['ipv6_forwarding_feature']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_forwarding_feature'] = ipv6_forwarding_feature
                continue

            p12 = re.compile(r'^\s*IPv6 *multicast *groups *locally *joined:$')
            m = p12.match(line)
            if m:
                continue

            p13 = re.compile(r'^\s*(?P<ipv6_multicast_groups>[a-z0-9\:\s]+)$')
            m = p13.match(line)
            if m:
                ipv6_multicast_groups = m.groupdict()['ipv6_multicast_groups']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_multicast_groups'] = ipv6_multicast_groups
                continue

            p14 = re.compile(r'^\s*IPv6 *multicast *(S,G) *entries *joined:'
                              ' *(?P<ipv6_multicast_entries>[a-z]+)$')
            m = p14.match(line)
            if m:
                ipv6_multicast_entries = m.groupdict()['ipv6_multicast_entries']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_multicast_entries'] = ipv6_multicast_entries
                continue

            p15 = re.compile(r'^\s*IPv6 MTU: *(?P<ipv6_mtu>[0-9]+)'
                              ' *\(using *link *MTU\)$')
            m = p15.match(line)
            if m:
                ipv6_mtu = m.groupdict()['ipv6_mtu']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_mtu'] = ipv6_mtu
                continue

            p16 = re.compile(r'^\s*IPv6 *unicast *reverse *path *forwarding:'
                              ' *(?P<ipv6_unicast_rev_path_forwarding>[a-z]+)$')
            m = p16.match(line)
            if m:
                ipv6_unicast_rev_path_forwarding = m.groupdict()['ipv6_unicast_rev_path_forwarding']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_unicast_rev_path_forwarding'] = ipv6_unicast_rev_path_forwarding
                continue

            p17 = re.compile(r'^\s*IPv6 *load *sharing:'
                             ' *(?P<ipv6_load_sharing>[a-z]+)$')
            m = p17.match(line)
            if m:
                ipv6_load_sharing = m.groupdict()['ipv6_load_sharing']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_load_sharing'] = ipv6_load_sharing
                continue

            p18 = re.compile(r'^\s*IPv6 *interface *statistics *last *reset:'
                              ' *(?P<ipv6_last_reset>[a-z]+)$')
            m = p18.match(line)
            if m:
                ipv6_last_reset = m.groupdict()['ipv6_last_reset']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_last_reset'] = ipv6_last_reset
                continue

            p19 = re.compile(r'^\s*IPv6 *interface *RP-traffic *statistics:'
                              ' *(?P<ipv6_rp_traffic_statistics>[a-z\(\)\/]+)$')
            m = p19.match(line)
            if m:
                ipv6_rp_traffic_statistics = m.groupdict()['ipv6_rp_traffic_statistics']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['ipv6_rp_traffic_statistics'] = ipv6_rp_traffic_statistics
                continue

            p20 = re.compile(r'^\s*Unicast *packets: (?P<unicast_packets>[0-9\/]+)$')
            m = p20.match(line)
            if m:
                unicast_packets = m.groupdict()[unicast_packets]

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['unicast_packets'] = unicast_packets
                continue

            p21 = re.compile(r'^\s*Unicast *bytes: *(?P<unicast_bytes>[0-9\/]+)$')
            m = p21.match(line)
            if m:
                unicast_bytes = m.groupdict()[unicast_bytes]

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['unicast_bytes'] = unicast_bytes
                continue

            p22 = re.compile(r'^\s*Multicast *packets: *(?P<multicast_packets>[0-9\/]+)$')
            m = p22.match(line)
            if m:
                multicast_packets = m.groupdict()['multicast_packets']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['multicast_packets'] = multicast_packets
                continue

            p23 = re.compile(r'^\s*Multicast *bytes: *(?P<multicast_bytes>[0-9\/]+)$')
            m = p23.match(line)
            if m:
                multicast_bytes = m.groupdict()['multicast_bytes']

                ipv6_interface_dict['vrf'][vrf]['interface'][interface]['multicast_bytes'] = multicast_bytes
                continue

        return ipv6_interface_dict



#############################################################################
# Parser For Show Vrf All Interface
#############################################################################


class ShowVrfAllInterfaceSchema(MetaParser):

    schema = {'interface': 
                {Any():
                    {'vrf_name': str,
                     'vrf_id': str,
                     'site_of_origin': str
                    },
                },
            }

class ShowVrfAllInterface(ShowVrfAllInterfaceSchema):

    def cli(self):
        out = self.device.execute('show vrf all interface')

        vrf_all_interface_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            p1 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\.\/]+) *(?P<vrf_name>[a-zA-Z0-9]+)'
                   ' *(?P<vrf_id>[0-9]+) *(?P<site_of_origin>[a-zA-Z\-]+)$')

            m = p1.match(line)
            if m:

                interface = m.groupdict()['interface']
                vrf_name = m.groupdict()['vrf_name']
                vrf_id = m.groupdict()['vrf_id']
                site_of_origin = m.groupdict()['site_of_origin']

                if 'interface' not in vrf_all_interface_dict:
                    vrf_all_interface_dict['interface'] = {}
                if interface not in vrf_all_interface_dict['interface']:
                    vrf_all_interface_dict['interface'][interface] = {}
                vrf_all_interface_dict['interface'][interface]['vrf_name'] = vrf_name
                vrf_all_interface_dict['interface'][interface]['vrf_id'] = vrf_id
                vrf_all_interface_dict['interface'][interface]['site_of_origin'] = site_of_origin

        return vrf_all_interface_dict









            














