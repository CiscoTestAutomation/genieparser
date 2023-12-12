"""show_mcast.py

IOSXE parsers for the following show commands:

    * show ip mroute
    * show ipv6 mroute
    * show ip mroute
    * show ip mroute vrf <vrf_name>
    * show ipv6 mroute
    * show ipv6 mroute vrf <vrf_name>
    * show ip mroute static
    * show ip mroute vrf <vrf_name> static
    * show ip multicast
    * show ip multicast vrf <vrf_name>
    * show ip multicast mpls vif
    * show consistency-checker run-id <id>
    * show consistency-checker run-id <id> detail
    * show consistency-checker mcast <layer> start all'
    * 'show consistency-checker mcast <layer> start <address> <source>',
    * 'show consistency-checker mcast <layer> start vrf <instance_name> <address> <source>',
    * 'show consistency-checker mcast <layer> start vlan <vlan_id> <address>
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# =====================================
# Parser for 'show ip mroute'
# Parser for 'show ip mroute vrf xxx'
# Parser for 'show ipv6 mroute'
# Parser for 'show ipv6 mroute vrf xxx'
# =====================================

class ShowIpMrouteSchema(MetaParser):
    """Schema for:
        show ip mroute
        show ip mroute {group}
        show ip mroute {group} {source}
        show ip mroute verbose
        show ip mroute {group} verbose
        show ip mroute {group} {source} verbose
        show ip mroute vrf {vrf}
        show ip mroute vrf {vrf} {group}
        show ip mroute vrf {vrf} {group} {source}
        show ip mroute vrf {vrf} verbose
        show ip mroute vrf {vrf} {group} verbose
        show ip mroute vrf {vrf} {group} {source} verbose
        show ipv6 mroute
        show ipv6 mroute {group}
        show ipv6 mroute {group} {source}
        show ipv6 mroute verbose
        show ipv6 mroute {group} verbose
        show ipv6 mroute {group} {source} verbose
        show ipv6 mroute vrf {vrf}
        show ipv6 mroute vrf {vrf} {group}
        show ipv6 mroute vrf {vrf} {group} {source}
        show ipv6 mroute vrf {vrf} verbose
        show ipv6 mroute vrf {vrf} {group} verbose
        show ipv6 mroute vrf {vrf} {group} {source} verbose"""

    schema = {'vrf':         
                {Any():
                    {'address_family':
                        {Any(): 
                            {Optional('multicast_group'): 
                                {Any(): 
                                    {Optional('source_address'): 
                                        {Any(): 
                                            {Optional('uptime'): str,
                                             Optional('expire'): str,
                                             Optional('flags'): str,
                                             Optional('rp_bit'): bool,
                                             Optional('msdp_learned'): bool,                                             
                                             Optional('rp'): str,
                                             Optional('rpf_nbr'): str,
                                             Optional('rpf_info'): str,
                                             Optional('upstream_interface'):
                                                {Any():
                                                    {
                                                        'rpf_nbr': str,
                                                    }
                                                },
                                             Optional('incoming_interface_list'):
                                                {Any(): 
                                                    {Optional('rpf_nbr'): str,
                                                     Optional('rpf_info'): str,
                                                     Optional('state'): str,
                                                     Optional('iif_lisp_rloc'): str,
                                                     Optional('iif_lisp_group'): str,
                                                     Optional('lisp_vrf'): str,
                                                    },
                                                },
                                             Optional('outgoing_interface_list'): 
                                                {Any(): 
                                                    {'uptime': str,
                                                     'expire': str,
                                                     'state_mode': str,
                                                     Optional('flags'): str,
                                                     Optional('pkts'): int,
                                                     Optional('vcd'): str,
                                                     Optional('lisp_mcast_source'): str,
                                                     Optional('lisp_mcast_group'): str,
                                                     Optional('vxlan_version'): str,
                                                     Optional('vxlan_vni'): str,
                                                     Optional('vxlan_nxthop'): str,
                                                     Optional('lisp_join_sender_list'):
                                                        {Any():
                                                            {'uptime': str,
                                                             'expire': str,
                                                            },
                                                        },
                                                    },
                                                },
                                             Optional('extranet_rx_vrf_list'):
                                                {Any():
                                                    {'e_src':str,
                                                     'e_grp':str,
                                                     'e_uptime':str,
                                                     'e_expire':str,
                                                     Optional('e_rp'):str,
                                                     'e_oif_count':str,
                                                     'e_flags':str,
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

class ShowIpMroute(ShowIpMrouteSchema):
    """Parser for:
      show ip mroute
      show ip mroute {group}
      show ip mroute {group} {source}
      show ip mroute verbose
      show ip mroute {group} verbose
      show ip mroute {group} {source} verbose
      show ip mroute vrf {vrf}
      show ip mroute vrf {vrf} {group}
      show ip mroute vrf {vrf} {group} {source}
      show ip mroute vrf {vrf} verbose
      show ip mroute vrf {vrf} {group} verbose
      show ip mroute vrf {vrf} {group} {source} verbose"""

    cli_command = ['show ip mroute',
                   'show ip mroute vrf {vrf}',
                   'show ip mroute vrf {vrf} {group} {source}',
                   'show ip mroute vrf {vrf} {group}',
                   'show ip mroute {group}',
                   'show ip mroute {group} {source}',
                   'show ip mroute {verbose}',
                   'show ip mroute {group} {verbose}',
                   'show ip mroute {group} {source} {verbose}',
                   'show ip mroute vrf {vrf} {verbose}',
                   'show ip mroute vrf {vrf} {group} {verbose}',
                   'show ip mroute vrf {vrf} {group} {source} {verbose}' ]
    exclude = ['expire', 'uptime', 'outgoing_interface_list', 'flags']


    def cli(self, vrf='', verbose='', group='', source='', address_family='ipv4', output=None):
        cmd="show ip mroute"
        
        if output is None:
            if vrf:
                cmd += " vrf {vrf}".format(vrf=vrf)
            else:
                vrf='default'    
            if group:
                cmd += " {group}".format(group=group)
            if source:
                cmd += " {source}".format(source=source)
            if verbose:
                cmd += " {verbose}".format(verbose=verbose)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        mroute_dict = {}
        sub_dict = {}
        outgoing = False
        # IP Multicast Routing Table
        # Multicast Routing Table
        p1 = re.compile(r'^(?P<address_family>[\w\W]+)? *[mM]ulticast'
                        ' +[rR]outing +[tT]able$')
        # (*, 239.1.1.1), 00:00:03/stopped, RP 10.4.1.1, flags: SPF
        # (10.4.1.1, 239.1.1.1), 00:00:03/00:02:57, flags: PFT
        # (*, FF07::1), 00:04:45/00:02:47, RP 2001:DB8:6::6, flags:S
        # (2001:DB8:999::99, FF07::1), 00:02:06/00:01:23, flags:SFT
        # (50.50.50.2, 239.0.0.13), 00:00:39/00:02:20, flags:
        p2 = re.compile(r'^\((?P<source_address>[\w\:\.\*\/]+),'
                            '(\s+)?(?P<multicast_group>[\w\:\.\/]+)\),'
                            ' +(?P<uptime>[\w\:\.]+)\/'
                            '(?P<expires>[\w\:\.\-]+),'
                            '( +RP +(?P<rendezvous_point>[\w\:\.]+),)?'
                            ' +flags: *(?P<flags>[a-zA-Z]*)$')  
                            
        # Incoming interface: Null, RPF nbr 224.0.0.0224.0.0.0
        # Incoming interface: Loopback0, RPF nbr 0.0.0.0, Registering
        # Incoming interface: Lspvif10, RPF nbr 3.3.3.3, MDT [10, 3.3.3.3]/00:02:11
        # Incoming interface: LISP0.4100, RPF nbr 100.22.22.22, LISP: [100.22.22.22, 232.100.100.234]
        # Incoming interface: LISP0.4100, RPF nbr 100.88.88.88, using vrf VRF1
        p3 = re.compile(r'^Incoming +interface:'
                       ' +(?P<incoming_interface>[a-zA-Z0-9\/\-\.]+),'
                       ' +RPF +nbr +(?P<rpf_nbr>[\w\:\.]+)'
                       '(\s*,\s+LISP:\s\[(?P<iif_lisp_rloc>[\d\.]+)\,\s(?P<iif_lisp_group>[\d\.]+)\])?'
                       '(\s*,\s+using\s+vrf\s+(?P<lisp_vrf>[a-zA-Z0-9]+)\s*)?'
                       '(, *(?P<status>.*))?$') 
                       
        # Incoming interface:Tunnel5
        p3_1 = re.compile(r'^Incoming +interface:'
                         ' *(?P<incoming_interface>[a-zA-Z0-9\/\-\.]+)$')  
        # RPF nbr:2001:db8:90:24::6
        p3_2 = re.compile(r'^RPF +nbr: *(?P<rpf_nbr>[\w\:\.]+)$')
        # Outgoing interface list: Null
        # Outgoing interface list:
        p4 =  re.compile(r'^Outgoing +interface +list:|^Immediate +Outgoing +interface +list:'
                         '|^Inherited +Outgoing +interface +list:'
                         '( *(?P<intf>\w+))?$')       
        # Vlan5, Forward/Dense, 00:03:25/00:00:00, H
        # Vlan5, Forward/Dense, 00:04:35/00:02:30
        # ATM0/0, VCD 14, Forward/Sparse, 00:03:57/00:02:53
        # POS4/0, Forward, 00:02:06/00:03:27
        # LISP0.4100, (172.24.0.3, 232.0.0.199), Forward/Sparse, 00:10:33/stopped
        # LISP0.101, NH 100:44:44::44, Forward, 04:54:20/00:03:09
        # Vlan500, VXLAN v4 Encap: (50000, 225.2.2.2), Forward/Sparse, 00:00:54/00:02:05
        # Vlan500, VXLAN v6 Encap: (50000, FF13::1), Forward/Sparse, 00:17:31/stopped, flags:
        p5 = re.compile(r'^(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+)(\,\s+)?'
                            '(VCD +(?P<vcd>\d+))?(\,\s+)?'
                            '(NH)?(\s+)?(\(?(?P<lisp_mcast_source>[0-9\.:]+)(\,\s+)?(?P<lisp_mcast_group>[0-9\.]+)?\)?)?(\,\s+)?'
                            '(VXLAN +(?P<vxlan_version>[a-z0-9]+)(\s+)?(Encap:)?(\s+)?(\(?(?P<vxlan_vni>[0-9]+)(\,\s+)?(?P<vxlan_nxthop>[\w\:\.]+)?\)?)?)?(\,\s+)?'
                            '(?P<state_mode>[\w\-\/-]+)(\,\s+)?'
                            '(?P<uptime>[a-zA-Z0-9\:]+)\/'
                            '(?P<expire>[\w\:]+)(\,\s+)?'
                            '(Pkts\:(?P<pkts>\w+))?(\,\s+)?'
                            '(flags\:\s+(?P<flags>\w+)?$|(,\s+flags\:)?$)')
        # 100.11.11.11, 2d22h/00:02:36
        p5_1 = re.compile(r'^\s*(?P<lisp_js_addr>[0-9\.]+)\,\s*'
                            '(?P<lisp_js_uptime>[\w\:]+)\/(?P<lisp_js_expire>[\w\:]+)$')
        # Extranet receivers in vrf internet:
        p7 = re.compile(r'^Extranet receivers in vrf (?P<extranet_vrf>[a-zA-Z0-9]+)\:\s*$')
        # (192.168.1.3, 232.64.64.1), 21:38:05/00:03:25, OIF count: 1, flags: sTpl
        # (*, 239.5.1.100), 12:54:25/stopped, RP 152.1.1.1, OIF count: 0, flags: SP
        p8 = re.compile(r'^\((?P<e_src>[\d\.\*]+)\,(\s+)?'
                              '(?P<e_grp>[\d\.]+)\)\,(\s+)?'
                              '(?P<e_uptime>[\w\:]+)\/'
                              '(?P<e_expire>[\w\:]+)\,(\s+)?'
                              '(RP\s+(?P<e_rp>[\d\.]+)\,(\s+)?)?'
                              '(OIF count:\s(?P<e_oif_count>\d+))\,(\s+)?'
                              '(flags: (?P<e_flags>[\w]+))(\s+)?$')
        for line in out.splitlines():
            line = line.strip()

            # IP Multicast Routing Table
            # Multicast Routing Table
            ### add the default value, incase above commands not in output
            #address_family='ipv4'
            m = p1.match(line)
            if m:
                address_family = m.groupdict()['address_family']
                if address_family:
                    if address_family.strip().lower() == 'ip':
                        address_family = 'ipv4'
                else:
                    address_family = 'ipv6'                   
                continue    


            mroute_dict.setdefault('vrf',{})     
            mroute_data = mroute_dict['vrf'].setdefault(vrf,{}).setdefault('address_family',{}).setdefault(address_family,{})
    

            # if IP Multicast Routing Table not in output
            if 'vrf' not in mroute_dict:
                mroute_dict['vrf'] = {}
                mroute_dict['vrf'][vrf] = {}
                mroute_dict['vrf'][vrf]['address_family'] = {}
                address_family="ipv4"
                mroute_dict['vrf'][vrf]['address_family'][address_family] = {}
                
            # (*, 239.1.1.1), 00:00:03/stopped, RP 10.4.1.1, flags: SPF
            # (10.4.1.1, 239.1.1.1), 00:00:03/00:02:57, flags: PFT
            # (*, FF07::1), 00:04:45/00:02:47, RP 2001:DB8:6::6, flags:S
            # (2001:DB8:999::99, FF07::1), 00:02:06/00:01:23, flags:SFT
            m = p2.match(line)
            if m:
                source_address = m.groupdict()['source_address']
                multicast_group = m.groupdict()['multicast_group']
                ### initiate index value to zero for each S,G pair for multiple OG interfaces
                idx=0
                previous_intf = ""


                mroute_data.setdefault('multicast_group',{})
                sub_dict = mroute_data.setdefault('multicast_group',{}).setdefault(
                    multicast_group,{}).setdefault('source_address',
                    {}).setdefault(source_address,{})

                sub_dict['uptime'] = m.groupdict()['uptime']
                sub_dict['expire'] = m.groupdict()['expires']
                flags = m.groupdict()['flags']
                sub_dict['flags'] = flags
                if "M" in flags:
                    sub_dict['msdp_learned'] = True
                else:
                    sub_dict['msdp_learned'] = False
                if "R" in flags:
                    sub_dict['rp_bit'] = True
                else:
                    sub_dict['rp_bit'] = False

                
                rendezvous_point = m.groupdict()['rendezvous_point']
                if rendezvous_point:
                    sub_dict['rp'] = rendezvous_point

                continue

            # Incoming interface: Null, RPF nbr 224.0.0.0224.0.0.0
            # Incoming interface: Loopback0, RPF nbr 0.0.0.0, Registering
            # Incoming interface: Lspvif10, RPF nbr 3.3.3.3, MDT [10, 3.3.3.3]/00:02:11
            # Incoming interface: LISP0.4100, RPF nbr 100.22.22.22, LISP: [100.22.22.22, 232.100.100.234]
            # Incoming interface: LISP0.4100, RPF nbr 100.88.88.88, using vrf VRF1
            m = p3.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']
                rpf_nbr = m.groupdict()['rpf_nbr']
                rpf_info = m.groupdict()['status']
                
                sub_dict['rpf_nbr'] = rpf_nbr
                if rpf_info:
                    sub_dict['rpf_info'] = rpf_info.lower()

                if incoming_interface.lower() == 'null':
                    sub_dict['rpf_nbr'] = rpf_nbr
                    if rpf_info:
                        sub_dict['rpf_info'] = rpf_info.lower()
                    continue

                ing_intf_dict = sub_dict.setdefault('incoming_interface_list',{}).setdefault(incoming_interface,{})

                ing_intf_dict['rpf_nbr'] = rpf_nbr
                if rpf_info:
                    ing_intf_dict['rpf_info'] = rpf_info.lower()
                if m.groupdict()['iif_lisp_rloc']:
                    sub_dict['incoming_interface_list'][incoming_interface]['iif_lisp_rloc'] = m.groupdict()['iif_lisp_rloc']
                    sub_dict['incoming_interface_list'][incoming_interface]['iif_lisp_group'] = m.groupdict()['iif_lisp_group']
                if m.groupdict()['lisp_vrf']:
                    sub_dict['incoming_interface_list'][incoming_interface]['lisp_vrf'] = m.groupdict()['lisp_vrf']
                continue

            # Incoming interface:Tunnel5
            m = p3_1.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']

                if incoming_interface.lower() == 'null':
                    continue

                ing_intf_dict = sub_dict.setdefault('incoming_interface_list',{}).setdefault(incoming_interface,{})

                continue
                
            # ##Incoming interface list:
            p3_4 = re.compile(r'^(?P<incoming_interface>\S+)\, +(?P<state>[\w\/-]+)$')
            m = p3_4.match(line)
            if m:
                res = m.groupdict()
                incmg_intf = res['incoming_interface']
                if 'incoming_interface_list' not in sub_dict:
                    sub_dict['incoming_interface_list'] = {}
                sub_dict['incoming_interface_list'][incmg_intf]={}
                sub_dict['incoming_interface_list'][incmg_intf]['state']=res['state']
                continue
                
            # RPF nbr:2001:db8:90:24::6
            m = p3_2.match(line)
            if m:
                rpf_nbr = m.groupdict()['rpf_nbr']
                try:
                    sub_dict['rpf_nbr'] = rpf_nbr
                    ing_intf_dict['rpf_nbr'] = rpf_nbr
                except Exception:
                    sub_dict['rpf_nbr'] = rpf_nbr
                continue

            # Outgoing interface list: Null
            # Outgoing interface list:
            m = p4.match(line)
            if m:
                intf = m.groupdict()['intf']
                if intf:
                    outgoing = False
                else:
                    outgoing = True
                continue

            # 100.11.11.11, 2d22h/00:02:36
            m = p5_1.match(line)
            if m:
                r = m.groupdict()
                lisp_join_sender_addr = r['lisp_js_addr']
                out_intf_dict.setdefault('lisp_join_sender_list',{}).setdefault(lisp_join_sender_addr,{})
                out_intf_dict['lisp_join_sender_list'][lisp_join_sender_addr]['uptime'] = r['lisp_js_uptime']
                out_intf_dict['lisp_join_sender_list'][lisp_join_sender_addr]['expire'] = r['lisp_js_expire']
                continue
            # Vlan5, Forward/Dense, 00:03:25/00:00:00, H
            # Vlan5, Forward/Dense, 00:04:35/00:02:30
            # ATM0/0, VCD 14, Forward/Sparse, 00:03:57/00:02:53
            # POS4/0, Forward, 00:02:06/00:03:27
            # LISP0.4100, (172.24.0.3, 232.0.0.199), Forward/Sparse, 00:10:33/stopped
            # Vlan500, VXLAN v4 Encap: (50000, 225.2.2.2), Forward/Sparse, 00:00:54/00:02:05
            # Vlan500, VXLAN v6 Encap: (50000, FF13::1), Forward/Sparse, 00:17:31/stopped, flags:
            m = p5.match(line)
            if m and outgoing:
                ### adding below code for multiple outgoing interfaces with same different rloc's example below
                #### LISP0.1, 100.154.154.154, Forward/Sparse, 00:00:52/00:02:46, Pkts:2, flags: p
                ####LISP0.1, 100.99.99.99, Forward/Sparse, 00:00:52/00:03:00, Pkts:2, flags: p
                ####LISP0.1, 100.33.33.33, Forward/Sparse, 00:00:52/00:03:20, Pkts:2, flags: p
                ####LISP0.1, 100.22.22.22, Forward/Sparse, 00:00:52/00:03:00, Pkts:2, flags: p

                egress_interface = m.groupdict()['outgoing_interface']
                lisp_mcast_source = m.groupdict()['lisp_mcast_source']
                if egress_interface == previous_intf:
                    idx+=1
                    outgoing_interface='{}-{}'.format(m.groupdict()['outgoing_interface'],idx )
                else:
                    outgoing_interface=egress_interface
                    previous_intf = egress_interface

                out_intf_dict = sub_dict.setdefault('outgoing_interface_list',{}).setdefault(outgoing_interface,{})
                sub_dict['outgoing_interface_list'][outgoing_interface]['uptime'] =  m.groupdict()['uptime']
                sub_dict['outgoing_interface_list'][outgoing_interface]['expire'] = m.groupdict()['expire']
                sub_dict['outgoing_interface_list'][outgoing_interface]['state_mode'] = m.groupdict()['state_mode'].lower()
                if m.groupdict()['flags']:
                    sub_dict['outgoing_interface_list'][outgoing_interface]['flags'] = m.groupdict()['flags']
                if m.groupdict()['pkts']:
                    sub_dict['outgoing_interface_list'][outgoing_interface]['pkts'] = int(m.groupdict()['pkts'])
                if m.groupdict()['vcd']:
                    sub_dict['outgoing_interface_list'][outgoing_interface]['vcd'] = m.groupdict()['vcd']
                if m.groupdict()['lisp_mcast_source']:
                    sub_dict['outgoing_interface_list'][outgoing_interface]['lisp_mcast_source'] = m.groupdict()['lisp_mcast_source']
                if m.groupdict()['lisp_mcast_group']:
                    sub_dict['outgoing_interface_list'][outgoing_interface]['lisp_mcast_group'] = m.groupdict()['lisp_mcast_group']
                if m.groupdict()['vxlan_version']:
                    sub_dict['outgoing_interface_list'][outgoing_interface]['vxlan_version'] = m.groupdict()['vxlan_version']
                    if m.groupdict()['vxlan_vni']:
                        sub_dict['outgoing_interface_list'][outgoing_interface]['vxlan_vni'] = m.groupdict()['vxlan_vni']
                    if m.groupdict()['vxlan_nxthop']:
                        sub_dict['outgoing_interface_list'][outgoing_interface]['vxlan_nxthop'] = m.groupdict()['vxlan_nxthop']   
                continue
                
            # Bidir-Upstream: Lspvif52, RPF nbr: 1.1.1.1
            p6 = re.compile(r'^Bidir-Upstream: +(?P<upstream_interface>[a-zA-Z0-9\/\-\.]+), '
                            '+RPF +nbr\:? +(?P<rpf_nbr>[\w\:\.]+)(, *(?P<status>\w+))?$')
            m = p6.match(line)
            if m:
                r=m.groupdict()
                upstream_interface=r['upstream_interface']
                sub_dict['upstream_interface'] = {}
                sub_dict['upstream_interface'][upstream_interface]={}
                sub_dict['upstream_interface'][upstream_interface]['rpf_nbr']=r['rpf_nbr']
                continue
            # Extranet receivers in vrf internet:
            m = p7.match(line)
            if m:
                r = m.groupdict()
                extranet_vrf = r['extranet_vrf']
                sub_dict.setdefault('extranet_rx_vrf_list',{}).setdefault(extranet_vrf,{})
                continue
            # (192.168.1.3, 232.64.64.1), 21:38:05/00:03:25, OIF count: 1, flags: sTpl
            # (*, 239.5.1.100), 12:54:25/stopped, RP 152.1.1.1, OIF count: 0, flags: SP
            m = p8.match(line)
            if m:
                r = m.groupdict()
                if extranet_vrf:
                    sub_dict['extranet_rx_vrf_list'][extranet_vrf]['e_src'] = r['e_src']
                    sub_dict['extranet_rx_vrf_list'][extranet_vrf]['e_grp'] = r['e_grp']
                    sub_dict['extranet_rx_vrf_list'][extranet_vrf]['e_uptime'] = r['e_uptime']
                    sub_dict['extranet_rx_vrf_list'][extranet_vrf]['e_expire'] = r['e_expire']
                    sub_dict['extranet_rx_vrf_list'][extranet_vrf]['e_oif_count'] = r['e_oif_count']
                    sub_dict['extranet_rx_vrf_list'][extranet_vrf]['e_flags'] = r['e_flags']
                    if r['e_rp']:
                        sub_dict['extranet_rx_vrf_list'][extranet_vrf]['e_rp'] = r['e_rp']
                continue

        return mroute_dict

# ===========================================
# Parser for 'show ipv6 mroute'
# Parser for 'show ipv6 mroute vrf xxx'
# ===========================================
class ShowIpv6Mroute(ShowIpMroute):
    """Parser for:
      show ipv6 mroute
       show ipv6 mroute vrf {vrf}
      show ipv6 mroute {group}
      show ipv6 mroute {group} {source}
      show ipv6 mroute verbose
      show ipv6 mroute {group} verbose
      show ipv6 mroute {group} {source} verbose
      show ipv6 mroute vrf {vrf} {group}
      show ipv6 mroute vrf {vrf} {group} {source}
      show ipv6 mroute vrf {vrf} verbose
      show ipv6 mroute vrf {vrf} {group} verbose
      show ipv6 mroute vrf {vrf} {group} {source} verbose"""

    cli_command = ['show ipv6 mroute',
                   'show ipv6 mroute vrf {vrf}',
                   'show ipv6 mroute {group}',
                   'show ipv6 mroute vrf {vrf} {group} {source}',
                   'show ipv6 mroute vrf {vrf} {group}',
                   'show ipv6 mroute {group} {source}',
                   'show ipv6 mroute {verbose}',
                   'show ipv6 mroute {group} {verbose}',
                   'show ipv6 mroute {group} {source} {verbose}',
                   'show ipv6 mroute vrf {vrf} {verbose}',
                   'show ipv6 mroute vrf {vrf} {group} {verbose}',
                   'show ipv6 mroute vrf {vrf} {group} {source} {verbose}' ]
    exclude = ['expire', 'uptime', 'joins', 'leaves',
               'incoming_interface_list', '(Tunnel.*)']


    def cli(self, vrf='', verbose='', group='', source='', address_family='ipv6', output=None):
        cmd="show ipv6 mroute"
        if output is None:
            if vrf:
                cmd += " vrf {vrf}".format(vrf=vrf)
            else:
                vrf='default'    
            if group:
                cmd += " {group}".format(group=group)
            if source:
                cmd += " {source}".format(source=source)
            if verbose:
                cmd += " {verbose}".format(verbose=verbose)
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(vrf=vrf, address_family='ipv6', output=out)


# ===========================================
# Parser for 'show ip mroute static'
# Parser for 'show ip mroute vrf xxx static'
# ===========================================

class ShowIpMrouteStaticSchema(MetaParser):
    """Schema for:
        show ip mroute static
        show ip mroute vrf <vrf> static
    """
    schema = {'vrf': 
                {Any():
                    {'mroute':
                        {Any():
                            {'path':
                                {Any():
                                    {'neighbor_address': str,
                                     Optional('admin_distance'): str
                                    }
                                },
                            },
                        },
                    },
                },
            }

class ShowIpMrouteStatic(ShowIpMrouteStaticSchema):
    """Parser for:
            show ip mroute static
            show ip mroute vrf <vrf> static
        """
    cli_command = ['show ip mroute static', 'show ip mroute vrf {vrf} static']

    def cli(self, vrf='',output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output


        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # Mroute: 172.16.0.0/16, RPF neighbor: 172.30.10.13, distance: 1
            p1 = re.compile(r'^Mroute: +(?P<mroute>[\w\:\.\/]+),'
                             ' RPF +neighbor: +(?P<rpf_nbr>[\w\.\:]+),'
                             ' distance: +(?P<distance>\d+)$')
                              
            m = p1.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                rpf_nbr = m.groupdict()['rpf_nbr']
                distance = m.groupdict()['distance']

                path = rpf_nbr + ' ' + distance

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                if 'mroute' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['mroute'] = {}
                if mroute not in ret_dict['vrf'][vrf]['mroute']:
                    ret_dict['vrf'][vrf]['mroute'][mroute] = {}

                if 'mroute' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['mroute'] = {}
                if mroute not in ret_dict['vrf'][vrf]['mroute']:
                    ret_dict['vrf'][vrf]['mroute'][mroute] = {}
                    
                if 'path' not in ret_dict['vrf'][vrf]['mroute'][mroute]:
                    ret_dict['vrf'][vrf]['mroute'][mroute]['path'] = {}
                if path not in ret_dict['vrf'][vrf]['mroute'][mroute]['path']:
                    ret_dict['vrf'][vrf]['mroute'][mroute]['path'][path] = {}

                ret_dict['vrf'][vrf]['mroute'][mroute]['path'][path]\
                    ['neighbor_address'] = rpf_nbr

                ret_dict['vrf'][vrf]['mroute'][mroute]['path'][path]\
                    ['admin_distance'] = distance

                continue

        return ret_dict


# ===========================================
# Parser for 'show ip multicast'
# Parser for 'show ip multicast vrf xxx'
# ===========================================

class ShowIpMulticastSchema(MetaParser):
    """Schema for:
        show ip multicast
        show ip multicast vrf <vrf>
    """
    schema = {
        'vrf': {
            Any(): {
                'enable': bool,
                'multipath': bool,
                'route_limit': str,
                'fallback_group_mode': str,
                'multicast_bound_with_filter_autorp': int,
                Optional('mo_frr'): bool,
            },
        },
    }

class ShowIpMulticast(ShowIpMulticastSchema):
    """Parser for:
        show ip multicast
        show ip multicast vrf <vrf>
    """
    cli_command = ['show ip multicast', 'show ip multicast vrf {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Multicast Routing: enabled
            p1 = re.compile(r'^Multicast +Routing: +(?P<status>\w+)$')
                              
            m = p1.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                if 'enabled' in status:
                    ret_dict['vrf'][vrf]['enable'] = True
                else:
                    ret_dict['vrf'][vrf]['enable'] = False
                continue

            # Multicast Multipath: enabled
            p2 = re.compile(r'^Multicast +Multipath: +(?P<status>\w+)$')
                              
            m = p2.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                if 'enabled' in status:
                    ret_dict['vrf'][vrf]['multipath'] = True
                else:
                    ret_dict['vrf'][vrf]['multipath'] = False
                continue

            # Multicast Route limit: No limit
            p3 = re.compile(r'^Multicast +Route +limit: +(?P<status>[\w\s]+)$')
                              
            m = p3.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                ret_dict['vrf'][vrf]['route_limit'] = status
                continue

            # Multicast Fallback group mode: Sparse
            p4 = re.compile(r'^Multicast +Fallback +group +mode: +(?P<mode>[\w\s]+)$')
                              
            m = p4.match(line)
            if m:
                mode = m.groupdict()['mode'].lower()
                ret_dict['vrf'][vrf]['fallback_group_mode'] = mode
                continue

            # Number of multicast boundaries configured with filter-autorp option: 0
            p5 = re.compile(r'^Number +of +multicast +boundaries +configured +'
                             'with +filter\-autorp +option: +(?P<num>\d+)$')
                              
            m = p5.match(line)
            if m:
                num = m.groupdict()['num']
                ret_dict['vrf'][vrf]['multicast_bound_with_filter_autorp'] = int(num)
                continue

            # MoFRR: Disabled
            p2 = re.compile(r'^MoFRR: +(?P<status>\w+)$')
                              
            m = p2.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                if 'enabled' in status:
                    ret_dict['vrf'][vrf]['mo_frr'] = True
                else:
                    ret_dict['vrf'][vrf]['mo_frr'] = False
                continue

        return ret_dict

class ShowIpMulticastMplsvifSchema(MetaParser):
    """Schema for:
        show ip multicast mpls vif
    """
    schema = {
        'interfaces': {
            Any(): {
                'next_hop': str,
                'application': str,
                'ref_count': str,
                'table': int,
                'vrf': str,
                'flags': str,
            },
        },
    }

class ShowIpMulticastMplsvif(ShowIpMulticastMplsvifSchema):
    """Parser for:
        show ip multicast mpls vif
    """
    cli_command = 'show ip multicast mpls vif'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        if not out.strip():
            return ret_dict

        ## Lspvif9     0.0.0.0              MDT               N/A       11   (vrf vrf3001) 0x1
        p1=re.compile(r"(?P<interface>[a-zA-Z0-9]+)\s+(?P<next_hop>\d+\.\d+\.\d+\.\d+)\s+"
                    "(?P<application>\S+)\s+(?P<ref_count>\S+)\s+(?P<table>\S+)\s+[a-zA-Z\(]*\s*"
                    "(?P<vrf>[a-z0-9]+)\)*\s+(?P<flags>\S+)")

        for line in out.splitlines():
            line=line.strip()

            ## Lspvif9     0.0.0.0              MDT               N/A       11   (vrf vrf3001) 0x1
            m=p1.match(line)
            if m:
                r=m.groupdict()
                intf_dict=ret_dict.setdefault('interfaces',{}).setdefault(r["interface"],{})
                r.pop('interface')
                for key,value in r.items():
                    intf_dict.update({key:int(value) if value.isdigit() else value})

        return ret_dict

class ShowIpMrouteCountSchema(MetaParser):
    ''' search for
        show ip mroute count
    '''

    schema = {
        'routes': int,
        'bytes_of_memory': int,
        'groups': int,
        'average': float,
        'group_id': {
            Any(): {
                'source_count': int,
                'pkt_forwarded': int,
                'pkt_received': int
            }
        },
    }


class ShowIpMrouteCount(ShowIpMrouteCountSchema):
    ''' Parser for
        show ip mroute count
    '''

    cli_command = 'show ip mroute count'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 1009 routes using 1103272 bytes of memory
        p1 = re.compile(r'(?P<routes>\d+)\s+routes\s+using\s+(?P<bytes_of_memory>\d+)')

        # 1005 groups, 0.00 average sources per group
        p2 = re.compile(r'(?P<groups>\d+)\s+groups,\s(?P<average>[\d\.]+)\s+average')

        # Group: 232.3.6.233, Source count: 0, Packets forwarded: 0, Packets received: 0
        p3 = re.compile(
            r'Group:\s+(?P<group>[\w.]+),\s+Source\scount:\s(?P<source_count>\d+),\s+Packets\sforwarded:\s(?P<pkt_forwarded>\d+),\s+Packets\sreceived:\s(?P<pkt_received>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # 1009 routes using 1103272 bytes of memory
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'routes': int(group['routes'])})
                ret_dict.update({'bytes_of_memory': int(group['bytes_of_memory'])})
                continue

            # 1005 groups, 0.00 average sources per group
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'groups': int(group['groups'])})
                ret_dict.update({'average': float(group['average'])})
                continue

            # Group: 232.3.6.233, Source count: 0, Packets forwarded: 0, Packets received: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                groupid = group['group']
                if 'group_id' not in ret_dict:
                    group_dict = ret_dict.setdefault('group_id', {})
                group_dict[groupid] = {}
                group_dict[groupid]['source_count'] = int(group['source_count'])
                group_dict[groupid]['pkt_forwarded'] = int(group['pkt_forwarded'])
                group_dict[groupid]['pkt_received'] = int(group['pkt_received'])
                continue

        return ret_dict

#=================================================
# Schema for 'show consistency-checker mcast {layer} start all'
#=================================================

class ShowConsistencyCheckerMcastStartAllSchema(MetaParser):
    """Schema for 
        * 'show consistency-checker mcast {layer} start all'
        * 'show consistency-checker mcast {layer} start {address} {source}',
        * 'show consistency-checker mcast {layer} start {address}',
        * 'show consistency-checker mcast {layer} start vrf {instance_name} {address} {source}',
        * 'show consistency-checker mcast {layer} start vlan {vlan_id} {address}'
    """
    schema = {
        'run_id': int,
        Optional('layer'): str
    }

#=================================================
# Parser for 'show consistency-checker mcast {layer} start all'
#=================================================

class ShowConsistencyCheckerMcastStartAll(ShowConsistencyCheckerMcastStartAllSchema):
    """Parser for 
        * 'show consistency-checker mcast {layer} start all',
        * 'show consistency-checker mcast {layer} start {address} {source}',
        * 'show consistency-checker mcast {layer} start {address}',
        * 'show consistency-checker mcast {layer} start vrf {instance_name} {address} {source}',
        * 'show consistency-checker mcast {layer} start vlan {vlan_id} {address}'
    """

    cli_command = ['show consistency-checker mcast {layer} start all',
    'show consistency-checker mcast {layer} start {address} {source}',
    'show consistency-checker mcast {layer} start {address}',
    'show consistency-checker mcast {layer} start vrf {instance_name} {address} {source}',
    'show consistency-checker mcast {layer} start vlan {vlan_id} {address}'
    ]

    def cli(self, layer, source=None, address=None, instance_name=None, vlan_id=None, output=None):
        if output is None:
            if instance_name and address and source:
                cmd = self.cli_command[3].format(layer=layer, instance_name=instance_name, address=address, source=source)
            elif address and source is None:
                cmd = self.cli_command[2].format(layer=layer, address=address)
            elif vlan_id and address:
                cmd = self.cli_command[4].format(layer=layer, vlan_id=vlan_id, address=address)
            elif address and source:
                cmd = self.cli_command[1].format(layer=layer, address=address, source=source)
            else:
                cmd = self.cli_command[0].format(layer=layer)
            output = self.device.execute(cmd)

        # L3 multicast Full scan started. Run_id: 2181
        p1 = re.compile(r'^(?P<layer>(\w\d+)) multicast +Full +scan +started. Run_id: +(?P<run_id>(\d+))$')

        # Single entry scan started with Run_id: 2255
        p2 = re.compile(r'^Single +entry +scan +started +with +Run_id: +(?P<run_id>(\d+))$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # L3 multicast Full scan started. Run_id: 2181
            m = p1.match(line)
            if m:
                ret_dict['layer'] = m.groupdict()['layer']
                ret_dict['run_id'] = int(m.groupdict()['run_id'])
                continue
            
            # Single entry scan started with Run_id: 2255
            m = p2.match(line)
            if m:
                ret_dict['run_id'] = int(m.groupdict()['run_id'])
                continue

        return ret_dict

#=================================================
# Schema for 'show consistency-checker run-id detail'
#=================================================
class ShowConsistencyCheckerRunIdDetailSchema(MetaParser):
    """Schema for 
        * 'show consistency-checker run-id {id} detail'
    """
    schema = {
        'process': {
            Any(): {
                'type': str,
            }
        },
        'switch': {
            Any(): {
                'process': {
                    Any(): {
                        Optional('process_type'): str
                    }
               }
           }
       }
   }

#=================================================
# Parser for 'show consistency-checker run-id detail'
#=================================================
class ShowConsistencyCheckerRunIdDetail(ShowConsistencyCheckerRunIdDetailSchema):
    """  Parser for 
        * 'show consistency-checker run-id {id} detail'
    """

    cli_command = 'show consistency-checker run-id {id} detail'
    
    def cli(self, id, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(id=id))
        # Process: IOSD
        # Process: FMAN-RP
        p1 = re.compile(r'^Process:\s+(?P<type>[\w\s\-]+)$')
        # Switch: 1 Process: FMAN-FP
        # Switch: 1 Process: FED
        p2 = re.compile(r'^Switch:\s+(?P<switch>[\d]+)+\s+Process:\s+(?P<process_type>[\w\s\-]+)$')
        
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # Process: IOSD
            # Process: FMAN-RP
            m = p1.match(line)
            if m:
                ret_dict.setdefault('process', {}).setdefault(m.groupdict()['type'], {}).setdefault('type', m.groupdict()['type'])
                continue

            # Switch: 1 Process: FMAN-FP
            # Switch: 1 Process: FED
            m = p2.match(line)
            if m: 
                key_chain_dict = ret_dict.setdefault('switch', {}).setdefault(m.groupdict()['switch'], {})
                key_dict = key_chain_dict.setdefault('process', {}).setdefault(m.groupdict()['process_type'], {})
                key_dict['process_type'] = m.groupdict()['process_type']
                continue

        return ret_dict

#=================================================
# Schema for 'show consistency-checker run-id'
#=================================================
class ShowConsistencyCheckerRunIdSchema(MetaParser):
        schema = {
        'process': {
            Any(): {
                'object_type': {
                    Any():{
                            'starttime':str,
                            Optional('entries'):int ,
                            Optional('exceptions'):int,
                            Optional('fulltable'):str,
                            Optional('garbagedetector'):str,
                            Optional('hwcheck'):str,
                            Optional('hwshadow'):str,
                            Optional('state'):str,
                            Optional('actual'):int,
                            Optional('inherited'):int,
                            Optional('missing'):int,
                            Optional('stale'):int,
                            Optional('others'):int,
                            Optional('hardware'):int,
                    },
                },
            },
        },
        Optional('switch'): {
            Any(): {
                'process': {
                    Any(): {
                        'object_type': {
                            Any():{
                                    'starttime':str,
                                    'state':str,
                                    'actual':int,
                                    'inherited':int,
                                    'missing':int,
                                    'stale':int,
                                    'others':int,
                                    Optional('hardware'):int
                                },
                            },
                        },
                    },
                },
            },
        }
        
#==================================================
# Parser for 'show consistency-checker run-id'
#==================================================
class ShowConsistencyCheckerRunId(ShowConsistencyCheckerRunIdSchema):
    cli_command = 'show consistency-checker run-id {id}'

    def cli(self, id, output=None):
        if output is None:
            cmd = self.cli_command.format(id=id)
            output = self.device.execute(cmd)

        # Process: IOSD
        # Process: FMAN-RP
        p1 = re.compile(r'^Process:\s+(?P<type>[\w\s\-]+)$')

        # Object-Type    Start-time                Entries  Exceptions  Flags
        #  l2m_vlan      2023/04/28 03:51:03         72         0       F GD Hw HS
        #  l2m_group     2023/04/28 03:51:03          0         0       F GD Hw HS
        p2 = re.compile(r'^(?P<object_type>[\w\s\_]+)\s+(?P<starttime>(\d+\/){2}\d+.\d+:\d+:\d+)\s+(?P<entries>[\d]+)\s+(?P<exceptions>[\d]+)\s+\b(?P<fulltable>F)?\b\s+\b(?P<garbagedetector>GD)?\b\s+\b(?P<hwcheck>Hw)?\b\s+\b(?P<hwshadow>HS)?\b$')

        # Object-Type       Start-time                State           A/  I/  M/  S/Oth 
        #  l2m_vlan       2023/04/28 03:51:03      Consistent        0/  0/  0/  0/  0
        #  l2m_group      2023/04/28 03:51:03       Consistent        0/  0/  0/  0/  0
        p3 = re.compile(r'^(?P<object_type>[\w\s\-]+)\s+(?P<starttime>(\d+\/){2}\d+.\d+:\d+:\d+)\s+(?P<state>[\w]+)\s+(?P<actual>[\d]+)/\s+(?P<inherited>[\d]+)/\s+(?P<missing>[\d]+)/\s+(?P<stale>[\d]+)/\s+(?P<others>[\d]+)$')

        # Switch: 1 Process: FMAN-FP
        # Switch: 1 Process: FED
        p4 = re.compile(r'^Switch:\s+(?P<switch>[\d]+)+\s+Process:\s+(?P<process_type>[\w\s\-]+)$')

        # Object-Type    Start-time              State              A/  I/  M/  S/ HW/Oth
        # l2m_vlan       2023/05/08 05:05:36     Consistent         0/  0/  0/  0/  0/  0
        # l2m_group      2023/05/08 05:05:36     Consistent         0/  0/  0/  0/  0/  0
        p5 = re.compile(r'^(?P<object_type>[\w\s\-]+)\s+(?P<starttime>(\d+\/){2}\d+.\d+:\d+:\d+)\s+(?P<state>[\w]+)\s+(?P<actual>[\d]+)/\s+(?P<inherited>[\d]+)/\s+(?P<missing>[\d]+)/\s+(?P<stale>[\d]+)/\s+(?P<hardware>[\d]+)/\s+(?P<others>[\d]+)$')

        # l3m_entry      2023/11/03 12:37:18        1012         0    F Hw HS
        p6 = re.compile(r'^(?P<object_type>[\w\s\_]+)\s+(?P<starttime>(\d+\/){2}\d+.\d+:\d+:\d+)\s+(?P<entries>[\d]+)\s+(?P<exceptions>[\d]+)\s+\b(?P<fulltable>F+)?\b\s+\b(?P<hwcheck>Hw)?\b\s+\b(?P<hwshadow>HS)?\b$')
        
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Process: IOSD
            # Process: FMAN-RP
            m = p1.match(line)
            if m:
                process_dict = ret_dict.setdefault('process', {}).setdefault(m.groupdict()['type'], {})
                continue

            # Object-Type    Start-time                Entries  Exceptions  Flags
            #  l2m_vlan      2023/04/28 03:51:03         72         0       F GD Hw HS
            #  l2m_group     2023/04/28 03:51:03          0         0       F GD Hw HS
            m=p2.match(line)
            if m:
                object_type=m.groupdict()['object_type'].strip()
                object_dict= process_dict.setdefault('object_type', {}).setdefault(object_type, {})
                object_dict['starttime']=m.groupdict()['starttime']
                object_dict['entries']=int(m.groupdict()['entries'])
                object_dict['exceptions']=int(m.groupdict()['exceptions'])
                object_dict['fulltable']=m.groupdict()['fulltable']
                object_dict['garbagedetector']=m.groupdict()['garbagedetector']
                object_dict['hwcheck']=m.groupdict()['hwcheck']
                object_dict['hwshadow']=m.groupdict()['hwshadow']
                continue

            # Object-Type       Start-time                State           A/  I/  M/  S/Oth 
            #  l2m_vlan        2023/04/28 03:51:03      Consistent        0/  0/  0/  0/  0
            #  l2m_group      2023/04/28 03:51:03       Consistent        0/  0/  0/  0/  0 
            m=p3.match(line)
            if m:
                object_type=m.groupdict()['object_type'].strip()
                object_dict= process_dict.setdefault('object_type', {}).setdefault(object_type, {})
                object_dict['starttime']=m.groupdict()['starttime']
                object_dict['state']=m.groupdict()['state']
                object_dict['actual']=int(m.groupdict()['actual'])
                object_dict['inherited']=int(m.groupdict()['inherited'])
                object_dict['missing']=int(m.groupdict()['missing'])
                object_dict['stale']=int(m.groupdict()['stale'])
                object_dict['others']=int(m.groupdict()['others'])
                continue 
            
            # Switch: 1 Process: FMAN-FP
            # Switch: 1 Process: FED
            m = p4.match(line)
            flag = 0
            if m:
                consistency_checker = m.groupdict()['switch']
                key_chain_dict = ret_dict.setdefault('switch', {}).setdefault(consistency_checker, {})
                key_name = m.groupdict()['process_type']
                process_dict = key_chain_dict.setdefault('process', {}).setdefault(key_name, {})
                flag = 1
                continue

            # Object-Type    Start-time              State              A/  I/  M/  S/ HW/Oth
            # l2m_vlan       2023/05/08 05:05:36     Consistent         0/  0/  0/  0/  0/  0
            # l2m_group      2023/05/08 05:05:36     Consistent         0/  0/  0/  0/  0/  0
            m = p5.match(line)
            if m:
                if flag == 1:
                    object_type=m.groupdict()['object_type'].strip()
                    object_dict1= process_dict.setdefault('object_type', {}).setdefault(object_type, {})
                    object_dict1['starttime']=m.groupdict()['starttime']
                    object_dict1['state']=m.groupdict()['state']
                    object_dict1['actual']=int(m.groupdict()['actual'])
                    object_dict1['inherited']=int(m.groupdict()['inherited'])
                    object_dict1['missing']=int(m.groupdict()['missing'])
                    object_dict1['stale']=int(m.groupdict()['stale'])
                    object_dict1['others']=int(m.groupdict()['others'])
                    object_dict1['hardware']=int(m.groupdict()['hardware'])
                    continue
                else:
                    object_type=m.groupdict()['object_type'].strip()
                    object_dict= process_dict.setdefault('object_type', {}).setdefault(object_type, {})
                    object_dict['starttime']=m.groupdict()['starttime']
                    object_dict['state']=m.groupdict()['state']
                    object_dict['actual']=int(m.groupdict()['actual'])
                    object_dict['inherited']=int(m.groupdict()['inherited'])
                    object_dict['missing']=int(m.groupdict()['missing'])
                    object_dict['stale']=int(m.groupdict()['stale'])
                    object_dict['others']=int(m.groupdict()['others'])
                    object_dict['hardware']=int(m.groupdict()['hardware'])
                    continue
            
            m=p6.match(line)
            if m:
                object_type=m.groupdict()['object_type'].strip()
                object_dict= process_dict.setdefault('object_type', {}).setdefault(object_type, {})
                object_dict['starttime']=m.groupdict()['starttime']
                object_dict['entries']=int(m.groupdict()['entries'])
                object_dict['exceptions']=int(m.groupdict()['exceptions'])
                object_dict['fulltable']=m.groupdict()['fulltable']
                object_dict['hwcheck']=m.groupdict()['hwcheck']
                object_dict['hwshadow']=m.groupdict()['hwshadow']
                continue
                    
        return ret_dict
    