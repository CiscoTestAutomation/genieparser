''' show_run.py

IOSXE parsers for the following show commands:
    * 'show run policy-map {name}'
    * 'show running-config interface {interface}'
        * 'show running-config all | sec {interface}'
        * 'show running-config mdns-sd' 

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, ListOf, \
                                               Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common

# =================================================
# Schema for:
#   * 'show run policy-map {name}'
# ==================================================
class ShowRunPolicyMapSchema(MetaParser):
    
    schema = {
        'policy_map': {
            Any(): {
                'class': {
                    Any(): {
                        Optional('qos_set'): {
                            Optional('ip precedence'): str,
                            Optional('precedence'): str,
                            Optional('dscp'): str,
                            Optional('cos'): str,
                            Optional('qos-group'): str,
                        },
                        Optional('police'): {
                            Optional('cir_bps'): str,
                            Optional('pir_bps'): str,
                            Optional('cir_bc_bytes'): str,
                            Optional('cir_be_bytes'): str,
                            Optional('conformed'): str,
                            Optional('exceeded'): str,
                        },
                        Optional('bandwidth_percent'): str,
                        Optional('priority_percent'): str,
                        Optional('priority_level'): str,
                        Optional('target_shape_rate'): str,
                        Optional('service_policy'): str,
                        Optional('service_policy_input'): str,
                        Optional('service_policy_output'): str,
                    },
                }
            },
        }
    }


# ===================================
# Parser for:
#   * 'show run policy-map {name}'
# ===================================
class ShowRunPolicyMap(ShowRunPolicyMapSchema):

    ''' Parser for
        * "show run policy-map {name}"
    '''

    cli_command = ['show run policy-map {name}']

    def cli(self, name, output=None):
        if output is None:
            cmd = self.cli_command[0].format(name=name)
            # Execute command on device
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        config_dict = {}

        # police cir 400000 conform-action transmit  exceed-action drop
        # police cir 100000 pir  70000 conform-action transmit  exceed-action drop
        # police cir 8000000 bc 4000 be 1000 conform-action transmit  exceed-action transmit  violate-action drop
        p1 = re.compile(r'^police +cir +(?P<cir_bps>(\d+))( +pir +(?P<pir_bps>(\d+)))?'
            '( +bc +(?P<cir_bc_bytes>(\d+)))?( +be +(?P<cir_be_bytes>(\d+)))?'
            ' +conform-action +(?P<conformed>(\w+)) +exceed-action +(?P<exceeded>(\w+))'
            '( +violate-action +(?P<violated>(\w+)))?$')

        # policy-map L3VPN-out_child
        p1_1 = re.compile(r'^policy-map +(?P<policy_map>([\w\-\_]+))$')

        # class ARP_in
        p1_2 = re.compile(r'^class +(?P<class_name>([\w\-\_]+))$')

        # shape average 10000000
        # shape average 80000 320 0
        p2 = re.compile(r'^shape +average +(?P<target_shape_rate>(\d+))$')

        # set ip precedence 4
        p3_1 = re.compile(r'^set +ip +precedence +(?P<ip_precedence>(\w+))$')

        # set precedence 5
        p3_2 = re.compile(r'^set +precedence +(?P<precedence>(\w+))$')

        # set qos-group 4
        p4 = re.compile(r'^set +qos-group +(?P<qos_group>(\w+))$')

        # bandwidth percent 25
        p5 = re.compile(r'^bandwidth percent +(?P<bandwidth_percent>(\d+))$')

        # priority level 2
        p6_1 = re.compile(r'^priority +level +(?P<priority_level>(\d+))$')

        # priority percent 20
        p6_2 = re.compile(r'^priority +percent +(?P<priority_percent>(\d+))$')

        # service-policy input L3VPN-0_in
        p7 = re.compile(r'^service-policy( +(?P<direction>(\w+)))? +(?P<service_policy>([\w\-\_]+))$')

        # set dscp ef
        # set dscp 46
        p8 = re.compile(r'^set +dscp +(?P<dscp>(\w+))$')

        # set cos 0
        p9 = re.compile(r'^set +cos +(?P<cos>(\d+))$')

        for line in out.splitlines():

            line = line.strip()

            # policy-map L3VPN-out_child
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                policy_map = m.groupdict()['policy_map']
                config_dict.setdefault('policy_map', {})
                config_dict['policy_map'].setdefault(policy_map, {})
                continue

            # class ARP_in
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                class_name = m.groupdict()['class_name']
                if 'class' not in config_dict['policy_map']:
                    config_dict['policy_map'][policy_map]\
                        .setdefault('class', {})
                config_dict['policy_map'][policy_map]['class']\
                    .setdefault(class_name, {})
                continue

            # police cir 400000 conform-action transmit  exceed-action drop
            # police cir 100000 pir  70000 conform-action transmit  exceed-action drop
            # police cir 8000000 bc 4000 be 1000 conform-action transmit  exceed-action transmit  violate-action drop
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if 'police' not in \
                    config_dict['policy_map'][policy_map]['class'][class_name]:
                    config_dict['policy_map'][policy_map]['class'][class_name]\
                        .setdefault('police', {})
                config_dict['policy_map'][policy_map]['class'][class_name]\
                    ['police'].update({k: v for k, v in group.items() if v})
                continue

            # shape average 10000000
            # shape average 80000 320 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                config_dict['policy_map'][policy_map]['class'][class_name]\
                    .update({k: v for k, v in group.items() if v})
                continue

            # set ip precedence 4
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                if 'qos_set' not in \
                    config_dict['policy_map'][policy_map]['class'][class_name]:
                    config_dict['policy_map'][policy_map]['class'][class_name]\
                        .setdefault('qos_set', {})
                config_dict['policy_map'][policy_map]['class'][class_name]\
                    ['qos_set'].update(
                        {k.replace('_', ' '): v for k, v in group.items() if v})
                continue

            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                if 'qos_set' not in \
                    config_dict['policy_map'][policy_map]['class'][class_name]:
                    config_dict['policy_map'][policy_map]['class'][class_name]\
                        .setdefault('qos_set', {})
                config_dict['policy_map'][policy_map]['class'][class_name]\
                    ['qos_set'].update(
                        {k: v for k, v in group.items() if v})
                continue

            # set qos-group 4
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if 'qos_set' not in \
                    config_dict['policy_map'][policy_map]['class'][class_name]:
                    config_dict['policy_map'][policy_map]['class'][class_name]\
                        .setdefault('qos_set', {})
                config_dict['policy_map'][policy_map]['class'][class_name]\
                    ['qos_set'].update(
                        {k.replace('_', '-'): v for k, v in group.items() if v})
                continue

            # bandwidth percent 25
            m = p5.match(line)
            if m:
                group = m.groupdict()
                config_dict['policy_map'][policy_map]['class'][class_name]\
                    .update({k: v for k, v in group.items() if v})
                continue

            # priority level 2
            m = p6_1.match(line)
            if m:
                group = m.groupdict()
                config_dict['policy_map'][policy_map]['class'][class_name]\
                    .update({k: v for k, v in group.items() if v})
                continue

            # priority percent 20
            m = p6_2.match(line)
            if m:
                group = m.groupdict()
                config_dict['policy_map'][policy_map]['class'][class_name]\
                    .update({k: v for k, v in group.items() if v})
                continue

            # service-policy input L3VPN-0_in
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if m.groupdict()['direction']:
                    if m.groupdict()['direction'] == 'input':
                        config_dict['policy_map'][policy_map]['class']\
                            [class_name]['service_policy_input'] = \
                                m.groupdict()['service_policy']
                    else:
                        config_dict['policy_map'][policy_map]['class']\
                            [class_name]['service_policy_output'] = \
                                m.groupdict()['service_policy']
                else:
                    config_dict['policy_map'][policy_map]['class'][class_name]\
                        ['service_policy'] = m.groupdict()['service_policy']
                continue

            # set dscp ef
            # set dscp 46
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if 'qos_set' not in config_dict['policy_map'][policy_map]\
                    ['class'][class_name]:
                    config_dict['policy_map'][policy_map]['class'][class_name]\
                        .setdefault('qos_set', {})
                config_dict['policy_map'][policy_map]['class'][class_name]\
                    ['qos_set'].update(
                        {k: v for k, v in group.items() if v})
                continue

            # set cos 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if 'qos_set' not in config_dict['policy_map'][policy_map]\
                    ['class'][class_name]:
                    config_dict['policy_map'][policy_map]['class'][class_name]\
                        .setdefault('qos_set', {})
                config_dict['policy_map'][policy_map]['class'][class_name]\
                    ['qos_set'].update(
                        {k: v for k, v in group.items() if v})
                continue

        return config_dict


# ==================================================
# Schema for:
#   * show running-config interface {interface}
# ==================================================
class ShowRunInterfaceSchema(MetaParser):

    schema = {
        'interfaces': {
            Any(): {
                Optional('authentication_control_direction'): str,
                Optional('authentication_event_fail_action'): str,
                Optional('authentication_fallback'): str,
                Optional('authentication_host_mode'): str,
                Optional('authentication_order'): str,
                Optional('authentication_periodic'): bool,
                Optional('authentication_port_control'): str,
                Optional('authentication_priority'): str,
                Optional('authentication_timer_inactivity'): str,
                Optional('authentication_timer_reauthenticate_server'): bool,
                Optional('authentication_violation'): str,
                Optional('trust_device'): str,
                Optional('carrier_delay'): list,
                Optional('shutdown'): bool,
                Optional('encapsulation_dot1q'): str,
                Optional('description'): str,
                Optional('dot1x_pae_authenticator'): bool,
                Optional('dot1x_timeout_quiet_period'): str,
                Optional('dot1x_timeout_server_timeout'): str,
                Optional('dot1x_timeout_tx_period'): str,
                Optional('ip_arp_inspection_limit_rate'): str,
                Optional('ip_dhcp_snooping_limit_rate'): str,
                Optional('ip_ospf'): {
                    Any(): {
                        'area': str,
                    },
                },
                Optional('ipv4'): {
                    'ip': str,
                    'netmask': str,
                },
                Optional('ipv6'): list,
                Optional('ipv6_ospf'): {
                    Any(): {
                        'area': str,
                    },
                },
                Optional('ipv6_enable'): bool,
                Optional('ipv6_destination_guard_attach_policy'): str,
                Optional('ipv6_source_guard_attach_policy'): str,
                Optional('ipv6_ospfv3'): {
                    Any(): {
                        'area': str,
                    },
                },
                Optional('acl'): {
                    Optional('inbound'): {
                        'acl_name': str,
                        'direction': str,
                    },
                    Optional('outbound'): {
                        'acl_name': str,
                        'direction': str,
                    }
                },
                Optional('load_interval'): str,
                Optional('mab'): bool,
                Optional('negotiation_auto'): bool,
                Optional('snmp_trap_link_status'): bool,
                Optional('snmp_trap_mac_notification_change_added'): bool,
                Optional('snmp_trap_mac_notification_change_removed'): bool,
                Optional('spanning_tree_bpduguard'): str,
                Optional('spanning_tree_portfast'): bool,
                Optional('spanning_tree_portfast_trunk'): bool,
                Optional('spanning_tree_bpdufilter'): str,
                Optional('switchport_access_vlan'): str,
                Optional('switchport_trunk_vlans'): str,
                Optional('keepalive'): bool,
                Optional('switchport_mode'): str,
                Optional('input_policy'): str,
                Optional('output_policy'): str,
                Optional('switchport_nonegotiate'): str,
                Optional('vrf'): str,
                Optional('src_ip'): str,
                Optional('tunnel_mode'): str,
                Optional('tunnel_dst'):str,
                Optional('autoroute_announce'):str,
                Optional('autoroute_destination'):str,
                Optional('tunnel_priority'):list,
                Optional('tunnel_bandwidth'):int,
                Optional('tunnel_path_option'):{
                    Any():{
                        Optional('path_type'):str,
                        Optional('path_name'):str,
                    },
                },
                Optional('mpls_ip'):str,
                Optional('channel_group'): {
                        'chg': int,
                        'mode': str,
                },
                Optional('power_inline'): {
                        Optional('state'): str,
                        Optional('max_watts'): str,
                },
                Optional('power_inline_port_priority'): str,
                Optional('flow_monitor_input'): str,
                Optional('switchport_protected'): bool,
                Optional('switchport_block_unicast'): bool,
                Optional('switchport_block_multicast'): bool,
                Optional('ip_dhcp_snooping_trust'): bool,
                Optional('ip_arp_inspection_trust'): bool,
                Optional('lisp_mobility'): str,
                Optional('mac_address_sticky'):str,
                Optional('source_template'):str,
                Optional('host_reachability_protocol'): str,
                Optional('source_interface'): str,
                Optional('member_vni'): {
                    Any():
                         {Optional('vrf'): str,
                          Optional('ingress_replication'): {
                              'enabled': bool,
                              Optional('remote_peer_ip'): str,
                          },
                          Optional('mcast_group'): str,
                          Optional('local_routing'): bool
                          }
                     },
            }
        }
    }


# ==================================================
# Parser for:
#   * show running-config interface {interface}
#   * show running-config | section ^interface
# ==================================================
class ShowRunInterface(ShowRunInterfaceSchema):

    ''' Parser for
         show running-config interface {interface},
         show running-config | section ^interface
    '''

    cli_command = ['show running-config interface {interface}',
                   'show running-config | section ^interface']

    def cli(self, interface=None, output=None):

        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]

            # Execute command on device
            output = self.device.execute(cmd)

        # Init vars
        config_dict = {}

        # interface GigabitEthernet0
        p1 = re.compile(r'^interface +(?P<interface>[\S]+)$')

        # description "Boot lan interface"
        # description ISE Controlled Port
        p2 = re.compile(r'^description +(?P<description>[\S\s]+)$')

        # vrf forwarding Mgmt-intf
        # ip vrf forwarding oam
        p3 = re.compile(r'^(ip )?vrf +forwarding +(?P<vrf>[\S\s]+)$')

        # ip address 10.1.21.249 255.255.255.0
        p4 = re.compile(r'^ip +address +(?P<ip>[\S]+) +(?P<netmask>[\S]+)$')

        # ipv6 address 2001:db8:4:1::1/64
        # ipv6 address 2001:db8:400:1::2/112
        p5 = re.compile(r'^ipv6 address +(?P<ipv6>.+)$')

        # shutdown
        p6 = re.compile(r'^(?P<shutdown>shutdown)$')

        # encapsulation dot1Q 201
        p7 = re.compile(r'^encapsulation +dot1Q +(?P<dot1q>[\d]+)$')

        # carrier-delay up 60
        # carrier-delay down 60
        p8 = re.compile(r'^carrier-delay +(?P<carrier_delay>.+)$')

        # negotiation auto
        # no negotiation auto
        p9 = re.compile(r'^(?P<negotiation>no +)?negotiation +auto$')

        # cdp enable
        p10 = re.compile(r'^cdp +(?P<cdp>enable)$')

        # no keepalive
        p11 = re.compile(r'^(?P<keepalive>no +)?keepalive$')

        # switchport access vlan 70
        p12 = re.compile(r'^switchport +access +vlan +(?P<vlan>[\d]+)$')

        # switchport mode access
        p13 = re.compile(r'^switchport +mode +(?P<switchport_mode>[\S\s]+)$')

        # switchport nonegotiate
        p14 = re.compile(r'^switchport +(?P<nonegotiate>nonegotiate)$')

        # ip arp inspection limit rate 1024
        p15 = re.compile(r'^ip +arp +inspection +limit +rate +(?P<rate>[\d]+)$')

        # load-interval 30
        p16 = re.compile(r'^load-interval +(?P<load_interval>\d+)$')

        # authentication control-direction in
        p17 = re.compile(r'^authentication +control-direction +(?P<direction>\w+)$')

        # authentication event fail action next-method
        p18 = re.compile(r'^authentication +event +fail +action +(?P<action>[\S\s]+)$')

        # authentication host-mode multi-auth
        p19 = re.compile(r'^authentication +host-mode +(?P<host_mode>[\S\s]+)$')

        # authentication order dot1x mab
        p20 = re.compile(r'^authentication +order +(?P<order>[\S\s]+)$')

        # authentication priority dot1x mab
        p21 = re.compile(r'^authentication +priority +(?P<priority>[\S\s]+)$')

        # authentication port-control auto
        p22 = re.compile(r'^authentication +port-control +(?P<port_control>[\S\s]+)$')

        # authentication periodic
        p23 = re.compile(r'^(?P<periodic>authentication periodic)$')

        # authentication timer reauthenticate server
        p24 = re.compile(r'^(?P<reauth>authentication +timer +reauthenticate +server)$')

        # authentication timer inactivity 65535
        p24_1 = re.compile(r'^authentication +timer +inactivity +(?P<inactivity>\d+)$')

        # authentication violation restrict
        p25 = re.compile(r'^authentication +violation +(?P<violation>[\S\s]+)$')

        # authentication fallback dot1x
        p26 = re.compile(r'^authentication +fallback +(?P<fallback>[\S\s]+)$')

        # mab
        p27 = re.compile(r'^(?P<mab>mab)$')

        # snmp trap mac-notification change added
        p28 = re.compile(r'^snmp +trap +mac-notification +change +added$')

        # snmp trap mac-notification change removed
        p29 = re.compile(r'^snmp +trap +mac-notification +change +removed$')

        # no snmp trap link-status
        p30 = re.compile(r'^no +snmp +trap +link-status$')

        # dot1x pae authenticator
        p31 = re.compile(r'^dot1x +pae +authenticator$')

        # dot1x timeout quiet-period 5
        p32 = re.compile(r'^dot1x +timeout +quiet-period +(?P<quiet_period>\d+)$')

        # dot1x timeout server-timeout 10
        p33 = re.compile(r'^dot1x +timeout +server-timeout +(?P<server_timeout>\d+)$')

        # dot1x timeout tx-period 5
        p34 = re.compile(r'^dot1x +timeout +tx-period +(?P<tx_period>\d+)$')

        # spanning-tree portfast
        p35 = re.compile(r'^spanning-tree +portfast$')

        # spanning-tree bpduguard enable
        p36 = re.compile(r'^spanning-tree +bpduguard +(?P<bpduguard>[\S\s]+)$')

        # ip dhcp snooping limit rate 100
        p37 = re.compile(r'^ip +dhcp +snooping +limit +rate +(?P<rate>[\d]+)$')

        # ipv6 enable
        p38 = re.compile(r'^ipv6 enable$')

        # ip ospf 2 area 0
        # ipv6 ospf 1 area 0
        p39 = re.compile(r'^(?P<ip>ip|ipv6) +ospf +(?P<ospf>\d+) +area +(?P<area>[\d]+)$')

        # ospfv3 1 ipv6 area 0
        p40 = re.compile(r'^ospfv3 +(?P<rate>[\d]+) +ipv6 +area +(?P<area>[\d]+)$')

        # channel-group 1 mode active
        p41 = re.compile(r'^channel-group +(?P<group>[\d]+) +mode +(?P<mode>[\w]+)$')

        # power inline port priority high
        p42 = re.compile(r'^power +inline +port +priority +(?P<power_priority>[\w]+)$')

        # power inline static max 20000
        p43 = re.compile(r'^power +inline +(?P<state>never|static)( +max +(?P<max_watts>[\d]+))?$')

        # spanning-tree bpdufilter enable
        p44 = re.compile(r'^spanning-tree +bpdufilter +(?P<bpdufilter>[\S\s]+)$')

        # ip flow monitor IPv4NETFLOW input
        p45 = re.compile(r'^ip +flow +monitor +(?P<flow_monitor_input>[\w]+) +input$')

        # switchport protected
        p46 = re.compile(r'^switchport +protected$')

        # switchport block unicast
        p47 = re.compile(r'^switchport +block +unicast$')

        # switchport block multicast
        p48 = re.compile(r'^switchport +block +multicast$')

        # switchport trunk allowed vlan 820,900-905
        p49 = re.compile(r'^switchport +trunk +allowed +vlan (?P<vlans>[\S\s]+)$')

        # ip dhcp snooping trust
        p50 = re.compile(r'^ip +dhcp +snooping +trust$')

        # ip arp inspection trust
        p51 = re.compile(r'^ip +arp +inspection +trust$')

        #ip unnumbered Loopback0
        p52 = re.compile(r'^ip unnumbered (?P<src_address>\S+)$')

        # tunnel mode mpls traffic-eng
        p53 = re.compile(r"^tunnel mode (?P<tunnel_mode>[a-zA-Z\- ]+)$")

        # tunnel destination 2.2.2.2
        p54 = re.compile(r"^tunnel destination (?P<tunnel_dst>\S+)$")

        # tunnel mpls traffic-eng priority 7 7
        p55 = re.compile(r"^tunnel mpls traffic-eng priority (?P<value>[a-zA-Z0-9 ]+)$")

        # tunnel mpls traffic-eng bandwidth 500
        p56 = re.compile(r"^tunnel mpls traffic-eng bandwidth (?P<value>[0-9 ]+)$")

        # tunnel mpls traffic-eng path-option 1 dynamic
        p57 = re.compile(r"^tunnel mpls traffic-eng path-option (?P<value>[0-9]+)\s*(?:explicit name)? +(?P<path_type>\S+)$")

        # mpls ip
        p58 = re.compile(r"^mpls ip$")

        # service-policy input AutoQos-4.0-CiscoPhone-Input-Policy
        p59 = re.compile(r'^service-policy\s+input\s+(?P<input_policy>\S+)$')

        # service-policy output AutoQos-4.0-Output-Policy
        p60 = re.compile(r'^service-policy\s+output\s+(?P<output_policy>\S+)$')

        # switchport port-security mac-address sticky 1020.4bb1.6f2f
        p61 = re.compile(r"^switchport port-security mac-address sticky (?P<value>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})$")

        # source template USER_NoAuth
        p62 = re.compile(r"^source template (?P<template>\w+)$")

        # host-reachability protocol bgp
        p63 = re.compile(r'^host-reachability protocol (?P<protocol>[a-zA-Z]+)$')

        # source-interface loopback1
        p64 = re.compile(r'^source-interface (?P<src_intf>[a-zA-Z0-9\-]+)$')

        # member vni 20011 ingress-replication
        p65 = re.compile(r'^member vni (?P<vni>[0-9]+) ingress-replication$')

        # member vni 20012 mcast-group 224.1.1.1
        p66 = re.compile(r'^member vni (?P<vni>[0-9]+) mcast-group (?P<ip>[0-9\.]+)$')

        # member vni 20011 ingress-replication local-routing
        p67 = re.compile(r'^member vni (?P<vni>[0-9]+) ingress-replication '
                         r'local-routing$')

        # member vni 20011
        p68 = re.compile(r'^member vni (?P<vni>[0-9]+)$')

        # ingress-replication 1.1.1.1
        p69 = re.compile(r'^ingress-replication (?P<ip>[0-9\.]+)$')

        # member vni 20012 mcast-group 224.1.1.1 local-routing
        p70 = re.compile(r'^member vni (?P<vni>[0-9]+) mcast-group (?P<ip>[0-9\.]+) '
                         r'local-routing$')

        # member vni 30000 vrf red
        p71 = re.compile(r'^member vni (?P<vni>[0-9]+) vrf (?P<vrf>[a-zA-Z\-]+)$')

        # ip access-group DELETE_ME in ; ip access-group TEST-OUT out
        p72 = re.compile(r'^ip access-group (?P<acl_name>[\w\-.#<>]+) (?P<direction>\w+)$')

        # lisp mobility 20_1_1_0-global-IPV4
        p73 = re.compile(r'^\s*lisp mobility +(?P<lisp_mobility>[\w-]+)$')

        #trust device cisco-phone / trust device ip-camera
        p74 = re.compile(r'^trust\sdevice\s(?P<trust_device>\S+)$')

        #ipv6 destination-guard attach-policy Univ-v6-IPDG-Policy1
        p75 = re.compile(r'^ipv6\sdestination-guard\sattach-policy\s(?P<ipv6_destination_guard_attach_policy>\S+)$')

        #ipv6 source-guard attach-policy Univ-v6-IPSG-Policy2
        p76 = re.compile(r'^ipv6\ssource-guard\sattach-policy\s(?P<ipv6_source_guard_attach_policy>\S+)$')

        # spanning-tree portfast trunk
        p77 = re.compile(r"^spanning-tree +portfast +trunk$")

        for line in output.splitlines():
            line = line.strip()

            # interface GigabitEthernet0
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                intf_dict = config_dict.setdefault('interfaces', {})\
                                       .setdefault(interface, {})
                continue
            
            # description ISE Controlled Port
            m = p2.match(line)
            if m:
                description = m.groupdict()['description']
                intf_dict.update({'description': description})
                continue
            
            # vrf forwarding Mgmt-intf
            m = p3.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                intf_dict.update({'vrf': vrf})
                continue

            # # ip address 10.1.21.249 255.255.255.0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ipv4':{
                                    'ip': group['ip'],
                                    'netmask': group['netmask']},
                                })
                continue

            # ipv6 address 2001:db8:4:1::1/64
            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf_dict.setdefault('ipv6', []).append(group['ipv6'])
                continue

            # shutdown
            m = p6.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'shutdown': True})
                continue

            # encapsulation dot1Q 201
            m = p7.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'encapsulation_dot1q': group['dot1q']})
                continue

            # carrier-delay up 60
            # carrier-delay down 60
            m = p8.match(line)
            if m:
                group = m.groupdict()
                intf_dict.setdefault('carrier_delay', [])\
                         .append(group['carrier_delay'])
                continue

            # negotiation auto
            # no negotiation auto
            m = p9.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'negotiation_auto': group['negotiation'] is None})
                continue

            # cdp enable
            m = p10.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'cdp': group['cdp']})
                continue

            # no keepalive
            m = p11.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'keepalive': group['keepalive'] is None})
                continue

            # switchport access vlan 70
            m = p12.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_access_vlan': group['vlan']})
                continue

            # switchport mode access
            m = p13.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_mode': group['switchport_mode']})
                continue
            
            # switchport nonegotiate
            m = p14.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'switchport_nonegotiate': group['nonegotiate']})
                continue
            
            # ip arp inspection limit rate 1024
            m = p15.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'ip_arp_inspection_limit_rate': group['rate']})
                continue

            # load-interval 30
            m = p16.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'load_interval': group['load_interval']})
                continue
            
            # authentication control-direction
            m = p17.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'authentication_control_direction': group['direction']})
                continue

            # authentication event fail action next-method
            m = p18.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'authentication_event_fail_action': group['action']})
                continue

            # authentication host-mode multi-auth
            m = p19.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'authentication_host_mode': group['host_mode']})
                continue

            # authentication order dot1x mab
            m = p20.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'authentication_order': group['order']})
                continue

            # authentication priority dot1x mab
            m = p21.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'authentication_priority': group['priority']})
                continue

            # authentication port-control auto
            m = p22.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'authentication_port_control': group['port_control']})
                continue

            # authentication periodic
            m = p23.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'authentication_periodic': True})
                continue

            # authentication timer reauthenticate server
            m = p24.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'authentication_timer_reauthenticate_server': True})
                continue

            # authentication timer inactivity 65535
            m = p24_1.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'authentication_timer_inactivity': group['inactivity']})
                continue

            # authentication violation restrict
            m = p25.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'authentication_violation': group['violation']})
                continue

            # authentication fallback dot1x
            m = p26.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'authentication_fallback': group['fallback']})
                continue

            # mab
            m = p27.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'mab': True})
                continue

            # snmp trap mac-notification change added
            m = p28.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'snmp_trap_mac_notification_change_added': True})
                continue

            # snmp trap mac-notification change removed
            m = p29.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'snmp_trap_mac_notification_change_removed': True})
                continue

            # no snmp trap link-status
            m = p30.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'snmp_trap_link_status': False})
                continue

            # dot1x pae authenticator
            m = p31.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'dot1x_pae_authenticator': True})
                continue

            # dot1x timeout quiet-period 5
            m = p32.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'dot1x_timeout_quiet_period': group['quiet_period']})
                continue

            # dot1x timeout server-timeout 10
            m = p33.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'dot1x_timeout_server_timeout': group['server_timeout']})
                continue

            # dot1x timeout tx-period 5
            m = p34.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'dot1x_timeout_tx_period': group['tx_period']})
                continue

            # spanning-tree portfast
            m = p35.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'spanning_tree_portfast': True})
                continue

            # spanning-tree bpduguard enable
            m = p36.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'spanning_tree_bpduguard': group['bpduguard']})
                continue

            # ip dhcp snooping limit rate 100
            m = p37.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ip_dhcp_snooping_limit_rate': group['rate']})
                continue

            # ipv6 enable
            m = p38.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ipv6_enable': True})
                continue

            # ip ospf 2 area 0
            # ipv6 ospf 1 area 0
            m = p39.match(line)
            if m:
                group = m.groupdict()
                ip = group['ip']
                ospf = group['ospf']
                area = group['area']
                intf_dict.setdefault('{}_ospf'.format(ip), {})\
                         .setdefault(ospf, {}).update({'area': area})
                continue

            # ospfv3 1 ipv6 area 0
            p40 = re.compile(r'^ospfv3 +(?P<ospfv3>[\d]+) +(?P<ip>ip|ipv6) +area +(?P<area>[\d]+)$')
            m = p40.match(line)
            if m:
                group = m.groupdict()
                ip = group['ip']
                ospf = group['ospfv3']
                area = group['area']
                intf_dict.setdefault('{}_ospfv3'.format(ip), {})\
                         .setdefault(ospf, {}).update({'area': area})
                continue

            # channel-group 1 mode active
            m = p41.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'channel_group': {
                                    'chg': int(group['group']),
                                    'mode': group['mode']},
                                })
                continue

            # power inline port priority high
            m = p42.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'power_inline_port_priority': group['power_priority']})

            # power inline never|static
            m = p43.match(line)
            if m:
                group = m.groupdict()
                if group['max_watts']:
                    intf_dict.update({'power_inline': {
                                    'state': group['state'],
                                    'max_watts': group['max_watts']},
                                    })
                else:
                    intf_dict.update({'power_inline': {
                                    'state': group['state']},
                                    })
                continue
            
            # spanning-tree bpdufilter enable
            m = p44.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'spanning_tree_bpdufilter': group['bpdufilter']})
                continue

            # ip flow monitor IPv4NETFLOW input
            m = p45.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update(
                    {'flow_monitor_input': group['flow_monitor_input']})
                continue

            # switchport protected
            m = p46.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_protected': True})
                continue

            # switchport block unicast
            m = p47.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_block_unicast': True})
                continue

            # switchport block multicast
            m = p48.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_block_multicast': True})
                continue

            # switchport trunk allowed vlan 820,900-905
            m = p49.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_trunk_vlans': group['vlans']})
                continue

            # ip dhcp snooping trust
            m = p50.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ip_dhcp_snooping_trust': True})
                continue

            # ip arp inspection trust
            m = p51.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ip_arp_inspection_trust': True})
                continue

            # ip unnumbered Loopback0
            m = p52.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'src_ip':group['src_address']})
                continue
                
            # tunnel mode mpls traffic-eng
            m = p53.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'tunnel_mode':group['tunnel_mode']})
                continue
            
            #tunnel destination 2.2.2.2
            m = p54.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'tunnel_dst':group['tunnel_dst']})
                continue
                
            if "autoroute announce" in line:
                intf_dict.update({'autoroute_announce':'enabled'}) 
            if "autoroute destination" in line:
                intf_dict.update({'autoroute_destination':'enabled'}) 

                
            #tunnel destination 2.2.2.2
            m = p55.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'tunnel_priority':[group['value']]})
                continue
                
            #tunnel mpls traffic-eng bandwidth 500
            m = p56.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'tunnel_bandwidth':int(group['value'])})
                continue
  
            # tunnel mpls traffic-eng path-option 1 dynamic
            m =p57.match(line)
            if m:
                group=m.groupdict()
                sub_dict=intf_dict.setdefault("tunnel_path_option",{})\
                                  .setdefault(group['value'],{})
                if group['path_type'] == "dynamic":
                    sub_dict.update({'path_type':group['path_type']})
                else:
                    sub_dict.update({'path_type':'explicit'})
                    sub_dict.update({'path_name':group['path_type']}) 
                continue    

            # mpls ip
            m = p58.match(line)
            if m:
                intf_dict.update({'mpls_ip':'enabled'})
                continue

            # service-policy input AutoQos-4.0-CiscoPhone-Input-Policy
            m = p59.match(line)
            if m:
                group = m.groupdict()
                input_policy = group['input_policy']
                intf_dict.update({'input_policy': group['input_policy']})
                continue

            # service-policy output AutoQos-4.0-Output-Policy
            m = p60.match(line)
            if m:
                group = m.groupdict()
                output_policy = group['output_policy']
                intf_dict.update({'output_policy': group['output_policy']})

            # switchport port-security mac-address sticky 1020.4bb1.6f2f
            m = p61.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'mac_address_sticky':group['value']})
                continue

            # source template USER_NoAuth
            m = p62.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'source_template':group['template']})
                continue

            # host-reachability protocol bgp
            m = p63.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'host_reachability_protocol': group['protocol']})
                continue

            # source-interface loopback1
            m = p64.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'source_interface': group['src_intf']})
                continue

            # member vni 20011 ingress-replication
            m = p65.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'ingress_replication': {
                                                    'enabled': True}}})
                continue

            # member vni 20012 mcast-group 224.1.1.1
            m = p66.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'mcast_group': group['ip']}})
                continue

            # member vni 20011 ingress-replication local-routing
            m = p67.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'ingress_replication': {
                                                    'enabled': True
                                                  },
                                                  'local_routing': True}})
                continue

            # member vni 20011
            m = p68.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                vni = group['vni']
                continue

            # ingress-replication 1.1.1.1
            m = p69.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({vni: {'ingress_replication': {
                                            'enabled': True,
                                            'remote_peer_ip': group['ip']}}})
                continue

            # member vni 20012 mcast-group 224.1.1.1 local-routing
            m = p70.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'mcast_group': group['ip'],
                                                  'local_routing': True}})
                continue

            # member vni 30000 vrf red
            m = p71.match(line)
            if m:
                member_vni = intf_dict.setdefault('member_vni', {})
                group = m.groupdict()
                member_vni.update({group['vni']: {'vrf': group['vrf']}})
                continue

            # ip access-group DELETE_ME in ; ip access-group TEST-OUT out
            m = p72.match(line)
            if m:
                intf_dict['acl'] = {}
                group = m.groupdict()
                if group['direction'] == 'in':
                    inbound_dict = {'inbound': {
                        'acl_name': group['acl_name'],
                        'direction': group['direction']},
                    }
                    continue

                elif group['direction'] == 'out':
                    outbound_dict = {'outbound': {
                        'acl_name': group['acl_name'],
                        'direction': group['direction']},
                    }

                intf_dict['acl'].update(inbound_dict)
                intf_dict['acl'].update(outbound_dict)

            # lisp mobility 20_1_1_0-global-IPV4
            m = p73.match(line)
            if m:
                lisp_mobility = m.groupdict()['lisp_mobility']
                intf_dict.update({'lisp_mobility': lisp_mobility})
                continue

            #trust device cisco-phone / trust device ip-camera
            m = p74.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'trust_device': group['trust_device']})
                continue

            #ipv6 destination-guard attach-policy Univ-v6-IPDG-Policy1
            m = p75.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ipv6_destination_guard_attach_policy': group['ipv6_destination_guard_attach_policy']})
                continue

            #ipv6 source-guard attach-policy Univ-v6-IPSG-Policy2
            m = p76.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ipv6_source_guard_attach_policy': group['ipv6_source_guard_attach_policy']})
                continue

            # spanning-tree portfast trunk
            m = p77.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'spanning_tree_portfast_trunk': True})
                continue

        return config_dict


# =================
# Schema for:
#  * 'show running-config mdns-sd'
# =================
class ShowRunMdnsSdSchema(MetaParser):
    """Schema for show running-config mdns-sd"""

    schema = {
        'mdns_gateway': {
            'mode': str,
            Optional('act_qry_timer'): int,
            Optional('rate_limit'): int,
            Optional('srvc_mdns_qry'): str,
            Optional('cache_mem_max'): int,
            Optional('srvc_enu_prd'): int,
            Optional('air_prnt_hlp'): str,
            Optional('any_qry'): str,
            Optional('cach_sync_timer'): int,
            Optional('act_res_timer'): int,
            Optional('src_intf'): str,
            Optional('agent_ip'): str,
        },
        Optional('mdns_loc_filter'): {
            Optional('loc_filter_names'): {
                Any(): {
                    Optional('loc_fil_name'): str,
                    Optional('loc_grps'): {
                        Any(): {
                            Optional('loc_grp'): str,
                            Optional('vlan_no'): ListOf(str),
                            Optional('role'): ListOf(str),
                        },
                    },
                },
            },
        },
        Optional('mdns_srvc_def'): {
            Optional('srvc_def_names'): {
                Any(): {
                    Optional('srvc_def_name'): str,
                    Optional('srvc_type'): ListOf(str),
                },
            },
        },
        'mdns_srvc_list': {
            Optional('srvc_list_names'): {
                Any(): {
                    Optional('srvc_list_name'): str,
                    Optional('fil_dir'): str,
                    Optional('srvc_list_1'): ListOf(str),
                    Optional('mat_srvc_lists'): {
                        Any(): {
                            Optional('srvc_list'): str,
                            Optional('service_types'): str
                        },
                    },
                },
            },
        },
        Optional('mdns_srvc_pol'): {
            Optional('srvc_pol_names'): {
                Any(): {
                    Optional('srvc_poli_name'): str,
                    Optional('policy_srvc_lists'): {
                        Any(): {
                            Optional('poli_srvc_list'): str,
                            Optional('bound_dir'): str,
                        },
                    },
                },
            },
        },
        Optional('mdns_location_grps'): {
            Optional('loc_grp_names'): {
                Any(): {
                    Optional('loc_grp_name'): str,
                    Optional('vl_no'): ListOf(str),
                    Optional('intf'): ListOf(str),
                },
            },
        },
    }


# ==============
# Parser for:
#  * 'show running-config mdns-sd'
# =================
class ShowRunMdnsSd(ShowRunMdnsSdSchema):
    '''Parser for show running-config mdns-sd'''

    cli_command = 'show running-config mdns-sd'

    def cli(self, output=None):

        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        out_dict = {}

        # mdns-sd gateway
        p0 = re.compile(r"^mdns-sd +gateway$")

        # mode service-peer
        p1 = re.compile(r"^mode +(?P<mode>[\w-]+)$")

        # active-query timer 10
        p2 = re.compile(r"^active-query +timer +(?P<act_qry_timer>(\d)+)$")

        # rate-limit 10
        p3 = re.compile(r"^rate-limit +(?P<rate_limit>[\d]+)$")

        # service-mdns-query all
        p4 = re.compile(r"^service-mdns-query +(?P<srvc_mdns_qry>[\w]+)$")

        # cache-memory-max 10
        p5 = re.compile(r"^cache-memory-max +(?P<cache_mem_max>[\d]+)$")

        # service-type-enumeration period 15
        p6 = re.compile(r"^service-type-enumeration +period +(?P<srvc_enu_prd>[\d]+)$")

        # air-print-helper enable
        p7 = re.compile(r"^air-print-helper +(?P<air_prnt_hlp>[\w]+)$")

        # any-query forward
        p8 = re.compile(r"^any-query +(?P<any_qry>[\w]+)$")

        # cache-sync timer 15
        p9 = re.compile(r"^cache-sync timer +(?P<cach_sync_timer>(\d)+)$")

        # active-response timer 10
        p10 = re.compile(r"^active-response +timer +(?P<act_res_timer>[\d]+)$")

        # mdns-sd location-filter filter1
        p11 = re.compile(r"^mdns-sd +location-filter +(?P<loc_fil_name>[\d\w-]+)$")

        # match location-group all vlan 1101 role none
        p12 = re.compile(r"^match +location-group +(?P<loc_grp>\d+|\S+) +vlan +(?P<vlan_no>[\d]+) +role +(?P<role>[\w]+)$")

        # mdns-sd service-definition custom1
        p13 = re.compile(r"^mdns-sd +service-definition +(?P<srvc_def_name>[\d\w]+)$")

        # service-type _airplay._tcp.local
        p14 = re.compile(r"^service-type +(?P<srvc_type>[\w.-]+)$")

        # mdns-sd service-list policie4 OUT
        p15 = re.compile(r"^mdns-sd +service-list +(?P<srvc_list_name>[\d\w]+) +(?P<fil_dir>(IN|OUT))$")

        # match custom1
        p16 = re.compile(r"^match +(?P<srvc_list_1>[\d\w-]+)$")

        # match custom1 message-type query
        p17 = re.compile(r"^match +(?P<srvc_list>[\d\w-]+) +message-type +(?P<service_types>(announcement|any|query))$")

        # mdns-sd service-policy policy2
        p18 = re.compile(r"^mdns-sd +service-policy +(?P<srvc_poli_name>[\d\w]+)$")

        # service-list policie3 IN
        p19 = re.compile(r"^service-list +(?P<poli_srvc_list>[\d\w-]+) +(?P<bound_dir>(IN|OUT))$")

        # mdns-sd location-group 4096 vlan 1101
        p20 = re.compile(r"^mdns-sd +location-group +(?P<loc_grp_name>\d+|\S+) +vlan +(?P<vl_no>[\d]+)$")

        # interface Gi5/0/15
        p21 = re.compile(r"^interface +(?P<intf>[\w\/]+)$")

        # source-interface Vlan4030
        p22 = re.compile(r"^source-interface +Vlan(?P<src_intf>[\d]+)$")
                
        # sdg-agent 4000:1:30::1
        # sdg-agent 40.1.21.1
        p23 = re.compile(r"^sdg-agent +(?P<agent_ip>([\d:.]+))$")
        
        for line in out.splitlines():
            line = line.strip()
            
            # mdns-sd gateway
            m = p0.match(line)
            if m:
                ret_dict = out_dict.setdefault('mdns_gateway', {})
                continue

            # mode service-peer
            m = p1.match(line)
            if m:
                ret_dict['mode'] = m.groupdict()['mode']
                continue

            # active-query timer 10
            m = p2.match(line)
            if m:
                ret_dict['act_qry_timer'] = int(m.groupdict()['act_qry_timer'])
                continue

            # rate-limit 10
            m = p3.match(line)
            if m:
                ret_dict['rate_limit'] = int(m.groupdict()['rate_limit'])
                continue

            # service-mdns-query all
            m = p4.match(line)
            if m:
                ret_dict['srvc_mdns_qry'] = m.groupdict()['srvc_mdns_qry']
                continue

            # cache-memory-max 10
            m = p5.match(line)
            if m:
                ret_dict['cache_mem_max'] = int(m.groupdict()['cache_mem_max'])
                continue

            # service-type-enumeration period 15
            m = p6.match(line)
            if m:
                ret_dict['srvc_enu_prd'] = int(m.groupdict()['srvc_enu_prd'])
                continue

            # air-print-helper enable
            m = p7.match(line)
            if m:
                ret_dict['air_prnt_hlp'] = m.groupdict()['air_prnt_hlp']
                continue

            # any-query forward
            m = p8.match(line)
            if m:
                ret_dict['any_qry'] = m.groupdict()['any_qry']
                continue

            # cache-sync timer 15
            m = p9.match(line)
            if m:
                ret_dict['cach_sync_timer'] = \
                    int(m.groupdict()['cach_sync_timer'])
                continue

            # active-response timer 10
            m = p10.match(line)
            if m:
                ret_dict['act_res_timer'] = int(m.groupdict()['act_res_timer'])
                continue

            # mdns-sd location-filter filter1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                fil_dict = out_dict.setdefault('mdns_loc_filter', {})
                loc_filter_names = fil_dict.setdefault('loc_filter_names', {})
                loc_fil_name = \
                    loc_filter_names.setdefault(group['loc_fil_name'], {})
                continue

            # match location-group all vlan 1101 role none
            m = p12.match(line)
            if m:
                group = m.groupdict()
                loc_grps = loc_fil_name.setdefault('loc_grps',{})
                loc_grp = loc_grps.setdefault(group['loc_grp'], {})
                vlan_no = \
                    loc_grp.setdefault('vlan_no', []).append(group['vlan_no'])
                role = loc_grp.setdefault('role', []).append(group['role'])
                continue

            # mdns-sd service-definition custom1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                srvc_def_dict = out_dict.setdefault('mdns_srvc_def', {})
                srvc_def_names = srvc_def_dict.setdefault('srvc_def_names', {})
                srvc_def_name = \
                    srvc_def_names.setdefault(group['srvc_def_name'], {})
                continue

            # service-type _airplay._tcp.local
            m = p14.match(line)
            if m:
                group = m.groupdict()
                srvc_def_name.setdefault('srvc_type', [])\
                             .append(group['srvc_type'])
                continue

            # mdns-sd service-list policie4 OUT
            m = p15.match(line)
            if m:
                group = m.groupdict()
                srvc_list_dict = out_dict.setdefault('mdns_srvc_list', {})
                srvc_list_names = \
                    srvc_list_dict.setdefault('srvc_list_names', {})
                srvc_list_name = \
                    srvc_list_names.setdefault(group['srvc_list_name'], {})
                srvc_list_name.update({
                    'fil_dir': m.groupdict()['fil_dir'],
                })
                continue

            # match custom1
            m = p16.match(line)
            if m:
                group = m.groupdict()
                srvc_list_name.setdefault('srvc_list_1', [])\
                              .append(group['srvc_list_1'])
                continue

            # match custom1 message-type query
            m = p17.match(line)
            if m:
                group = m.groupdict()
                mat_srvc_lists = srvc_list_name.setdefault('mat_srvc_lists',{})
                srvc_list = mat_srvc_lists.setdefault(group['srvc_list'], {})
                srvc_list.update({
                    'service_types': m.groupdict()['service_types'],
                })
                continue

            # mdns-sd service-policy policy2
            m = p18.match(line)
            if m:
                group = m.groupdict()
                policy_dict = out_dict.setdefault('mdns_srvc_pol', {})
                policy_names = policy_dict.setdefault('srvc_pol_names', {})
                srvc_poli_name = \
                    policy_names.setdefault(group['srvc_poli_name'], {})
                continue

            # service-list policie3 IN
            m = p19.match(line)
            if m:
                group = m.groupdict()
                policy_srvc_lists = \
                    srvc_poli_name.setdefault('policy_srvc_lists',{})
                poli_srvc_list = \
                    policy_srvc_lists.setdefault(group['poli_srvc_list'], {})
                poli_srvc_list.update({
                    'bound_dir': m.groupdict()['bound_dir'],
                })
                continue

            # mdns-sd location-group 4096 vlan 1101
            m = p20.match(line)
            if m:
                group = m.groupdict()
                loc_dict = out_dict.setdefault('mdns_location_grps', {})
                loc_grps_names = loc_dict.setdefault('loc_grp_names', {})
                loc_grp_name = \
                    loc_grps_names.setdefault(group['loc_grp_name'], {})
                vl_no = loc_grp_name.setdefault('vl_no', [])\
                                    .append(group['vl_no'])
                continue

            # interface Gi5/0/15
            m = p21.match(line)
            if m:
                group = m.groupdict()
                loc_grp_name.setdefault('intf', [])\
                            .append(Common.convert_intf_name(group['intf']))
                continue
            
            # source-interface Vlan4030
            m = p22.match(line)
            if m:
                ret_dict['src_intf'] = m.groupdict()['src_intf']
                continue
                
            # sdg-agent 4000:1:30::1
            m = p23.match(line)
            if m:
                ret_dict['agent_ip'] = m.groupdict()['agent_ip']
                continue
      
        return out_dict

# ==================================================
# Schema for:
#   * show running-config all | sec {interface}
# ==================================================
class ShowRunAllSectionInterfaceSchema(MetaParser):

    schema = {
        'interfaces': {
            Any(): {
                Optional('mvrp_timer_leave_all'): int,
                Optional('mvrp_timer_leave'): int,
                Optional('mvrp_timer_join'): int,
                Optional('mvrp_timer_periodic'): bool,
                Optional('mvrp'):bool,
                Optional('logging_event_link_status'): bool,
                Optional('logging_event_trunk_status'):bool,
                Optional('authentication_periodic'): bool,
                Optional('authentication_port_control'): str,
                Optional('authentication_timer_reauthenticate_server'): bool,
                Optional('authentication_linksec_policy'):bool,
                Optional('access_session_control_direction'):str,
                Optional('access_session_host_mode'): str,
                Optional('access_session_closed'): bool,
                Optional('carrier_delay'): int,
                Optional('shutdown'): bool,
                Optional('medium_p2p'): bool,
                Optional('ip_access_group'):str,
                Optional('ip_arp_inspection_limit_rate'): str,
                Optional('load_interval'): int,
                Optional('negotiation_auto'): bool,
                Optional('macsec_replay_protection'): bool,
                Optional('cdp_log_mismatch_duplex'): bool,
                Optional('cdp_tlv_location'): bool,
                Optional('cdp_tlv_server_location'): bool,
                Optional('cdp_tlv_app'): bool,
                Optional('ipv6_mld_snooping_tcn_flood'): bool,
                Optional('switchport'):bool,
                Optional('switchport_access_vlan'): str,
                Optional('switchport_trunk_allowed_all'):bool,
                Optional('switchport_mode'): str,
                Optional('switchport_nonegotiate'): bool,
                Optional('switchport_autostate_exclude'):bool,
                Optional('switchport_protected'): bool,
                Optional('switchport_block_unicast'): bool,
                Optional('switchport_block_multicast'): bool,
                Optional('switchport_vepa_enabled'):bool,
                Optional('ip_arp_inspection_trust'): bool,
            }
        }
    }


# ==================================================
# Parser for:
#   * show running-config all | sec {interface}
# ==================================================
class ShowRunAllSectionInterface(ShowRunAllSectionInterfaceSchema):

    ''' Parser for
        * show running-config all | sec {interface}
    '''

    cli_command = 'show running-config all | sec {interface}'

    def cli(self, interface, output=None):

        if output is None:
            # Execute command on device
            output = self.device.execute(self.cli_command.format(interface=interface))

        # Init vars
        config_dict = {}

        # interface GigabitEthernet0
        p1 = re.compile(r'^interface +(?P<interface>[\S]+)$')

        # mvrp timer leave-all 1000
        p2 = re.compile(r'^mvrp +timer +leave-all +(?P<timeout>[\d]+)$')

        #  mvrp timer leave 60
        p3 = re.compile(r'^mvrp +timer +leave +(?P<timeout>[\d]+)$')

        # mvrp timer join 20
        p4 = re.compile(r'^mvrp +timer +join +(?P<timeout>[\d]+)$')

        # no mvrp timer periodic
        p5 = re.compile(r'^no +mvrp +timer +periodic$')

        # no mvrp
        p6 = re.compile(r'^no +mvrp$')

        # switchport
        p7 = re.compile(r'^switchport$')

        # no shutdown
        p8 = re.compile(r'^no +(?P<shutdown>shutdown)$')

        # carrier-delay 2
        p9 = re.compile(r'^carrier-delay +(?P<carrier_delay>[\S\s]+)$')

        # switchport access vlan 70
        p10 = re.compile(r'^switchport +access +vlan +(?P<vlan>[\d]+)$')

        # switchport mode access
        p11 = re.compile(r'^switchport +mode +(?P<switchport_mode>[\S\s]+)$')

        # no switchport nonegotiate
        p12 = re.compile(r'^no +switchport +(?P<nonegotiate>nonegotiate)$')

        # ip arp inspection limit rate 1024
        p13 = re.compile(r'^ip +arp +inspection +limit +rate +(?P<rate>[\d]+)$')

        # load-interval 30
        p14 = re.compile(r'^load-interval +(?P<load_interval>\d+)$')

        # access-session control-direction in
        p15 = re.compile(r'^access-session +control-direction +(?P<direction>\w+)$')

        # access-session host-mode multi-auth
        p16 = re.compile(r'^access-session +host-mode +(?P<host_mode>[\S\s]+)$')

        # authentication port-control auto
        p17 = re.compile(r'^authentication +port-control +(?P<port_control>[\S\s]+)$')

        # authentication periodic
        p18 = re.compile(r'^(?P<periodic>authentication periodic)$')

        # authentication timer reauthenticate server
        p19 = re.compile(r'^(?P<reauth>authentication +timer +reauthenticate +server)$')

        # no switchport protected
        p20 = re.compile(r'^no +switchport +protected$')

        # no switchport block unicast
        p21 = re.compile(r'^no +switchport +block +unicast$')

        # no switchport block multicast
        p22 = re.compile(r'^no +switchport +block +multicast$')

        # switchport trunk allowed vlan all
        p23 = re.compile(r'^switchport +trunk +allowed +vlan +all$')

        # no switchport autostate exclude
        p24 = re.compile(r'^no +switchport +autostate +exclude$')

        # no ip arp inspection trust
        p25 = re.compile(r'^no +ip +arp +inspection +trust$')

        # no switchport vepa enabled
        p26 = re.compile(r'^no +switchport +vepa +enabled$')

        #  ip access-group DEFAULT-ACCESS in
        p27 = re.compile(r'^ip +access-group +(?P<group_name>[\w]+) +in$')

        # logging event link-status
        p28 = re.compile(r'^logging +event +link-status$')

        #  logging event trunk-status
        p29 = re.compile(r'^logging +event +trunk-status$')

        # no medium p2p
        p30 = re.compile(r'^no +medium +p2p$')

        # no macsec replay-protection
        p31 = re.compile(r'^no +macsec +replay-protection$')

        # cdp log mismatch duplex
        p32 = re.compile(r'^cdp +log +mismatch +duplex$')

        # cdp tlv location
        p33 = re.compile(r'^cdp +tlv +location$')

        # cdp tlv server-location
        p34 = re.compile(r'^cdp +tlv +server-location$')

        # cdp tlv app
        p35 = re.compile(r'^cdp +tlv +app$')

        # ipv6 mld snooping tcn flood
        p36 = re.compile(r'^ipv6 +mld +snooping +tcn +flood$')

        # authentication linksec policy
        p37 = re.compile(r'^authentication +linksec +policy$')

        # no access-session closed
        p38 = re.compile(r'^no +access-session +closed$')

        for line in output.splitlines():
            line = line.strip()

            # interface GigabitEthernet0
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                intf_dict = config_dict.setdefault('interfaces', {}).setdefault(interface, {})
                continue

            # mvrp timer leave-all 1000
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'mvrp_timer_leave_all': int(group['timeout'])})
                continue

            #  mvrp timer leave 60
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'mvrp_timer_leave': int(group['timeout'])})
                continue

            # mvrp timer join 20
            m = p4.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'mvrp_timer_join': int(group['timeout'])})
                continue

            # no mvrp timer periodic
            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'mvrp_timer_periodic': False})
                continue

            # no mvrp
            m = p6.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'mvrp': False})
                continue

            # switchport
            m = p7.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport': True})
                continue

            # no shutdown
            m = p8.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'shutdown': False})
                continue

            # carrier-delay 2
            m = p9.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'carrier_delay': int(group['carrier_delay'])})
                continue

            # switchport access vlan 70
            m = p10.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_access_vlan': group['vlan']})
                continue

            # switchport mode access
            m = p11.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_mode': group['switchport_mode']})
                continue

            # no switchport nonegotiate
            m = p12.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_nonegotiate': group['nonegotiate'] is None})
                continue

            # ip arp inspection limit rate 1024
            m = p13.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ip_arp_inspection_limit_rate': group['rate']})
                continue

            # load-interval 30
            m = p14.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'load_interval': int(group['load_interval'])})
                continue

            # access-session control-direction
            m = p15.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'access_session_control_direction': group['direction']})
                continue

            # access-session host-mode multi-auth
            m = p16.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'access_session_host_mode': group['host_mode']})
                continue

            # authentication port-control auto
            m = p17.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'authentication_port_control': group['port_control']})
                continue

            # authentication periodic
            m = p18.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'authentication_periodic': True})
                continue

            # authentication timer reauthenticate server
            m = p19.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'authentication_timer_reauthenticate_server': True})
                continue

            # switchport protected
            m = p20.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_protected': False})
                continue

            # switchport block unicast
            m = p21.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_block_unicast': False})
                continue

            # switchport block multicast
            m = p22.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_block_multicast': False})
                continue

            # switchport trunk allowed vlan all
            m = p23.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_trunk_allowed_all': True})
                continue

            # no switchport autostate exclude
            m = p24.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_autostate_exclude': False})
                continue

            # no ip arp inspection trust
            m = p25.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ip_arp_inspection_trust': False})
                continue

            # no switchport vepa enabled
            m = p26.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'switchport_vepa_enabled': False})
                continue

            #  ip access-group DEFAULT-ACCESS in
            m = p27.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ip_access_group': group['group_name']})
                continue

            # logging event link-status
            m = p28.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'logging_event_link_status': True})
                continue

            #  logging event trunk-status
            m = p29.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'logging_event_trunk_status': True})
                continue

            # no medium p2p
            m = p30.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'medium_p2p': False})
                continue

            # no macsec replay-protection
            m = p31.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'macsec_replay_protection': False})
                continue

            # cdp log mismatch duplex
            m = p32.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'cdp_log_mismatch_duplex': True})
                continue

            # cdp tlv location
            m = p33.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'cdp_tlv_location': True})
                continue

            # cdp tlv server-location
            m = p34.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'cdp_tlv_server_location': True})
                continue

            # cdp tlv app
            m = p35.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'cdp_tlv_app': True})
                continue

            # ipv6 mld snooping tcn flood
            m = p36.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'ipv6_mld_snooping_tcn_flood': True})
                continue

            # authentication linksec policy
            m = p37.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'authentication_linksec_policy': True})
                continue

            # no access-session closed
            m = p38.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'access_session_closed': False})
                continue

        return config_dict


# ==================================================
# Schema for:
# 	* show running-config aaa user-name
#   * show running-config aaa username
# ==================================================
class ShowRunningConfigAAAUsernameSchema(MetaParser):
    schema = {
        'username': {
            Any(): {
                Optional('creation_time'): int,
                Optional('password'): {
                    Optional('type'): int,
                    Optional('password'): str,
                },
                Optional('privilege'): int,
                Optional('common_criteria_policy'): str,
                Optional('view'): str,
                Optional('type'): str,
                Optional('onetime'): bool,
                Optional('secret'): {
                    Optional('type'): int,
                    Optional('secret'): str,
                },
            },
        },
    }


# ==================================================
# Schema for:
#   * show running-config aaa user-name
# ==================================================
class ShowRunningAAAUserName(ShowRunningConfigAAAUsernameSchema):
    """Parser for:
        * 'show running-config aaa user-name'
    """
    cli_command = 'show running-config aaa user-name'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # user-name testuser
        p1 = re.compile(r'^user-name +(?P<username>.*)$')

        # creation-time 1628765288
        p2 = re.compile(r'^creation-time +(?P<creation_time>\d+)$')

        # privilege 15
        p3 = re.compile(r'^privilege +(?P<privilege>\d+)$')

        # common-criteria-policy Test-CC
        p4 = re.compile(r'^common-criteria-policy +(?P<common_criteria_policy>.*)$')

        # view test
        p5 = re.compile(r'^view +(?P<view>.*)$')

        # password 0 P@ssw0rd
        p6 = re.compile(r'^password +(?P<type>\d) +(?P<password>.*)$')

        # type lobby-admin
        p7 = re.compile(r'^type +(?P<type>lobby-admin|default|mgmt-user)$')

        # secret 9 $9$giSG8jar6eJuV.$9Q83x2F4M8cs6UjRqCHSDo6/hrRlHzY5z0IFQOV3lZM
        p8 = re.compile(r'^secret +(?P<type>\d) +(?P<secret>.*)$')

        # one-time
        p9 = re.compile(r'^one-time$')

        # Initial return dictionary
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # user-name testuser
            m = p1.match(line)
            if m:
                group = m.groupdict()
                username = group['username']
                users_dict = ret_dict.setdefault('username', {}).setdefault(username, {})
                continue

            # creation-time 1628765288
            m = p2.match(line)
            if m:
                group = m.groupdict()
                users_dict['creation_time'] = int(group['creation_time'])
                continue

            # privilege 15
            m = p3.match(line)
            if m:
                group = m.groupdict()
                users_dict['privilege'] = int(group['privilege'])
                continue

            # common-criteria-policy Test-CC
            m = p4.match(line)
            if m:
                group = m.groupdict()
                users_dict['common_criteria_policy'] = group['common_criteria_policy']
                continue

            # view test
            m = p5.match(line)
            if m:
                group = m.groupdict()
                users_dict['view'] = group['view']
                continue

            # password 0 P@ssw0rd
            m = p6.match(line)
            if m:
                group = m.groupdict()
                pass_dict = users_dict.setdefault('password', {})
                pass_dict['type'] = int(group['type'])
                pass_dict['password'] = group['password']
                continue

            # type lobby-admin
            m = p7.match(line)
            if m:
                group = m.groupdict()
                users_dict['type'] = group['type']
                continue

            # secret 9 $9$giSG8jar6eJuV.$9Q83x2F4M8cs6UjRqCHSDo6/hrRlHzY5z0IFQOV3lZM
            m = p8.match(line)
            if m:
                group = m.groupdict()
                pass_dict = users_dict.setdefault('secret', {})
                pass_dict['type'] = int(group['type'])
                pass_dict['secret'] = group['secret']
                continue

            # one-time
            m = p9.match(line)
            if m:
                users_dict['onetime'] = True
                continue

        return ret_dict


# ==================================================
# Schema for:
#   * show running-config aaa username
# ==================================================
class ShowRunningConfigAAAUsername(ShowRunningConfigAAAUsernameSchema):
    """Parser for :
        * 'show running-config aaa username'
    """

    cli_command = 'show running-config aaa username'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # username testuser password 0 lab
        p1 = re.compile(r'^username +(?P<username>\S+) +password +(?P<type>\d) +(?P<password>.*)$')

        # username testuser common-criteria-policy Test-CC password 0 password
        p2 = re.compile(
            r'^username +(?P<username>\S+) +common-criteria-policy +(?P<common_criteria_policy>.*) '
            r'+password +(?P<type>\d) +(?P<password>.*)$')

        # username testuser secret 9 $9$A2OfV.30kNlIhE$ZEJQIT6aUj.TfCzqGQr.h4AmjQd/bWikQaGRlaLv0nQ
        p3 = re.compile(r'^username +(?P<username>\S+) +secret +(?P<type>\d) +(?P<secret>.*)$')

        # username testuser one-time secret 9 $9$AuJ8xgW8aBBuF.$HyAzLk.3ILFsKrEvd4YjaAHbtonVMLikXw2pnrlkYJY
        p4 = re.compile(
            r'^username +(?P<username>\S+) +one-time +(?P<Onetime>)\s*secret +(?P<type>\d+) +(?P<secret>.*)$')

        # username testuser privilege 15 password 0 lab
        p5 = re.compile(
            r'^username +(?P<username>\S+) +privilege +(?P<privilege>\d+) +password +(?P<type>\d) +(?P<password>.*)$')

        # username testuser common-criteria-policy Test-CC secret 9 $9$7K9qbCZMJa2Vuk$6bS3.Bv7AkBXhTHpTH9V9fhMnJCQe1a9O7xBWHtOKo.
        p6 = re.compile(
            r'^username +(?P<username>\S+) +common-criteria-policy +(?P<common_criteria_policy>.*) '
            r'+secret +(?P<type>\d) +(?P<secret>.*)$')

        # username testuser one-time password 0 password
        p7 = re.compile(
            r'^username +(?P<username>\S+) +one-time +(?P<Onetime>)\s*password +(?P<type>\d) +(?P<password>.*)$')

        # Initial return dictionary
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # username testuser password 0 lab
            m = p1.match(line)
            if m:
                group = m.groupdict()
                username = group['username']
                users_dict = ret_dict.setdefault('username', {}).setdefault(username, {})
                pass_dict = users_dict.setdefault('password', {})
                pass_dict['type'] = int(group['type'])
                pass_dict['password'] = group['password']
                continue

            # username testuser common-criteria-policy Test-CC password 0 password
            m = p2.match(line)
            if m:
                group = m.groupdict()
                username = group['username']
                users_dict = ret_dict.setdefault('username', {}).setdefault(username, {})
                users_dict['common_criteria_policy'] = group['common_criteria_policy']
                pass_dict = users_dict.setdefault('password', {})
                pass_dict['type'] = int(group['type'])
                pass_dict['password'] = group['password']
                continue

            # username testuser secret 9 $9$A2OfV.30kNlIhE$ZEJQIT6aUj.TfCzqGQr.h4AmjQd/bWikQaGRlaLv0nQ
            m = p3.match(line)
            if m:
                group = m.groupdict()
                username = group['username']
                users_dict = ret_dict.setdefault('username', {}).setdefault(username, {})
                secret_dict = users_dict.setdefault('secret', {})
                secret_dict['type'] = int(group['type'])
                secret_dict['secret'] = group['secret']
                continue

            # username testuser one-time secret 9 $9$AuJ8xgW8aBBuF.$HyAzLk.3ILFsKrEvd4YjaAHbtonVMLikXw2pnrlkYJY
            m = p4.match(line)
            if m:
                group = m.groupdict()
                username = group['username']
                users_dict = ret_dict.setdefault('username', {}).setdefault(username, {})
                users_dict['onetime'] = True
                secret_dict = users_dict.setdefault('secret', {})
                secret_dict['type'] = int(group['type'])
                secret_dict['secret'] = group['secret']
                continue

            # username testuser privilege 15 password 0 lab
            m = p5.match(line)
            if m:
                group = m.groupdict()
                username = group['username']
                users_dict = ret_dict.setdefault('username', {}).setdefault(username, {})
                users_dict['privilege'] = int(group['privilege'])
                pass_dict = users_dict.setdefault('password', {})
                pass_dict['type'] = int(group['type'])
                pass_dict['password'] = group['password']
                continue

            # username testuser common-criteria-policy Test-CC secret 9 $9$7K9qbCZMJa2Vuk$6bS3.Bv7AkBXhTHpTH9V9fhMnJCQe1a9O7xBWHtOKo.
            m = p6.match(line)
            if m:
                group = m.groupdict()
                username = group['username']
                users_dict = ret_dict.setdefault('username', {}).setdefault(username, {})
                users_dict['common_criteria_policy'] = group['common_criteria_policy']
                secret_dict = users_dict.setdefault('secret', {})
                secret_dict['type'] = int(group['type'])
                secret_dict['secret'] = group['secret']
                continue

            # username testuser one-time password 0 password
            m = p7.match(line)
            if m:
                group = m.groupdict()
                username = group['username']
                users_dict = ret_dict.setdefault('username', {}).setdefault(username, {})
                users_dict['onetime'] = True
                pass_dict = users_dict.setdefault('password', {})
                pass_dict['type'] = int(group['type'])
                pass_dict['password'] = group['password']
                continue

        return ret_dict


# =================================================
# Schema for:
#   * 'show running-config flow monitor'
# ==================================================

class ShowRunningConfigFlowMonitorSchema(MetaParser):
    schema = {
        'flow_monitor_name': {
            Any(): {
                Optional('exporter_name'): str,
                Optional('cache_timeout_type'): str,
                Optional('cache_timeout_time'): int,
                Optional('record_name'): str
            },
        },
    }

# ===================================
# Parser for:
#   * 'show running-config flow monitor'
# ===================================

class ShowRunningConfigFlowMonitor(ShowRunningConfigFlowMonitorSchema):

    cli_command = 'show running-config flow monitor'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # flow monitor monitor_l2_in
        p1 = re.compile(r'^flow\smonitor\s(?P<flow_monitor_name>\S+)$')

        # exporter StealthWatch_Exporter
        p2 = re.compile(r'^exporter\s(?P<exporter_name>\S+)$')

        # cache timeout active 60
        p3 = re.compile(r'^cache\stimeout\s(?P<cache_timeout_type>\S+)\s(?P<cache_timeout_time>\d+)$')

        # record record_l2_in
        p4 = re.compile(r'^record\s(?P<record_name>\S+)$')

        for line in out.splitlines():

            line = line.strip()

            # flow monitor monitor_l2_in
            m = p1.match(line)
            if m:
                group = m.groupdict()
                flow_monitor_name = group['flow_monitor_name']
                flow_dict = ret_dict.setdefault('flow_monitor_name', {}).setdefault(flow_monitor_name, {})
                continue

            # exporter StealthWatch_Exporter
            m = p2.match(line)
            if m:
                group = m.groupdict()
                flow_dict['exporter_name'] = group['exporter_name']
                continue

            # cache timeout active 60
            m = p3.match(line)
            if m:
                group = m.groupdict()
                flow_dict['cache_timeout_type'] = group['cache_timeout_type']
                flow_dict['cache_timeout_time'] = int(group['cache_timeout_time'])
                continue

            # record record_l2_in
            m = p4.match(line)
            if m:
                group = m.groupdict()
                flow_dict['record_name'] = group['record_name']
                continue

        return ret_dict


